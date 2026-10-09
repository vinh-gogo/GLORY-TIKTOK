# Active Context: GLORY-TIKTOK

## 1. Current Work Focus
Refining the vocabulary browsing and learning UX across the interactive Glossary table (`/words/`) and Word detail pages (`/words/<lemma>/`), ensuring high stability, balanced layouts, and responsive cross-device performance.

---

## 2. Recent Changes & Decisions

### 2.1. Professional Homepage Redesign (Glossary & Word Detail Showcase)
- **User Problem Addressed:** Homepage previously used PaperMod's minimalist `profileMode` with only 5 small buttons, completely failing to spotlight the platform's two core assets: the interactive 213+ word **Glossary** and deep-dive **Word Detail Pages**.
- **Comprehensive Homepage Architecture (`layouts/index.html`):**
  - **Hero & Live Search:** Headline, subtitle, and an instant search bar with search suggestions (`deadline`, `reschedule`, `postpone`, `touch-base`, `pedestrian`).
  - **Metrics & Stats Strip:** Live counts for 213+ words, 3 levels (Core, Target, Advanced), 100% ETS-style content, 0đ ad-free.
  - **Focus 1 — Interactive Glossary Showcase:** Split feature section explaining the 3 TOEIC bands and 26-letter filter with an interactive visual table mockup and direct CTA.
  - **Focus 2 — Word Detail Deep-Dive Showcase:** Split feature section highlighting IPA phonetics, pronunciation alerts, collocations, confusing words, and keyboard shortcuts (`←`/`→`) with an interactive word card mockup.
  - **Lesson Sets & TikTok Video Hub:** Grid showcasing Sets 013, 001, 002.
  - **Closing CTA Banner:** High-conversion invitation to begin studying.
- **Custom CSS:** Added responsive styles in `assets/css/extended/custom.css`.

### 2.2. Smart Filter Coordination (Phân cấp TOEIC & Chữ cái A–Z)
- **Root Cause Identified:** Filter deadlock occurred because Band and Letter filters used rigid intersecting AND logic without dynamic feedback: selecting a band like Advanced (13 words only in B, C, E, L, R, S, T) while Letter A was active produced 0 words. Furthermore, `#glossary-reset-btn` shared `.glossary-filter-btn` class, causing click events to read `targetBand = null` and breaking the view.
- **Coordinated State System (`syncFilters`):**
  - Clicking a letter automatically switches Band to `all` if that band has 0 words for the letter (and vice versa).
  - Dynamically calculates letter availability: letters with 0 words in the active band become disabled in real time.
  - Dynamically updates count badges on TOEIC level buttons (e.g. Core (10), Target (11), Advanced (0)).
  - Separated reset button selector and added swipable mobile horizontal scroll for the A-Z bar.

### 2.2. About Page Redesign & Creator Profile (Glory 01 / @wbk.lqv)
- **Profile Info:** Updated channel name to **Glory 01**, TikTok username to `wbk.lqv`, and profile URL to `https://www.tiktok.com/@wbk.lqv` across `hugo.yaml`, shortcodes, and lesson sets.
- **Human-Centric Redesign:** Replaced generic AI-style copy and bullet lists in `content/about.md` with an authentic, relatable creator voice in a bespoke layout (`layouts/about/single.html`).
- **Visual Components:** Added hero profile card with glowing avatar and direct TikTok CTA button, 3-pillar Bento Grid ("Tại sao không chỉ dừng lại ở TikTok?"), interactive 3-step daily study loop, content manifesto, and community connect card.
- **Custom CSS:** Added responsive styling for the About page in `assets/css/extended/custom.css`.

### 2.2. Navigation & Word Detail Layout (Commit `d9ebc6f`)
- **Issue:** Long Vietnamese definitions inside the bottom navigation cards (`← Từ trước` and `Từ tiếp theo →`) caused unequal card stretching, breaking the 50/50 visual balance.
- **Fix:**
  - Updated CSS Grid in [`assets/css/extended/custom.css`](file:///D:/GLORY-TIKTOK/assets/css/extended/custom.css) to `grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);`.
  - Added `min-width: 0`, `max-width: 100%`, and `overflow: hidden` to `.bottom-nav-card` and `.card-text`.
  - Added `text-overflow: ellipsis; white-space: nowrap;` for `.card-word` and `.card-summary`.
  - Applied `truncate 36` in [`layouts/words/single.html`](file:///D:/GLORY-TIKTOK/layouts/words/single.html) with informative full-text tooltips via HTML `title` attributes.

### 2.2. Interactive Glossary Upgrades
- **A–Z Alphabet Filter:** Implemented a full 26-letter bar with disabled styling for empty letters, automatic smooth scroll to table top upon clicking, and mutual reset between search query and letter filters.
- **TOEIC Level Color Coding:** Distinct badge and button colors for Core (emerald green), Target (cyan/blue), and Advanced (purple).
- **Typography & Dark Mode:** Styled vocabulary lemma in pure white on dark backgrounds while preserving the vibrant accent color for IPA phonetics.
- **Sticky Table Header:** Fixed `position: sticky` on the `<thead>` element by overriding PaperMod's `reset.css` table overflow behavior.
- **Header Branding:** Updated site title to "Glory 01 – Blog" and added an animated SVG logo.

---

## 3. Active Decisions & Considerations
- **Git Branch Strategy:** Active work remains strictly on `dev`. Production merges to `main` occur only at release milestones to conserve Cloudflare and GitHub Actions allowances.
- **Validation Mandate:** Every task modifying content or layouts must pass:
  1. `python scripts/validate/validate.py`
  2. `hugo --gc --minify`
- **Data Completeness:** 213 words currently populated in `data/lexicon/`. Any uncertain vocabulary fields must be tagged `review.status: needs_review`.

---

## 4. Next Steps
1. **Lesson Expansion:** Prepare lesson set templates and content for missing sets 003 through 012.
2. **Phase 3 Audio Integration:** Prototype audio playback infrastructure using Cloudflare R2 and lightweight HTML5 audio players.
3. **Practice Timers:** Build the interactive exam countdown simulator reading directly from `data/exam/toeic-speaking.yaml`.
