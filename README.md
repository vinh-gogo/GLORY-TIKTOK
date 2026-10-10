# Glory 01 – Website từ vựng TOEIC (mobile-first) 📖

Website: **[https://glory-tiktok.pages.dev](https://glory-tiktok.pages.dev)** · Kênh TikTok: **[@wbk.lqv](https://www.tiktok.com/@wbk.lqv)**

Nơi tra cứu và học tiếp sau mỗi video TikTok: **từ vựng**, **collocations**, **từ đồng nghĩa** và **câu nói hay** theo cấp độ, thiết kế cho điện thoại trước, desktop sau. Xây dựng bằng **Hugo (extended)** + **PaperMod** (không sửa theme; mọi tùy biến nằm trong `layouts/`, `assets/`).

> Định hướng và kế hoạch: [`PLAN_NEN_MONG_Tu_Vung_TOEIC.md`](PLAN_NEN_MONG_Tu_Vung_TOEIC.md). Quy tắc làm việc: [`AGENTS.md`](AGENTS.md). Kế hoạch cũ (TOEIC Speaking) đã lưu ở `docs/archive/`.

## Cấu trúc nội dung

| URL | Nội dung | Nguồn dữ liệu |
| :--- | :--- | :--- |
| `/glossary/` | Từ vựng A–Z, lọc theo cấp độ/chủ đề, tìm nhanh | `data/lexicon/<chữ>/<id>.yaml` |
| `/words/<id>/` | Trang từ: nghĩa, IPA, collocations, ví dụ, đồng nghĩa, từ dễ nhầm | như trên |
| `/collocations/` | Collocations gom theo chủ đề | sinh từ lexicon |
| `/synonyms/` | Nhóm đồng nghĩa có sắc thái + đồng nghĩa theo từng từ | `data/synsets/` (chưa có nhóm nào) + lexicon |
| `/quotes/` | Câu nói hay (câu chưa duyệt có nhãn) | `data/quotes/*.yaml` |
| `/levels/<band>/`, `/topics/<slug>/` | Từ theo cấp độ / chủ đề | `data/levels.yaml`, `data/topics.yaml` |
| `/sets/…`, `/001`… | Bộ từ theo video TikTok | `content/sets/*.md` |
| `/search/` | Tìm kiếm không dấu/có dấu, không cần server | `/search-index.json` (sinh khi build) |
| `/methodology/` | Nguồn, trạng thái duyệt, cách phân cấp độ | `data/sources.yaml`, `data/levels.yaml` |

Cấp độ (`foundation / core / target / advanced`) là **phân loại biên tập** của Glory 01 quy chiếu CEFR để tham khảo — ETS không công bố danh sách từ theo mức điểm. Mọi con số điểm đọc từ `data/levels.yaml`, không viết cứng.

## Phát triển cục bộ

Yêu cầu: **Hugo Extended** ≥ 0.146 (Cloudflare Pages hiện build bằng 0.146.0; CI cũng dùng 0.146.0; đã thử thêm 0.147.7 và 0.167.0; template dùng site.Data để chạy được trên cả bản cũ — bản ≥ 0.156 chỉ in cảnh báo deprecated), **Python 3.12** (`pip install pyyaml jsonschema`), **Git**.

```bash
git clone --recurse-submodules https://github.com/vinh-gogo/GLORY-TIKTOK.git
cd GLORY-TIKTOK
hugo server -D          # http://localhost:1313/
```

## Cổng kiểm tra bắt buộc trước khi báo hoàn thành

```bash
python scripts/validate/validate.py        # 0 lỗi (cảnh báo được liệt kê, không chặn)
hugo --gc --minify                          # build sạch
python scripts/build/gen_redirects.py --check
python scripts/validate/check_urls.py       # mọi URL trong docs/url-inventory-*.txt còn sống (trực tiếp hoặc qua redirect)
python scripts/validate/test_validate.py    # bộ test của validator (22 test, ~1 phút)
python scripts/levels/wordlists.py report      # đối chiếu lexicon với TSL/NGSL (cần `fetch` trước; chỉ báo cáo)
```

## Thêm nội dung

- **Mục từ mới:** viết lô `sources/batches/NNN-<chủ-đề>.yaml` theo `sources/batches/_template.yaml` rồi chạy `python scripts/import/import_batch.py <file>`. Mục mới mặc định `ai_draft` (không hiện trên web) cho tới khi được đối chiếu. IPA/nghĩa/collocation chưa chắc → `needs_review` + lý do. **Không bịa dữ liệu, không chép từ điển/đề thi.**
- **Bộ từ theo video:** `hugo new sets/set-014.md`, điền `words:` (id có trong lexicon) và link TikTok **thật** (link dạng `.../video/1234567xxx` bị coi là placeholder).
- **Redirect:** đổi/bỏ URL phải thêm quy tắc vào `scripts/build/gen_redirects.py` (sinh `static/_redirects`) và viết ADR trong `docs/adr/`.

## Cấu trúc thư mục chính

```
data/            levels.yaml, topics.yaml, sources.yaml, lexicon/, quotes/, synsets/ (khi có)
schemas/         word.v3.json, synset.v1.json, quote.v1.json, set.v3.json
content/         trang tĩnh + sets/ + bộ điều hợp nội dung (_content.gotmpl) sinh trang từ dữ liệu
layouts/         template dự án (ghi đè PaperMod); _partials/ gồm head, wcard, words-visible, extend_footer
assets/          css/extended/00-tokens … 30-components, js/search.js, glossary.js, ui.js
scripts/         validate/, migrate/, build/, import/, levels/, ipa/
sources/         batches/ (lô nhập), raw/ (danh sách ứng viên nội bộ — không phải nguồn kiểm chứng)
docs/            adr/, audit-*, changelog-data.md, archive/ (nội dung Speaking cũ), design/
```

## Triển khai Cloudflare Pages

Build command `hugo --gc --minify`, output `public`, không cần đặt `HUGO_VERSION` (mặc định hiện là 0.146.0; template tương thích 0.146.0 → 0.167.0, nếu nâng `HUGO_VERSION` thì thử build trước). File `static/_redirects` được sinh bởi script, **không sửa tay**.
