# Tech Context: GLORY-TIKTOK

## 1. Technologies & Versions
- **Static Site Generator:** Hugo Extended v0.167.0+ (Windows amd64 build).
- **Hugo Theme:** PaperMod (Git submodule at `themes/PaperMod`).
- **Validation Language:** Python 3.12+ (standard library + PyYAML).
- **Deployment Platform:** Cloudflare Pages (automated CI build & deploy from GitHub repo `vinh-gogo/GLORY-TIKTOK`).
- **Target Storage (Future Audio):** Cloudflare R2.
- **Frontend Core:** Semantic HTML5, CSS Variables, CSS Grid / Flexbox, Vanilla ES6+ JavaScript.

---

## 2. Development Setup & Commands

### 2.1. Environment
- **Operating System:** Windows 11 (PowerShell terminal).
- **Root Directory:** `D:\GLORY-TIKTOK`.
- **Primary Development Branch:** `dev`.
- **Production Branch:** `main` (only updated on deliberate release merges to save GitHub Actions runner minutes).

### 2.2. Standard Verification Workflow
Before reporting any task complete or committing changes, run the following verification sequence:

1. **Data Schema & Integrity Validation:**
   ```powershell
   python scripts/validate/validate.py
   ```
   *Expected output:* `[OK] Validation successful! All schemas, lexicon entries, and sets are verified.`

2. **Hugo Site Build Verification:**
   ```powershell
   hugo --gc --minify
   ```
   *Expected output:* Successful build of all pages (currently 364+ pages) in < 1 second with 0 errors.

3. **Git Commits & Branch Integrity:**
   - Always commit to `dev`.
   - On Windows, if Git touches submodule trees or `.git/modules`, run with unsandboxed / bypass privileges when required to prevent permission denial locks.

---

## 3. Technical Constraints & Rules
- **Exam Timings:** All question parameters (preparation seconds, speaking seconds) must strictly be read from `data/exam/toeic-speaking.yaml`. Never hardcode seconds in templates or JS.
- **URL Immutability:** Never modify published slugs or aliases (`/013`, `/words/<lemma>`). Any required redirect must be registered in `static/_redirects` with an accompanying ADR.
- **Hugo Deprecation Awareness:** Hugo v0.156.0+ deprecated `.Site.Data` in favor of `hugo.Data`, and `.Language.LanguageDirection` / `.Language.LanguageCode`. Maintain backward and forward template compatibility.
- **Client Privacy:** Do not load remote tracking scripts or upload audio recordings. All user speech practice and settings remain stored strictly in `localStorage` or `IndexedDB`.
