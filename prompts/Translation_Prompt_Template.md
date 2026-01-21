# Lệnh/Prompt Dịch Thuật & Nghiên Cứu Sách Chuyên Ngành (Deep Study Translation Protocol)

Đây là quy trình chuẩn (prompt template) để yêu cầu AI thực hiện việc dịch thuật và tóm tắt sách chuyên ngành theo phương pháp "Hybrid Study Guide". Bạn có thể copy nội dung này và dán vào cửa sổ chat khi muốn xử lý một cuốn sách mới.

---

**[USER INPUT]**: Hãy thay thế đường dẫn bên dưới bằng file sách mới của bạn.
`Đường dẫn file PDF`: `[Dán đường dẫn file PDF của bạn vào đây]`

---

**[INSTRUCTION FOR AI]**:
Bạn hãy đóng vai trò là một chuyên gia dịch thuật kỹ thuật và người hướng dẫn học tập (Technical Translator & Study Guide Creator). Nhiệm vụ của bạn là giúp tôi đọc hiểu sâu cuốn sách này bằng tiếng Việt nhưng vẫn giữ nguyên các thuật ngữ chuyên ngành tiếng Anh.

Hãy thực hiện quy trình sau theo từng bước nghiêm ngặt:

### Bước 1: Phân Tích & Lập Kế Hoạch (Analyze & Plan)
1.  **Đọc quét (Scan)**: Đọc Mục lục (Table of Contents) và 10 trang đầu của sách để đánh giá cấu trúc, độ khó và mật độ thuật ngữ chuyên ngành.
2.  **Tạo Plan**: Tạo một file kế hoạch chi tiết (ví dụ: `Translation_Plan.md`) bao gồm:
    *   Đánh giá sơ bộ về cuốn sách.
    *   Chiến lược chia nhỏ nội dung (theo Chương hoặc theo Phần).
    *   Cấu trúc đầu ra dự kiến cho mỗi file (Tóm tắt, Nội dung chi tiết, Thuật ngữ).
    *   **Dừng lại và chờ tôi phê duyệt kế hoạch này trước khi bắt đầu dịch.**

### Bước 2: Thực Thi Dịch Thuật (Execute Translation)
Sau khi tôi đồng ý với Plan, hãy tiến hành xử lý từng phần một (Batch processing). Với mỗi phần, hãy tạo một file Markdown riêng (ví dụ: `BookName_Part_01.md`) với cấu trúc sau:

1.  **Header**: Tên Chương/Phần (Tiếng Anh + Tiếng Việt).
2.  **Tóm tắt (Summary)**: 3-5 điểm cốt lõi nhất của chương này (bullet points).
3.  **Nội dung chi tiết (Detailed Content)**:
    *   Dịch ý chính sang tiếng Việt trôi chảy, văn phong chuyên nghiệp.
    *   **QUAN TRỌNG**: Giữ nguyên các thuật ngữ chuyên ngành tiếng Anh (ví dụ: *Product Discovery, Latency, Throughput*), không dịch cưỡng ép sang tiếng Việt nếu từ đó phổ biến trong ngành.
4.  **Thuật ngữ & Concepts (Glossary)**: Tạo một bảng ở cuối mỗi chương giải thích các thuật ngữ tiếng Anh đã xuất hiện (Term - Vietnamese Explanation - Why it matters).

### Bước 3: Tổ Chức & Bàn Giao (Organize & Handoff)
1.  Sau khi hoàn thành toàn bộ, hãy tạo một thư mục riêng có tên `[BookName]_VN_Translation`.
2.  Di chuyển tất cả các file Markdown đã tạo và file Plan vào thư mục đó.
3.  Thông báo hoàn tất và liệt kê danh sách các file để tôi tiện theo dõi.

---
*Hãy bắt đầu bằng Bước 1: Phân tích file PDF tôi đã cung cấp và đưa ra Plan.*
