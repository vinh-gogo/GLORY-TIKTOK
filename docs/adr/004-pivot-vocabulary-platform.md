# ADR 004: Đổi trọng tâm sang web học từ vựng TOEIC

- **Trạng thái:** Accepted (theo yêu cầu triển khai `PLAN_NEN_MONG_Tu_Vung_TOEIC.md`)
- **Ngày:** 2026-10-10

## 1. Bối cảnh
Web được dựng theo hướng "TOEIC Speaking theo video" (đồng hồ bấm giờ, dạng bài Q1–Q11, series, parts). Dữ liệu thực tế là từ vựng kinh doanh kiểu TOEIC Listening & Reading. Mục tiêu mới: web học **từ vựng, collocations, từ đồng nghĩa, câu nói hay**, ưu tiên điện thoại (người dùng đến từ TikTok).

## 2. Quyết định
- Hướng web: từ vựng TOEIC (thang điểm tham chiếu Listening & Reading 10–990).
- Gỡ khỏi giao diện: shortcode `practice` (đồng hồ Speaking), trang `guides`, taxonomy `parts`/`series`/`tags`, nhúng video TikTok, trang About trang trí.
- Giữ nguyên: URL `/words/<slug>/`, `/glossary/`, `/quotes/`, `/search/`, `/about/`, `/sets/*` và alias `/001`, `/002`, `/013`.
- Mã nguồn bị gỡ được lưu tại `docs/archive/speaking/` (không xóa lịch sử Git).
- `data/exam/toeic-speaking.yaml` được **giữ lại** cho giai đoạn Speaking sau này.
- Hai plan cũ chuyển vào `docs/archive/`.

## 3. Hệ quả
- Mọi URL cũ bị gỡ đều có 301 trong `static/_redirects` (sinh bằng `scripts/build/gen_redirects.py`).
- `AGENTS.md` được cập nhật: quy tắc 1 trỏ tới plan mới, quy tắc 6 mở rộng sang `data/levels.yaml`.
- Tính năng Speaking (đồng hồ thi, ghi âm, mock test) tạm dừng, không bị xóa khỏi lộ trình dài hạn.
