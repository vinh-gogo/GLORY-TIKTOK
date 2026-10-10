# Quy tắc cho AI làm việc trong repo GLORY-TIKTOK

1. Đọc `PLAN_NEN_MONG_Tu_Vung_TOEIC.md` (Mục 1, 3, 5, 6, 8) và `docs/adr/004-pivot-vocabulary-platform.md` trước khi sửa bất cứ thứ gì. (Plan Speaking cũ nằm ở `docs/archive/`, chỉ để tham chiếu.)
2. KHÔNG bịa dữ liệu. IPA/nghĩa/collocation không chắc chắn → đặt `review.status: needs_review` và ghi lý do. Không đoán.
3. KHÔNG sao chép đề thi ETS hoặc câu chữ từ điển có bản quyền. Viết nội dung gốc ("ETS-style").
4. KHÔNG đổi slug/URL/alias đã tồn tại. Nếu bắt buộc, thêm redirect trong `static/_redirects` và ghi ADR.
5. Mọi thay đổi dữ liệu phải qua `scripts/validate/validate.py`. Chạy `hugo --gc --minify` thành công trước khi báo hoàn thành.
6. Mọi thông số đề thi/thang điểm đọc từ `data/exam/*.yaml` và `data/levels.yaml` — không hard-code số giây hay số điểm ở nơi khác.
7. Tiếng Việt: dùng đủ dấu; thuật ngữ giữ tiếng Anh khi chuẩn (collocation, shadowing, prompt...).
8. Mỗi task một mục tiêu; mô tả: đã làm gì, kiểm tra thế nào, điều gì chưa chắc chắn.
9. Quyết định kiến trúc mới → viết ADR trong `docs/adr/`.
10. Không thu thập dữ liệu cá nhân; không upload ghi âm của người dùng khi chưa có cơ chế đồng ý rõ ràng.
11. Khi gặp mâu thuẫn giữa tài liệu này và nguồn chính thức (ETS), ưu tiên nguồn chính thức và ghi rõ mâu thuẫn.
