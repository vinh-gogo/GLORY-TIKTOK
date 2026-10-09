import os
import yaml

LEXICON_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "lexicon")

words_data = [
    {
        "schema_version": 2,
        "id": "acknowledge",
        "lemma": "acknowledge",
        "pos": ["verb"],
        "ipa": {"us": "/əkˈnɑːlɪdʒ/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["email", "customer-service", "business"],
        "speaking_use": ["read-aloud", "respond-to-questions"],
        "senses": [
            {
                "id": "acknowledge-1",
                "meaning_vi": "Xác nhận đã nhận được (thư từ, thanh toán, đơn hàng) / Thừa nhận",
                "note_vi": "Cực kỳ phổ biến trong giao tiếp email công sở và dịch vụ khách hàng."
            }
        ],
        "collocations": [
            {"phrase": "acknowledge receipt of", "meaning_vi": "xác nhận đã nhận được (hàng/thư)", "evidence": "corpus"},
            {"phrase": "promptly acknowledge", "meaning_vi": "nhanh chóng gửi xác nhận", "evidence": "corpus"},
            {"phrase": "acknowledge the contribution", "meaning_vi": "ghi nhận sự đóng góp", "evidence": "corpus"},
            {"phrase": "formally acknowledge", "meaning_vi": "chính thức xác nhận", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "knowledge",
                "ipa": "/ˈnɑːlɪdʒ/",
                "meaning": "kiến thức, sự hiểu biết",
                "kind": "spelling-sound",
                "difference_vi": "Acknowledge là động từ xác nhận đã nhận; knowledge là danh từ chỉ kiến thức."
            }
        ],
        "confusing_meanings": [
            {
                "word": "confirm",
                "meaning": "xác nhận tính chính xác",
                "difference_vi": "Confirm là xác nhận tính chuẩn xác của lịch hẹn; acknowledge là thông báo cho đối phương biết mình đã nhận được tài liệu/hàng hóa."
            }
        ],
        "synonyms": [
            {"word": "recognize", "meaning_vi": "công nhận"},
            {"word": "admit", "meaning_vi": "thừa nhận"}
        ],
        "examples": [
            {
                "en": "We would like to acknowledge receipt of your application for the marketing manager position.",
                "vi": "Chúng tôi xin xác nhận đã nhận được hồ sơ ứng tuyển của bạn cho vị trí trưởng phòng tiếp thị."
            }
        ],
        "pronunciation_tips_vi": "Chữ cái 'k' là ÂM CÂM! Trọng âm rơi vào âm tiết thứ hai /-ˈnɑː-/. Âm cuối là /dʒ/ bật dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "adjourn",
        "lemma": "adjourn",
        "pos": ["verb"],
        "ipa": {"us": "/əˈdʒɜːrn/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["meetings", "legal", "business"],
        "speaking_use": ["read-aloud", "respond-with-info"],
        "senses": [
            {
                "id": "adjourn-1",
                "meaning_vi": "Tạm hoãn, bế mạc cuộc họp (để nghỉ hoặc chuyển sang buổi khác)",
                "note_vi": "Thuật ngữ trang trọng trong các cuộc họp hội đồng quản trị hoặc hội nghị."
            }
        ],
        "collocations": [
            {"phrase": "adjourn the meeting", "meaning_vi": "bế mạc / tạm hoãn cuộc họp", "evidence": "corpus"},
            {"phrase": "motion to adjourn", "meaning_vi": "đề xuất kết thúc phiên họp", "evidence": "corpus"},
            {"phrase": "adjourn until tomorrow", "meaning_vi": "hoãn phiên họp cho đến ngày mai", "evidence": "corpus"},
            {"phrase": "the session was adjourned", "meaning_vi": "phiên họp đã được tuyên bố bế mạc", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "adjust",
                "ipa": "/əˈdʒʌst/",
                "meaning": "điều chỉnh, sửa lại cho vừa",
                "kind": "spelling-sound",
                "difference_vi": "Adjourn là tạm dừng bế mạc cuộc họp; adjust mang nghĩa điều chỉnh đồ vật hoặc thích nghi."
            }
        ],
        "confusing_meanings": [
            {
                "word": "postpone",
                "meaning": "dời lịch trước khi diễn ra",
                "difference_vi": "Postpone là dời cuộc họp sang một ngày khác trước khi nó bắt đầu; adjourn là tạm dừng hoặc bế mạc cuộc họp đang diễn ra."
            }
        ],
        "synonyms": [
            {"word": "suspend", "meaning_vi": "tạm đình chỉ"},
            {"word": "recess", "meaning_vi": "tạm nghỉ phiên họp"}
        ],
        "examples": [
            {
                "en": "The chairperson decided to adjourn the board meeting until two o'clock this afternoon.",
                "vi": "Chủ tọa đã quyết định tạm hoãn cuộc họp hội đồng quản trị cho đến hai giờ chiều nay."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈdʒɜːrn/. Chú ý âm /ɜːr/ cong lưỡi chuẩn giọng Mỹ, âm /n/ ngân nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "allocate",
        "lemma": "allocate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈæləkeɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["budget", "management", "business"],
        "speaking_use": ["respond-with-info", "respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "allocate-1",
                "meaning_vi": "Phân bổ, chỉ định (ngân sách, nguồn vốn, nhân sự cho mục đích cụ thể)",
                "note_vi": "Từ chìa khóa trong quản lý tài chính và phân bổ tài nguyên dự án."
            }
        ],
        "collocations": [
            {"phrase": "allocate funds", "meaning_vi": "phân bổ các nguồn vốn", "evidence": "corpus"},
            {"phrase": "allocate resources", "meaning_vi": "phân bổ tài nguyên", "evidence": "corpus"},
            {"phrase": "allocate a budget", "meaning_vi": "phân bổ hạn mức ngân sách", "evidence": "corpus"},
            {"phrase": "allocate evenly", "meaning_vi": "phân chia đồng đều", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "locate",
                "ipa": "/ˈloʊkeɪt/",
                "meaning": "xác định vị trí",
                "kind": "spelling-sound",
                "difference_vi": "Allocate là phân bổ nguồn lực; locate là tìm ra vị trí của ai hoặc cái gì."
            }
        ],
        "confusing_meanings": [
            {
                "word": "distribute",
                "meaning": "phân phát rộng rãi",
                "difference_vi": "Distribute là chia phát hàng hóa đến nhiều địa điểm; allocate là quyết định dành riêng một khoản tiền/tài nguyên cho mục đích chuyên biệt."
            }
        ],
        "synonyms": [
            {"word": "designate", "meaning_vi": "chỉ định"},
            {"word": "assign", "meaning_vi": "phân công"}
        ],
        "examples": [
            {
                "en": "The company voted to allocate two million dollars to upgrade its digital infrastructure.",
                "vi": "Công ty đã bỏ phiếu quyết định phân bổ hai triệu đô la để nâng cấp cơ sở hạ tầng kỹ thuật số."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈæ-/. Đuôi kết thúc bằng /-keɪt/, bật nhẹ âm /t/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "benefit",
        "lemma": "benefit",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈbenɪfɪt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["benefits", "work", "hiring"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "benefit-1",
                "meaning_vi": "Lợi ích, chế độ phúc lợi nhân viên / Hưởng lợi từ",
                "note_vi": "Thường gặp khi nói về bảo hiểm y tế, ngày nghỉ phép có lương, chế độ hưu trí."
            }
        ],
        "collocations": [
            {"phrase": "employee benefits", "meaning_vi": "chế độ phúc lợi cho nhân viên", "evidence": "corpus"},
            {"phrase": "health insurance benefits", "meaning_vi": "quyền lợi bảo hiểm y tế", "evidence": "corpus"},
            {"phrase": "benefit from", "meaning_vi": "hưởng lợi từ điều gì", "evidence": "corpus"},
            {"phrase": "fringe benefits", "meaning_vi": "phúc lợi bổ sung ngoài lương", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "beneficial",
                "ipa": "/ˌbenɪˈfɪʃl/",
                "meaning": "có lợi, mang lại tiện ích",
                "kind": "spelling-sound",
                "difference_vi": "Benefit là danh từ (phúc lợi) hoặc động từ (hưởng lợi); beneficial là tính từ mang nghĩa có lợi."
            }
        ],
        "confusing_meanings": [
            {
                "word": "advantage",
                "meaning": "ưu thế vượt trội",
                "difference_vi": "Advantage là điểm mạnh hơn đối thủ; benefit là chế độ quyền lợi tốt đẹp mà người lao động nhận được."
            }
        ],
        "synonyms": [
            {"word": "perk", "meaning_vi": "quyền lợi đãi ngộ thêm"},
            {"word": "advantage", "meaning_vi": "lợi thế"}
        ],
        "examples": [
            {
                "en": "In addition to a competitive salary, the company provides comprehensive employee health benefits.",
                "vi": "Ngoài mức lương cạnh tranh, công ty còn cung cấp các chế độ phúc lợi sức khỏe toàn diện cho nhân viên."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈben-/. Âm cuối /-fɪt/ bật rõ âm /t/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "cancel",
        "lemma": "cancel",
        "pos": ["verb"],
        "ipa": {"us": "/ˈkænsl/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["travel", "meetings", "shopping"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "cancel-1",
                "meaning_vi": "Hủy bỏ (cuộc hẹn, chuyến bay, đơn đặt hàng)",
                "note_vi": "Xuất hiện khắp các đề thi khi có sự cố lịch trình hoặc hủy bỏ đơn mua hàng."
            }
        ],
        "collocations": [
            {"phrase": "cancel a reservation", "meaning_vi": "hủy chỗ đã đặt trước", "evidence": "corpus"},
            {"phrase": "cancel an order", "meaning_vi": "hủy một đơn hàng", "evidence": "corpus"},
            {"phrase": "cancel due to weather", "meaning_vi": "hủy lịch do điều kiện thời tiết", "evidence": "corpus"},
            {"phrase": "free cancellation", "meaning_vi": "hủy đặt chỗ miễn phí", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "conceal",
                "ipa": "/kənˈsiːl/",
                "meaning": "che giấu, giấu giếm",
                "kind": "spelling-sound",
                "difference_vi": "Cancel là hủy bỏ kế hoạch; conceal mang nghĩa giấu giếm điều gì đó."
            }
        ],
        "confusing_meanings": [
            {
                "word": "postpone",
                "meaning": "tạm hoãn dời ngày",
                "difference_vi": "Postpone là dời cuộc hẹn sang ngày khác; cancel là hủy bỏ hoàn toàn sự kiện."
            }
        ],
        "synonyms": [
            {"word": "call off", "meaning_vi": "bãi bỏ"},
            {"word": "abort", "meaning_vi": "hủy ngang"}
        ],
        "examples": [
            {
                "en": "The airline had to cancel all afternoon departures because of dense fog covering the runway.",
                "vi": "Hãng hàng không đã phải hủy tất cả các chuyến bay khởi hành vào buổi chiều vì sương mù dày đặc bao phủ đường băng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈkæn-/. Âm đuôi /-sl/ đọc liền mượt mà, không thêm 'ờ'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "capacity",
        "lemma": "capacity",
        "pos": ["noun"],
        "ipa": {"us": "/kəˈpæsəti/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["manufacturing", "hotels", "events"],
        "speaking_use": ["describe-picture", "respond-with-info"],
        "senses": [
            {
                "id": "capacity-1",
                "meaning_vi": "Công suất hoạt động / Sức chứa (người, hàng hóa)",
                "note_vi": "Hay gặp khi mô tả phòng hội nghị chứa bao nhiêu người hoặc nhà máy chạy hết công suất."
            }
        ],
        "collocations": [
            {"phrase": "seating capacity", "meaning_vi": "sức chứa chỗ ngồi", "evidence": "corpus"},
            {"phrase": "operate at full capacity", "meaning_vi": "vận hành hết công suất tối đa", "evidence": "corpus"},
            {"phrase": "storage capacity", "meaning_vi": "dung tích kho chứa", "evidence": "corpus"},
            {"phrase": "expand capacity", "meaning_vi": "mở rộng công suất sản xuất", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "capability",
                "ipa": "/ˌkeɪpəˈbɪləti/",
                "meaning": "năng lực, khả năng làm việc",
                "kind": "spelling-sound",
                "difference_vi": "Capacity là sức chứa hoặc công suất máy móc; capability là năng lực hoặc trình độ làm việc của con người."
            }
        ],
        "confusing_meanings": [
            {
                "word": "volume",
                "meaning": "thể tích vật lý",
                "difference_vi": "Volume là thể tích đo lường không gian; capacity là ngưỡng giới hạn tối đa có thể tiếp nhận được."
            }
        ],
        "synonyms": [
            {"word": "volume", "meaning_vi": "dung tích"},
            {"word": "maximum output", "meaning_vi": "sản lượng tối đa"}
        ],
        "examples": [
            {
                "en": "The newly renovated auditorium has a maximum seating capacity of eight hundred people.",
                "vi": "Khán phòng mới được cải tạo có sức chứa chỗ ngồi tối đa là tám trăm người."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈpæs-/. Âm đầu là schwa /kə-/, đuôi /-ti/ đọc dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "collaborate",
        "lemma": "collaborate",
        "pos": ["verb"],
        "ipa": {"us": "/kəˈlæbəreɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["work", "management"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "collaborate-1",
                "meaning_vi": "Hợp tác, cộng tác cùng làm việc trong một dự án",
                "note_vi": "Chủ đề làm việc nhóm (teamwork) trong Part 3 và Part 5."
            }
        ],
        "collocations": [
            {"phrase": "collaborate with colleagues", "meaning_vi": "cộng tác với các đồng nghiệp", "evidence": "corpus"},
            {"phrase": "collaborate on a project", "meaning_vi": "hợp tác thực hiện một dự án", "evidence": "corpus"},
            {"phrase": "closely collaborate", "meaning_vi": "hợp tác chặt chẽ", "evidence": "corpus"},
            {"phrase": "international collaboration", "meaning_vi": "sự hợp tác quốc tế", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "corroborate",
                "ipa": "/kəˈrɑːbəreɪt/",
                "meaning": "chứng thực, củng cố bằng chứng",
                "kind": "spelling-sound",
                "difference_vi": "Collaborate là cùng nhau làm việc; corroborate mang nghĩa đưa ra chứng cứ xác minh điều gì."
            }
        ],
        "confusing_meanings": [
            {
                "word": "cooperate",
                "meaning": "hợp tác giúp đỡ",
                "difference_vi": "Cooperate là sẵn sàng giúp đỡ hoặc tuân thủ yêu cầu; collaborate là cùng bắt tay vào sáng tạo và thực hiện chung một dự án."
            }
        ],
        "synonyms": [
            {"word": "cooperate", "meaning_vi": "hợp tác"},
            {"word": "team up", "meaning_vi": "lập đội cùng làm"}
        ],
        "examples": [
            {
                "en": "Our engineering team will collaborate with external designers to develop the next-generation product.",
                "vi": "Đội ngũ kỹ thuật của chúng tôi sẽ cộng tác với các nhà thiết kế bên ngoài để phát triển sản phẩm thế hệ tiếp theo."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈlæb-/. Đuôi kết thúc bằng /-reɪt/, bật nhẹ âm /t/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "compensation",
        "lemma": "compensation",
        "pos": ["noun"],
        "ipa": {"us": "/ˌkɑːmpenˈseɪʃn/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["benefits", "hiring", "legal"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "compensation-1",
                "meaning_vi": "Chế độ thù lao lương bổng / Tiền bồi thường thiệt hại",
                "note_vi": "Dùng để chỉ toàn bộ gói lương thưởng hoặc khoản tiền đền bù khi xảy ra sự cố."
            }
        ],
        "collocations": [
            {"phrase": "compensation package", "meaning_vi": "gói chế độ thù lao đãi ngộ", "evidence": "corpus"},
            {"phrase": "financial compensation", "meaning_vi": "khoản tiền bồi thường tài chính", "evidence": "corpus"},
            {"phrase": "competitive compensation", "meaning_vi": "mức thù lao có tính cạnh tranh cao", "evidence": "corpus"},
            {"phrase": "workers' compensation", "meaning_vi": "bảo hiểm bồi thường tai nạn lao động", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "composition",
                "ipa": "/ˌkɑːmpəˈzɪʃn/",
                "meaning": "thành phần cấu tạo, bài luận",
                "kind": "spelling-sound",
                "difference_vi": "Compensation là tiền thù lao hoặc bồi thường; composition là thành phần kết cấu hoặc tác phẩm sáng tác."
            }
        ],
        "confusing_meanings": [
            {
                "word": "salary",
                "meaning": "lương tháng cơ bản",
                "difference_vi": "Salary là tiền lương cố định hàng tháng; compensation là tổng gói đãi ngộ gồm lương, thưởng, phúc lợi và phụ cấp."
            }
        ],
        "synonyms": [
            {"word": "remuneration", "meaning_vi": "tiền thù lao"},
            {"word": "recompense", "meaning_vi": "sự đền bù"}
        ],
        "examples": [
            {
                "en": "The company offers a competitive compensation package that includes health insurance and annual bonuses.",
                "vi": "Công ty cung cấp một gói thù lao cạnh tranh bao gồm bảo hiểm y tế và tiền thưởng hàng năm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm chính rơi vào âm tiết thứ ba /-ˈseɪ-/. Âm đầu là /kɑːm-/, âm đuôi /-ʃn/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "coordinate",
        "lemma": "coordinate",
        "pos": ["verb"],
        "ipa": {"us": "/koʊˈɔːrdɪneɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["management", "events", "work"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "coordinate-1",
                "meaning_vi": "Điều phối, phối hợp nhịp nhàng các hoạt động/lịch trình",
                "note_vi": "Rất hay gặp khi nói về công việc của điều phối viên dự án hoặc tổ chức sự kiện."
            }
        ],
        "collocations": [
            {"phrase": "coordinate efforts", "meaning_vi": "phối hợp các nỗ lực", "evidence": "corpus"},
            {"phrase": "coordinate the schedule", "meaning_vi": "điều phối lịch trình công tác", "evidence": "corpus"},
            {"phrase": "project coordinator", "meaning_vi": "điều phối viên dự án", "evidence": "corpus"},
            {"phrase": "coordinate with other departments", "meaning_vi": "phối hợp cùng các phòng ban khác", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "subordinate",
                "ipa": "/səˈbɔːrdɪnət/",
                "meaning": "cấp dưới, phụ thuộc",
                "kind": "spelling-sound",
                "difference_vi": "Coordinate là điều phối công việc; subordinate là nhân viên cấp dưới trực tiếp."
            }
        ],
        "confusing_meanings": [
            {
                "word": "manage",
                "meaning": "quản lý chỉ đạo",
                "difference_vi": "Manage là điều hành ra chỉ thị; coordinate là kết nối và sắp xếp các mắt xích làm việc ăn ý với nhau."
            }
        ],
        "synonyms": [
            {"word": "organize", "meaning_vi": "tổ chức sắp xếp"},
            {"word": "synchronize", "meaning_vi": "đồng bộ hóa"}
        ],
        "examples": [
            {
                "en": "The project coordinator will ensure all marketing materials are delivered before the conference starts.",
                "vi": "Điều phối viên dự án sẽ đảm bảo tất cả tài liệu tiếp thị được chuyển đến trước khi hội nghị bắt đầu."
            }
        ],
        "pronunciation_tips_vi": "Khi là động từ, phát âm âm đuôi là /-neɪt/ có trọng âm phụ. Âm đầu là /koʊ-/, âm tiết hai /-ˈɔːr-/ nhận trọng âm chính.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "delegate",
        "lemma": "delegate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈdelɪɡeɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["management", "work"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "delegate-1",
                "meaning_vi": "Phân công nhiệm vụ, ủy thác quyền hạn cho cấp dưới",
                "note_vi": "Kỹ năng quản lý lãnh đạo cốt lõi trong Part 5 (Express an opinion về phong cách lãnh đạo)."
            }
        ],
        "collocations": [
            {"phrase": "delegate tasks", "meaning_vi": "phân công các đầu việc", "evidence": "corpus"},
            {"phrase": "delegate authority", "meaning_vi": "ủy thác quyền hạn", "evidence": "corpus"},
            {"phrase": "effectively delegate", "meaning_vi": "phân chia công việc hiệu quả", "evidence": "corpus"},
            {"phrase": "delegate responsibilities", "meaning_vi": "giao phó trách nhiệm", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "dedicate",
                "ipa": "/ˈdedɪkeɪt/",
                "meaning": "cống hiến, tận tâm",
                "kind": "spelling-sound",
                "difference_vi": "Delegate là giao quyền phân công; dedicate là cống hiến hết lòng cho công việc."
            }
        ],
        "confusing_meanings": [
            {
                "word": "assign",
                "meaning": "giao việc đơn thuần",
                "difference_vi": "Assign chỉ đơn thuần giao đầu việc; delegate là trao luôn quyền hạn và quyền tự quyết cho cấp dưới."
            }
        ],
        "synonyms": [
            {"word": "assign", "meaning_vi": "phân công"},
            {"word": "entrust", "meaning_vi": "giao phó"}
        ],
        "examples": [
            {
                "en": "A successful manager knows how to delegate responsibilities effectively to trusted team members.",
                "vi": "Một nhà quản lý thành công luôn biết cách phân chia trách nhiệm hiệu quả cho các thành viên đáng tin cậy trong nhóm."
            }
        ],
        "pronunciation_tips_vi": "Khi là động từ, đuôi đọc là /-ɡeɪt/ có âm /eɪ/. Khi là danh từ (đại biểu), đuôi đọc là /-ɡət/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "eligible",
        "lemma": "eligible",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈelɪdʒəbl/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["benefits", "hiring", "shopping"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "eligible-1",
                "meaning_vi": "Đủ điều kiện, đủ tiêu chuẩn hưởng quyền lợi/chính sách",
                "note_vi": "Cực kỳ phổ biến trong thông báo chính sách thưởng, thăng chức, hoàn tiền hoặc giảm giá."
            }
        ],
        "collocations": [
            {"phrase": "eligible for promotion", "meaning_vi": "đủ điều kiện để được thăng chức", "evidence": "corpus"},
            {"phrase": "eligible for a refund", "meaning_vi": "đủ điều kiện được hoàn tiền", "evidence": "corpus"},
            {"phrase": "eligible to participate", "meaning_vi": "đủ tư cách tham dự", "evidence": "corpus"},
            {"phrase": "eligible candidate", "meaning_vi": "ứng viên đủ tiêu chuẩn", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "illegible",
                "ipa": "/ɪˈledʒəbl/",
                "meaning": "chữ viết mờ khó đọc",
                "kind": "spelling-sound",
                "difference_vi": "Eligible nghĩa là đủ tư cách/điều kiện; illegible nghĩa là chữ viết nguệch ngoạc không thể đọc được."
            }
        ],
        "confusing_meanings": [
            {
                "word": "qualified",
                "meaning": "có chuyên môn kinh nghiệm",
                "difference_vi": "Qualified nhấn mạnh vào năng lực kỹ năng chuyên môn; eligible là đáp ứng đúng các quy định tiêu chí hành chính."
            }
        ],
        "synonyms": [
            {"word": "qualified", "meaning_vi": "đủ tư cách"},
            {"word": "entitled", "meaning_vi": "có quyền hưởng"}
        ],
        "examples": [
            {
                "en": "Employees who complete six months of service are eligible for paid annual vacation.",
                "vi": "Nhân viên hoàn thành sáu tháng làm việc sẽ đủ điều kiện được hưởng kỳ nghỉ thường niên có lương."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈel-/. Âm giữa là /ɪdʒ/ nhẹ, đuôi /-əbl/ đọc dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "expedite",
        "lemma": "expedite",
        "pos": ["verb"],
        "ipa": {"us": "/ˈekspədaɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["logistics", "customer-service", "business"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "expedite-1",
                "meaning_vi": "Xử lý nhanh, đẩy nhanh tiến độ (giao hàng, thủ tục, giải quyết sự cố)",
                "note_vi": "Từ vựng trang trọng thường dùng trong chăm sóc khách hàng và chuyển phát hỏa tốc."
            }
        ],
        "collocations": [
            {"phrase": "expedite delivery", "meaning_vi": "đẩy nhanh tiến độ giao hàng hỏa tốc", "evidence": "corpus"},
            {"phrase": "expedite the process", "meaning_vi": "đẩy nhanh quy trình xử lý", "evidence": "corpus"},
            {"phrase": "expedite a shipment", "meaning_vi": "thúc đẩy chuyển phát đơn hàng", "evidence": "corpus"},
            {"phrase": "pay extra to expedite", "meaning_vi": "trả thêm phụ phí để chuyển phát nhanh", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "expect",
                "ipa": "/ɪkˈspekt/",
                "meaning": "kỳ vọng, mong chờ",
                "kind": "spelling-sound",
                "difference_vi": "Expedite là xúc tiến đẩy nhanh quy trình; expect mang nghĩa chờ đợi hoặc kỳ vọng."
            }
        ],
        "confusing_meanings": [
            {
                "word": "accelerate",
                "meaning": "tăng tốc độ chuyển động",
                "difference_vi": "Accelerate là tăng vận tốc vật lý; expedite là đẩy nhanh tiến độ xử lý thủ tục hành chính hoặc tiến trình đơn hàng."
            }
        ],
        "synonyms": [
            {"word": "speed up", "meaning_vi": "tăng tốc"},
            {"word": "accelerate", "meaning_vi": "đẩy nhanh"}
        ],
        "examples": [
            {
                "en": "We requested the supplier to expedite the shipment so we could meet our project deadline.",
                "vi": "Chúng tôi đã yêu cầu nhà cung cấp đẩy nhanh tiến độ giao hàng để có thể kịp hạn chót của dự án."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈeks-/. Âm đuôi là /-daɪt/ với nguyên âm đôi /aɪ/ và bật nhẹ âm /t/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "facility",
        "lemma": "facility",
        "pos": ["noun"],
        "ipa": {"us": "/fəˈsɪləti/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["manufacturing", "business", "events"],
        "speaking_use": ["describe-picture", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "facility-1",
                "meaning_vi": "Cơ sở vật chất, nhà máy, trang thiết bị tiện nghi",
                "note_vi": "Từ bao quát chỉ nhà xưởng sản xuất, trung tâm thể thao, hoặc cơ sở hạ tầng văn phòng."
            }
        ],
        "collocations": [
            {"phrase": "manufacturing facility", "meaning_vi": "cơ sở / nhà máy sản xuất", "evidence": "corpus"},
            {"phrase": "state-of-the-art facility", "meaning_vi": "cơ sở hạ tầng tối tân hiện đại", "evidence": "corpus"},
            {"phrase": "facility management", "meaning_vi": "quản lý cơ sở vật chất", "evidence": "corpus"},
            {"phrase": "research facility", "meaning_vi": "cơ sở nghiên cứu khoa học", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "faculty",
                "ipa": "/ˈfæklti/",
                "meaning": "đội ngũ giảng viên, khoa trường đại học",
                "kind": "spelling-sound",
                "difference_vi": "Facility là cơ sở hạ tầng vật chất; faculty là đội ngũ giảng viên hoặc khả năng trí tuệ."
            }
        ],
        "confusing_meanings": [
            {
                "word": "building",
                "meaning": "tòa nhà vật lý",
                "difference_vi": "Building là công trình xây dựng gạch đá; facility là toàn bộ tổ hợp cơ sở vật chất phục vụ hoạt động cụ thể."
            }
        ],
        "synonyms": [
            {"word": "establishment", "meaning_vi": "cơ sở"},
            {"word": "premises", "meaning_vi": "khuôn viên cơ sở"}
        ],
        "examples": [
            {
                "en": "The company invested ten million dollars to construct a state-of-the-art manufacturing facility.",
                "vi": "Công ty đã đầu tư mười triệu đô la để xây dựng một nhà máy sản xuất hiện đại bậc nhất."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈsɪl-/. Âm đầu là schwa /fə-/, đuôi /-ti/ đọc dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "incentive",
        "lemma": "incentive",
        "pos": ["noun"],
        "ipa": {"us": "/ɪnˈsentɪv/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["benefits", "sales", "management"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "incentive-1",
                "meaning_vi": "Sự khích lệ, tiền thưởng động viên (nhằm thúc đẩy năng suất/doanh số)",
                "note_vi": "Thường dùng trong chính sách hoa hồng bán hàng hoặc phần thưởng tạo động lực cho nhân viên."
            }
        ],
        "collocations": [
            {"phrase": "financial incentive", "meaning_vi": "phần thưởng tài chính khích lệ", "evidence": "corpus"},
            {"phrase": "sales incentive", "meaning_vi": "tiền thưởng thúc đẩy doanh số", "evidence": "corpus"},
            {"phrase": "provide an incentive", "meaning_vi": "tạo động lực thúc đẩy", "evidence": "corpus"},
            {"phrase": "strong incentive", "meaning_vi": "động lực to lớn", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "intensive",
                "ipa": "/ɪnˈtensɪv/",
                "meaning": "chuyên sâu, cấp tốc",
                "kind": "spelling-sound",
                "difference_vi": "Incentive (danh từ) là động lực khích lệ; intensive (tính từ) là mang tính chuyên sâu cao độ."
            }
        ],
        "confusing_meanings": [
            {
                "word": "bonus",
                "meaning": "tiền thưởng thêm",
                "difference_vi": "Bonus là tiền thưởng trao sau khi đạt kết quả; incentive là phần thưởng hứa hẹn từ trước để kích thích nỗ lực."
            }
        ],
        "synonyms": [
            {"word": "motivation", "meaning_vi": "động lực"},
            {"word": "stimulus", "meaning_vi": "chất xúc tác kích thích"}
        ],
        "examples": [
            {
                "en": "Offering performance bonuses provides a strong incentive for employees to exceed their quarterly sales targets.",
                "vi": "Đưa ra các khoản thưởng theo hiệu suất làm việc tạo ra động lực to lớn giúp nhân viên vượt chỉ tiêu doanh số hàng quý."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈsen-/. Âm đuôi /-tɪv/ dứt khoát, tránh nhầm với tính từ 'intensive'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "invoice",
        "lemma": "invoice",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈɪnvɔɪs/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["budget", "sales", "business"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "invoice-1",
                "meaning_vi": "Hóa đơn yêu cầu thanh toán (gửi cho khách trước khi trả tiền)",
                "note_vi": "Từ ngữ kế toán công sở phổ biến nhất trong các bài thi TOEIC."
            }
        ],
        "collocations": [
            {"phrase": "issue an invoice", "meaning_vi": "xuất hóa đơn yêu cầu thanh toán", "evidence": "corpus"},
            {"phrase": "pay an invoice", "meaning_vi": "thanh toán hóa đơn", "evidence": "corpus"},
            {"phrase": "invoice number", "meaning_vi": "mã số hóa đơn", "evidence": "corpus"},
            {"phrase": "outstanding invoice", "meaning_vi": "hóa đơn chưa được thanh toán (còn nợ)", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "invoke",
                "ipa": "/ɪnˈvoʊk/",
                "meaning": "viện dẫn luật, khơi gợi",
                "kind": "spelling-sound",
                "difference_vi": "Invoice là hóa đơn tính tiền; invoke mang nghĩa viện dẫn điều luật hoặc cầu khẩn."
            }
        ],
        "confusing_meanings": [
            {
                "word": "receipt",
                "meaning": "biên lai đã thanh toán",
                "difference_vi": "Invoice là chứng từ đòi tiền gửi trước; receipt là bằng chứng xác nhận tiền đã được trả xong."
            }
        ],
        "synonyms": [
            {"word": "bill", "meaning_vi": "hóa đơn tính tiền"}
        ],
        "examples": [
            {
                "en": "The accounting department will issue an invoice immediately after the goods have been shipped.",
                "vi": "Phòng kế toán sẽ phát hành hóa đơn thanh toán ngay sau khi hàng hóa được gửi đi."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈɪn-/. Âm tiết hai có nguyên âm đôi /ɔɪ/ và kết thúc bằng âm /s/ xì nhẹ: /ˈɪnvɔɪs/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "maintenance",
        "lemma": "maintenance",
        "pos": ["noun"],
        "ipa": {"us": "/ˈmeɪntənəns/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["equipment", "manufacturing", "technology"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "maintenance-1",
                "meaning_vi": "Sự bảo trì, bảo dưỡng định kỳ máy móc/thiết bị",
                "note_vi": "Rất hay gặp trong Part 1 (thông báo máy in/thang máy bảo trì) và Part 4 (lịch bảo trì hệ thống)."
            }
        ],
        "collocations": [
            {"phrase": "routine maintenance", "meaning_vi": "bảo trì định kỳ thường xuyên", "evidence": "corpus"},
            {"phrase": "maintenance schedule", "meaning_vi": "lịch trình bảo dưỡng định kỳ", "evidence": "corpus"},
            {"phrase": "under maintenance", "meaning_vi": "đang trong quá trình bảo trì", "evidence": "corpus"},
            {"phrase": "maintenance worker", "meaning_vi": "nhân viên bảo trì", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "maintain",
                "ipa": "/meɪnˈteɪn/",
                "meaning": "duy trì, bảo dưỡng (động từ)",
                "kind": "spelling-sound",
                "difference_vi": "Động từ maintain nhấn âm hai /meɪnˈteɪn/; danh từ maintenance nhấn âm đầu /ˈmeɪntənəns/."
            }
        ],
        "confusing_meanings": [
            {
                "word": "repair",
                "meaning": "sửa chữa đồ đã hỏng",
                "difference_vi": "Repair là khắc phục khi đồ vật đã bị hỏng; maintenance là chăm sóc bảo dưỡng định kỳ để ngăn ngừa hư hỏng."
            }
        ],
        "synonyms": [
            {"word": "upkeep", "meaning_vi": "sự gìn giữ bảo dưỡng"},
            {"word": "servicing", "meaning_vi": "sự bảo trì máy móc"}
        ],
        "examples": [
            {
                "en": "The office elevator will be temporarily out of service this Saturday for scheduled maintenance.",
                "vi": "Thang máy văn phòng sẽ tạm thời ngừng hoạt động vào thứ Bảy này để tiến hành bảo trì theo kế hoạch."
            }
        ],
        "pronunciation_tips_vi": "LƯU Ý TRỌNG ÂM: Khác với động từ maintain nhấn âm hai, danh từ maintenance nhấn âm ĐẦU /ˈmeɪn-/, hai âm sau là schwa /-tənəns/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "promote",
        "lemma": "promote",
        "pos": ["verb"],
        "ipa": {"us": "/prəˈmoʊt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "marketing", "business"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "promote-1",
                "meaning_vi": "Thăng chức cho nhân viên / Quảng bá, tiếp thị sản phẩm",
                "note_vi": "Có hai tầng nghĩa quan trọng bậc nhất trong TOEIC: thăng tiến sự nghiệp và tiếp thị thương hiệu."
            }
        ],
        "collocations": [
            {"phrase": "promoted to manager", "meaning_vi": "được thăng chức lên vị trí quản lý", "evidence": "corpus"},
            {"phrase": "promote a product", "meaning_vi": "quảng bá một sản phẩm", "evidence": "corpus"},
            {"phrase": "promote teamwork", "meaning_vi": "thúc đẩy tinh thần làm việc nhóm", "evidence": "corpus"},
            {"phrase": "heavily promote", "meaning_vi": "quảng bá rầm rộ trên diện rộng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "prompt",
                "ipa": "/prɑːmpt/",
                "meaning": "nhanh chóng, ngay tức thì",
                "kind": "spelling-sound",
                "difference_vi": "Promote là thăng chức hoặc quảng bá; prompt là tính từ mau lẹ hoặc lời nhắc nhở."
            }
        ],
        "confusing_meanings": [
            {
                "word": "advertise",
                "meaning": "đăng quảng cáo",
                "difference_vi": "Advertise chỉ đơn thuần là mua quảng cáo trên truyền thông; promote là hoạt động xúc tiến tiếp thị đa kênh rộng hơn."
            }
        ],
        "synonyms": [
            {"word": "advance", "meaning_vi": "tiến cử, thăng tiến"},
            {"word": "endorse", "meaning_vi": "ủng hộ, quảng bá"}
        ],
        "examples": [
            {
                "en": "Because of her exceptional leadership, she was recently promoted to regional sales director.",
                "vi": "Nhờ năng lực lãnh đạo xuất sắc của mình, cô ấy gần đây đã được thăng chức lên vị trí giám đốc kinh doanh khu vực."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈmoʊt/. Âm đầu là schwa /prə-/, âm tiết hai có nguyên âm đôi /oʊ/ và bật nhẹ âm /t/ cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "turnover",
        "lemma": "turnover",
        "pos": ["noun"],
        "ipa": {"us": "/ˈtɜːrnoʊvər/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["hiring", "sales", "management"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "turnover-1",
                "meaning_vi": "Tỷ lệ luân chuyển nhân sự (nhảy việc) / Doanh số luân chuyển vốn",
                "note_vi": "Chủ đề giữ chân nhân tài (employee retention) hoặc tốc độ quay vòng hàng hóa."
            }
        ],
        "collocations": [
            {"phrase": "high employee turnover", "meaning_vi": "tỷ lệ nhân viên nhảy việc cao", "evidence": "corpus"},
            {"phrase": "reduce turnover", "meaning_vi": "giảm thiểu tỷ lệ nhân viên nghỉ việc", "evidence": "corpus"},
            {"phrase": "annual turnover", "meaning_vi": "doanh số hàng năm", "evidence": "corpus"},
            {"phrase": "staff turnover rate", "meaning_vi": "tỷ lệ thay thế nhân sự", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "takeover",
                "ipa": "/ˈteɪkoʊvər/",
                "meaning": "sự thâu tóm công ty",
                "kind": "spelling-sound",
                "difference_vi": "Turnover là tỷ lệ nhảy việc hoặc doanh số; takeover là thương vụ mua lại thâu tóm doanh nghiệp."
            }
        ],
        "confusing_meanings": [
            {
                "word": "retention",
                "meaning": "sự giữ chân nhân sự",
                "difference_vi": "Retention là tỷ lệ nhân viên ở lại gắn bó; turnover là tỷ lệ nhân viên rời bỏ công ty."
            }
        ],
        "synonyms": [
            {"word": "attrition", "meaning_vi": "sự hao hụt nhân sự tự nhiên"},
            {"word": "sales volume", "meaning_vi": "khối lượng doanh số"}
        ],
        "examples": [
            {
                "en": "Offering competitive salaries and flexible working hours helps the company reduce high employee turnover.",
                "vi": "Cung cấp mức lương cạnh tranh và giờ làm việc linh hoạt giúp công ty giảm thiểu tỷ lệ nhân viên nhảy việc cao."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép: /ˈtɜːrn/ + /oʊvər/. Trọng âm rơi vào âm tiết đầu /ˈtɜːrn-/. Chú ý âm /ɜːr/ cong lưỡi chuẩn giọng Mỹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    }
]

def main():
    created_count = 0
    for w in words_data:
        first_letter = w["id"][0]
        letter_dir = os.path.join(LEXICON_DIR, first_letter)
        os.makedirs(letter_dir, exist_ok=True)
        file_path = os.path.join(letter_dir, f"{w['id']}.yaml")
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(w, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        created_count += 1
        print(f"Created: {file_path}")
    print(f"\n[OK] Successfully created {created_count} lexicon files.")

if __name__ == "__main__":
    main()
