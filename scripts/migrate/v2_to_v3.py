#!/usr/bin/env python3
"""
Migrate dữ liệu v2 -> v3 (PLAN_NEN_MONG T2.2, T2.8). Idempotent: chạy lại nhiều lần cho kết quả giống nhau.

- Lexicon: bỏ `speaking_use`; ánh xạ `topics` theo data/topics.yaml; `level.basis` -> danh sách mã nguồn;
  `collocations[].evidence` (chuỗi) -> object {source, checked_at}; chuẩn hóa mã nguồn trong `review`.
  KHÔNG tự sinh synset, KHÔNG tự đổi band/cefr (chưa có cơ sở độc lập — xem ADR-005).
- Quotes: tách data/quotes.yaml thành data/quotes/<id>.yaml (schema quote.v1).
- Sets: tinh gọn front matter về schema set.v3.

Dùng:
    python scripts/migrate/v2_to_v3.py --dry-run
    python scripts/migrate/v2_to_v3.py --apply
"""
import argparse
import glob
import json
import os
import re
import sys

import yaml

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TODAY = "2026-10-10"

SOURCE_ALIASES = {
    "vocabulary.md": "vocabulary-md",
    "synonyms.md": "synonyms-md",
    "Oxford Learner's Dictionary": "oxford-ref",
    "Oxford Learner's Dictionaries": "oxford-ref",
}

WORD_KEY_ORDER = [
    "schema_version", "id", "lemma", "pos", "ipa", "audio", "level", "topics", "senses",
    "collocations", "synsets", "synonyms", "confused_words", "confusing_meanings",
    "examples", "pronunciation_tips_vi", "review",
]


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def dump_yaml(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)


def norm_source(s):
    return SOURCE_ALIASES.get(s, s)


def migrate_word(d, legacy_map, report):
    if d.get("schema_version") == 3:
        return d, False
    wid = d["id"]
    out = dict(d)
    out["schema_version"] = 3
    out.pop("speaking_use", None)

    # topics
    new_topics, dropped = [], []
    for t in d.get("topics") or []:
        if t not in legacy_map:
            report["unknown_topics"].append((wid, t))
            continue
        m = legacy_map[t]
        if m is None:
            dropped.append(t)
        elif m not in new_topics:
            new_topics.append(m)
    if len(new_topics) > 3:
        report["topics_truncated"].append((wid, list(new_topics)))
        new_topics = new_topics[:3]
    if not new_topics:
        report["no_topic_after_map"].append((wid, d.get("topics")))
    out["topics"] = new_topics

    # level
    lv = dict(d.get("level") or {})
    old_basis = lv.get("basis")
    report["old_basis"][str(old_basis)] = report["old_basis"].get(str(old_basis), 0) + 1
    lv["basis"] = ["editorial"]
    out["level"] = {k: lv[k] for k in ("band", "cefr", "basis") if k in lv}

    # review
    rv = dict(d.get("review") or {})
    checked_at = str(rv.get("checked_at") or TODAY)
    rv["checked_at"] = checked_at
    if rv.get("sources"):
        rv["sources"] = [norm_source(s) for s in rv["sources"]]
    if rv.get("checked_by"):
        rv["checked_by"] = [norm_source(s) for s in rv["checked_by"]]
    out["review"] = rv

    # collocations
    cols = []
    for c in d.get("collocations") or []:
        c = dict(c)
        ev = c.get("evidence")
        if not isinstance(ev, dict):
            c["evidence"] = {
                "source": "unverified",
                "checked_at": checked_at,
                "note": "legacy: ghi 'corpus' chung chung, chưa có bằng chứng cụ thể",
            }
        cols.append(c)
    if cols:
        out["collocations"] = cols

    ordered = {k: out[k] for k in WORD_KEY_ORDER if k in out}
    for k in out:  # giữ trường lạ để validator báo lỗi thay vì âm thầm xóa
        if k not in ordered:
            ordered[k] = out[k]
    return ordered, True


def migrate_lexicon(apply, report):
    topics_cfg = load_yaml(os.path.join(BASE, "data", "topics.yaml"))
    legacy_map = topics_cfg["legacy_map"]
    n_changed = 0
    for path in sorted(glob.glob(os.path.join(BASE, "data", "lexicon", "**", "*.yaml"), recursive=True)):
        d = load_yaml(path)
        new, changed = migrate_word(d, legacy_map, report)
        if changed:
            n_changed += 1
            if apply:
                dump_yaml(path, new)
    report["lexicon_changed"] = n_changed


def band_of(word_id, lex_bands):
    return lex_bands.get(word_id)


def migrate_quotes(apply, report):
    legacy = os.path.join(BASE, "data", "quotes.yaml")
    if not os.path.exists(legacy):
        report["quotes_changed"] = 0
        return
    data = load_yaml(legacy)
    lex = {}
    for p in glob.glob(os.path.join(BASE, "data", "lexicon", "**", "*.yaml"), recursive=True):
        w = load_yaml(p)
        lex[w["id"]] = w.get("level", {}).get("band")
    order = ["foundation", "core", "target", "advanced"]
    cat_map = {  # CẦN DUYỆT: ánh xạ category tự do cũ sang chủ đề chuẩn
        "workplace": "offices", "customer-service": "general-business",
        "mindset": "offices", "leadership": "offices",
    }
    n = 0
    for law in data.get("laws", []):
        hl, bands = [], []
        for c in law.get("collocations", []):
            item = {"phrase": c["term"], "meaning_vi": c["meaning"]}
            m = re.match(r"^/words/([a-z0-9-]+)/$", c.get("link", ""))
            if m and m.group(1) in lex:
                item["word"] = m.group(1)
                if lex[m.group(1)]:
                    bands.append(lex[m.group(1)])
            else:
                report["quote_highlights_without_word"].append((law["id"], c["term"]))
            hl.append(item)
        band = max(bands, key=order.index) if bands else "core"
        q = {
            "schema_version": 1,
            "id": law["id"],
            "title_vi": law["name_vi"],
            "title_en": law["name_en"],
            "topic": cat_map.get(law.get("category"), "offices"),
            "band": band,
            "quote_en": law["quote_en"],
            "quote_vi": law["quote_vi"],
            "highlights": hl,
            "origin": "original",
            "review": {
                "status": "ai_draft",
                "checked_by": ["glory-editorial"],
                "checked_at": TODAY,
                "reason": "Câu cũ chưa có bản ghi kiểm duyệt trước khi migrate; chưa đối chiếu độc lập.",
            },
        }
        n += 1
        if apply:
            dump_yaml(os.path.join(BASE, "data", "quotes", law["id"] + ".yaml"), q)
    report["quotes_changed"] = n
    if apply:
        os.remove(legacy)


def migrate_sets(apply, report):
    n = 0
    for path in sorted(glob.glob(os.path.join(BASE, "content", "sets", "set-*.md"))):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        parts = text.split("---", 2)
        fm = yaml.safe_load(parts[1])
        if fm.get("schema_version") == 3:
            continue
        keep = {"schema_version": 3, "title": fm["title"], "date": str(fm.get("date")), "draft": fm.get("draft", False),
                "summary": fm.get("summary", ""), "topics": [], "tiktok": fm.get("tiktok", ""),
                "aliases": fm.get("aliases", []), "words": fm.get("words", [])}
        topics_cfg = load_yaml(os.path.join(BASE, "data", "topics.yaml"))["legacy_map"]
        for t in fm.get("topics", []):
            m = topics_cfg.get(t)
            if m and m not in keep["topics"]:
                keep["topics"].append(m)
        body = ""
        n += 1
        if apply:
            fm_text = yaml.safe_dump(keep, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write("---\n" + fm_text + "---\n\n" + body)
    report["sets_changed"] = n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-sets", action="store_true", help="Không động vào content/sets/")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run
    report = {
        "unknown_topics": [], "topics_truncated": [], "no_topic_after_map": [],
        "old_basis": {}, "quote_highlights_without_word": [],
    }
    migrate_lexicon(apply, report)
    migrate_quotes(apply, report)
    if not args.skip_sets:
        migrate_sets(apply, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print("[APPLIED]" if apply else "[DRY-RUN] không ghi gì cả.")


if __name__ == "__main__":
    main()
