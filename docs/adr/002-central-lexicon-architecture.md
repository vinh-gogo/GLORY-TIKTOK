# ADR 002: Kiến trúc Kho từ vựng trung tâm (Central Lexicon)

- **Trạng thái:** Accepted
- **Ngày quyết định:** 2026-10-10
- **Tác giả:** AI Assistant & Team Glory 01

## 1. Bối cảnh
Ở phiên bản v1, toàn bộ thông tin từ vựng (IPA, loại từ, nghĩa, collocations, từ dễ nhầm) được khai báo trực tiếp trong front matter của từng file bài học `content/sets/set-xxx.md`.
Nhược điểm khi mở rộng lên 340+ bài học:
- Trùng lặp dữ liệu: một từ như `deadline` hay `schedule` xuất hiện ở nhiều set phải viết lại nhiều lần.
- Không thể tự động tạo Từ điển A–Z (`/glossary/`) hoặc sinh Flashcard SRS/Quiz một cách nhất quán.
- Khi sửa lỗi chính tả hay bổ sung ví dụ phải sửa ở nhiều file.

## 2. Quyết định
Tách biệt triệt để **Dữ liệu từ vựng** và **Nội dung bài học**:
1. Toàn bộ từ vựng được lưu trữ tại `data/lexicon/<initial>/<id>.yaml` (mỗi từ là 1 file độc lập, chuẩn `schemas/word.v2.json`).
2. Các bài học trong `content/sets/*.md` chỉ tham chiếu danh sách `id` của từ (vd: `words: [deadline, workload, commute]`).
3. Sử dụng Hugo Content Adapters (`content/words/_content.gotmpl`) để tự động tạo trang chi tiết `/words/<slug>/` trực tiếp từ kho `data/lexicon/`.
4. Duy trì tính tương thích ngược: Shortcode `words` chấp nhận cả danh sách `id` (v2) lẫn mảng object inline (v1).

## 3. Hệ quả
- Dữ liệu duy nhất (Single Source of Truth), quản lý phiên bản dễ dàng.
- Mở rộng quy mô lên hàng nghìn từ vựng mà không làm phình file Markdown của các bài học.
