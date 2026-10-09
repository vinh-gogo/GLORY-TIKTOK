# ADR 003: Lưu trữ Audio và Giới hạn nền tảng Cloudflare

- **Trạng thái:** Accepted
- **Ngày quyết định:** 2026-10-10
- **Tác giả:** AI Assistant & Team Glory 01

## 1. Bối cảnh
Khi website phát triển lên ~340 bài học với ~2.500 từ vựng và hàng nghìn câu ví dụ:
- Số lượng file audio phát âm (từ, collocations, câu ví dụ, bài thi mẫu) có thể lên đến hơn 10.000 file MP3.
- Cloudflare Pages có giới hạn tối đa 20.000 file tĩnh cho mỗi lần deploy (file count limit) và giới hạn kích thước repository khi commit lên Git.
- Việc commit file nhị phân (audio .mp3) trực tiếp vào git repo sẽ làm repo phình to nhanh chóng (bloated git repository), gây chậm chạp khi clone.

## 2. Quyết định
1. **Không commit file audio nhị phân vào Git repo.**
2. Toàn bộ file âm thanh được host độc lập trên **Cloudflare R2 Object Storage** với custom domain riêng: `audio.glory-tiktok.pages.dev`.
3. Trong kho dữ liệu `data/lexicon/` và `data/exam/`, các đường dẫn audio chỉ lưu dạng đường dẫn tương đối (vd: `audio: { us: "words/deadline-us.mp3" }`).
4. Shortcode `audio` và các audio player trên client sẽ tự động nối `baseURL` của R2 để phát trực tiếp với cơ chế lazy-loading.
5. Quản lý toàn bộ danh mục audio bằng một file manifest: `audio-manifest.json` ghi nhận hash, engine TTS và thời lượng.

## 3. Hệ quả
- Git repository giữ được kích thước siêu nhẹ (< 20MB) và tốc độ clone/build tức thì.
- Không bao giờ chạm giới hạn số lượng file deploy của Cloudflare Pages.
- Cloudflare R2 miễn phí băng thông ra (Zero Egress Fees), tối ưu chi phí vận hành ở mức 0đ.
