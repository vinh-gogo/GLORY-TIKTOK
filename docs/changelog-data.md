# Nhật ký thay đổi dữ liệu

Ghi mọi thay đổi **ý nghĩa** của dữ liệu (đổi band, hạ/nâng trạng thái, đổi chủ đề, thêm/xóa mục). Mới nhất ở trên.

## 2026-10-11 — Lô pilot foundation + sửa redirect

- Thêm 10 mục foundation (`price, customer, order, service, payment, office, manager, report, meeting, email`) từ `sources/batches/001-foundation-pilot.yaml` qua `scripts/import/import_batch.py`. Trạng thái **`ai_draft`**: IPA, nghĩa, collocation do AI viết, `evidence: unverified`, **chưa có reviewer** → KHÔNG sinh trang `/words/<id>/` (`content/words/_content.gotmpl` bỏ qua `ai_draft`); set/quote/synset chỉ link tới từ có trang.
- Tổng: 213 từ đã xuất bản + 10 bản nháp ẩn. Band của 213 từ cũ không đổi.
- `data/topics.yaml legacy_map`: thêm `exam-skills: null` (URL cũ trước đó chết) → redirect về trang chủ chủ đề.
- `data/levels.yaml`: thêm `band_order` để template hiển thị band theo thứ tự foundation → advanced.
- `data/sources.yaml`: kiểm tra giấy phép CMUdict (BSD-style), Wiktionary (CC BY-SA 4.0); WordNet chỉ làm nguồn phụ (chưa kiểm tra được); xem ADR-006.
- Tải TSL 1.2 (1.250 mục) và NGSL 1.2 (2.809 mục), kiểm tra giấy phép CC BY-SA 4.0 trực tiếp trên trang nguồn; thêm `scripts/levels/wordlists.py` (`fetch/report/candidates`) và `docs/freq-coverage-report.csv`. **Không đổi band hay `level.basis` của bất kỳ mục nào**; 3.877 từ TSL/NGSL chưa có trong lexicon chỉ là danh sách việc (không nhập nội dung). Xem ADR-005 §4, ADR-006 §5.
- Nhập hàng loạt 3.867 từ TSL/NGSL (sources/batches/002-tsl-ngsl-drafts.yaml) ở trạng thái **i_draft, không có trang công khai**: IPA sinh từ CMUdict bằng quy tắc, band TẠM theo hạng tần suất (ADR-005 chưa chốt), nghĩa/từ loại/chủ đề/câu ví dụ do AI viết, chưa duyệt. Mục có nhiều cách đọc hoặc nghĩa mơ hồ có tiền tố [CẦN KIỂM TRA] trong review.reason. 10 từ không có trong CMUdict bị bỏ (xem sources/batches/work/skipped.csv khi tạo lại). Tổng data/lexicon: 4.090 mục (213 xuất bản + 3.877 nháp).

## 2026-10-10 — Migrate lexicon sang schema v3 (F2)

- 213 mục `data/lexicon/` → schema v3: gỡ `speaking_use` (lưu trữ ở `docs/archive/speaking/speaking_use.csv`), `level.basis` thành danh sách (`[editorial]`), `collocations[].evidence` thành đối tượng (`source: unverified` cho dữ liệu cũ), chủ đề ánh xạ theo `data/topics.yaml` (1–3/từ).
- **Band không đổi** ở mọi mục (core 106 / target 94 / advanced 13; foundation 0). Chưa chạy gán band lại vì chưa có danh sách tần suất độc lập.
- Không mục nào đổi `review.status`.
- `data/quotes.yaml` (12 định luật) tách thành `data/quotes/law-01..12.yaml`; trạng thái `ai_draft`, `origin: original`.
- 3 set trong `content/sets/` chuyển sang schema `set.v3` (chỉ front matter; bỏ `practice`, `series`, `parts`). Tóm tắt của set-002/013 bỏ cách nói “Part 2/Part 3”.
- URL không đổi: `/words/<id>/` (213 trang), `/sets/*`, `/001`, `/002`, `/013`. URL cũ của `topics`, `parts`, `tags`, `series`, `guides`, `/words/` được chuyển hướng (`static/_redirects`, sinh bởi `scripts/build/gen_redirects.py`; đối chiếu bằng `scripts/validate/check_urls.py`).
