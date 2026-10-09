schema_version: 2
id: "{{ replace .File.ContentBaseName "-" " " | urlize }}"
lemma: "{{ replace .File.ContentBaseName "-" " " }}"
pos:
  - noun
ipa:
  us: "/.../"
level:
  cefr: B1
  band: core
  basis: "editorial"
topics:
  - work
speaking_use:
  - respond-to-questions
senses:
  - id: "{{ replace .File.ContentBaseName "-" " " | urlize }}-1"
    meaning_vi: "Định nghĩa tiếng Việt"
    note_vi: "Lưu ý ngữ cảnh"
confused_words:
  - ref: ""
    kind: spelling-sound
    difference_vi: "Điểm khác biệt để tránh nhầm lẫn"
confusing_meanings:
  - ref: ""
    difference_vi: "Phân biệt sắc thái nghĩa"
collocations:
  - phrase: ""
    meaning_vi: "Nghĩa tiếng Việt"
    evidence: "corpus"
synonyms:
  - word: ""
    meaning_vi: "Nghĩa tiếng Việt"
examples:
  - en: "Sample sentence in speaking context."
    vi: "Dịch nghĩa tiếng Việt câu ví dụ."
pronunciation_tips_vi: "Mẹo phát âm cho người Việt"
review:
  status: ai_cross_checked
  checked_by:
    - cmudict
  checked_at: "2026-10-10"
