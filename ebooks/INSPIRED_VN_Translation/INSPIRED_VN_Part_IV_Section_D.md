# PHẦN IV: QUY TRÌNH PHÙ HỢP (THE RIGHT PROCESS) - Phần D: Kiểm Thử (Testing)

Trong Phần D này, chúng ta tập trung vào việc **kiểm thử (testing)** các ý tưởng và nguyên mẫu để thu thập bằng chứng xác thực trước khi quyết định xây dựng.

---

# Chương 50: Kiểm Thử Khả Năng Sử Dụng (Testing Usability)

## Tóm tắt (Summary)
*   **Mục đích**: Tìm ra các vấn đề về sử dụng (usability issues) để người dùng có thể thực sự sử dụng được sản phẩm.
*   **Thời điểm**: Làm trong giai đoạn Discovery, TRƯỚC KHI xây dựng sản phẩm thật.
*   **Cách làm**:
    *   Sử dụng **High-fidelity Prototype**.
    *   Quan sát người dùng thực hiện nhiệm vụ (đừng giúp đỡ họ, hãy giữ im lặng và quan sát).
    *   Tìm kiếm 3 trường hợp: (1) làm được ngay, (2) chật vật mới làm được, (3) bỏ cuộc.

---

# Chương 51: Kiểm Thử Giá Trị (Testing Value)

## Tóm tắt (Summary)
*   **Sự thật**: Khách hàng có thể dùng được sản phẩm (Usability) nhưng chưa chắc họ đã *muốn* dùng hoặc mua nó (Value).
*   **Nhiệm vụ**: Phải đảm bảo sản phẩm giải quyết vấn đề tốt hơn đáng kể so với giải pháp hiện tại của họ thì họ mới chịu chuyển đổi.
*   **Phương pháp**: Kết hợp cả định tính (Qualitative) và định lượng (Quantitative).

---

# Chương 52: Các Kỹ Thuật Kiểm Thử Nhu Cầu (Demand Testing Techniques)

## Tóm tắt (Summary)
*   **Vấn đề**: Lãng phí lớn nhất là xây xong sản phẩm rồi mới biết không ai cần.
*   **Kỹ thuật "Fake Door"**: Thêm một nút bấm hoặc menu cho tính năng mới (dù chưa có tính năng đó). Khi bấm vào, hiện thông báo "Chúng tôi đang xây dựng...". Đo lường tỷ lệ click để biết mức độ quan tâm.
*   **Landing Page Test**: Tạo trang giới thiệu sản phẩm như thể nó đã tồn tại, xem có bao nhiêu người bấm đăng ký.

---

# Chương 53: Các Kỹ Thuật Kiểm Thử Giá Trị Định Tính (Qualitative Value Testing Techniques)

## Tóm tắt (Summary)
*   **Mục đích**: Hiểu "Tại sao?" (Why). Tại sao họ thích hoặc không thích?
*   **Cách kiểm chứng "tiền tươi thóc thật"**: Đừng chỉ hỏi "Bạn có thích không?". Hãy yêu cầu họ trả giá bằng một cái gì đó thực tế:
    *   **Tiền**: Ký hợp đồng không ràng buộc (Letter of Intent), trả tiền trước.
    *   **Danh tiếng**: Giới thiệu cho bạn bè/sếp.
    *   **Thời gian**: Dành thời gian làm việc với team.
    *   **Quyền truy cập**: Đưa mật khẩu hệ thống hiện tại để team import dữ liệu.

---

# Chương 54: Các Kỹ Thuật Kiểm Thử Giá Trị Định Lượng (Quantitative Value Testing Techniques)

## Tóm tắt (Summary)
*   **Mục đích**: Thu thập bằng chứng số liệu (Evidence). "Bao nhiêu người thực sự làm việc này?".
*   **A/B Testing**: Tiêu chuẩn vàng. So sánh phiên bản cũ và mới trên 1% người dùng.
*   **Invite-only Testing**: Mời một nhóm nhỏ dùng thử (dành cho B2B hoặc khi không đủ traffic để A/B test).
*   **Analytics**: Phải gắn tracking (đo lường) ngay từ đầu. Đừng bao giờ tung tính năng mà không biết nó có được dùng hay không.

---

# Chương 55: Kiểm Thử Tính Khả Thi (Testing Feasibility)

## Tóm tắt (Summary)
*   **Người thực hiện**: Engineers (Kỹ sư).
*   **Câu hỏi**: Chúng ta có biết cách xây dựng không? Có đủ thời gian không? Có mở rộng (scale) được không? Hiệu năng có ổn không?
*   **Lưu ý**: Đừng ép kỹ sư trả lời ngay trong cuộc họp. Hãy cho họ thời gian nghiên cứu (1-2 ngày) để có câu trả lời chính xác hoặc xây dựng *Feasibility Prototype*.

---

# Chương 56: Kiểm Thử Tính Khả Thi Kinh Doanh (Testing Business Viability)

## Tóm tắt (Summary)
*   **Người thực hiện**: Product Manager (làm việc với các bên liên quan).
*   **Các khía cạnh**:
    *   **Marketing**: Có làm hỏng thương hiệu không?
    *   **Sales**: Sales có bán được cái này không?
    *   **Legal/Compliance**: Có phạm luật hay vi phạm chính sách bảo mật không?
    *   **Finance**: Chúng ta có đủ tiền làm và duy trì không?
*   **Vai trò PM**: Bạn phải hiểu rõ những ràng buộc này ngay từ đầu để không lãng phí công sức team.

---

# Chương 57: Hồ Sơ: Kate Arnold của Netflix

*   **Bài học**: Netflix không tự nhiên mà thành công. Kate Arnold (PM) và team đã phải thử nghiệm rất nhiều mô hình kinh doanh (bao gồm cả bán mình cho Blockbuster nhưng bị từ chối). Sự chuyển đổi sang mô hình đăng ký bao tháng (subscription) và hàng loạt tính năng như "hàng đợi" (queue), "gợi ý phim" (recommendation) đều là kết quả của quá trình khám phá và kiểm thử giá trị liên tục.

---

## Thuật ngữ & Concepts (Glossary) - Phần D

| Thuật ngữ (English) | Giải thích (Vietnamese) |
| :--- | :--- |
| **Usability Testing** | Kiểm thử khả năng sử dụng. Quan sát người dùng thao tác để xem họ có gặp khó khăn gì không. |
| **A/B Testing** | Thử nghiệm phân tách. Chia người dùng thành 2 nhóm (A và B) để xem phiên bản nào hiệu quả hơn. |
| **Fake Door Test** | Thử nghiệm "Cửa giả". Treo biển tính năng để đo nhu cầu trước khi thực sự xây dựng nó. |
| **Feasibility Prototype** | Nguyên mẫu khả thi. Code nháp (thường vứt đi sau đó) để chứng minh một giải pháp kỹ thuật là làm được. |
| **Qualitative vs Quantitative** | Định tính (Chất lượng/Tại sao) vs Định lượng (Số lượng/Bao nhiêu). Cần cả hai để ra quyết định tốt. |
