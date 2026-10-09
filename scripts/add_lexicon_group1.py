# -*- coding: utf-8 -*-
"""
Batch generator for Lexicon Group 1:
Hợp đồng, Nhân sự & Tiền lương (21 words)
"""
import os
import yaml

words_group1 = [
    {
        "id": "provision",
        "lemma": "provision",
        "pos": ["noun"],
        "ipa": {"us": "/prəˈvɪʒn/", "uk": "/prəˈvɪʒn/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["contracts-negotiation", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "provision-1",
                "meaning_vi": "Điều khoản trong hợp đồng hoặc thỏa thuận pháp lý",
                "note_vi": "Thường dùng ở dạng số nhiều (provisions) trong văn bản hợp đồng kinh tế."
            },
            {
                "id": "provision-2",
                "meaning_vi": "Sự cung cấp, sự dự phòng chuẩn bị trước",
                "note_vi": "Cụm 'make provision for' có nghĩa là chuẩn bị trước cho tình huống tương lai."
            }
        ],
        "confused_words": [
            {
                "word": "provide",
                "ipa": "/prəˈvaɪd/",
                "difference_vi": "Provide là động từ (cung cấp), còn provision là danh từ chỉ điều khoản hoặc sự chuẩn bị."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Provision vừa có nghĩa là 'điều khoản hợp đồng', vừa có nghĩa là 'sự cung ứng/dự phòng tài chính'."
            }
        ],
        "collocations": [
            {"phrase": "under the provisions of", "meaning_vi": "theo các điều khoản của", "evidence": "corpus"},
            {"phrase": "contractual provision", "meaning_vi": "điều khoản trong hợp đồng", "evidence": "corpus"},
            {"phrase": "make provision for", "meaning_vi": "chuẩn bị trước / dự phòng cho", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "clause", "meaning_vi": "điều khoản"},
            {"word": "stipulation", "meaning_vi": "quy định ràng buộc"},
            {"word": "term", "meaning_vi": "điều khoản"}
        ],
        "examples": [
            {
                "en": "Under the provisions of the agreement, both parties must give 30 days' notice before termination.",
                "vi": "Theo các điều khoản của thỏa thuận, cả hai bên phải thông báo trước 30 ngày trước khi chấm dứt hợp đồng."
            },
            {
                "en": "The company made financial provision for potential supply chain disruptions.",
                "vi": "Công ty đã lập quỹ dự phòng tài chính cho các sự cố gián đoạn chuỗi cung ứng tiềm ẩn."
            }
        ],
        "pronunciation_tips_vi": "Âm đuôi là /ʒn/ rung nhẹ môi cong, không đọc thành âm /z/ hay /ʃ/ thông thường.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "clause",
        "lemma": "clause",
        "pos": ["noun"],
        "ipa": {"us": "/klɔːz/", "uk": "/klɔːz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["contracts-negotiation", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "clause-1",
                "meaning_vi": "Điều khoản cụ thể trong văn bản hợp đồng hoặc luật pháp",
                "note_vi": "Một phần độc lập, mang tính ràng buộc rõ ràng như điều khoản bảo mật, phạt vi phạm."
            }
        ],
        "confused_words": [
            {
                "word": "cause",
                "ipa": "/kɔːz/",
                "difference_vi": "Cause nghĩa là nguyên nhân (không có chữ 'l'), còn clause là điều khoản hợp đồng hoặc mệnh đề ngữ pháp."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Trong ngữ pháp, clause là 'mệnh đề' (gồm chủ ngữ + vị ngữ); trong kinh doanh pháp lý, clause là 'điều khoản'."
            }
        ],
        "collocations": [
            {"phrase": "confidentiality clause", "meaning_vi": "điều khoản bảo mật thông tin", "evidence": "corpus"},
            {"phrase": "penalty clause", "meaning_vi": "điều khoản phạt vi phạm hợp đồng", "evidence": "corpus"},
            {"phrase": "insert a clause", "meaning_vi": "chèn thêm một điều khoản", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "provision", "meaning_vi": "điều khoản"},
            {"word": "section", "meaning_vi": "mục, phần"},
            {"word": "article", "meaning_vi": "điều khoản (trong luật/hiến pháp)"}
        ],
        "examples": [
            {
                "en": "We added a confidentiality clause to prevent sensitive project details from leaking.",
                "vi": "Chúng tôi đã thêm điều khoản bảo mật để ngăn thông tin nhạy cảm của dự án bị rò rỉ."
            }
        ],
        "pronunciation_tips_vi": "Phát âm phụ âm đôi /kl/ dứt khoát, nguyên âm /ɔː/ dài, âm cuối là /z/ rung thanh quản.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "breach",
        "lemma": "breach",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/briːtʃ/", "uk": "/briːtʃ/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["contracts-negotiation", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "breach-1",
                "meaning_vi": "Sự vi phạm thỏa thuận, hợp đồng hoặc quy định an ninh; (v) vi phạm",
                "note_vi": "Xuất hiện thường xuyên trong bối cảnh tranh chấp pháp lý và an toàn dữ liệu số."
            }
        ],
        "confused_words": [
            {
                "word": "bleach",
                "ipa": "/bliːtʃ/",
                "difference_vi": "Bleach là chất tẩy trắng (/l/), còn breach là sự vi phạm (/r/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Breach ngoài nghĩa vi phạm quy định còn có nghĩa là 'chỗ thủng rách' ở bức tường thành phòng thủ."
            }
        ],
        "collocations": [
            {"phrase": "breach of contract", "meaning_vi": "sự vi phạm hợp đồng", "evidence": "corpus"},
            {"phrase": "security breach", "meaning_vi": "lỗ hổng / sự cố vi phạm an ninh dữ liệu", "evidence": "corpus"},
            {"phrase": "material breach", "meaning_vi": "vi phạm nghiêm trọng (trọng yếu)", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "violation", "meaning_vi": "sự vi phạm"},
            {"word": "infringement", "meaning_vi": "sự xâm phạm bản quyền/luật lệ"}
        ],
        "examples": [
            {
                "en": "Failing to deliver the equipment on schedule constituted a material breach of contract.",
                "vi": "Việc không giao thiết bị đúng hạn đã cấu thành sự vi phạm hợp đồng nghiêm trọng."
            }
        ],
        "pronunciation_tips_vi": "Nguyên âm /iː/ kéo dài, âm cuối bật /tʃ/ rõ ràng, phân biệt với âm /ʃ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "compromise",
        "lemma": "compromise",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈkɑːmprəmaɪz/", "uk": "/ˈkɒmprəmaɪz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["contracts-negotiation", "meetings-office"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "compromise-1",
                "meaning_vi": "Sự thỏa hiệp, nhân nhượng lẫn nhau; (v) đi đến thỏa hiệp",
                "note_vi": "Giải pháp dung hòa khi hai bên có ý kiến hoặc lợi ích khác nhau."
            },
            {
                "id": "compromise-2",
                "meaning_vi": "Làm tổn hại, gây nguy hiểm hoặc làm suy giảm chất lượng/an toàn",
                "note_vi": "Thường gặp: compromise on quality (hạ chuẩn chất lượng), compromise system security."
            }
        ],
        "confused_words": [
            {
                "word": "compose",
                "ipa": "/kəmˈpoʊz/",
                "difference_vi": "Compose nghĩa là sáng tác, tạo thành; còn compromise là thỏa hiệp hoặc làm tổn hại."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Compromise mang nghĩa tích cực là 'đạt được thỏa hiệp', nhưng mang nghĩa tiêu cực là 'làm giảm sút uy tín/chất lượng'."
            }
        ],
        "collocations": [
            {"phrase": "reach a compromise", "meaning_vi": "đạt được sự thỏa hiệp", "evidence": "corpus"},
            {"phrase": "compromise on quality", "meaning_vi": "hạ thấp / nhân nhượng về mặt chất lượng", "evidence": "corpus"},
            {"phrase": "acceptable compromise", "meaning_vi": "sự thỏa hiệp có thể chấp nhận được", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "settlement", "meaning_vi": "sự dàn xếp thỏa thuận"},
            {"word": "concession", "meaning_vi": "sự nhượng bộ"}
        ],
        "examples": [
            {
                "en": "Both negotiating teams made concessions to reach an acceptable compromise.",
                "vi": "Cả hai đội đàm phán đều đưa ra nhượng bộ để đạt được sự thỏa hiệp chấp nhận được."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈkɑːm/, đuôi âm là /aɪz/ với âm /z/ rung rõ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "binding",
        "lemma": "binding",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈbaɪndɪŋ/", "uk": "/ˈbaɪndɪŋ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["contracts-negotiation", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "binding-1",
                "meaning_vi": "Có tính ràng buộc về mặt pháp lý hoặc nghĩa vụ",
                "note_vi": "Các bên bắt buộc phải tuân theo và chịu trách nhiệm trước pháp luật nếu vi phạm."
            }
        ],
        "confused_words": [
            {
                "word": "blind",
                "ipa": "/blaɪnd/",
                "difference_vi": "Blind nghĩa là khiếm thị/mù quáng; binding là có tính ràng buộc pháp lý."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Binding là tính từ 'ràng buộc pháp lý', nhưng danh từ binding lại là 'gáy sách/bìa đóng sách'."
            }
        ],
        "collocations": [
            {"phrase": "legally binding", "meaning_vi": "ràng buộc về mặt pháp lý", "evidence": "corpus"},
            {"phrase": "binding agreement", "meaning_vi": "thỏa thuận có tính ràng buộc", "evidence": "corpus"},
            {"phrase": "binding arbitration", "meaning_vi": "phán quyết trọng tài có tính ràng buộc", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "obligatory", "meaning_vi": "mang tính bắt buộc"},
            {"word": "enforceable", "meaning_vi": "có thể thực thi theo luật"}
        ],
        "examples": [
            {
                "en": "Once signed by both parties, this document becomes a legally binding agreement.",
                "vi": "Sau khi được cả hai bên ký kết, văn bản này trở thành một thỏa thuận có tính ràng buộc pháp lý."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu là nhị trùng âm /aɪ/ ('bai-nd-ing'), nhấn mạnh âm tiết đầu tiên.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "party",
        "lemma": "party",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpɑːrti/", "uk": "/ˈpɑːti/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["contracts-negotiation", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "party-1",
                "meaning_vi": "Bên tham gia vào hợp đồng, thỏa thuận hoặc tranh chấp pháp lý",
                "note_vi": "Trong ngữ cảnh thương mại và pháp lý, party luôn có nghĩa là đối tác/bên ký kết, không phải bữa tiệc."
            }
        ],
        "confused_words": [
            {
                "word": "partner",
                "ipa": "/ˈpɑːrtnər/",
                "difference_vi": "Partner là đối tác đồng hành dài hạn; party là bên ký kết cụ thể trong một văn bản pháp lý."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Party thông thường là bữa tiệc hoặc đảng phái chính trị; trong TOEIC Speaking thương mại luôn chỉ bên tham gia hợp đồng."
            }
        ],
        "collocations": [
            {"phrase": "third party", "meaning_vi": "bên thứ ba", "evidence": "corpus"},
            {"phrase": "contracting parties", "meaning_vi": "các bên ký kết hợp đồng", "evidence": "corpus"},
            {"phrase": "interested party", "meaning_vi": "bên có quyền lợi liên quan", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "signatory", "meaning_vi": "bên ký tên"},
            {"word": "participant", "meaning_vi": "người / bên tham gia"}
        ],
        "examples": [
            {
                "en": "Confidential details cannot be disclosed to any third party without written consent.",
                "vi": "Các chi tiết mật không được tiết lộ cho bất kỳ bên thứ ba nào nếu không có văn bản đồng ý."
            }
        ],
        "pronunciation_tips_vi": "Trong tiếng Anh-Mỹ (US), âm /t/ giữa hai nguyên âm thường hóa thành âm flap [ɾ], nghe nhẹ như âm 'd' mềm.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "specify",
        "lemma": "specify",
        "pos": ["verb"],
        "ipa": {"us": "/ˈspesɪfaɪ/", "uk": "/ˈspesɪfaɪ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["contracts-negotiation", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "specify-1",
                "meaning_vi": "Chỉ rõ, định rõ, nêu rõ chi tiết cụ thể",
                "note_vi": "Thường dùng trong các hướng dẫn, tiêu chuẩn kỹ thuật hoặc điều khoản hợp đồng."
            }
        ],
        "confused_words": [
            {
                "word": "specific",
                "ipa": "/spəˈsɪfɪk/",
                "difference_vi": "Specific là tính từ (cụ thể), trọng âm 2; specify là động từ (chỉ rõ), trọng âm 1."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Specify là chỉ rõ bằng văn bản hay lời nói; phân biệt với state (phát biểu chung chung)."
            }
        ],
        "collocations": [
            {"phrase": "clearly specify", "meaning_vi": "nêu rõ, chỉ định rõ ràng", "evidence": "corpus"},
            {"phrase": "specify the requirements", "meaning_vi": "nêu rõ các yêu cầu", "evidence": "corpus"},
            {"phrase": "unless otherwise specified", "meaning_vi": "trừ khi có quy định khác", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "state", "meaning_vi": "tuyên bố, nêu rõ"},
            {"word": "stipulate", "meaning_vi": "quy định cụ thể"},
            {"word": "indicate", "meaning_vi": "chỉ ra"}
        ],
        "examples": [
            {
                "en": "The contract clearly specifies delivery deadlines and penalty rates for delays.",
                "vi": "Hợp đồng nêu rõ thời hạn giao hàng và mức phạt đối với sự chậm trễ."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ nhất /ˈspes/, âm cuối là nhị trùng âm /aɪ/ rõ nét.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "establish",
        "lemma": "establish",
        "pos": ["verb"],
        "ipa": {"us": "/ɪˈstæblɪʃ/", "uk": "/ɪˈstæblɪʃ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["contracts-negotiation", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "establish-1",
                "meaning_vi": "Thiết lập, thành lập (công ty, mối quan hệ, quy trình chuẩn)",
                "note_vi": "Dùng khi bắt đầu tạo lập một tổ chức hoặc hệ thống vận hành có tính bền vững."
            }
        ],
        "confused_words": [
            {
                "word": "found",
                "ipa": "/faʊnd/",
                "difference_vi": "Found nghĩa là sáng lập tổ chức ban đầu; establish bao hàm cả việc tạo dựng chỗ đứng và vận hành quy chuẩn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Establish an organization (thành lập) khác với establish a fact (xác minh làm rõ một sự thật)."
            }
        ],
        "collocations": [
            {"phrase": "establish a partnership", "meaning_vi": "thiết lập quan hệ đối tác", "evidence": "corpus"},
            {"phrase": "establish guidelines", "meaning_vi": "ban hành các hướng dẫn quy chế", "evidence": "corpus"},
            {"phrase": "well-established firm", "meaning_vi": "công ty có uy tín lâu năm", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "found", "meaning_vi": "thành lập"},
            {"word": "set up", "meaning_vi": "thiết lập"},
            {"word": "institute", "meaning_vi": "ban hành, khởi xướng"}
        ],
        "examples": [
            {
                "en": "We established a strategic partnership to expand our distribution network overseas.",
                "vi": "Chúng tôi đã thiết lập quan hệ đối tác chiến lược nhằm mở rộng mạng lưới phân phối ra nước ngoài."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /stæb/, âm kết thúc là /ʃ/ tròn môi bật hơi nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "renew",
        "lemma": "renew",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈnuː/", "uk": "/rɪˈnjuː/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["contracts-negotiation", "sales-customer-service"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "renew-1",
                "meaning_vi": "Gia hạn hợp đồng, đổi mới gói dịch vụ thuê bao hoặc giấy phép",
                "note_vi": "Kéo dài hiệu lực của một văn bản hoặc thỏa thuận sẵn có thêm một kỳ hạn mới."
            }
        ],
        "confused_words": [
            {
                "word": "resume",
                "ipa": "/rɪˈzuːm/",
                "difference_vi": "Resume là tiếp tục lại sau khi tạm dừng; renew là gia hạn hiệu lực hợp đồng hoặc giấy phép."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Renew a contract (gia hạn hợp đồng) khác với renewable energy (năng lượng tái tạo)."
            }
        ],
        "collocations": [
            {"phrase": "renew a contract", "meaning_vi": "gia hạn hợp đồng", "evidence": "corpus"},
            {"phrase": "renew a subscription", "meaning_vi": "gia hạn gói đăng ký dịch vụ", "evidence": "corpus"},
            {"phrase": "automatically renew", "meaning_vi": "tự động gia hạn", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "extend", "meaning_vi": "kéo dài kỳ hạn"},
            {"word": "continue", "meaning_vi": "tiếp tục duy trì"}
        ],
        "examples": [
            {
                "en": "The tenant decided to renew the office lease for another two years.",
                "vi": "Bên thuê đã quyết định gia hạn hợp đồng thuê văn phòng thêm hai năm nữa."
            }
        ],
        "pronunciation_tips_vi": "Giọng Mỹ đọc là /rɪˈnuː/ (âm 'u' dài), giọng Anh đọc là /rɪˈnjuː/ có phụ âm đệm /j/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "reference",
        "lemma": "reference",
        "pos": ["noun"],
        "ipa": {"us": "/ˈrefrəns/", "uk": "/ˈrefrəns/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["human-resources", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "reference-1",
                "meaning_vi": "Thư giới thiệu, người xác nhận tham chiếu lý lịch ứng viên",
                "note_vi": "Người có thể cung cấp chứng thực về năng lực làm việc và tư cách đạo đức của người tìm việc."
            }
        ],
        "confused_words": [
            {
                "word": "referee",
                "ipa": "/ˌrefəˈriː/",
                "difference_vi": "Referee là trọng tài thể thao hoặc người tham chiếu tại Anh; reference là thư giới thiệu hoặc thông tin tham chiếu."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Reference trong tuyển dụng là người/thư tham chiếu; trong tài liệu là sự trích dẫn nguồn tài liệu tham khảo."
            }
        ],
        "collocations": [
            {"phrase": "check references", "meaning_vi": "xác minh thông tin người tham chiếu", "evidence": "corpus"},
            {"phrase": "professional reference", "meaning_vi": "người tham chiếu chuyên môn", "evidence": "corpus"},
            {"phrase": "letters of reference", "meaning_vi": "thư giới thiệu năng lực", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "recommendation", "meaning_vi": "sự tiến cử, lời khuyên"},
            {"word": "endorsement", "meaning_vi": "sự bảo đảm uy tín"}
        ],
        "examples": [
            {
                "en": "The hiring committee checked all three references before making a final job offer.",
                "vi": "Hội đồng tuyển dụng đã kiểm tra cả ba người tham chiếu trước khi đưa ra lời mời nhận việc chính thức."
            }
        ],
        "pronunciation_tips_vi": "Từ này có 2 hoặc 3 âm tiết /ˈref-rəns/, trọng âm rơi vào âm đầu tiên, đừng nhấn vào âm thứ hai.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "background",
        "lemma": "background",
        "pos": ["noun"],
        "ipa": {"us": "/ˈbækɡraʊnd/", "uk": "/ˈbækɡraʊnd/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources", "describe-picture"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "background-1",
                "meaning_vi": "Nền tảng học vấn, kinh nghiệm quá khứ của một người",
                "note_vi": "Rất quan trọng trong Part 3 (phỏng vấn xin việc) và Part 2 (miêu tả hậu cảnh bức tranh)."
            }
        ],
        "confused_words": [
            {
                "word": "foreground",
                "ipa": "/ˈfɔːrɡraʊnd/",
                "difference_vi": "Foreground là tiền cảnh (phía trước bức ảnh), background là hậu cảnh (phía sau) hoặc nền tảng học vấn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Trong tranh TOEIC Part 2: background = hậu cảnh; trong hồ sơ xin việc: background = trình độ và kinh nghiệm trước đây."
            }
        ],
        "collocations": [
            {"phrase": "background check", "meaning_vi": "thẩm tra lý lịch cá nhân", "evidence": "corpus"},
            {"phrase": "educational background", "meaning_vi": "nền tảng học vấn", "evidence": "corpus"},
            {"phrase": "solid background in", "meaning_vi": "nền tảng vững chắc trong lĩnh vực", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "experience", "meaning_vi": "kinh nghiệm"},
            {"word": "qualifications", "meaning_vi": "năng lực chuyên môn"}
        ],
        "examples": [
            {
                "en": "She has a solid background in digital marketing and customer analytics.",
                "vi": "Cô ấy có nền tảng vững chắc về tiếp thị kỹ thuật số và phân tích dữ liệu khách hàng."
            },
            {
                "en": "In the background of the picture, several tall office buildings are visible.",
                "vi": "Ở phía hậu cảnh của bức ảnh, có thể nhìn thấy một vài tòa nhà văn phòng cao tầng."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép gồm 'back' và 'ground', trọng âm chính nhấn ở /ˈbæk/, nhị trùng âm /aʊ/ rõ ràng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "shortlist",
        "lemma": "shortlist",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈʃɔːrtlɪst/", "uk": "/ˈʃɔːtlɪst/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "shortlist-1",
                "meaning_vi": "Danh sách rút gọn các ứng viên xuất sắc nhất; (v) chọn vào danh sách vòng sau",
                "note_vi": "Bước lọc hồ sơ cuối cùng trước khi phỏng vấn trực tiếp hoặc bỏ phiếu tuyển dụng."
            }
        ],
        "confused_words": [
            {
                "word": "blacklist",
                "ipa": "/ˈblæklɪst/",
                "difference_vi": "Blacklist là sổ đen (danh sách loại trừ/cấm), còn shortlist là danh sách ứng viên sáng giá nhất được chọn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Shortlist có thể làm danh từ (the shortlist) hoặc động từ chủ động (we shortlisted five candidates)."
            }
        ],
        "collocations": [
            {"phrase": "shortlist candidates", "meaning_vi": "lọc ứng viên vào danh sách rút gọn", "evidence": "corpus"},
            {"phrase": "on the shortlist", "meaning_vi": "nằm trong danh sách rút gọn", "evidence": "corpus"},
            {"phrase": "make the shortlist", "meaning_vi": "lọt vào danh sách chung kết", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "select", "meaning_vi": "lựa chọn"},
            {"word": "filter", "meaning_vi": "sàng lọc"}
        ],
        "examples": [
            {
                "en": "Out of fifty applicants, only five were shortlisted for the managerial position.",
                "vi": "Trong số năm mươi ứng viên, chỉ có năm người được đưa vào danh sách rút gọn cho vị trí quản lý."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu /ʃ/ chu môi dày, nguyên âm /ɔːr/ uốn lưỡi, âm đuôi /st/ kết thúc sắc gọn.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "hire",
        "lemma": "hire",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/ˈhaɪər/", "uk": "/ˈhaɪə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "hire-1",
                "meaning_vi": "Tuyển dụng nhân viên mới; thuê thiết bị ngắn hạn",
                "note_vi": "Trong tiếng Anh-Mỹ, hire chủ yếu dùng cho tuyển dụng nhân sự (đồng nghĩa với employ)."
            }
        ],
        "confused_words": [
            {
                "word": "fire",
                "ipa": "/ˈfaɪər/",
                "difference_vi": "Fire là sa thải (ngược nghĩa hoàn toàn với hire là tuyển dụng)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Hire nhân sự (dài hạn trong US) khác với rent đồ vật (thuê trả tiền theo ngày/tháng)."
            }
        ],
        "collocations": [
            {"phrase": "hire qualified staff", "meaning_vi": "tuyển dụng nhân viên đủ tiêu chuẩn", "evidence": "corpus"},
            {"phrase": "new hire", "meaning_vi": "nhân viên mới được tuyển", "evidence": "corpus"},
            {"phrase": "freeze on hiring", "meaning_vi": "đóng băng việc tuyển dụng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "employ", "meaning_vi": "thuê nhân công, tuyển dụng"},
            {"word": "recruit", "meaning_vi": "chiêu mộ, tuyển quân"}
        ],
        "examples": [
            {
                "en": "The firm plans to hire ten software developers next quarter to support product expansion.",
                "vi": "Công ty dự định tuyển mười lập trình viên phần mềm vào quý tới để hỗ trợ việc mở rộng sản phẩm."
            }
        ],
        "pronunciation_tips_vi": "Phát âm /haɪər/ có âm họng nhẹ ở đầu và nhị trùng âm /aɪ/ kết hợp âm lướt nhẹ /ər/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "reject",
        "lemma": "reject",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈdʒekt/", "uk": "/rɪˈdʒekt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources", "production-quality-control"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "reject-1",
                "meaning_vi": "Từ chối, bác bỏ (đơn xin việc, đề xuất, sản phẩm lỗi)",
                "note_vi": "Khi là danh từ, trọng âm đổi thành /ˈriːdʒekt/ (sản phẩm phế phẩm bị loại bỏ)."
            }
        ],
        "confused_words": [
            {
                "word": "refuse",
                "ipa": "/rɪˈfjuːz/",
                "difference_vi": "Refuse là từ chối làm gì (refuse to do); reject thường đi với danh từ (reject an offer/proposal)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Động từ /rɪˈdʒekt/ (từ chối) khác với danh từ /ˈriːdʒekt/ (sản phẩm lỗi bị trả về)."
            }
        ],
        "collocations": [
            {"phrase": "reject an application", "meaning_vi": "từ chối hồ sơ ứng tuyển", "evidence": "corpus"},
            {"phrase": "reject a proposal", "meaning_vi": "bác bỏ bản đề xuất", "evidence": "corpus"},
            {"phrase": "reject rate", "meaning_vi": "tỷ lệ phế phẩm bị loại", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "turn down", "meaning_vi": "khước từ, từ chối"},
            {"word": "decline", "meaning_vi": "từ chối lịch sự"}
        ],
        "examples": [
            {
                "en": "The board rejected the merger proposal due to excessive financial risks.",
                "vi": "Hội đồng quản trị đã bác bỏ đề xuất sáp nhập do rủi ro tài chính quá lớn."
            }
        ],
        "pronunciation_tips_vi": "Động từ nhấn âm 2 /dʒekt/, chú ý âm tắc xát /dʒ/ bật mạnh ở đầu âm tiết thứ hai.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "salary",
        "lemma": "salary",
        "pos": ["noun"],
        "ipa": {"us": "/ˈsæləri/", "uk": "/ˈsæləri/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "salary-1",
                "meaning_vi": "Tiền lương cố định (thường tính theo tháng hoặc theo năm)",
                "note_vi": "Thường trả cho nhân viên văn phòng, quản lý hoặc chuyên gia hưởng lương tháng cố định."
            }
        ],
        "confused_words": [
            {
                "word": "wage",
                "ipa": "/weɪdʒ/",
                "difference_vi": "Salary là lương cố định theo tháng/năm; wage là tiền công tính theo giờ hoặc theo ngày."
            },
            {
                "word": "celery",
                "ipa": "/ˈseləri/",
                "difference_vi": "Celery là rau cần tây (bắt đầu bằng âm /s/ mềm và nguyên âm /e/), salary là tiền lương (nguyên âm /æ/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Gross salary là lương gộp trước thuế; net salary là lương thực nhận về tay sau khi trừ thuế và bảo hiểm."
            }
        ],
        "collocations": [
            {"phrase": "competitive salary", "meaning_vi": "mức lương có tính cạnh tranh cao", "evidence": "corpus"},
            {"phrase": "salary increase", "meaning_vi": "sự tăng lương", "evidence": "corpus"},
            {"phrase": "base salary", "meaning_vi": "mức lương cơ bản (chưa gồm thưởng)", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "pay", "meaning_vi": "tiền lương, tiền công"},
            {"word": "remuneration", "meaning_vi": "thù lao, lương bổng"}
        ],
        "examples": [
            {
                "en": "We offer a competitive base salary along with comprehensive health insurance benefits.",
                "vi": "Chúng tôi đưa ra mức lương cơ bản cạnh tranh cùng chế độ bảo hiểm y tế toàn diện."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈsæ/, nguyên âm /æ/ mở rộng miệng bẹt, không đọc thành 'sa-la-ri'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "wage",
        "lemma": "wage",
        "pos": ["noun"],
        "ipa": {"us": "/weɪdʒ/", "uk": "/weɪdʒ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "wage-1",
                "meaning_vi": "Tiền công trả theo giờ, theo ngày hoặc theo tuần",
                "note_vi": "Thường gắn liền với lao động trực tiếp, sản xuất nhà máy hoặc nhân viên bán thời gian."
            }
        ],
        "confused_words": [
            {
                "word": "salary",
                "ipa": "/ˈsæləri/",
                "difference_vi": "Wage tính theo giờ/tuần; salary tính theo kỳ lương hàng tháng hoặc hàng năm."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Danh từ wage là tiền công; động từ 'wage war' có nghĩa là tiến hành chiến tranh."
            }
        ],
        "collocations": [
            {"phrase": "minimum wage", "meaning_vi": "mức lương tối thiểu theo luật", "evidence": "corpus"},
            {"phrase": "hourly wage", "meaning_vi": "tiền công tính theo giờ làm", "evidence": "corpus"},
            {"phrase": "wage increase", "meaning_vi": "sự tăng tiền công lao động", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "earnings", "meaning_vi": "tiền thù lao kiếm được"},
            {"word": "pay rate", "meaning_vi": "đơn giá tiền công"}
        ],
        "examples": [
            {
                "en": "The government announced a 5% raise in the national minimum wage.",
                "vi": "Chính phủ đã công bố mức tăng 5% đối với mức lương tối thiểu quốc gia."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu là /w/, nguyên âm đôi /eɪ/, âm cuối là âm tắc xát /dʒ/ rung cổ họng rõ nét.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "pension",
        "lemma": "pension",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpenʃn/", "uk": "/ˈpenʃn/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "pension-1",
                "meaning_vi": "Lương hưu, tiền trợ cấp hưu trí định kỳ",
                "note_vi": "Khoản chi trả cố định cho nhân viên sau khi hết tuổi lao động hoặc nghỉ hưu."
            }
        ],
        "confused_words": [
            {
                "word": "tension",
                "ipa": "/ˈtenʃn/",
                "difference_vi": "Tension là sự căng thẳng áp lực; pension là tiền lương hưu trí."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "State pension là lương hưu do chính phủ chi trả; company pension plan là quỹ hưu trí do doanh nghiệp đóng góp."
            }
        ],
        "collocations": [
            {"phrase": "pension scheme", "meaning_vi": "chế độ hưu trí / chương trình lương hưu", "evidence": "corpus"},
            {"phrase": "draw a pension", "meaning_vi": "lãnh nhận tiền lương hưu", "evidence": "corpus"},
            {"phrase": "pension contribution", "meaning_vi": "khoản đóng góp vào quỹ hưu trí", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "retirement fund", "meaning_vi": "quỹ hưu trí"},
            {"word": "annuity", "meaning_vi": "tiền trợ cấp niên kim định kỳ"}
        ],
        "examples": [
            {
                "en": "All full-time employees are automatically enrolled in the corporate pension scheme.",
                "vi": "Tất cả nhân viên chính thức đều được tự động tham gia vào chương trình hưu trí của công ty."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu bật /p/, nguyên âm ngắn /e/, âm đuôi là /ʃn/ cong môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "severance",
        "lemma": "severance",
        "pos": ["noun"],
        "ipa": {"us": "/ˈsevərəns/", "uk": "/ˈsevərəns/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "severance-1",
                "meaning_vi": "Khoản trợ cấp thôi việc khi chấm dứt hợp đồng lao động",
                "note_vi": "Gói tài chính đền bù cho người lao động khi công ty cắt giảm biên chế hoặc giải thể."
            }
        ],
        "confused_words": [
            {
                "word": "severe",
                "ipa": "/sɪˈvɪr/",
                "difference_vi": "Severe là tính từ (nghiêm trọng, khốc liệt); severance là danh từ (khoản trợ cấp thôi việc)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Severance bắt nguồn từ động từ sever (cắt đứt); trong nhân sự luôn đi với severance package (gói đền bù nghỉ việc)."
            }
        ],
        "collocations": [
            {"phrase": "severance pay", "meaning_vi": "tiền trợ cấp thôi việc", "evidence": "corpus"},
            {"phrase": "severance package", "meaning_vi": "gói quyền lợi đền bù thôi việc", "evidence": "corpus"},
            {"phrase": "receive severance", "meaning_vi": "nhận khoản trợ cấp thôi việc", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "redundancy pay", "meaning_vi": "khoản bồi thường khi giảm biên chế"},
            {"word": "compensation", "meaning_vi": "tiền đền bù, thù lao"}
        ],
        "examples": [
            {
                "en": "Staff members affected by the factory closure will receive a generous severance package.",
                "vi": "Những nhân viên bị ảnh hưởng bởi việc đóng cửa nhà máy sẽ nhận được gói trợ cấp thôi việc thỏa đáng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈsev/, âm giữa lướt nhẹ /ər/, kết thúc bằng /əns/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "bonus",
        "lemma": "bonus",
        "pos": ["noun"],
        "ipa": {"us": "/ˈboʊnəs/", "uk": "/ˈbəʊnəs/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "bonus-1",
                "meaning_vi": "Tiền thưởng thêm ngoài lương cơ bản nhờ thành tích tốt",
                "note_vi": "Khoản chi thêm theo quý, năm hoặc dự án để khuyến khích tinh thần làm việc."
            }
        ],
        "confused_words": [
            {
                "word": "bone",
                "ipa": "/boʊn/",
                "difference_vi": "Bone là xương; bonus là tiền thưởng hoặc phần thưởng cộng thêm."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Bonus trong tiền lương là tiền thưởng; trong đời sống bonus là lợi ích thêm ngoài dự kiến ('as a bonus')."
            }
        ],
        "collocations": [
            {"phrase": "annual bonus", "meaning_vi": "tiền thưởng hàng năm", "evidence": "corpus"},
            {"phrase": "performance bonus", "meaning_vi": "tiền thưởng dựa theo năng suất làm việc", "evidence": "corpus"},
            {"phrase": "receive a bonus", "meaning_vi": "nhận khoản tiền thưởng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "incentive", "meaning_vi": "khoản khích lệ, tiền thưởng"},
            {"word": "reward", "meaning_vi": "phần thưởng"}
        ],
        "examples": [
            {
                "en": "Sales representatives who exceed their targets receive a quarterly performance bonus.",
                "vi": "Đại diện bán hàng vượt chỉ tiêu sẽ nhận được khoản tiền thưởng hiệu suất theo quý."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu là nhị trùng âm /oʊ/ (giọng Mỹ) hoặc /əʊ/ (giọng Anh), âm thứ hai là /nəs/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "allowance",
        "lemma": "allowance",
        "pos": ["noun"],
        "ipa": {"us": "/əˈlaʊəns/", "uk": "/əˈlaʊəns/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["salary-benefits", "human-resources"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "allowance-1",
                "meaning_vi": "Khoản phụ cấp hỗ trợ cho các chi phí cụ thể (đi lại, ăn ở, công tác)",
                "note_vi": "Tiền cấp thêm để bù đắp các chi phí phát sinh trong quá trình thực hiện công vụ."
            },
            {
                "id": "allowance-2",
                "meaning_vi": "Định mức tiêu chuẩn cho phép (như hành lý mang theo)",
                "note_vi": "Thường gặp trong ngành du lịch/hàng không: baggage allowance (định mức hành lý miễn cước)."
            }
        ],
        "confused_words": [
            {
                "word": "allow",
                "ipa": "/əˈlaʊ/",
                "difference_vi": "Allow là động từ (cho phép); allowance là danh từ (khoản tiền phụ cấp hoặc định mức cho phép)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Allowance cho nhân viên là phụ cấp tiền tệ; baggage allowance trong sân bay là hạn mức cân nặng hành lý."
            }
        ],
        "collocations": [
            {"phrase": "travel allowance", "meaning_vi": "phụ cấp công tác / đi lại", "evidence": "corpus"},
            {"phrase": "meal allowance", "meaning_vi": "phụ cấp tiền ăn", "evidence": "corpus"},
            {"phrase": "baggage allowance", "meaning_vi": "định mức hành lý được mang theo", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "stipend", "meaning_vi": "khoản sinh hoạt phí, phụ cấp"},
            {"word": "subsidy", "meaning_vi": "tiền trợ cấp, hỗ trợ giá"}
        ],
        "examples": [
            {
                "en": "Engineers working on remote construction sites are entitled to a daily housing allowance.",
                "vi": "Các kỹ sư làm việc tại các công trường vùng xa được hưởng khoản phụ cấp nhà ở hàng ngày."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /laʊ/, nhị trùng âm /aʊ/ mở to khẩu hình.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "remuneration",
        "lemma": "remuneration",
        "pos": ["noun"],
        "ipa": {"us": "/rɪˌmjuːnəˈreɪʃn/", "uk": "/rɪˌmjuːnəˈreɪʃn/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 800+"},
        "topics": ["salary-benefits", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "remuneration-1",
                "meaning_vi": "Khoản thù lao, tiền công và các đãi ngộ tài chính trả cho công việc",
                "note_vi": "Thuật ngữ trang trọng bao hàm cả tiền lương, tiền thưởng và các quyền lợi đãi ngộ khác."
            }
        ],
        "confused_words": [
            {
                "word": "renovation",
                "ipa": "/ˌrenəˈveɪʃn/",
                "difference_vi": "Renovation là sự cải tạo nâng cấp công trình; remuneration là tiền thù lao đãi ngộ lao động."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Remuneration là thuật ngữ tài chính/pháp lý chính thức, rộng hơn từ pay hoặc salary."
            }
        ],
        "collocations": [
            {"phrase": "remuneration package", "meaning_vi": "gói thù lao đãi ngộ tổng thể", "evidence": "corpus"},
            {"phrase": "adequate remuneration", "meaning_vi": "mức thù lao xứng đáng, thỏa đáng", "evidence": "corpus"},
            {"phrase": "remuneration committee", "meaning_vi": "ủy ban thẩm định lương thưởng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "compensation", "meaning_vi": "tiền thù lao, bồi hoàn"},
            {"word": "earnings", "meaning_vi": "thu nhập"}
        ],
        "examples": [
            {
                "en": "The executive remuneration package includes base salary, stock options, and private medical cover.",
                "vi": "Gói thù lao dành cho cấp quản lý bao gồm lương cơ bản, quyền mua cổ phiếu và bảo hiểm y tế tư nhân."
            }
        ],
        "pronunciation_tips_vi": "Từ có 5 âm tiết, trọng âm chính rơi vào âm tiết thứ tư /reɪ/, đừng nhầm chữ 'm' và 'n' (re-mu-ne-ra-tion).",
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
    for w in words_group1:
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
    print(f"\n[OK] Group 1 created {count} words successfully.")

if __name__ == "__main__":
    main()
