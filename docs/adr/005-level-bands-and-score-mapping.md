# ADR 005: Thang điểm & phân tầng từ vựng (thay phần ánh xạ điểm của ADR-001)

- **Trạng thái:** Accepted một phần — ngưỡng tần suất **chưa chốt** (chờ dữ liệu TSL/CEFR-J)
- **Ngày:** 2026-10-10

## 1. Bối cảnh
ADR-001 cấm dùng nhãn điểm như chuẩn chính thức, nhưng 133/213 mục vẫn ghi `basis: "TOEIC 650/700/750+/800+"`. Ngoài ra `band` trùng khớp 100% với `cefr` (suy cơ học), và chưa có tầng cho người mới.

## 2. Quyết định
- 4 tầng: `foundation` (A2), `core` (B1), `target` (B2), `advanced` (C1). Định nghĩa tại `data/levels.yaml`.
- Khoảng điểm hiển thị đọc từ `data/levels.yaml` (không viết cứng). Số liệu dựa trên hướng dẫn ánh xạ CEFR của ETS.
- `level.basis` là **danh sách mã nguồn** trong `data/sources.yaml`. Chỉ ghi nguồn đã thật sự dùng.
- Thuật toán gán band (`scripts/levels/assign_band.py`): CEFR của từ (tín hiệu A) + thứ hạng tần suất TSL/BSL/NGSL (tín hiệu B); đồng thuận → gán; lệch ≥ 1 tầng hoặc thiếu tín hiệu → `needs_review`.

## 3. Mâu thuẫn / điều chưa xác minh (AGENTS.md quy tắc 11)
- **Chưa đối chiếu được văn bản gốc ETS**: URL thử truy cập trả 404 ngày 2026-10-10; bảng ánh xạ lấy từ nguồn thứ cấp. `data/levels.yaml` có cờ `verified_primary: false` và web hiển thị chú thích tương ứng.
- **Chưa có tệp danh sách TSL/NGSL/CEFR-J** trong repo, nên chưa chạy được thuật toán. Thực hiện trong giai đoạn tiếp theo: đặt tệp vào `sources/wordlists/` (kèm giấy phép), chạy `assign_band.py`, rồi chốt ngưỡng tần suất vào mục 4 của ADR này.

## 4. Ngưỡng tần suất
_Chưa chốt._ Cập nhật 2026-10-11 (đã tải TSL 1.2 + NGSL 1.2, xem ADR-006 §5 và `docs/freq-coverage-report.csv`):

- TSL và NGSL là hai danh sách **rời nhau** (giao = 0), mỗi danh sách có thang hạng riêng → không có một ngưỡng `freq_rank_max` chung. Nếu dùng, ngưỡng phải khai báo **theo từng danh sách** và `assign_band.py` phải được sửa tương ứng.
- Cả hai chỉ cho **tần suất**, không cho cấp độ điểm. Chưa có nguồn công bố nào gắn tần suất với CEFR/điểm TOEIC bằng phương pháp kiểm chứng được. Vì vậy tần suất chỉ là tín hiệu B hỗ trợ; tín hiệu A (CEFR của từ, ví dụ CEFR-J) vẫn chưa có và giấy phép chưa kiểm tra.
- Quan sát (không dùng để đổi band): trong 223 mục, 10/10 từ `foundation` nằm trong NGSL; 101/105 từ đơn của `core` nằm trong TSL hoặc NGSL; 75/93 của `target`; chỉ 4/13 của `advanced` (9 từ như *remuneration*, *severance*, *tariff* nằm ngoài cả hai danh sách). Xu hướng "band cao → hiếm hơn" khớp với cảm nhận biên tập nhưng chưa phải bằng chứng cho từng từ.
- Đề xuất để thảo luận (chưa chấp nhận): chia nhóm theo khoảng hạng cố định của từng danh sách (ví dụ mỗi 400 từ đầu của TSL/NGSL), coi "không có trong cả hai danh sách" là tín hiệu hiếm; mọi từ lệch với band hiện tại chuyển `needs_review`, không tự đổi band.

## 5. Hệ quả với 213 mục hiện có
Chưa có cơ sở độc lập để đổi band, nên **giữ nguyên `band`/`cefr`**, nhưng sửa `basis` thành `[editorial]` (trung thực hơn nhãn "TOEIC 650…"). Tầng `foundation` hiện rỗng — cần bổ sung ở giai đoạn mở rộng dữ liệu.
