#!/usr/bin/env python3
"""Tạo bộ khung cho lô nhập hàng loạt từ TSL/NGSL (chưa có trong lexicon).

    python scripts/import/make_chunks.py            # ghi sources/batches/work/in/chunk-NNN.csv + skipped.csv

- IPA: lấy TỪ CMUdict (đối chiếu độc lập, giấy phép BSD-style) rồi đổi ARPAbet → IPA Mỹ bằng quy tắc cố định.
  Vị trí dấu trọng âm được đặt theo heuristic "onset tối đa" → có thể lệch so với từ điển; mọi mục vẫn là ai_draft.
  Từ không có trong CMUdict KHÔNG được nhập (ghi ở skipped.csv) vì schema bắt buộc IPA và quy tắc cấm đoán IPA.
- band: TẠM THỜI theo hạng tần suất (không phải bằng chứng về cấp độ; ADR-005 chưa chốt):
    NGSL hạng ≤1000 → foundation; ≤2000 → core; còn lại → target
    TSL  hạng ≤400  → core;       ≤800  → target; còn lại → advanced
  Chỉ dùng cho bản nháp ẩn (ai_draft); reviewer phải xác nhận/đổi.
Yêu cầu: pip install cmudict; sources/wordlists/candidates.csv (xem scripts/levels/wordlists.py candidates).
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "sources" / "batches" / "work"
CHUNK = 130

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

VOWELS = {
    "AA": "ɑ", "AE": "æ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ", "EH": "ɛ", "EY": "eɪ",
    "IH": "ɪ", "IY": "i", "OW": "oʊ", "OY": "ɔɪ", "UH": "ʊ", "UW": "u",
}
CONS = {
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "F": "f", "G": "ɡ", "HH": "h", "JH": "dʒ",
    "K": "k", "L": "l", "M": "m", "N": "n", "NG": "ŋ", "P": "p", "R": "r", "S": "s",
    "SH": "ʃ", "T": "t", "TH": "θ", "V": "v", "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ",
}
# Cụm phụ âm được coi là onset hợp lệ của một âm tiết (heuristic).
ONSETS2 = {
    "P L", "P R", "B L", "B R", "T R", "D R", "K L", "K R", "G L", "G R", "F L", "F R", "TH R",
    "SH R", "S L", "S M", "S N", "S P", "S T", "S K", "S W", "T W", "K W", "D W", "HH Y", "K Y",
    "P Y", "B Y", "M Y", "F Y", "V Y", "T Y", "D Y", "N Y", "L Y", "S Y", "Z Y",
}
ONSETS3 = {"S P L", "S P R", "S T R", "S K R", "S K W", "S K L"}


def vowel_ipa(p: str) -> str:
    base, stress = p[:-1], p[-1]
    if base == "AH":
        return "ʌ" if stress in "12" else "ə"
    if base == "ER":
        return "ɝ" if stress in "12" else "ɚ"
    return VOWELS[base]


def arpa_to_ipa(phones: list[str]) -> str:
    vidx = [i for i, p in enumerate(phones) if p[-1].isdigit()]
    if not vidx:
        return ""
    # onset của âm tiết k = các phụ âm cuối đoạn nằm giữa vowel k-1 và k (max-onset heuristic)
    starts = []
    for k, v in enumerate(vidx):
        lo = vidx[k - 1] + 1 if k else 0
        cluster = phones[lo:v]
        n = 0
        if k == 0:
            n = len(cluster)
        else:
            for take in (3, 2, 1):
                if len(cluster) >= take and (take == 1 or " ".join(cluster[-take:]) in (ONSETS3 if take == 3 else ONSETS2)):
                    n = take
                    break
        starts.append(v - n)
    out = []
    for k, v in enumerate(vidx):
        stress = phones[v][-1]
        lo = starts[k]
        hi = starts[k + 1] if k + 1 < len(vidx) else len(phones)
        syl = ""
        for i in range(lo, hi):
            p = phones[i]
            syl += vowel_ipa(p) if p[-1].isdigit() else CONS[p]
        mark = "ˈ" if stress == "1" else ("ˌ" if stress == "2" else "")
        if len(vidx) == 1:
            mark = ""
        out.append(mark + syl)
    return "/" + "".join(out) + "/"


def provisional_band(lst: str, rank: int) -> str:
    if lst == "ngsl":
        return "foundation" if rank <= 1000 else ("core" if rank <= 2000 else "target")
    return "core" if rank <= 400 else ("target" if rank <= 800 else "advanced")


def main() -> int:
    try:
        import cmudict
    except ImportError:
        print("Cần: pip install cmudict")
        return 2
    d = cmudict.dict()
    rows = []
    with (ROOT / "sources" / "wordlists" / "candidates.csv").open(encoding="utf-8", newline="") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    rows = list(csv.DictReader(lines))
    ok, skipped = [], []
    for r in rows:
        lemma = r["lemma"].strip().lower()
        if lemma not in d:
            skipped.append([lemma, r["list"], r["rank"], "không có trong CMUdict"])
            continue
        ipa = arpa_to_ipa(d[lemma][0])
        if not ipa or any(c in lemma for c in " "):
            skipped.append([lemma, r["list"], r["rank"], "không tạo được IPA / cụm nhiều từ"])
            continue
        ok.append([lemma, r["list"], r["rank"], ipa, provisional_band(r["list"], int(r["rank"]))])
    (WORK / "in").mkdir(parents=True, exist_ok=True)
    for old in (WORK / "in").glob("chunk-*.csv"):
        old.unlink()
    for n in range(0, len(ok), CHUNK):
        p = WORK / "in" / f"chunk-{n // CHUNK + 1:03d}.csv"
        with p.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["lemma", "list", "rank", "ipa", "band"])
            w.writerows(ok[n:n + CHUNK])
    with (WORK / "skipped.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["lemma", "list", "rank", "ly_do"])
        w.writerows(skipped)
    print(f"{len(ok)} từ có IPA CMUdict → {(len(ok) + CHUNK - 1) // CHUNK} chunk; bỏ qua {len(skipped)} (xem skipped.csv)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
