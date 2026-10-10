#!/usr/bin/env python3
"""Ghép kết quả soạn tay (sources/batches/work/out/chunk-NNN.jsonl) với bộ khung (work/in/chunk-NNN.csv).

    python scripts/import/merge_chunks.py --check 001 002     # chỉ kiểm tra các chunk đó
    python scripts/import/merge_chunks.py                      # kiểm tra tất cả + ghi sources/batches/002-tsl-ngsl-drafts.yaml

Mỗi dòng JSONL (một từ, đúng thứ tự file in):
  {"lemma": "...", "pos": ["noun"], "topic": "<slug trong data/topics.yaml>",
   "vi": "nghĩa chính (tiếng Việt, đủ dấu)", "en": "câu ví dụ tự viết", "en_vi": "dịch tiếng Việt",
   "uncertain": false, "why": "chỉ khi uncertain=true: vì sao chưa chắc"}
Mục uncertain=true hoặc có nhiều cách đọc (CMUdict) → vẫn ai_draft nhưng reason bắt đầu bằng [CẦN KIỂM TRA]. KHÔNG mục nào được hiện trên web.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "sources" / "batches" / "work"
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

POS_OK = {"noun", "verb", "adjective", "adverb", "preposition", "conjunction", "pronoun", "determiner",
          "interjection", "number", "modal", "particle", "article"}


def load_chunk(n: str, topics: set[str]):
    errs, entries = [], []
    inp = list(csv.DictReader((WORK / "in" / f"chunk-{n}.csv").open(encoding="utf-8", newline="")))
    outp = WORK / "out" / f"chunk-{n}.jsonl"
    if not outp.exists():
        return [f"chunk-{n}: thiếu file out"], []
    lines = [ln for ln in outp.read_text(encoding="utf-8-sig").splitlines() if ln.strip()]
    if len(lines) != len(inp):
        errs.append(f"chunk-{n}: {len(lines)} dòng out ≠ {len(inp)} từ in")
    for i, ln in enumerate(lines):
        try:
            o = json.loads(ln)
        except json.JSONDecodeError as ex:
            errs.append(f"chunk-{n} dòng {i + 1}: JSON lỗi: {ex}")
            continue
        if i >= len(inp):
            break
        row = inp[i]
        tag = f"chunk-{n} dòng {i + 1} ({row['lemma']})"
        if o.get("lemma", "").lower() != row["lemma"]:
            errs.append(f"{tag}: lemma không khớp ({o.get('lemma')!r}) — phải đúng thứ tự file in")
            continue
        pos = o.get("pos")
        if not isinstance(pos, list) or not pos or any(p not in POS_OK for p in pos):
            errs.append(f"{tag}: pos không hợp lệ {pos!r} (cho phép: {sorted(POS_OK)})")
        if o.get("topic") not in topics:
            errs.append(f"{tag}: topic không hợp lệ {o.get('topic')!r}")
        for k in ("vi", "en", "en_vi"):
            if not isinstance(o.get(k), str) or not o[k].strip():
                errs.append(f"{tag}: thiếu {k}")
        if o.get("uncertain") and not o.get("why"):
            errs.append(f"{tag}: uncertain=true nhưng thiếu why")
        entries.append((row, o))
    return errs, entries


def main() -> int:
    args = sys.argv[1:]
    check_only = args and args[0] == "--check"
    topics = set(yaml.safe_load((ROOT / "data" / "topics.yaml").read_text(encoding="utf-8"))["topics"])
    names = sorted(p.stem.split("-")[1] for p in (WORK / "in").glob("chunk-*.csv"))
    if check_only:
        names = [n.zfill(3) for n in args[1:]]
    all_errs, all_entries = [], []
    for n in names:
        e, ent = load_chunk(n, topics)
        all_errs += e
        all_entries += ent
    if all_errs:
        print(f"[LỖI] {len(all_errs)} vấn đề:")
        for m in all_errs[:80]:
            print("  -", m)
        return 1
    print(f"OK: {len(all_entries)} mục hợp lệ trong {len(names)} chunk")
    if check_only:
        return 0
    multi: dict[str, list[str]] = {}
    try:
        import cmudict
        sys.path.insert(0, str(Path(__file__).parent))
        from make_chunks import arpa_to_ipa
        cd = cmudict.dict()
        for r_, _o in all_entries:
            ipas = []
            for ph in cd.get(r_["lemma"], []):
                v = arpa_to_ipa(ph)
                if v and v not in ipas:
                    ipas.append(v)
            if len(ipas) > 1:
                multi[r_["lemma"]] = ipas
    except ImportError:
        pass
    batch = {"batch": {"id": "002-tsl-ngsl-drafts", "topic": "general-business", "band": "core",
                       "author": "antigravity-ai", "created_at": "2026-10-11"}, "entries": []}
    for row, o in all_entries:
        ent = {
            "lemma": row["lemma"],
            "pos": o["pos"],
            "ipa": {"us": row["ipa"]},
            "level": {"band": row["band"], "basis": [row["list"]]},
            "topics": [o["topic"]],
            "senses": [{"meaning_vi": o["vi"].strip()}],
            "examples": [{"en": o["en"].strip(), "vi": o["en_vi"].strip()}],
        }
        slug = re.sub(r"[^a-z0-9]+", "-", row["lemma"].lower()).strip("-")
        exist = ROOT / "data" / "lexicon" / slug[0] / f"{slug}.yaml"
        if exist.exists() and yaml.safe_load(exist.read_text(encoding="utf-8"))["lemma"].lower() != row["lemma"]:
            ent["id"] = f"{slug}-{o['pos'][0]}"  # tránh trùng id với mục khác lemma (vd: résumé ↔ resume)
        why = (f"Mục từ {row['list'].upper()} hạng {row['rank']}. IPA lấy từ CMUdict (đổi sang IPA bằng quy tắc, vị trí dấu trọng âm theo heuristic); "
               "band TẠM theo hạng tần suất (ADR-005 chưa chốt); nghĩa, từ loại, chủ đề, câu ví dụ do AI viết, chưa duyệt.")
        # Lô hàng loạt LUÔN là ai_draft: mục needs_review vẫn có trang công khai (xem methodology), bản nháp thì không.
        # Điểm cần chú ý được ghi ở đầu `reason` (tiền tố [CẦN KIỂM TRA]) để reviewer lọc.
        if o.get("uncertain"):
            ent["review"] = {"status": "ai_draft", "reason": "[CẦN KIỂM TRA] " + o["why"].strip() + " — " + why}
        elif row["lemma"] in multi:
            alt = "; ".join(multi[row["lemma"]])
            ent["review"] = {"status": "ai_draft",
                             "reason": f"[CẦN KIỂM TRA] CMUdict có nhiều cách đọc ({alt}); IPA đang ghi là cách đầu tiên, cần kiểm tra có khớp nghĩa đã chọn không. — " + why}
        else:
            ent["review"] = {"status": "ai_draft", "reason": why}
        batch["entries"].append(ent)
    dest = ROOT / "sources" / "batches" / "002-tsl-ngsl-drafts.yaml"
    dest.write_text("# Sinh tự động bởi scripts/import/merge_chunks.py — KHÔNG sửa tay; sửa chunk rồi chạy lại.\n"
                    "# Dữ liệu phái sinh từ TSL/NGSL (CC BY-SA 4.0, ghi công: sources/wordlists/ATTRIBUTION.txt).\n"
                    + yaml.safe_dump(batch, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    print(f"ghi {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
