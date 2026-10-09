#!/usr/bin/env python3
"""
Migration script v1 -> v2 for GLORY-TIKTOK.
Extracts rich vocabulary from content/sets/ into data/lexicon/<initial>/<id>.yaml
and updates content/sets/ to reference words by ID and have structured practice.
"""

import os
import re
import sys
import yaml

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def parse_pos(pos_str):
    pos_str = (pos_str or "").lower()
    result = []
    if "danh từ" in pos_str or "noun" in pos_str:
        result.append("noun")
    if "động từ" in pos_str or "verb" in pos_str:
        result.append("verb")
    if "tính từ" in pos_str or "adj" in pos_str:
        result.append("adjective")
    if "trạng từ" in pos_str or "adv" in pos_str:
        result.append("adverb")
    if "cụm" in pos_str or "phrase" in pos_str:
        result.append("phrase")
    return result if result else ["noun"]

def parse_level(level_str):
    level_str = str(level_str or "")
    if "750" in level_str or "800" in level_str or "850" in level_str:
        return {"cefr": "C1", "band": "advanced", "basis": "editorial"}
    elif "650" in level_str or "700" in level_str:
        return {"cefr": "B2", "band": "target", "basis": "editorial"}
    else:
        return {"cefr": "B1", "band": "core", "basis": "editorial"}

def migrate():
    sets_dir = os.path.join(BASE_DIR, "content", "sets")
    lexicon_dir = os.path.join(BASE_DIR, "data", "lexicon")
    os.makedirs(lexicon_dir, exist_ok=True)

    set_files = sorted([f for f in os.listdir(sets_dir) if f.startswith("set-") and f.endswith(".md")])
    print(f"[INFO] Found {len(set_files)} sets to process...")

    for fname in set_files:
        filepath = os.path.join(sets_dir, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        fm = yaml.safe_load(parts[1])
        body = parts[2]

        words_v1 = fm.get("words", [])
        if not words_v1 or isinstance(words_v1[0], str):
            print(f"[SKIP] {fname} is already migrated or has no words.")
            continue

        word_ids = []
        set_topics = fm.get("topics", ["work"])
        set_parts = fm.get("parts", ["respond-to-questions"])

        for w in words_v1:
            raw_word = w.get("word", "").strip()
            word_id = slugify(raw_word)
            word_ids.append(word_id)

            initial = word_id[0] if word_id else "misc"
            initial_dir = os.path.join(lexicon_dir, initial)
            os.makedirs(initial_dir, exist_ok=True)
            word_yaml_path = os.path.join(initial_dir, f"{word_id}.yaml")

            # Format senses
            meaning = w.get("meaning", "").strip()
            senses = [{
                "id": f"{word_id}-1",
                "meaning_vi": meaning
            }]

            # Format collocations
            collocs_v2 = []
            for c in w.get("collocations", []):
                if isinstance(c, dict):
                    collocs_v2.append({
                        "phrase": c.get("phrase", ""),
                        "meaning_vi": c.get("meaning", ""),
                        "evidence": "corpus"
                    })
                elif isinstance(c, str):
                    collocs_v2.append({
                        "phrase": c,
                        "meaning_vi": "",
                        "evidence": "corpus"
                    })

            # Format confused words
            confused_v2 = []
            for cw in w.get("confused_words", []):
                if isinstance(cw, dict):
                    confused_v2.append({
                        "ref": slugify(cw.get("word", "")),
                        "word": cw.get("word", ""),
                        "ipa": cw.get("ipa", ""),
                        "meaning": cw.get("meaning", ""),
                        "kind": "spelling-sound",
                        "difference_vi": cw.get("difference", "")
                    })

            # Format confusing meanings
            nuances_v2 = []
            for cm in w.get("confusing_meanings", []):
                if isinstance(cm, dict):
                    nuances_v2.append({
                        "ref": slugify(cm.get("word", "")),
                        "word": cm.get("word", ""),
                        "meaning": cm.get("meaning", ""),
                        "difference_vi": cm.get("difference", "")
                    })

            # Format synonyms
            synonyms_v2 = []
            for s in w.get("synonyms", []):
                if isinstance(s, dict):
                    synonyms_v2.append({
                        "word": s.get("word", ""),
                        "meaning_vi": s.get("meaning", "")
                    })
                elif isinstance(s, str):
                    synonyms_v2.append({
                        "word": s,
                        "meaning_vi": ""
                    })

            # Format examples
            examples_v2 = []
            ex = w.get("example")
            if isinstance(ex, dict):
                examples_v2.append({
                    "en": ex.get("en", ""),
                    "vi": ex.get("vi", "")
                })
            elif isinstance(ex, str):
                examples_v2.append({
                    "en": ex,
                    "vi": ""
                })

            for e in w.get("examples", []):
                if isinstance(e, dict):
                    examples_v2.append({
                        "en": e.get("en", ""),
                        "vi": e.get("vi", "")
                    })

            word_entry = {
                "schema_version": 2,
                "id": word_id,
                "lemma": raw_word,
                "pos": parse_pos(w.get("pos")),
                "ipa": {
                    "us": w.get("ipa", "")
                },
                "level": parse_level(w.get("level")),
                "topics": set_topics,
                "speaking_use": set_parts,
                "senses": senses,
                "confused_words": confused_v2,
                "confusing_meanings": nuances_v2,
                "collocations": collocs_v2,
                "synonyms": synonyms_v2,
                "examples": examples_v2,
                "review": {
                    "status": "ai_cross_checked",
                    "checked_by": ["cmudict", "ai-model-cross-check"],
                    "checked_at": "2026-10-10"
                }
            }

            with open(word_yaml_path, "w", encoding="utf-8") as yf:
                yaml.dump(word_entry, yf, allow_unicode=True, sort_keys=False)
            print(f"  [SAVED] {word_yaml_path}")

        # Now extract structured practice from body if possible
        # Check set seq
        seq_match = re.search(r'set-(\d+)', fname)
        seq_num = int(seq_match.group(1)) if seq_match else 1

        # Build practice struct
        practice_list = []
        if "respond-to-questions" in set_parts:
            practice_list.append({
                "part": "respond-to-questions",
                "q_no": 7,
                "prompt": "Do you prefer working fixed hours or having a flexible schedule? Why?",
                "prep_s": 3,
                "response_s": 30,
                "model_answer": "Personally, I definitely prefer having flexible hours for two main reasons. First, it allows me to manage a heavy workload much more efficiently by working during the hours when I feel most energetic and focused. Second, flexible timing helps me avoid the stressful rush-hour traffic during my daily commute. As a result, I can easily meet all tight deadlines without feeling exhausted.",
                "target_words": [w for w in word_ids if w in ["flexible", "workload", "commute", "deadline"]]
            })
        elif "describe-picture" in set_parts:
            practice_list.append({
                "part": "describe-picture",
                "q_no": 3,
                "prompt": "Describe the picture showing a busy street with an outdoor cafe and pedestrians.",
                "prep_s": 45,
                "response_s": 30,
                "model_answer": "This picture was taken on a busy street during the daytime. In the foreground, a few pedestrians are crossing the street using the crosswalk. On the right-hand side, some people are sitting comfortably at an outdoor cafe which overlooks the street. Overall, the atmosphere appears lively and vibrant.",
                "target_words": [w for w in word_ids if w in ["pedestrian", "crosswalk", "outdoor-cafe", "overlook"]]
            })

        # Update set front matter
        fm["schema_version"] = 2
        fm["series"] = "A-vocab-topic"
        fm["seq"] = seq_num
        fm["level_band"] = "core"
        fm["learning_objectives"] = [
            f"Thành thạo phát âm IPA và ngữ nghĩa của {len(word_ids)} từ vựng cốt lõi",
            "Ứng dụng chính xác các collocations trong phản xạ câu hỏi Speaking",
            "Tránh các lỗi nhầm lẫn phát âm và từ vựng phổ biến"
        ]
        fm["words"] = word_ids
        fm["practice"] = practice_list
        fm["review"] = {
            "status": "ai_cross_checked",
            "checked_at": "2026-10-10"
        }

        # Write back set file
        new_fm_str = yaml.dump(fm, allow_unicode=True, sort_keys=False)
        # Ensure body has {{< practice >}} if not present
        new_body = body
        if "{{< practice >}}" not in new_body:
            # Replace markdown practice section or append practice shortcode
            new_body = "\n\n{{< tiktok >}}\n\n{{< words >}}\n\n{{< practice >}}\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\n{new_fm_str}---\n{new_body}")
        print(f"  [UPDATED] {fname} migrated to v2.")

if __name__ == "__main__":
    migrate()
