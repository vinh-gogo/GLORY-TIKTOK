# Progress Tracking: GLORY-TIKTOK

## 1. What Works
- [x] **Central Lexicon System:**
  - 213 distinct vocabulary YAML files in `data/lexicon/`.
  - Schema validation pipeline in `scripts/validate/validate.py` passing with 0 errors.
  - Automatic page generation for all words under `/words/<lemma>/`.
- [x] **Interactive Glossary Table (`/words/`):**
  - 1440px expanded desktop view.
  - Sticky table header (`<thead>`) staying pinned during vertical scrolling.
  - Instant live search input with multi-column filtering.
  - Full 26-letter A–Z alphabet filter with disabled states for unrepresented letters.
  - 3-tier level filter buttons (Core, Target, Advanced) with synchronized color coding.
  - Clickable table rows routing directly to word detail pages.
- [x] **Word Detail View (`/words/<lemma>/`):**
  - High-contrast typography with pure white lemma in dark mode.
  - IPA pronunciation guide and grammatical details.
  - Sticky navigation bar with category and breadcrumbs.
  - Keyboard navigation (Left/Right arrow keys) for seamless sequential study.
  - Balanced 50/50 bottom navigation cards with defensive CSS grid sizing, text truncation, and hover tooltips.
- [x] **Site Header & Branding:**
  - Brand title set to "Glory 01 – Blog".
  - Professional, cute animated SVG icon embedded in the header.
- [x] **Performance & Build:**
  - Hugo static generation builds all 364 pages in ~400ms.
  - Zero heavy JavaScript dependencies.

---

## 2. What's Left to Build

### Phase 2: Content & Lesson Expansion
- [ ] Implement lesson sets 003–012 in `content/sets/`.
- [ ] Expand central lexicon from 213 words towards the target milestone (~2,500 entries).
- [ ] Structure sample responses with question classification (Q1–Q11).

### Phase 3: Audio & Pronunciation Tools
- [ ] Establish Cloudflare R2 bucket and audio naming conventions.
- [ ] Add pronunciation audio player widgets to word pages and glossary.
- [ ] Implement shadowing player with playback speed controls (0.8x, 1.0x, 1.2x).

### Phase 4: Exam Simulation Tools
- [ ] Build speaking exam countdown timer reading parameters from `data/exam/toeic-speaking.yaml`.
- [ ] Add client-side voice recording and playback (Web Audio API / MediaRecorder) stored locally.

### Phase 5: Retention & Practice
- [ ] Spaced Repetition System (SRS) flashcard review module.
- [ ] Quick collocation and pronunciation quiz mode.
- [ ] LocalStorage progress tracking (words mastered, lessons completed).

---

## 3. Current Status
- **Overall Status:** Healthy & Stable on branch `dev`.
- **Pages Built:** 364 pages.
- **Lexicon Entries:** 213 files validated.
- **Lesson Sets Live:** 3 sets (001, 002, 013).

---

## 4. Known Issues & Tech Debt
- **Minor:** Hugo build warnings regarding `.Site.Data` deprecation (scheduled for cleanup to `hugo.Data` in future template refactor).
- **Minor:** Cloudflare Pages deployment limits need monitoring as audio assets are planned (handled by ADR-003 via Cloudflare R2).
