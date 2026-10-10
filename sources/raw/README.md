# sources/raw — danh sách ứng viên nội bộ

`vocabulary.md` và `synonyms.md` là **danh sách ứng viên nội bộ** (nguồn gợi ý từ để soạn), được chuyển từ thư mục gốc repo.

- Chúng **không phải nguồn kiểm chứng độc lập**: không được ghi vào `review.checked_by` hay `review.sources` như bằng chứng đã kiểm tra (xem `data/sources.yaml`, `independent: false`).
- Không dùng làm nội dung hiển thị trực tiếp; mọi mục từ phải đi qua `sources/batches/*.yaml` → `scripts/import/import_batch.py` → validator.
- Không thêm vào đây nội dung chép từ từ điển hoặc đề thi có bản quyền.
