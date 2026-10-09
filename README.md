# Glory 01 – Website Đồng Hành Kênh TikTok TOEIC Speaking 🎙️

Website chính thức: **[https://glory-tiktok.pages.dev](https://glory-tiktok.pages.dev)**  
Kênh TikTok: **[@wbk.lqv](https://www.tiktok.com/@wbk.lqv)**

Nền tảng lưu trữ, tra cứu và luyện phản xạ từ vựng TOEIC Speaking theo từng video TikTok, xây dựng trên **Hugo (bản extended)** cùng giao diện **PaperMod**.

---

## 🌟 Điểm nổi bật

- **Tối ưu Mobile (Link Bio TikTok):** Giao diện ProfileMode tại trang chủ hoạt động hoàn hảo khi người xem bấm vào link bio từ TikTok.
- **Thẻ từ vựng chuẩn thi (`{{< words >}}`):**
  - **Từ chính & Loại từ (POS):** Danh từ, Động từ, Tính từ,... kèm tiếng Việt.
  - **Phiên âm quốc tế IPA:** Chuẩn giọng Mỹ / Anh.
  - **Level mục tiêu trong TOEIC:** Phân cấp rõ ràng (550+, 650+, 700+, 850+).
  - **Từ dễ nhầm (Mặt chữ / Phát âm):** Cảnh báo các cặp từ phát âm hoặc viết na ná nhau (vd: *deadline* vs *timeline*, *commute* vs *compute*).
  - **Phân biệt sắc thái nghĩa:** Tránh nhầm lẫn ngữ cảnh sử dụng (vd: *deadline* vs *due date*, *reschedule* vs *postpone*).
  - **Collocations ghi điểm:** Mọi cụm từ đều có dịch nghĩa tiếng Việt chi tiết (vd: *meet a deadline* ➔ *kịp hạn chót*).
  - **Ví dụ phản xạ song ngữ (EN - VI):** Câu ví dụ thực tế kèm bản dịch tiếng Việt chuẩn xác.
- **Phân loại thông minh (Taxonomies):**
  - **Chủ đề (`/topics/`):** Gom nhóm từ vựng theo chủ đề (công việc, đời sống, du lịch, mua sắm,...).
  - **Dạng bài (`/parts/`):** Phân loại theo 5 dạng câu hỏi TOEIC Speaking chuẩn ETS (`read-aloud`, `describe-picture`, `respond-to-questions`, `respond-with-info`, `express-opinion`).
- **Tìm kiếm tức thì (`/search/`):** Tìm kiếm không cần server (PaperMod + Fuse.js), tra cứu nhanh từ vựng, collocations và bài học.
- **Tốc độ cực nhanh & Chi phí 0đ:** Tĩnh hoàn toàn, build siêu nhanh với Hugo và deploy miễn phí qua Cloudflare Pages.

---

## 🚀 Hướng dẫn phát triển cục bộ (Local Development)

### 1. Yêu cầu cài đặt
- **Hugo Extended** phiên bản >= `0.160.0` (Khuyên dùng `0.167.0`).
- **Git**.

### 2. Tải mã nguồn kèm Submodules
```bash
git clone --recurse-submodules https://github.com/vinh-gogo/GLORY-TIKTOK.git
cd GLORY-TIKTOK
```

Nếu đã clone repo mà chưa tải theme:
```bash
git submodule update --init --recursive
```

### 3. Chạy server phát triển
```bash
hugo server -D
```
Truy cập trình duyệt tại địa chỉ: `http://localhost:1313/`

---

## ✍️ Quy trình thêm bài học mới (Chỉ 1 phút)

Mỗi bài học tương ứng với một video TikTok. Để tạo bài học mới, chạy lệnh:

```bash
hugo new sets/set-014.md
```

Hệ thống sẽ tự động tạo file tại `content/sets/set-014.md` với khung chuẩn đầy đủ các trường:

```yaml
---
title: "Set 014 – Từ vựng chủ đề mua sắm & hoàn tiền"
date: 2026-10-10
draft: false
summary: "Các từ vựng và collocations về mua sắm, đổi trả và hoàn tiền trong TOEIC Speaking."
topics: ["shopping"]
parts: ["respond-to-questions"]
tags: ["shopping", "speaking-part-3"]
tiktok: "https://www.tiktok.com/@glory01/video/1234567890"
aliases: ["/014"] # Người xem gõ nhanh: glory-tiktok.pages.dev/014
words:
  - word: "refund"
    pos: "Danh từ (n.) / Động từ (v.)"
    ipa: "/ˈriːfʌnd/"
    level: "TOEIC 550+"
    meaning: "Khoản tiền hoàn lại; (v) hoàn tiền cho khách hàng"
    confused_words:
      - word: "refuse"
        ipa: "/rɪˈfjuːz/"
        meaning: "Từ chối"
        difference: "Tránh nhầm âm đuôi -fund /fʌnd/ và -fuse /fjuːz/"
    confusing_meanings:
      - word: "exchange"
        meaning: "Đổi sang món hàng khác (không nhận lại tiền mặt)"
        difference: "Refund là lấy lại tiền; exchange là đổi lấy sản phẩm thay thế"
    collocations:
      - phrase: "full refund"
        meaning: "Hoàn lại toàn bộ 100% số tiền"
      - phrase: "request a refund"
        meaning: "Yêu cầu được hoàn tiền"
      - phrase: "eligible for a refund"
        meaning: "Đủ điều kiện nhận lại tiền"
    example:
      en: "Customers are eligible for a full refund within 30 days of purchase."
      vi: "Khách hàng đủ điều kiện nhận lại toàn bộ tiền trong vòng 30 ngày kể từ ngày mua."
---

{{< tiktok >}}

{{< words >}}

## 🎙️ Luyện tập phản xạ Speaking (Practice)

### Câu hỏi mẫu (Prompt)
> **Question:** ...

### Gợi ý phản xạ (Sample Response)
> **Response:** ...
```

---

## ☁️ Hướng dẫn Triển khai lên Cloudflare Pages (`glory-tiktok.pages.dev`)

1. **Đẩy mã nguồn lên GitHub:**
   ```bash
   git add .
   git commit -m "feat: complete website setup for TikTok Glory 01"
   git push origin main
   ```

2. **Kết nối Cloudflare Pages:**
   - Đăng nhập vào [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > tab **Pages** > **Connect to Git**.
   - Chọn kho lưu trữ `vinh-gogo/GLORY-TIKTOK`.

3. **Cài đặt thông số Build (Build settings):**
   - **Project name:** `glory-tiktok`
   - **Framework preset:** `Hugo`
   - **Build command:** `hugo --gc --minify`
   - **Build output directory:** `public`

4. **Biến môi trường (Environment variables):**
   Thêm biến môi trường:
   - `HUGO_VERSION`: `0.146.0` (hoặc `0.167.0`)

5. **Trang web trực tiếp:**
   - Sau khi hoàn thành build, trang web hoạt động tại: **`https://glory-tiktok.pages.dev`**

---

## 📂 Cấu trúc thư mục

```
GLORY-TIKTOK/
├── archetypes/
│   └── sets.md                     # Khung mẫu sinh tự động cho set bài học mới
├── assets/
│   └── css/extended/custom.css     # CSS tùy biến thẻ từ vựng & tối ưu di động
├── content/
│   ├── about.md                    # Giới thiệu kênh Glory 01 & lưu ý bản quyền ETS
│   ├── search.md                   # Trang tìm kiếm tức thì
│   ├── sets/                       # Các set bài học từ vựng theo video TikTok
│   └── guides/                     # Cẩm nang 5 dạng bài thi TOEIC Speaking
├── layouts/
│   └── shortcodes/
│       ├── words.html              # Shortcode render thẻ từ vựng chi tiết
│       └── tiktok.html             # Shortcode nhúng video & liên kết mở app TikTok
├── static/
│   └── images/avatar.svg           # Ảnh đại diện kênh Glory 01
├── themes/PaperMod/                # Git submodule theme PaperMod
├── hugo.yaml                       # File cấu hình trung tâm (baseURL: glory-tiktok.pages.dev)
└── README.md                       # Tài liệu hướng dẫn sử dụng
```
