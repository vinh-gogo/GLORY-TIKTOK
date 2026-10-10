#!/usr/bin/env python3
"""Tải & đối chiếu danh sách tần suất TSL 1.2 / NGSL 1.2 (Browne & Culligan; CC BY-SA 4.0).

    python scripts/levels/wordlists.py fetch        # tải về sources/wordlists/ (cần mạng) + kiểm tra số dòng
    python scripts/levels/wordlists.py report       # đối chiếu data/lexicon với TSL/NGSL → docs/freq-coverage-report.csv
    python scripts/levels/wordlists.py candidates   # từ trong TSL/NGSL chưa có trong lexicon → sources/wordlists/candidates.csv

QUAN TRỌNG
- TSL và NGSL là HAI danh sách rời nhau (TSL là phần bổ sung ngoài NGSL; giao = 0). Thứ hạng của hai danh sách
  KHÔNG so sánh được với nhau → không có ngưỡng "freq_rank_max" chung (xem ADR-005).
- Script chỉ BÁO CÁO. Không sửa `level.band`, không ghi `level.basis`.
- Tệp tải về (CC BY-SA 4.0) không được commit (xem .gitignore); báo cáo kèm ghi công nguồn.
- Dạng biến cách (meeting → meet) được nối về từ gốc bằng tệp `*_lemmatized_for_teaching.csv`.
  Từ phái sinh (collaborate vs collaboration) KHÔNG được nối tự động.
"""
from __future__ import annotations

import csv
import io
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WL = ROOT / "sources" / "wordlists"
BASE = "https://www.newgeneralservicelist.com/s/"
FILES = {
    "TSL_12_stats.csv": 1250,
    "TSL_12_lemmatized_for_teaching.csv": None,
    "NGSL_12_stats.csv": 2809,
    "NGSL_12_lemmatized_for_teaching.csv": None,
}
ATTRIBUTION = (
    "TOEIC Service List 1.2 (Browne, C. & Culligan, B.) và New General Service List 1.2 "
    "(Browne, C., Culligan, B. & Phillips, J.), https://www.newgeneralservicelist.com/ — "
    "Creative Commons Attribution-ShareAlike 4.0 International."
)

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode("cp1252")  # tệp gốc có ký tự không phải UTF-8


def load_ranks(name: str, wcol: str, rcol: str) -> dict[str, int]:
    rows = csv.DictReader(io.StringIO(read_text(WL / name), newline=""))
    return {r[wcol].strip().lower(): int(r[rcol]) for r in rows}


def load_variants(name: str) -> dict[str, str]:
    """form → headword (dòng '#' là chú thích)."""
    out: dict[str, str] = {}
    for line in read_text(WL / name).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        forms = [x.strip().lower() for x in line.split(",") if x.strip()]
        for f in forms:
            out.setdefault(f, forms[0])
    return out


def load_lists():
    tsl = load_ranks("TSL_12_stats.csv", "Word", "TSL Rank")
    ngsl = load_ranks("NGSL_12_stats.csv", "Lemma", "SFI Rank")
    var = {"tsl": load_variants("TSL_12_lemmatized_for_teaching.csv"),
           "ngsl": load_variants("NGSL_12_lemmatized_for_teaching.csv")}
    return {"ngsl": ngsl, "tsl": tsl}, var


def lookup(lemma: str, ranks: dict, var: dict):
    """Trả (list, headword, rank, via) hoặc None. Khớp trực tiếp trước, rồi biến cách."""
    for lst in ("ngsl", "tsl"):
        if lemma in ranks[lst]:
            return lst, lemma, ranks[lst][lemma], "exact"
    for lst in ("ngsl", "tsl"):
        head = var[lst].get(lemma)
        if head and head in ranks[lst]:
            return lst, head, ranks[lst][head], "inflection"
    return None


def cmd_fetch() -> int:
    WL.mkdir(parents=True, exist_ok=True)
    for name, expect in FILES.items():
        data = urllib.request.urlopen(BASE + name, timeout=60).read()
        (WL / name).write_bytes(data)
        print(f"tải {name}: {len(data)} byte")
    ranks, _ = load_lists()
    for lst, expect in (("tsl", 1250), ("ngsl", 2809)):
        n = len(ranks[lst])
        flag = "OK" if n == expect else f"LỆCH (mong đợi {expect})"
        print(f"{lst.upper()}: {n} mục — {flag}")
    if not (WL / "ATTRIBUTION.txt").exists():
        (WL / "ATTRIBUTION.txt").write_text(ATTRIBUTION + "\n", encoding="utf-8")
    return 0


def cmd_report() -> int:
    ranks, var = load_lists()
    rows, counts = [], {}
    for f in sorted((ROOT / "data" / "lexicon").rglob("*.yaml")):
        w = yaml.safe_load(f.read_text(encoding="utf-8"))
        lemma = w["lemma"].lower()
        hit = lookup(lemma, ranks, var) if " " not in lemma else None
        if " " in lemma:
            lst, head, rank, via = "", "", "", "multiword"
        elif hit:
            lst, head, rank, via = hit
        else:
            lst, head, rank, via = "", "", "", "not_in_lists"
        counts[(w["level"]["band"], lst or via)] = counts.get((w["level"]["band"], lst or via), 0) + 1
        rows.append([lemma, w["level"]["band"], w["review"]["status"], lst, head, rank, via])
    out = ROOT / "docs" / "freq-coverage-report.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        fh.write("# Nguồn: " + ATTRIBUTION + " Báo cáo này là dữ liệu phái sinh, cùng giấy phép CC BY-SA 4.0.\n")
        w_ = csv.writer(fh)
        w_.writerow(["lemma", "band_hien_tai", "review_status", "list", "headword", "rank_trong_list", "khop"])
        w_.writerows(rows)
    print(f"ghi {out} ({len(rows)} dòng)")
    for k in sorted(counts):
        print(k, counts[k])
    return 0


def cmd_candidates() -> int:
    ranks, _ = load_lists()
    have = set()
    for f in (ROOT / "data" / "lexicon").rglob("*.yaml"):
        have.add(yaml.safe_load(f.read_text(encoding="utf-8"))["lemma"].lower())
    out = WL / "candidates.csv"
    n = 0
    with out.open("w", encoding="utf-8", newline="") as fh:
        fh.write("# Nguồn: " + ATTRIBUTION + "\n")
        w_ = csv.writer(fh)
        w_.writerow(["lemma", "list", "rank"])
        for lst in ("tsl", "ngsl"):
            for lemma, rank in sorted(ranks[lst].items(), key=lambda kv: kv[1]):
                if lemma not in have:
                    w_.writerow([lemma, lst, rank])
                    n += 1
    print(f"ghi {out}: {n} từ ứng viên chưa có trong lexicon (chỉ là danh sách việc cần làm, KHÔNG phải nội dung)")
    return 0


def main() -> int:
    cmds = {"fetch": cmd_fetch, "report": cmd_report, "candidates": cmd_candidates}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 2
    return cmds[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
