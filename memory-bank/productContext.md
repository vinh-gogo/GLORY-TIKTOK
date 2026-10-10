# Product Context: GLORY-TIKTOK

> **Cập nhật 2026-10 — ĐỊNH HƯỚNG ĐÃ ĐỔI.** Sản phẩm chuyển từ site luyện TOEIC Speaking sang nền tảng từ vựng / collocations / đồng nghĩa / câu nói hay, mobile-first. Các phần bên dưới nói về Speaking (bộ đếm giờ, 11 dạng câu hỏi, `data/exam/toeic-speaking.yaml`, `/parts/`, `/guides/`, `custom.css`) là **lịch sử**; nguồn đúng hiện hành: `PLAN_NEN_MONG_Tu_Vung_TOEIC.md`, `docs/adr/004`–`008` và `activeContext.md`. Nội dung Speaking cũ lưu ở `docs/archive/`.

## 1. Why This Project Exists
Learners who discover the *Glory 01* educational channel on TikTok frequently struggle to retain vocabulary, master pronunciation, and transfer knowledge into spontaneous spoken English under timed exam conditions. Short-form video platforms inherently lack:
- Structured search and comprehensive reference lookup.
- Interactive pronunciation verification and phonetic guidance.
- Timed speaking practice environments matching ETS test software.
- Spaced repetition and progress tracking.

GLORY-TIKTOK provides an accessible, ad-free, high-speed web companion that deepens and solidifies the learning sparked by social media videos.

---

## 2. Problems It Solves
1. **Content Fragmentation:** Eliminates the frustration of searching through dozens of TikTok clips to find a specific phrase or pronunciation tip.
2. **Vietnamese Speaker Pronunciation Pitfalls:** Explicitly highlights confusing word pairs, sound-alikes, silent letters, and syllable stress to overcome common Vietnamese L1 interference.
3. **Test Anxiety & Timing Pressure:** Bridges the gap between passive listening and active speaking with realistic, timed countdown simulators for all 11 TOEIC Speaking tasks.
4. **Data Redundancy & Inconsistency:** Eliminates conflicting definitions and duplicated collocations across lesson sets through a unified, schema-validated central lexicon.

---

## 3. How It Works
- **Entry Points:** Learners enter via QR codes, video descriptions, or memorable short URLs (e.g. `glory01.com/013` or `glory01.com/words/deadline`).
- **Interactive Glossary (`/words/`):**
  - Instant live search by keyword, IPA, meaning, or topic.
  - Full 26-letter A–Z alphabet bar with automated disabled state for letters without words.
  - Color-coded TOEIC level tags: **Core** (green), **Target** (blue), **Advanced** (purple).
  - 1440px wide desktop presentation with sticky table header for comfortable scanning.
  - Entire table row clickability directly navigating to word detail.
- **Word Detail Pages (`/words/<lemma>/`):**
  - Rich word cards: lemma (styled in crisp white in dark mode), exact IPA phonetics, part of speech, Vietnamese translations, and high-frequency collocations.
  - Contextual navigation: Sticky top bar with quick jump, floating side arrows, and balanced bottom navigation cards (`← Từ trước` and `Từ tiếp theo →`) with single-line truncated summaries and full hover tooltips.
  - Keyboard shortcuts: Left/Right arrow keys navigate seamlessly between consecutive words.
- **Lesson Sets (`/sets/<id>/`):**
  - Embedded video lesson with lazy loading.
  - Targeted vocabulary checklist referencing central lexicon items.
  - Model responses with highlighted collocations.
  - Practice prompts ready for future timed exam simulations.

---

## 4. User Experience Goals
- **Distraction-Free Learning:** Clean typography, minimalist PaperMod layout, zero intrusive ads or popups.
- **Frictionless Mobile-First Experience:** Ultra-fast load times, thumb-friendly tap targets, smooth horizontal table scrolling.
- **Progressive Enhancement:** Works completely as static HTML even with JavaScript disabled; dynamic JS islands progressively enhance UX (timers, audio players, search, filters).
