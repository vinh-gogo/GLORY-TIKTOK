# ADR 008: Nhóm đồng nghĩa (synsets) tách khỏi mục từ

- **Trạng thái:** Accepted — giai đoạn chuyển tiếp
- **Ngày:** 2026-10-10

## 1. Bối cảnh
`synonyms` hiện là danh sách chuỗi rời trong từng mục từ (463 mục), không có ghi chú sắc thái và không liên kết thành nhóm.

## 2. Quyết định
- Thêm thực thể `Synset` tại `data/synsets/<id>.yaml` (schema `synset.v1.json`): các thành viên kèm `register`, `nuance_vi`, và câu "không thay thế được cho nhau".
- Mục từ có thêm trường `synsets: [id]` để tham chiếu.
- **Chuyển tiếp:** trường `synonyms` cũ **được giữ** (deprecated) cho tới khi synset tương ứng được viết và duyệt — tránh mất dữ liệu đang hiển thị. Migrate **không** tự sinh synset: ghi nhận xét sắc thái cần kiến thức ngôn ngữ đã kiểm chứng (AGENTS.md quy tắc 2).
- `/synonyms/` hiển thị hai phần: nhóm đồng nghĩa đã duyệt (nếu có) và bảng "đồng nghĩa theo từ" lấy từ `synonyms` cũ.

## 3. Hệ quả
- Giai đoạn mở rộng dữ liệu phải viết synset mới (mục tiêu 300) và gỡ `synonyms` cũ khi đã thay thế.
