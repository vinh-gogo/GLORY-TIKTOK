# -*- coding: utf-8 -*-
"""
Batch generator for Lexicon Group 3:
Bán hàng, Dịch vụ, Sản xuất & Vận chuyển (31 words)
"""
import os
import yaml

words_group3 = [
    {
        "id": "transaction",
        "lemma": "transaction",
        "pos": ["noun"],
        "ipa": {"us": "/trænˈzækʃn/", "uk": "/trænˈzækʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service", "finance-accounting"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "transaction-1",
                "meaning_vi": "Giao dịch thương mại, việc mua bán hoặc chuyển tiền",
                "note_vi": "Hành vi trao đổi thanh toán giữa người mua và người bán."
            }
        ],
        "confused_words": [
            {
                "word": "transition",
                "ipa": "/trænˈzɪʃn/",
                "difference_vi": "Transition là sự chuyển tiếp giai đoạn; transaction là giao dịch tiền tệ/thương mại."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Bank transaction là giao dịch ngân hàng; real estate transaction là mua bán bất động sản."
            }
        ],
        "collocations": [
            {"phrase": "complete a transaction", "meaning_vi": "hoàn tất giao dịch", "evidence": "corpus"},
            {"phrase": "secure online transaction", "meaning_vi": "giao dịch trực tuyến bảo mật", "evidence": "corpus"},
            {"phrase": "business transaction", "meaning_vi": "giao dịch thương mại", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "deal", "meaning_vi": "thương vụ"},
            {"word": "trade", "meaning_vi": "hoạt động trao đổi mua bán"}
        ],
        "examples": [
            {
                "en": "You will receive an automated confirmation email once the transaction is completed.",
                "vi": "Bạn sẽ nhận được email xác nhận tự động sau khi giao dịch được hoàn tất."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /zæk/, đuôi kết thúc bằng /ʃn/ cong môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "wholesale",
        "lemma": "wholesale",
        "pos": ["noun", "adjective", "adverb"],
        "ipa": {"us": "/ˈhoʊlseɪl/", "uk": "/ˈhəʊlseɪl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["sales-customer-service", "shipping-logistics"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "wholesale-1",
                "meaning_vi": "Bán buôn, bán sỉ số lượng lớn với mức chiết khấu cao",
                "note_vi": "Ngược nghĩa trực tiếp với retail (bán lẻ)."
            }
        ],
        "confused_words": [
            {
                "word": "retail",
                "ipa": "/ˈriːteɪl/",
                "difference_vi": "Wholesale là bán sỉ cho các đại lý; retail là bán lẻ trực tiếp tới tay người tiêu dùng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Wholesale price là đơn giá bán sỉ; buy at wholesale nghĩa là mua với giá buôn sỉ."
            }
        ],
        "collocations": [
            {"phrase": "wholesale price", "meaning_vi": "giá bán buôn / bán sỉ", "evidence": "corpus"},
            {"phrase": "wholesale distributor", "meaning_vi": "nhà phân phối bán sỉ", "evidence": "corpus"},
            {"phrase": "buy at wholesale", "meaning_vi": "mua với giá sỉ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "bulk selling", "meaning_vi": "bán theo lô lớn"},
            {"word": "volume distribution", "meaning_vi": "phân phối số lượng lớn"}
        ],
        "examples": [
            {
                "en": "Retail stores purchase goods from the wholesale distributor at a 40% discount.",
                "vi": "Các cửa hàng bán lẻ mua hàng hóa từ nhà phân phối bán sỉ với mức chiết khấu 40%."
            }
        ],
        "pronunciation_tips_vi": "Chữ 'w' câm, phát âm bắt đầu bằng âm /h/ thở nhẹ /ˈhoʊl/, âm hai là /seɪl/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "retail",
        "lemma": "retail",
        "pos": ["noun", "adjective", "adverb"],
        "ipa": {"us": "/ˈriːteɪl/", "uk": "/ˈriːteɪl/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "retail-1",
                "meaning_vi": "Bán lẻ hàng hóa trực tiếp tới người tiêu dùng tại cửa hàng hoặc trực tuyến",
                "note_vi": "Kênh phân phối chặng cuối đến tay khách hàng cá nhân."
            }
        ],
        "confused_words": [
            {
                "word": "detail",
                "ipa": "/ˈdiːteɪl/",
                "difference_vi": "Detail là chi tiết cụ thể; retail là hoạt động bán lẻ hàng hóa."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Retail outlet = điểm bán lẻ; retail price = giá bán lẻ niêm yết cho khách."
            }
        ],
        "collocations": [
            {"phrase": "retail outlet", "meaning_vi": "cửa hàng bán lẻ", "evidence": "corpus"},
            {"phrase": "suggested retail price", "meaning_vi": "giá bán lẻ đề xuất của nhà sản xuất", "evidence": "corpus"},
            {"phrase": "retail chain", "meaning_vi": "chuỗi cửa hàng bán lẻ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "store selling", "meaning_vi": "bán hàng tại tiệm"},
            {"word": "consumer sales", "meaning_vi": "bán hàng cho người tiêu dùng"}
        ],
        "examples": [
            {
                "en": "The nationwide retail chain opened three new locations in metropolitan shopping malls.",
                "vi": "Chuỗi bán lẻ trên toàn quốc đã khai trương ba địa điểm mới tại các trung tâm thương mại đô thị."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ nhất /ˈriː/, nguyên âm /iː/ kéo dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "voucher",
        "lemma": "voucher",
        "pos": ["noun"],
        "ipa": {"us": "/ˈvaʊtʃər/", "uk": "/ˈvaʊtʃə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "voucher-1",
                "meaning_vi": "Phiếu quà tặng, phiếu giảm giá hoặc chứng từ thanh toán dịch vụ",
                "note_vi": "Văn bản hoặc mã số điện tử dùng để trừ tiền khi mua sắm."
            }
        ],
        "confused_words": [
            {
                "word": "coupon",
                "ipa": "/ˈkuːpɑːn/",
                "difference_vi": "Coupon thường là mẩu phiếu giảm giá ngắn hạn; voucher có thể là phiếu quà tặng mệnh giá tiền cố định."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Gift voucher = phiếu quà tặng; travel voucher = phiếu giảm giá vé máy bay/khách sạn bù đắp chậm trễ."
            }
        ],
        "collocations": [
            {"phrase": "discount voucher", "meaning_vi": "phiếu giảm giá", "evidence": "corpus"},
            {"phrase": "redeem a gift voucher", "meaning_vi": "đổi phiếu quà tặng để lấy hàng", "evidence": "corpus"},
            {"phrase": "promotional voucher", "meaning_vi": "phiếu ưu đãi khuyến mãi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "coupon", "meaning_vi": "phiếu mua hàng giảm giá"},
            {"word": "token", "meaning_vi": "phiếu thế chân, tích lũy"}
        ],
        "examples": [
            {
                "en": "Passengers whose flights were delayed received a dinner voucher for the terminal restaurant.",
                "vi": "Những hành khách có chuyến bay bị hoãn đã nhận được phiếu ăn tối tại nhà hàng trong nhà ga."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈvaʊ/, nhị trùng âm /aʊ/ rõ ràng, kết thúc bằng /tʃər/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "redeem",
        "lemma": "redeem",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈdiːm/", "uk": "/rɪˈdiːm/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["sales-customer-service"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "redeem-1",
                "meaning_vi": "Quy đổi phiếu thưởng, mã giảm giá hoặc điểm tích lũy thành quà/tiền mặt",
                "note_vi": "Hành động sử dụng voucher hoặc điểm thưởng tại quầy thanh toán."
            }
        ],
        "confused_words": [
            {
                "word": "deem",
                "ipa": "/diːm/",
                "difference_vi": "Deem nghĩa là coi như, cho rằng; redeem là quy đổi phiếu lấy hàng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Redeem a coupon = quy đổi phiếu giảm giá; redeem oneself = chuộc lại lỗi lầm."
            }
        ],
        "collocations": [
            {"phrase": "redeem a coupon", "meaning_vi": "đổi phiếu giảm giá khi thanh toán", "evidence": "corpus"},
            {"phrase": "redeem reward points", "meaning_vi": "đổi điểm tích lũy thưởng thành quà", "evidence": "corpus"},
            {"phrase": "redeemable for cash", "meaning_vi": "có thể quy đổi ra tiền mặt", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "exchange", "meaning_vi": "đổi lấy"},
            {"word": "cash in", "meaning_vi": "đổi thành tiền mặt"}
        ],
        "examples": [
            {
                "en": "Customers can redeem their accumulated loyalty points for merchandise or store discounts.",
                "vi": "Khách hàng có thể đổi điểm tích lũy thành viên của mình để lấy hàng hóa hoặc giảm giá mua sắm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /diːm/, nguyên âm /iː/ kéo dài.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "feedback",
        "lemma": "feedback",
        "pos": ["noun"],
        "ipa": {"us": "/ˈfiːdbæk/", "uk": "/ˈfiːdbæk/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "feedback-1",
                "meaning_vi": "Ý kiến phản hồi, nhận xét đánh giá của khách hàng hoặc cấp trên",
                "note_vi": "Là danh từ không đếm được (uncountable noun), không thêm số nhiều -s."
            }
        ],
        "confused_words": [
            {
                "word": "feed",
                "ipa": "/fiːd/",
                "difference_vi": "Feed là cho ăn hoặc cung cấp dữ liệu; feedback là ý kiến đánh giá phản hồi."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Positive feedback = lời khen ngợi phản hồi tốt; constructive feedback = góp ý mang tính xây dựng."
            }
        ],
        "collocations": [
            {"phrase": "customer feedback", "meaning_vi": "phản hồi từ khách hàng", "evidence": "corpus"},
            {"phrase": "provide constructive feedback", "meaning_vi": "đưa ra ý kiến đóng góp mang tính xây dựng", "evidence": "corpus"},
            {"phrase": "feedback form", "meaning_vi": "phiếu lấy ý kiến phản hồi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "comments", "meaning_vi": "bình luận, ý kiến"},
            {"word": "evaluation", "meaning_vi": "đánh giá"},
            {"word": "response", "meaning_vi": "phản hồi"}
        ],
        "examples": [
            {
                "en": "We appreciate your feedback and will use your suggestions to improve our customer support.",
                "vi": "Chúng tôi rất trân trọng phản hồi của bạn và sẽ sử dụng những đề xuất này để cải thiện dịch vụ hỗ trợ khách hàng."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép gồm 'feed' /fiːd/ và 'back' /bæk/, trọng âm chính nhấn ở /ˈfiːd/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "satisfaction",
        "lemma": "satisfaction",
        "pos": ["noun"],
        "ipa": {"us": "/ˌsætɪsˈfækʃn/", "uk": "/ˌsætɪsˈfækʃn/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "satisfaction-1",
                "meaning_vi": "Sự hài lòng, sự thỏa mãn về chất lượng dịch vụ hoặc sản phẩm",
                "note_vi": "Mục tiêu hàng đầu trong quản trị trải nghiệm khách hàng."
            }
        ],
        "confused_words": [
            {
                "word": "satisfy",
                "ipa": "/ˈsætɪsfaɪ/",
                "difference_vi": "Satisfy là động từ làm thỏa mãn; satisfaction là danh từ sự hài lòng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Customer satisfaction = sự hài lòng của khách; job satisfaction = sự thỏa mãn với công việc hiện tại."
            }
        ],
        "collocations": [
            {"phrase": "customer satisfaction", "meaning_vi": "sự hài lòng của khách hàng", "evidence": "corpus"},
            {"phrase": "satisfaction guarantee", "meaning_vi": "cam kết bảo đảm làm khách hài lòng", "evidence": "corpus"},
            {"phrase": "express satisfaction", "meaning_vi": "bày tỏ sự hài lòng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "contentment", "meaning_vi": "sự bằng lòng"},
            {"word": "pleasure", "meaning_vi": "sự vui vẻ, hài lòng"}
        ],
        "examples": [
            {
                "en": "Recent surveys show an 85% rate of customer satisfaction with our online banking services.",
                "vi": "Các cuộc khảo sát gần đây cho thấy tỷ lệ hài lòng của khách hàng đạt 85% đối với các dịch vụ ngân hàng trực tuyến của chúng tôi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ ba /ˈfæk/, đuôi kết thúc là /ʃn/ cong môi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "dissatisfaction",
        "lemma": "dissatisfaction",
        "pos": ["noun"],
        "ipa": {"us": "/dɪsˌsætɪsˈfækʃn/", "uk": "/dɪsˌsætɪsˈfækʃn/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["sales-customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "dissatisfaction-1",
                "meaning_vi": "Sự bất mãn, sự không hài lòng về chất lượng phục vụ hoặc sản phẩm",
                "note_vi": "Trái nghĩa với satisfaction, thường dẫn đến phàn nàn và yêu cầu hoàn tiền."
            }
        ],
        "confused_words": [
            {
                "word": "satisfaction",
                "ipa": "/ˌsætɪsˈfækʃn/",
                "difference_vi": "Satisfaction là hài lòng; thêm tiền tố dis- tạo thành từ trái nghĩa (không hài lòng)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Express dissatisfaction = bày tỏ sự không hài lòng; cause of dissatisfaction = nguyên nhân gây bức xúc."
            }
        ],
        "collocations": [
            {"phrase": "express dissatisfaction", "meaning_vi": "bày tỏ sự không hài lòng", "evidence": "corpus"},
            {"phrase": "customer dissatisfaction", "meaning_vi": "sự bất mãn của khách hàng", "evidence": "corpus"},
            {"phrase": "source of dissatisfaction", "meaning_vi": "nguyên nhân gây bức xúc, bất bình", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "discontent", "meaning_vi": "sự bất mãn"},
            {"word": "displeasure", "meaning_vi": "sự phật ý, không vừa lòng"}
        ],
        "examples": [
            {
                "en": "Several diners expressed dissatisfaction regarding the prolonged wait times for food delivery.",
                "vi": "Một số thực khách đã bày tỏ sự không hài lòng về thời gian chờ đợi món ăn quá lâu."
            }
        ],
        "pronunciation_tips_vi": "Chú ý âm đôi /s/ ở đầu giữa 'dis' và 'sa', trọng âm chính ở /ˈfæk/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "guarantee",
        "lemma": "guarantee",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/ˌɡærənˈtiː/", "uk": "/ˌɡærənˈtiː/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service", "contracts-negotiation"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "guarantee-1",
                "meaning_vi": "Cam kết bảo đảm chất lượng; giấy bảo hành; (v) cam đoan chắc chắn",
                "note_vi": "Lời hứa chính thức về việc sửa chữa hoặc hoàn tiền nếu sản phẩm gặp trục trặc."
            }
        ],
        "confused_words": [
            {
                "word": "warranty",
                "ipa": "/ˈwɔːrənti/",
                "difference_vi": "Warranty là văn bản bảo hành bằng văn bản cụ thể; guarantee là sự cam kết bảo đảm (vừa là danh từ vừa là động từ)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Money-back guarantee = cam kết hoàn tiền nếu không ưng ý; under guarantee = đang trong thời hạn bảo hành."
            }
        ],
        "collocations": [
            {"phrase": "money-back guarantee", "meaning_vi": "cam kết hoàn tiền nếu không vừa ý", "evidence": "corpus"},
            {"phrase": "under guarantee", "meaning_vi": "đang trong thời gian bảo hành", "evidence": "corpus"},
            {"phrase": "guarantee delivery", "meaning_vi": "cam đoan giao hàng đúng hẹn", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "promise", "meaning_vi": "lời hứa"},
            {"word": "assure", "meaning_vi": "cam đoan, quả quyết"},
            {"word": "warranty", "meaning_vi": "chế độ bảo hành"}
        ],
        "examples": [
            {
                "en": "All our electronic appliances come with a two-year manufacturer guarantee against technical defects.",
                "vi": "Tất cả các thiết bị điện tử của chúng tôi đều đi kèm với cam kết bảo hành hai năm của nhà sản xuất đối với các lỗi kỹ thuật."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết cuối /tiː/, nguyên âm /iː/ kéo dài, không nhấn âm đầu.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "exchange",
        "lemma": "exchange",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/ɪksˈtʃeɪndʒ/", "uk": "/ɪksˈtʃeɪndʒ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["sales-customer-service", "finance-accounting"],
        "speaking_use": ["respond-to-questions", "respond-with-info"],
        "senses": [
            {
                "id": "exchange-1",
                "meaning_vi": "Đổi trả món hàng lấy món khác tại cửa hàng; sự trao đổi ngoại tệ hoặc thông tin",
                "note_vi": "Phổ biến trong chính sách đổi trả hàng hóa (exchange policy)."
            }
        ],
        "confused_words": [
            {
                "word": "change",
                "ipa": "/tʃeɪndʒ/",
                "difference_vi": "Change là thay đổi chung hoặc tiền lẻ; exchange là đổi vật này lấy vật khác tương đương."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Exchange an item = đổi món hàng khác; foreign exchange = giao dịch đổi ngoại tệ."
            }
        ],
        "collocations": [
            {"phrase": "exchange policy", "meaning_vi": "chính sách đổi trả hàng hóa", "evidence": "corpus"},
            {"phrase": "exchange for a different size", "meaning_vi": "đổi lấy kích cỡ khác", "evidence": "corpus"},
            {"phrase": "exchange rate", "meaning_vi": "tỷ giá hối đoái tiền tệ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "swap", "meaning_vi": "hoán đổi"},
            {"word": "trade", "meaning_vi": "trao đổi hàng"}
        ],
        "examples": [
            {
                "en": "Items purchased on sale can be exchanged within fourteen days with an original store receipt.",
                "vi": "Hàng hóa mua trong đợt giảm giá có thể được đổi trong vòng mười bốn ngày kèm theo hóa đơn gốc."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈtʃeɪndʒ/, âm /tʃ/ bật dứt khoát kết thúc bằng âm rung /dʒ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "complimentary",
        "lemma": "complimentary",
        "pos": ["adjective"],
        "ipa": {"us": "/ˌkɑːmplɪˈmentri/", "uk": "/ˌkɒmplɪˈmentri/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["sales-customer-service", "hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "complimentary-1",
                "meaning_vi": "Miễn phí, được tặng kèm như một dịch vụ ưu đãi",
                "note_vi": "Rất hay gặp trong nhà hàng, khách sạn và các chuyến bay (complimentary breakfast/beverage)."
            }
        ],
        "confused_words": [
            {
                "word": "complementary",
                "ipa": "/ˌkɑːmplɪˈmentri/",
                "difference_vi": "Đồng âm hoàn toàn nhưng khác nghĩa: complementary (có chữ 'e') là bổ sung tương hỗ cho nhau; complimentary (có chữ 'i') là miễn phí hoặc khen ngợi."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Complimentary breakfast = bữa sáng miễn phí kèm phòng; complimentary remarks = lời ngợi khen tán dương."
            }
        ],
        "collocations": [
            {"phrase": "complimentary breakfast", "meaning_vi": "bữa ăn sáng miễn phí", "evidence": "corpus"},
            {"phrase": "complimentary ticket", "meaning_vi": "vé mời xem miễn phí", "evidence": "corpus"},
            {"phrase": "complimentary shuttle service", "meaning_vi": "dịch vụ xe đưa đón miễn phí", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "free of charge", "meaning_vi": "miễn phí hoàn toàn"},
            {"word": "courtesy", "meaning_vi": "mang tính đãi ngộ lịch thiệp"}
        ],
        "examples": [
            {
                "en": "Hotel guests can enjoy complimentary Wi-Fi and access to the fitness center during their stay.",
                "vi": "Khách lưu trú tại khách sạn được sử dụng Wi-Fi miễn phí và vào trung tâm thể hình trong suốt kỳ nghỉ."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm chính rơi vào âm thứ ba /ˈmen/, đọc là /ˌkɑːmplɪˈmentri/ lướt âm cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "defective",
        "lemma": "defective",
        "pos": ["adjective"],
        "ipa": {"us": "/dɪˈfektɪv/", "uk": "/dɪˈfektɪv/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["production-quality-control", "sales-customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "defective-1",
                "meaning_vi": "Bị lỗi kỹ thuật, hỏng hóc, có khiếm khuyết không sử dụng được",
                "note_vi": "Tính từ miêu tả sản phẩm không đạt tiêu chuẩn xuất xưởng hoặc bị khách trả về."
            }
        ],
        "confused_words": [
            {
                "word": "defect",
                "ipa": "/ˈdiːfekt/",
                "difference_vi": "Defect là danh từ (lỗi, khuyết tật); defective là tính từ (bị lỗi kỹ thuật)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Defective product = sản phẩm bị lỗi lắp ráp; defective reasoning = lập luận suy diễn sai lầm."
            }
        ],
        "collocations": [
            {"phrase": "defective merchandise", "meaning_vi": "hàng hóa bị lỗi", "evidence": "corpus"},
            {"phrase": "defective parts", "meaning_vi": "các bộ phận linh kiện bị hư hỏng", "evidence": "corpus"},
            {"phrase": "return defective items", "meaning_vi": "trả lại các món hàng lỗi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "faulty", "meaning_vi": "có lỗi"},
            {"word": "flawed", "meaning_vi": "bị khiếm khuyết"},
            {"word": "malfunctioning", "meaning_vi": "bị hỏng chức năng"}
        ],
        "examples": [
            {
                "en": "Any defective units discovered during final inspection were immediately set aside for repairs.",
                "vi": "Bất kỳ sản phẩm lỗi nào được phát hiện trong khâu kiểm định cuối cùng đều được cách ly ngay để sửa chữa."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈfek/, âm đuôi /tɪv/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "assembly",
        "lemma": "assembly",
        "pos": ["noun"],
        "ipa": {"us": "/əˈsembli/", "uk": "/əˈsembli/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["production-quality-control", "describe-picture"],
        "speaking_use": ["describe-picture", "respond-with-info"],
        "senses": [
            {
                "id": "assembly-1",
                "meaning_vi": "Sự lắp ráp linh kiện thành phẩm; dây chuyền sản xuất lắp ráp",
                "note_vi": "Hình ảnh rất quen thuộc trong tranh TOEIC Part 2 chụp nhà xưởng công nghiệp."
            },
            {
                "id": "assembly-2",
                "meaning_vi": "Đại hội đồng, cuộc họp toàn thể của một tổ chức",
                "note_vi": "Như trong General Assembly (Đại hội đồng Liên hợp quốc)."
            }
        ],
        "confused_words": [
            {
                "word": "assemble",
                "ipa": "/əˈsembl/",
                "difference_vi": "Assemble là động từ lắp ráp hoặc tập hợp; assembly là danh từ sự lắp ráp hoặc dây chuyền."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Assembly line là dây chuyền lắp ráp công nghiệp; assembly instructions là tờ hướng dẫn lắp ghép đồ nội thất."
            }
        ],
        "collocations": [
            {"phrase": "assembly line", "meaning_vi": "dây chuyền lắp ráp nhà máy", "evidence": "corpus"},
            {"phrase": "assembly instructions", "meaning_vi": "hướng dẫn lắp ráp đồ", "evidence": "corpus"},
            {"phrase": "automated assembly", "meaning_vi": "hệ thống lắp ráp tự động hóa", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "construction", "meaning_vi": "sự dựng thành hình"},
            {"word": "manufacturing line", "meaning_vi": "dây chuyền chế tạo"}
        ],
        "examples": [
            {
                "en": "Workers on the automotive assembly line wear protective goggles and noise-canceling headsets.",
                "vi": "Công nhân trên dây chuyền lắp ráp ô tô đeo kính bảo hộ và tai nghe chống ồn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈsem/, âm đuôi /li/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "malfunction",
        "lemma": "malfunction",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˌmælˈfʌŋkʃn/", "uk": "/ˌmælˈfʌŋkʃn/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["production-quality-control", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "malfunction-1",
                "meaning_vi": "Sự cố trục trặc kỹ thuật, máy móc hỏng hóc không hoạt động; (v) bị lỗi vận hành",
                "note_vi": "Tiền tố mal- (xấu/sai) kết hợp với function (chức năng)."
            }
        ],
        "confused_words": [
            {
                "word": "function",
                "ipa": "/ˈfʌŋkʃn/",
                "difference_vi": "Function là chức năng hoạt động bình thường; malfunction là sự trục trặc, lỗi vận hành."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Equipment malfunction = sự cố máy móc hỏng; software malfunction = lỗi phần mềm gián đoạn."
            }
        ],
        "collocations": [
            {"phrase": "equipment malfunction", "meaning_vi": "trục trặc thiết bị máy móc", "evidence": "corpus"},
            {"phrase": "mechanical malfunction", "meaning_vi": "sự cố cơ khí", "evidence": "corpus"},
            {"phrase": "malfunction suddenly", "meaning_vi": "đột ngột bị hỏng hóc", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "glitch", "meaning_vi": "sự cố nhỏ bất ngờ"},
            {"word": "breakdown", "meaning_vi": "sự đổ vỡ, hỏng máy móc"}
        ],
        "examples": [
            {
                "en": "Production was temporarily halted due to an unexpected equipment malfunction in the packaging unit.",
                "vi": "Việc sản xuất đã tạm thời bị ngừng lại do sự cố trục trặc thiết bị bất ngờ tại bộ phận đóng gói."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm thứ hai /ˈfʌŋk/, có âm ngắt /ŋk/ trước khi sang /ʃn/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "benchmark",
        "lemma": "benchmark",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈbentʃmɑːrk/", "uk": "/ˈbentʃmɑːk/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["production-quality-control", "management-operations"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "benchmark-1",
                "meaning_vi": "Tiêu chuẩn đối sánh, mốc chuẩn chất lượng để đo lường và so sánh",
                "note_vi": "Mức chuẩn mực tốt nhất trong ngành để các doanh nghiệp khác noi theo phấn đấu."
            }
        ],
        "confused_words": [
            {
                "word": "bench",
                "ipa": "/bentʃ/",
                "difference_vi": "Bench là chiếc ghế dài; benchmark là tiêu chuẩn đối chuẩn chất lượng."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Set a benchmark = đặt ra tiêu chuẩn chuẩn mực mới; benchmark against competitors = đối sánh năng lực với đối thủ cạnh tranh."
            }
        ],
        "collocations": [
            {"phrase": "industry benchmark", "meaning_vi": "chuẩn mực tiêu chuẩn của ngành", "evidence": "corpus"},
            {"phrase": "set a new benchmark", "meaning_vi": "thiết lập một mốc chuẩn mới", "evidence": "corpus"},
            {"phrase": "benchmark against", "meaning_vi": "so sánh đối chuẩn với đối thủ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "standard", "meaning_vi": "tiêu chuẩn"},
            {"word": "criterion", "meaning_vi": "tiêu chí đo lường"},
            {"word": "gauge", "meaning_vi": "thước đo"}
        ],
        "examples": [
            {
                "en": "The facility sets a high industry benchmark for energy efficiency and minimal carbon emissions.",
                "vi": "Cơ sở này đã thiết lập một chuẩn mực ngành rất cao về hiệu quả sử dụng năng lượng và giảm thiểu phát thải carbon."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈbentʃ/, âm thứ hai có âm /r/ uốn lưỡi rõ /ˈmɑːrk/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "output",
        "lemma": "output",
        "pos": ["noun"],
        "ipa": {"us": "/ˈaʊtpʊt/", "uk": "/ˈaʊtpʊt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["production-quality-control"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "output-1",
                "meaning_vi": "Sản lượng sản xuất, tổng số lượng thành phẩm tạo ra trong một kỳ",
                "note_vi": "Chỉ tiêu quan trọng đo lường hiệu năng của nhà xưởng hoặc đội nhóm sản xuất."
            }
        ],
        "confused_words": [
            {
                "word": "input",
                "ipa": "/ˈɪnpʊt/",
                "difference_vi": "Input là đầu vào (nguyên liệu, dữ liệu); output là sản lượng đầu ra."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Manufacturing output = sản lượng chế tạo nhà máy; output data = dữ liệu trích xuất đầu ra của máy tính."
            }
        ],
        "collocations": [
            {"phrase": "daily manufacturing output", "meaning_vi": "sản lượng chế tạo hàng ngày", "evidence": "corpus"},
            {"phrase": "increase total output", "meaning_vi": "tăng tổng sản lượng đầu ra", "evidence": "corpus"},
            {"phrase": "output per worker", "meaning_vi": "năng suất sản lượng trên mỗi công nhân", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "production", "meaning_vi": "sự sản xuất, sản lượng"},
            {"word": "yield", "meaning_vi": "sản lượng thu hoạch / sản xuất"}
        ],
        "examples": [
            {
                "en": "By installing automated robotic arms, the factory increased its weekly output by twenty percent.",
                "vi": "Bằng cách lắp đặt cánh tay robot tự động, nhà máy đã tăng sản lượng hàng tuần thêm 20%."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈaʊt/, âm thứ hai đọc gọn là /pʊt/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "plant",
        "lemma": "plant",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/plænt/", "uk": "/plɑːnt/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["production-quality-control", "describe-picture"],
        "speaking_use": ["describe-picture", "respond-with-info"],
        "senses": [
            {
                "id": "plant-1",
                "meaning_vi": "Nhà máy, xí nghiệp sản xuất công nghiệp nặng hoặc nhà máy điện",
                "note_vi": "Trong ngữ cảnh TOEIC kinh tế, plant thường có nghĩa là nhà xưởng, không phải cái cây."
            }
        ],
        "confused_words": [
            {
                "word": "planet",
                "ipa": "/ˈplænɪt/",
                "difference_vi": "Planet là hành tinh ngoài vũ trụ; plant là cây cối hoặc nhà máy sản xuất."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Manufacturing plant = nhà máy sản xuất; house plant = cây cảnh trồng trong nhà."
            }
        ],
        "collocations": [
            {"phrase": "manufacturing plant", "meaning_vi": "nhà máy sản xuất công nghiệp", "evidence": "corpus"},
            {"phrase": "power plant", "meaning_vi": "nhà máy phát điện", "evidence": "corpus"},
            {"phrase": "plant manager", "meaning_vi": "giám đốc điều hành nhà máy", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "factory", "meaning_vi": "nhà máy xí nghiệp"},
            {"word": "facility", "meaning_vi": "cơ sở sản xuất"},
            {"word": "mill", "meaning_vi": "xưởng xay xát / cán thép"}
        ],
        "examples": [
            {
                "en": "The pharmaceutical company is constructing a new manufacturing plant near the port.",
                "vi": "Công ty dược phẩm đang xây dựng một nhà máy sản xuất mới ở gần cảng biển."
            }
        ],
        "pronunciation_tips_vi": "Trong tiếng Mỹ phát âm là /plænt/ với nguyên âm /æ/ bẹt miệng; tiếng Anh là /plɑːnt/ âm /ɑː/ sâu.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "flaw",
        "lemma": "flaw",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/flɔː/", "uk": "/flɔː/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["production-quality-control"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "flaw-1",
                "meaning_vi": "Tì vết, vết nứt, lỗi khiếm khuyết trong thiết kế hoặc sản phẩm",
                "note_vi": "Điểm thiếu sót làm giảm giá trị hoặc độ bền của sản phẩm."
            }
        ],
        "confused_words": [
            {
                "word": "floor",
                "ipa": "/flɔːr/",
                "difference_vi": "Floor là sàn nhà hoặc tầng nhà (có âm /r/); flaw là lỗi khiếm khuyết (không có âm r)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Design flaw = lỗi trong khâu thiết kế bản vẽ; fatal flaw = khiếm khuyết chết người phá hủy toàn bộ hệ thống."
            }
        ],
        "collocations": [
            {"phrase": "design flaw", "meaning_vi": "lỗi trong thiết kế", "evidence": "corpus"},
            {"phrase": "minor flaw", "meaning_vi": "tì vết / khuyết điểm nhỏ", "evidence": "corpus"},
            {"phrase": "fatal flaw", "meaning_vi": "khiếm khuyết chí mạng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "defect", "meaning_vi": "khuyết tật, lỗi"},
            {"word": "fault", "meaning_vi": "thiếu sót, điểm yếu"},
            {"word": "imperfection", "meaning_vi": "điểm không hoàn hảo"}
        ],
        "examples": [
            {
                "en": "Engineers redesigned the cooling system after identifying a critical design flaw.",
                "vi": "Các kỹ sư đã thiết kế lại hệ thống làm mát sau khi xác định được một lỗi thiết kế nghiêm trọng."
            }
        ],
        "pronunciation_tips_vi": "Nguyên âm /ɔː/ tròn môi kéo dài, không bật âm /r/ ở đuôi.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "discard",
        "lemma": "discard",
        "pos": ["verb"],
        "ipa": {"us": "/dɪˈskɑːrd/", "uk": "/dɪˈskɑːd/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["production-quality-control", "management-operations"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "discard-1",
                "meaning_vi": "Vứt bỏ, loại bỏ các vật phẩm phế liệu hoặc tài liệu không còn dùng được",
                "note_vi": "Bỏ đi những thứ không còn giá trị sử dụng."
            }
        ],
        "confused_words": [
            {
                "word": "discount",
                "ipa": "/ˈdɪskaʊnt/",
                "difference_vi": "Discount là giảm giá; discard là vứt bỏ, thải loại đi."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Discard damaged materials = loại bỏ vật liệu hư hỏng; discard an idea = từ bỏ một ý tưởng."
            }
        ],
        "collocations": [
            {"phrase": "discard damaged goods", "meaning_vi": "vứt bỏ hàng hóa đã bị hư hại", "evidence": "corpus"},
            {"phrase": "properly discard", "meaning_vi": "thải bỏ đúng cách theo quy định", "evidence": "corpus"},
            {"phrase": "discard waste", "meaning_vi": "vứt bỏ rác thải sản xuất", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "throw away", "meaning_vi": "vứt đi"},
            {"word": "dispose of", "meaning_vi": "tiêu hủy, xử lý rác"},
            {"word": "get rid of", "meaning_vi": "loại trừ, dẹp bỏ"}
        ],
        "examples": [
            {
                "en": "Hazardous chemicals must be discarded in designated containment barrels according to safety laws.",
                "vi": "Hóa chất nguy hại phải được thải bỏ vào các thùng chứa chuyên dụng theo đúng luật an toàn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈskɑːrd/, âm /r/ uốn lưỡi rõ trong giọng Mỹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "recall",
        "lemma": "recall",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/rɪˈkɔːl/", "uk": "/rɪˈkɔːl/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["production-quality-control", "sales-customer-service"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "recall-1",
                "meaning_vi": "Thu hồi sản phẩm bị lỗi trên thị trường; (v) triệu hồi sản phẩm về nhà máy",
                "note_vi": "Khi là danh từ thu hồi sản phẩm, trọng âm thường chuyển lên âm đầu /ˈriːkɔːl/."
            },
            {
                "id": "recall-2",
                "meaning_vi": "Nhớ lại một sự việc trong quá khứ",
                "note_vi": "Đồng nghĩa với remember."
            }
        ],
        "confused_words": [
            {
                "word": "call back",
                "ipa": "/kɔːl bæk/",
                "difference_vi": "Call back là gọi điện lại; recall là chiến dịch thu hồi toàn bộ sản phẩm lỗi hoặc hồi tưởng ký ức."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Product recall = chiến dịch thu hồi sản phẩm; as far as I recall = theo như tôi nhớ lại."
            }
        ],
        "collocations": [
            {"phrase": "product recall", "meaning_vi": "chiến dịch thu hồi sản phẩm lỗi", "evidence": "corpus"},
            {"phrase": "issue a recall", "meaning_vi": "phát lệnh triệu hồi sản phẩm", "evidence": "corpus"},
            {"phrase": "voluntary recall", "meaning_vi": "sự chủ động tự nguyện thu hồi sản phẩm", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "withdraw", "meaning_vi": "rút lại, thu hồi khỏi thị trường"},
            {"word": "remember", "meaning_vi": "nhớ lại"}
        ],
        "examples": [
            {
                "en": "The automaker issued a voluntary recall of 50,000 sedans to fix a faulty airbag sensor.",
                "vi": "Hãng sản xuất ô tô đã phát lệnh tự nguyện thu hồi 50.000 chiếc xe sedan để sửa cảm biến túi khí bị lỗi."
            }
        ],
        "pronunciation_tips_vi": "Động từ nhấn âm 2 /rɪˈkɔːl/, danh từ thường nhấn âm 1 /ˈriːkɔːl/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "consignment",
        "lemma": "consignment",
        "pos": ["noun"],
        "ipa": {"us": "/kənˈsaɪnmənt/", "uk": "/kənˈsaɪnmənt/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["shipping-logistics", "sales-customer-service"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "consignment-1",
                "meaning_vi": "Lô hàng hóa ký gửi vận chuyển hoặc gửi bán hộ",
                "note_vi": "Hình thức giao hàng cho đại lý bán hộ và thanh toán sau khi bán được hàng."
            }
        ],
        "confused_words": [
            {
                "word": "assignment",
                "ipa": "/əˈsaɪnmənt/",
                "difference_vi": "Assignment là nhiệm vụ hoặc bài tập được giao; consignment là lô hàng gửi đi hoặc hàng ký gửi."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "On consignment = phương thức ký gửi (chưa phải trả tiền ngay cho đến khi bán xong)."
            }
        ],
        "collocations": [
            {"phrase": "on consignment", "meaning_vi": "theo hình thức ký gửi", "evidence": "corpus"},
            {"phrase": "consignment of goods", "meaning_vi": "lô hàng hóa vận chuyển", "evidence": "corpus"},
            {"phrase": "receive a consignment", "meaning_vi": "nhận một lô hàng ký gửi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "shipment", "meaning_vi": "chuyến hàng"},
            {"word": "batch", "meaning_vi": "lô hàng"},
            {"word": "cargo", "meaning_vi": "hàng hóa chuyên chở"}
        ],
        "examples": [
            {
                "en": "The boutique agreed to display local artisan jewelry on consignment with a 20% commission.",
                "vi": "Cửa hàng thời trang đã đồng ý trưng bày trang sức thủ công địa phương theo hình thức ký gửi với mức hoa hồng 20%."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈsaɪn/, nhị trùng âm /aɪ/ ngân dài, chữ 'g' câm.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "dispatch",
        "lemma": "dispatch",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/dɪˈspætʃ/", "uk": "/dɪˈspætʃ/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "dispatch-1",
                "meaning_vi": "Gửi đi, phái đi, điều động đơn hàng xuất kho hoặc phương tiện cứu hộ",
                "note_vi": "Hành động cho xuất xưởng và chuyển giao hàng hóa cho bưu cục vận tải."
            }
        ],
        "confused_words": [
            {
                "word": "patch",
                "ipa": "/pætʃ/",
                "difference_vi": "Patch là miếng vá bản vá; dispatch là xuất gửi đi."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Dispatch orders = xuất gửi các đơn hàng; dispatch an ambulance = điều xe cứu thương khẩn cấp."
            }
        ],
        "collocations": [
            {"phrase": "dispatch orders", "meaning_vi": "gửi các đơn hàng đi", "evidence": "corpus"},
            {"phrase": "prompt dispatch", "meaning_vi": "sự gửi hàng nhanh chóng tức thì", "evidence": "corpus"},
            {"phrase": "ready for dispatch", "meaning_vi": "đã sẵn sàng để xuất xưởng gửi đi", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "ship", "meaning_vi": "giao hàng"},
            {"word": "send off", "meaning_vi": "phái gửi đi"},
            {"word": "forward", "meaning_vi": "chuyển tiếp"}
        ],
        "examples": [
            {
                "en": "All orders placed before 2:00 PM are dispatched from our fulfillment center on the same business day.",
                "vi": "Tất cả các đơn đặt trước 2:00 chiều đều được xuất kho gửi đi từ trung tâm xử lý đơn trong cùng ngày làm việc."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /ˈspætʃ/, nguyên âm /æ/ bẹt miệng, âm đuôi /tʃ/ bật rõ ràng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "freight",
        "lemma": "freight",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/freɪt/", "uk": "/freɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "describe-picture"],
        "senses": [
            {
                "id": "freight-1",
                "meaning_vi": "Hàng hóa vận chuyển bằng tàu thủy, tàu hỏa hoặc máy bay; cước phí vận chuyển hàng",
                "note_vi": "Thường dùng cho việc vận tải hàng hóa số lượng lớn trên quy mô thương mại quốc tế."
            }
        ],
        "confused_words": [
            {
                "word": "flight",
                "ipa": "/flaɪt/",
                "difference_vi": "Flight là chuyến bay chở người hoặc hàng (/l/); freight là hàng hóa chuyên chở thương mại (/r/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Air freight = vận tải hàng không; freight charges = cước phí chuyên chở."
            }
        ],
        "collocations": [
            {"phrase": "air freight", "meaning_vi": "vận chuyển hàng hóa bằng đường hàng không", "evidence": "corpus"},
            {"phrase": "freight charges", "meaning_vi": "cước phí vận tải hàng hóa", "evidence": "corpus"},
            {"phrase": "freight forwarder", "meaning_vi": "đại lý giao nhận hàng hóa quốc tế", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "cargo", "meaning_vi": "hàng hóa chuyên chở"},
            {"word": "consignment", "meaning_vi": "lô hàng vận chuyển"}
        ],
        "examples": [
            {
                "en": "Due to rising fuel costs, ocean freight rates have increased by fifteen percent over the last quarter.",
                "vi": "Do chi phí nhiên liệu tăng cao, giá cước vận tải đường biển đã tăng mười lăm phần trăm trong quý vừa qua."
            }
        ],
        "pronunciation_tips_vi": "Chữ 'gh' câm hoàn toàn, phát âm là /freɪt/ với nhị trùng âm /eɪ/ và âm cuối /t/ đanh gọn.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "carrier",
        "lemma": "carrier",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkæriər/", "uk": "/ˈkæriə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "carrier-1",
                "meaning_vi": "Hãng vận chuyển, công ty vận tải chuyên chở hàng hóa hoặc hành khách",
                "note_vi": "Bao gồm các hãng hàng không (air carrier), đội xe tải hoặc hãng tàu biển."
            }
        ],
        "confused_words": [
            {
                "word": "courier",
                "ipa": "/ˈkʊriər/",
                "difference_vi": "Courier là nhân viên chuyển phát nhanh thư từ/bưu phẩm nhỏ; carrier là doanh nghiệp/hãng chuyên chở hàng quy mô lớn."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Common carrier = hãng vận tải công cộng theo biểu giá công khai; mail carrier = nhân viên bưu tá giao thư."
            }
        ],
        "collocations": [
            {"phrase": "shipping carrier", "meaning_vi": "hãng vận tải giao nhận hàng", "evidence": "corpus"},
            {"phrase": "common carrier", "meaning_vi": "đơn vị vận tải công cộng", "evidence": "corpus"},
            {"phrase": "reliable carrier", "meaning_vi": "đơn vị vận chuyển đáng tin cậy", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "transporter", "meaning_vi": "nhà vận tải"},
            {"word": "shipper", "meaning_vi": "chủ hãng tàu/giao hàng"}
        ],
        "examples": [
            {
                "en": "We partner with several reputable shipping carriers to guarantee swift international delivery.",
                "vi": "Chúng tôi hợp tác với nhiều hãng vận chuyển uy tín để đảm bảo việc giao hàng quốc tế nhanh chóng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈkæ/, nguyên âm /æ/ bẹt miệng mở rộng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "cargo",
        "lemma": "cargo",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkɑːrɡoʊ/", "uk": "/ˈkɑːɡəʊ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics", "describe-picture"],
        "speaking_use": ["describe-picture", "respond-with-info"],
        "senses": [
            {
                "id": "cargo-1",
                "meaning_vi": "Hàng hóa chuyên chở trên tàu thủy, máy bay hoặc xe tải lớn",
                "note_vi": "Thường thấy trong ảnh Part 2 chụp container tại bến cảng (cargo container, cargo ship)."
            }
        ],
        "confused_words": [
            {
                "word": "freight",
                "ipa": "/freɪt/",
                "difference_vi": "Cargo và freight đồng nghĩa, tuy nhiên cargo thường chỉ các kiện hàng vật lý trên tàu/máy bay, freight bao gồm cả dịch vụ và cước phí."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Cargo ship = tàu chở hàng; cargo hold = khoang chứa hàng của máy bay hoặc tàu thủy."
            }
        ],
        "collocations": [
            {"phrase": "cargo ship", "meaning_vi": "tàu chở hàng hóa", "evidence": "corpus"},
            {"phrase": "load cargo", "meaning_vi": "bốc dỡ / xếp hàng hóa lên phương tiện", "evidence": "corpus"},
            {"phrase": "cargo container", "meaning_vi": "thùng công-ten-nơ chứa hàng", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "freight", "meaning_vi": "hàng hóa chuyên chở"},
            {"word": "load", "meaning_vi": "tải trọng hàng"}
        ],
        "examples": [
            {
                "en": "Dock workers used giant cranes to unload heavy cargo containers from the vessel.",
                "vi": "Công nhân cảng đã dùng cần cẩu khổng lồ để dỡ các thùng container chở hàng nặng từ con tàu."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈkɑːr/, uốn lưỡi âm /r/, âm thứ hai là /ɡoʊ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "courier",
        "lemma": "courier",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkʊriər/", "uk": "/ˈkʊriə/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "courier-1",
                "meaning_vi": "Nhân viên chuyển phát nhanh, công ty dịch vụ chuyển phát thư từ và bưu kiện",
                "note_vi": "Dịch vụ giao tận tay người nhận với tốc độ nhanh và tính xác thực cao."
            }
        ],
        "confused_words": [
            {
                "word": "carrier",
                "ipa": "/ˈkæriər/",
                "difference_vi": "Courier là chuyển phát nhanh bưu kiện tận tay; carrier là hãng vận chuyển lớn (đường biển, hàng không)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Send by courier = gửi bằng dịch vụ chuyển phát nhanh; motorcycle courier = nhân viên giao hàng bằng xe máy."
            }
        ],
        "collocations": [
            {"phrase": "express courier", "meaning_vi": "dịch vụ chuyển phát hỏa tốc", "evidence": "corpus"},
            {"phrase": "send via courier", "meaning_vi": "gửi qua đường chuyển phát nhanh", "evidence": "corpus"},
            {"phrase": "courier service", "meaning_vi": "dịch vụ chuyển phát bưu kiện", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "messenger", "meaning_vi": "người đưa tin"},
            {"word": "delivery person", "meaning_vi": "nhân viên giao hàng"}
        ],
        "examples": [
            {
                "en": "The legal contract was delivered by an express courier and signed by the recipient upon arrival.",
                "vi": "Hợp đồng pháp lý đã được chuyển phát bởi dịch vụ hỏa tốc và được người nhận ký tên ngay khi tới nơi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm đầu /ˈkʊr/, nguyên âm ngắn /ʊ/ như trong từ 'foot'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "tracking",
        "lemma": "tracking",
        "pos": ["noun"],
        "ipa": {"us": "/ˈtrækɪŋ/", "uk": "/ˈtrækɪŋ/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics", "sales-customer-service"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "tracking-1",
                "meaning_vi": "Việc theo dõi định vị hành trình của đơn hàng hoặc kiện hàng trực tuyến",
                "note_vi": "Mã tracking number cho phép khách hàng tra cứu vị trí món đồ theo thời gian thực."
            }
        ],
        "confused_words": [
            {
                "word": "track",
                "ipa": "/træk/",
                "difference_vi": "Track là đường ray xe lửa hoặc dấu vết; tracking là việc định vị theo dõi lộ trình."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Tracking number = mã vận đơn tra cứu; eye tracking = công nghệ theo dõi cử động mắt."
            }
        ],
        "collocations": [
            {"phrase": "tracking number", "meaning_vi": "mã số vận đơn theo dõi kiện hàng", "evidence": "corpus"},
            {"phrase": "track a shipment", "meaning_vi": "theo dõi đường đi của chuyến hàng", "evidence": "corpus"},
            {"phrase": "real-time tracking", "meaning_vi": "theo dõi định vị theo thời gian thực", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "monitoring", "meaning_vi": "sự theo dõi giám sát"},
            {"word": "tracing", "meaning_vi": "truy tìm dấu vết"}
        ],
        "examples": [
            {
                "en": "Please enter your ten-digit tracking number on our website to see the current location of your package.",
                "vi": "Vui lòng nhập mã vận đơn mười chữ số của bạn trên trang web của chúng tôi để xem vị trí hiện tại của kiện hàng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈtræk/, nguyên âm /æ/ bẹt miệng mở rộng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "transit",
        "lemma": "transit",
        "pos": ["noun"],
        "ipa": {"us": "/ˈtrænzɪt/", "uk": "/ˈtrænzɪt/"},
        "level": {"band": "target", "cefr": "B2", "basis": "TOEIC 700"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "transit-1",
                "meaning_vi": "Quá trình vận chuyển trên đường; việc quá cảnh qua một địa điểm trung gian",
                "note_vi": "Cụm 'in transit' rất phổ biến, có nghĩa là đang trên đường vận chuyển."
            }
        ],
        "confused_words": [
            {
                "word": "transition",
                "ipa": "/trænˈzɪʃn/",
                "difference_vi": "Transition là sự biến đổi giai đoạn; transit là việc chuyên chở hoặc quá cảnh."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "In transit = đang trên đường giao hàng; public transit = hệ thống giao thông công cộng."
            }
        ],
        "collocations": [
            {"phrase": "in transit", "meaning_vi": "đang trong quá trình vận chuyển trên đường", "evidence": "corpus"},
            {"phrase": "transit time", "meaning_vi": "thời gian vận chuyển hàng", "evidence": "corpus"},
            {"phrase": "damaged in transit", "meaning_vi": "bị hư hại trong lúc vận chuyển", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "transportation", "meaning_vi": "việc chuyên chở"},
            {"word": "passage", "meaning_vi": "sự đi qua"}
        ],
        "examples": [
            {
                "en": "Estimated transit time for standard overland shipping is three to five business days.",
                "vi": "Thời gian vận chuyển ước tính cho dịch vụ giao hàng đường bộ tiêu chuẩn là từ ba đến năm ngày làm việc."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈtræn/, âm giữa phát âm là /z/ hoặc /s/ rung nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "tariff",
        "lemma": "tariff",
        "pos": ["noun"],
        "ipa": {"us": "/ˈtærɪf/", "uk": "/ˈtærɪf/"},
        "level": {"band": "advanced", "cefr": "C1", "basis": "TOEIC 750+"},
        "topics": ["shipping-logistics", "finance-accounting"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "tariff-1",
                "meaning_vi": "Thuế quan đánh vào hàng hóa xuất nhập khẩu; biểu giá cước phí",
                "note_vi": "Chính sách thuế quan giữa các quốc gia ảnh hưởng trực tiếp đến chi phí giao thương quốc tế."
            }
        ],
        "confused_words": [
            {
                "word": "traffic",
                "ipa": "/ˈtræfɪk/",
                "difference_vi": "Traffic là giao thông đường xá (/tr/); tariff là biểu thuế quan xuất nhập khẩu (/t/)."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Impose tariffs = áp đặt mức thuế quan; customs tariff = biểu thuế hải quan."
            }
        ],
        "collocations": [
            {"phrase": "impose tariffs", "meaning_vi": "áp đặt mức thuế quan lên hàng nhập khẩu", "evidence": "corpus"},
            {"phrase": "protective tariff", "meaning_vi": "thuế quan bảo hộ hàng nội địa", "evidence": "corpus"},
            {"phrase": "tariff barriers", "meaning_vi": "các rào cản thuế quan thương mại", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "duty", "meaning_vi": "thuế xuất nhập khẩu"},
            {"word": "customs tax", "meaning_vi": "thuế hải quan"}
        ],
        "examples": [
            {
                "en": "The government decided to lower tariffs on imported raw materials to support local manufacturers.",
                "vi": "Chính phủ đã quyết định hạ thuế quan đối với nguyên liệu thô nhập khẩu để hỗ trợ các nhà sản xuất trong nước."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈtær/, nguyên âm /æ/ bẹt miệng, âm đuôi /ɪf/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "customs",
        "lemma": "customs",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkʌstəmz/", "uk": "/ˈkʌstəmz/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics", "hospitality-travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "customs-1",
                "meaning_vi": "Cơ quan hải quan; thủ tục kiểm tra hàng hóa xuất nhập cảnh tại sân bay hoặc cửa khẩu",
                "note_vi": "Luôn có đuôi -s khi chỉ cơ quan hải quan hoặc thủ tục thông quan."
            }
        ],
        "confused_words": [
            {
                "word": "custom",
                "ipa": "/ˈkʌstəm/",
                "difference_vi": "Custom (không có -s) là phong tục tập quán; customs (có -s) là cơ quan hải quan hoặc hàng rào thông quan."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Clear customs = hoàn tất thủ tục thông quan; customs officer = viên chức hải quan."
            }
        ],
        "collocations": [
            {"phrase": "clear customs", "meaning_vi": "thông quan hải quan thành công", "evidence": "corpus"},
            {"phrase": "customs declaration", "meaning_vi": "tờ khai báo hải quan", "evidence": "corpus"},
            {"phrase": "customs inspection", "meaning_vi": "sự kiểm tra hàng hóa của hải quan", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "border control", "meaning_vi": "kiểm soát biên giới"},
            {"word": "port authority", "meaning_vi": "cơ quan quản lý cảng"}
        ],
        "examples": [
            {
                "en": "All overseas shipments must clear customs before they can be released for domestic transport.",
                "vi": "Tất cả các lô hàng gửi từ nước ngoài đều phải thông quan hải quan trước khi được giải phóng để vận chuyển nội địa."
            }
        ],
        "pronunciation_tips_vi": "Âm đầu là /ˈkʌs/, âm cuối kết thúc bằng âm rung /z/, đừng bỏ quên âm /s/ và /z/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["glory-editorial"],
            "checked_at": "2026-10-10",
            "sources": ["vocabulary.md", "synonyms.md", "Oxford Learner's Dictionary"]
        }
    },
    {
        "id": "fragile",
        "lemma": "fragile",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈfrædʒl/", "uk": "/ˈfrædʒaɪl/"},
        "level": {"band": "core", "cefr": "B1", "basis": "TOEIC 650"},
        "topics": ["shipping-logistics"],
        "speaking_use": ["respond-with-info", "describe-picture"],
        "senses": [
            {
                "id": "fragile-1",
                "meaning_vi": "Dễ vỡ, dễ hư hại (thủy tinh, gốm sứ); cần xử lý cẩn thận khi vận chuyển",
                "note_vi": "Nhãn 'FRAGILE' dán nổi bật trên thùng các-tông trong kho bãi hoặc hình ảnh Part 2."
            }
        ],
        "confused_words": [
            {
                "word": "fragment",
                "ipa": "/ˈfræɡmənt/",
                "difference_vi": "Fragment là mảnh vỡ; fragile là tính từ miêu tả tính chất dễ vỡ nát."
            }
        ],
        "confusing_meanings": [
            {
                "difference_vi": "Fragile items = đồ đạc dễ vỡ; fragile economy = nền kinh tế mong manh dễ tổn thương."
            }
        ],
        "collocations": [
            {"phrase": "handle fragile items", "meaning_vi": "xử lý cẩn thận đồ dễ vỡ", "evidence": "corpus"},
            {"phrase": "fragile sticker", "meaning_vi": "nhãn dán cảnh báo hàng dễ vỡ", "evidence": "corpus"},
            {"phrase": "fragile glassware", "meaning_vi": "đồ thủy tinh dễ vỡ", "evidence": "corpus"}
        ],
        "synonyms": [
            {"word": "delicate", "meaning_vi": "mỏng manh, tinh xảo"},
            {"word": "breakable", "meaning_vi": "dễ vỡ"}
        ],
        "examples": [
            {
                "en": "Boxes containing ceramic tableware should be marked 'FRAGILE' and handled with extreme care.",
                "vi": "Những thùng chứa bộ đồ ăn bằng gốm sứ phải được đánh dấu 'DỄ VỠ' và được bốc xếp hết sức cẩn thận."
            }
        ],
        "pronunciation_tips_vi": "Tiếng Mỹ đọc là /ˈfrædʒl/ (âm tiết thứ hai phát âm /dʒl/ ngắn gọn); tiếng Anh đọc là /ˈfrædʒaɪl/.",
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
    for w in words_group3:
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
    print(f"\n[OK] Group 3 created {count} words successfully.")

if __name__ == "__main__":
    main()
