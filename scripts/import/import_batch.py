#!/usr/bin/env python3
"""Nhập một lô từ vựng (sources/batches/*.yaml) → data/lexicon/<chữ>/<id>.yaml (schema v3).

- KHÔNG ghi đè mục đã có (trừ khi --force). KHÔNG tự nâng trạng thái duyệt: mục mới = ai_draft.
- Mỗi mục được kiểm tra bằng schemas/word.v3.json trước khi ghi; có lỗi thì không ghi gì cả.
- `--out` cho phép ghi ra thư mục khác (dùng để chạy thử, không đụng data/lexicon).

Chạy:  python scripts/import/import_batch.py <batch.yaml> [--dry-run] [--force] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[2]
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def slugify(lemma: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", lemma.lower()).strip("-")
    if not s:
        raise ValueError(f"Không tạo được id từ lemma {lemma!r}")
    return s


def build_entry(raw: dict, meta: dict, topics: dict, bands: dict, sources: dict) -> dict:
    e = dict(raw)
    e.setdefault("schema_version", 3)
    e["id"] = e.get("id") or slugify(e["lemma"])

    band = (e.get("level") or {}).get("band") or meta.get("band")
    if band not in bands:
        raise ValueError(f"{e['id']}: band không hợp lệ: {band!r}")
    level = dict(e.get("level") or {})
    level["band"] = band
    level.setdefault("cefr", bands[band]["cefr"])
    level.setdefault("basis", ["editorial"])
    e["level"] = level

    e.setdefault("topics", [meta["topic"]] if meta.get("topic") else [])
    for t in e["topics"]:
        if t not in topics:
            raise ValueError(f"{e['id']}: topic không có trong data/topics.yaml: {t!r}")

    created = str(meta.get("created_at") or date.today())
    senses = []
    for i, s in enumerate(e.get("senses") or [], 1):
        s = dict(s)
        s.setdefault("id", f"{e['id']}-{i}")
        senses.append(s)
    e["senses"] = senses

    colls = []
    for c in e.get("collocations") or []:
        c = dict(c)
        ev = c.get("evidence")
        if not ev:
            # Mặc định trung thực: chưa kiểm tra → unverified (V11 sẽ cảnh báo cho tới khi có bằng chứng).
            c["evidence"] = {"source": "unverified", "checked_at": created, "note": "mục mới từ lô nhập, chưa kiểm tra"}
        elif ev.get("source") not in sources:
            raise ValueError(f"{e['id']}: evidence.source không có trong data/sources.yaml: {ev.get('source')!r}")
        colls.append(c)
    if colls:
        e["collocations"] = colls

    # Trạng thái duyệt: luôn bắt đầu ở ai_draft trừ khi lô chủ động ghi needs_review.
    rv = dict(e.get("review") or {})
    if rv.get("status") not in (None, "ai_draft", "needs_review"):
        raise ValueError(f"{e['id']}: lô nhập không được tự đặt status={rv.get('status')!r}; chỉ ai_draft/needs_review")
    rv.setdefault("status", "ai_draft")
    rv.setdefault("checked_at", str(meta.get("created_at") or date.today()))
    if meta.get("author"):
        rv.setdefault("reason", f"Mục mới từ lô {meta.get('id')} ({meta['author']}); chưa đối chiếu độc lập.")
    e["review"] = rv
    return e


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "data" / "lexicon"))
    args = ap.parse_args()

    batch = yaml.safe_load(Path(args.batch).read_text(encoding="utf-8"))
    meta = batch.get("batch") or {}
    topics = yaml.safe_load((ROOT / "data" / "topics.yaml").read_text(encoding="utf-8"))["topics"]
    bands = yaml.safe_load((ROOT / "data" / "levels.yaml").read_text(encoding="utf-8"))["bands"]
    sources = yaml.safe_load((ROOT / "data" / "sources.yaml").read_text(encoding="utf-8"))["sources"]
    validator = Draft7Validator(json.loads((ROOT / "schemas" / "word.v3.json").read_text(encoding="utf-8")))

    out_root = Path(args.out)
    planned, errors, seen = [], [], set()
    for raw in batch.get("entries") or []:
        try:
            e = build_entry(raw, meta, topics, bands, sources)
        except (ValueError, KeyError) as ex:
            errors.append(str(ex))
            continue
        for err in validator.iter_errors(e):
            errors.append(f"{e['id']}: schema: {'/'.join(map(str, err.path)) or '(gốc)'}: {err.message}")
        if e["id"] in seen:
            errors.append(f"{e['id']}: trùng id trong lô")
        seen.add(e["id"])
        dest = out_root / e["id"][0] / f"{e['id']}.yaml"
        if dest.exists() and not args.force:
            errors.append(f"{e['id']}: đã tồn tại ({dest}); dùng --force nếu thật sự muốn ghi đè")
        planned.append((dest, e))

    if errors:
        print(f"[LỖI] {len(errors)} vấn đề — không ghi gì:")
        for m in errors:
            print("  -", m)
        return 1

    for dest, e in planned:
        print(("[dry-run] " if args.dry_run else "ghi ") + str(dest))
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            order = ["schema_version", "id", "lemma", "pos", "ipa", "level", "topics", "senses", "collocations",
                     "synonyms", "confused_words", "confusing_meanings", "examples", "pronunciation_tips_vi", "review"]
            ordered = {k: e[k] for k in order if k in e}
            ordered.update({k: v for k, v in e.items() if k not in ordered})
            dest.write_text(yaml.safe_dump(ordered, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8", newline="\n")
    print(f"Xong: {len(planned)} mục{' (dry-run)' if args.dry_run else ''}. Nhớ chạy scripts/validate/validate.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
