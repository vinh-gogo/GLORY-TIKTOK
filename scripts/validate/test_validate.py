#!/usr/bin/env python3
"""Kiểm thử validator (PLAN T2.1 + T2.3): mỗi quy tắc có ít nhất 1 ca lỗi cố ý, mỗi schema có mẫu hợp lệ/không hợp lệ.

Cách làm: sao chép data/, schemas/, content/, layouts/ sang thư mục tạm, chèn lỗi, chạy validate.py với GLORY_ROOT trỏ vào
bản sao, rồi kiểm tra mã lỗi/cảnh báo trong báo cáo JSON. Không đụng dữ liệu thật.

Chạy:  python scripts/validate/test_validate.py
V6 (CMUdict) chỉ được kiểm thử khi cài gói `cmudict`; nếu không sẽ SKIP (không tính là đã kiểm thử).
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
VALIDATE = ROOT / "scripts" / "validate" / "validate.py"
SAMPLE = "data/lexicon/d/deadline.yaml"


def _skip_drafts(directory, names):
    """Bỏ các mục lexicon `ai_draft` khi sao chép (hàng nghìn bản nháp chỉ làm test chậm; không ảnh hưởng mã được kiểm)."""
    if Path(directory).parent.name != "lexicon":
        return []
    out = []
    for n in names:
        p = Path(directory) / n
        if p.suffix == ".yaml" and "status: ai_draft" in p.read_text(encoding="utf-8"):
            out.append(n)
    return out


def run(mutator=None):
    """→ (returncode, [mã lỗi], [mã cảnh báo])"""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        for d in ("data", "schemas", "content", "layouts"):
            shutil.copytree(ROOT / d, t / d, ignore=_skip_drafts)
        if mutator:
            mutator(t)
        rep = t / "rep.json"
        env = {**os.environ, "GLORY_ROOT": str(t), "PYTHONIOENCODING": "utf-8"}
        p = subprocess.run([sys.executable, str(VALIDATE), "--report", str(rep)], env=env, capture_output=True,
                           text=True, encoding="utf-8")
        data = json.loads(rep.read_text(encoding="utf-8")) if rep.exists() else {"errors": [], "warnings": []}
        return p.returncode, [e[0] for e in data["errors"]], [w[0] for w in data["warnings"]]


def edit_yaml(rel, fn):
    def _m(t: Path):
        p = t / rel
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        fn(d)
        p.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return _m


def write(rel, text):
    def _m(t: Path):
        p = t / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return _m


VALID_SYNSET = {
    "schema_version": 1, "id": "syn-test-demo", "head_vi": "Ví dụ", "pos": "noun",
    "members": [{"word": "alpha", "nuance_vi": "sắc thái một"}, {"word": "beta", "nuance_vi": "sắc thái hai"}],
    "review": {"status": "ai_draft"},
}


class ValidatorErrors(unittest.TestCase):
    def assertError(self, mutator, code):
        rc, errs, _ = run(mutator)
        self.assertEqual(rc, 1, f"mong đợi lỗi {code}, nhưng validator thoát {rc}; lỗi: {errs}")
        self.assertIn(code, errs)

    def assertWarn(self, mutator, code):
        rc, errs, warns = run(mutator)
        self.assertEqual(rc, 0, f"không được có lỗi, nhưng có {errs}")
        self.assertIn(code, warns)

    def test_baseline_passes(self):
        rc, errs, _ = run()
        self.assertEqual((rc, errs), (0, []))

    # --- V1: schema ---
    def test_v1_word_missing_required(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d.pop("senses")), "V1")

    def test_v1_word_extra_property(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d.update(speaking_use=["x"])), "V1")

    def test_v1_quote_missing_required(self):
        self.assertError(edit_yaml("data/quotes/law-01.yaml", lambda d: d.pop("quote_en")), "V1")

    def test_v1_set_invalid(self):
        def m(t):
            p = t / "content/sets/set-001.md"
            p.write_text(p.read_text(encoding="utf-8").replace("schema_version: 3", "schema_version: 99"), encoding="utf-8")
        self.assertError(m, "V1")

    def test_v1_synset_valid_then_invalid(self):
        rc, errs, _ = run(write("data/synsets/syn-test-demo.yaml", yaml.safe_dump(VALID_SYNSET, allow_unicode=True)))
        self.assertEqual((rc, errs), (0, []), "synset hợp lệ phải qua")
        bad = dict(VALID_SYNSET, members=[VALID_SYNSET["members"][0]])  # thiếu thành viên (minItems 2)
        self.assertError(write("data/synsets/syn-test-demo.yaml", yaml.safe_dump(bad, allow_unicode=True)), "V1")

    # --- V2 ---
    def test_v2_id_mismatch(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d.update(id="deadlinex")), "V2")

    def test_v2_duplicate_lemma(self):
        def m(t):
            p = t / SAMPLE
            d = yaml.safe_load(p.read_text(encoding="utf-8"))
            d["id"] = "deadlinetwo"
            (t / "data/lexicon/d/deadlinetwo.yaml").write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False), encoding="utf-8")
        self.assertError(m, "V2")

    # --- V3 ---
    def test_v3_set_unknown_word(self):
        def m(t):
            p = t / "content/sets/set-001.md"
            p.write_text(p.read_text(encoding="utf-8").replace("words:\n", "words:\n- zzz-not-a-word\n", 1), encoding="utf-8")
        self.assertError(m, "V3")

    def test_v3_quote_unknown_highlight_word(self):
        def fn(d):
            d["highlights"][0]["word"] = "zzz-not-a-word"
        self.assertError(edit_yaml("data/quotes/law-01.yaml", fn), "V3")

    # --- V4 ---
    def test_v4_unknown_topic(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d.update(topics=["no-such-topic"])), "V4")

    def test_v4_unknown_source(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d["review"].update(sources=["no-such-source"])), "V4")

    # --- V5 ---
    def test_v5_invalid_ipa_char(self):
        self.assertError(edit_yaml(SAMPLE, lambda d: d["ipa"].update(us="/ˈdЖdlaɪn/")), "V5")

    # --- V9 / V10 ---
    def test_v9_needs_review_without_reason(self):
        def fn(d):
            d["review"]["status"] = "needs_review"
            d["review"].pop("reason", None)
        self.assertError(edit_yaml(SAMPLE, fn), "V9")

    def test_v10_no_independent_source(self):
        def fn(d):
            d["review"]["checked_by"] = ["glory-editorial"]
            d["review"]["sources"] = ["vocabulary-md"]
            d["review"]["status"] = "ai_cross_checked"
        self.assertError(edit_yaml(SAMPLE, fn), "V10")

    # --- V14 ---
    def test_v14_hardcoded_score(self):
        self.assertError(write("layouts/zz-test.html", "<p>Mục tiêu TOEIC 750+</p>\n"), "V14")

    # --- Cảnh báo ---
    def test_v7_collocation_without_lemma(self):
        def fn(d):
            d["collocations"].append({"phrase": "completely unrelated phrase", "meaning_vi": "cụm không liên quan",
                                      "evidence": {"source": "unverified", "checked_at": "2026-10-10"}})
        self.assertWarn(edit_yaml(SAMPLE, fn), "V7")

    def test_v8_example_without_lemma(self):
        self.assertWarn(edit_yaml(SAMPLE, lambda d: d["examples"].append({"en": "Nothing relevant appears here.", "vi": "Không liên quan."})), "V8")

    def test_v11_unverified_collocation(self):
        rc, errs, warns = run()
        self.assertIn("V11", warns)

    def test_v12_missing_vietnamese_diacritics(self):
        self.assertWarn(edit_yaml(SAMPLE, lambda d: d["senses"][0].update(note_vi="Day la ghi chu tieng Viet khong co dau nao ca")), "V12")

    def test_v13_band_cefr_mismatch(self):
        self.assertWarn(edit_yaml(SAMPLE, lambda d: d["level"].update(band="core", cefr="C1")), "V13")


@unittest.skipUnless(shutil.which("python") and importlib.util.find_spec("cmudict"), "V6 cần gói cmudict (pip install cmudict) — chưa được kiểm thử")
class ValidatorV6(unittest.TestCase):
    def test_v6_lemma_missing_in_cmudict(self):
        def fn(d):
            d["lemma"] = "zzqxj"
            d["id"] = "zzqxj"
        rc, errs, warns = run(edit_yaml(SAMPLE, fn))
        self.assertIn('V6', warns)


if __name__ == "__main__":
    unittest.main(verbosity=2)
