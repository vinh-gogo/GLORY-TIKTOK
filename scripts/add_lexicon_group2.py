# -*- coding: utf-8 -*-
"""
Batch generator for Lexicon Group 2:
Quản trị, Vận hành, Tài chính & Tiếp thị (28 words)
"""
import os
import yaml

words_group2 = [
    {
        "id": "supervise",
        "lemma": "supervise",
        "pos": ["verb"],
        "ipa": {"us": "/ˈsuːpərvaɪz/", "uk": "/ˈsuːpəvaɪz/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["management-operations", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "supervise-1",
                "meaning_vi": "Giám sát, quản lý và theo dõi công việc của cấp dưới",
                "note_vi": "Đảm bảo công việc được thực hiện đúng quy trình và tiêu chuẩn."
            }
        ],
        "confused_words": [
            {
                "word": "supervisor",
                "ipa": "/ˈsuːpərvaɪzər/",
                "difference_vi": "Supervisor là danh từ chỉ người giám sát; supervise là động từ thực hiện việc giám sát."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Supervise là theo dõi trực tiếp hàng ngày; manage là quản lý chiến lược và tài nguyên tổng thể."
            }
        ],
        "collocations": [
            {"phrase": "supervise daily operations", "meaning_vi": "giám sát các hoạt động hàng ngày", "evidence": "corpus"},
            {"phrase": "supervise staff members", "meaning_vi": "giám sát đội ngũ nhân viên", "evidence": "corpus"},
            {"phrase": "closely supervise", "meaning_vi": "giám sát chặt chẽ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "oversee", "meaning_vi": "quan sát, giám sát"},
            {"word": "monitor", "meaning_vi": "theo dõi"},
            {"word": "manage", "meaning_vi": "quản lý"}
        ],
        "examples": [
            {
                "en": "The shift leader is responsible for supervising all warehouse operations.",
                "vi": "Trưởng ca chịu trách nhiệm giám sát toàn bộ hoạt động vận hành trong kho."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈsuː/, âm cuối là /vaɪz/ với âm /z/ rung nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "appraise",
        "lemma": "appraise",
        "pos": ["verb"],
        "ipa": {"us": "/əˈpreɪz/", "uk": "/əˈpreɪz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["management-operations", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "appraise-1",
                "meaning_vi": "Đánh giá chất lượng, hiệu suất làm việc hoặc định giá trị tài sản",
                "note_vi": "Xuất hiện phổ biến trong đánh giá nhân viên (performance appraisal) và định giá tài sản."
            }
        ],
        "confused_words": [
            {
                "word": "praise",
                "ipa": "/preɪz/",
                "difference_vi": "Praise nghĩa là khen ngợi; appraise là đánh giá hoặc định giá chuyên môn."
            },
            {
                "word": "apprise",
                "ipa": "/əˈpraɪz/",
                "difference_vi": "Apprise nghĩa là thông báo cho ai biết (nguyên âm /aɪ/); appraise là đánh giá (nguyên âm /eɪ/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Appraise nhân viên là đánh giá năng lực; appraise tài sản là thẩm định giá trị tiền tệ."
            }
        ],
        "collocations": [
            {"phrase": "appraise employee performance", "meaning_vi": "đánh giá hiệu quả làm việc của nhân viên", "evidence": "corpus"},
            {"phrase": "appraise property value", "meaning_vi": "thẩm định giá trị bất động sản", "evidence": "corpus"},
            {"phrase": "conduct an appraisal", "meaning_vi": "tiến hành đợt đánh giá", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "evaluate", "meaning_vi": "đánh giá"},
            {"word": "assess", "meaning_vi": "thẩm định, định lượng"},
            {"word": "estimate", "meaning_vi": "ước tính giá trị"}
        ],
        "examples": [
            {
                "en": "Managers meet with team members once a year to appraise their performance and set new goals.",
                "vi": "Các nhà quản lý gặp các thành viên trong nhóm mỗi năm một lần để đánh giá hiệu suất và đặt ra mục tiêu mới."
            }
        ],
        "pronunciation_tips_vi": "Nhấn trọng âm ở âm tiết thứ hai /preɪz/, nhị trùng âm /eɪ/ kéo dài và kết thúc bằng âm /z/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "demote",
        "lemma": "demote",
        "pos": ["verb"],
        "ipa": {"us": "/dɪˈmoʊt/", "uk": "/dɪˈməʊt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["human-resources", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "demote-1",
                "meaning_vi": "Giáng chức, hạ bậc lương hoặc chuyển xuống vị trí thấp hơn",
                "note_vi": "Ngược nghĩa với promote (thăng chức)."
            }
        ],
        "confused_words": [
            {
                "word": "promote",
                "ipa": "/prəˈmoʊt/",
                "difference_vi": "Promote là thăng chức; demote là giáng chức."
            },
            {
                "word": "remote",
                "ipa": "/rɪˈmoʊt/",
                "difference_vi": "Remote là xa xôi hoặc làm việc từ xa; demote là hạ cấp chức vụ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Demote là hạ cấp bậc trong tổ chức vì sai phạm hoặc tái cơ cấu; khác với dismiss là cho thôi việc luôn."
            }
        ],
        "collocations": [
            {"phrase": "demote to a lower rank", "meaning_vi": "giáng xuống cấp bậc thấp hơn", "evidence": "corpus"},
            {"phrase": "demote for misconduct", "meaning_vi": "bị giáng chức do vi phạm kỷ luật", "evidence": "corpus"},
            {"phrase": "face demotion", "meaning_vi": "đối mặt với nguy cơ bị giáng chức", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "downgrade", "meaning_vi": "hạ cấp"},
            {"word": "relegate", "meaning_vi": "đẩy xuống vị trí thấp"}
        ],
        "examples": [
            {
                "en": "Following the accounting discrepancies, the finance director was demoted to an advisory role.",
                "vi": "Sau những sai lệch sổ sách kế toán, giám đốc tài chính đã bị giáng chức xuống vai trò cố vấn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /moʊt/ với nguyên âm đôi /oʊ/ tròn môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "dismiss",
        "lemma": "dismiss",
        "pos": ["verb"],
        "ipa": {"us": "/dɪsˈmɪs/", "uk": "/dɪsˈmɪs/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["human-resources", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "dismiss-1",
                "meaning_vi": "Sa thải nhân viên; bác bỏ một ý tưởng hoặc khiếu nại",
                "note_vi": "Dùng trong văn cảnh nhân sự chính thức tương đương fire hoặc lay off."
            }
        ],
        "confused_words": [
            {
                "word": "miss",
                "ipa": "/mɪs/",
                "difference_vi": "Miss là bỏ lỡ hoặc nhớ; dismiss là sa thải hoặc gạt bỏ ý kiến."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Dismiss an employee = sa thải nhân viên; dismiss an idea = gạt bỏ ý tưởng coi là không đáng quan tâm."
            }
        ],
        "collocations": [
            {"phrase": "dismiss an employee", "meaning_vi": "sa thải một nhân viên", "evidence": "corpus"},
            {"phrase": "dismiss an idea", "meaning_vi": "gạt bỏ một ý kiến", "evidence": "corpus"},
            {"phrase": "wrongfully dismissed", "meaning_vi": "bị sa thải trái pháp luật", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "fire", "meaning_vi": "sa thải"},
            {"word": "discharge", "meaning_vi": "cho xuất viện / cho thôi việc"},
            {"word": "lay off", "meaning_vi": "cho nghỉ việc vì giảm biên chế"}
        ],
        "examples": [
            {
                "en": "The manager decided to dismiss the complaint because there was insufficient evidence.",
                "vi": "Người quản lý đã quyết định bác bỏ khiếu nại vì không có đủ bằng chứng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /mɪs/, âm /s/ gió kết thúc sắc nét.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "resign",
        "lemma": "resign",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈzaɪn/", "uk": "/rɪˈzaɪn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "resign-1",
                "meaning_vi": "Từ chức, nộp đơn xin nghỉ việc chủ động",
                "note_vi": "Quyết định nghỉ việc xuất phát từ nguyện vọng cá nhân của người lao động."
            }
        ],
        "confused_words": [
            {
                "word": "re-sign",
                "ipa": "/ˌriːˈsaɪn/",
                "difference_vi": "Re-sign (có gạch nối) là ký lại hợp đồng mới; resign (liền nhau) là từ chức, xin nghỉ việc."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Resign from a post = từ bỏ chức vụ; resign oneself to = cam chịu một số phận không mong muốn."
            }
        ],
        "collocations": [
            {"phrase": "resign from a position", "meaning_vi": "từ chức khỏi một vị trí", "evidence": "corpus"},
            {"phrase": "tender one's resignation", "meaning_vi": "đệ đơn xin từ chức", "evidence": "corpus"},
            {"phrase": "resign with immediate effect", "meaning_vi": "từ chức có hiệu lực ngay lập tức", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "quit", "meaning_vi": "bỏ việc"},
            {"word": "step down", "meaning_vi": "từ chức, rút lui"},
            {"word": "leave", "meaning_vi": "rời bỏ vị trí"}
        ],
        "examples": [
            {
                "en": "The vice president tendered his resignation to pursue opportunities in another industry.",
                "vi": "Phó chủ tịch đã đệ đơn từ chức để theo đuổi cơ hội trong một ngành nghề khác."
            }
        ],
        "pronunciation_tips_vi": "Chữ 's' đọc thành âm rung /z/, chữ 'g' câm hoàn toàn, phát âm là /rɪˈzaɪn/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "retire",
        "lemma": "retire",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈtaɪər/", "uk": "/rɪˈtaɪə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources", "salary-benefits"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "retire-1",
                "meaning_vi": "Nghỉ hưu, kết thúc sự nghiệp lao động sau khi đủ tuổi",
                "note_vi": "Gắn liền với các chính sách hưu trí và tiệc chia tay đồng nghiệp (retirement party)."
            }
        ],
        "confused_words": [
            {
                "word": "tired",
                "ipa": "/ˈtaɪərd/",
                "difference_vi": "Tired là tính từ mệt mỏi; retire là động từ nghỉ hưu."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Retire from a career = nghỉ hưu; retire to bed = đi ngủ (nghĩa văn học cổ)."
            }
        ],
        "collocations": [
            {"phrase": "retire from work", "meaning_vi": "nghỉ hưu, ngừng làm việc", "evidence": "corpus"},
            {"phrase": "reach retirement age", "meaning_vi": "đến tuổi về hưu", "evidence": "corpus"},
            {"phrase": "retire comfortably", "meaning_vi": "nghỉ hưu với cuộc sống an nhàn", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "stop working", "meaning_vi": "ngừng làm việc"},
            {"word": "step aside", "meaning_vi": "lui về nghỉ ngơi"}
        ],
        "examples": [
            {
                "en": "After forty years of dedicated service, our head engineer plans to retire next month.",
                "vi": "Sau bốn mươi năm cống hiến tận tụy, kỹ sư trưởng của chúng tôi dự định sẽ nghỉ hưu vào tháng tới."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /taɪər/ với nhị trùng âm /aɪ/ dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "restructure",
        "lemma": "restructure",
        "pos": ["verb"],
        "ipa": {"us": "/ˌriːˈstrʌktʃər/", "uk": "/ˌriːˈstrʌktʃə/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["management-operations", "finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "restructure-1",
                "meaning_vi": "Tái cấu trúc tổ chức bộ máy, vận hành hoặc các khoản nợ tài chính",
                "note_vi": "Biện pháp sắp xếp lại phòng ban hoặc cấu trúc vốn để nâng cao năng suất và cắt giảm chi phí."
            }
        ],
        "confused_words": [
            {
                "word": "structure",
                "ipa": "/ˈstrʌktʃər/",
                "difference_vi": "Structure là cấu trúc sẵn có; restructure là hành động cơ cấu lại."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Corporate restructuring thường đi kèm việc tinh giản biên chế hoặc sáp nhập các ban bệ."
            }
        ],
        "collocations": [
            {"phrase": "restructure a department", "meaning_vi": "tái cơ cấu một phòng ban", "evidence": "corpus"},
            {"phrase": "corporate restructuring", "meaning_vi": "sự tái cấu trúc doanh nghiệp", "evidence": "corpus"},
            {"phrase": "restructure financial debt", "meaning_vi": "cơ cấu lại các khoản nợ tài chính", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "reorganize", "meaning_vi": "sắp xếp lại tổ chức"},
            {"word": "overhaul", "meaning_vi": "đại tu toàn diện"}
        ],
        "examples": [
            {
                "en": "The corporation is restructuring its sales division to better respond to digital demands.",
                "vi": "Tập đoàn đang tái cấu trúc bộ phận kinh doanh để đáp ứng tốt hơn các nhu cầu số hóa."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu có tiền tố /riː/ nhấn phụ, trọng âm chính ở /ˈstrʌk/ có cụm phụ âm /str/ lướt nhanh.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "audit",
        "lemma": "audit",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈɔːdɪt/", "uk": "/ˈɔːdɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "audit-1",
                "meaning_vi": "Sự kiểm toán, cuộc kiểm tra sổ sách kế toán chính thức; (v) kiểm toán",
                "note_vi": "Thẩm tra độ chính xác và tính minh bạch của các báo cáo tài chính."
            }
        ],
        "confused_words": [
            {
                "word": "audio",
                "ipa": "/ˈɔːdioʊ/",
                "difference_vi": "Audio là âm thanh; audit là kiểm toán tài chính sổ sách."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Financial audit là kiểm toán tài chính; quality audit là kiểm tra quy trình chất lượng ISO."
            }
        ],
        "collocations": [
            {"phrase": "conduct an internal audit", "meaning_vi": "tiến hành kiểm toán nội bộ", "evidence": "corpus"},
            {"phrase": "annual financial audit", "meaning_vi": "cuộc kiểm toán tài chính thường niên", "evidence": "corpus"},
            {"phrase": "audit the company books", "meaning_vi": "kiểm toán sổ sách công ty", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "inspect", "meaning_vi": "thanh tra"},
            {"word": "examine", "meaning_vi": "kiểm tra kỹ lưỡng"},
            {"word": "review", "meaning_vi": "rà soát lại"}
        ],
        "examples": [
            {
                "en": "An independent auditing firm was hired to verify the accuracy of the financial statements.",
                "vi": "Một công ty kiểm toán độc lập đã được thuê để xác thực độ chính xác của các báo cáo tài chính."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈɔː/, nguyên âm /ɔː/ tròn môi mở vừa phải, âm đuôi /dɪt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "deficit",
        "lemma": "deficit",
        "pos": ["noun"],
        "ipa": {"us": "/ˈdefɪsɪt/", "uk": "/ˈdefɪsɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "deficit-1",
                "meaning_vi": "Sự thâm hụt tài chính (khi chi phí vượt quá số thu)",
                "note_vi": "Trái nghĩa trực tiếp với surplus (thặng dư)."
            }
        ],
        "confused_words": [
            {
                "word": "deficient",
                "ipa": "/dɪˈfɪʃnt/",
                "difference_vi": "Deficient là tính từ (thiếu hụt chất lượng/dưỡng chất); deficit là danh từ chỉ số tiền thâm hụt."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Budget deficit là thâm hụt ngân sách nhà nước/doanh nghiệp; trade deficit là thâm hụt cán cân thương mại."
            }
        ],
        "collocations": [
            {"phrase": "budget deficit", "meaning_vi": "thâm hụt ngân sách", "evidence": "corpus"},
            {"phrase": "trade deficit", "meaning_vi": "thâm hụt thương mại (nhập siêu)", "evidence": "corpus"},
            {"phrase": "reduce the deficit", "meaning_vi": "cắt giảm mức thâm hụt", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "shortfall", "meaning_vi": "khoản thiếu hụt"},
            {"word": "loss", "meaning_vi": "khoản thua lỗ"}
        ],
        "examples": [
            {
                "en": "Measures were implemented immediately to cut overhead and curb the growing budget deficit.",
                "vi": "Các biện pháp đã được thực thi ngay lập tức nhằm cắt giảm chi phí gián tiếp và kiềm chế thâm hụt ngân sách gia tăng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈdef/, đừng đọc nhầm trọng âm thành de-fi-cit.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "surplus",
        "lemma": "surplus",
        "pos": ["noun", "adjective"],
        "ipa": {"us": "/ˈsɜːrpləs/", "uk": "/ˈsɜːpləs/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "surplus-1",
                "meaning_vi": "Số thặng dư, phần dôi dư vượt quá nhu cầu; (adj) dư thừa",
                "note_vi": "Khi thu nhập vượt quá chi tiêu, hoặc lượng hàng tồn vượt quá mức cần thiết."
            }
        ],
        "confused_words": [
            {
                "word": "surface",
                "ipa": "/ˈsɜːrfɪs/",
                "difference_vi": "Surface là bề mặt; surplus là thặng dư tài chính hoặc hàng dôi dư."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Budget surplus là thặng dư ngân sách; surplus inventory là hàng hóa tồn kho dư thừa."
            }
        ],
        "collocations": [
            {"phrase": "budget surplus", "meaning_vi": "thặng dư ngân sách", "evidence": "corpus"},
            {"phrase": "surplus stock", "meaning_vi": "lượng hàng hóa dư thừa trong kho", "evidence": "corpus"},
            {"phrase": "generate a surplus", "meaning_vi": "tạo ra khoản thặng dư", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "excess", "meaning_vi": "sự vượt quá, dôi dư"},
            {"word": "extra", "meaning_vi": "phần thêm vào"}
        ],
        "examples": [
            {
                "en": "Thanks to robust export sales, the firm ended the fiscal year with a substantial surplus.",
                "vi": "Nhờ doanh số xuất khẩu mạnh mẽ, công ty đã kết thúc năm tài chính với một khoản thặng dư đáng kể."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈsɜːr/, âm thứ hai đọc là /pləs/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "fiscal",
        "lemma": "fiscal",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈfɪskl/", "uk": "/ˈfɪskl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "fiscal-1",
                "meaning_vi": "Thuộc về tài chính công, ngân sách tài khóa hoặc năm tài chính",
                "note_vi": "Cụm fiscal year (năm tài chính/năm tài khóa) là collocation cốt lõi của TOEIC."
            }
        ],
        "confused_words": [
            {
                "word": "physical",
                "ipa": "/ˈfɪzɪkl/",
                "difference_vi": "Physical là thuộc về thể chất hoặc vật lý (/z/); fiscal là thuộc về tài chính ngân sách (/s/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Fiscal liên quan đến chính sách thu thuế và chi tiêu của chính phủ hoặc năm kế toán doanh nghiệp."
            }
        ],
        "collocations": [
            {"phrase": "fiscal year", "meaning_vi": "năm tài chính / niên độ tài khóa", "evidence": "corpus"},
            {"phrase": "fiscal policy", "meaning_vi": "chính sách tài khóa", "evidence": "corpus"},
            {"phrase": "end of the fiscal quarter", "meaning_vi": "cuối quý tài chính", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "financial", "meaning_vi": "thuộc về tài chính"},
            {"word": "monetary", "meaning_vi": "thuộc về tiền tệ"}
        ],
        "examples": [
            {
                "en": "Revenue figures for the fourth quarter of the fiscal year exceeded analysts' projections.",
                "vi": "Số liệu doanh thu quý tư của năm tài chính đã vượt xa dự báo của các nhà phân tích."
            }
        ],
        "pronunciation_tips_vi": "Phát âm âm /s/ rõ (không đọc thành /z/ như 'physical'), âm đuôi là /kl/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "expenditure",
        "lemma": "expenditure",
        "pos": ["noun"],
        "ipa": {"us": "/ɪkˈspendɪtʃər/", "uk": "/ɪkˈspendɪtʃə/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "expenditure-1",
                "meaning_vi": "Khoản chi tiêu, tổng số tiền bỏ ra cho một mục đích cụ thể",
                "note_vi": "Thuật ngữ chính thống trong bảng cân đối kế toán và báo cáo ngân sách."
            }
        ],
        "confused_words": [
            {
                "word": "expense",
                "ipa": "/ɪkˈspens/",
                "difference_vi": "Expense thường chỉ chi phí phát sinh hàng ngày; expenditure mang tính tổng chi tiêu quy mô lớn của tổ chức."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Capital expenditure (CapEx) là chi đầu tư tài sản cố định; operational expenditure (OpEx) là chi phí vận hành thường xuyên."
            }
        ],
        "collocations": [
            {"phrase": "reduce overall expenditure", "meaning_vi": "cắt giảm tổng mức chi tiêu", "evidence": "corpus"},
            {"phrase": "capital expenditure", "meaning_vi": "chi phí đầu tư tài sản cố định", "evidence": "corpus"},
            {"phrase": "public expenditure", "meaning_vi": "chi tiêu công của nhà nước", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "spending", "meaning_vi": "sự chi tiêu"},
            {"word": "outlay", "meaning_vi": "khoản kinh phí bỏ ra"},
            {"word": "cost", "meaning_vi": "chi phí"}
        ],
        "examples": [
            {
                "en": "The board approved a 10% increase in research and development expenditure for next year.",
                "vi": "Hội đồng quản trị đã phê duyệt mức tăng 10% chi tiêu cho nghiên cứu và phát triển vào năm tới."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /spen/, đuôi kết thúc bằng /tʃər/ mềm mại.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "lucrative",
        "lemma": "lucrative",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈluːkrətɪv/", "uk": "/ˈluːkrətɪv/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["finance-accounting", "contracts-negotiation"],
        "speaking_use": ["express-opinion", "respond-with-info"],
        "senses": [
            {
                "id": "lucrative-1",
                "meaning_vi": "Sinh lời lớn, mang lại nhiều lợi nhuận tài chính béo bở",
                "note_vi": "Miêu tả các cơ hội kinh doanh, thỏa thuận thương mại hoặc thị trường hấp dẫn."
            }
        ],
        "confused_words": [
            {
                "word": "creative",
                "ipa": "/kriˈeɪtɪv/",
                "difference_vi": "Creative là sáng tạo; lucrative là sinh lời nhiều tiền bạc."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Lucrative nhấn mạnh vào khả năng kiếm được món tiền lớn nhanh chóng."
            }
        ],
        "collocations": [
            {"phrase": "lucrative contract", "meaning_vi": "hợp đồng béo bở, sinh lợi lớn", "evidence": "corpus"},
            {"phrase": "lucrative business opportunity", "meaning_vi": "cơ hội kinh doanh sinh lời cao", "evidence": "corpus"},
            {"phrase": "highly lucrative market", "meaning_vi": "thị trường cực kỳ tiềm năng về lợi nhuận", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "profitable", "meaning_vi": "có lãi, sinh lời"},
            {"word": "gainful", "meaning_vi": "có thu nhập tốt"},
            {"word": "rewarding", "meaning_vi": "xứng đáng, đem lại nhiều lợi ích"}
        ],
        "examples": [
            {
                "en": "Securing that overseas distribution deal proved to be extremely lucrative for the company.",
                "vi": "Giành được thỏa thuận phân phối ở nước ngoài đó đã được chứng minh là cực kỳ sinh lợi cho công ty."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈluː/, nguyên âm /uː/ dài, hai âm sau đọc lướt nhẹ /krətɪv/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "asset",
        "lemma": "asset",
        "pos": ["noun"],
        "ipa": {"us": "/ˈæset/", "uk": "/ˈæset/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "asset-1",
                "meaning_vi": "Tài sản có giá trị của doanh nghiệp; nhân tố hoặc kỹ năng quý báu",
                "note_vi": "Trong kế toán: tài sản = nợ phải trả + vốn chủ sở hữu (Assets = Liabilities + Equity)."
            }
        ],
        "confused_words": [
            {
                "word": "assess",
                "ipa": "/əˈses/",
                "difference_vi": "Assess là động từ đánh giá (trọng âm 2); asset là danh từ tài sản (trọng âm 1)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Fixed assets = tài sản cố định (nhà xưởng, máy móc); an asset to the team = một nhân sự quý giá cho đội ngũ."
            }
        ],
        "collocations": [
            {"phrase": "fixed assets", "meaning_vi": "tài sản cố định", "evidence": "corpus"},
            {"phrase": "valuable asset", "meaning_vi": "tài sản / nhân tố quý giá", "evidence": "corpus"},
            {"phrase": "liquid assets", "meaning_vi": "tài sản có tính thanh khoản cao", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "property", "meaning_vi": "bất động sản, tài sản"},
            {"word": "resource", "meaning_vi": "nguồn lực, tài nguyên"}
        ],
        "examples": [
            {
                "en": "Her fluency in three foreign languages makes her a tremendous asset to our global marketing division.",
                "vi": "Việc thông thạo ba ngoại ngữ biến cô ấy thành một nhân tố vô cùng quý báu cho bộ phận tiếp thị toàn cầu của chúng tôi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈæ/, nguyên âm /æ/ bẹt miệng rộng, âm đuôi /t/ sắc nét.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "liability",
        "lemma": "liability",
        "pos": ["noun"],
        "ipa": {"us": "/ˌlaɪəˈbɪləti/", "uk": "/ˌlaɪəˈbɪləti/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "liability-1",
                "meaning_vi": "Khoản nợ phải trả trên bảng cân đối kế toán; trách nhiệm pháp lý",
                "note_vi": "Đối nghịch với asset (tài sản)."
            }
        ],
        "confused_words": [
            {
                "word": "reliable",
                "ipa": "/rɪˈlaɪəbl/",
                "difference_vi": "Reliable là tính từ đáng tin cậy; liability là danh từ gánh nặng nợ nần hoặc trách nhiệm pháp lý."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Trong tài chính, liabilities là các khoản nợ phải trả; trong đời sống, liability là gánh nặng gây cản trở."
            }
        ],
        "collocations": [
            {"phrase": "total liabilities", "meaning_vi": "tổng nợ phải trả", "evidence": "corpus"},
            {"phrase": "legal liability", "meaning_vi": "trách nhiệm pháp lý trước pháp luật", "evidence": "corpus"},
            {"phrase": "accept liability", "meaning_vi": "nhận trách nhiệm bồi thường", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "obligation", "meaning_vi": "nghĩa vụ thanh toán"},
            {"word": "debt", "meaning_vi": "khoản nợ"}
        ],
        "examples": [
            {
                "en": "The airline denied any legal liability for the damage caused by severe weather delays.",
                "vi": "Hãng hàng không từ chối mọi trách nhiệm pháp lý đối với thiệt hại gây ra bởi sự chậm trễ do thời tiết xấu."
            }
        ],
        "pronunciation_tips_vi": "Từ có 5 âm tiết, trọng âm chính rơi vào âm thứ ba /ˈbɪl/, âm đầu là /laɪ.ə/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "dividend",
        "lemma": "dividend",
        "pos": ["noun"],
        "ipa": {"us": "/ˈdɪvɪdend/", "uk": "/ˈdɪvɪdend/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "dividend-1",
                "meaning_vi": "Cổ tức, khoản lợi nhuận chia cho các cổ đông của công ty",
                "note_vi": "Khoản chi trả từ lợi nhuận sau thuế cho người nắm giữ cổ phần."
            }
        ],
        "confused_words": [
            {
                "word": "divide",
                "ipa": "/dɪˈvaɪd/",
                "difference_vi": "Divide là động từ chia rẽ/phân chia; dividend là danh từ cổ tức nhận được từ cổ phiếu."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Dividend trong chứng khoán là cổ tức tiền mặt hoặc cổ phiếu; thành ngữ 'pay dividends' nghĩa là mang lại trái ngọt/kết quả tốt đẹp trong tương lai."
            }
        ],
        "collocations": [
            {"phrase": "pay a dividend", "meaning_vi": "chi trả cổ tức", "evidence": "corpus"},
            {"phrase": "quarterly dividend", "meaning_vi": "cổ tức chi trả hàng quý", "evidence": "corpus"},
            {"phrase": "dividend payout ratio", "meaning_vi": "tỷ lệ chi trả cổ tức trên lợi nhuận", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "share of profits", "meaning_vi": "phần chia lợi nhuận"},
            {"word": "yield", "meaning_vi": "tỷ suất lợi tức"}
        ],
        "examples": [
            {
                "en": "Shareholders voted to approve a quarterly dividend of fifty cents per common share.",
                "vi": "Các cổ đông đã biểu quyết thông qua mức cổ tức hàng quý là năm mươi xu cho mỗi cổ phiếu phổ thông."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈdɪv/, âm thứ ba là /dend/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "portfolio",
        "lemma": "portfolio",
        "pos": ["noun"],
        "ipa": {"us": "/pɔːrtˈfoʊlioʊ/", "uk": "/pɔːtˈfəʊliəʊ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting", "marketing-advertising"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "portfolio-1",
                "meaning_vi": "Danh mục đầu tư tài chính; danh mục các sản phẩm / dịch vụ của công ty",
                "note_vi": "Tập hợp các tài sản đầu tư như cổ phiếu, trái phiếu hoặc bộ sản phẩm chủ lực."
            }
        ],
        "confused_words": [
            {
                "word": "profile",
                "ipa": "/ˈproʊfaɪl/",
                "difference_vi": "Profile là hồ sơ cá nhân hoặc tóm tắt sơ lược; portfolio là bộ sưu tập tác phẩm hoặc danh mục đầu tư tài chính."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Investment portfolio là danh mục đầu tư tài chính; design portfolio là tập tài liệu tổng hợp các dự án thiết kế đã làm."
            }
        ],
        "collocations": [
            {"phrase": "investment portfolio", "meaning_vi": "danh mục đầu tư tài chính", "evidence": "corpus"},
            {"phrase": "product portfolio", "meaning_vi": "danh mục các sản phẩm kinh doanh", "evidence": "corpus"},
            {"phrase": "diversify one's portfolio", "meaning_vi": "đa dạng hóa danh mục đầu tư", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "range of products", "meaning_vi": "chuỗi các sản phẩm"},
            {"word": "collection", "meaning_vi": "bộ sưu tập"}
        ],
        "examples": [
            {
                "en": "Financial advisors recommend diversifying your investment portfolio to minimize market risks.",
                "vi": "Các chuyên gia tư vấn tài chính khuyên bạn nên đa dạng hóa danh mục đầu tư để giảm thiểu rủi ro thị trường."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈfoʊ/, nguyên âm uốn lưỡi /ɔːrt/ ở âm đầu.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "demographic",
        "lemma": "demographic",
        "pos": ["noun", "adjective"],
        "ipa": {"us": "/ˌdeməˈɡræfɪk/", "uk": "/ˌdeməˈɡræfɪk/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "demographic-1",
                "meaning_vi": "Nhóm nhân khẩu học cụ thể (độ tuổi, thu nhập, giới tính); (adj) thuộc nhân khẩu học",
                "note_vi": "Yếu tố căn bản để phân đoạn thị trường khách hàng mục tiêu."
            }
        ],
        "confused_words": [
            {
                "word": "geographic",
                "ipa": "/ˌdʒiːəˈɡræfɪk/",
                "difference_vi": "Geographic là thuộc về địa lý vùng miền; demographic là thuộc về đặc điểm dân cư nhân khẩu học."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Dạng số nhiều 'demographics' chỉ toàn bộ số liệu thống kê dân số của một thị trường."
            }
        ],
        "collocations": [
            {"phrase": "target demographic", "meaning_vi": "nhóm khách hàng mục tiêu nhân khẩu học", "evidence": "corpus"},
            {"phrase": "demographic data", "meaning_vi": "dữ liệu nhân khẩu học", "evidence": "corpus"},
            {"phrase": "younger demographic", "meaning_vi": "phân khúc khách hàng trẻ tuổi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "population group", "meaning_vi": "nhóm dân số"},
            {"word": "target market", "meaning_vi": "thị trường mục tiêu"}
        ],
        "examples": [
            {
                "en": "The new smartphone campaign is tailored specifically to appeal to the younger demographic.",
                "vi": "Chiến dịch điện thoại thông minh mới được thiết kế riêng nhằm thu hút nhóm khách hàng trẻ tuổi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ ba /ˈɡræf/, nguyên âm /æ/ mở rộng khẩu hình miệng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "consumer",
        "lemma": "consumer",
        "pos": ["noun"],
        "ipa": {"us": "/kənˈsuːmər/", "uk": "/kənˈsjuːmə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising", "sales-customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "consumer-1",
                "meaning_vi": "Người tiêu dùng, người sử dụng trực tiếp sản phẩm hoặc dịch vụ cuối cùng",
                "note_vi": "Khác với customer (người trả tiền mua, có thể mua để bán lại)."
            }
        ],
        "confused_words": [
            {
                "word": "customer",
                "ipa": "/ˈkʌstəmər/",
                "difference_vi": "Customer là khách hàng tại điểm bán; consumer là người trực tiếp sử dụng sản phẩm."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Consumer goods = hàng tiêu dùng hàng ngày (thực phẩm, đồ gia dụng)."
            }
        ],
        "collocations": [
            {"phrase": "consumer demand", "meaning_vi": "nhu cầu của người tiêu dùng", "evidence": "corpus"},
            {"phrase": "consumer behavior", "meaning_vi": "hành vi tiêu dùng của khách hàng", "evidence": "corpus"},
            {"phrase": "protect consumer rights", "meaning_vi": "bảo vệ quyền lợi người tiêu dùng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "buyer", "meaning_vi": "người mua"},
            {"word": "end-user", "meaning_vi": "người dùng cuối"},
            {"word": "client", "meaning_vi": "khách hàng"}
        ],
        "examples": [
            {
                "en": "Online surveys help businesses gain valuable insights into changing consumer preferences.",
                "vi": "Các cuộc khảo sát trực tuyến giúp doanh nghiệp có được cái nhìn sâu sắc quý giá về thị hiếu tiêu dùng đang thay đổi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /suːm/, giọng Mỹ đọc là /kənˈsuːmər/, không có âm /j/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "endorse",
        "lemma": "endorse",
        "pos": ["verb"],
        "ipa": {"us": "/ɪnˈdɔːrs/", "uk": "/ɪnˈdɔːs/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["marketing-advertising", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "endorse-1",
                "meaning_vi": "Đại diện quảng cáo, bảo chứng cho thương hiệu; công khai ủng hộ một chính sách",
                "note_vi": "Xuất hiện trong các hợp đồng đại sứ thương hiệu người nổi tiếng (celebrity endorsement)."
            },
            {
                "id": "endorse-2",
                "meaning_vi": "Ký hậu mặt sau chi phiếu (ngân hàng)",
                "note_vi": "Ký xác nhận chuyển nhượng quyền thụ hưởng séc."
            }
        ],
        "confused_words": [
            {
                "word": "enforce",
                "ipa": "/ɪnˈfɔːrs/",
                "difference_vi": "Enforce nghĩa là cưỡng chế thi hành luật pháp (/f/); endorse là ủng hộ hoặc đại diện quảng bá (/d/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Endorse a candidate = ủng hộ ứng cử viên; endorse a product = quảng cáo bảo chứng cho sản phẩm."
            }
        ],
        "collocations": [
            {"phrase": "endorse a product", "meaning_vi": "quảng bá / bảo chứng cho một sản phẩm", "evidence": "corpus"},
            {"phrase": "celebrity endorsement", "meaning_vi": "sự đại diện quảng cáo bởi người nổi tiếng", "evidence": "corpus"},
            {"phrase": "officially endorse", "meaning_vi": "chính thức lên tiếng ủng hộ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "support", "meaning_vi": "ủng hộ"},
            {"word": "back", "meaning_vi": "hậu thuẫn, đứng sau"},
            {"word": "advocate", "meaning_vi": "tán thành"}
        ],
        "examples": [
            {
                "en": "The sports apparel manufacturer signed a tennis champion to endorse their new shoe line.",
                "vi": "Hãng sản xuất trang phục thể thao đã ký hợp đồng với một nhà vô địch quần vợt để quảng bá cho dòng giày mới của họ."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈdɔːrs/, âm /r/ uốn lưỡi và âm /s/ kết thúc rõ ràng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "outreach",
        "lemma": "outreach",
        "pos": ["noun"],
        "ipa": {"us": "/ˈaʊtriːtʃ/", "uk": "/ˈaʊtriːtʃ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "outreach-1",
                "meaning_vi": "Hoạt động tiếp cận cộng đồng, chương trình mở rộng quan hệ khách hàng",
                "note_vi": "Các chiến dịch chủ động kết nối mang tính xã hội hoặc mở rộng độ phủ khách hàng."
            }
        ],
        "confused_words": [
            {
                "word": "reach",
                "ipa": "/riːtʃ/",
                "difference_vi": "Reach là độ với tới hoặc chạm đến; outreach là các chương trình chủ động tiếp cận cộng đồng bên ngoài."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Community outreach là công tác xã hội thiện nguyện; customer outreach là hoạt động tiếp cận khách hàng tiềm năng."
            }
        ],
        "collocations": [
            {"phrase": "community outreach", "meaning_vi": "hoạt động tiếp cận và hỗ trợ cộng đồng", "evidence": "corpus"},
            {"phrase": "outreach campaign", "meaning_vi": "chiến dịch truyền thông tiếp cận", "evidence": "corpus"},
            {"phrase": "expand customer outreach", "meaning_vi": "mở rộng phạm vi tiếp cận khách hàng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "engagement", "meaning_vi": "sự tương tác kết nối"},
            {"word": "involvement", "meaning_vi": "sự tham gia gắn kết"}
        ],
        "examples": [
            {
                "en": "As part of its corporate social responsibility, the company launched an educational outreach program.",
                "vi": "Như một phần của trách nhiệm xã hội doanh nghiệp, công ty đã triển khai chương trình tiếp cận giáo dục vì cộng đồng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈaʊt/, âm thứ hai kết thúc bằng âm /tʃ/ bật hơi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "brochure",
        "lemma": "brochure",
        "pos": ["noun"],
        "ipa": {"us": "/broʊˈʃʊr/", "uk": "/ˈbrəʊʃə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising", "hospitality-travel"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "brochure-1",
                "meaning_vi": "Tập tài liệu quảng cáo gấp nhiều trang (giới thiệu sản phẩm, tour du lịch)",
                "note_vi": "Ấn phẩm tiếp thị in màu giới thiệu chi tiết sản phẩm, dịch vụ hoặc tour tham quan."
            }
        ],
        "confused_words": [
            {
                "word": "pamphlet",
                "ipa": "/ˈpæmflət/",
                "difference_vi": "Pamphlet là tập tài liệu mỏng thường dùng tuyên truyền quan điểm; brochure thường dày dặn in màu bóng bẩy để quảng cáo thương mại."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Travel brochure = cẩm nang du lịch quảng bá; product brochure = sách giới thiệu sản phẩm."
            }
        ],
        "collocations": [
            {"phrase": "promotional brochure", "meaning_vi": "tập tài liệu quảng cáo xúc tiến", "evidence": "corpus"},
            {"phrase": "print brochures", "meaning_vi": "in ấn các tập tài liệu giới thiệu", "evidence": "corpus"},
            {"phrase": "distribute brochures", "meaning_vi": "phát tài liệu quảng cáo", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "booklet", "meaning_vi": "tập sách nhỏ"},
            {"word": "pamphlet", "meaning_vi": "tờ gấp tài liệu"},
            {"word": "catalog", "meaning_vi": "danh mục sản phẩm"}
        ],
        "examples": [
            {
                "en": "You can pick up a promotional brochure at the front desk for detailed package pricing.",
                "vi": "Bạn có thể lấy một tập tài liệu quảng cáo tại quầy lễ tân để xem chi tiết giá các gói dịch vụ."
            }
        ],
        "pronunciation_tips_vi": "Trong tiếng Mỹ nhấn âm hai /broʊˈʃʊr/, âm giữa là /ʃ/ tròn môi, đừng đọc thành âm 'ch'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "leaflet",
        "lemma": "leaflet",
        "pos": ["noun"],
        "ipa": {"us": "/ˈliːflət/", "uk": "/ˈliːflət/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "leaflet-1",
                "meaning_vi": "Tờ rơi quảng cáo hoặc truyền đơn thông tin (thường là 1 tờ in 2 mặt)",
                "note_vi": "Được phát trực tiếp trên đường phố hoặc để tại các quầy thông tin."
            }
        ],
        "confused_words": [
            {
                "word": "leaf",
                "ipa": "/liːf/",
                "difference_vi": "Leaf là chiếc lá cây; leaflet là tờ rơi thông tin."
            },
            {
                "word": "flyer",
                "ipa": "/ˈflaɪər/",
                "difference_vi": "Flyer và leaflet đều là tờ rơi, flyer thường là 1 tờ đơn giản in màu, leaflet có thể gấp lại thành các nếp."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Informational leaflet = tờ rơi cung cấp thông tin y tế/chỉ dẫn; marketing leaflet = tờ rơi khuyến mãi giảm giá."
            }
        ],
        "collocations": [
            {"phrase": "informational leaflet", "meaning_vi": "tờ rơi cung cấp thông tin chỉ dẫn", "evidence": "corpus"},
            {"phrase": "hand out leaflets", "meaning_vi": "phát tờ rơi tận tay", "evidence": "corpus"},
            {"phrase": "advertising leaflet", "meaning_vi": "tờ rơi quảng cáo thương mại", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "flyer", "meaning_vi": "tờ rơi"},
            {"word": "handout", "meaning_vi": "tài liệu phát tay"}
        ],
        "examples": [
            {
                "en": "Volunteers stood at the station entrance handing out leaflets about the upcoming charity event.",
                "vi": "Các tình nguyện viên đã đứng ở lối vào nhà ga để phát tờ rơi về sự kiện từ thiện sắp tới."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈliːf/, nguyên âm /iː/ dài, âm đuôi /lət/ phát âm nhanh dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "publicize",
        "lemma": "publicize",
        "pos": ["verb"],
        "ipa": {"us": "/ˈpʌblɪsaɪz/", "uk": "/ˈpʌblɪsaɪz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "publicize-1",
                "meaning_vi": "Quảng bá rộng rãi, công khai đưa tin trước công chúng",
                "note_vi": "Hành động thu hút sự chú ý của dư luận và truyền thông tới một sự kiện hoặc sản phẩm."
            }
        ],
        "confused_words": [
            {
                "word": "publish",
                "ipa": "/ˈpʌblɪʃ/",
                "difference_vi": "Publish là xuất bản sách báo; publicize là quảng bá thông tin cho công chúng biết tới."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Publicize an event = quảng bá sự kiện; publish a book = in ấn phát hành sách."
            }
        ],
        "collocations": [
            {"phrase": "widely publicize", "meaning_vi": "quảng bá rộng rãi tới công chúng", "evidence": "corpus"},
            {"phrase": "publicize an event", "meaning_vi": "đưa tin quảng bá cho một sự kiện", "evidence": "corpus"},
            {"phrase": "publicize new products", "meaning_vi": "quảng bá các dòng sản phẩm mới", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "promote", "meaning_vi": "quảng bá, xúc tiến"},
            {"word": "advertise", "meaning_vi": "chạy quảng cáo"},
            {"word": "broadcast", "meaning_vi": "phát sóng thông điệp"}
        ],
        "examples": [
            {
                "en": "We used social media channels to publicize the grand opening of our flagship store.",
                "vi": "Chúng tôi đã sử dụng các kênh mạng xã hội để quảng bá cho lễ khai trương cửa hàng trọng điểm của mình."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈpʌb/, âm cuối là nhị trùng âm /saɪz/ kết thúc bằng âm rung /z/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "slogan",
        "lemma": "slogan",
        "pos": ["noun"],
        "ipa": {"us": "/ˈsloʊɡən/", "uk": "/ˈsləʊɡən/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "slogan-1",
                "meaning_vi": "Khẩu hiệu quảng cáo, câu tiêu ngữ ngắn gọn dễ nhớ của thương hiệu",
                "note_vi": "Câu khẩu hiệu ấn tượng gắn liền với định vị thương hiệu trong tâm trí khách hàng."
            }
        ],
        "confused_words": [
            {
                "word": "motto",
                "ipa": "/ˈmɑːtoʊ/",
                "difference_vi": "Motto là phương châm sống hoặc lý tưởng; slogan là khẩu hiệu dùng cho chiến dịch tiếp thị thương mại."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Catchy slogan = khẩu hiệu bắt tai, dễ thuộc; campaign slogan = khẩu hiệu của chiến dịch ngắn hạn."
            }
        ],
        "collocations": [
            {"phrase": "advertising slogan", "meaning_vi": "khẩu hiệu quảng cáo thương mại", "evidence": "corpus"},
            {"phrase": "catchy slogan", "meaning_vi": "câu khẩu hiệu lôi cuốn, dễ nhớ", "evidence": "corpus"},
            {"phrase": "memorable campaign slogan", "meaning_vi": "khẩu hiệu chiến dịch đáng nhớ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "tagline", "meaning_vi": "câu định vị thương hiệu"},
            {"word": "catchphrase", "meaning_vi": "câu nói cửa miệng tạo trào lưu"}
        ],
        "examples": [
            {
                "en": "The creative team came up with a memorable slogan that boosted brand recognition instantly.",
                "vi": "Đội ngũ sáng tạo đã nghĩ ra một câu khẩu hiệu đáng nhớ giúp nâng cao độ nhận diện thương hiệu ngay tức thì."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈsloʊ/, nhị trùng âm /oʊ/ mở rồi thu nhỏ vành môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "brand",
        "lemma": "brand",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/brænd/", "uk": "/brænd/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "brand-1",
                "meaning_vi": "Thương hiệu, nhãn hiệu sản phẩm; (v) xây dựng nhận thức thương hiệu",
                "note_vi": "Khái niệm cốt lõi trong marketing bao gồm cả tên gọi, logo, uy tín và cảm nhận người dùng."
            }
        ],
        "confused_words": [
            {
                "word": "blend",
                "ipa": "/blend/",
                "difference_vi": "Blend là sự pha trộn hỗn hợp; brand là nhãn hiệu thương hiệu."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Brand loyalty = lòng trung thành với thương hiệu; brand awareness = mức độ nhận biết thương hiệu của công chúng."
            }
        ],
        "collocations": [
            {"phrase": "brand awareness", "meaning_vi": "độ nhận diện thương hiệu", "evidence": "corpus"},
            {"phrase": "brand loyalty", "meaning_vi": "lòng trung thành của người dùng với nhãn hiệu", "evidence": "corpus"},
            {"phrase": "build a strong brand", "meaning_vi": "xây dựng thương hiệu vững mạnh", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "trademark", "meaning_vi": "nhãn hiệu đã đăng ký bản quyền"},
            {"word": "label", "meaning_vi": "nhãn mác"}
        ],
        "examples": [
            {
                "en": "Investing in quality packaging helps build a strong brand image in the retail market.",
                "vi": "Đầu tư vào bao bì chất lượng giúp xây dựng hình ảnh thương hiệu vững chắc trên thị trường bán lẻ."
            }
        ],
        "pronunciation_tips_vi": "Phát âm cụm phụ âm /br/ nhanh, nguyên âm /æ/ bẹt miệng, âm đuôi /nd/ ngân nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "sponsor",
        "lemma": "sponsor",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/ˈspɑːnsər/", "uk": "/ˈspɒnsə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "sponsor-1",
                "meaning_vi": "Tài trợ kinh phí cho một sự kiện hoặc chương trình; (n) nhà tài trợ",
                "note_vi": "Đổi lại quyền lợi gắn logo hoặc quảng bá thương hiệu trong khuôn khổ sự kiện."
            }
        ],
        "confused_words": [
            {
                "word": "spousal",
                "ipa": "/ˈspaʊzl/",
                "difference_vi": "Spousal là thuộc về hôn phối vợ chồng; sponsor là người tài trợ hoặc động từ tài trợ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Corporate sponsor = nhà tài trợ doanh nghiệp; visa sponsor = đơn vị bảo lãnh thị thực."
            }
        ],
        "collocations": [
            {"phrase": "sponsor an event", "meaning_vi": "tài trợ cho một sự kiện", "evidence": "corpus"},
            {"phrase": "corporate sponsor", "meaning_vi": "nhà tài trợ cấp doanh nghiệp", "evidence": "corpus"},
            {"phrase": "official sponsor", "meaning_vi": "nhà tài trợ chính thức", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "fund", "meaning_vi": "rót vốn, cấp tiền"},
            {"word": "finance", "meaning_vi": "tài trợ kinh phí"},
            {"word": "back", "meaning_vi": "hậu thuẫn tài chính"}
        ],
        "examples": [
            {
                "en": "Several major tech corporations agreed to sponsor the international robotics exhibition.",
                "vi": "Một số tập đoàn công nghệ lớn đã đồng ý tài trợ cho triển lãm chế tạo robot quốc tế."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ nhất /ˈspɑːn/, âm 'o' trong US phát âm là /ɑː/ dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "segment",
        "lemma": "segment",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈseɡmənt/", "uk": "/ˈseɡmənt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["marketing-advertising"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "segment-1",
                "meaning_vi": "Phân khúc thị trường hoặc nhóm khách hàng đặc thù; (v) phân khúc hóa",
                "note_vi": "Khi là động từ, phát âm thường chuyển trọng âm thành /seɡˈment/."
            }
        ],
        "confused_words": [
            {
                "word": "sediment",
                "ipa": "/ˈsedɪmənt/",
                "difference_vi": "Sediment là chất cặn lắng tích tụ; segment là phân khúc thị trường hoặc mẩu đoạn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Market segment là phân khúc thị trường; TV segment là một chuyên mục phát sóng trên truyền hình."
            }
        ],
        "collocations": [
            {"phrase": "market segment", "meaning_vi": "phân khúc thị trường", "evidence": "corpus"},
            {"phrase": "key customer segment", "meaning_vi": "phân khúc khách hàng trọng điểm", "evidence": "corpus"},
            {"phrase": "segment the audience", "meaning_vi": "phân loại nhóm khán thính giả", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "section", "meaning_vi": "phần, mục"},
            {"word": "sector", "meaning_vi": "khu vực thị trường"},
            {"word": "division", "meaning_vi": "sự phân chia"}
        ],
        "examples": [
            {
                "en": "Our marketing strategy focuses on the premium market segment where profit margins are higher.",
                "vi": "Chiến lược tiếp thị của chúng tôi tập trung vào phân khúc thị trường cao cấp nơi có biên lợi nhuận cao hơn."
            }
        ],
        "pronunciation_tips_vi": "Danh từ nhấn âm 1 /ˈseɡ-mənt/, động từ nhấn âm 2 /seɡ-ˈment/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    }
]

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "data", "lexicon")
    count = 0
    for w in words_group2:
        w_id = w["id"]
        w_lemma = w["lemma"]
        first_letter = w_lemma[0].lower()
        target_dir = os.path.join(base_dir, first_letter)
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, f"{w_id}.yaml")
        data = {"schema_version": 2}
        for k, v in w.items():
            data[k] = v
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Created: {file_path}")
        count += 1
    print(f"\n[OK] Group 2 created {count} words successfully.")

if __name__ == "__main__":
    main()
