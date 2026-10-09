# -*- coding: utf-8 -*-
"""
Batch generator for Lexicon Group 4B:
Du lịch, Khách sạn, Pháp lý & Quy chế tuân thủ (26 words)
"""
import os
import yaml

words_group4b = [
    {
        "id": "reservation",
        "lemma": "reservation",
        "pos": ["noun"],
        "ipa": {"us": "/ˌrezərˈveɪʃn/", "uk": "/ˌrezəˈveɪʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "reservation-1",
                "meaning_vi": "Sự đặt trước chỗ ngồi, phòng khách sạn hoặc vé máy bay",
                "note_vi": "Collocation cốt lõi trong TOEIC: make a reservation, confirm a reservation."
            },
            {
                "id": "reservation-2",
                "meaning_vi": "Sự hoài nghi, dè dặt, do dự trước một quyết định",
                "note_vi": "Thường dùng: have reservations about sth."
            }
        ],
        "confused_words": [
            {
                "word": "preserve",
                "ipa": "/prɪˈzɜːrv/",
                "difference_vi": "Preserve là bảo tồn; reserve là giữ chỗ trước; reservation là việc đặt chỗ trước."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Hotel reservation = đặt phòng khách sạn; have reservations = có nỗi băn khoăn hoài nghi."
            }
        ],
        "collocations": [
            {"phrase": "make a reservation", "meaning_vi": "đặt chỗ trước", "evidence": "corpus"},
            {"phrase": "confirm a hotel reservation", "meaning_vi": "xác nhận việc đặt phòng khách sạn", "evidence": "corpus"},
            {"phrase": "cancel a reservation without penalty", "meaning_vi": "hủy đặt chỗ mà không bị phạt tiền", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "booking", "meaning_vi": "việc đặt chỗ"},
            {"word": "pre-arrangement", "meaning_vi": "sự sắp xếp trước"}
        ],
        "examples": [
            {
                "en": "We strongly recommend making a dinner reservation at least two days in advance for weekend dining.",
                "vi": "Chúng tôi thực sự khuyên bạn nên đặt bàn ăn tối trước ít nhất hai ngày cho các bữa ăn cuối tuần."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm chính rơi vào âm thứ ba /ˈveɪ/, đuôi kết thúc là /ʃn/ cong môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "banquet",
        "lemma": "banquet",
        "pos": ["noun"],
        "ipa": {"us": "/ˈbæŋkwɪt/", "uk": "/ˈbæŋkwɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["hospitality-travel", "meetings-office"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "banquet-1",
                "meaning_vi": "Bữa tiệc lớn, yến tiệc chiêu đãi trang trọng (tiệc tất niên, trao giải, mừng công)",
                "note_vi": "Thường tổ chức tại sảnh khách sạn lớn với nhiều quan khách và bài phát biểu."
            }
        ],
        "confused_words": [
            {
                "word": "bank",
                "ipa": "/bæŋk/",
                "difference_vi": "Bank là ngân hàng; banquet là bữa yến tiệc trang trọng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Banquet hall = phòng đại tiệc; awards banquet = tiệc trao giải tôn vinh."
            }
        ],
        "collocations": [
            {"phrase": "annual awards banquet", "meaning_vi": "tiệc trao giải thưởng thường niên", "evidence": "corpus"},
            {"phrase": "banquet hall", "meaning_vi": "phòng khánh tiết / sảnh tiệc", "evidence": "corpus"},
            {"phrase": "attend a formal banquet", "meaning_vi": "tham dự buổi tiệc chiêu đãi trang trọng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "feast", "meaning_vi": "yến tiệc thịnh soạn"},
            {"word": "formal dinner", "meaning_vi": "bữa tiệc tối trang trọng"},
            {"word": "reception", "meaning_vi": "buổi tiệc đón tiếp"}
        ],
        "examples": [
            {
                "en": "The annual corporate banquet will be held in the grand ballroom on the third floor.",
                "vi": "Tiệc thường niên của tập đoàn sẽ được tổ chức tại khán phòng đại tiệc ở tầng ba."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈbæŋk/, âm thứ hai đọc là /wɪt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "venue",
        "lemma": "venue",
        "pos": ["noun"],
        "ipa": {"us": "/ˈvenjuː/", "uk": "/ˈvenjuː/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["hospitality-travel", "meetings-office"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "venue-1",
                "meaning_vi": "Địa điểm tổ chức sự kiện (hội nghị, triển lãm, hòa nhạc, tiệc cưới)",
                "note_vi": "Nơi được chọn để diễn ra một hoạt động đông người có quy mô."
            }
        ],
        "confused_words": [
            {
                "word": "avenue",
                "ipa": "/ˈævənuː/",
                "difference_vi": "Avenue là đại lộ; venue là địa điểm tổ chức sự kiện."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Conference venue = địa điểm hội thảo; wedding venue = sảnh tiệc cưới."
            }
        ],
        "collocations": [
            {"phrase": "ideal venue for events", "meaning_vi": "địa điểm lý tưởng cho các sự kiện", "evidence": "corpus"},
            {"phrase": "select a conference venue", "meaning_vi": "chọn địa điểm tổ chức hội nghị", "evidence": "corpus"},
            {"phrase": "outdoor venue", "meaning_vi": "địa điểm tổ chức ngoài trời", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "location", "meaning_vi": "vị trí, địa điểm"},
            {"word": "site", "meaning_vi": "khu vực tổ chức"},
            {"word": "setting", "meaning_vi": "khung cảnh địa điểm"}
        ],
        "examples": [
            {
                "en": "The convention center serves as an ideal venue for hosting international trade expos.",
                "vi": "Trung tâm hội nghị đóng vai trò là một địa điểm lý tưởng để tổ chức các triển lãm thương mại quốc tế."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈven/, âm thứ hai là /juː/ có âm bán nguyên âm /j/ lướt nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "cater",
        "lemma": "cater",
        "pos": ["verb"],
        "ipa": {"us": "/ˈkeɪtər/", "uk": "/ˈkeɪtə/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "cater-1",
                "meaning_vi": "Cung cấp dịch vụ nấu cỗ và đồ ăn thức uống cho các sự kiện",
                "note_vi": "Thường đi kèm với catering service (dịch vụ nấu tiệc lưu động)."
            },
            {
                "id": "cater-2",
                "meaning_vi": "Đáp ứng, phục vụ theo nhu cầu hoặc thị hiếu riêng biệt (cater to)",
                "note_vi": "Cấu trúc: cater to the needs of..."
            }
        ],
        "confused_words": [
            {
                "word": "caterpillar",
                "ipa": "/ˈkætərpɪlər/",
                "difference_vi": "Caterpillar là con sâu bướm; cater là cung cấp dịch vụ ẩm thực hoặc phục vụ thị hiếu."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Cater a party = nấu tiệc cho bữa tiệc; cater to tourists = chuyên phục vụ đối tượng du khách."
            }
        ],
        "collocations": [
            {"phrase": "cater a wedding reception", "meaning_vi": "phục vụ tiệc cưới", "evidence": "corpus"},
            {"phrase": "cater to customer needs", "meaning_vi": "đáp ứng các nhu cầu của khách hàng", "evidence": "corpus"},
            {"phrase": "outside catering service", "meaning_vi": "dịch vụ đặt tiệc nấu từ bên ngoài", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "provide food", "meaning_vi": "cung cấp đồ ăn"},
            {"word": "serve", "meaning_vi": "phục vụ"},
            {"word": "accommodate", "meaning_vi": "đáp ứng thị hiếu"}
        ],
        "examples": [
            {
                "en": "A prestigious local restaurant was hired to cater the corporate anniversary dinner.",
                "vi": "Một nhà hàng địa phương danh tiếng đã được thuê để phục vụ tiệc tối kỷ niệm thành lập công ty."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈkeɪ/, nhị trùng âm /eɪ/ rõ nét, âm cuối lướt /tər/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "baggage",
        "lemma": "baggage",
        "pos": ["noun"],
        "ipa": {"us": "/ˈbæɡɪdʒ/", "uk": "/ˈbæɡɪdʒ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "baggage-1",
                "meaning_vi": "Hành lý, va li túi xách mang theo của hành khách",
                "note_vi": "Danh từ không đếm được (uncountable noun), dùng baggage claim (khu lấy hành lý sân bay)."
            }
        ],
        "confused_words": [
            {
                "word": "luggage",
                "ipa": "/ˈlʌɡɪdʒ/",
                "difference_vi": "Baggage và luggage đồng nghĩa hoàn toàn; luggage phổ biến hơn trong tiếng Anh-Anh, baggage phổ biến trong tiếng Anh-Mỹ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Carry-on baggage = hành lý xách tay lên máy bay; checked baggage = hành lý ký gửi dưới khoang hàng."
            }
        ],
        "collocations": [
            {"phrase": "excess baggage fee", "meaning_vi": "phí hành lý quá cước", "evidence": "corpus"},
            {"phrase": "baggage claim area", "meaning_vi": "khu vực trả lại hành lý tại sân bay", "evidence": "corpus"},
            {"phrase": "carry-on baggage", "meaning_vi": "hành lý xách tay", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "luggage", "meaning_vi": "hành lý"},
            {"word": "suitcases", "meaning_vi": "va li đồ đạc"}
        ],
        "examples": [
            {
                "en": "Passengers can proceed to Carousel 4 in the baggage claim area to collect their luggage.",
                "vi": "Hành khách có thể di chuyển đến băng chuyền số 4 tại khu vực nhận hành lý để lấy đồ đạc của mình."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈbæɡ/, âm đuôi là /ɪdʒ/ rung cổ họng rõ ràng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "shuttle",
        "lemma": "shuttle",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈʃʌtl/", "uk": "/ˈʃʌtl/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "shuttle-1",
                "meaning_vi": "Tuyến xe buýt / tàu đưa đón cự ly ngắn chạy định kỳ giữa hai điểm; (v) đưa đón qua lại",
                "note_vi": "Phổ biến nhất là shuttle bus giữa sân bay và khách sạn."
            }
        ],
        "confused_words": [
            {
                "word": "subtle",
                "ipa": "/ˈsʌtl/",
                "difference_vi": "Subtle là tinh tế, khéo léo (bắt đầu bằng âm /s/); shuttle là xe buýt trung chuyển (bắt đầu bằng /ʃ/ chu môi)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Airport shuttle = xe đưa đón sân bay; space shuttle = tàu con thoi vũ trụ."
            }
        ],
        "collocations": [
            {"phrase": "airport shuttle bus", "meaning_vi": "xe buýt đưa đón sân bay", "evidence": "corpus"},
            {"phrase": "shuttle service operates", "meaning_vi": "dịch vụ xe đưa đón vận hành", "evidence": "corpus"},
            {"phrase": "free shuttle", "meaning_vi": "xe trung chuyển đưa đón miễn phí", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "transit bus", "meaning_vi": "xe buýt chuyển tiếp"},
            {"word": "transfer", "meaning_vi": "chuyến xe đưa đón"}
        ],
        "examples": [
            {
                "en": "A complimentary hotel shuttle runs every twenty minutes between Terminal 2 and the resort.",
                "vi": "Xe đưa đón miễn phí của khách sạn chạy 20 phút một chuyến giữa Nhà ga số 2 và khu nghỉ dưỡng."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu /ʃ/ chu môi dày, nguyên âm /ʌ/ mở tự nhiên, kết thúc bằng /tl/ nhanh.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "concierge",
        "lemma": "concierge",
        "pos": ["noun"],
        "ipa": {"us": "/koʊnˈsjerʒ/", "uk": "/kɒnˈsieəʒ/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "concierge-1",
                "meaning_vi": "Nhân viên hỗ trợ thông tin đặc biệt tại khách sạn cao cấp (hỗ trợ đặt vé, gợi ý tour)",
                "note_vi": "Bộ phận chăm sóc cá nhân hóa giúp khách lưu trú đặt bàn ăn ngon, mua vé xem kịch hoặc gọi xe."
            }
        ],
        "confused_words": [
            {
                "word": "receptionist",
                "ipa": "/rɪˈsepʃənɪst/",
                "difference_vi": "Receptionist là lễ tân làm thủ tục nhận/trả phòng; concierge là người chuyên hỗ trợ trải nghiệm dịch vụ du lịch bên ngoài."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Concierge desk = quầy dịch vụ chăm sóc khách đặc biệt; concierge service = dịch vụ hỗ trợ cao cấp."
            }
        ],
        "collocations": [
            {"phrase": "concierge desk", "meaning_vi": "quầy hỗ trợ thông tin đặc biệt của khách sạn", "evidence": "corpus"},
            {"phrase": "ask the concierge", "meaning_vi": "hỏi nhân viên hỗ trợ du lịch", "evidence": "corpus"},
            {"phrase": "concierge services", "meaning_vi": "dịch vụ hỗ trợ chăm sóc khách lưu trú", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "guest services assistant", "meaning_vi": "nhân viên dịch vụ khách hàng"},
            {"word": "doorkeeper", "meaning_vi": "người gác cổng hỗ trợ"}
        ],
        "examples": [
            {
                "en": "The hotel concierge helped us secure last-minute tickets to the sold-out opera performance.",
                "vi": "Nhân viên hỗ trợ khách sạn đã giúp chúng tôi mua được vé giờ chót cho buổi biểu diễn nhạc kịch đã cháy vé."
            }
        ],
        "pronunciation_tips_vi": "Từ gốc Pháp, âm đuôi phát âm là /ʒ/ rung nhẹ đầu lưỡi, không đọc thành âm 'd' hay 'ch'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "hospitality",
        "lemma": "hospitality",
        "pos": ["noun"],
        "ipa": {"us": "/ˌhɑːspɪˈtæləti/", "uk": "/ˌhɒspɪˈtæləti/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["hospitality-travel"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "hospitality-1",
                "meaning_vi": "Lòng hiếu khách, sự đón tiếp niềm nở; ngành dịch vụ nhà hàng - khách sạn - du lịch",
                "note_vi": "Khái niệm chỉ toàn bộ khối ngành dịch vụ khách sạn ẩm thực (hospitality industry)."
            }
        ],
        "confused_words": [
            {
                "word": "hospital",
                "ipa": "/ˈhɑːspɪtl/",
                "difference_vi": "Hospital là bệnh viện y tế; hospitality là sự hiếu khách hoặc ngành kinh doanh khách sạn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Warm hospitality = sự đón tiếp nồng hậu; hospitality sector = khối ngành dịch vụ du lịch khách sạn."
            }
        ],
        "collocations": [
            {"phrase": "hospitality industry", "meaning_vi": "ngành công nghiệp dịch vụ khách sạn - nhà hàng", "evidence": "corpus"},
            {"phrase": "warm hospitality", "meaning_vi": "sự hiếu khách nồng ấm", "evidence": "corpus"},
            {"phrase": "hospitality suite", "meaning_vi": "phòng tiếp tân chiêu đãi khách quý", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "welcoming service", "meaning_vi": "dịch vụ đón tiếp chu đáo"},
            {"word": "cordiality", "meaning_vi": "sự thân tình nồng hậu"}
        ],
        "examples": [
            {
                "en": "The resort is renowned for its warm hospitality and world-class customer care.",
                "vi": "Khu nghỉ dưỡng nổi tiếng với lòng hiếu khách nồng hậu và dịch vụ chăm sóc khách hàng đẳng cấp thế giới."
            }
        ],
        "pronunciation_tips_vi": "Từ có 5 âm tiết, trọng âm chính rơi vào âm thứ ba /ˈtæl/, đừng nhầm sang từ 'hospital'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "patron",
        "lemma": "patron",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpeɪtrən/", "uk": "/ˈpeɪtrən/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["hospitality-travel", "sales-customer-service"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "patron-1",
                "meaning_vi": "Khách quen, người thường xuyên ghé thăm bảo tàng, nhà hàng, thư viện hoặc nhà hát",
                "note_vi": "Từ trang trọng chỉ khách hàng của các cơ sở văn hóa ẩm thực nghệ thuật."
            },
            {
                "id": "patron-2",
                "meaning_vi": "Nhà bảo trợ, người bảo trợ tài chính cho các hoạt động nghệ thuật",
                "note_vi": "Như trong 'patron of the arts' (nhà bảo trợ nghệ thuật)."
            }
        ],
        "confused_words": [
            {
                "word": "pattern",
                "ipa": "/ˈpætərn/",
                "difference_vi": "Pattern là hoa văn họa tiết hoặc khuôn mẫu; patron là khách quen hoặc người bảo trợ nghệ thuật."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Library patrons = độc giả thư viện; patron of the arts = nhà tài trợ cho giới nghệ sĩ."
            }
        ],
        "collocations": [
            {"phrase": "regular patrons", "meaning_vi": "những vị khách quen thuộc", "evidence": "corpus"},
            {"phrase": "patrons of the arts", "meaning_vi": "những nhà bảo trợ nghệ thuật", "evidence": "corpus"},
            {"phrase": "reserved for patrons", "meaning_vi": "dành riêng cho khách quen / khách dùng dịch vụ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "customer", "meaning_vi": "khách hàng"},
            {"word": "client", "meaning_vi": "thân chủ"},
            {"word": "supporter", "meaning_vi": "người ủng hộ"}
        ],
        "examples": [
            {
                "en": "The museum offers exclusive preview nights for annual members and museum patrons.",
                "vi": "Bảo tàng tổ chức các đêm xem trước đặc quyền dành cho hội viên thường niên và khách bảo trợ bảo tàng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈpeɪ/, nhị trùng âm /eɪ/ rõ nét, không đọc là 'pa-tron'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "comply",
        "lemma": "comply",
        "pos": ["verb"],
        "ipa": {"us": "/kəmˈplaɪ/", "uk": "/kəmˈplaɪ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "comply-1",
                "meaning_vi": "Tuân thủ, chấp hành đúng các quy định, điều lệ hoặc luật an toàn lao động",
                "note_vi": "Đi kèm giới từ with: comply with regulations / standards."
            }
        ],
        "confused_words": [
            {
                "word": "apply",
                "ipa": "/əˈplaɪ/",
                "difference_vi": "Apply là nộp đơn ứng tuyển hoặc áp dụng; comply là tuân thủ quy chuẩn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Comply with safety codes = tuân thủ các quy tắc an toàn; failure to comply = sự không tuân thủ."
            }
        ],
        "collocations": [
            {"phrase": "comply with regulations", "meaning_vi": "tuân thủ các quy định hiện hành", "evidence": "corpus"},
            {"phrase": "comply with safety standards", "meaning_vi": "tuân thủ các tiêu chuẩn an toàn", "evidence": "corpus"},
            {"phrase": "failure to comply", "meaning_vi": "sự không chấp hành quy định", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "obey", "meaning_vi": "vâng lời, tuân lệnh"},
            {"word": "conform", "meaning_vi": "phù hợp quy chuẩn"},
            {"word": "abide by", "meaning_vi": "tuân theo cam kết"}
        ],
        "examples": [
            {
                "en": "All building plans must strictly comply with national environmental protection standards.",
                "vi": "Tất cả các bản thiết kế xây dựng phải tuân thủ nghiêm ngặt các tiêu chuẩn bảo vệ môi trường quốc gia."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /plaɪ/, nhị trùng âm /aɪ/ ngân dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "adhere",
        "lemma": "adhere",
        "pos": ["verb"],
        "ipa": {"us": "/ədˈhɪr/", "uk": "/ədˈhɪə/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "adhere-1",
                "meaning_vi": "Bám sát, tuân thủ nghiêm ngặt nguyên tắc, lịch trình hoặc chính sách đề ra",
                "note_vi": "Đi kèm giới từ to: adhere to guidelines / policies / schedule."
            },
            {
                "id": "adhere-2",
                "meaning_vi": "Dính chặt vào bề mặt (vật lý)",
                "note_vi": "Như chất keo dán (adhesive)."
            }
        ],
        "confused_words": [
            {
                "word": "adhesion",
                "ipa": "/ədˈhiːʒn/",
                "difference_vi": "Adhesion là độ bám dính vật lý; adhere là động từ tuân thủ bám sát."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Adhere to the policy = tuân thủ chính sách; adhere to the surface = dính chặt vào bề mặt."
            }
        ],
        "collocations": [
            {"phrase": "adhere to guidelines", "meaning_vi": "bám sát các chỉ dẫn quy chế", "evidence": "corpus"},
            {"phrase": "adhere to the schedule", "meaning_vi": "tuân thủ đúng lịch trình đã định", "evidence": "corpus"},
            {"phrase": "strictly adhere", "meaning_vi": "tuân thủ một cách nghiêm ngặt", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "stick to", "meaning_vi": "bám lấy, không rời"},
            {"word": "follow", "meaning_vi": "làm theo"},
            {"word": "observe", "meaning_vi": "tuân thủ chấp hành"}
        ],
        "examples": [
            {
                "en": "Staff members are required to strictly adhere to the company dress code policy.",
                "vi": "Nhân viên bắt buộc phải tuân thủ nghiêm ngặt chính sách về trang phục của công ty."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /hɪr/, âm /h/ thở rõ ràng trước nguyên âm đôi /ɪr/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "conform",
        "lemma": "conform",
        "pos": ["verb"],
        "ipa": {"us": "/kənˈfɔːrm/", "uk": "/kənˈfɔːm/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "production-quality-control"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "conform-1",
                "meaning_vi": "Phù hợp với, ăn khớp với quy chuẩn kỹ thuật hoặc thông lệ xã hội",
                "note_vi": "Đi kèm giới từ to/with: conform to specifications / international standards."
            }
        ],
        "confused_words": [
            {
                "word": "confirm",
                "ipa": "/kənˈfɜːrm/",
                "difference_vi": "Confirm là xác nhận kiểm tra lại thông tin (/ɜːr/); conform là tuân thủ phù hợp với tiêu chuẩn (/ɔːr/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Conform to safety standards = phù hợp tiêu chuẩn an toàn; conform to social norms = thuận theo chuẩn mực xã hội."
            }
        ],
        "collocations": [
            {"phrase": "conform to safety standards", "meaning_vi": "phù hợp với các tiêu chuẩn an toàn", "evidence": "corpus"},
            {"phrase": "conform with specifications", "meaning_vi": "ăn khớp với thông số kỹ thuật", "evidence": "corpus"},
            {"phrase": "fail to conform", "meaning_vi": "không đáp ứng chuẩn mực quy định", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "match", "meaning_vi": "khớp với"},
            {"word": "fit", "meaning_vi": "vừa vặn, phù hợp"},
            {"word": "comply", "meaning_vi": "tuân theo"}
        ],
        "examples": [
            {
                "en": "All manufactured parts must conform to rigorous international quality specifications.",
                "vi": "Tất cả các bộ phận được sản xuất phải đáp ứng phù hợp với các thông số kỹ thuật chất lượng quốc tế khắt khe."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈfɔːrm/, nguyên âm /ɔː/ dài có âm /r/ uốn lưỡi rõ nét, phân biệt với /ɜːr/ trong 'confirm'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "observe",
        "lemma": "observe",
        "pos": ["verb"],
        "ipa": {"us": "/əbˈzɜːrv/", "uk": "/əbˈzɜːv/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "observe-1",
                "meaning_vi": "Tuân thủ, chấp hành (luật pháp, thỏa thuận); cử hành (ngày lễ kỷ niệm)",
                "note_vi": "Văn cảnh pháp lý: observe the rules / terms of agreement."
            },
            {
                "id": "observe-2",
                "meaning_vi": "Quan sát kỹ lưỡng bằng mắt để theo dõi hiện tượng",
                "note_vi": "Như trong observe customer behavior."
            }
        ],
        "confused_words": [
            {
                "word": "absorb",
                "ipa": "/əbˈzɔːrb/",
                "difference_vi": "Absorb là hấp thụ, thấm hút (/ɔːr/); observe là quan sát hoặc tuân thủ (/ɜːr/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Observe the law = tuân thủ pháp luật; observe a holiday = nghỉ lễ kỷ niệm; observe behavior = quan sát hành vi."
            }
        ],
        "collocations": [
            {"phrase": "observe the law", "meaning_vi": "tuân thủ luật pháp", "evidence": "corpus"},
            {"phrase": "observe strict confidentiality", "meaning_vi": "tuân thủ nguyên tắc bảo mật nghiêm ngặt", "evidence": "corpus"},
            {"phrase": "observe customer behavior", "meaning_vi": "quan sát hành vi khách mua hàng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "abide by", "meaning_vi": "tuân theo"},
            {"word": "watch", "meaning_vi": "theo dõi"},
            {"word": "celebrate", "meaning_vi": "kỷ niệm ngày lễ"}
        ],
        "examples": [
            {
                "en": "All employees are expected to observe strict confidentiality regarding trade secrets.",
                "vi": "Mọi nhân viên đều được kỳ vọng sẽ tuân thủ nghiêm ngặt chế độ bảo mật đối với các bí mật kinh doanh."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈzɜːrv/, chữ 's' phát âm thành /z/ rung, đuôi là /rv/ khép kín.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "regulation",
        "lemma": "regulation",
        "pos": ["noun"],
        "ipa": {"us": "/ˌreɡjuˈleɪʃn/", "uk": "/ˌreɡjuˈleɪʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "regulation-1",
                "meaning_vi": "Quy định, quy chế chính thức do cơ quan quản lý hoặc ban giám đốc ban hành",
                "note_vi": "Các quy tắc bắt buộc nhân viên và doanh nghiệp phải tuân theo."
            }
        ],
        "confused_words": [
            {
                "word": "regular",
                "ipa": "/ˈreɡjələr/",
                "difference_vi": "Regular là tính từ đều đặn hoặc bình thường; regulation là danh từ quy chế điều lệ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Safety regulations = quy chuẩn an toàn; government regulation = sự điều tiết của nhà nước."
            }
        ],
        "collocations": [
            {"phrase": "safety regulations", "meaning_vi": "các quy định an toàn", "evidence": "corpus"},
            {"phrase": "comply with regulations", "meaning_vi": "tuân thủ các quy định hiện hành", "evidence": "corpus"},
            {"phrase": "tighten regulations", "meaning_vi": "siết chặt các quy chế quản lý", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "rule", "meaning_vi": "quy tắc"},
            {"word": "code", "meaning_vi": "bộ quy tắc"},
            {"word": "directive", "meaning_vi": "chỉ thị"}
        ],
        "examples": [
            {
                "en": "Strict safety regulations must be observed by all personnel working on the construction site.",
                "vi": "Các quy định an toàn nghiêm ngặt phải được toàn thể nhân sự làm việc tại công trường tuân thủ."
            }
        ],
        "pronunciation_tips_vi": "Từ có 4 âm tiết, trọng âm chính rơi vào âm thứ ba /ˈleɪ/, đuôi kết thúc là /ʃn/ tròn môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "legislation",
        "lemma": "legislation",
        "pos": ["noun"],
        "ipa": {"us": "/ˌledʒɪsˈleɪʃn/", "uk": "/ˌledʒɪsˈleɪʃn/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "legislation-1",
                "meaning_vi": "Luật pháp, đạo luật, các văn bản quy phạm pháp luật do quốc hội ban hành",
                "note_vi": "Khung pháp lý cao nhất điều chỉnh hoạt động của toàn xã hội và doanh nghiệp."
            }
        ],
        "confused_words": [
            {
                "word": "legislator",
                "ipa": "/ˈledʒɪsleɪtər/",
                "difference_vi": "Legislator là nhà làm luật (đại biểu quốc hội); legislation là văn bản pháp luật hoặc công tác lập pháp."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Pass legislation = thông qua một đạo luật; under current legislation = chiếu theo pháp luật hiện hành."
            }
        ],
        "collocations": [
            {"phrase": "pass legislation", "meaning_vi": "thông qua một đạo luật", "evidence": "corpus"},
            {"phrase": "under current legislation", "meaning_vi": "theo luật pháp hiện hành", "evidence": "corpus"},
            {"phrase": "environmental legislation", "meaning_vi": "luật về bảo vệ môi trường", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "statute", "meaning_vi": "đạo luật thành văn"},
            {"word": "law", "meaning_vi": "luật pháp"},
            {"word": "act", "meaning_vi": "đạo luật"}
        ],
        "examples": [
            {
                "en": "Parliament recently passed new legislation to protect consumer privacy in digital transactions.",
                "vi": "Quốc hội gần đây đã thông qua đạo luật mới nhằm bảo vệ quyền riêng tư của người tiêu dùng trong các giao dịch số."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ ba /ˈleɪ/, chú ý âm tắc xát /dʒ/ ở đầu /ˈledʒ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "policy",
        "lemma": "policy",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpɑːləsi/", "uk": "/ˈpɒləsi/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "policy-1",
                "meaning_vi": "Chính sách, chủ trương nguyên tắc của công ty hoặc chính phủ",
                "note_vi": "Văn bản định hướng hành động chung như return policy (chính sách đổi trả)."
            },
            {
                "id": "policy-2",
                "meaning_vi": "Hợp đồng bảo hiểm (insurance policy)",
                "note_vi": "Chứng thư cam kết bồi thường bảo hiểm."
            }
        ],
        "confused_words": [
            {
                "word": "police",
                "ipa": "/pəˈliːs/",
                "difference_vi": "Police là cảnh sát (nhấn âm 2); policy là chính sách hoặc hợp đồng bảo hiểm (nhấn âm 1)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Company policy = chính sách công ty; insurance policy = hợp đồng bảo hiểm rủi ro."
            }
        ],
        "collocations": [
            {"phrase": "company policy", "meaning_vi": "chính sách nội bộ của công ty", "evidence": "corpus"},
            {"phrase": "return policy", "meaning_vi": "chính sách đổi trả hàng", "evidence": "corpus"},
            {"phrase": "insurance policy", "meaning_vi": "hợp đồng bảo hiểm", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "strategy", "meaning_vi": "chiến lược"},
            {"word": "guidelines", "meaning_vi": "chỉ dẫn đường lối"},
            {"word": "protocol", "meaning_vi": "nghi thức, quy trình"}
        ],
        "examples": [
            {
                "en": "In accordance with company policy, all receipts must be reviewed before reimbursement is issued.",
                "vi": "Theo đúng chính sách của công ty, tất cả hóa đơn phải được xét duyệt trước khi xuất tiền bồi hoàn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈpɑː/, nguyên âm /ɑː/ dài trong tiếng Mỹ, đừng đọc nhầm thành 'police'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "lawsuit",
        "lemma": "lawsuit",
        "pos": ["noun"],
        "ipa": {"us": "/ˈlɔːsuːt/", "uk": "/ˈlɔːsjuːt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "lawsuit-1",
                "meaning_vi": "Vụ kiện cáo, việc khởi kiện dân sự trước tòa án",
                "note_vi": "Collocation kinh điển: file a lawsuit against sb (đâm đơn kiện ai ra tòa)."
            }
        ],
        "confused_words": [
            {
                "word": "suit",
                "ipa": "/suːt/",
                "difference_vi": "Suit là bộ comple âu phục; lawsuit là vụ kiện tụng pháp đình."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "File a lawsuit = đệ đơn kiện; settle a lawsuit = hòa giải giàn xếp vụ kiện ngoài tòa."
            }
        ],
        "collocations": [
            {"phrase": "file a lawsuit", "meaning_vi": "đâm đơn khởi kiện ra tòa", "evidence": "corpus"},
            {"phrase": "settle a lawsuit", "meaning_vi": "dàn xếp hòa giải một vụ kiện", "evidence": "corpus"},
            {"phrase": "threat of a lawsuit", "meaning_vi": "nguy cơ bị khởi kiện trước pháp luật", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "litigation", "meaning_vi": "quá trình tố tụng kiện cáo"},
            {"word": "legal action", "meaning_vi": "hành động pháp lý"},
            {"word": "court case", "meaning_vi": "vụ án tại tòa"}
        ],
        "examples": [
            {
                "en": "The corporation filed a lawsuit against its former supplier for breach of confidentiality.",
                "vi": "Tập đoàn đã đệ đơn kiện nhà cung cấp cũ ra tòa vì vi phạm thỏa thuận bảo mật."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép gồm 'law' /ˈlɔː/ và 'suit' /suːt/, trọng âm chính nhấn ở âm đầu.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "attorney",
        "lemma": "attorney",
        "pos": ["noun"],
        "ipa": {"us": "/əˈtɜːrni/", "uk": "/əˈtɜːni/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "attorney-1",
                "meaning_vi": "Luật sư đại diện pháp lý, người được ủy quyền hành động trước pháp luật",
                "note_vi": "Từ thông dụng tại Mỹ tương đương lawyer (lawyer là người có bằng luật; attorney là người đại diện trước tòa)."
            }
        ],
        "confused_words": [
            {
                "word": "lawyer",
                "ipa": "/ˈlɔːjər/",
                "difference_vi": "Lawyer là danh từ chung chỉ giới luật gia; attorney là luật sư đại diện thân chủ trong vụ việc cụ thể."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Corporate attorney = luật sư doanh nghiệp; power of attorney = giấy ủy quyền pháp lý."
            }
        ],
        "collocations": [
            {"phrase": "consult an attorney", "meaning_vi": "tham vấn ý kiến luật sư", "evidence": "corpus"},
            {"phrase": "corporate attorney", "meaning_vi": "luật sư đại diện cho doanh nghiệp", "evidence": "corpus"},
            {"phrase": "power of attorney", "meaning_vi": "giấy ủy quyền pháp lý", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "lawyer", "meaning_vi": "luật sư"},
            {"word": "counsel", "meaning_vi": "cố vấn pháp luật"},
            {"word": "barrister", "meaning_vi": "luật sư tranh tụng (Anh)"}
        ],
        "examples": [
            {
                "en": "We consulted a specialized corporate attorney before signing the international licensing agreement.",
                "vi": "Chúng tôi đã tham vấn một luật sư doanh nghiệp chuyên ngành trước khi ký thỏa thuận cấp phép quốc tế."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈtɜːr/, uốn lưỡi âm /r/ rõ nét trong tiếng Mỹ, kết thúc bằng /ni/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "penalty",
        "lemma": "penalty",
        "pos": ["noun"],
        "ipa": {"us": "/ˈpenəlti/", "uk": "/ˈpenəlti/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "penalty-1",
                "meaning_vi": "Hình phạt, mức tiền phạt do vi phạm hợp đồng hoặc không tuân thủ quy định",
                "note_vi": "Khoản chế tài tài chính áp đặt khi một bên không hoàn thành cam kết."
            }
        ],
        "confused_words": [
            {
                "word": "fine",
                "ipa": "/faɪn/",
                "difference_vi": "Fine là tiền phạt vi phạm pháp luật công quyền (giao thông, trốn thuế); penalty bao gồm cả phạt vi phạm hợp đồng kinh tế tư nhân."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Early withdrawal penalty = phí phạt rút tiền tiết kiệm trước hạn; penalty clause = điều khoản phạt vi phạm."
            }
        ],
        "collocations": [
            {"phrase": "pay a penalty", "meaning_vi": "nộp tiền phạt vi phạm", "evidence": "corpus"},
            {"phrase": "penalty clause", "meaning_vi": "điều khoản phạt hợp đồng", "evidence": "corpus"},
            {"phrase": "without penalty", "meaning_vi": "không bị phạt tiền, miễn phạt", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "fine", "meaning_vi": "tiền phạt"},
            {"word": "sanction", "meaning_vi": "biện pháp chế tài"},
            {"word": "punishment", "meaning_vi": "hình phạt"}
        ],
        "examples": [
            {
                "en": "Customers can cancel their reservation up to 48 hours prior to arrival without penalty.",
                "vi": "Khách hàng có thể hủy đặt phòng tối đa 48 giờ trước khi đến mà không bị phạt tiền."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈpen/, âm giữa lướt /əl/, kết thúc bằng /ti/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "fine",
        "lemma": "fine",
        "pos": ["noun", "verb", "adjective"],
        "ipa": {"us": "/faɪn/", "uk": "/faɪn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "fine-1",
                "meaning_vi": "Khoản tiền phạt do cơ quan chức năng hoặc tòa án áp đặt; (v) phạt tiền",
                "note_vi": "Phổ biến trong vi phạm luật giao thông, trốn thuế hoặc xả thải sai quy định."
            },
            {
                "id": "fine-2",
                "meaning_vi": "Tốt đẹp, chất lượng cao hoặc sắc mảnh tinh tế (adjective)",
                "note_vi": "Như trong fine dining (ẩm thực cao cấp), fine print (dòng chữ nhỏ trong hợp đồng)."
            }
        ],
        "confused_words": [
            {
                "word": "fee",
                "ipa": "/fiː/",
                "difference_vi": "Fee là lệ phí dịch vụ thông thường; fine là tiền phạt do làm sai luật."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Pay a heavy fine = nộp khoản tiền phạt nặng; fine dining = dịch vụ nhà hàng sang trọng."
            }
        ],
        "collocations": [
            {"phrase": "pay a heavy fine", "meaning_vi": "nộp một khoản tiền phạt nặng", "evidence": "corpus"},
            {"phrase": "impose a fine", "meaning_vi": "áp đặt mức phạt tiền", "evidence": "corpus"},
            {"phrase": "read the fine print", "meaning_vi": "đọc kỹ các điều khoản chữ nhỏ trong hợp đồng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "penalty", "meaning_vi": "hình phạt tiền"},
            {"word": "financial sanction", "meaning_vi": "chế tài tài chính"}
        ],
        "examples": [
            {
                "en": "The chemical plant was fined $50,000 for improper disposal of industrial wastewater.",
                "vi": "Nhà máy hóa chất đã bị phạt 50.000 đô la do xả nước thải công nghiệp không đúng quy định."
            }
        ],
        "pronunciation_tips_vi": "Phát âm /faɪn/ với nhị trùng âm /aɪ/ mở rộng khẩu hình, kết thúc bằng âm /n/ ngân mũi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "liable",
        "lemma": "liable",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈlaɪəbl/", "uk": "/ˈlaɪəbl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "liable-1",
                "meaning_vi": "Có trách nhiệm pháp lý phải bồi thường thiệt hại (legally liable)",
                "note_vi": "Cấu trúc: be held liable for damage / be liable to pay."
            },
            {
                "id": "liable-2",
                "meaning_vi": "Có khả năng dễ bị, có xu hướng xảy ra điều không tốt (liable to do sth)",
                "note_vi": "Tương tự prone to hoặc likely to."
            }
        ],
        "confused_words": [
            {
                "word": "reliable",
                "ipa": "/rɪˈlaɪəbl/",
                "difference_vi": "Reliable là đáng tin cậy; liable là chịu trách nhiệm pháp lý hoặc dễ bị tổn thương."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Legally liable for loss = chịu trách nhiệm pháp lý bồi thường thiệt hại; liable to change = dễ bị biến động thay đổi."
            }
        ],
        "collocations": [
            {"phrase": "held legally liable", "meaning_vi": "bị quy trách nhiệm pháp lý bồi thường", "evidence": "corpus"},
            {"phrase": "liable for damages", "meaning_vi": "có nghĩa vụ bồi thường thiệt hại", "evidence": "corpus"},
            {"phrase": "liable to change without notice", "meaning_vi": "có thể thay đổi mà không cần báo trước", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "responsible", "meaning_vi": "chịu trách nhiệm"},
            {"word": "accountable", "meaning_vi": "phải giải trình, chịu hậu quả"},
            {"word": "answerable", "meaning_vi": "có nghĩa vụ trả lời trước pháp luật"}
        ],
        "examples": [
            {
                "en": "The contractor will be held legally liable for any structural flaws discovered within three years.",
                "vi": "Nhà thầu sẽ phải chịu trách nhiệm pháp lý đối với bất kỳ lỗi kết cấu nào được phát hiện trong vòng ba năm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈlaɪ/, âm thứ hai lướt nhẹ /əbl/, không đọc thành 'lai-a-bồ'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "confidential",
        "lemma": "confidential",
        "pos": ["adjective"],
        "ipa": {"us": "/ˌkɑːnfɪˈdenʃl/", "uk": "/ˌkɒnfɪˈdenʃl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "contracts-negotiation"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "confidential-1",
                "meaning_vi": "Bảo mật, tuyệt mật, không được phép tiết lộ ra ngoài",
                "note_vi": "Đóng dấu đỏ 'CONFIDENTIAL' trên hồ sơ nhân sự, tài chính hoặc bí mật công nghệ."
            }
        ],
        "confused_words": [
            {
                "word": "confident",
                "ipa": "/ˈkɑːnfɪdənt/",
                "difference_vi": "Confident là tự tin (trọng âm 1); confidential là bí mật, mang tính bảo mật cao (trọng âm 3)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Confidential information = thông tin tuyệt mật; strictly confidential = bảo mật tuyệt đối."
            }
        ],
        "collocations": [
            {"phrase": "strictly confidential", "meaning_vi": "tuyệt mật, bảo mật nghiêm ngặt", "evidence": "corpus"},
            {"phrase": "confidential documents", "meaning_vi": "tài liệu bảo mật", "evidence": "corpus"},
            {"phrase": "keep information confidential", "meaning_vi": "giữ kín thông tin bảo mật", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "secret", "meaning_vi": "bí mật"},
            {"word": "classified", "meaning_vi": "thuộc diện tuyệt mật"},
            {"word": "private", "meaning_vi": "riêng tư, không công khai"}
        ],
        "examples": [
            {
                "en": "All employees must sign a non-disclosure agreement to keep client records strictly confidential.",
                "vi": "Tất cả nhân viên phải ký thỏa thuận không tiết lộ để giữ cho hồ sơ khách hàng được bảo mật tuyệt đối."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ ba /ˈden/, đuôi kết thúc là /ʃl/ cong môi nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "mandatory",
        "lemma": "mandatory",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈmændətɔːri/", "uk": "/ˈmændətəri/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "human-resources"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "mandatory-1",
                "meaning_vi": "Mang tính bắt buộc theo luật hoặc theo quy định của tổ chức",
                "note_vi": "Trái nghĩa với optional (tùy chọn tự nguyện)."
            }
        ],
        "confused_words": [
            {
                "word": "optional",
                "ipa": "/ˈɑːpʃənl/",
                "difference_vi": "Optional là tự chọn tùy ý; mandatory là bắt buộc phải tuân thủ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Mandatory training session = buổi tập huấn bắt buộc; mandatory requirement = yêu cầu bắt buộc không thể thiếu."
            }
        ],
        "collocations": [
            {"phrase": "mandatory training session", "meaning_vi": "buổi tập huấn bắt buộc", "evidence": "corpus"},
            {"phrase": "mandatory requirement", "meaning_vi": "yêu cầu bắt buộc", "evidence": "corpus"},
            {"phrase": "make attendance mandatory", "meaning_vi": "bắt buộc phải tham dự đầy đủ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "compulsory", "meaning_vi": "cưỡng bách, bắt buộc"},
            {"word": "obligatory", "meaning_vi": "có tính nghĩa vụ bắt buộc"},
            {"word": "required", "meaning_vi": "được yêu cầu"}
        ],
        "examples": [
            {
                "en": "Attendance at the annual workplace safety briefing is mandatory for all production personnel.",
                "vi": "Việc tham dự buổi hướng dẫn an toàn nơi làm việc thường niên là bắt buộc đối với toàn thể nhân viên sản xuất."
            }
        ],
        "pronunciation_tips_vi": "Trong tiếng Mỹ phát âm là /ˈmændətɔːri/ có âm /tɔː/ rõ ở âm tiết thứ ba; tiếng Anh là /ˈmændətəri/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "authorize",
        "lemma": "authorize",
        "pos": ["verb"],
        "ipa": {"us": "/ˈɔːθəraɪz/", "uk": "/ˈɔːθəraɪz/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "authorize-1",
                "meaning_vi": "Cấp phép chính thức, ủy quyền hoặc phê duyệt quyền hạn cho ai làm gì",
                "note_vi": "Hành động cho phép bằng văn bản hoặc mật khẩu hệ thống."
            }
        ],
        "confused_words": [
            {
                "word": "authority",
                "ipa": "/əˈθɔːrəti/",
                "difference_vi": "Authority là danh từ thẩm quyền hoặc nhà chức trách; authorize là động từ cấp quyền, phê duyệt."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Authorized personnel only = chỉ dành riêng cho nhân viên có thẩm quyền; authorize expenditure = phê duyệt khoản chi tiêu."
            }
        ],
        "collocations": [
            {"phrase": "authorized personnel only", "meaning_vi": "chỉ nhân sự được cấp phép mới được vào", "evidence": "corpus"},
            {"phrase": "authorize payment", "meaning_vi": "phê duyệt lệnh thanh toán", "evidence": "corpus"},
            {"phrase": "officially authorize", "meaning_vi": "chính thức cấp quyền cho phép", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "approve", "meaning_vi": "phê chuẩn"},
            {"word": "sanction", "meaning_vi": "cho phép chính thức"},
            {"word": "empower", "meaning_vi": "trao quyền"}
        ],
        "examples": [
            {
                "en": "Only the chief financial officer is authorized to approve capital expenditures exceeding $10,000.",
                "vi": "Chỉ giám đốc tài chính mới có thẩm quyền phê duyệt các khoản chi đầu tư vượt quá 10.000 đô la."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈɔːθ/, âm /θ/ cắn nhẹ đầu lưỡi thổi hơi, âm đuôi /raɪz/ kết thúc bằng âm rung /z/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "restrict",
        "lemma": "restrict",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈstrɪkt/", "uk": "/rɪˈstrɪkt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["legal-compliance", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "restrict-1",
                "meaning_vi": "Hạn chế, giới hạn quyền truy cập, số lượng hoặc phạm vi áp dụng",
                "note_vi": "Đặt ra ranh giới ngăn cấm sự bành trướng hoặc xâm nhập tự do."
            }
        ],
        "confused_words": [
            {
                "word": "strict",
                "ipa": "/strɪkt/",
                "difference_vi": "Strict là tính từ nghiêm ngặt; restrict là động từ hạn chế, giới hạn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Restricted area = khu vực giới hạn ra vào; restrict access = hạn chế quyền truy cập."
            }
        ],
        "collocations": [
            {"phrase": "restrict access to", "meaning_vi": "hạn chế quyền tiếp cận tới", "evidence": "corpus"},
            {"phrase": "restricted area", "meaning_vi": "khu vực giới hạn ra vào", "evidence": "corpus"},
            {"phrase": "restrict spending", "meaning_vi": "thắt chặt chi tiêu", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "limit", "meaning_vi": "giới hạn"},
            {"word": "confine", "meaning_vi": "giam hãm, thu hẹp"},
            {"word": "constrain", "meaning_vi": "ràng buộc"}
        ],
        "examples": [
            {
                "en": "Access to the server room is strictly restricted to certified network administrators.",
                "vi": "Việc ra vào phòng máy chủ bị hạn chế nghiêm ngặt, chỉ dành cho các quản trị viên mạng đã được cấp chứng chỉ."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈstrɪkt/, cụm phụ âm /str/ lướt nhanh dứt khoát kết thúc bằng /kt/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "prohibit",
        "lemma": "prohibit",
        "pos": ["verb"],
        "ipa": {"us": "/prəˈhɪbɪt/", "uk": "/prəˈhɪbɪt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["legal-compliance"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "prohibit-1",
                "meaning_vi": "Cấm đoán tuyệt đối theo luật hoặc theo quy định chính thức",
                "note_vi": "Mức độ cấm đoán nặng nề và mang tính pháp chế hơn từ ban thông thường."
            }
        ],
        "confused_words": [
            {
                "word": "inhibit",
                "ipa": "/ɪnˈhɪbɪt/",
                "difference_vi": "Inhibit là ức chế, kìm hãm sự phát triển sinh học/tâm lý; prohibit là cấm đoán bằng luật lệ."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Strictly prohibited = bị nghiêm cấm hoàn toàn; prohibit from doing sth = cấm ai làm việc gì."
            }
        ],
        "collocations": [
            {"phrase": "strictly prohibited", "meaning_vi": "bị nghiêm cấm tuyệt đối", "evidence": "corpus"},
            {"phrase": "prohibit by law", "meaning_vi": "bị cấm theo quy định của pháp luật", "evidence": "corpus"},
            {"phrase": "prohibit smoking", "meaning_vi": "cấm hút thuốc", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "ban", "meaning_vi": "cấm vận, cấm chỉ"},
            {"word": "forbid", "meaning_vi": "ngăn cấm"},
            {"word": "bar", "meaning_vi": "chặn cửa cấm đoán"}
        ],
        "examples": [
            {
                "en": "Taking photographs inside the manufacturing cleanroom is strictly prohibited by company policy.",
                "vi": "Việc chụp ảnh bên trong phòng sạch sản xuất bị nghiêm cấm tuyệt đối theo chính sách của công ty."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈhɪb/, âm /h/ phát âm rõ ràng, không đọc lướt câm.",
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
    for w in words_group4b:
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
    print(f"\n[OK] Group 4B created {count} words successfully.")

if __name__ == "__main__":
    main()
