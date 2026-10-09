# -*- coding: utf-8 -*-
"""
Batch generator for Lexicon Group 4A:
Văn phòng, Nhân sự bổ sung & Bất động sản (27 words)
"""
import os
import yaml

words_group4a = [
    {
        "id": "entitled",
        "lemma": "entitled",
        "pos": ["adjective"],
        "ipa": {"us": "/ɪnˈtaɪtld/", "uk": "/ɪnˈtaɪtld/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["human-resources", "salary-benefits"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "entitled-1",
                "meaning_vi": "Được quyền hưởng, đủ tư cách thụ hưởng quyền lợi hoặc trợ cấp",
                "note_vi": "Cấu trúc kinh điển: be entitled to + danh từ / be entitled to do sth."
            }
        ],
        "confused_words": [
            {
                "word": "titled",
                "ipa": "/ˈtaɪtld/",
                "difference_vi": "Titled là có tựa đề hoặc có tước vị; entitled là được quyền hưởng chế độ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Be entitled to benefits = được quyền hưởng trợ cấp; an entitled attitude = thái độ ngạo mạn tự cho mình là trung tâm."
            }
        ],
        "collocations": [
            {"phrase": "entitled to benefits", "meaning_vi": "được quyền hưởng các khoản phúc lợi", "evidence": "corpus"},
            {"phrase": "entitled to a full refund", "meaning_vi": "được quyền nhận lại toàn bộ tiền hoàn", "evidence": "corpus"},
            {"phrase": "entitled to paid leave", "meaning_vi": "được quyền nghỉ phép hưởng nguyên lương", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "eligible", "meaning_vi": "đủ điều kiện, đủ tiêu chuẩn"},
            {"word": "authorized", "meaning_vi": "được phép, có thẩm quyền"}
        ],
        "examples": [
            {
                "en": "Full-time employees are entitled to fifteen days of paid annual leave each year.",
                "vi": "Nhân viên chính thức được quyền hưởng mười lăm ngày nghỉ phép thường niên có lương mỗi năm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈtaɪt/, âm cuối /ld/ phát âm uốn lưỡi nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "subordinate",
        "lemma": "subordinate",
        "pos": ["noun", "adjective"],
        "ipa": {"us": "/səˈbɔːrdɪnət/", "uk": "/səˈbɔːdɪnət/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["human-resources", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "subordinate-1",
                "meaning_vi": "Cấp dưới, nhân viên dưới quyền; (adj) có vị trí thấp hơn trong tổ chức",
                "note_vi": "Khi là động từ (làm cho phụ thuộc), phát âm chuyển thành /səˈbɔːrdɪneɪt/."
            }
        ],
        "confused_words": [
            {
                "word": "coordinate",
                "ipa": "/koʊˈɔːrdɪneɪt/",
                "difference_vi": "Coordinate là điều phối ngang hàng; subordinate là cấp bậc thấp hơn trực tiếp."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Danh từ và tính từ đọc đuôi /-nət/; động từ đọc đuôi /-neɪt/."
            }
        ],
        "collocations": [
            {"phrase": "manage subordinates", "meaning_vi": "quản lý các nhân viên cấp dưới", "evidence": "corpus"},
            {"phrase": "subordinate role", "meaning_vi": "vai trò phụ thuộc, thứ yếu", "evidence": "corpus"},
            {"phrase": "treat subordinates fairly", "meaning_vi": "đối xử công bằng với nhân viên dưới quyền", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "assistant", "meaning_vi": "trợ tá"},
            {"word": "junior", "meaning_vi": "cấp dưới, ít thâm niên"},
            {"word": "underling", "meaning_vi": "người dưới quyền"}
        ],
        "examples": [
            {
                "en": "Effective leaders know how to delegate tasks and inspire confidence in their subordinates.",
                "vi": "Những nhà lãnh đạo hiệu quả biết cách giao phó nhiệm vụ và truyền cảm hứng tự tin cho cấp dưới của mình."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /ˈbɔːr/, đuôi danh từ phát âm là /nət/ ngắn.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "reimbursement",
        "lemma": "reimbursement",
        "pos": ["noun"],
        "ipa": {"us": "/ˌriːɪmˈbɜːrsmənt/", "uk": "/ˌriːɪmˈbɜːsmənt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["finance-accounting", "salary-benefits"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "reimbursement-1",
                "meaning_vi": "Khoản hoàn trả chi phí công tác hoặc thanh toán bồi hoàn số tiền đã ứng trước",
                "note_vi": "Quy trình nhân viên nộp hóa đơn công tác để kế toán trả lại tiền túi đã bỏ ra."
            }
        ],
        "confused_words": [
            {
                "word": "refund",
                "ipa": "/ˈriːfʌnd/",
                "difference_vi": "Refund là hoàn tiền mua sắm cho khách hàng; reimbursement là bồi hoàn chi phí công tác cho nhân viên."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Travel expense reimbursement = bồi hoàn chi phí đi lại; tuition reimbursement = hỗ trợ hoàn trả học phí nâng cao nghiệp vụ."
            }
        ],
        "collocations": [
            {"phrase": "seek reimbursement", "meaning_vi": "nộp đơn yêu cầu thanh toán bồi hoàn", "evidence": "corpus"},
            {"phrase": "travel reimbursement", "meaning_vi": "khoản bồi hoàn công tác phí", "evidence": "corpus"},
            {"phrase": "reimbursement claim", "meaning_vi": "hồ sơ đề nghị bồi hoàn chi phí", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "repayment", "meaning_vi": "sự trả lại tiền"},
            {"word": "compensation", "meaning_vi": "khoản đền bù bồi hoàn"}
        ],
        "examples": [
            {
                "en": "Staff members must submit original itemized receipts within thirty days to receive travel reimbursement.",
                "vi": "Nhân viên phải nộp hóa đơn chi tiết bản gốc trong vòng 30 ngày để nhận bồi hoàn công tác phí."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ ba /ˈbɜːrs/, chú ý âm /r/ uốn lưỡi và âm /s/ kết hợp đuôi /mənt/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "promotion",
        "lemma": "promotion",
        "pos": ["noun"],
        "ipa": {"us": "/prəˈmoʊʃn/", "uk": "/prəˈməʊʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["human-resources", "marketing-advertising"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "promotion-1",
                "meaning_vi": "Sự thăng chức, đề bạt lên vị trí công tác cao hơn trong công ty",
                "note_vi": "Ngược nghĩa với demotion (sự giáng chức)."
            },
            {
                "id": "promotion-2",
                "meaning_vi": "Chương trình khuyến mãi giảm giá; chiến dịch quảng bá tiếp thị",
                "note_vi": "Thường thấy trong sales: promotional offer, special promotion."
            }
        ],
        "confused_words": [
            {
                "word": "demotion",
                "ipa": "/dɪˈmoʊʃn/",
                "difference_vi": "Promotion là thăng cấp hoặc khuyến mãi; demotion là giáng chức."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Job promotion = thăng tiến nghề nghiệp; sales promotion = khuyến mãi kích cầu mua sắm."
            }
        ],
        "collocations": [
            {"phrase": "earn a promotion", "meaning_vi": "đạt được sự thăng chức xứng đáng", "evidence": "corpus"},
            {"phrase": "sales promotion", "meaning_vi": "chương trình xúc tiến khuyến mãi", "evidence": "corpus"},
            {"phrase": "promotion opportunity", "meaning_vi": "cơ hội thăng tiến nghề nghiệp", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "advancement", "meaning_vi": "sự tiến bộ, thăng tiến"},
            {"word": "advertising", "meaning_vi": "hoạt động quảng bá"}
        ],
        "examples": [
            {
                "en": "Her exceptional leadership during the regional restructuring earned her a well-deserved promotion to director.",
                "vi": "Khả năng lãnh đạo xuất sắc trong đợt tái cấu trúc khu vực đã giúp cô ấy được thăng chức giám đốc một cách xứng đáng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈmoʊ/, đuôi kết thúc là /ʃn/ cong môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "awareness",
        "lemma": "awareness",
        "pos": ["noun"],
        "ipa": {"us": "/əˈwernəs/", "uk": "/əˈweənəs/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "awareness-1",
                "meaning_vi": "Nhận thức, mức độ hiểu biết hoặc nhận diện về một thương hiệu / vấn đề xã hội",
                "note_vi": "Collocation kinh điển: raise awareness (nâng cao nhận thức), brand awareness (độ nhận diện thương hiệu)."
            }
        ],
        "confused_words": [
            {
                "word": "aware",
                "ipa": "/əˈwer/",
                "difference_vi": "Aware là tính từ có nhận thức; awareness là danh từ mức độ nhận thức."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Brand awareness = độ nhận diện thương hiệu trong công chúng; safety awareness = ý thức an toàn lao động."
            }
        ],
        "collocations": [
            {"phrase": "raise awareness", "meaning_vi": "nâng cao nhận thức cộng đồng", "evidence": "corpus"},
            {"phrase": "brand awareness", "meaning_vi": "mức độ nhận diện thương hiệu", "evidence": "corpus"},
            {"phrase": "environmental awareness", "meaning_vi": "ý thức bảo vệ môi trường", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "consciousness", "meaning_vi": "sự tỉnh thức, ý thức"},
            {"word": "recognition", "meaning_vi": "sự nhận biết, công nhận"}
        ],
        "examples": [
            {
                "en": "The social media campaign significantly boosted brand awareness among young urban professionals.",
                "vi": "Chiến dịch truyền thông xã hội đã nâng cao đáng kể độ nhận diện thương hiệu trong giới chuyên gia trẻ ở đô thị."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈwer/, âm đầu lướt nhẹ /ə/, kết thúc bằng /nəs/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "survey",
        "lemma": "survey",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈsɜːrveɪ/", "uk": "/ˈsɜːveɪ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "survey-1",
                "meaning_vi": "Cuộc điều tra khảo sát ý kiến; (v) tiến hành khảo sát nghiên cứu",
                "note_vi": "Công cụ lấy dữ liệu khách hàng hoặc đo lường mức độ gắn kết nhân viên."
            }
        ],
        "confused_words": [
            {
                "word": "surveillance",
                "ipa": "/sɜːrˈveɪləns/",
                "difference_vi": "Surveillance là sự giám sát camera an ninh; survey là khảo sát thăm dò ý kiến."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Customer survey = khảo sát ý kiến khách hàng; land survey = đo đạc trắc địa đất đai."
            }
        ],
        "collocations": [
            {"phrase": "conduct a survey", "meaning_vi": "tiến hành một cuộc khảo sát ý kiến", "evidence": "corpus"},
            {"phrase": "survey results", "meaning_vi": "kết quả khảo sát thống kê", "evidence": "corpus"},
            {"phrase": "customer satisfaction survey", "meaning_vi": "khảo sát mức độ hài lòng của khách hàng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "poll", "meaning_vi": "thăm dò dư luận"},
            {"word": "questionnaire", "meaning_vi": "bảng câu hỏi khảo sát"},
            {"word": "investigation", "meaning_vi": "cuộc điều tra tìm hiểu"}
        ],
        "examples": [
            {
                "en": "According to a recent employee survey, ninety percent favored a flexible hybrid work model.",
                "vi": "Theo một cuộc khảo sát nhân viên gần đây, chín mươi phần trăm ủng hộ mô hình làm việc kết hợp linh hoạt."
            }
        ],
        "pronunciation_tips_vi": "Danh từ nhấn âm 1 /ˈsɜːrveɪ/, động từ có thể nhấn âm 2 /sərˈveɪ/, âm cuối là nhị trùng âm /eɪ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "launch",
        "lemma": "launch",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/lɔːntʃ/", "uk": "/lɔːntʃ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["marketing-advertising", "sales-customer-service"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "launch-1",
                "meaning_vi": "Ra mắt, tung ra thị trường (sản phẩm, dịch vụ, chiến dịch mới); (n) lễ ra mắt",
                "note_vi": "Xuất hiện với tần suất cực cao trong phần quảng bá sản phẩm mới."
            }
        ],
        "confused_words": [
            {
                "word": "lunch",
                "ipa": "/lʌntʃ/",
                "difference_vi": "Lunch là bữa ăn trưa (nguyên âm /ʌ/); launch là ra mắt sản phẩm mới (nguyên âm dài /ɔː/). Phải phân biệt rõ ràng khi nói."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Product launch = buổi ra mắt giới thiệu sản phẩm mới; launch a rocket = phóng tên lửa."
            }
        ],
        "collocations": [
            {"phrase": "launch a new product", "meaning_vi": "tung sản phẩm mới ra thị trường", "evidence": "corpus"},
            {"phrase": "official launch date", "meaning_vi": "ngày ra mắt chính thức", "evidence": "corpus"},
            {"phrase": "launch a marketing campaign", "meaning_vi": "phát động chiến dịch tiếp thị", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "introduce", "meaning_vi": "giới thiệu ra thị trường"},
            {"word": "release", "meaning_vi": "phát hành"},
            {"word": "initiate", "meaning_vi": "khởi xướng"}
        ],
        "examples": [
            {
                "en": "The tech start-up plans to launch its flagship mobile application next month.",
                "vi": "Công ty khởi nghiệp công nghệ dự định ra mắt ứng dụng di động chủ lực của mình vào tháng tới."
            }
        ],
        "pronunciation_tips_vi": "Nguyên âm /ɔː/ dài tròn môi, kết thúc bằng âm /ntʃ/ bật hơi sắc nét, đừng nhầm với 'lunch' /lʌntʃ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "minutes",
        "lemma": "minutes",
        "pos": ["noun"],
        "ipa": {"us": "/ˈmɪnɪts/", "uk": "/ˈmɪnɪts/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["meetings-office"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "minutes-1",
                "meaning_vi": "Biên bản cuộc họp, văn bản ghi chép tóm tắt nội dung và các nghị quyết đã thông qua",
                "note_vi": "Luôn ở dạng số nhiều khi mang nghĩa biên bản cuộc họp."
            }
        ],
        "confused_words": [
            {
                "word": "minute",
                "ipa": "/maɪˈnuːt/",
                "difference_vi": "Minute tính từ là cực nhỏ, vi mô (/maɪˈnuːt/); minutes danh từ số nhiều là biên bản họp (/ˈmɪnɪts/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Minutes of the meeting = biên bản cuộc họp; five minutes = khoảng thời gian 5 phút."
            }
        ],
        "collocations": [
            {"phrase": "take the minutes", "meaning_vi": "ghi chép biên bản cuộc họp", "evidence": "corpus"},
            {"phrase": "approve the minutes", "meaning_vi": "thông qua biên bản cuộc họp", "evidence": "corpus"},
            {"phrase": "distribute the minutes", "meaning_vi": "gửi phát biên bản cuộc họp cho các bên", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "meeting records", "meaning_vi": "hồ sơ ghi chép cuộc họp"},
            {"word": "official proceedings", "meaning_vi": "biên bản nghị sự chính thức"}
        ],
        "examples": [
            {
                "en": "The secretary took the minutes and circulated them to all board members the following morning.",
                "vi": "Thư ký đã ghi biên bản cuộc họp và gửi tới tất cả các thành viên hội đồng quản trị vào sáng hôm sau."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈmɪn/, âm cuối có âm /ts/ cọ xát đầu lưỡi dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "convene",
        "lemma": "convene",
        "pos": ["verb"],
        "ipa": {"us": "/kənˈviːn/", "uk": "/kənˈviːn/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["meetings-office", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "convene-1",
                "meaning_vi": "Triệu tập cuộc họp, tập hợp các thành viên tham dự đại hội",
                "note_vi": "Hành động chính thức phát lệnh mở cuộc họp hội đồng hoặc hội nghị."
            }
        ],
        "confused_words": [
            {
                "word": "convince",
                "ipa": "/kənˈvɪns/",
                "difference_vi": "Convince là thuyết phục ai tin tưởng; convene là triệu tập cuộc họp."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Convene a meeting = triệu tập cuộc họp; convene in the auditorium = tập trung tại khán phòng."
            }
        ],
        "collocations": [
            {"phrase": "convene a meeting", "meaning_vi": "triệu tập cuộc họp chính thức", "evidence": "corpus"},
            {"phrase": "convene a committee", "meaning_vi": "thành lập và triệu tập một ủy ban", "evidence": "corpus"},
            {"phrase": "convene an emergency session", "meaning_vi": "triệu tập một phiên họp khẩn cấp", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "assemble", "meaning_vi": "tập hợp lại"},
            {"word": "summon", "meaning_vi": "triệu tập"},
            {"word": "call", "meaning_vi": "mở lời triệu tập"}
        ],
        "examples": [
            {
                "en": "The chairperson convened an emergency meeting to address the abrupt drop in stock price.",
                "vi": "Chủ tọa đã triệu tập một cuộc họp khẩn cấp để xử lý việc giá cổ phiếu sụt giảm đột ngột."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /viːn/, nguyên âm /iː/ kéo dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "memorandum",
        "lemma": "memorandum",
        "pos": ["noun"],
        "ipa": {"us": "/ˌmeməˈrændəm/", "uk": "/ˌmeməˈrændəm/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["meetings-office", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "memorandum-1",
                "meaning_vi": "Bản ghi nhớ nội bộ công ty (thường viết tắt là memo); văn bản thỏa thuận sơ bộ",
                "note_vi": "Văn bản trao đổi công vụ nội bộ nhằm thông báo chính sách mới hoặc chỉ thị quan trọng."
            }
        ],
        "confused_words": [
            {
                "word": "memorial",
                "ipa": "/məˈmɔːriəl/",
                "difference_vi": "Memorial là đài tưởng niệm; memorandum là bản thông báo ghi nhớ nội bộ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Internal memo = thông báo lưu hành nội bộ; memorandum of understanding (MOU) = biên bản ghi nhớ hợp tác chiến lược giữa hai đơn vị."
            }
        ],
        "collocations": [
            {"phrase": "internal memorandum", "meaning_vi": "bản ghi nhớ lưu hành nội bộ", "evidence": "corpus"},
            {"phrase": "memorandum of understanding", "meaning_vi": "biên bản ghi nhớ hợp tác (MOU)", "evidence": "corpus"},
            {"phrase": "issue a memorandum", "meaning_vi": "ban hành một bản ghi nhớ chỉ thị", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "memo", "meaning_vi": "thông báo vắn tắt nội bộ"},
            {"word": "notice", "meaning_vi": "thông tri"},
            {"word": "circular", "meaning_vi": "công văn gửi thông báo"}
        ],
        "examples": [
            {
                "en": "Management sent an internal memorandum reminding all staff to wear visitor badges at all times.",
                "vi": "Ban quản lý đã gửi một bản ghi nhớ nội bộ nhắc nhở toàn thể nhân viên phải đeo thẻ khách mọi lúc."
            }
        ],
        "pronunciation_tips_vi": "Từ có 4 âm tiết, trọng âm chính rơi vào âm thứ ba /ˈræn/, âm cuối đọc là /dəm/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "clerical",
        "lemma": "clerical",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈklerɪkl/", "uk": "/ˈklerɪkl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["meetings-office", "human-resources"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "clerical-1",
                "meaning_vi": "Thuộc công việc bàn giấy, văn thư hành chính tổng hợp",
                "note_vi": "Bao gồm soạn thảo, lưu trữ hồ sơ, nhập liệu và trực điện thoại văn phòng."
            }
        ],
        "confused_words": [
            {
                "word": "clerk",
                "ipa": "/klɜːrk/",
                "difference_vi": "Clerk là nhân viên văn thư hoặc nhân viên thu ngân; clerical là tính từ thuộc về công việc văn phòng hành chính."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Clerical error = sai sót do sơ suất đánh máy/ghi chép sổ sách; clerical duties = nghiệp vụ hành chính."
            }
        ],
        "collocations": [
            {"phrase": "clerical error", "meaning_vi": "sai sót trong quá trình đánh máy / ghi chép sổ sách", "evidence": "corpus"},
            {"phrase": "clerical duties", "meaning_vi": "các nhiệm vụ hành chính bàn giấy", "evidence": "corpus"},
            {"phrase": "clerical staff", "meaning_vi": "đội ngũ nhân viên văn thư", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "administrative", "meaning_vi": "thuộc về hành chính"},
            {"word": "secretarial", "meaning_vi": "thuộc công việc thư ký"}
        ],
        "examples": [
            {
                "en": "The wrong invoice total was simply due to an unintended clerical error during data entry.",
                "vi": "Tổng số tiền trên hóa đơn bị sai chỉ đơn giản là do lỗi đánh máy vô ý trong quá trình nhập dữ liệu."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈkler/, nguyên âm /e/ mở tự nhiên, âm cuối là /ɪkl/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "stationery",
        "lemma": "stationery",
        "pos": ["noun"],
        "ipa": {"us": "/ˈsteɪʃəneri/", "uk": "/ˈsteɪʃənri/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["meetings-office"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "stationery-1",
                "meaning_vi": "Văn phòng phẩm (giấy in, bút, bìa hồ sơ, kẹp ghim)",
                "note_vi": "Đồ dùng văn phòng cần thiết cho bàn làm việc hàng ngày."
            }
        ],
        "confused_words": [
            {
                "word": "stationary",
                "ipa": "/ˈsteɪʃəneri/",
                "difference_vi": "Đồng âm hoàn toàn nhưng khác chính tả và nghĩa: stationary (có 'a') nghĩa là đứng yên bất động; stationery (có 'e') là đồ dùng văn phòng phẩm."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Office stationery = đồ dùng văn phòng; personalized stationery = giấy viết thư in sẵn tên riêng sang trọng."
            }
        ],
        "collocations": [
            {"phrase": "office stationery", "meaning_vi": "văn phòng phẩm dùng trong văn phòng", "evidence": "corpus"},
            {"phrase": "order stationery", "meaning_vi": "đặt mua văn phòng phẩm", "evidence": "corpus"},
            {"phrase": "stationery cupboard", "meaning_vi": "tủ đựng văn phòng phẩm", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "office supplies", "meaning_vi": "đồ dùng văn phòng"},
            {"word": "paper goods", "meaning_vi": "các sản phẩm giấy in"}
        ],
        "examples": [
            {
                "en": "The administrative assistant is preparing a bulk order for office stationery and printer toner.",
                "vi": "Trợ lý hành chính đang chuẩn bị một đơn đặt hàng lớn văn phòng phẩm và mực máy in."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈsteɪ/, nhị trùng âm /eɪ/ rõ nét, đuôi /neri/ đọc nhanh.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "filing",
        "lemma": "filing",
        "pos": ["noun"],
        "ipa": {"us": "/ˈfaɪlɪŋ/", "uk": "/ˈfaɪlɪŋ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["meetings-office", "describe-picture"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "filing-1",
                "meaning_vi": "Việc sắp xếp hồ sơ lưu trữ; tủ đựng tài liệu ngăn kéo (filing cabinet)",
                "note_vi": "Thường gặp trong Part 2 tả văn phòng: a filing cabinet, filing documents."
            }
        ],
        "confused_words": [
            {
                "word": "filling",
                "ipa": "/ˈfɪlɪŋ/",
                "difference_vi": "Filling là nhân bánh hoặc sự lấp đầy (nguyên âm ngắn /ɪ/); filing là việc cất trữ hồ sơ (nhị trùng âm /aɪ/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Filing cabinet = tủ đựng tài liệu văn phòng; tax filing = việc nộp hồ sơ kê khai thuế."
            }
        ],
        "collocations": [
            {"phrase": "filing cabinet", "meaning_vi": "tủ đựng hồ sơ tài liệu văn phòng", "evidence": "corpus"},
            {"phrase": "filing system", "meaning_vi": "hệ thống phân loại lưu trữ hồ sơ", "evidence": "corpus"},
            {"phrase": "tax filing deadline", "meaning_vi": "hạn chót nộp hồ sơ quyết toán thuế", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "archiving", "meaning_vi": "lưu trữ tài liệu"},
            {"word": "record-keeping", "meaning_vi": "lập và giữ sổ sách lưu trữ"}
        ],
        "examples": [
            {
                "en": "Confidential personnel contracts are locked securely inside the metal filing cabinet.",
                "vi": "Hợp đồng nhân sự mật được cất khóa cẩn thận bên trong tủ hồ sơ bằng kim loại."
            }
        ],
        "pronunciation_tips_vi": "Phát âm nhị trùng âm /ˈfaɪ/ rõ ràng, uốn lưỡi âm /l/ nhẹ trước khi sang /ɪŋ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "lease",
        "lemma": "lease",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/liːs/", "uk": "/liːs/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "lease-1",
                "meaning_vi": "Hợp đồng thuê tài sản dài hạn (nhà đất, thiết bị máy móc); (v) cho thuê hoặc thuê theo hợp đồng",
                "note_vi": "Thường có tính ràng buộc pháp lý chặt chẽ hơn từ rent thông thường."
            }
        ],
        "confused_words": [
            {
                "word": "least",
                "ipa": "/liːst/",
                "difference_vi": "Least là ít nhất (có âm cuối /st/); lease là hợp đồng thuê dài hạn (kết thúc bằng âm /s/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Sign a lease = ký hợp đồng thuê nhà; lease agreement = thỏa thuận hợp đồng cho thuê."
            }
        ],
        "collocations": [
            {"phrase": "sign a lease", "meaning_vi": "ký hợp đồng thuê tài sản", "evidence": "corpus"},
            {"phrase": "lease agreement", "meaning_vi": "văn bản thỏa thuận hợp đồng thuê", "evidence": "corpus"},
            {"phrase": "expire of a lease", "meaning_vi": "hết hạn hợp đồng cho thuê", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "rental agreement", "meaning_vi": "thỏa thuận thuê mướn"},
            {"word": "charter", "meaning_vi": "hợp đồng thuê bao trọn gói"}
        ],
        "examples": [
            {
                "en": "The law firm signed a five-year lease for the entire top floor of the commercial tower.",
                "vi": "Công ty luật đã ký hợp đồng thuê năm năm cho toàn bộ tầng cao nhất của tòa tháp thương mại."
            }
        ],
        "pronunciation_tips_vi": "Nguyên âm /iː/ dài, âm cuối là âm /s/ gió rõ nét, không phát âm thành âm /z/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "tenant",
        "lemma": "tenant",
        "pos": ["noun"],
        "ipa": {"us": "/ˈtenənt/", "uk": "/ˈtenənt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "tenant-1",
                "meaning_vi": "Người thuê nhà, người hoặc công ty thuê mặt bằng kinh doanh",
                "note_vi": "Đối tác ký kết hợp đồng thuê với chủ nhà (landlord)."
            }
        ],
        "confused_words": [
            {
                "word": "landlord",
                "ipa": "/ˈlændlɔːrd/",
                "difference_vi": "Tenant là người đi thuê; landlord là chủ nhà cho thuê."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Prospective tenant = người thuê tiềm năng; commercial tenant = doanh nghiệp thuê mặt bằng."
            }
        ],
        "collocations": [
            {"phrase": "prospective tenant", "meaning_vi": "người thuê nhà tiềm năng", "evidence": "corpus"},
            {"phrase": "commercial tenant", "meaning_vi": "đơn vị thuê mặt bằng thương mại", "evidence": "corpus"},
            {"phrase": "tenant rights", "meaning_vi": "quyền lợi của người đi thuê nhà", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "renter", "meaning_vi": "người thuê nhà"},
            {"word": "occupant", "meaning_vi": "người cư ngụ, sử dụng"}
        ],
        "examples": [
            {
                "en": "All prospective tenants must undergo credit checks before the lease can be finalized.",
                "vi": "Tất cả những người thuê tiềm năng đều phải trải qua kiểm tra tín dụng trước khi hợp đồng thuê có thể được chốt."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈten/, âm thứ hai đọc lướt /ənt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "landlord",
        "lemma": "landlord",
        "pos": ["noun"],
        "ipa": {"us": "/ˈlændlɔːrd/", "uk": "/ˈlændlɔːd/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "landlord-1",
                "meaning_vi": "Chủ nhà, người sở hữu đất đai hoặc bất động sản cho người khác thuê",
                "note_vi": "Người nhận tiền thuê nhà và chịu trách nhiệm bảo trì kết cấu bất động sản."
            }
        ],
        "confused_words": [
            {
                "word": "landlady",
                "ipa": "/ˈlændleɪdi/",
                "difference_vi": "Landlord là chủ nhà nam hoặc nói chung; landlady là nữ chủ nhà cho thuê."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Contact the landlord = liên hệ chủ nhà; landlord's permission = sự cho phép của chủ sở hữu nhà."
            }
        ],
        "collocations": [
            {"phrase": "contact the landlord", "meaning_vi": "liên hệ với chủ nhà", "evidence": "corpus"},
            {"phrase": "landlord and tenant", "meaning_vi": "bên cho thuê và bên thuê", "evidence": "corpus"},
            {"phrase": "landlord's consent", "meaning_vi": "sự ưng thuận của chủ sở hữu nhà", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "property owner", "meaning_vi": "chủ sở hữu bất động sản"},
            {"word": "lessor", "meaning_vi": "bên cho thuê theo hợp đồng"}
        ],
        "examples": [
            {
                "en": "Tenants must obtain written consent from the landlord before making alterations to the apartment.",
                "vi": "Người thuê nhà phải có được sự đồng ý bằng văn bản từ chủ nhà trước khi sửa chữa thay đổi căn hộ."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép gồm 'land' /ˈlænd/ và 'lord' /lɔːrd/, trọng âm rơi vào âm tiết đầu.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "premises",
        "lemma": "premises",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpremɪsɪz/", "uk": "/ˈpremɪsɪz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction", "legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "premises-1",
                "meaning_vi": "Khuôn viên, cơ sở mặt bằng kinh doanh (bao gồm đất đai và toàn bộ tòa nhà)",
                "note_vi": "Luôn có dạng số nhiều -es khi chỉ mặt bằng cơ sở doanh nghiệp."
            }
        ],
        "confused_words": [
            {
                "word": "premise",
                "ipa": "/ˈpremɪs/",
                "difference_vi": "Premise (số ít) là tiền đề logic trong triết học; premises (có -es) là khuôn viên cơ sở nhà xưởng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "On the premises = ngay tại khuôn viên cơ sở; business premises = mặt bằng kinh doanh."
            }
        ],
        "collocations": [
            {"phrase": "on the premises", "meaning_vi": "ngay trong khuôn viên cơ sở", "evidence": "corpus"},
            {"phrase": "business premises", "meaning_vi": "mặt bằng cơ sở kinh doanh", "evidence": "corpus"},
            {"phrase": "vacate the premises", "meaning_vi": "dọn đi, bàn giao lại mặt bằng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "property", "meaning_vi": "khu bất động sản"},
            {"word": "site", "meaning_vi": "địa điểm, cơ sở"},
            {"word": "facility", "meaning_vi": "cơ sở vật chất"}
        ],
        "examples": [
            {
                "en": "Smoking is strictly prohibited anywhere on the hospital premises.",
                "vi": "Hút thuốc bị nghiêm cấm hoàn toàn tại bất kỳ đâu trong khuôn viên bệnh viện."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈprem/, hai âm sau đọc là /ɪsɪz/ có âm xát /s/ và /z/ rõ ràng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "renovate",
        "lemma": "renovate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈrenəveɪt/", "uk": "/ˈrenəveɪt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "renovate-1",
                "meaning_vi": "Cải tạo, nâng cấp, tu bổ lại công trình nhà ở hoặc tòa nhà cũ",
                "note_vi": "Làm mới và sửa sang để phục hồi tình trạng ban đầu hoặc hiện đại hóa cơ sở."
            }
        ],
        "confused_words": [
            {
                "word": "innovate",
                "ipa": "/ˈɪnəveɪt/",
                "difference_vi": "Innovate là đổi mới sáng tạo công nghệ/phương pháp; renovate là cải tạo tu bổ công trình xây dựng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Renovate a building = nâng cấp sửa chữa tòa nhà; completely renovated = được đại tu làm mới hoàn toàn."
            }
        ],
        "collocations": [
            {"phrase": "renovate an old building", "meaning_vi": "cải tạo một tòa nhà cổ", "evidence": "corpus"},
            {"phrase": "completely renovated", "meaning_vi": "được tu bổ nâng cấp toàn diện", "evidence": "corpus"},
            {"phrase": "renovation project", "meaning_vi": "dự án cải tạo sửa chữa", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "refurbish", "meaning_vi": "tân trang lại"},
            {"word": "remodel", "meaning_vi": "sửa đổi cấu trúc không gian"},
            {"word": "upgrade", "meaning_vi": "nâng cấp"}
        ],
        "examples": [
            {
                "en": "The downtown branch will close for two weeks while the lobby is being thoroughly renovated.",
                "vi": "Chi nhánh trung tâm sẽ đóng cửa trong hai tuần trong khi sảnh chờ đang được cải tạo toàn diện."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈren/, âm đuôi là /veɪt/ có âm /t/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "refurbish",
        "lemma": "refurbish",
        "pos": ["verb"],
        "ipa": {"us": "/ˌriːˈfɜːrbɪʃ/", "uk": "/ˌriːˈfɜːbɪʃ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "refurbish-1",
                "meaning_vi": "Tân trang, trang trí lại nội thất hoặc sơn sửa làm mới phòng ốc",
                "note_vi": "Tập trung nhiều vào làm đẹp bề mặt, thay mới đồ đạc và nội thất trang trí."
            }
        ],
        "confused_words": [
            {
                "word": "furnish",
                "ipa": "/ˈfɜːrnɪʃ/",
                "difference_vi": "Furnish là trang bị sắm sửa đồ đạc ban đầu; refurbish là làm mới, tân trang lại đồ đạc nội thất cũ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Newly refurbished = vừa mới được tân trang lại; refurbished electronics = hàng điện tử đã qua kiểm tra thay vỏ làm mới lại."
            }
        ],
        "collocations": [
            {"phrase": "newly refurbished", "meaning_vi": "vừa mới được tân trang sửa sang", "evidence": "corpus"},
            {"phrase": "refurbish the hotel rooms", "meaning_vi": "tân trang lại các phòng khách sạn", "evidence": "corpus"},
            {"phrase": "cost of refurbishing", "meaning_vi": "chi phí tân trang nội thất", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "redecorate", "meaning_vi": "trang hoàng lại"},
            {"word": "spruce up", "meaning_vi": "làm cho khang trang hơn"},
            {"word": "restore", "meaning_vi": "phục hồi lại"}
        ],
        "examples": [
            {
                "en": "The boutique hotel boasts newly refurbished guest suites equipped with state-of-the-art amenities.",
                "vi": "Khách sạn phong cách này tự hào có các dãy phòng nghỉ vừa được tân trang hoàn toàn với tiện nghi tối tân."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /fɜːrb/, âm cuối kết thúc bằng /ɪʃ/ cong môi nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "demolish",
        "lemma": "demolish",
        "pos": ["verb"],
        "ipa": {"us": "/dɪˈmɑːlɪʃ/", "uk": "/dɪˈmɒlɪʃ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "demolish-1",
                "meaning_vi": "Phá dỡ, đánh sập công trình xây dựng cũ để giải phóng mặt bằng",
                "note_vi": "Hành động san phẳng tòa nhà hư hại để xây dựng công trình mới."
            }
        ],
        "confused_words": [
            {
                "word": "abolish",
                "ipa": "/əˈbɑːlɪʃ/",
                "difference_vi": "Abolish là bãi bỏ luật lệ, phong tục; demolish là phá hủy, đập bỏ công trình vật chất."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Demolish a building = đập bỏ tòa nhà; demolish an argument = đập tan luận điểm phản biện hoàn toàn."
            }
        ],
        "collocations": [
            {"phrase": "demolish a building", "meaning_vi": "phá dỡ một tòa nhà", "evidence": "corpus"},
            {"phrase": "scheduled for demolition", "meaning_vi": "đã lên lịch để phá dỡ", "evidence": "corpus"},
            {"phrase": "demolish to make way for", "meaning_vi": "phá dỡ để nhường chỗ xây dựng công trình mới", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "tear down", "meaning_vi": "kéo đổ, dỡ bỏ"},
            {"word": "knock down", "meaning_vi": "san bằng"},
            {"word": "destroy", "meaning_vi": "phá hủy"}
        ],
        "examples": [
            {
                "en": "The abandoned factory will be demolished next week to make way for a modern community park.",
                "vi": "Nhà máy bỏ hoang sẽ bị phá dỡ vào tuần tới để nhường chỗ cho một công viên cộng đồng hiện đại."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈmɑːl/, âm đuôi /ɪʃ/ cong môi bật hơi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "spacious",
        "lemma": "spacious",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈspeɪʃəs/", "uk": "/ˈspeɪʃəs/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction", "hospitality-travel"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "spacious-1",
                "meaning_vi": "Rộng rãi, thoáng đãng, có nhiều diện tích không gian",
                "note_vi": "Từ ngữ yêu thích để miêu tả văn phòng làm việc, căn hộ hoặc phòng họp lớn."
            }
        ],
        "confused_words": [
            {
                "word": "special",
                "ipa": "/ˈspeʃl/",
                "difference_vi": "Special là đặc biệt; spacious là rộng rãi thoáng đãng."
            },
            {
                "word": "specious",
                "ipa": "/ˈspiːʃəs/",
                "difference_vi": "Specious là giả tạo, chỉ có vẻ ngoài đúng đắn (/iː/); spacious là rộng rãi diện tích (/eɪ/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Spacious living room = phòng khách rộng thênh thang; spacious layout = bố cục mặt sàn thoáng đãng."
            }
        ],
        "collocations": [
            {"phrase": "spacious office", "meaning_vi": "văn phòng làm việc rộng rãi", "evidence": "corpus"},
            {"phrase": "spacious living room", "meaning_vi": "phòng sinh hoạt rộng rãi", "evidence": "corpus"},
            {"phrase": "bright and spacious", "meaning_vi": "ngập tràn ánh sáng và thoáng mát", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "roomy", "meaning_vi": "nhiều chỗ, rộng rãi"},
            {"word": "commodious", "meaning_vi": "thênh thang tiện nghi"},
            {"word": "airy", "meaning_vi": "thoáng khí"}
        ],
        "examples": [
            {
                "en": "The newly leased headquarters offers spacious conference facilities and an open floor plan.",
                "vi": "Trụ sở mới thuê cung cấp các phòng hội nghị rộng rãi và sơ đồ mặt sàn mở."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈspeɪ/, âm thứ hai đọc là /ʃəs/ tròn môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "estate",
        "lemma": "estate",
        "pos": ["noun"],
        "ipa": {"us": "/ɪˈsteɪt/", "uk": "/ɪˈsteɪt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "estate-1",
                "meaning_vi": "Bất động sản, khu đất xây dựng; toàn bộ tài sản thừa kế của một người",
                "note_vi": "Collocation cực kỳ quan trọng: real estate (ngành bất động sản), real estate agent (nhà môi giới nhà đất)."
            }
        ],
        "confused_words": [
            {
                "word": "state",
                "ipa": "/steɪt/",
                "difference_vi": "State là bang hoặc trạng thái; estate là điền trang hoặc bất động sản nhà đất."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Real estate = thị trường bất động sản; industrial estate = khu công nghiệp tập trung."
            }
        ],
        "collocations": [
            {"phrase": "real estate agent", "meaning_vi": "môi giới viên bất động sản", "evidence": "corpus"},
            {"phrase": "real estate market", "meaning_vi": "thị trường bất động sản", "evidence": "corpus"},
            {"phrase": "industrial estate", "meaning_vi": "khu đất công nghiệp", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "property", "meaning_vi": "tài sản bất động sản"},
            {"word": "landholding", "meaning_vi": "khu đất sở hữu"}
        ],
        "examples": [
            {
                "en": "Commercial real estate prices in the financial district have reached an all-time high.",
                "vi": "Giá bất động sản thương mại tại khu tài chính đã chạm mức cao nhất mọi thời đại."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /steɪt/ với nhị trùng âm /eɪ/ rõ nét, âm đầu /ɪ/ lướt nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "deposit",
        "lemma": "deposit",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/dɪˈpɑːzɪt/", "uk": "/dɪˈpɒzɪt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["real-estate-construction", "finance-accounting"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "deposit-1",
                "meaning_vi": "Tiền đặt cọc giữ chỗ hoặc tiền bảo đảm thuê nhà; tiền gửi tiết kiệm ngân hàng",
                "note_vi": "Khoản tiền trả trước để đảm bảo hợp đồng hoặc giữ tài sản an toàn."
            }
        ],
        "confused_words": [
            {
                "word": "withdraw",
                "ipa": "/wɪðˈdrɔː/",
                "difference_vi": "Deposit tiền là gửi tiền vào tài khoản; withdraw là rút tiền ra."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Security deposit = tiền đặt cọc bảo đảm tài sản thuê; bank deposit = tiền gửi vào ngân hàng."
            }
        ],
        "collocations": [
            {"phrase": "security deposit", "meaning_vi": "tiền đặt cọc bảo đảm tài sản thuê", "evidence": "corpus"},
            {"phrase": "refundable deposit", "meaning_vi": "khoản tiền đặt cọc có thể hoàn trả lại", "evidence": "corpus"},
            {"phrase": "deposit money into an account", "meaning_vi": "nộp tiền vào tài khoản ngân hàng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "down payment", "meaning_vi": "khoản tiền trả trước"},
            {"word": "advance payment", "meaning_vi": "tiền tạm ứng"}
        ],
        "examples": [
            {
                "en": "The tenant paid two months' rent as a refundable security deposit prior to moving in.",
                "vi": "Người thuê đã trả hai tháng tiền nhà làm khoản đặt cọc bảo đảm có hoàn lại trước khi chuyển vào ở."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈpɑːz/, chữ 's' phát âm thành âm /z/ rung.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "utility",
        "lemma": "utility",
        "pos": ["noun"],
        "ipa": {"us": "/juːˈtɪləti/", "uk": "/juːˈtɪləti/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "utility-1",
                "meaning_vi": "Dịch vụ tiện ích thiết yếu (điện, nước, khí đốt, internet sinh hoạt); (n) tính hữu dụng",
                "note_vi": "Thường ở dạng số nhiều (utilities) khi nhắc tới các hóa đơn sinh hoạt hàng tháng."
            }
        ],
        "confused_words": [
            {
                "word": "utilize",
                "ipa": "/ˈjuːtəlaɪz/",
                "difference_vi": "Utilize là động từ tận dụng; utility là danh từ dịch vụ tiện ích điện nước hoặc độ hữu dụng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Utility bills = hóa đơn tiền điện nước; public utility = doanh nghiệp tiện ích công cộng (nhà máy nước/điện lực)."
            }
        ],
        "collocations": [
            {"phrase": "utility bills", "meaning_vi": "hóa đơn tiền điện, nước sinh hoạt", "evidence": "corpus"},
            {"phrase": "public utility", "meaning_vi": "dịch vụ tiện ích công ích công cộng", "evidence": "corpus"},
            {"phrase": "utilities included", "meaning_vi": "đã bao gồm các chi phí điện nước trong giá thuê", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "public services", "meaning_vi": "dịch vụ công ích"},
            {"word": "amenities", "meaning_vi": "tiện ích sinh hoạt"}
        ],
        "examples": [
            {
                "en": "The monthly rental fee is $1,200, with water and high-speed internet utilities included.",
                "vi": "Mức giá thuê hàng tháng là 1.200 đô la, đã bao gồm các tiện ích nước sinh hoạt và internet tốc độ cao."
            }
        ],
        "pronunciation_tips_vi": "Từ có 4 âm tiết, trọng âm chính rơi vào âm thứ hai /ˈtɪl/, âm đầu là /juː/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "vacate",
        "lemma": "vacate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈveɪkeɪt/", "uk": "/vəˈkeɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction", "hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "vacate-1",
                "meaning_vi": "Bàn giao lại mặt bằng, dọn sạch đồ đạc rời đi khỏi phòng hoặc chức vụ",
                "note_vi": "Thường dùng khi hết hạn thuê nhà hoặc thời hạn trả phòng khách sạn (check-out)."
            }
        ],
        "confused_words": [
            {
                "word": "vacation",
                "ipa": "/veɪˈkeɪʃn/",
                "difference_vi": "Vacation là kỳ nghỉ phép dưỡng sức; vacate là hành động dọn đồ rời khỏi phòng hoặc văn phòng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Vacate the premises = dọn khỏi khu nhà mặt bằng; vacate an office = rời khỏi phòng làm việc/từ bỏ vị trí chức danh."
            }
        ],
        "collocations": [
            {"phrase": "vacate the premises", "meaning_vi": "dọn sạch đồ rời khỏi mặt bằng", "evidence": "corpus"},
            {"phrase": "vacate a hotel room", "meaning_vi": "trả phòng khách sạn đúng giờ", "evidence": "corpus"},
            {"phrase": "notice to vacate", "meaning_vi": "thông báo yêu cầu chuyển đi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "leave", "meaning_vi": "rời đi"},
            {"word": "evacuate", "meaning_vi": "sơ tán, di tản khỏi"},
            {"word": "clear out", "meaning_vi": "dọn sạch sẽ ra ngoài"}
        ],
        "examples": [
            {
                "en": "Guests are kindly requested to vacate their rooms by 11:00 AM on the day of departure.",
                "vi": "Kính đề nghị quý khách dọn đồ trả phòng trước 11:00 trưa vào ngày khởi hành."
            }
        ],
        "pronunciation_tips_vi": "Trong tiếng Mỹ nhấn âm 1 /ˈveɪkeɪt/, nhị trùng âm /eɪ/ lặp lại ở cả hai âm tiết.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "occupancy",
        "lemma": "occupancy",
        "pos": ["noun"],
        "ipa": {"us": "/ˈɑːkjəpənsi/", "uk": "/ˈɒkjəpənsi/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["real-estate-construction", "hospitality-travel"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "occupancy-1",
                "meaning_vi": "Tỷ lệ lấp đầy phòng khách sạn hoặc mặt bằng tòa nhà; tình trạng sử dụng mặt bằng",
                "note_vi": "Chỉ số kinh doanh cốt lõi của ngành khách sạn và bất động sản (occupancy rate)."
            }
        ],
        "confused_words": [
            {
                "word": "occupation",
                "ipa": "/ˌɑːkjuˈpeɪʃn/",
                "difference_vi": "Occupation là nghề nghiệp chuyên môn hoặc sự chiếm đóng; occupancy là tỷ lệ sử dụng lấp đầy phòng ốc."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Occupancy rate = tỷ lệ lấp đầy phòng; maximum occupancy = số lượng người tối đa được phép cư trú trong phòng."
            }
        ],
        "collocations": [
            {"phrase": "occupancy rate", "meaning_vi": "tỷ lệ lấp đầy buồng phòng", "evidence": "corpus"},
            {"phrase": "maximum occupancy", "meaning_vi": "sức chứa tối đa người cho phép", "evidence": "corpus"},
            {"phrase": "single occupancy", "meaning_vi": "ở một người một phòng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "tenancy", "meaning_vi": "thời gian thuê mướn"},
            {"word": "utilization rate", "meaning_vi": "tỷ lệ tận dụng công suất"}
        ],
        "examples": [
            {
                "en": "During the peak summer festival, coastal resorts recorded an average occupancy rate of ninety-five percent.",
                "vi": "Trong dịp lễ hội mùa hè cao điểm, các khu nghỉ dưỡng ven biển đã ghi nhận tỷ lệ lấp đầy phòng trung bình đạt 95%."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈɑːk/, âm tiết thứ hai đọc là /jə/ nhẹ, kết thúc bằng /si/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "accommodation",
        "lemma": "accommodation",
        "pos": ["noun"],
        "ipa": {"us": "/əˌkɑːməˈdeɪʃn/", "uk": "/əˌkɒməˈdeɪʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "accommodation-1",
                "meaning_vi": "Chỗ ở, phòng nghỉ lưu trú (khách sạn, nhà nghỉ, căn hộ du lịch)",
                "note_vi": "Trong tiếng Anh-Anh thường dùng không đếm được (accommodation), tiếng Anh-Mỹ có thể dùng số nhiều (accommodations)."
            }
        ],
        "confused_words": [
            {
                "word": "accommodate",
                "ipa": "/əˈkɑːmədeɪt/",
                "difference_vi": "Accommodate là động từ chứa được, đáp ứng; accommodation là danh từ chỗ ở lưu trú."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Hotel accommodation = chỗ nghỉ khách sạn; reasonable accommodation trong luật lao động = việc điều chỉnh điều kiện làm việc hợp lý cho người khuyết tật."
            }
        ],
        "collocations": [
            {"phrase": "hotel accommodation", "meaning_vi": "chỗ nghỉ ngơi tại khách sạn", "evidence": "corpus"},
            {"phrase": "book accommodation", "meaning_vi": "đặt chỗ ở lưu trú trước", "evidence": "corpus"},
            {"phrase": "temporary accommodation", "meaning_vi": "chỗ ở tạm thời", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "lodging", "meaning_vi": "nơi ăn chốn ở"},
            {"word": "housing", "meaning_vi": "nhà ở"},
            {"word": "living quarters", "meaning_vi": "khu cư xá"}
        ],
        "examples": [
            {
                "en": "The conference package includes luxury hotel accommodation and daily breakfast buffet.",
                "vi": "Gói hội nghị bao gồm chỗ ở khách sạn sang trọng và tiệc buffet bữa sáng hàng ngày."
            }
        ],
        "pronunciation_tips_vi": "Từ có 5 âm tiết, trọng âm chính rơi vào âm thứ tư /ˈdeɪ/, âm /ɑː/ dài ở âm tiết thứ hai.",
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
    for w in words_group4a:
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
    print(f"\n[OK] Group 4A created {count} words successfully.")

if __name__ == "__main__":
    main()
