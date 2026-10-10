# Kiểm toán lexicon v3 — 2026-10 (T2.7)

> Phạm vi: 213 mục trong `data/lexicon/` sau khi migrate sang schema v3 bằng `scripts/migrate/v2_to_v3.py`.
> Kiểm toán này **ghi nhận thực trạng**, không nâng trạng thái duyệt của bất kỳ mục nào.

## 1. Kết quả tự động

| Chỉ số | Giá trị |
| :--- | :--- |
| Mục đã migrate qua `schemas/word.v3.json` | **213 / 213** |
| `python scripts/validate/validate.py` | 0 lỗi, ~730 cảnh báo (xem mục 3) |
| Band: foundation / core / target / advanced | 0 / 106 / 94 / 13 |
| Trạng thái duyệt | 213 × `ai_cross_checked` (không mục nào `human_verified`) |
| Collocations / synonyms (legacy) / ví dụ | 709 / 463 / 215 |
| Chủ đề (1–3 mỗi từ) | 1 chủ đề: 99 · 2 chủ đề: 99 · 3 chủ đề: 15 |
| Câu nói hay | 12 (`data/quotes/law-*.yaml`), tất cả `ai_draft` |
| Synset (nhóm đồng nghĩa có sắc thái) | 0 |

Phân bố chủ đề (số lượt gắn): general-business 109, offices 72, personnel 42, travel 26, finance-budgeting 26, purchasing 24, manufacturing 20, housing-property 13, technical-areas 4, daily-life 4, entertainment 1, health 1.

## 2. Những gì chưa được chứng minh (cần người duyệt)

1. **`level.basis` = `[editorial]` cho cả 213 mục.** Band/CEFR giữ nguyên như cũ (trùng khớp 100% với CEFR cũ), chưa đối chiếu với danh sách tần suất độc lập (TSL/BSL/NGSL) hay CEFR-J — các danh sách này **chưa có trong repo** và giấy phép chưa kiểm tra (ADR-006). Ngưỡng tần suất chưa chốt (ADR-005). `scripts/levels/assign_band.py` đã sẵn sàng, hiện báo `no_signal` cho 213 mục.
2. **Tầng `foundation` rỗng.** Cần soạn mới qua pipeline nhập lô, không thể suy ra từ dữ liệu hiện có.
3. **709 collocation chưa có bằng chứng cụ thể.** Dữ liệu cũ chỉ ghi “corpus” chung chung → chuyển thành `evidence.source: unverified` kèm ghi chú legacy (cảnh báo V11). Không có collocation nào được gán nguồn mới trong đợt này.
4. **Nguồn đối chiếu ghi trong `review`.** 201/213 mục có `oxford-ref` trong `checked_by`/`sources`, các mục còn lại ghi nguồn khác (cmudict, mô hình AI…). Repo **không có bằng chứng** những gì đã được đối chiếu ở từng mục, nên đây là *tuyên bố ghi sẵn nhưng không kiểm chứng được*. Validator V10 chấp nhận để không hạ hàng loạt trạng thái; quyết định hạ trạng thái hay không thuộc về người duyệt (câu hỏi mở).
5. **IPA chưa chạy V6 (CMUdict).** Gói `cmudict` chưa được cài trong môi trường này; `scripts/ipa/check_cmudict.py` đã kiểm thử với từ điển mẫu nhỏ nhưng chưa chạy trên dữ liệu thật. Kiểm tra chỉ là heuristic (số âm tiết + vị trí trọng âm).
6. **23 tham chiếu `confused_words`/`highlights` trỏ ra ngoài lexicon** (V3 cảnh báo); 22 cụm highlight của Câu nói hay chưa có mục từ tương ứng (ví dụ cần thêm qua pipeline).
7. **Liên kết TikTok của 3 set là placeholder** (`.../video/1234567xxx`). Template không hiện nút “Xem video” cho link kiểu này, thay bằng link kênh.
8. **Bảng điểm ETS ↔ CEFR** trong `data/levels.yaml` mới đối chiếu qua nguồn thứ cấp (ets.org trả 404 khi truy cập 2026-10-10): `verified_primary: false`. Danh sách nhóm chủ đề ETS trong `data/topics.yaml` cũng chưa đối chiếu văn bản gốc.
9. **Ánh xạ chủ đề cũ → mới** của `events`, `education`, `media` đang gộp tạm (đánh dấu “CẦN DUYỆT” trong `data/topics.yaml`).
10. **32 dòng ghi chú trong `data/lexicon/` còn nhắc “Part N” của đề thi** (ví dụ `annual`, `applicant`, `assemble`, `background`, `cargo`, `crucial`, `delegate`…). Các ghi chú này có vẻ trộn cách đánh số Part của Speaking với Listening/Reading (ví dụ “Part 5 (Express an Opinion)” là cách gọi của Speaking) và **chưa được đối chiếu với ETS**, nên có thể không khớp bài thi L&R. Chưa sửa trong đợt này để không tự ý viết lại nội dung biên tập; cần người duyệt viết lại hoặc bỏ các tham chiếu Part (tìm bằng `Part [0-9]` trong `data/lexicon`).

## 3. Cảnh báo validator (không chặn build)

- V11 ~739: collocation chưa có bằng chứng (709 legacy + 30 từ lô pilot `ai_draft`).
- V3 ~23: tham chiếu tới từ chưa có trong lexicon; + 1 link TikTok placeholder.
- V7/V8: vài mục.
- V6: bỏ qua (thiếu CMUdict).

**Lô pilot (2026-10-11):** 10 từ foundation (`price`, `customer`, `order`, `service`, `payment`, `office`, `manager`, `report`, `meeting`, `email`) nhập bằng `import_batch.py` ở trạng thái `ai_draft` (AI viết, chưa ai duyệt). Chúng **không có trang `/words/<id>/`** cho tới khi reviewer nâng trạng thái. Hiện: 213 từ xuất bản + 10 bản nháp ẩn.

**Bộ test validator:** `scripts/validate/test_validate.py` (22 test, chạy trong CI); test V6 bị bỏ qua nếu chưa cài `cmudict`.

## 4. Việc tiếp theo đề xuất

1. Người duyệt quyết định chính sách cho mục 2.4 (giữ / hạ về `ai_draft` các mục chỉ có tuyên bố không kiểm chứng).
2. Tải TSL/BSL/NGSL + CEFR-J vào `sources/wordlists/` **sau khi** kiểm tra giấy phép, chạy `assign_band.py`, chốt ngưỡng ở ADR-005.
3. Cài `cmudict`, chạy `check_cmudict.py`, xử lý các mục `mismatch`.
4. Soạn lô đầu cho `foundation` bằng `scripts/import/import_batch.py` (mục mới mặc định `ai_draft`, không hiện trên web).
