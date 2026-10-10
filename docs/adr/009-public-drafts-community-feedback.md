# ADR 009: Công khai bản nháp từ vựng để cộng đồng đóng góp sửa đổi

- **Trạng thái:** Accepted
- **Ngày:** 2026-10-11

## 1. Bối cảnh
Trước đây, hệ thống chỉ xuất bản 213 từ đã được đối chiếu (`ai_cross_checked`, `human_verified`). Khoảng 3.877 từ vựng nhập từ TSL 1.2 và NGSL 1.2 được lưu ở trạng thái `ai_draft` và bị ẩn hoàn toàn (không tạo trang `/words/<id>/`). Người dùng yêu cầu đưa toàn bộ từ vựng vào website để người học có thể tra cứu và cộng đồng cùng đọc, đóng góp chỉnh sửa dần dần ("cứ để vô đi đọc từ từ rồi cộng đồng góp ý sửa từ từ").

## 2. Quyết định
1. **Sinh trang cho tất cả từ vựng:** Mọi mục từ trong `data/lexicon/` đều được sinh trang chi tiết `/words/<id>/`.
2. **Minh bạch trạng thái duyệt:**
   - Các từ chưa kiểm duyệt (`ai_draft`, `needs_review`) hiển thị huy hiệu **Nháp** (`.badge-draft`) trên thẻ từ ở mọi danh sách (Glossary A–Z, Tìm kiếm, Taxonomy).
   - Trang chi tiết hiển thị khung cảnh báo nổi bật: nêu rõ đây là bản nháp do AI soạn / IPA sinh từ CMUdict, có thể chưa chuẩn xác, khuyến khích đối chiếu và bấm nút **Báo lỗi** (liên kết tới GitHub Issue template đã điền sẵn mã từ).
3. **SEO & Chỉ mục tìm kiếm công cộng:**
   - Trang nháp có tham số `robotsNoIndex: true` và `sitemap: disable: true` để các công cụ tìm kiếm (Google, Bing) không lập chỉ mục nội dung chưa qua kiểm duyệt chất lượng.
4. **Tìm kiếm nội bộ & Từ điển A–Z:**
   - `/search-index.json` bao gồm cả các từ nháp (kèm cờ `d: 1`), cho phép người dùng tìm kiếm toàn bộ kho từ vựng.
   - Thẻ kết quả tìm kiếm và thẻ từ điển hiển thị huy hiệu "Nháp".
   - Danh sách `/glossary/` hiển thị tổng số từ và số lượng từ đã đối chiếu độc lập.
   - Các trang chủ đề và cấp độ giới hạn 120 thẻ đầu (ưu tiên từ đã đối chiếu) và dẫn link vào `/glossary/?band=...` hoặc `?topic=...` để tránh phình DOM.
5. **Hiệu năng điều hướng:**
   - Điều hướng từ trước/sau (`prev`/`next`) trên trang từ vựng sử dụng `.Weight` (O(1)) thay vì duyệt tuyến tính qua danh sách hơn 4.000 từ (tránh O(N^2) khi build).
6. **Bản quyền & Ghi công:**
   - Trang `/methodology/` bổ sung mục ghi công rõ ràng tới TOEIC Service List 1.2 và New General Service List 1.2 theo giấy phép CC BY-SA 4.0.

## 3. Hệ quả
- Số lượng trang của website tăng lên ~4.180 trang.
- Người dùng có thể tra cứu nhanh toàn bộ kho từ TOEIC cơ bản và nâng cao.
- Tránh được việc người học nhầm lẫn nội dung do AI soạn với nội dung đã được thẩm định nhờ hệ thống huy hiệu và cảnh báo rõ ràng.
