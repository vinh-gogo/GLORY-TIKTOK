#!/usr/bin/env python3
"""Kiểm tra IPA (US) của từ vựng với CMU Pronouncing Dictionary — quy tắc V6 (PLAN_NEN_MONG 8.2).

Phương pháp (HEURISTIC, không thay người duyệt): so SỐ ÂM TIẾT và VỊ TRÍ TRỌNG ÂM CHÍNH giữa IPA trong dữ liệu và CMUdict.
Không so từng âm vì ánh xạ ARPAbet→IPA không 1-1 với quy ước IPA của dữ liệu (ví dụ /ɑːr/ vs AA+R).
- Phụ âm tự thành âm tiết (…ʃn, …tl, …zm) được phép lệch 1 âm tiết → ghi "tolerated".
- Từ nhiều từ (touch-base...): bỏ qua; từ không có trong từ điển: "missing".

Nguồn từ điển (ưu tiên theo thứ tự):
    --cmudict-file <đường dẫn file cmudict dạng text: "WORD  P1 P2 …">
    gói Python `cmudict` (pip install cmudict) — chưa cài mặc định; không có thì script thoát 0 với thông báo.
Báo cáo CSV: docs/ipa-check-report.csv
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

IPA_VOWELS = set("aeiouɑɒæɔəɛɪʊʌɜɚɝɐɨʉøœyɘɵ")
SYLLABIC_END = re.compile(r"[ʃʒszdtvfkgpbθð]\s*[nlm]$|ʃn̩|n̩|l̩|m̩")


def ipa_stats(ipa: str) -> tuple[int, int | None]:
    """→ (số âm tiết theo cụm nguyên âm, chỉ số âm tiết mang trọng âm chính hoặc None)."""
    s = ipa.strip("/ ")
    n, in_v, stress_idx, pending_stress = 0, False, None, False
    for ch in s:
        if ch == "ˈ":
            pending_stress = True
            in_v = False
            continue
        if ch in IPA_VOWELS:
            if not in_v:
                n += 1
                in_v = True
                if pending_stress and stress_idx is None:
                    stress_idx = n - 1
                pending_stress = False
        elif ch in "ːˑ\u0361":  # độ dài/ligature không ngắt cụm nguyên âm
            continue
        else:
            in_v = False
    return n, stress_idx


def cmu_stats(phones: list[str]) -> tuple[int, int | None]:
    n, stress = 0, None
    for p in phones:
        m = re.match(r"^[A-Z]+([012])$", p)
        if m:
            if m.group(1) == "1" and stress is None:
                stress = n
            n += 1
    return n, stress


def load_cmu(path: str | None) -> dict[str, list[list[str]]] | None:
    if path:
        d: dict[str, list[list[str]]] = {}
        for line in Path(path).read_text(encoding="latin-1").splitlines():
            if not line or line.startswith(";;;"):
                continue
            w, *ph = line.split()
            d.setdefault(re.sub(r"\(\d+\)$", "", w.lower()), []).append(ph)
        return d
    try:
        import cmudict  # type: ignore
    except ImportError:
        return None
    return {w: list(p) for w, p in cmudict.dict().items()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cmudict-file")
    args = ap.parse_args()

    cmu = load_cmu(args.cmudict_file)
    if cmu is None:
        print("Bỏ qua V6: chưa có CMUdict (cài `pip install cmudict` hoặc truyền --cmudict-file).")
        return 0

    rows, counts = [], {}
    for f in sorted((ROOT / "data" / "lexicon").rglob("*.yaml")):
        w = yaml.safe_load(f.read_text(encoding="utf-8"))
        lemma = w["lemma"].lower()
        us = (w.get("ipa") or {}).get("us", "")
        if not us or " " in lemma or "-" in lemma:
            status, detail = "skipped", "nhiều từ hoặc thiếu IPA"
        elif lemma not in cmu:
            status, detail = "missing", "không có trong CMUdict"
        else:
            n_i, s_i = ipa_stats(us)
            best = None
            for ph in cmu[lemma]:
                n_c, s_c = cmu_stats(ph)
                tol = n_c - n_i == 1 and SYLLABIC_END.search(us.strip("/"))
                ok_n = n_c == n_i or tol
                ok_s = s_i is None or s_c is None or s_i == s_c
                cand = ("ok" if ok_n and ok_s and not tol else "tolerated" if ok_n and ok_s else "mismatch",
                        f"IPA: {n_i} âm tiết, trọng âm #{s_i}; CMU: {n_c} âm tiết, trọng âm #{s_c}")
                if best is None or cand[0] == "ok" or (cand[0] == "tolerated" and best[0] == "mismatch"):
                    best = cand
                if cand[0] == "ok":
                    break
            status, detail = best  # type: ignore[misc]
        counts[status] = counts.get(status, 0) + 1
        rows.append({"id": w["id"], "ipa_us": us, "status": status, "detail": detail})

    out = ROOT / "docs" / "ipa-check-report.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=["id", "ipa_us", "status", "detail"])
        wr.writeheader()
        wr.writerows(rows)
    print(f"{len(rows)} mục → {out.relative_to(ROOT)} | " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
