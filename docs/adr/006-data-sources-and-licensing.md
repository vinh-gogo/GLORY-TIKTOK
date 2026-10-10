# ADR 006: Nguồn dữ liệu, giấy phép và ghi công

- **Trạng thái:** Proposed — chờ kiểm tra giấy phép từ văn bản gốc
- **Ngày:** 2026-10-10

## 1. Bối cảnh
Kho từ vựng cần danh sách ứng viên/tần suất, đối chiếu IPA, quan hệ đồng nghĩa và bằng chứng collocation. Mỗi nguồn có giấy phép khác nhau.

## 2. Quyết định
- Mọi nguồn được phép dùng nằm trong `data/sources.yaml`; validator chặn mã nguồn lạ.
- Từ điển có bản quyền (Oxford, Cambridge…): **chỉ đối chiếu**, không chép câu chữ (AGENTS.md quy tắc 3).
- `vocabulary.md`/`synonyms.md` là danh sách ứng viên nội bộ, **không** tính là nguồn đối chiếu độc lập.
- Danh sách TSL/BSL/NGSL: theo trang dự án NGSL là CC BY-SA 4.0 — cần ghi công trên `/methodology/`.

## 3. Kết quả kiểm tra giấy phép (2026-10-11)

| Nguồn | Kết quả | Mức xác minh |
| :--- | :--- | :--- |
| CMU Pronouncing Dictionary | Giấy phép dạng BSD; phải giữ thông báo bản quyền khi phân phối lại | Đã đọc văn bản gốc (cmusphinx/cmudict, tệp LICENSE) |
| Wiktionary | CC BY-SA 4.0 (trang Wiktionary:Copyrights khai báo rel=license) | Đã đọc trang gốc. Chỉ đối chiếu; chép nội dung sẽ kéo theo ShareAlike |
| Princeton WordNet 3.0 | Cho phép dùng/sao chép/phân phối không phí nếu giữ thông báo bản quyền và miễn trừ; không dùng tên Princeton để quảng bá | **Thứ cấp** (trang gốc trả 403; đọc qua kết quả tìm kiếm). Cần đọc bản gốc trước khi dùng dữ liệu |
| TSL 1.2 / NGSL 1.2 | CC BY-SA 4.0 — ghi rõ trên trang TSL và trang NGSL ("by Browne, C., Culligan, B. (and Phillips, J.) … Creative Commons Attribution-ShareAlike 4.0 International License"); tác giả ghi thêm "permissions beyond the scope of this license may be available" qua charlie-browne.com | **Đã đọc trực tiếp (2026-10-11)**. Tải thử 5 tệp TSL và 2 tệp NGSL (HTTP 200); đếm đúng 1.250 mục TSL và 2.809 mục NGSL |
| BSL | CC BY-SA 4.0 theo trang dự án | Chưa kiểm tra riêng; hiện chưa dùng |
| CEFR-J, Ngram, SkELL, LanguageTool, Oxford/Cambridge | Chưa kiểm tra | — |

## 4. Việc còn mở
- **ShareAlike:** chưa xác định danh sách từ của web có được xem là "tác phẩm phái sinh" hay không. Cần quyết định giấy phép nội dung của web (all rights reserved hay CC BY-SA…) **trước khi** nhập danh sách TSL/NGSL vào kho (câu hỏi Q6).
- Hoàn tất kiểm tra các nguồn ở dòng "chưa kiểm tra" trước khi dùng dữ liệu của chúng.
- Ghi công (attribution) trên /methodology/ cho mọi nguồn dữ liệu được dùng thật.

## 5. Đánh giá nguồn tần suất / từ vựng TOEIC (2026-10-11)

Không tìm thấy danh sách từ vựng TOEIC **theo mức điểm** do ETS công bố miễn phí. Phân loại các nguồn đã xem:

**Dùng được (đã xác minh, tải được):**
- **TSL 1.2** — 1.250 từ, xây từ kho ngữ liệu 1,5 triệu từ gồm giáo trình/đề luyện thi TOEIC; cùng NGSL phủ ~98,5% đề TOEIC gần nhất (tuyên bố của tác giả). Số liệu trên trang tổng quan (1.200 từ/99%) cũ hơn trang TSL 1.2 (1.250 từ/98,5%) → dùng số của bản 1.2, đã đếm đúng 1.250 mục. **TSL không phải danh sách do ETS công bố** — web không được ghi "danh sách chính thức của ETS".
- **NGSL 1.2** — 2.809 từ lõi tiếng Anh phổ thông. TSL và NGSL **rời nhau** (đã đối chiếu: giao = 0 từ); các từ rất thường như *manager*, *meeting* nằm trong NGSL, không nằm trong TSL → bắt buộc dùng cả hai.
- **BSL 1.2** (1.700 từ tiếng Anh thương mại, kho ngữ liệu 64 triệu từ): tùy chọn để mở rộng, không phải danh sách TOEIC; chưa tải.

**Chỉ tham khảo (không nhập dữ liệu):**
- Sách ETS Global/IIBC (1.500–1.800 từ, trả phí, bản quyền) — không sao chép.
- EnglishCentral (dựa trên TSL 2013, CC BY-SA) và gói R `list_toeic` (5 nhóm độ khó do tác giả tự đặt) — chỉ để hiểu cách người khác chia nhóm.

**Loại trừ:** `LEE-WHITE/toeic-vocab-tw` (Hugging Face; không nêu nguồn, phiên bản mâu thuẫn, có lỗi rõ như "dewer/dewest", "followingly" → có dấu hiệu do AI sinh, chưa duyệt); các app/danh sách thương mại không có nguồn; danh sách mang nhãn "ETS" trên Vocabulary.com không có bằng chứng liên quan tới ETS. Không đưa vào `data/sources.yaml`.

**Hệ quả kỹ thuật:** TSL/NGSL chỉ cho **thứ hạng tần suất**, không cho cấp độ điểm. Vì hai danh sách có thang hạng riêng nên không thể có một ngưỡng `freq_rank_max` chung như `assign_band.py` đang giả định (xem ADR-005 §4). Công cụ mới: `scripts/levels/wordlists.py` (`fetch` / `report` / `candidates`); tệp tải về không commit (CC BY-SA, xem `.gitignore`), báo cáo `docs/freq-coverage-report.csv` ghi công nguồn.
