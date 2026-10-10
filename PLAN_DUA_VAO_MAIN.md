# KẾ HOẠCH ĐƯA CÔNG VIỆC ĐÃ XONG VÀO `main` (TỪNG PHẦN)

> Trạng thái lập kế hoạch: 2026-10-11. **Chưa commit/push gì** — mọi thay đổi (pivot sang nền tảng từ vựng) đang nằm trong working tree của nhánh `dev`. Kế hoạch này chỉ mô tả; chờ bạn duyệt rồi mới thực hiện.

## 1. Hiện trạng git (đã đọc bằng lệnh chỉ-đọc)

| Mục | Giá trị |
| :--- | :--- |
| Nhánh làm việc | `dev` (= `origin/dev`, commit `453d88d`) |
| `main` | `ba6d263` (= `origin/main`) — hơn `dev` 5 commit **chỉ là commit merge/sync** (`git diff dev main` rỗng → **nội dung hai nhánh giống hệt**) |
| Thay đổi chưa commit | ~266 file tracked đổi/xóa (+7.310 / −23.242 dòng) và ~4.000 file mới (3.877 trong `data/lexicon/`) |
| Luồng đã dùng | PR #1 `dev → main`; Cloudflare Pages deploy từ `main` |

Hệ quả: trước khi mở PR cần **đồng bộ `main` vào `dev`** (merge không xung đột vì cây giống nhau), để PR không bị báo "behind".

## 2. Kết quả kiểm tra hiện tại (toàn bộ working tree)

- `validate.py`: 0 lỗi, 757 cảnh báo (4.090 file lexicon) · `hugo --gc --minify`: sạch, ~14 s, 213 trang `/words/` (bản nháp không có trang) · `gen_redirects.py --check`: OK · `test_validate.py`: OK (V6 test chạy khi có `cmudict`).
- Đã sửa trong phiên này: lô 3.867 từ nhập hàng loạt **luôn là `ai_draft`** (trước đó 699 mục `needs_review` bị Hugo tạo trang công khai — đã chặn, xem §5).

## 3. Nguyên tắc cắt lát

1. Mỗi PR **tự build xanh** khi đứng một mình trên `main` (CI: validate → test → hugo → redirects → check_urls).
2. Phần phụ thuộc nhau (schema v3 ↔ dữ liệu ↔ template ↔ redirect) **không tách** — nếu tách, `main` sẽ vỡ ở giữa chừng.
3. Phần rủi ro cao (xóa file, đổi URL) đi sau khi nền đã chạy ổn trên preview.
4. Dùng **Squash merge** cho từng PR, giữ lịch sử `main` gọn; nhánh con tạo từ `main` mới nhất sau mỗi lần merge.
5. Không commit `sources/wordlists/*` (CC BY-SA, `.gitignore`) và `sources/batches/work/in/`.

## 4. Các lát (thứ tự merge)

### PR-0 — Đồng bộ nền (không đổi nội dung)
- `git checkout dev && git merge origin/main` (kỳ vọng: không xung đột, không đổi cây).
- Kiểm tra: `git diff origin/main --stat` chỉ còn phần việc của ta.

### PR-1 — Luật chơi & tài liệu (rủi ro thấp, không ảnh hưởng build)
- `AGENTS.md`, `.clinerules`, `PLAN_NEN_MONG_Tu_Vung_TOEIC.md`, plan này, `docs/adr/004–008`, `docs/design/`, `docs/audit-*`, `docs/changelog-data.md`, `docs/url-inventory-*.txt`, `memory-bank/*`.
- Chuyển plan Speaking cũ vào `docs/archive/` (di chuyển file; chưa xóa `synonyms.md`, `vocabulary.md`, ảnh tham chiếu — để PR-5).
- Cổng: Hugo build y nguyên (chỉ markdown); đọc lại link nội bộ.

### PR-2 — **Lõi pivot (nguyên khối, chia nhiều commit để dễ review)**
Gồm F0→F3, vì dữ liệu v3, validator, template và redirect phụ thuộc lẫn nhau:
1. `data/levels.yaml`, `topics.yaml`, `sources.yaml`, `schemas/*.v3.json`.
2. Migrate 213 từ sang schema v3 + `data/quotes/` (12 file) + `content/sets/*`, `scripts/migrate/*`.
3. `scripts/validate/validate.py` (V1–V14), `test_validate.py`, `check_urls.py`.
4. `hugo.yaml` (taxonomy `topic`/`level`, menu 5 mục), `layouts/`, `assets/css/extended/`, `assets/js/`, `content/*`.
5. `scripts/build/gen_redirects.py` + `static/_redirects` (89 quy tắc) + `.github/workflows/ci.yml`.
- Cổng (bắt buộc xanh): validate 0 lỗi · `test_validate.py` OK · hugo sạch · `gen_redirects.py --check` · `check_urls.py` 0 URL chết (295 URL, 64 qua redirect).
- Kiểm tra trên **Cloudflare Pages preview** của PR: mở thật bằng điện thoại ở `/`, `/glossary/`, 1 trang từ, `/collocations/`, `/quotes/`, `/search/`; thử vài URL cũ (`/parts/...`, `/topics/...`) phải chuyển hướng đúng. Đã có kiểm tra không tràn ngang 360/320px bằng Edge headless; **chưa thử** trên iOS/Android/WebView TikTok — làm ở bước này.
- Điều kiện chặn merge: xác nhận redirect trên preview hoạt động (Cloudflare `_redirects` chỉ chạy trên Pages, không chạy ở `hugo server`).

### PR-3 — Công cụ nhập liệu + lô pilot (ẩn)
- `scripts/import/import_batch.py`, `sources/batches/_template.yaml`, `001-foundation-pilot.yaml` (10 từ `ai_draft`), `scripts/levels/*`, `scripts/ipa/check_cmudict.py`, `sources/raw/README.md`, `content/words/_content.gotmpl` (bỏ qua `ai_draft`).
- Lưu ý: PR này **phải đi cùng hoặc sau PR-2** (importer đọc schema v3).
- Cổng: như PR-2; thêm kiểm tra `public/words/price/` **không** tồn tại.

### PR-4 — Lô nháp hàng loạt 3.867 từ TSL/NGSL (ẩn) — **chờ quyết định, xem §6**
- `data/lexicon/*` (+3.867 file; toàn bộ `data/lexicon/` ≈ 3,3 MB), `sources/batches/002-tsl-ngsl-drafts.yaml`, `sources/batches/work/out/*.jsonl`, `scripts/import/make_chunks.py`, `merge_chunks.py`, `scripts/levels/wordlists.py`, `data/sources.yaml` (license TSL/NGSL), `docs/freq-coverage-report.csv`, `docs/adr/005–006` (cập nhật).
- Cổng: validate 0 lỗi (thời gian chạy < 2 phút) · hugo ~14 s · **đúng 213 trang `/words/<id>/`** · `search-index.json` không chứa từ nháp (kích thước không đổi so với trước) · không trang nào có `review_status` ngoài `ai_cross_checked`/`human_verified`.
- Chia nhỏ nếu repo quá nặng: tách theo chữ cái hoặc theo chunk (30 chunk × ~130 từ) — nhưng không cần cho build.

### PR-5 — Dọn dẹp xóa file cũ (sau khi PR-2 chạy ổn trên production ≥ 1–2 ngày)
- Xóa: `vocabulary.md`, `synonyms.md`, `ref_vocabularies_style*.png`, `scripts/add_lexicon_*.py`, shortcode cũ (`practice`, `tiktok`, `words`), `layouts/words/list.html`, `data/quotes.yaml`, các plan Speaking còn ở gốc.
- Trước khi xóa: `grep` toàn repo xem còn tham chiếu không; `sources.yaml` có mã `vocabulary-md`/`synonyms-md` (nguồn nội bộ) — giữ mã, chỉ xóa file (hoặc chuyển vào `docs/archive/`).
- Cổng: build + `check_urls.py`.

## 5. Rủi ro & cách giảm

| Rủi ro | Mức | Giảm thiểu |
| :--- | :--- | :--- |
| Đổi cấu trúc URL làm 404 (SEO, link TikTok cũ) | Cao | Redirect sinh tự động + `check_urls.py` bắt buộc 0 chết; kiểm tra trên preview; theo dõi 404 sau deploy |
| Trang từ nháp lộ ra công khai (đã suýt xảy ra: `needs_review` có trang) | Cao | Bản nhập hàng loạt luôn `ai_draft`; **thêm test CI**: đếm trang `/words/` = số mục `ai_cross_checked`/`human_verified` (xem §7) |
| Giấy phép CC BY-SA của TSL/NGSL (dữ liệu phái sinh: lemma + band tạm) | Trung bình | Quyết định Q6 trước PR-4; ghi công ở `/methodology/`; không commit file gốc |
| PR-2 quá lớn khó review | Trung bình | Chia commit theo 5 bước ở trên; review theo commit |
| `main` vỡ giữa chừng | Cao | Mỗi PR build xanh độc lập; rollback bằng `git revert <merge-commit>` |
| Nội dung nháp sai (nghĩa/IPA) | Thấp (ẩn) | Không hiển thị; tiền tố `[CẦN KIỂM TRA]`; duyệt theo lô nhỏ (xem §8) |
| Tìm kiếm/glossary chậm khi dữ liệu lớn | Thấp | Chỉ từ đã duyệt vào index; đo lại khi vượt ~1.500 từ |

## 6. Cần bạn quyết định trước khi thực hiện

1. **Q6 — giấy phép nội dung web**: `all rights reserved` hay CC BY-SA? (ảnh hưởng PR-4 vì dữ liệu phái sinh từ TSL/NGSL).
2. **Có đưa 3.867 bản nháp vào `main` không** (PR-4)? Lựa chọn: (a) có, ẩn hoàn toàn; (b) giữ ở nhánh riêng `data/drafts` đến khi có người duyệt; (c) chỉ đưa các lô đã duyệt.
3. **Ai bấm commit/push/PR?** Sandbox của tôi chặn git ghi; tôi chỉ chạy được khi bạn cho phép chạy ngoài sandbox. Nếu đồng ý, tôi sẽ soạn commit + mô tả PR theo đúng AGENTS.md (đã làm gì / kiểm tra thế nào / điều chưa chắc).
4. **Tên miền & deploy**: `baseURL` hiện `https://glory-tiktok.pages.dev/` — xác nhận Cloudflare Pages build command là `hugo --gc --minify` và biến `HUGO_VERSION=0.167.0`.

## 7. Bổ sung cần làm trước PR-2/PR-4 (nhỏ)

- Thêm vào CI một bước kiểm tra "không lộ bản nháp": sau `hugo`, đếm thư mục `public/words/*` và so với số mục đã duyệt trong `data/lexicon/`; fail nếu lệch.
- Thêm `pip install cmudict` vào CI **chỉ khi** muốn V6 chạy (hiện bỏ qua nếu thiếu).
- Ghi chú trong PR-2: 32 ghi chú còn nhắc "Part N" (audit #10) — chưa sửa, cần người duyệt.

## 8. Sau khi lên `main` (vận hành)

- **Quy trình xuất bản từ vựng**: reviewer lấy ~50 mục `ai_draft` → đối chiếu IPA/nghĩa độc lập (CMUdict, từ điển, Ngram/SkELL) → nâng `ai_cross_checked`/`human_verified` → PR nhỏ → merge → tự có trang. Mỗi PR một lô, chạy đủ cổng.
- Hệ số đo: số từ đã duyệt theo band; tỷ lệ `[CẦN KIỂM TRA]`; 404 trong log Cloudflare 7 ngày đầu.
- Theo dõi: Lighthouse mobile (LCP < 2,5 s trên 4G), thử thật trong WebView TikTok.

## 9. Checklist thực hiện mỗi PR

- [ ] Nhánh con tạo từ `main` mới nhất
- [ ] `python scripts/validate/validate.py` → 0 lỗi
- [ ] `python scripts/validate/test_validate.py` → OK
- [ ] `hugo --gc --minify` → sạch
- [ ] `python scripts/build/gen_redirects.py --check`
- [ ] `python scripts/validate/check_urls.py` → 0 chết
- [ ] Preview Pages mở được trên điện thoại
- [ ] Mô tả PR: đã làm gì / kiểm tra thế nào / điều chưa chắc chắn
- [ ] Squash merge → xác nhận deploy production → ghi vào `docs/changelog-data.md` nếu đổi dữ liệu
