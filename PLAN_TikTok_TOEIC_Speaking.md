# Kế hoạch & Trạng thái Dự án Web Kênh TikTok TOEIC Speaking (Glory 01)

Cập nhật lần cuối: **10/10/2026** · Kênh TikTok: **[Glory 01 (@wbk.lqv)](https://www.tiktok.com/@wbk.lqv)** · Website: **[https://glory-tiktok.pages.dev](https://glory-tiktok.pages.dev)**

---

## 1. Mục tiêu và vai trò của web

Web là kho lưu trữ có thể tìm lại và ôn luyện được; TikTok là nơi thu hút người xem mới.

- **Vấn đề của TikTok:** Video trôi theo feed thuật toán, người xem khó tìm lại bài cũ, không có bảng từ đầy đủ phiên âm, sắc thái nghĩa, collocations để lưu, in hay ôn tập phản xạ.
- **Web giải quyết:**
  - **Một link duy nhất trong bio** (`glory-tiktok.pages.dev`) dẫn tới toàn bộ các set bài học.
  - **Mỗi video có một trang riêng:** Đầy đủ từ chính, loại từ (POS), phiên âm IPA, level TOEIC, từ dễ nhầm chữ/âm, từ dễ nhầm nghĩa, collocations song ngữ và ví dụ phản xạ song ngữ.
  - **Tra cứu nhanh:** Gom theo chủ đề (`/topics/`), theo 5 dạng bài thi chuẩn ETS (`/parts/`), hoặc tìm kiếm tức thì (`/search/`).
  - **Luyện nói tại chỗ:** Dàn ý trả lời mẫu (Sample Response) cho các phần thi Speaking Part 2, Part 3, Part 5.

---

## 2. Bảng theo dõi tiến độ các trang & Tính năng

| Trang | Đường dẫn | Nội dung & Vai trò | Trạng thái hiện tại |
| :--- | :--- | :--- | :--- |
| **Trang chủ** | `/` | ProfileMode tối ưu mobile (Avatar Glory 01, link TikTok bio, nút điều hướng) |  **Hoàn thành (Live)** |
| **Bộ bài học** | `/sets/` | Danh sách các set bài học theo video; mỗi set có thẻ từ và video nhúng |  **Hoàn thành (Live)** |
| **Chủ đề** | `/topics/` | Phân loại từ vựng theo chủ đề đời sống, công việc, mua sắm,... |  **Hoàn thành (Live)** |
| **Dạng bài** | `/parts/` | Phân loại theo 5 dạng câu hỏi TOEIC Speaking chuẩn ETS |  **Hoàn thành (Live)** |
| **Hướng dẫn** | `/guides/` | Cẩm nang chiến thuật 5 dạng bài thi, tiêu chí chấm điểm ETS |  **Hoàn thành (Live)** |
| **Tìm kiếm** | `/search/` | Tìm kiếm tức thì không cần server (PaperMod + Fuse.js) |  **Hoàn thành (Live)** |
| **Giới thiệu** | `/about/` | Giới thiệu kênh Glory 01, liên hệ và lưu ý miễn trừ trách nhiệm ETS |  **Hoàn thành (Live)** |
| **Rút gọn URL** | `/001`, `/013` | Aliases giúp người xem TikTok gõ nhanh từ màn hình điện thoại |  **Hoàn thành (Live)** |
| **Tra từ A–Z** | `/glossary/` | Bảng tra cứu mọi từ đã dạy gom tự động từ các set bài học | ⏳ *Dự kiến v2* |

Menu chính trên thanh điều hướng gồm 6 mục: **Bộ bài học, Chủ đề, Dạng bài, Hướng dẫn, Tìm kiếm, Giới thiệu**.

---

## 3. Mô hình nội dung chi tiết (Rich Vocabulary Schema)

Mỗi video clip TikTok tương ứng với một file Markdown đánh số 3 chữ số (`content/sets/set-013.md`) để URL luôn ổn định (`/sets/set-013/` và alias `/013`).

### 3.1. Tiêu chuẩn dữ liệu bắt buộc cho mỗi từ vựng
Tất cả các thành phần trong từ vựng **đều bắt buộc kèm giải nghĩa tiếng Việt**:
1. **`word`**: Từ chính tiếng Anh.
2. **`pos`**: Loại từ kèm tiếng Việt (vd: `Danh từ (n.)`, `Động từ (v.)`, `Tính từ (adj.)`, `Cụm từ (phr.)`).
3. **`ipa`**: Phiên âm quốc tế chuẩn (vd: `/ˈdedlaɪn/`).
4. **`level`**: Phân cấp trình độ trong TOEIC (vd: `TOEIC 550+`, `TOEIC 650+`, `TOEIC 700+`, `TOEIC 850+`).
5. **`meaning`**: Định nghĩa tiếng Việt cốt lõi, dễ hiểu.
6. **`confused_words`**: Các từ dễ nhầm về mặt chữ hoặc phát âm (kèm từ, IPA, nghĩa tiếng Việt và điểm khác biệt).
7. **`confusing_meanings`**: Phân biệt sắc thái nghĩa với các từ na ná (kèm từ, nghĩa tiếng Việt và ngữ cảnh sử dụng).
8. **`collocations`**: Các cụm từ ăn điểm đi kèm, **mỗi cụm đều có nghĩa tiếng Việt**.
9. **`synonyms`**: Từ đồng nghĩa (kèm nghĩa tiếng Việt).
10. **`example`**: Câu ví dụ tiếng Anh thực tế (`en`) và **bản dịch nghĩa tiếng Việt (`vi`)**.

### 3.2. Front Matter mẫu chuẩn thực tế

```yaml
---
title: "Set 013 – Từ vựng chủ đề công việc hằng ngày"
date: 2026-10-09
draft: false
summary: "Bộ từ vựng then chốt Part 3 TOEIC Speaking: deadline, khối lượng công việc, giờ giấc linh hoạt và đi lại công sở kèm phân tích từ dễ nhầm."
topics: ["work"]
parts: ["respond-to-questions"]
tags: ["work", "speaking-part-3", "collocations", "confused-words"]
tiktok: "https://www.tiktok.com/@glory01/video/1234567890"
aliases: ["/013"]
words:
  - word: "deadline"
    pos: "Danh từ (n.)"
    ipa: "/ˈdedlaɪn/"
    level: "TOEIC 550+"
    meaning: "Hạn chót, thời hạn cuối cùng phải hoàn thành công việc"
    confused_words:
      - word: "timeline"
        ipa: "/ˈtaɪmlaɪn/"
        meaning: "Tiến độ / mốc thời gian tổng thể của dự án"
        difference: "Deadline là 1 mốc chót cố định; timeline là toàn bộ lộ trình các giai đoạn"
      - word: "lifeline"
        ipa: "/ˈlaɪflaɪn/"
        meaning: "Dây an toàn / phao cứu sinh / sự trợ giúp cứu cánh"
        difference: "Tránh phát âm nhầm âm đầu dead- /ˈded/ thành life- /ˈlaɪf/"
    confusing_meanings:
      - word: "due date"
        meaning: "Ngày đến hạn (thanh toán hóa đơn, nộp bài tập)"
        difference: "Deadline dùng cho áp lực hoàn thành công việc/dự án; due date là ngày đáo hạn tiền bạc hoặc giấy tờ"
    collocations:
      - phrase: "meet a deadline"
        meaning: "Kịp hạn chót, hoàn thành đúng hạn"
      - phrase: "miss a deadline"
        meaning: "Trễ hạn chót, không kịp tiến độ"
      - phrase: "tight deadline"
        meaning: "Hạn chót gấp gáp, thời gian rất ngắn"
      - phrase: "extend the deadline"
        meaning: "Gia hạn thêm thời gian nộp"
    synonyms:
      - word: "target date"
        meaning: "ngày mục tiêu"
    example:
      en: "We often have to work overtime to meet tight deadlines at the end of the quarter."
      vi: "Chúng tôi thường phải làm thêm giờ để kịp các hạn chót gấp gáp vào cuối quý."
---

{{< tiktok >}}

{{< words >}}

## 🎙️ Luyện tập phản xạ Speaking (Part 3)

### Câu hỏi mẫu (Question 7 - 30s):
> **Prompt:** *Do you prefer working fixed hours or having a flexible schedule? Why?*

### Gợi ý phản xạ 30 giây (Sample Response):
> "Personally, I definitely prefer having **flexible hours** for two main reasons..."
```

### 3.3. Danh sách giá trị chuẩn cho phân loại `parts`
Đối chiếu theo [Examinee Handbook của ETS](https://www.ets.org/content/dam/ets-org/pdfs/toeic/toeic-speaking-writing-examinee-handbook.pdf):
- `read-aloud`: Đọc to văn bản (Câu 1–2).
- `describe-picture`: Miêu tả tranh (Câu 3–4).
- `respond-to-questions`: Trả lời câu hỏi tình huống (Câu 5–7).
- `respond-with-info`: Trả lời dựa trên thông tin cho sẵn (Câu 8–10).
- `express-opinion`: Bày tỏ quan điểm cá nhân (Câu 11).

---

## 4. Công nghệ & Cấu hình hệ thống

| Thành phần | Công nghệ chọn | Trạng thái kỹ thuật |
| :--- | :--- | :--- |
| **Bộ sinh tĩnh** | Hugo bản extended (`v0.167.0`) |  Hoạt động tốt, build toàn trang trong ~130ms |
| **Giao diện chính** | PaperMod (Theme) |  Đã tích hợp qua Git Submodule (`themes/PaperMod`) |
| **Quản lý mã nguồn** | GitHub (`vinh-gogo/GLORY-TIKTOK`) |  Nhánh `main`, commit sạch, có `.gitignore` |
| **Lưu trữ & Tên miền** | Cloudflare Pages (`glory-tiktok.pages.dev`) |  Cấu hình build `hugo --gc --minify`, output `public` |
| **Tìm kiếm nội bộ** | PaperMod Fuse.js Client Search |  Tự động sinh `public/index.json` lập chỉ mục mọi từ & nghĩa |
| **Giao diện thẻ từ vựng** | Shortcode `words.html` + `custom.css` |  Mobile-first, hỗ trợ Light/Dark mode tự động |
| **Nhúng video TikTok** | Shortcode `tiktok.html` |  Hỗ trợ embed trực tiếp kèm nút CTA mở app TikTok |

### 4.1. File cấu hình thực tế `hugo.yaml`

```yaml
baseURL: "https://glory-tiktok.pages.dev/"
locale: vi
defaultContentLanguage: vi
title: "Glory 01 – TOEIC Speaking"
theme: PaperMod

outputs:
  home: [HTML, RSS, JSON]

taxonomies:
  tag: tags
  topic: topics
  part: parts

params:
  description: "Kho từ vựng chuẩn thi TOEIC Speaking: loại từ, IPA, level TOEIC, từ dễ nhầm, collocations và câu ví dụ song ngữ"
  author: "Glory 01"
  defaultTheme: auto
  disableThemeToggle: false
  ShowReadingTime: false
  ShowShareButtons: true
  ShowPostNavLinks: true
  ShowBreadCrumbs: true
  ShowCodeCopyButtons: true
  comments: false

  profileMode:
    enabled: true
    title: "Glory 01"
    subtitle: "Kho từ vựng & phản xạ TOEIC Speaking đồng hành cùng kênh TikTok @glory01"
    imageUrl: "/images/avatar.svg"
    imageTitle: "Glory 01"
    imageWidth: 120
    imageHeight: 120
    buttons:
      - name: "📚 Bộ bài học"
        url: "/sets/"
      - name: "🏷️ Theo chủ đề"
        url: "/topics/"
      - name: "🎯 Theo dạng bài"
        url: "/parts/"
      - name: "🎬 TikTok @glory01"
        url: "https://www.tiktok.com/@glory01"

  fuseOpts:
    isCaseSensitive: false
    shouldSort: true
    location: 0
    distance: 1000
    threshold: 0.4
    minMatchCharLength: 2
    keys: ["title", "permalink", "summary", "content"]

menu:
  main:
    - { name: "Bộ bài học", url: "/sets/", weight: 1 }
    - { name: "Chủ đề", url: "/topics/", weight: 2 }
    - { name: "Dạng bài", url: "/parts/", weight: 3 }
    - { name: "Hướng dẫn", url: "/guides/", weight: 4 }
    - { name: "Tìm kiếm", url: "/search/", weight: 5 }
    - { name: "Giới thiệu", url: "/about/", weight: 6 }
```

---

## 5. Cấu trúc cây thư mục mã nguồn hiện tại

```
D:\GLORY-TIKTOK\
├── archetypes/
│   ├── default.md                  # Khung mẫu chung
│   └── sets.md                     # Khung mẫu tạo bài học mới (hugo new sets/set-xxx.md)
├── assets/
│   └── css/extended/custom.css     # CSS tùy biến thẻ từ, level badge, nuance box, mobile-first
├── content/
│   ├── about.md                    # Giới thiệu kênh Glory 01, liên hệ & ETS disclaimer
│   ├── search.md                   # Trang tìm kiếm tức thì
│   ├── sets/
│   │   ├── _index.md               # Trang mục lục các set bài học
│   │   ├── set-001.md              # Set 001: Từ vựng & Collocations họp hành công sở
│   │   ├── set-002.md              # Set 002: Miêu tả tranh Part 2 (đường phố & quán cafe)
│   │   └── set-013.md              # Set 013: Từ vựng công việc hằng ngày
│   └── guides/
│       ├── _index.md               # Trang mục lục cẩm nang
│       └── 01-overview-5-parts.md  # Hướng dẫn tổng quan 5 dạng bài chuẩn ETS
├── layouts/
│   └── shortcodes/
│       ├── words.html              # Shortcode render thẻ từ vựng đầy đủ các trường
│       └── tiktok.html             # Shortcode nhúng video TikTok & nút CTA di động
├── static/
│   └── images/
│       └── avatar.svg              # Logo thương hiệu vector Glory 01
├── themes/
│   └── PaperMod/                   # Git submodule theme PaperMod
├── .gitignore                      # Bỏ qua public/, cache lock
├── .gitmodules                     # Cấu hình submodule cho Cloudflare Pages
├── hugo.yaml                       # Cấu hình trung tâm Hugo
├── README.md                       # Tài liệu hướng dẫn sử dụng & quy trình xuất bản
└── PLAN_TikTok_TOEIC_Speaking.md   # Bản kế hoạch và tài liệu đối soát dự án (file này)
```

---

## 6. Hướng dẫn vận hành định kỳ

1. **Tạo set bài học mới sau khi đăng video TikTok:**
   ```bash
   hugo new sets/set-014.md
   ```
2. **Xem trước trên máy tính cá nhân:**
   ```bash
   hugo server -D
   ```
3. **Đẩy lên GitHub để Cloudflare Pages tự động build lại website:**
   ```bash
   git add .
   git commit -m "feat: add set 014"
   git push origin main
   ```
