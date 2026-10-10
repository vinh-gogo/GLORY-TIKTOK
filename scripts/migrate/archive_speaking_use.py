#!/usr/bin/env python3
"""Lưu giá trị `speaking_use` (v2) từ Git HEAD ra CSV trước khi gỡ khỏi schema v3 (PLAN T1.x / D1).
Chạy MỘT lần, trước khi commit migration. Kết quả: docs/archive/speaking/speaking_use.csv"""
import csv
import glob
import os
import subprocess
import sys

import yaml

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
out = os.path.join(BASE, "docs", "archive", "speaking", "speaking_use.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)
rows = []
for path in sorted(glob.glob(os.path.join(BASE, "data", "lexicon", "**", "*.yaml"), recursive=True)):
    rel = os.path.relpath(path, BASE).replace("\\", "/")
    p = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=BASE, capture_output=True)
    if p.returncode != 0:
        print("skip", rel, file=sys.stderr)
        continue
    d = yaml.safe_load(p.stdout.decode("utf-8"))
    rows.append((d["id"], ";".join(d.get("speaking_use") or [])))
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "speaking_use"])
    w.writerows(rows)
print(f"wrote {len(rows)} rows -> {out}")
