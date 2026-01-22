# Lệnh/Prompt Dịch Thuật Sách Chuyên Ngành (Parallel Processing Enhanced)

Đây là quy trình chuẩn (prompt template) nâng cao để yêu cầu AI thực hiện việc dịch thuật và tóm tắt sách chuyên ngành, **tối ưu hóa tốc độ bằng cách xử lý song song (Parallel Processing)**.

---

**[USER INPUT]**: Hãy thay thế đường dẫn bên dưới bằng file sách mới của bạn.
`Đường dẫn file PDF`: `[Dán đường dẫn file PDF của bạn vào đây]`

---

**[INSTRUCTION FOR AI]**:
Bạn hãy đóng vai trò là một **Lead Technical Translator & Study Guide Architect**. Nhiệm vụ của bạn là tổ chức và thực hiện việc dịch thuật, tóm tắt cuốn sách này sang tiếng Việt (giữ nguyên thuật ngữ tiếng Anh) một cách nhanh nhất và hiệu quả nhất bằng kỹ thuật xử lý song song.

Hãy thực hiện quy trình sau theo từng bước nghiêm ngặt:

### Bước 1: Phân Tích & Lập Chiến Lược Song Song (Analyze & Strategy)
1.  **Quét nhanh (Quick Scan)**: Đọc Mục lục (Table of Contents) để nắm cấu trúc sách.
2.  **Chia để trị (Divide & Conquer)**: Phân chia nội dung sách thành các phần logic (ví dụ: 3-4 phần lớn) có thể xử lý độc lập.
    *   *Ví dụ: Phần 1 (Chương 1-4), Phần 2 (Chương 5-8), Phần 3 (Chương 9-End).*
3.  **Tạo Plan**: Tạo file `Translation_Plan.md` trình bày chiến lược chia phần và cấu trúc đầu ra.
    *   **Dừng lại và chờ tôi phê duyệt kế hoạch trước khi thực thi.**

### Bước 2: Thực Thi Đa Luồng (Parallel Execution)
Sau khi tôi đồng ý với Plan, hãy kích hoạt các **Sub-agents (Tiểu trình)** chạy song song để xử lý từng phần đồng thời.

*   **Agent A**: Phụ trách Phần 1.
*   **Agent B**: Phụ trách Phần 2.
*   **Agent C**: Phụ trách Phần 3 (v.v...).

**Yêu cầu đầu ra cho mỗi Agent:**
Tạo file Markdown riêng cho từng phần (ví dụ: `BookName_Part_01.md`) với cấu trúc chuẩn:
1.  **Header**: Tên Phần/Chương.
2.  **Tóm tắt (Summary)**: 3-5 điểm cốt lõi nhất (bullet points).
3.  **Nội dung chi tiết (Detailed Content)**:
    *   Dịch ý chính sang tiếng Việt trôi chảy.
    *   **QUAN TRỌNG**: Giữ nguyên thuật ngữ chuyên ngành tiếng Anh (ví dụ: *Product Discovery, Latency*).
4.  **Glossary**: Bảng giải thích thuật ngữ ở cuối file.

### Bước 3: Hợp Nhất & Bàn Giao (Consolidate & Handoff)
1.  Sau khi các Agent hoàn tất, hãy kiểm tra (review) nhanh để đảm bảo tính nhất quán về thuật ngữ.
2.  Tạo thư mục `[BookName]_VN_Translation`.
3.  Di chuyển tất cả các file thành phẩm vào thư mục đó.
4.  Báo cáo hoàn tất.

---
*Hãy bắt đầu bằng Bước 1: Phân tích file PDF và đề xuất chiến lược chia phần để xử lý song song.*
