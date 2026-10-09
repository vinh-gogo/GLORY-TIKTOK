# Kế hoạch xây web cho kênh TikTok học TOEIC Speaking

Oct 9, 2026 · @hello

## 1. Mục tiêu và vai trò của web

Web là kho lưu trữ có thể tìm lại và ôn luyện được; TikTok vẫn là nơi thu hút người xem mới.

**Vấn đề của TikTok:** video trôi theo feed, người xem khó tìm lại set cũ, không có bảng từ đầy đủ để lưu, in hay ôn lặp lại.

**Web giải quyết:**

- Một link duy nhất trong bio dẫn tới toàn bộ set bài học.
- Mỗi video có một trang riêng: danh sách từ, từ đồng nghĩa, collocations, câu ví dụ.
- Tìm lại theo chủ đề hoặc theo phần thi, không phải lướt lại kênh.
- Về sau thêm phát âm, flashcard và quiz để ôn ngay trên web.

**Người dùng chính (giả định, bạn sửa nếu khác):** người đang luyện TOEIC Speaking, xem TikTok trên điện thoại, muốn có bản ghi chép sau khi xem video.

**Chỉ số theo dõi:** lượt truy cập từ TikTok (gắn UTM), số trang xem mỗi lượt, tỷ lệ quay lại sau 7 ngày, set được xem nhiều nhất. Đặt mốc mục tiêu sau khi có 4 tuần số liệu thật, không đặt số khi chưa có dữ liệu.

## 2. Cấu trúc các trang

Trang chủ là trung tâm cho link bio, mọi trang còn lại đi ra từ đó; đường dẫn đặt bằng tiếng Anh ngắn để người xem dễ gõ lại từ màn hình video.

| Trang | Đường dẫn | Nội dung | Giai đoạn |
| --- | --- | --- | --- |
| Trang chủ | `/` | Set mới nhất, nút vào từng mục, link sang TikTok | MVP |
| Bộ bài học | `/sets/` | Mỗi video một trang: từ vựng, từ đồng nghĩa, collocations, câu ví dụ, video nhúng | MVP |
| Giới thiệu | `/about/` | Giới thiệu kênh, cách liên hệ, lưu ý không liên kết với ETS | MVP |
| Chủ đề | `/topics/` | Gom các set theo chủ đề (công việc, du lịch, mua sắm...) | v1.1 |
| Dạng bài | `/parts/` | Gom nội dung theo dạng câu hỏi trong bài thi | v1.1 |
| Hướng dẫn | `/guides/` | Cách trả lời từng dạng bài, mẫu câu, lỗi phát âm hay gặp | v1.1 |
| Tìm kiếm | `/search/` | Tìm theo từ hoặc chủ đề | v1.1 |
| Tra từ A–Z | `/glossary/` | Mọi từ đã dạy, tự sinh từ dữ liệu của các set | v2 |

Menu chính giữ tối đa 5 mục (Bộ bài học, Chủ đề, Hướng dẫn, Tìm kiếm, Giới thiệu) để vừa màn hình điện thoại.

## 3. Mô hình nội dung

Mỗi video là một "set" và mỗi set là một file Markdown; từ vựng nằm trong front matter để web tự dựng thẻ từ và, về sau, bảng tra A–Z.

- **Tên file:** `content/sets/set-013.md`, đánh số 3 chữ số để URL ổn định (`/sets/set-013/`).
- **Phân loại:** `topics` (chủ đề như work, travel, shopping), `parts` (dạng bài thi), `tags` (tự do).
- **Tạo set mới:** `hugo new sets/set-013.md` sinh sẵn khung bên dưới nhờ archetype, bạn chỉ điền từ.

Front matter mẫu (nội dung là ví dụ):

```yaml
---
title: "Set 013 – Từ vựng chủ đề công việc"
date: 2026-10-10
draft: false
summary: "8 từ và collocations dùng khi mô tả công việc hằng ngày."
topics: ["work"]
parts: ["respond-to-questions"]
tiktok: "https://www.tiktok.com/@ten-kenh/video/ID"
aliases: ["/013"]
words:
  - word: "deadline"
    ipa: "/ˈdedlaɪn/"
    meaning: "hạn chót"
    synonyms: ["due date", "cut-off"]
    collocations: ["meet a deadline", "miss a deadline"]
    example: "We have to meet the deadline by Friday."
---
```

Thân bài chỉ cần một dòng gọi shortcode `words` để hiển thị mỗi từ thành một thẻ gọn trên điện thoại, rồi thêm phần luyện nói (câu hỏi mẫu, câu trả lời mẫu) nếu có.

**Giá trị cho `parts`:** `read-aloud`, `describe-picture`, `respond-to-questions`, `respond-with-info`, `express-opinion`. Mình phân theo dạng bài, không theo số câu, vì số thứ tự câu khác nhau giữa các tài liệu ETS. Bài thi gồm 11 câu, khoảng 20 phút, thang điểm 0–200; hãy đối chiếu danh sách dạng bài với [Examinee Handbook](https://www.ets.org/content/dam/ets-org/pdfs/toeic/toeic-speaking-writing-examinee-handbook.pdf) mới nhất và trang [TOEIC Speaking & Writing của ETS](https://www.ets.org/toeic/test-takers/about/speaking-writing.html) trước khi chốt tên các trang `/parts/`.

## 4. Công nghệ và cấu hình

Giữ nguyên bộ công cụ của [blog mẫu](https://glory-hinody.pages.dev/posts/bai-viet-dau-tien/) (Hugo + PaperMod + Cloudflare Pages), nên bước dựng site lần đầu làm lại đúng Giai đoạn 0–4 trong bài đó, khoảng 2–3 giờ.

| Thành phần | Chọn | Ghi chú |
| --- | --- | --- |
| Tạo site | Hugo bản extended + theme PaperMod | Viết Markdown, build trong vài giây |
| Mã nguồn | GitHub | PaperMod thêm bằng submodule |
| Đăng web | Cloudflare Pages | Tự build mỗi lần `git push`, HTTPS tự cấp |
| Thống kê | Cloudflare Web Analytics | Miễn phí, không dùng cookie |
| Tìm kiếm | Search có sẵn của PaperMod | Chạy trên trình duyệt, không cần máy chủ |
| Bình luận | Chưa bật ở MVP | Giscus bắt buộc tài khoản GitHub, người học từ TikTok thường không có; xét lại ở v3 |

**Khác blog mẫu:** dùng section `sets` thay `posts`; thêm hai phân loại `topics` và `parts`; trang chủ dạng `profileMode` để làm trung tâm liên kết; bật tìm kiếm; tắt bình luận. Nếu không dùng Giscus thì repo có thể để private.

Cấu hình `hugo.yaml` đề xuất (đổi tên miền, tên kênh, avatar):

```yaml
baseURL: "https://TEN-WEB.pages.dev/"
locale: vi
defaultContentLanguage: vi
title: "Tên kênh – TOEIC Speaking"
theme: PaperMod

outputs:
  home: [HTML, RSS, JSON]   # JSON để tìm kiếm

taxonomies:
  tag: tags
  topic: topics
  part: parts

params:
  description: "Từ vựng, từ đồng nghĩa, collocations cho TOEIC Speaking"
  defaultTheme: auto
  comments: false
  profileMode:
    enabled: true
    title: "Tên kênh"
    subtitle: "Học mọi thứ để cải thiện TOEIC Speaking"
    imageUrl: "/avatar.png"
    buttons:
      - name: "Set mới nhất"
        url: "/sets/"
      - name: "Theo chủ đề"
        url: "/topics/"
      - name: "TikTok"
        url: "https://www.tiktok.com/@ten-kenh"

menu:
  main:
    - { name: "Bộ bài học", url: "/sets/", weight: 1 }
    - { name: "Chủ đề", url: "/topics/", weight: 2 }
    - { name: "Hướng dẫn", url: "/guides/", weight: 3 }
    - { name: "Tìm kiếm", url: "/search/", weight: 4 }
    - { name: "Giới thiệu", url: "/about/", weight: 5 }
```

Tìm kiếm cần thêm file `content/search.md` với `layout: "search"`. Cloudflare Pages dùng lệnh build `hugo --gc --minify`, thư mục `public`, biến môi trường `HUGO_VERSION` đúng bản đang dùng, và nhớ commit file `.gitmodules`; các lỗi hay gặp đã liệt kê trong bài mẫu.
