schema_version: 3
id: "{{ replace .File.ContentBaseName " " "-" | urlize }}"
lemma: "{{ replace .File.ContentBaseName "-" " " }}"
pos:
  - noun
ipa:
  us: "/.../"        # CHƯA điền → giữ status needs_review
level:
  cefr: B1
  band: core         # foundation | core | target | advanced (data/levels.yaml)
  basis:
    - editorial      # mã nguồn trong data/sources.yaml
topics:
  - offices          # 1–3 slug trong data/topics.yaml
senses:
  - id: "{{ replace .File.ContentBaseName " " "-" | urlize }}-1"
    meaning_vi: "Định nghĩa tiếng Việt"
    note_vi: "Lưu ý ngữ cảnh"
collocations:
  - phrase: ""
    meaning_vi: "Nghĩa tiếng Việt"
    evidence:
      source: unverified   # nguồn trong data/sources.yaml; không điền nguồn khi chưa kiểm tra
      checked_at: "YYYY-MM-DD"
synonyms:
  - word: ""
    meaning_vi: "Nghĩa tiếng Việt"
examples:
  - en: "Câu ví dụ tự viết, không chép từ điển/đề thi."
    vi: "Dịch nghĩa tiếng Việt câu ví dụ."
pronunciation_tips_vi: "Mẹo phát âm cho người Việt"
review:
  status: needs_review
  reason: "Mục mới tạo từ archetype, chưa đối chiếu."
  checked_at: "YYYY-MM-DD"
