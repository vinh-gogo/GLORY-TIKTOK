# ADR 007: Tìm kiếm chung tự viết

- **Trạng thái:** Accepted
- **Ngày:** 2026-10-10

## 1. Bối cảnh
Hai hệ tìm kiếm cùng tồn tại: `/search/` (PaperMod + Fuse.js, index cả `content`) và ô lọc trong `/glossary/`. Index Fuse phình theo nội dung và không xử lý tiếng Việt không dấu.

## 2. Quyết định
- Một bộ tìm kiếm duy nhất `assets/js/search.js` (không phụ thuộc thư viện), dùng cho trang chủ, `/glossary/` và `/search/`.
- Hugo sinh `/search-index.json` rút gọn (lemma, ipa, pos, band, topics, nghĩa, collocation); index tải lười khi người dùng chạm ô tìm kiếm.
- Chuẩn hóa không dấu (NFD, `đ → d`) để "han chot" khớp "hạn chót".
- Xếp hạng: khớp lemma > tiền tố lemma > collocation > nghĩa tiếng Việt.

## 3. Hệ quả
- Gỡ `fuseOpts` và output `JSON` của home.
- Nếu index vượt ngân sách (100 KB gzip ở 1.500 mục): chia mảnh theo chữ cái hoặc đánh giá Pagefind (ADR mới).
