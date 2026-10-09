import os
import yaml

LEXICON_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "lexicon")

words_data = [
    {
        "schema_version": 2,
        "id": "agreement",
        "lemma": "agreement",
        "pos": ["noun"],
        "ipa": {"us": "/əˈɡriːmənt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["contracts", "business", "meetings"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "agreement-1",
                "meaning_vi": "Sự thỏa thuận, hợp đồng cam kết giữa các bên",
                "note_vi": "Dùng phổ biến trong đàm phán thương mại và ký kết văn bản thỏa thuận."
            }
        ],
        "collocations": [
            {"phrase": "reach an agreement", "meaning_vi": "đạt được thỏa thuận", "evidence": "corpus"},
            {"phrase": "come to an agreement", "meaning_vi": "đi đến thống nhất chung", "evidence": "corpus"},
            {"phrase": "signed agreement", "meaning_vi": "bản thỏa thuận đã được ký kết", "evidence": "corpus"},
            {"phrase": "terms of the agreement", "meaning_vi": "các điều khoản của bản thỏa thuận", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "argument",
                "ipa": "/ˈɑːrɡjumənt/",
                "meaning": "sự tranh cãi, bất đồng",
                "kind": "spelling-sound",
                "difference_vi": "Agreement là sự đồng thuận, nhất trí; argument là cuộc tranh cãi hoặc bất đồng ý kiến."
            }
        ],
        "confusing_meanings": [
            {
                "word": "contract",
                "meaning": "hợp đồng pháp lý có chế tài chặt chẽ",
                "difference_vi": "Contract là hợp đồng chính thức có ràng buộc pháp lý; agreement là sự thỏa thuận nói chung (có thể bằng lời nói hoặc văn bản ghi nhớ)."
            }
        ],
        "synonyms": [
            {"word": "contract", "meaning_vi": "hợp đồng"},
            {"word": "deal", "meaning_vi": "thương vụ thỏa thuận"}
        ],
        "examples": [
            {
                "en": "After lengthy discussions, both companies finally reached a mutual agreement yesterday.",
                "vi": "Sau các cuộc thảo luận kéo dài, cả hai công ty cuối cùng đã đạt được thỏa thuận chung vào ngày hôm qua."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈɡriː-/. Lưu ý nguyên âm dài /iː/, đuôi /-mənt/ phát âm schwa nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "assemble",
        "lemma": "assemble",
        "pos": ["verb"],
        "ipa": {"us": "/əˈsembl/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["manufacturing", "equipment", "meetings"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "assemble-1",
                "meaning_vi": "Lắp ráp linh kiện, đồ đạc / Tập hợp mọi người lại một nơi",
                "note_vi": "Part 2 thường gặp cảnh công nhân lắp ráp thiết bị hoặc mọi người tập hợp trong phòng họp."
            }
        ],
        "collocations": [
            {"phrase": "assemble parts", "meaning_vi": "lắp ráp các linh kiện phụ tùng", "evidence": "corpus"},
            {"phrase": "easily assembled", "meaning_vi": "dễ dàng lắp ráp", "evidence": "corpus"},
            {"phrase": "assembly line", "meaning_vi": "dây chuyền lắp ráp sản xuất", "evidence": "corpus"},
            {"phrase": "assemble in the auditorium", "meaning_vi": "tập hợp tại khán phòng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "resemble",
                "ipa": "/rɪˈzembl/",
                "meaning": "giống nhau về ngoại hình",
                "kind": "spelling-sound",
                "difference_vi": "Assemble là lắp ráp hoặc tập hợp; resemble là trông giống một ai đó hoặc vật gì đó."
            }
        ],
        "confusing_meanings": [
            {
                "word": "gather",
                "meaning": "tụ họp tự nhiên",
                "difference_vi": "Gather là hành động tụ tập tự nhiên của đám đông; assemble mang tính tổ chức bài bản hoặc thao tác kỹ thuật lắp ráp linh kiện."
            }
        ],
        "synonyms": [
            {"word": "put together", "meaning_vi": "ghép lại"},
            {"word": "gather", "meaning_vi": "tập hợp"}
        ],
        "examples": [
            {
                "en": "The new office furniture comes with clear instructions and can be easily assembled in minutes.",
                "vi": "Nội thất văn phòng mới đi kèm với hướng dẫn rõ ràng và có thể dễ dàng lắp ráp trong vài phút."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈsem-/. Âm đuôi /-bl/ đọc dứt khoát không thêm 'ờ'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "assess",
        "lemma": "assess",
        "pos": ["verb"],
        "ipa": {"us": "/əˈses/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["business", "management", "education"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "assess-1",
                "meaning_vi": "Đánh giá, thẩm định (tình hình, hiệu quả, thiệt hại)",
                "note_vi": "Rất hay gặp khi nói về thẩm định hiệu quả dự án, đánh giá năng lực nhân viên."
            }
        ],
        "collocations": [
            {"phrase": "assess performance", "meaning_vi": "đánh giá hiệu quả làm việc", "evidence": "corpus"},
            {"phrase": "assess the damage", "meaning_vi": "ước tính/thẩm định thiệt hại", "evidence": "corpus"},
            {"phrase": "assess the impact", "meaning_vi": "đánh giá mức độ ảnh hưởng", "evidence": "corpus"},
            {"phrase": "thoroughly assess", "meaning_vi": "đánh giá một cách kỹ lưỡng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "access",
                "ipa": "/ˈækses/",
                "meaning": "sự truy cập, lối vào",
                "kind": "spelling-sound",
                "difference_vi": "Assess (động từ) nhấn âm hai mang nghĩa đánh giá; access (danh từ/động từ) nhấn âm đầu mang nghĩa truy cập."
            }
        ],
        "confusing_meanings": [
            {
                "word": "evaluate",
                "meaning": "đánh giá toàn diện dựa trên hệ thống tiêu chí",
                "difference_vi": "Assess thường dùng khi đo lường mức độ, quy mô hoặc giá trị thiệt hại; evaluate mang tính phân tích tổng hợp chất lượng."
            }
        ],
        "synonyms": [
            {"word": "evaluate", "meaning_vi": "đánh giá"},
            {"word": "estimate", "meaning_vi": "ước lượng"}
        ],
        "examples": [
            {
                "en": "The supervisor will assess each employee's annual performance at the end of this quarter.",
                "vi": "Người giám sát sẽ đánh giá hiệu quả công việc hàng năm của từng nhân viên vào cuối quý này."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈses/. Âm đầu là schwa /ə/ nhẹ, tránh nhầm với danh từ 'access' nhấn âm đầu /ˈæk/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "campaign",
        "lemma": "campaign",
        "pos": ["noun"],
        "ipa": {"us": "/kæmˈpeɪn/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["marketing", "business"],
        "speaking_use": ["read-aloud", "respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "campaign-1",
                "meaning_vi": "Chiến dịch (quảng cáo, tiếp thị, nâng cao nhận thức)",
                "note_vi": "Từ trọng tâm trong mảng Marketing & Bán hàng (Part 1, 3, 5)."
            }
        ],
        "collocations": [
            {"phrase": "marketing campaign", "meaning_vi": "chiến dịch tiếp thị", "evidence": "corpus"},
            {"phrase": "advertising campaign", "meaning_vi": "chiến dịch quảng cáo", "evidence": "corpus"},
            {"phrase": "launch a campaign", "meaning_vi": "tung ra / khởi động một chiến dịch", "evidence": "corpus"},
            {"phrase": "successful campaign", "meaning_vi": "chiến dịch thành công vang dội", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "champion",
                "ipa": "/ˈtʃæmpiən/",
                "meaning": "nhà vô địch, quán quân",
                "kind": "spelling-sound",
                "difference_vi": "Campaign phát âm /kæmˈpeɪn/ là chiến dịch; champion phát âm /ˈtʃæmpiən/ là nhà vô địch."
            }
        ],
        "confusing_meanings": [
            {
                "word": "promotion",
                "meaning": "chương trình khuyến mãi giảm giá ngắn hạn",
                "difference_vi": "Promotion là đợt giảm giá kích cầu ngắn hạn; campaign là chiến dịch truyền thông toàn diện có kế hoạch dài hơi."
            }
        ],
        "synonyms": [
            {"word": "marketing drive", "meaning_vi": "đợt xúc tiến tiếp thị"},
            {"word": "promotional effort", "meaning_vi": "nỗ lực quảng bá"}
        ],
        "examples": [
            {
                "en": "The company plans to launch a nationwide advertising campaign for its new smartphone next month.",
                "vi": "Công ty có kế hoạch triển khai một chiến dịch quảng cáo trên toàn quốc cho chiếc điện thoại thông minh mới vào tháng tới."
            }
        ],
        "pronunciation_tips_vi": "Chữ cái 'g' là ÂM CÂM! Phát âm là /kæmˈpeɪn/, trọng âm rơi vào âm tiết hai với nguyên âm đôi /eɪ/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "candidate",
        "lemma": "candidate",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkændɪdət/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "work"],
        "speaking_use": ["respond-with-info", "respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "candidate-1",
                "meaning_vi": "Ứng viên sáng giá (đã được chọn vào danh sách phỏng vấn)",
                "note_vi": "Chủ đề tuyển dụng và phỏng vấn việc làm."
            }
        ],
        "collocations": [
            {"phrase": "ideal candidate", "meaning_vi": "ứng viên lý tưởng", "evidence": "corpus"},
            {"phrase": "qualified candidate", "meaning_vi": "ứng viên đủ tiêu chuẩn năng lực", "evidence": "corpus"},
            {"phrase": "prospective candidate", "meaning_vi": "ứng viên tiềm năng", "evidence": "corpus"},
            {"phrase": "shortlist candidates", "meaning_vi": "chọn lọc ứng viên vào danh sách rút gọn", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "candid",
                "ipa": "/ˈkændɪd/",
                "meaning": "thẳng thắn, bộc trực",
                "kind": "spelling-sound",
                "difference_vi": "Candidate là danh từ chỉ ứng viên; candid là tính từ mang nghĩa thành thật, bộc trực."
            }
        ],
        "confusing_meanings": [
            {
                "word": "applicant",
                "meaning": "người mới nộp hồ sơ bước đầu",
                "difference_vi": "Applicant là người nộp đơn đăng ký ban đầu; candidate là người đã qua sàng lọc để vào vòng tuyển chọn chính thức."
            }
        ],
        "synonyms": [
            {"word": "applicant", "meaning_vi": "người xin việc"},
            {"word": "nominee", "meaning_vi": "người được đề cử"}
        ],
        "examples": [
            {
                "en": "She is considered the most qualified candidate for the senior project manager vacancy.",
                "vi": "Cô ấy được đánh giá là ứng viên đủ tiêu chuẩn nhất cho vị trí trưởng nhóm quản lý dự án còn trống."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈkæn/. Âm đuôi là schwa /-dət/ ngắn gọn, bật nhẹ âm /t/ cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "client",
        "lemma": "client",
        "pos": ["noun"],
        "ipa": {"us": "/ˈklaɪənt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["sales", "business", "customer-service"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "client-1",
                "meaning_vi": "Khách hàng sử dụng dịch vụ chuyên nghiệp, đối tác thân thiết",
                "note_vi": "Thường dùng trong các ngành dịch vụ chuyên môn (luật, tư vấn, thiết kế, tài chính)."
            }
        ],
        "collocations": [
            {"phrase": "prospective client", "meaning_vi": "khách hàng tiềm năng", "evidence": "corpus"},
            {"phrase": "meet with a client", "meaning_vi": "gặp gỡ đối tác/khách hàng", "evidence": "corpus"},
            {"phrase": "corporate client", "meaning_vi": "khách hàng doanh nghiệp", "evidence": "corpus"},
            {"phrase": "client satisfaction", "meaning_vi": "sự hài lòng của khách hàng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "climate",
                "ipa": "/ˈklaɪmət/",
                "meaning": "khí hậu, thời tiết",
                "kind": "spelling-sound",
                "difference_vi": "Client kết thúc bằng /-ənt/ nghĩa là khách hàng; climate kết thúc bằng /-mət/ nghĩa là khí hậu."
            }
        ],
        "confusing_meanings": [
            {
                "word": "customer",
                "meaning": "người mua hàng hóa bán lẻ tại cửa hàng",
                "difference_vi": "Customer là khách mua sản phẩm đơn lẻ tại quầy; client là khách hàng thuê dịch vụ chuyên môn theo hợp đồng dài hạn."
            }
        ],
        "synonyms": [
            {"word": "customer", "meaning_vi": "khách hàng"},
            {"word": "patron", "meaning_vi": "khách quen"}
        ],
        "examples": [
            {
                "en": "Our senior consultant will travel to Chicago tomorrow morning to meet with an important client.",
                "vi": "Chuyên viên tư vấn cao cấp của chúng tôi sẽ đến Chicago vào sáng mai để gặp một khách hàng quan trọng."
            }
        ],
        "pronunciation_tips_vi": "Nguyên âm đôi /aɪ/ kéo dài rõ ràng: /ˈklaɪ-ənt/. Trọng âm rơi vào âm tiết đầu, âm /t/ cuối bật nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "contract",
        "lemma": "contract",
        "pos": ["noun"],
        "ipa": {"us": "/ˈkɑːntrækt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["contracts", "business", "sales"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "contract-1",
                "meaning_vi": "Hợp đồng kinh tế có tính ràng buộc pháp lý",
                "note_vi": "Xuất hiện khắp các bài thi TOEIC liên quan đến đàm phán, ký kết và gia hạn hợp đồng."
            }
        ],
        "collocations": [
            {"phrase": "sign a contract", "meaning_vi": "ký kết hợp đồng", "evidence": "corpus"},
            {"phrase": "breach of contract", "meaning_vi": "sự vi phạm hợp đồng", "evidence": "corpus"},
            {"phrase": "renew a contract", "meaning_vi": "gia hạn hợp đồng", "evidence": "corpus"},
            {"phrase": "legally binding contract", "meaning_vi": "hợp đồng có tính ràng buộc pháp lý", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "contact",
                "ipa": "/ˈkɑːntækt/",
                "meaning": "liên lạc, mối liên hệ",
                "kind": "spelling-sound",
                "difference_vi": "Contract có phụ âm 'r' (/ˈkɑːntrækt/) nghĩa là hợp đồng; contact không có 'r' (/ˈkɑːntækt/) nghĩa là liên hệ."
            }
        ],
        "confusing_meanings": [
            {
                "word": "agreement",
                "meaning": "sự thống nhất/thỏa thuận nói chung",
                "difference_vi": "Contract là văn bản pháp lý chính thức có điều khoản bắt buộc thi hành; agreement là sự đồng thuận rộng hơn."
            }
        ],
        "synonyms": [
            {"word": "agreement", "meaning_vi": "bản thỏa thuận"},
            {"word": "deal", "meaning_vi": "thỏa thuận thương vụ"}
        ],
        "examples": [
            {
                "en": "Both parties carefully reviewed all clauses before signing the three-year service contract.",
                "vi": "Cả hai bên đã xem xét cẩn thận tất cả các điều khoản trước khi ký hợp đồng dịch vụ ba năm."
            }
        ],
        "pronunciation_tips_vi": "Khi là danh từ, trọng âm rơi vào âm tiết đầu /ˈkɑːn-/. Chú ý cụm phụ âm /tr/ ở âm tiết hai /-trækt/, bật rõ âm /kt/ cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "crucial",
        "lemma": "crucial",
        "pos": ["adjective"],
        "ipa": {"us": "/ˈkruːʃl/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["management", "business"],
        "speaking_use": ["express-opinion", "respond-to-questions"],
        "senses": [
            {
                "id": "crucial-1",
                "meaning_vi": "Cốt yếu, mang tính quyết định, tối quan trọng",
                "note_vi": "Từ vựng ghi điểm rất cao trong phần Part 5 (Express an Opinion) khi giải thích lý do quan trọng."
            }
        ],
        "collocations": [
            {"phrase": "play a crucial role", "meaning_vi": "đóng vai trò cốt yếu", "evidence": "corpus"},
            {"phrase": "crucial factor", "meaning_vi": "yếu tố mang tính quyết định", "evidence": "corpus"},
            {"phrase": "crucial decision", "meaning_vi": "quyết định mang tính then chốt", "evidence": "corpus"},
            {"phrase": "of crucial importance", "meaning_vi": "có tầm quan trọng tối cao", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "crude",
                "ipa": "/kruːd/",
                "meaning": "thô sơ, chưa tinh chế (dầu thô)",
                "kind": "spelling-sound",
                "difference_vi": "Crucial phát âm /ˈkruːʃl/ nghĩa là cốt yếu; crude phát âm /kruːd/ nghĩa là thô mộc, chưa qua chế biến."
            }
        ],
        "confusing_meanings": [
            {
                "word": "important",
                "meaning": "quan trọng thông thường",
                "difference_vi": "Important là quan trọng nói chung; crucial là mang tính sống còn, quyết định trực tiếp tới thành bại của vấn đề."
            }
        ],
        "synonyms": [
            {"word": "vital", "meaning_vi": "sống còn"},
            {"word": "essential", "meaning_vi": "thiết yếu"},
            {"word": "critical", "meaning_vi": "mang tính quyết định"}
        ],
        "examples": [
            {
                "en": "Effective teamwork plays a crucial role in delivering complex software projects on schedule.",
                "vi": "Làm việc nhóm hiệu quả đóng vai trò cốt yếu trong việc bàn giao các dự án phần mềm phức tạp đúng tiến độ."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈkruː-/. Âm giữa là âm /ʃ/ ('sh'), đuôi /-l/ phát âm gọn: /ˈkruːʃl/, không đọc thành 'kru-si-an'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "defect",
        "lemma": "defect",
        "pos": ["noun"],
        "ipa": {"us": "/ˈdiːfekt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["manufacturing", "sales", "customer-service"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "defect-1",
                "meaning_vi": "Lỗi sản phẩm, khuyết tật kỹ thuật hoặc chi tiết hỏng",
                "note_vi": "Chủ đề kiểm định chất lượng xuất xưởng và bảo hành sản phẩm."
            }
        ],
        "collocations": [
            {"phrase": "manufacturing defect", "meaning_vi": "lỗi do quá trình sản xuất", "evidence": "corpus"},
            {"phrase": "free of defects", "meaning_vi": "không có bất kỳ khuyết tật nào", "evidence": "corpus"},
            {"phrase": "major defect", "meaning_vi": "lỗi nghiêm trọng", "evidence": "corpus"},
            {"phrase": "report a defect", "meaning_vi": "báo cáo sự cố hư hỏng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "defeat",
                "ipa": "/dɪˈfiːt/",
                "meaning": "đánh bại, sự thất bại",
                "kind": "spelling-sound",
                "difference_vi": "Defect là lỗi sản phẩm hư hỏng; defeat là đánh bại đối thủ hoặc sự thất bại trong thi đấu."
            }
        ],
        "confusing_meanings": [
            {
                "word": "error",
                "meaning": "sai sót do con người thao tác",
                "difference_vi": "Error là sai lầm trong tính toán hoặc hành vi con người; defect là khuyết tật vật lý tồn tại trên sản phẩm."
            }
        ],
        "synonyms": [
            {"word": "flaw", "meaning_vi": "vết tì, lỗi kỹ thuật"},
            {"word": "fault", "meaning_vi": "khuyết điểm, trục trặc"}
        ],
        "examples": [
            {
                "en": "Any appliance found to have a manufacturing defect will be replaced immediately at no extra cost.",
                "vi": "Bất kỳ thiết bị nào bị phát hiện có lỗi do nhà sản xuất sẽ được đổi mới ngay lập tức mà không phát sinh thêm chi phí."
            }
        ],
        "pronunciation_tips_vi": "Danh từ nhấn âm đầu /ˈdiː-/, âm tiết hai /-fekt/ bật rõ cụm phụ âm cuối /-kt/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "deliver",
        "lemma": "deliver",
        "pos": ["verb"],
        "ipa": {"us": "/dɪˈlɪvər/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["logistics", "shopping", "transport"],
        "speaking_use": ["read-aloud", "respond-to-questions"],
        "senses": [
            {
                "id": "deliver-1",
                "meaning_vi": "Giao hàng, chuyển phát hàng hóa / Phát biểu bài nói",
                "note_vi": "Rất phổ biến trong dịch vụ vận chuyển bưu kiện và phân phối hàng hóa."
            }
        ],
        "collocations": [
            {"phrase": "deliver a package", "meaning_vi": "giao một bưu kiện", "evidence": "corpus"},
            {"phrase": "prompt delivery", "meaning_vi": "việc giao hàng nhanh chóng", "evidence": "corpus"},
            {"phrase": "deliver a speech", "meaning_vi": "đọc một bài phát biểu", "evidence": "corpus"},
            {"phrase": "delivered on time", "meaning_vi": "được giao đúng hẹn", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "deliberate",
                "ipa": "/dɪˈlɪbərət/",
                "meaning": "cố tình, có chủ ý",
                "kind": "spelling-sound",
                "difference_vi": "Deliver là giao nhận hàng hóa; deliberate mang nghĩa cố ý làm việc gì hoặc suy xét thận trọng."
            }
        ],
        "confusing_meanings": [
            {
                "word": "ship",
                "meaning": "gửi hàng qua hãng vận chuyển",
                "difference_vi": "Ship là gửi hàng đi xa trên phương tiện vận tải; deliver là giao hàng tới tận tay người nhận ở bước cuối."
            }
        ],
        "synonyms": [
            {"word": "transport", "meaning_vi": "vận chuyển"},
            {"word": "distribute", "meaning_vi": "phân phối"}
        ],
        "examples": [
            {
                "en": "The courier company guarantees that your urgent package will be delivered before noon tomorrow.",
                "vi": "Công ty chuyển phát nhanh cam kết rằng kiện hàng khẩn cấp của bạn sẽ được giao trước trưa mai."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈlɪv-/. Âm đầu là /dɪ-/, âm cuối /-vər/ rung nhẹ môi dưới và cong lưỡi âm /r/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "efficient",
        "lemma": "efficient",
        "pos": ["adjective"],
        "ipa": {"us": "/ɪˈfɪʃnt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["work", "management", "technology"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "efficient-1",
                "meaning_vi": "Hiệu quả, năng suất cao (tiết kiệm thời gian, tiền bạc và công sức)",
                "note_vi": "Thường dùng để khen ngợi hệ thống làm việc, phương pháp quản lý hoặc nhân viên."
            }
        ],
        "collocations": [
            {"phrase": "energy-efficient", "meaning_vi": "tiết kiệm năng lượng", "evidence": "corpus"},
            {"phrase": "efficient method", "meaning_vi": "phương pháp làm việc hiệu quả", "evidence": "corpus"},
            {"phrase": "highly efficient", "meaning_vi": "cực kỳ hiệu quả, năng suất cao", "evidence": "corpus"},
            {"phrase": "cost-efficient", "meaning_vi": "tiết kiệm chi phí tối ưu", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "sufficient",
                "ipa": "/səˈfɪʃnt/",
                "meaning": "đầy đủ, vừa đủ số lượng",
                "kind": "spelling-sound",
                "difference_vi": "Efficient là đạt hiệu suất làm việc cao; sufficient là đủ về mặt số lượng hoặc điều kiện."
            }
        ],
        "confusing_meanings": [
            {
                "word": "effective",
                "meaning": "đạt được kết quả như mong muốn",
                "difference_vi": "Effective nhấn mạnh việc đạt được mục tiêu; efficient nhấn mạnh việc đạt kết quả đó với mức tiêu hao thời gian và chi phí ít nhất."
            }
        ],
        "synonyms": [
            {"word": "productive", "meaning_vi": "năng suất cao"},
            {"word": "streamlined", "meaning_vi": "tinh gọn tối ưu"}
        ],
        "examples": [
            {
                "en": "Implementing automated software makes inventory management significantly more efficient.",
                "vi": "Việc áp dụng phần mềm tự động giúp việc quản lý hàng tồn kho trở nên hiệu quả hơn đáng kể."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈfɪʃ-/. Chú ý âm /ʃ/ ('sh') và kết thúc bằng cụm phụ âm /-nt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "enhance",
        "lemma": "enhance",
        "pos": ["verb"],
        "ipa": {"us": "/ɪnˈhæns/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["marketing", "business", "training"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "enhance-1",
                "meaning_vi": "Nâng cao, gia tăng, cải thiện chất lượng hoặc giá trị",
                "note_vi": "Từ vựng trang trọng dùng trong đề xuất cải tiến sản phẩm, nâng cao kỹ năng."
            }
        ],
        "collocations": [
            {"phrase": "enhance productivity", "meaning_vi": "nâng cao năng suất làm việc", "evidence": "corpus"},
            {"phrase": "enhance customer experience", "meaning_vi": "cải thiện trải nghiệm khách hàng", "evidence": "corpus"},
            {"phrase": "enhance one's skills", "meaning_vi": "bồi dưỡng, nâng cao kỹ năng", "evidence": "corpus"},
            {"phrase": "enhance reputation", "meaning_vi": "nâng cao uy tín thương hiệu", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "enchant",
                "ipa": "/ɪnˈtʃænt/",
                "meaning": "mê hoặc, làm say mê",
                "kind": "spelling-sound",
                "difference_vi": "Enhance mang nghĩa cải thiện, tăng cường giá trị; enchant mang nghĩa làm say đắm, mê hoặc."
            }
        ],
        "confusing_meanings": [
            {
                "word": "increase",
                "meaning": "tăng về số lượng",
                "difference_vi": "Increase là tăng về mặt lượng hoặc số đo cơ học; enhance là nâng cao về mặt chất lượng, độ hấp dẫn hay uy tín."
            }
        ],
        "synonyms": [
            {"word": "improve", "meaning_vi": "cải thiện"},
            {"word": "upgrade", "meaning_vi": "nâng cấp"},
            {"word": "boost", "meaning_vi": "thúc đẩy"}
        ],
        "examples": [
            {
                "en": "Attending professional development workshops will certainly enhance your presentation skills.",
                "vi": "Tham dự các buổi hội thảo phát triển chuyên môn chắc chắn sẽ nâng cao kỹ năng thuyết trình của bạn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết hai /-ˈhæns/. Âm cuối là /s/ rõ ràng, không nuốt âm cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "evaluate",
        "lemma": "evaluate",
        "pos": ["verb"],
        "ipa": {"us": "/ɪˈvæljueɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["management", "business", "budget"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "evaluate-1",
                "meaning_vi": "Đánh giá, thẩm định kỹ lưỡng (chất lượng, hiệu quả, tính khả thi)",
                "note_vi": "Dùng khi ban lãnh đạo xem xét dự án, khảo sát phản hồi khách hàng."
            }
        ],
        "collocations": [
            {"phrase": "evaluate options", "meaning_vi": "xem xét đánh giá các phương án", "evidence": "corpus"},
            {"phrase": "evaluate performance", "meaning_vi": "đánh giá hiệu quả hoạt động", "evidence": "corpus"},
            {"phrase": "carefully evaluate", "meaning_vi": "cẩn trọng đánh giá", "evidence": "corpus"},
            {"phrase": "evaluate the results", "meaning_vi": "đánh giá các kết quả đạt được", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "evacuate",
                "ipa": "/ɪˈvækjueɪt/",
                "meaning": "sơ tán khẩn cấp",
                "kind": "spelling-sound",
                "difference_vi": "Evaluate có âm /l/ mang nghĩa đánh giá; evacuate có âm /k/ mang nghĩa sơ tán người ra khỏi nơi nguy hiểm."
            }
        ],
        "confusing_meanings": [
            {
                "word": "calculate",
                "meaning": "tính toán số học thuần túy",
                "difference_vi": "Calculate là phép tính con số cụ thể; evaluate là phân tích tổng hợp để đưa ra kết luận hoặc nhận xét giá trị."
            }
        ],
        "synonyms": [
            {"word": "assess", "meaning_vi": "thẩm định"},
            {"word": "appraise", "meaning_vi": "định giá, đánh giá"}
        ],
        "examples": [
            {
                "en": "The executive committee will carefully evaluate all vendor proposals before making a final choice.",
                "vi": "Ủy ban điều hành sẽ đánh giá cẩn thận tất cả các đề xuất từ nhà cung cấp trước khi đưa ra lựa chọn cuối cùng."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈvæl-/. Âm cuối kết thúc bằng /-ju-eɪt/, bật nhẹ âm /t/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "expand",
        "lemma": "expand",
        "pos": ["verb"],
        "ipa": {"us": "/ɪkˈspænd/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["business", "sales"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "expand-1",
                "meaning_vi": "Mở rộng quy mô (chi nhánh, thị trường, cơ sở vật chất)",
                "note_vi": "Chủ đề phát triển kinh doanh và mở rộng thị phần công ty."
            }
        ],
        "collocations": [
            {"phrase": "expand overseas", "meaning_vi": "mở rộng kinh doanh ra nước ngoài", "evidence": "corpus"},
            {"phrase": "expand the market", "meaning_vi": "mở rộng thị trường tiêu thụ", "evidence": "corpus"},
            {"phrase": "expand business operations", "meaning_vi": "mở rộng các hoạt động kinh doanh", "evidence": "corpus"},
            {"phrase": "rapidly expand", "meaning_vi": "mở rộng nhanh chóng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "expend",
                "ipa": "/ɪkˈspend/",
                "meaning": "tiêu tốn (tiền bạc, thời gian, công sức)",
                "kind": "spelling-sound",
                "difference_vi": "Expand phát âm /æ/ mang nghĩa mở rộng; expend phát âm /e/ mang nghĩa chi tiêu hoặc tiêu tốn tài nguyên."
            }
        ],
        "confusing_meanings": [
            {
                "word": "extend",
                "meaning": "kéo dài về thời gian hoặc khoảng cách",
                "difference_vi": "Extend là kéo dài về độ dài hoặc hạn chót; expand là mở rộng không gian, diện tích hoặc quy mô doanh nghiệp."
            }
        ],
        "synonyms": [
            {"word": "broaden", "meaning_vi": "mở rộng"},
            {"word": "enlarge", "meaning_vi": "phóng to, gia tăng kích thước"}
        ],
        "examples": [
            {
                "en": "The retail chain plans to expand its presence by opening ten new stores across the country.",
                "vi": "Chuỗi bán lẻ có kế hoạch mở rộng sự hiện diện bằng cách mở mười cửa hàng mới trên toàn quốc."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈspænd/. Nguyên âm /æ/ mở rộng miệng, bật dứt khoát cụm âm cuối /-nd/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "expense",
        "lemma": "expense",
        "pos": ["noun"],
        "ipa": {"us": "/ɪkˈspens/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["budget", "business", "travel"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "expense-1",
                "meaning_vi": "Chi phí, khoản tiền chi tiêu (công tác, vận hành)",
                "note_vi": "Thường gặp trong bối cảnh thanh toán công tác phí, báo cáo chi tiêu tài chính."
            }
        ],
        "collocations": [
            {"phrase": "travel expenses", "meaning_vi": "chi phí đi lại, công tác phí", "evidence": "corpus"},
            {"phrase": "reduce expenses", "meaning_vi": "cắt giảm chi phí chi tiêu", "evidence": "corpus"},
            {"phrase": "at the company's expense", "meaning_vi": "do công ty chi trả toàn bộ", "evidence": "corpus"},
            {"phrase": "expense report", "meaning_vi": "bảng báo cáo chi phí", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "expanse",
                "ipa": "/ɪkˈspæns/",
                "meaning": "dải đất rộng bao la",
                "kind": "spelling-sound",
                "difference_vi": "Expense có nguyên âm /e/ mang nghĩa chi phí; expanse có nguyên âm /æ/ mang nghĩa không gian bao la rộng lớn."
            }
        ],
        "confusing_meanings": [
            {
                "word": "price",
                "meaning": "giá bán niêm yết của hàng hóa",
                "difference_vi": "Price là mức giá đề ra cho sản phẩm; expense là số tiền thực tế bạn đã phải chi trả trong quá trình sinh hoạt hoặc làm việc."
            }
        ],
        "synonyms": [
            {"word": "expenditure", "meaning_vi": "khoản chi tiêu"},
            {"word": "cost", "meaning_vi": "chi phí"}
        ],
        "examples": [
            {
                "en": "Employees must submit all receipts along with their travel expense report by Friday afternoon.",
                "vi": "Nhân viên phải nộp tất cả các hóa đơn kèm theo báo cáo công tác phí trước chiều thứ Sáu."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈspens/. Âm cuối là /s/ xì nhẹ rõ ràng, tránh đọc nhầm thành âm đuôi 'x'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "fluctuate",
        "lemma": "fluctuate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈflʌktʃueɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["budget", "sales", "business"],
        "speaking_use": ["respond-with-info", "express-opinion"],
        "senses": [
            {
                "id": "fluctuate-1",
                "meaning_vi": "Biến động, dao động lên xuống thất thường (giá cả, tỉ giá, doanh số)",
                "note_vi": "Rất hay gặp khi mô tả biểu đồ số liệu hoặc tình hình thị trường tài chính."
            }
        ],
        "collocations": [
            {"phrase": "fluctuate wildly", "meaning_vi": "biến động dữ dội", "evidence": "corpus"},
            {"phrase": "prices fluctuate", "meaning_vi": "giá cả dao động thất thường", "evidence": "corpus"},
            {"phrase": "fluctuate between", "meaning_vi": "dao động trong khoảng từ... đến...", "evidence": "corpus"},
            {"phrase": "currency fluctuation", "meaning_vi": "sự biến động tỉ giá ngoại tệ", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "frustrate",
                "ipa": "/ˈfrʌstreɪt/",
                "meaning": "gây bực bội, thất vọng",
                "kind": "spelling-sound",
                "difference_vi": "Fluctuate là biến động số liệu; frustrate mang nghĩa làm ai đó nản lòng hoặc thất vọng."
            }
        ],
        "confusing_meanings": [
            {
                "word": "change",
                "meaning": "thay đổi nói chung",
                "difference_vi": "Change là sự biến đổi theo hướng bất kỳ; fluctuate là chuyển động lên xuống không ngừng quanh một mức trung bình."
            }
        ],
        "synonyms": [
            {"word": "vary", "meaning_vi": "thay đổi dao động"},
            {"word": "swing", "meaning_vi": "dao động mạnh"}
        ],
        "examples": [
            {
                "en": "Fuel prices continued to fluctuate significantly throughout the entire summer season.",
                "vi": "Giá nhiên liệu tiếp tục biến động đáng kể trong suốt toàn bộ mùa hè."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈflʌk-/. Âm giữa là /tʃu/ ('ch'), âm đuôi /-eɪt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "implement",
        "lemma": "implement",
        "pos": ["verb"],
        "ipa": {"us": "/ˈɪmplɪment/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["work", "management", "technology"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "implement-1",
                "meaning_vi": "Triển khai thực hiện, áp dụng (kế hoạch, chính sách, phần mềm mới)",
                "note_vi": "Từ chìa khóa trong đề xuất giải pháp cải tiến hiệu quả văn phòng."
            }
        ],
        "collocations": [
            {"phrase": "implement a policy", "meaning_vi": "áp dụng một chính sách", "evidence": "corpus"},
            {"phrase": "implement changes", "meaning_vi": "thực thi các thay đổi", "evidence": "corpus"},
            {"phrase": "successfully implement", "meaning_vi": "triển khai thành công tốt đẹp", "evidence": "corpus"},
            {"phrase": "implement a plan", "meaning_vi": "thực hiện một kế hoạch", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "compliment",
                "ipa": "/ˈkɑːmplɪmənt/",
                "meaning": "lời khen ngợi",
                "kind": "spelling-sound",
                "difference_vi": "Implement là triển khai thực thi kế hoạch; compliment là lời khen ngợi hoặc tán dương."
            }
        ],
        "confusing_meanings": [
            {
                "word": "plan",
                "meaning": "lập kế hoạch dự kiến",
                "difference_vi": "Plan là vạch ra ý định trên giấy; implement là bắt tay vào thực hiện cụ thể trong thực tế."
            }
        ],
        "synonyms": [
            {"word": "carry out", "meaning_vi": "tiến hành"},
            {"word": "execute", "meaning_vi": "thi hành"}
        ],
        "examples": [
            {
                "en": "The management decided to implement a hybrid working policy starting next month.",
                "vi": "Ban lãnh đạo đã quyết định triển khai chính sách làm việc kết hợp (tại nhà và văn phòng) bắt đầu từ tháng tới."
            }
        ],
        "pronunciation_tips_vi": "Khi là động từ, trọng âm rơi vào âm tiết đầu /ˈɪm-/. Âm cuối /-ment/ bật rõ âm /t/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "inspect",
        "lemma": "inspect",
        "pos": ["verb"],
        "ipa": {"us": "/ɪnˈspekt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["manufacturing", "equipment", "work"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "inspect-1",
                "meaning_vi": "Thanh tra, kiểm tra kỹ lưỡng (để phát hiện lỗi hoặc đảm bảo an toàn)",
                "note_vi": "Thường gặp trong miêu tả tranh Part 2 (kỹ sư kiểm tra máy móc) hoặc an toàn lao động."
            }
        ],
        "collocations": [
            {"phrase": "inspect the equipment", "meaning_vi": "kiểm tra máy móc thiết bị", "evidence": "corpus"},
            {"phrase": "thoroughly inspect", "meaning_vi": "thanh tra, kiểm tra toàn diện", "evidence": "corpus"},
            {"phrase": "safety inspection", "meaning_vi": "đợt thanh tra an toàn", "evidence": "corpus"},
            {"phrase": "inspect for damage", "meaning_vi": "kiểm tra xem có hư hỏng không", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "expect",
                "ipa": "/ɪkˈspekt/",
                "meaning": "kỳ vọng, mong đợi",
                "kind": "spelling-sound",
                "difference_vi": "Inspect có âm /n/ (/ɪnˈspekt/) nghĩa là kiểm tra thanh tra; expect (/ɪkˈspekt/) nghĩa là trông mong, kỳ vọng."
            }
        ],
        "confusing_meanings": [
            {
                "word": "look at",
                "meaning": "nhìn ngắm bình thường",
                "difference_vi": "Look at là nhìn ngắm thông thường; inspect là xem xét kỹ từng chi tiết với mục đích chuyên môn phát hiện lỗi."
            }
        ],
        "synonyms": [
            {"word": "examine", "meaning_vi": "xem xét cẩn thận"},
            {"word": "check", "meaning_vi": "kiểm tra"}
        ],
        "examples": [
            {
                "en": "Technicians will inspect the ventilation system to ensure all safety standards are met.",
                "vi": "Các kỹ thuật viên sẽ kiểm tra hệ thống thông gió để đảm bảo đáp ứng đầy đủ mọi tiêu chuẩn an toàn."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈspekt/. Chú ý phát âm rõ cụm phụ âm cuối /-kt/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "interview",
        "lemma": "interview",
        "pos": ["noun", "verb"],
        "ipa": {"us": "/ˈɪntərvjuː/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "work", "media"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "interview-1",
                "meaning_vi": "Buổi phỏng vấn xin việc / Phỏng vấn ứng viên",
                "note_vi": "Xuất hiện với tần suất cực cao trong chủ đề tuyển dụng và nhân sự."
            }
        ],
        "collocations": [
            {"phrase": "job interview", "meaning_vi": "buổi phỏng vấn xin việc", "evidence": "corpus"},
            {"phrase": "conduct an interview", "meaning_vi": "tiến hành buổi phỏng vấn", "evidence": "corpus"},
            {"phrase": "interview candidates", "meaning_vi": "phỏng vấn các ứng viên", "evidence": "corpus"},
            {"phrase": "schedule an interview", "meaning_vi": "sắp xếp lịch phỏng vấn", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "overview",
                "ipa": "/ˈoʊvərvjuː/",
                "meaning": "cái nhìn tổng quan",
                "kind": "spelling-sound",
                "difference_vi": "Interview là buổi phỏng vấn; overview là bảng tóm tắt hoặc cái nhìn tổng quan về một vấn đề."
            }
        ],
        "confusing_meanings": [
            {
                "word": "meeting",
                "meaning": "cuộc họp bàn bạc chung",
                "difference_vi": "Meeting là cuộc họp nội bộ; interview là cuộc đối thoại trang trọng nhằm đánh giá trình độ một người."
            }
        ],
        "synonyms": [
            {"word": "consultation", "meaning_vi": "buổi trao đổi ý kiến"}
        ],
        "examples": [
            {
                "en": "Candidates who pass the initial screening will be invited for a face-to-face interview next week.",
                "vi": "Các ứng viên vượt qua vòng sàng lọc ban đầu sẽ được mời tham dự buổi phỏng vấn trực tiếp vào tuần tới."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈɪn-/. Trong tiếng Anh Mỹ, người bản xứ thường phát âm lướt âm /t/ thành /ˈɪnərvjuː/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "inventory",
        "lemma": "inventory",
        "pos": ["noun"],
        "ipa": {"us": "/ˈɪnvəntɔːri/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["logistics", "shopping", "sales"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "inventory-1",
                "meaning_vi": "Hàng tồn kho, danh mục kiểm kê hàng hóa",
                "note_vi": "Chủ đề kho bãi, kiểm kê hàng hóa định kỳ và kiểm soát chuỗi cung ứng."
            }
        ],
        "collocations": [
            {"phrase": "take inventory", "meaning_vi": "tiến hành kiểm kê hàng hóa", "evidence": "corpus"},
            {"phrase": "in inventory", "meaning_vi": "còn hàng trong kho", "evidence": "corpus"},
            {"phrase": "inventory management", "meaning_vi": "việc quản lý hàng tồn kho", "evidence": "corpus"},
            {"phrase": "out of inventory", "meaning_vi": "hết sạch hàng trong kho", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "invention",
                "ipa": "/ɪnˈvenʃn/",
                "meaning": "sáng chế, phát minh",
                "kind": "spelling-sound",
                "difference_vi": "Inventory là việc kiểm kê hoặc lượng hàng tồn kho; invention là sáng chế phát minh mới."
            }
        ],
        "confusing_meanings": [
            {
                "word": "stock",
                "meaning": "lượng hàng hóa sẵn có để bán",
                "difference_vi": "Stock là hàng hóa trưng bày sẵn sàng bán; inventory là toàn bộ danh mục tài sản hàng hóa bao gồm cả vật liệu lưu kho."
            }
        ],
        "synonyms": [
            {"word": "stock", "meaning_vi": "kho hàng"},
            {"word": "merchandise", "meaning_vi": "hàng hóa"}
        ],
        "examples": [
            {
                "en": "The store will temporarily close early this evening so staff can take the annual inventory.",
                "vi": "Cửa hàng sẽ tạm thời đóng cửa sớm vào tối nay để nhân viên có thể tiến hành kiểm kê hàng hóa thường niên."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈɪn-/. Giọng Mỹ đọc rõ âm /-tɔːri/, không nuốt âm.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "obligation",
        "lemma": "obligation",
        "pos": ["noun"],
        "ipa": {"us": "/ˌɑːblɪˈɡeɪʃn/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["contracts", "business", "legal"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "obligation-1",
                "meaning_vi": "Nghĩa vụ pháp lý, bổn phận bắt buộc theo hợp đồng",
                "note_vi": "Dùng khi nói về trách nhiệm pháp lý phải thực hiện theo thỏa thuận hợp tác."
            }
        ],
        "collocations": [
            {"phrase": "fulfill an obligation", "meaning_vi": "hoàn thành nghĩa vụ cam kết", "evidence": "corpus"},
            {"phrase": "contractual obligation", "meaning_vi": "nghĩa vụ theo điều khoản hợp đồng", "evidence": "corpus"},
            {"phrase": "under no obligation", "meaning_vi": "hoàn toàn không bị ràng buộc bắt buộc", "evidence": "corpus"},
            {"phrase": "legal obligation", "meaning_vi": "nghĩa vụ pháp lý", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "allegation",
                "ipa": "/ˌæləˈɡeɪʃn/",
                "meaning": "lời cáo buộc",
                "kind": "spelling-sound",
                "difference_vi": "Obligation là nghĩa vụ bổn phận; allegation là lời cáo buộc chưa được chứng minh."
            }
        ],
        "confusing_meanings": [
            {
                "word": "duty",
                "meaning": "trách nhiệm bổn phận nói chung",
                "difference_vi": "Duty là nhiệm vụ chung theo lương tâm hoặc chức vụ; obligation nhấn mạnh nghĩa vụ có tính ràng buộc pháp lý cụ thể."
            }
        ],
        "synonyms": [
            {"word": "responsibility", "meaning_vi": "trách nhiệm"},
            {"word": "commitment", "meaning_vi": "sự cam kết"}
        ],
        "examples": [
            {
                "en": "Both parties have a clear contractual obligation to maintain strict confidentiality of project data.",
                "vi": "Cả hai bên đều có nghĩa vụ rõ ràng theo hợp đồng là phải giữ bí mật nghiêm ngặt đối với dữ liệu dự án."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm chính rơi vào âm tiết thứ ba /-ˈɡeɪ-/. Âm đầu là /ɑː/ mở rộng, đuôi /-ʃn/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "profit",
        "lemma": "profit",
        "pos": ["noun"],
        "ipa": {"us": "/ˈprɑːfɪt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["budget", "banking", "business"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "profit-1",
                "meaning_vi": "Lợi nhuận kinh doanh, tiền lãi thu được",
                "note_vi": "Từ trọng tâm trong các báo cáo tài chính hàng quý, hàng năm của doanh nghiệp."
            }
        ],
        "collocations": [
            {"phrase": "net profit", "meaning_vi": "lợi nhuận ròng (sau thuế)", "evidence": "corpus"},
            {"phrase": "generate a profit", "meaning_vi": "tạo ra lợi nhuận", "evidence": "corpus"},
            {"phrase": "profit margin", "meaning_vi": "biên độ lợi nhuận", "evidence": "corpus"},
            {"phrase": "record profit", "meaning_vi": "lợi nhuận kỷ lục", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "prophet",
                "ipa": "/ˈprɑːfɪt/",
                "meaning": "nhà tiên tri",
                "kind": "spelling-sound",
                "difference_vi": "Hai từ đồng âm dị nghĩa: profit là tiền lãi kinh doanh; prophet là nhà tiên tri trong tôn giáo."
            }
        ],
        "confusing_meanings": [
            {
                "word": "revenue",
                "meaning": "tổng doanh thu chưa trừ chi phí",
                "difference_vi": "Revenue là tổng số tiền bán được; profit là phần tiền lãi thực sự còn lại sau khi trừ toàn bộ chi phí."
            }
        ],
        "synonyms": [
            {"word": "earnings", "meaning_vi": "tiền kiếm được"},
            {"word": "financial gain", "meaning_vi": "khoản thu được"}
        ],
        "examples": [
            {
                "en": "Thanks to strong overseas sales, the company reported a twenty percent increase in quarterly profits.",
                "vi": "Nhờ doanh số bán hàng ở nước ngoài tăng mạnh, công ty đã báo cáo mức tăng lợi nhuận hàng quý lên đến hai mươi phần trăm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈprɑː-/. Âm đuôi /-fɪt/ bật rõ âm /t/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "recruit",
        "lemma": "recruit",
        "pos": ["verb", "noun"],
        "ipa": {"us": "/rɪˈkruːt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "work"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "recruit-1",
                "meaning_vi": "Tuyển dụng nhân sự mới / Tân binh, nhân viên mới tuyển",
                "note_vi": "Rất hay gặp trong chủ đề thu hút nhân tài và mở rộng đội ngũ nhân viên."
            }
        ],
        "collocations": [
            {"phrase": "actively recruit", "meaning_vi": "tích cực tìm kiếm và tuyển dụng", "evidence": "corpus"},
            {"phrase": "recruit talented staff", "meaning_vi": "tuyển mộ đội ngũ nhân sự tài năng", "evidence": "corpus"},
            {"phrase": "new recruits", "meaning_vi": "các nhân viên mới được tuyển dụng", "evidence": "corpus"},
            {"phrase": "recruitment agency", "meaning_vi": "công ty môi giới tuyển dụng", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "rescue",
                "ipa": "/ˈreskjuː/",
                "meaning": "giải cứu, cứu hộ",
                "kind": "spelling-sound",
                "difference_vi": "Recruit là tuyển mộ nhân sự; rescue mang nghĩa cứu thoát ai đó khỏi tai nạn hoặc hiểm nguy."
            }
        ],
        "confusing_meanings": [
            {
                "word": "hire",
                "meaning": "thuê người làm việc",
                "difference_vi": "Hire là quyết định thuê một cá nhân cụ thể; recruit là toàn bộ chiến dịch tìm kiếm và chiêu mộ nhân tài."
            }
        ],
        "synonyms": [
            {"word": "employ", "meaning_vi": "thuê tuyển"},
            {"word": "enlist", "meaning_vi": "chiêu mộ"}
        ],
        "examples": [
            {
                "en": "The firm is actively recruiting experienced software engineers to join its artificial intelligence division.",
                "vi": "Công ty đang tích cực tuyển dụng các kỹ sư phần mềm giàu kinh nghiệm để gia nhập bộ phận trí tuệ nhân tạo."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈkruːt/. Chú ý nguyên âm dài /uː/ kéo dài và bật âm /t/ cuối.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "requirement",
        "lemma": "requirement",
        "pos": ["noun"],
        "ipa": {"us": "/rɪˈkwaɪərmənt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "training", "contracts"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "requirement-1",
                "meaning_vi": "Yêu cầu bắt buộc, tiêu chuẩn cần đáp ứng",
                "note_vi": "Thường thấy trong bản mô tả công việc (job description) hoặc điều kiện tham gia khóa học."
            }
        ],
        "collocations": [
            {"phrase": "meet the requirements", "meaning_vi": "đáp ứng đầy đủ các yêu cầu", "evidence": "corpus"},
            {"phrase": "minimum requirement", "meaning_vi": "yêu cầu tối thiểu", "evidence": "corpus"},
            {"phrase": "mandatory requirement", "meaning_vi": "yêu cầu mang tính bắt buộc", "evidence": "corpus"},
            {"phrase": "fulfill requirements", "meaning_vi": "hoàn thành các tiêu chuẩn đặt ra", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "retirement",
                "ipa": "/rɪˈtaɪərmənt/",
                "meaning": "sự nghỉ hưu",
                "kind": "spelling-sound",
                "difference_vi": "Requirement có âm /kw/ mang nghĩa yêu cầu; retirement có âm /t/ mang nghĩa sự về hưu."
            }
        ],
        "confusing_meanings": [
            {
                "word": "recommendation",
                "meaning": "lời khuyên, đề xuất",
                "difference_vi": "Recommendation chỉ là lời gợi ý không bắt buộc; requirement là điều kiện tiên quyết bắt buộc phải có."
            }
        ],
        "synonyms": [
            {"word": "prerequisite", "meaning_vi": "điều kiện tiên quyết"},
            {"word": "specification", "meaning_vi": "tiêu chuẩn kỹ thuật"}
        ],
        "examples": [
            {
                "en": "Fluency in English and at least two years of sales experience are minimum requirements for this position.",
                "vi": "Thành thạo tiếng Anh và có ít nhất hai năm kinh nghiệm bán hàng là những yêu cầu tối thiểu cho vị trí này."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈkwaɪ-/. Chú ý âm /kw/ kết hợp nguyên âm đôi /aɪ/, đuôi /-mənt/ nhẹ.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "resolve",
        "lemma": "resolve",
        "pos": ["verb"],
        "ipa": {"us": "/rɪˈzɑːlv/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["customer-service", "management", "work"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "resolve-1",
                "meaning_vi": "Giải quyết dứt điểm (vấn đề khó khăn, mâu thuẫn, khiếu nại)",
                "note_vi": "Xuất hiện liên tục khi bàn về phương án xử lý sự cố khách hàng hoặc xung đột công sở."
            }
        ],
        "collocations": [
            {"phrase": "resolve complaints", "meaning_vi": "giải quyết dứt điểm các phàn nàn", "evidence": "corpus"},
            {"phrase": "resolve conflicts", "meaning_vi": "giải quyết xung đột mâu thuẫn", "evidence": "corpus"},
            {"phrase": "quickly resolve", "meaning_vi": "nhanh chóng giải quyết thỏa đáng", "evidence": "corpus"},
            {"phrase": "resolve an issue", "meaning_vi": "xử lý một vấn đề nan giải", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "revolve",
                "ipa": "/rɪˈvɑːlv/",
                "meaning": "quay tròn quanh một trục",
                "kind": "spelling-sound",
                "difference_vi": "Resolve mang nghĩa giải quyết vấn đề; revolve mang nghĩa chuyển động quay tròn xung quanh."
            }
        ],
        "confusing_meanings": [
            {
                "word": "solve",
                "meaning": "tìm ra đáp án của bài toán/câu đố",
                "difference_vi": "Solve là tìm ra lời giải chính xác; resolve là dàn xếp hòa giải ổn thỏa một mâu thuẫn hoặc tranh chấp rắc rối."
            }
        ],
        "synonyms": [
            {"word": "settle", "meaning_vi": "dàn xếp"},
            {"word": "fix", "meaning_vi": "khắc phục"},
            {"word": "handle", "meaning_vi": "xử lý"}
        ],
        "examples": [
            {
                "en": "The customer service team worked diligently to resolve the billing issue before the weekend.",
                "vi": "Đội ngũ chăm sóc khách hàng đã làm việc tận tụy để giải quyết dứt điểm sự cố hóa đơn trước kỳ nghỉ cuối tuần."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết thứ hai /-ˈzɑːlv/. Chú ý âm /z/ ở giữa (không đọc thành /s/) và âm cuối /lv/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "revenue",
        "lemma": "revenue",
        "pos": ["noun"],
        "ipa": {"us": "/ˈrevənuː/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["budget", "sales", "business"],
        "speaking_use": ["respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "revenue-1",
                "meaning_vi": "Doanh thu (tổng số tiền công ty thu về từ bán hàng/dịch vụ)",
                "note_vi": "Từ trọng điểm trong báo cáo doanh thu tài chính và đánh giá tăng trưởng."
            }
        ],
        "collocations": [
            {"phrase": "annual revenue", "meaning_vi": "tổng doanh thu hàng năm", "evidence": "corpus"},
            {"phrase": "boost revenue", "meaning_vi": "thúc đẩy gia tăng doanh thu", "evidence": "corpus"},
            {"phrase": "generate revenue", "meaning_vi": "tạo ra nguồn doanh thu", "evidence": "corpus"},
            {"phrase": "revenue growth", "meaning_vi": "sự tăng trưởng doanh thu", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "avenue",
                "ipa": "/ˈævənuː/",
                "meaning": "đại lộ, con đường lớn",
                "kind": "spelling-sound",
                "difference_vi": "Revenue là doanh thu tiền bạc; avenue là đại lộ giao thông hoặc con đường tiếp cận."
            }
        ],
        "confusing_meanings": [
            {
                "word": "profit",
                "meaning": "tiền lãi ròng",
                "difference_vi": "Revenue là tổng thu nhập gộp ban đầu; profit là tiền lãi sau khi trừ đi tất cả chi phí sản xuất và thuế."
            }
        ],
        "synonyms": [
            {"word": "turnover", "meaning_vi": "doanh số quay vòng"},
            {"word": "income", "meaning_vi": "thu nhập"}
        ],
        "examples": [
            {
                "en": "The company's annual revenue surpassed ten million dollars for the first time in its history.",
                "vi": "Doanh thu hàng năm của công ty đã lần đầu tiên trong lịch sử vượt qua mốc mười triệu đô la."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈrev-/. Giọng Mỹ đọc đuôi là /-nuː/ (âm 'u' dài), không đọc thành 'n-iu'.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "shipment",
        "lemma": "shipment",
        "pos": ["noun"],
        "ipa": {"us": "/ˈʃɪpmənt/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["logistics", "transport", "manufacturing"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "shipment-1",
                "meaning_vi": "Lô hàng vận chuyển, chuyến hàng được gửi đi",
                "note_vi": "Rất hay gặp trong Part 1 và Part 4 khi thông báo trạng thái hàng hóa gửi đi hoặc hàng bị chậm trễ."
            }
        ],
        "collocations": [
            {"phrase": "track a shipment", "meaning_vi": "theo dõi hành trình đơn hàng", "evidence": "corpus"},
            {"phrase": "receive a shipment", "meaning_vi": "tiếp nhận một lô hàng", "evidence": "corpus"},
            {"phrase": "delay the shipment", "meaning_vi": "hoãn chuyến giao hàng", "evidence": "corpus"},
            {"phrase": "incoming shipment", "meaning_vi": "lô hàng đang được chuyển tới", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "shipyard",
                "ipa": "/ˈʃɪpjɑːrd/",
                "meaning": "xưởng đóng tàu",
                "kind": "spelling-sound",
                "difference_vi": "Shipment là lô hàng bưu kiện được gửi đi; shipyard là xưởng đóng tàu thủy."
            }
        ],
        "confusing_meanings": [
            {
                "word": "cargo",
                "meaning": "hàng hóa chở trên tàu xe",
                "difference_vi": "Cargo là hàng hóa chở khối lượng lớn trên tàu/máy bay; shipment là một kiện hàng hoặc chuyến hàng cụ thể đã lên đơn gửi đi."
            }
        ],
        "synonyms": [
            {"word": "delivery", "meaning_vi": "kiện hàng giao"},
            {"word": "consignment", "meaning_vi": "lô hàng ủy gửi"}
        ],
        "examples": [
            {
                "en": "You can track the real-time status of your international shipment by entering the tracking number online.",
                "vi": "Bạn có thể theo dõi trạng thái theo thời gian thực của lô hàng quốc tế bằng cách nhập mã vận đơn trực tuyến."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈʃɪp-/. Âm đầu là /ʃ/ cong môi, đuôi /-mənt/ dứt khoát.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "terminate",
        "lemma": "terminate",
        "pos": ["verb"],
        "ipa": {"us": "/ˈtɜːrmɪneɪt/"},
        "level": {"cefr": "B2", "band": "target", "basis": "editorial"},
        "topics": ["contracts", "hiring", "business"],
        "speaking_use": ["respond-to-questions", "express-opinion"],
        "senses": [
            {
                "id": "terminate-1",
                "meaning_vi": "Chấm dứt (hợp đồng, thỏa thuận, quan hệ lao động)",
                "note_vi": "Thuật ngữ pháp lý chính thức khi kết thúc sớm một cam kết hoặc hợp đồng."
            }
        ],
        "collocations": [
            {"phrase": "terminate a contract", "meaning_vi": "chấm dứt một hợp đồng", "evidence": "corpus"},
            {"phrase": "terminate employment", "meaning_vi": "chấm dứt quan hệ việc làm", "evidence": "corpus"},
            {"phrase": "unilaterally terminate", "meaning_vi": "đơn phương chấm dứt hợp đồng", "evidence": "corpus"},
            {"phrase": "right to terminate", "meaning_vi": "quyền được đơn phương chấm dứt", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "determine",
                "ipa": "/dɪˈtɜːrmɪn/",
                "meaning": "xác định, quyết định kiên định",
                "kind": "spelling-sound",
                "difference_vi": "Terminate là kết thúc/chấm dứt hợp đồng; determine là xác định thông tin hoặc quyết tâm làm gì."
            }
        ],
        "confusing_meanings": [
            {
                "word": "stop",
                "meaning": "dừng lại tạm thời",
                "difference_vi": "Stop là dừng hành động thông thường; terminate là hành động pháp lý hủy bỏ/chấm dứt vĩnh viễn hiệu lực hợp đồng."
            }
        ],
        "synonyms": [
            {"word": "end", "meaning_vi": "kết thúc"},
            {"word": "cancel", "meaning_vi": "hủy bỏ"},
            {"word": "conclude", "meaning_vi": "khép lại"}
        ],
        "examples": [
            {
                "en": "The landlord has the legal right to terminate the lease agreement if the rent is unpaid for sixty days.",
                "vi": "Chủ nhà có quyền hợp pháp chấm dứt hợp đồng thuê nếu tiền thuê nhà không được thanh toán trong vòng sáu mươi ngày."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈtɜːr-/. Lưu ý âm /ɜːr/ giọng Mỹ cong lưỡi, âm đuôi /-neɪt/ bật rõ âm /t/.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "vacancy",
        "lemma": "vacancy",
        "pos": ["noun"],
        "ipa": {"us": "/ˈveɪkənsi/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["hiring", "hotels", "work"],
        "speaking_use": ["read-aloud", "respond-with-info", "respond-to-questions"],
        "senses": [
            {
                "id": "vacancy-1",
                "meaning_vi": "Vị trí tuyển dụng còn trống / Phòng khách sạn còn trống",
                "note_vi": "Gặp rất nhiều trong thông báo tuyển dụng và bảng thông báo khách sạn (Part 1, Part 4)."
            }
        ],
        "collocations": [
            {"phrase": "job vacancy", "meaning_vi": "vị trí công việc còn trống", "evidence": "corpus"},
            {"phrase": "fill a vacancy", "meaning_vi": "tuyển người lấp vào vị trí trống", "evidence": "corpus"},
            {"phrase": "no vacancies", "meaning_vi": "biển báo hết chỗ / hết phòng trống", "evidence": "corpus"},
            {"phrase": "current vacancy", "meaning_vi": "vị trí đang tuyển dụng hiện tại", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "vacation",
                "ipa": "/veɪˈkeɪʃn/",
                "meaning": "kỳ nghỉ lễ, chuyến du lịch",
                "kind": "spelling-sound",
                "difference_vi": "Vacancy có đuôi /-kənsi/ chỉ chỗ trống/vị trí tuyển dụng; vacation có đuôi /-keɪʃn/ chỉ kỳ nghỉ."
            }
        ],
        "confusing_meanings": [
            {
                "word": "opening",
                "meaning": "cơ hội việc làm đang mở",
                "difference_vi": "Cả hai từ tương đồng, tuy nhiên vacancy trang trọng hơn và thường dùng trong văn bản thông báo chính thức."
            }
        ],
        "synonyms": [
            {"word": "opening", "meaning_vi": "vị trí mở"},
            {"word": "available position", "meaning_vi": "vị trí đang có sẵn"}
        ],
        "examples": [
            {
                "en": "The marketing department announced an immediate job vacancy for an experienced digital copywriter.",
                "vi": "Phòng tiếp thị đã thông báo một vị trí việc làm tuyển gấp cho một chuyên viên viết nội dung số giàu kinh nghiệm."
            }
        ],
        "pronunciation_tips_vi": "Trọng âm rơi vào âm tiết đầu /ˈveɪ-/. Âm giữa là schwa /-kən-/, kết thúc bằng /-si/ nhẹ nhàng.",
        "review": {
            "status": "ai_cross_checked",
            "checked_by": ["model-b", "cmudict"],
            "checked_at": "2026-10-10",
            "sources": ["oxford-ref", "cambridge-ref", "cmudict"]
        }
    },
    {
        "schema_version": 2,
        "id": "warehouse",
        "lemma": "warehouse",
        "pos": ["noun"],
        "ipa": {"us": "/ˈwerhaʊs/"},
        "level": {"cefr": "B1", "band": "core", "basis": "editorial"},
        "topics": ["logistics", "manufacturing", "storage"],
        "speaking_use": ["describe-picture", "respond-to-questions"],
        "senses": [
            {
                "id": "warehouse-1",
                "meaning_vi": "Nhà kho lưu trữ hàng hóa và quản lý phân phối",
                "note_vi": "Rất hay gặp trong tranh miêu tả kho hàng (Part 2: xe nâng hàng, công nhân bốc xếp thùng carton)."
            }
        ],
        "collocations": [
            {"phrase": "warehouse worker", "meaning_vi": "công nhân kho bãi", "evidence": "corpus"},
            {"phrase": "store in a warehouse", "meaning_vi": "lưu trữ trong nhà kho", "evidence": "corpus"},
            {"phrase": "warehouse supervisor", "meaning_vi": "người giám sát kho hàng", "evidence": "corpus"},
            {"phrase": "central warehouse", "meaning_vi": "nhà kho tổng trung tâm", "evidence": "corpus"}
        ],
        "confused_words": [
            {
                "word": "farmhouse",
                "ipa": "/ˈfɑːrmhaʊs/",
                "meaning": "nhà ở trang trại",
                "kind": "spelling-sound",
                "difference_vi": "Warehouse là nhà kho chứa hàng hóa; farmhouse là nhà ở tại nông trại nông nghiệp."
            }
        ],
        "confusing_meanings": [
            {
                "word": "storehouse",
                "meaning": "nhà kho nhỏ chứa đồ linh tinh",
                "difference_vi": "Storehouse là kho chứa đồ thông thường; warehouse là kho vận công nghiệp quy mô lớn trong chuỗi phân phối hàng hóa."
            }
        ],
        "synonyms": [
            {"word": "storage facility", "meaning_vi": "cơ sở lưu trữ"},
            {"word": "depot", "meaning_vi": "trạm chứa hàng"}
        ],
        "examples": [
            {
                "en": "All newly manufactured electronics are stored in a climate-controlled warehouse before distribution.",
                "vi": "Tất cả các thiết bị điện tử mới sản xuất đều được lưu trữ trong nhà kho có kiểm soát nhiệt độ trước khi phân phối."
            }
        ],
        "pronunciation_tips_vi": "Từ ghép gồm hai từ: /ˈwer/ + /haʊs/. Trọng âm rơi vào âm tiết đầu /ˈwer-/. Lưu ý âm cuối là /s/ (không đọc thành /z/ khi là danh từ).",
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
