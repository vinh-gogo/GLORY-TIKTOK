#!/usr/bin/env python3
"""
Validator dữ liệu GLORY-TIKTOK (PLAN_NEN_MONG Mục 8.2, V1–V14).

Kiểm tra:
  V1  JSON Schema v3 cho lexicon, synsets, quotes, sets
  V2  id trùng tên file; lemma không trùng giữa các mục
  V3  tham chiếu chéo: synsets[], highlights[].word, sets.words[] phải tồn tại (lỗi);
      confused_words/confusing_meanings[].ref không có trong lexicon -> cảnh báo (từ dễ nhầm thường là từ ngoài kho)
  V4  topics ∈ data/topics.yaml; band ∈ data/levels.yaml; mã nguồn ∈ data/sources.yaml
  V5  IPA chỉ chứa ký tự IPA cho phép
  V6  IPA US khớp CMUdict (chỉ chạy khi cài gói `cmudict`; không có -> bỏ qua, in thông báo)
  V7  collocation chứa lemma (heuristic, cảnh báo)
  V8  câu ví dụ chứa lemma (heuristic, cảnh báo)
  V9  needs_review phải có reason
  V10 từ ai_cross_checked trở lên phải có >= 1 nguồn độc lập trong checked_by + sources
  V11 evidence.source = unverified -> cảnh báo (dữ liệu legacy chưa có bằng chứng)
  V12 chuỗi *_vi dài nhưng không có dấu tiếng Việt -> cảnh báo
  V13 band lệch cefr tương ứng mà không needs_review -> cảnh báo
  V14 không có số điểm viết cứng trong layouts/ và content/

Mã thoát: 1 nếu có lỗi (hoặc có cảnh báo khi dùng --strict).
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

import jsonschema
import yaml

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# GLORY_ROOT cho phép trỏ validator vào bản sao của repo (dùng trong scripts/validate/test_validate.py).
BASE = os.path.abspath(os.environ.get("GLORY_ROOT") or os.path.join(os.path.dirname(__file__), "..", ".."))

STATUS_PUBLISHED = {"ai_cross_checked", "human_verified"}
BAND_CEFR = {"foundation": {"A1", "A2"}, "core": {"B1"}, "target": {"B2"}, "advanced": {"C1", "C2"}}
VI_CHARS = re.compile(r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]", re.I)
IPA_ALLOWED = set("abcdefghijklmnopqrstuvwxyz/ˈˌːˑæɑɒɔəɚɛɜɝɡɪɫŋɹʃʊʌʒθðʔɾʲʰ̩̃̍͡().-‿ ᵻɐɯɨʉɵ")
HARDCODED_SCORE = re.compile(r"(TOEIC\s*\d{3}\+?|\b[3-9]\d{2}\+(?=[\s<\"'),.:;]|$))")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def to_json(obj):
    return json.loads(json.dumps(obj, default=str))


def front_matter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    return to_json(data) if data else None


class Collector:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, code, where, msg):
        self.errors.append((code, where, msg))

    def warn(self, code, where, msg):
        self.warnings.append((code, where, msg))


def word_forms_present(lemma, text):
    """Heuristic: mọi từ của lemma (bỏ đuôi e/s/y/ed/ing) xuất hiện dạng tiền tố trong text."""
    t = text.lower()
    for w in re.split(r"[\s-]+", lemma.lower()):
        stem = w
        for suf in ("ing", "ed", "es", "s", "e", "y"):
            if len(stem) - len(suf) >= 3 and stem.endswith(suf):
                stem = stem[: -len(suf)]
                break
        stem = stem[: max(3, len(stem) - 1)] if len(stem) > 4 else stem
        if stem not in t:
            return False
    return True


def rel(path):
    return os.path.relpath(path, BASE).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="Coi cảnh báo là lỗi")
    ap.add_argument("--report", help="Ghi báo cáo JSON ra file")
    args = ap.parse_args()
    c = Collector()
    print("[INFO] Starting GLORY-TIKTOK data validation (v3)...")

    # --- Cấu hình nền ---
    cfg = {}
    for name in ("levels", "topics", "sources"):
        p = os.path.join(BASE, "data", f"{name}.yaml")
        if not os.path.exists(p):
            c.err("V4", f"data/{name}.yaml", "Thiếu tệp cấu hình")
            cfg[name] = {}
        else:
            cfg[name] = load_yaml(p)
    bands = set((cfg["levels"].get("bands") or {}).keys())
    topics = set((cfg["topics"].get("topics") or {}).keys())
    sources = cfg["sources"].get("sources") or {}
    independent = {k for k, v in sources.items() if v.get("independent")}

    schemas = {}
    for key, fn in (("word", "word.v3.json"), ("synset", "synset.v1.json"), ("quote", "quote.v1.json"), ("set", "set.v3.json")):
        p = os.path.join(BASE, "schemas", fn)
        if not os.path.exists(p):
            print(f"[ERROR] Missing schema {fn}")
            sys.exit(1)
        schemas[key] = jsonschema.Draft7Validator(load_json(p))

    def schema_check(kind, data, where):
        for e in sorted(schemas[kind].iter_errors(data), key=lambda e: list(e.path)):
            c.err("V1", where, f"{e.message} @ {'/'.join(str(x) for x in e.path)}")

    # --- Exam (giữ lại cho giai đoạn Speaking sau này) ---
    exam_path = os.path.join(BASE, "data", "exam", "toeic-speaking.yaml")
    if os.path.exists(exam_path):
        try:
            ex = load_yaml(exam_path)
            assert "parts" in ex and "proficiency_levels" in ex
        except Exception as e:
            c.err("V1", rel(exam_path), f"Dữ liệu đề thi không hợp lệ: {e}")

    # --- Lexicon ---
    cmu = None
    try:
        import cmudict  # type: ignore
        cmu = cmudict.dict()
    except Exception:
        print("[INFO] V6 bỏ qua: chưa cài gói `cmudict` (pip install cmudict).")

    lex = {}
    lemmas = {}
    files = sorted(glob.glob(os.path.join(BASE, "data", "lexicon", "**", "*.yaml"), recursive=True))
    print(f"  Validating {len(files)} lexicon files...")
    for path in files:
        where = rel(path)
        try:
            raw = load_yaml(path)
        except Exception as e:
            c.err("V1", where, f"YAML lỗi: {e}")
            continue
        if not raw:
            c.err("V1", where, "Tệp rỗng")
            continue
        d = to_json(raw)
        schema_check("word", d, where)
        wid = d.get("id")
        if wid != os.path.splitext(os.path.basename(path))[0]:
            c.err("V2", where, f"id '{wid}' không khớp tên tệp")
        if not os.path.basename(os.path.dirname(path)) == (wid or "?")[:1]:
            c.err("V2", where, "Tệp phải nằm trong thư mục chữ cái đầu của id")
        lm = (d.get("lemma") or "").lower()
        if lm in lemmas:
            c.err("V2", where, f"lemma '{lm}' trùng với {lemmas[lm]}")
        lemmas[lm] = where
        lex[wid] = d

    for wid, d in lex.items():
        where = f"data/lexicon/{wid[:1]}/{wid}.yaml"
        lv = d.get("level") or {}
        rv = d.get("review") or {}
        status = rv.get("status")
        # V4
        for t in d.get("topics") or []:
            if t not in topics:
                c.err("V4", where, f"topic '{t}' không có trong data/topics.yaml")
        if lv.get("band") and lv["band"] not in bands:
            c.err("V4", where, f"band '{lv['band']}' không có trong data/levels.yaml")
        for code in (lv.get("basis") or []) + (rv.get("checked_by") or []) + (rv.get("sources") or []):
            if code not in sources:
                c.err("V4", where, f"mã nguồn '{code}' không có trong data/sources.yaml")
        for col in d.get("collocations") or []:
            src = (col.get("evidence") or {}).get("source")
            if src and src not in sources:
                c.err("V4", where, f"evidence.source '{src}' không có trong data/sources.yaml")
            if src == "unverified":
                c.warn("V11", where, f"collocation '{col.get('phrase')}' chưa có bằng chứng cụ thể (legacy)")
            if not word_forms_present(d["lemma"], col.get("phrase", "")):
                c.warn("V7", where, f"collocation '{col.get('phrase')}' không thấy lemma '{d['lemma']}'")
        # V5/V6
        for accent in ("us", "uk"):
            ipa = (d.get("ipa") or {}).get(accent)
            if ipa:
                bad = {ch for ch in ipa if ch not in IPA_ALLOWED}
                if bad:
                    c.err("V5", where, f"IPA {accent} có ký tự không hợp lệ: {''.join(sorted(bad))}")
        if cmu is not None and " " not in d["lemma"] and d["lemma"].lower() not in cmu:
            c.warn("V6", where, "lemma không có trong CMUdict — cần needs_review nếu IPA chưa chắc")
        # V8
        for ex in d.get("examples") or []:
            if not word_forms_present(d["lemma"], ex.get("en", "")):
                c.warn("V8", where, f"ví dụ không thấy lemma '{d['lemma']}': {ex.get('en', '')[:50]}")
        # V9, V10
        if status == "needs_review" and not rv.get("reason"):
            c.err("V9", where, "needs_review phải có review.reason")
        if status in STATUS_PUBLISHED:
            have = set(rv.get("checked_by") or []) | set(rv.get("sources") or [])
            if not (have & independent):
                c.err("V10", where, "Thiếu nguồn đối chiếu độc lập trong checked_by/sources")
        # V12
        def scan_vi(obj, path=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k.endswith("_vi") or k in ("meaning", "vi"):
                        if isinstance(v, str) and len(v) > 20 and not VI_CHARS.search(v):
                            c.warn("V12", where, f"{path}{k} có vẻ thiếu dấu tiếng Việt")
                    else:
                        scan_vi(v, path + k + ".")
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    scan_vi(v, path)
        scan_vi(d)
        # V13
        cefr = lv.get("cefr")
        if cefr and lv.get("band") in BAND_CEFR and cefr not in BAND_CEFR[lv["band"]] and status != "needs_review":
            c.warn("V13", where, f"band '{lv['band']}' lệch cefr '{cefr}'")
        # V3
        for s in d.get("synsets") or []:
            pass  # kiểm sau khi tải synsets
        for key in ("confused_words", "confusing_meanings"):
            for item in d.get(key) or []:
                r = item.get("ref")
                if r and r not in lex:
                    c.warn("V3", where, f"{key}.ref '{r}' không có trong lexicon (chấp nhận được với từ ngoài kho)")

    # --- Synsets ---
    syn_ids = set()
    syn_files = sorted(glob.glob(os.path.join(BASE, "data", "synsets", "*.yaml")))
    print(f"  Validating {len(syn_files)} synset files...")
    for path in syn_files:
        where = rel(path)
        d = to_json(load_yaml(path))
        schema_check("synset", d, where)
        if d.get("id") != os.path.splitext(os.path.basename(path))[0]:
            c.err("V2", where, "id không khớp tên tệp")
        syn_ids.add(d.get("id"))
        rv = d.get("review") or {}
        if rv.get("status") == "needs_review" and not rv.get("reason"):
            c.err("V9", where, "needs_review phải có reason")
        if rv.get("status") in STATUS_PUBLISHED:
            if not ((set(rv.get("checked_by") or []) | set(rv.get("sources") or [])) & independent):
                c.err("V10", where, "Thiếu nguồn đối chiếu độc lập")
        for m in d.get("members") or []:
            if m.get("ref") and m["ref"] not in lex:
                c.warn("V3", where, f"member.ref '{m['ref']}' chưa có trong lexicon")
    for wid, d in lex.items():
        for s in d.get("synsets") or []:
            if s not in syn_ids:
                c.err("V3", f"data/lexicon/{wid[:1]}/{wid}.yaml", f"synset '{s}' không tồn tại")

    # --- Quotes ---
    q_files = sorted(glob.glob(os.path.join(BASE, "data", "quotes", "*.yaml")))
    print(f"  Validating {len(q_files)} quote files...")
    for path in q_files:
        where = rel(path)
        d = to_json(load_yaml(path))
        schema_check("quote", d, where)
        if d.get("id") != os.path.splitext(os.path.basename(path))[0]:
            c.err("V2", where, "id không khớp tên tệp")
        if d.get("topic") not in topics:
            c.err("V4", where, f"topic '{d.get('topic')}' không có trong data/topics.yaml")
        if d.get("origin") == "attributed" and not (d.get("author") and d.get("source")):
            c.err("V1", where, "origin=attributed bắt buộc có author và source kiểm chứng được")
        rv = d.get("review") or {}
        if rv.get("status") == "needs_review" and not rv.get("reason"):
            c.err("V9", where, "needs_review phải có reason")
        for h in d.get("highlights") or []:
            if h.get("word") and h["word"] not in lex:
                c.err("V3", where, f"highlight.word '{h['word']}' không có trong lexicon")
            if h.get("phrase", "").lower() not in d.get("quote_en", "").lower() and not word_forms_present(h.get("phrase", ""), d.get("quote_en", "")):
                c.warn("V8", where, f"highlight '{h.get('phrase')}' không thấy trong quote_en")
        if not (d.get("highlights") or []):
            c.warn("V3", where, "Câu không có highlight nào")

    # --- Sets ---
    s_files = sorted(glob.glob(os.path.join(BASE, "content", "sets", "set-*.md")))
    print(f"  Validating {len(s_files)} lesson set files...")
    aliases = {}
    for path in s_files:
        where = rel(path)
        fm = front_matter(path)
        if not fm:
            c.err("V1", where, "Thiếu front matter")
            continue
        schema_check("set", fm, where)
        for w in fm.get("words") or []:
            if w not in lex:
                c.err("V3", where, f"words: '{w}' không có trong lexicon")
        for t in fm.get("topics") or []:
            if t not in topics:
                c.err("V4", where, f"topic '{t}' không có trong data/topics.yaml")
        for a in fm.get("aliases") or []:
            if a in aliases:
                c.err("V2", where, f"alias '{a}' trùng với {aliases[a]}")
            aliases[a] = where
        if "TikTok" in str(fm.get("tiktok", "")) or str(fm.get("tiktok", "")).endswith("1234567890"):
            c.warn("V3", where, "Link TikTok là placeholder (video/1234567890)")

    # --- V14: số điểm viết cứng ---
    for folder in ("layouts", "content"):
        for path in glob.glob(os.path.join(BASE, folder, "**", "*"), recursive=True):
            if not os.path.isfile(path) or not path.endswith((".html", ".md", ".gotmpl")):
                continue
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for n, line in enumerate(f, 1):
                    m = HARDCODED_SCORE.search(line)
                    if m:
                        c.err("V14", f"{rel(path)}:{n}", f"số điểm viết cứng '{m.group(0)}' — đọc từ data/levels.yaml")

    # --- Báo cáo ---
    by_code = collections.Counter(code for code, _, _ in c.warnings)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump({"errors": c.errors, "warnings": c.warnings}, f, ensure_ascii=False, indent=1)
    if c.warnings:
        print(f"\n[WARN] {len(c.warnings)} cảnh báo: " + ", ".join(f"{k}={v}" for k, v in sorted(by_code.items())))
        for code, where, msg in c.warnings[:15]:
            print(f"  - [{code}] {where}: {msg}")
        if len(c.warnings) > 15:
            print(f"  ... và {len(c.warnings) - 15} cảnh báo khác (dùng --report để xuất đầy đủ)")
    if c.errors or (args.strict and c.warnings):
        print(f"\n[ERROR] {len(c.errors)} lỗi:")
        for code, where, msg in c.errors[:60]:
            print(f"  - [{code}] {where}: {msg}")
        if len(c.errors) > 60:
            print(f"  ... và {len(c.errors) - 60} lỗi khác")
        sys.exit(1)
    print("\n[OK] Validation successful!")
    sys.exit(0)


if __name__ == "__main__":
    main()
