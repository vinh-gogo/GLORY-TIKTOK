# Project Brief: GLORY-TIKTOK

> **Cập nhật 2026-10 — ĐỊNH HƯỚNG ĐÃ ĐỔI.** Sản phẩm chuyển từ site luyện TOEIC Speaking sang nền tảng từ vựng / collocations / đồng nghĩa / câu nói hay, mobile-first. Các phần bên dưới nói về Speaking (bộ đếm giờ, 11 dạng câu hỏi, `data/exam/toeic-speaking.yaml`, `/parts/`, `/guides/`, `custom.css`) là **lịch sử**; nguồn đúng hiện hành: `PLAN_NEN_MONG_Tu_Vung_TOEIC.md`, `docs/adr/004`–`008` và `activeContext.md`. Nội dung Speaking cũ lưu ở `docs/archive/`.

## 1. Executive Summary
**GLORY-TIKTOK** (Glory 01 – TOEIC Speaking / Glory 01 – Blog) is an educational web platform designed to transform short-form TikTok learning content into a comprehensive, self-paced TOEIC Speaking preparation ecosystem. 

- **Repository:** `vinh-gogo/GLORY-TIKTOK`
- **Core Tech Stack:** Hugo Extended (Static Site Generator) + PaperMod Theme + Cloudflare Pages
- **Target Scale:** ~340 lesson sets, ~2,500 verified vocabulary and collocation entries, 5 TOEIC Speaking question types (Q1–Q11), 30 topics, and 10 full mock exams.

---

## 2. Core Requirements & Vision
1. **From Video Companion to Complete Study Ecosystem:**
   - TikTok serves as the awareness funnel; the website serves as the daily retention, practice, and mastery hub.
   - Comprehensive learning flow: Watch Video → Learn Vocabulary & Collocations → Listen to Native Audio / IPA Guidance → Practice with Realistic Exam Timers → Self-Evaluate & Shadow → Retain with Spaced Repetition (SRS).

2. **Data-First & Single Source of Truth:**
   - Central Lexicon Architecture (`data/lexicon/*.yaml`): Every vocabulary item, phonetic notation, collocation, and example exists in exactly one place.
   - Exam Parameters (`data/exam/toeic-speaking.yaml`): Question formats, preparation times, and speaking times are centrally declared and never hardcoded in templates.
   - Lesson sets (`content/sets/*.md`) only reference lexicon IDs.

3. **Pedagogical & Linguistic Integrity:**
   - Zero hallucination policy: AI must not invent IPA, definitions, or collocations. Unverified items are flagged with `review.status: needs_review`.
   - 100% original, copyright-compliant "ETS-style" prompts and examples (no copyrighted dictionary or test verbatim copying).
   - Vietnamese learner focus: Special attention to final consonants (-s, -ed, -t, -d), consonant clusters, sentence stress, and natural collocations.

4. **URL & Navigation Contracts:**
   - Permanent URLs: 3-digit identifiers (`/sets/001/`) and short aliases (`/013`, `/words/<lemma>`) are strictly preserved.
   - Smooth navigation: Sticky headers, A–Z alphabet filtering, keyboard navigation shortcuts (`←` / `→`), and balanced navigation controls.

5. **Performance, Privacy & Security:**
   - Sub-second Hugo build times (~400ms for 360+ pages).
   - High mobile Lighthouse scores (target ≥ 90).
   - Privacy-first: Practice data and audio recordings stay local on user devices (localStorage / IndexedDB); no telemetry or external upload without explicit consent.
