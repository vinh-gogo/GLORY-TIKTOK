#!/usr/bin/env python3
"""Sinh static/_redirects từ docs/url-inventory-*.txt và data/topics.yaml (legacy_map).

Quy tắc (AGENTS.md #4): URL cũ không được 404; khi bỏ/đổi phải có redirect + ADR (ADR-004).
Chạy:  python scripts/build/gen_redirects.py          # ghi static/_redirects
       python scripts/build/gen_redirects.py --check  # chỉ kiểm tra file hiện có có khớp không (CI)

Giới hạn Cloudflare Pages (theo tài liệu công khai, chưa đối chiếu lại bản mới nhất): 2.000 quy tắc tĩnh + 100 quy tắc
động (có `*`). Script cảnh báo khi vượt.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")
OUT = ROOT / "static" / "_redirects"

HEADER = """# Sinh tự động bởi scripts/build/gen_redirects.py — KHÔNG sửa tay (sửa data/topics.yaml hoặc script).
# Cú pháp Cloudflare Pages: <nguồn> <đích> <mã>. Quy tắc cụ thể đặt trước quy tắc chung.
"""


def build_rules() -> list[tuple[str, str, int]]:
    topics = yaml.safe_load((ROOT / "data" / "topics.yaml").read_text(encoding="utf-8"))
    new_slugs = set(topics["topics"])
    legacy = topics.get("legacy_map", {})

    rules: list[tuple[str, str, int]] = []

    # 1) Chủ đề cũ → chủ đề mới (kèm phân trang /page/N/ bằng dấu *)
    for old, new in sorted(legacy.items()):
        if old == new or old in new_slugs:
            continue  # slug còn dùng, URL không đổi
        dest = f"/topics/{new}/" if new else "/glossary/"
        rules.append((f"/topics/{old}/", dest, 301))
        rules.append((f"/topics/{old}/*", dest, 301))

    # 2) Khu vực đã bỏ
    rules += [
        ("/words/", "/glossary/", 301),         # trang /words/ không còn render; từng từ /words/<id>/ vẫn giữ nguyên
        ("/guides/", "/", 301),
        ("/guides/*", "/", 301),
        ("/parts/", "/glossary/", 301),
        ("/parts/*", "/glossary/", 301),
        ("/series/", "/sets/", 301),
        ("/series/*", "/sets/", 301),
        ("/tags/", "/glossary/", 301),
        ("/tags/*", "/glossary/", 301),
    ]
    return rules


def render(rules: list[tuple[str, str, int]]) -> str:
    lines = [HEADER.rstrip("\n"), ""]
    lines += [f"{s} {d} {c}" for s, d, c in rules]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    rules = build_rules()
    dyn = sum(1 for s, _, _ in rules if "*" in s)
    stat = len(rules) - dyn
    if dyn > 100 or stat > 2000:
        print(f"CẢNH BÁO: vượt giới hạn Cloudflare (tĩnh={stat}, động={dyn})", file=sys.stderr)
    text = render(rules)

    if args.check:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != text:
            print("static/_redirects không khớp. Chạy: python scripts/build/gen_redirects.py", file=sys.stderr)
            return 1
        print(f"OK: {len(rules)} quy tắc (tĩnh={stat}, động={dyn})")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"Đã ghi {OUT.relative_to(ROOT)}: {len(rules)} quy tắc (tĩnh={stat}, động={dyn})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
