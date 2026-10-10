#!/usr/bin/env python3
"""Kiểm tra mọi URL trong docs/url-inventory-*.txt vẫn truy cập được sau khi build.

Một URL "sống" nếu:  (a) có file tương ứng trong thư mục build, hoặc
                     (b) khớp một quy tắc trong static/_redirects mà ĐÍCH tồn tại (không đi qua >1 bước).
Bỏ qua URL phân trang `/page/N/` (alias phân trang cũ của PaperMod).

Chạy sau `hugo --gc --minify`:   python scripts/validate/check_urls.py [--public public] [--inventory <file>]
Mã thoát 1 nếu có URL chết.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def exists(public: Path, url: str) -> bool:
    p = url.split("#")[0].split("?")[0]
    rel = p.lstrip("/")
    cand = public / rel
    if p.endswith("/") or p == "":
        return (cand / "index.html").exists()
    return cand.is_file() or (cand / "index.html").exists()


def load_rules(path: Path) -> list[tuple[str, str]]:
    rules = []
    if not path.exists():
        return rules
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            rules.append((parts[0], parts[1]))
    return rules


def resolve(url: str, rules: list[tuple[str, str]]) -> str | None:
    for src, dst in rules:
        if "*" in src:
            prefix = src.split("*", 1)[0]
            if url.startswith(prefix):
                return dst.replace(":splat", url[len(prefix):])
        elif url == src:
            return dst
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", default=str(ROOT / "public"))
    ap.add_argument("--inventory", default=None)
    args = ap.parse_args()

    public = Path(args.public)
    inv = Path(args.inventory) if args.inventory else sorted((ROOT / "docs").glob("url-inventory-*.txt"))[-1]
    rules = load_rules(ROOT / "static" / "_redirects")

    urls = [u.strip() for u in inv.read_text(encoding="utf-8-sig").splitlines() if u.strip()]
    urls = [u for u in urls if not re.search(r"/page/\d+/?$", u)]

    dead, redirected, direct = [], 0, 0
    for u in urls:
        if exists(public, u):
            direct += 1
            continue
        dst = resolve(u, rules)
        if dst and exists(public, dst):
            redirected += 1
        else:
            dead.append((u, dst))

    print(f"URL kiểm tra: {len(urls)} | còn nguyên: {direct} | qua redirect: {redirected} | chết: {len(dead)}")
    for u, dst in dead[:50]:
        print(f"  CHẾT {u}" + (f" → {dst} (đích không tồn tại)" if dst else " (không có quy tắc)"))
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
