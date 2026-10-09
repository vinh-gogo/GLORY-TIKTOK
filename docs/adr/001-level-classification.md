# ADR 001: Phân loại trình độ từ vựng (Level Classification System)

- **Trạng thái:** Accepted
- **Ngày quyết định:** 2026-10-10
- **Tác giả:** AI Assistant & Team Glory 01

## 1. Bối cảnh
Trước đây, các bài học gán nhãn tùy ý như `level: "TOEIC 550+"`. Tuy nhiên, Viện Khảo thí Giáo dục Hoa Kỳ (ETS) không ban hành bất kỳ danh sách từ vựng chính thức nào được gán cứng theo từng mốc điểm TOEIC. Việc gán nhãn như vậy có nguy cơ gây hiểu lầm cho người học rằng đây là danh mục chính thức của ETS.

## 2. Quyết định
Thay thế nhãn điểm cứng bằng hệ phân cấp chuẩn kép:
1. **`cefr` (Khung tham chiếu Châu Âu):** `A1, A2, B1, B2, C1, C2` dựa trên đối chiếu danh sách tần suất từ vựng học thuật/kinh doanh quốc tế (NGSL, CEFR-J).
2. **`band` (Phân tầng biên tập của Glory 01):**
   - `core`: Từ vựng nền tảng bắt buộc để đạt mức giao tiếp cơ bản (tương đương target 90–120).
   - `target`: Từ vựng và collocations giúp đạt mức thành thạo công sở chuẩn (tương đương target 130–160).
   - `advanced`: Từ vựng, collocations và sắc thái cao cấp (tương đương target 160+).
3. **`basis`:** Luôn ghi rõ cơ sở phân loại (vd: `"editorial"`, `"cefr-j"`).

## 3. Hệ quả
- Giao diện có thể hiển thị badge phân cấp rõ ràng, minh bạch cơ sở học thuật.
- Người học hiểu đúng bản chất là từ vựng ứng dụng theo nhóm năng lực chứ không phải đề thi công bố của ETS.
