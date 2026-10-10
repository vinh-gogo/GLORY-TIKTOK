#!/usr/bin/env python3
"""So sánh `level.band` hiện có với tín hiệu bên ngoài (PLAN_NEN_MONG 6.4). CHỈ BÁO CÁO; ghi dữ liệu khi có --apply.

Đầu vào tùy chọn (chưa có trong repo — phải được tải về & kiểm tra giấy phép trước, xem ADR-006):
    sources/wordlists/cefr.csv   cột: lemma,cefr             (nhãn CEFR của từ — tín hiệu A)
    sources/wordlists/freq.csv   cột: lemma,rank,list        (thứ hạng TSL/BSL/NGSL — tín hiệu B)

Ngưỡng tần suất chưa được quyết (ADR-005). Khai báo trong data/levels.yaml khi đã chốt:
    bands.<band>.freq_rank_max: <số>      # hạng tối đa của band; band cuối có thể để null
Thiếu tín hiệu A hoặc B → mục được liệt kê là "no_signal"; KHÔNG đoán, KHÔNG đổi band.

Quy tắc khi đủ tín hiệu:
    - A và B đồng thuận band      → "agree"
    - Lệch ≥ 1 tầng               → "conflict": theo A, đề xuất review.status=needs_review (chỉ ghi khi --apply)
Báo cáo CSV: docs/band-assignment-report.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def band_from_rank(rank: int, order: list[str], bands: dict) -> str | None:
    for b in order:
        mx = bands[b].get("freq_rank_max")
        if mx is None:
            continue
        if rank <= mx:
            return b
    last = order[-1]
    return last if bands[last].get("freq_rank_max") is None and any(bands[b].get("freq_rank_max") for b in order) else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="đánh dấu needs_review cho mục lệch band (không đổi band)")
    args = ap.parse_args()

    levels = yaml.safe_load((ROOT / "data" / "levels.yaml").read_text(encoding="utf-8"))
    order, bands = levels["band_order"], levels["bands"]
    cefr_to_band = {b["cefr"]: k for k, b in bands.items()}
    cefr = {r["lemma"].lower(): r["cefr"] for r in read_csv(ROOT / "sources" / "wordlists" / "cefr.csv")}
    freq = {r["lemma"].lower(): int(r["rank"]) for r in read_csv(ROOT / "sources" / "wordlists" / "freq.csv")}
    thresholds_set = any(bands[b].get("freq_rank_max") for b in order)

    if not cefr and not freq:
        print("Chưa có sources/wordlists/*.csv → không có tín hiệu ngoài; mọi mục sẽ là no_signal.")
    if freq and not thresholds_set:
        print("Có freq.csv nhưng data/levels.yaml chưa khai báo freq_rank_max (ADR-005) → bỏ qua tín hiệu B.")

    rows, counts = [], {}
    for f in sorted((ROOT / "data" / "lexicon").rglob("*.yaml")):
        w = yaml.safe_load(f.read_text(encoding="utf-8"))
        lemma = w["lemma"].lower()
        cur = w["level"]["band"]
        a = cefr_to_band.get(cefr.get(lemma, ""))
        b = band_from_rank(freq[lemma], order, bands) if (lemma in freq and thresholds_set) else None
        if a is None or b is None:
            status = "no_signal"
        elif a == b:
            status = "agree"
        else:
            status = "conflict"
        counts[status] = counts.get(status, 0) + 1
        rows.append({"id": w["id"], "lemma": w["lemma"], "band_current": cur, "band_cefr": a or "", "band_freq": b or "",
                     "freq_rank": freq.get(lemma, ""), "status": status})

        if args.apply and status == "conflict":
            w["review"]["status"] = "needs_review"
            w["review"]["reason"] = "band lệch giữa CEFR và tần suất"
            f.write_text(yaml.safe_dump(w, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8", newline="\n")

    out = ROOT / "docs" / "band-assignment-report.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
    print(f"{len(rows)} mục → {out.relative_to(ROOT)} | " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
