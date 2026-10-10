# Active Context: GLORY-TIKTOK

## 1. Current Work Focus
**Pivot (2026-10):** từ site luyện TOEIC Speaking sang **nền tảng từ vựng / collocations / đồng nghĩa / câu nói hay**, mobile-first. Kế hoạch gốc: `PLAN_NEN_MONG_Tu_Vung_TOEIC.md`. Các quyết định kiến trúc: `docs/adr/004`–`008`.

Đã triển khai nền móng (F0–F3, F5 một phần) — xem `progress.md`. **F4 (mở rộng lên ~1.500 từ / 4.500 collocation / 300 synset / 100 câu) CHƯA làm**: cần nguồn kiểm chứng và người duyệt; chỉ dựng pipeline (`scripts/import/import_batch.py`).

## 2. Kiến trúc hiện tại (tóm tắt)
- Dữ liệu: `data/lexicon/` (schema v3), `data/levels.yaml` (4 band, `band_order`), `data/topics.yaml` (14 chủ đề + `legacy_map`), `data/sources.yaml`, `data/quotes/`.
- Trang từ sinh bởi `content/words/_content.gotmpl`; `/words/` (danh sách) bị ẩn, chỉ giữ `/words/<id>/`. Danh sách chỉ hiện từ `ai_cross_checked`/`human_verified` (`layouts/_partials/words-visible.html`).
- Tìm kiếm: `/search-index.json` (output format `SearchIndex`), JS chuẩn hóa tiếng Việt không dấu (`assets/js/search.js`); không dùng Fuse.
- UI: tab bar dưới trên mobile (`.tabbar`), menu ngang ≥768px; CSS module trong `assets/css/extended/`.
- Redirect: `static/_redirects` sinh bởi `scripts/build/gen_redirects.py`; `scripts/validate/check_urls.py` đối chiếu `docs/url-inventory-2026-10.txt`.

## 3. Active Decisions & Considerations
- **Git Branch Strategy:** làm việc trên `dev`; merge `main` ở mốc phát hành.
- **Validation Mandate:** `python scripts/validate/validate.py` (0 lỗi) + `hugo --gc --minify` (sạch) + `check_urls.py`.
- **Không bịa dữ liệu:** mục chưa chắc → `needs_review` + `reason`. 213 mục hiện có là `ai_cross_checked` nhưng `level.basis=[editorial]`, 709 collocation `evidence: unverified` (xem `docs/audit-2026-10-lexicon-v3.md`).
- Bảng điểm ETS↔CEFR và danh sách nhóm chủ đề ETS **chưa đối chiếu văn bản gốc** (`verified_primary: false`).

## 4. Next Steps
1. Người duyệt quyết định các câu hỏi mở (Q2/Q3/Q6/Q8 trong plan) và chính sách cho mục có tuyên bố nguồn không kiểm chứng.
2. Đưa danh sách tần suất (TSL/BSL/NGSL) + CEFR-J vào `sources/wordlists/` sau khi kiểm tra giấy phép → chạy `scripts/levels/assign_band.py` → chốt ngưỡng ở ADR-005.
3. Cài `cmudict` → chạy `scripts/ipa/check_cmudict.py`.
4. Soạn lô đầu cho tầng `foundation`, rồi mở rộng theo lô (F4).
5. Thay link TikTok placeholder của các set bằng link video thật; thử nghiệm trên thiết bị thật + Lighthouse.
