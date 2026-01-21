# PHẦN IV: QUY TRÌNH PHÙ HỢP (THE RIGHT PROCESS) - Phần C: Tạo Nguyên Mẫu (Prototyping)

Trong Phần C này, chúng ta tập trung vào công cụ mạnh mẽ nhất của Product Discovery: **Nguyên mẫu (Prototype)**. Nguyên tắc vàng: "Học hỏi nhanh nhất và rẻ nhất có thể".

---

# Chương 45: Các Nguyên Tắc Của Nguyên Mẫu (Principles of Prototypes)

## Tóm tắt (Summary)
*   **Mục đích**: Học hỏi một cái gì đó với chi phí thấp hơn nhiều (thường là 1/10) so với việc xây dựng sản phẩm thật.
*   **Tác dụng**: Buộc bạn phải suy nghĩ sâu sắc hơn về giải pháp, giúp team cộng tác tốt hơn, và là công cụ giao tiếp mạnh mẽ.
*   **Fidelity (Độ trung thực)**: Không có một mức độ "chuẩn". Tùy mục đích mà dùng Low-fidelity (phác thảo) hay High-fidelity (giống thật).

---

# Chương 46: Kỹ Thuật Nguyên Mẫu Khả Thi (Feasibility Prototype Technique)

## Tóm tắt (Summary)
*   **Khi nào dùng**: Khi kỹ sư lo ngại về rủi ro kỹ thuật (thuật toán mới, hiệu năng, công nghệ mới...).
*   **Cách làm**: Kỹ sư viết một đoạn code "vừa đủ" để chứng minh là làm được.
*   **Lưu ý**: Đây là code vứt đi (throwaway code), không phải code sản phẩm. Mục đích chỉ để trả lời câu hỏi: "Có làm được không?".

---

# Chương 47: Kỹ Thuật Nguyên Mẫu Người Dùng (User Prototype Technique)

## Tóm tắt (Summary)
*   **Khái niệm**: Là một bản mô phỏng (simulation) trải nghiệm người dùng. Nó trông có vẻ thật nhưng không có backend thực sự ("Smoke and mirrors").
*   **Các loại**:
    *   **Low-fidelity**: Wireframe, phác thảo giấy (tốt để tư duy luồng đi).
    *   **High-fidelity**: Clickable mockup, trông y như thật (tốt để test với người dùng và test giá trị).
*   **Lợi ích**: Giúp xác thực xem người dùng có hiểu cách dùng và có thích sản phẩm không mà không tốn công code.

---

# Chương 48: Kỹ Thuật Nguyên Mẫu Dữ Liệu Thực (Live-Data Prototype Technique)

## Tóm tắt (Summary)
*   **Khi nào dùng**: Khi cần chứng minh một điều gì đó bằng dữ liệu thực tế (ví dụ: test thuật toán tìm kiếm, game dynamics, social features).
*   **Cách làm**: Xây dựng một phiên bản rất giới hạn nhưng chạy được, thu thập dữ liệu thật từ một nhóm nhỏ người dùng.
*   **Rủi ro**: Đừng nhầm lẫn đây là sản phẩm hoàn chỉnh. Nó chưa sẵn sàng để scale hay maintain.

---

# Chương 49: Kỹ Thuật Nguyên Mẫu Lai (Hybrid Prototype Technique)

## Tóm tắt (Summary)
*   **Wizard of Oz Prototype**: Một kỹ thuật thú vị kết hợp giữa giao diện người dùng (trông như thật) và con người làm thủ công ở phía sau (thay vì máy móc).
*   **Ví dụ**: Bạn làm một dịch vụ trợ lý ảo. Thay vì code AI phức tạp, khi người dùng chat, bạn (PM) tự tay trả lời họ ở phía sau.
*   **Lợi ích**: Kiểm chứng được nhu cầu thực tế mà không tốn thời gian xây dựng hệ thống tự động phức tạp.

---

## Thuật ngữ & Concepts (Glossary) - Phần C

| Thuật ngữ (English) | Giải thích (Vietnamese) |
| :--- | :--- |
| **Prototype** | Nguyên mẫu. Một bản mô phỏng sản phẩm dùng để học hỏi và kiểm thử, không phải là sản phẩm thật để bán. |
| **Low-fidelity** | Độ trung thực thấp (ví dụ: bản vẽ tay). Nhanh, rẻ, dùng để trao đổi ý tưởng nội bộ. |
| **High-fidelity** | Độ trung thực cao (ví dụ: thiết kế tương tác y như thật). Dùng để test với khách hàng và đánh giá giá trị. |
| **Wizard of Oz** | Kỹ thuật "Phù thủy xứ Oz": Giao diện thì tự động, nhưng bên trong là người làm thủ công ("Fake it until you make it"). |
