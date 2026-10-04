# Tóm tắt bản thảo B — ý tưởng và kết quả (tiếng Việt)

Mọi con số dưới đây lấy từ `paper2/output/tables/` (do R sinh ra); bản thảo đầy đủ là `paper2/manuscript/manuscript_B.Rmd` (xuất DOCX: `manuscript_B.docx`).

## 1. Ý tưởng

**Tên tạm:** *What drives Black–Litterman performance? Anchor, views and covariance in a factorial test on Vietnamese bank and equity portfolios.*

**Câu hỏi:** trong danh mục Black–Litterman (BL), bốn "nguyên liệu" — **neo cân bằng (anchor)**, **tín hiệu/quan điểm (view)**, **ước lượng hiệp phương sai**, **mức trần vị thế (cap)** — nguyên liệu nào giải thích phần lớn chênh lệch Sharpe ngoài mẫu, và kết luận có lặp lại ở một mẫu độc lập không?

**Vì sao đổi hướng:** bài đầu (BL với quan điểm phân cụm K-means) cho kết quả rỗng: không mô hình nào vượt 1/N có ý nghĩa thống kê, và Sharpe 0,94 của bài BL-K_IO cũ không tái tạo được trên dữ liệu hiện có (bản cài đặt lại theo mô tả bài chỉ cho 0,71, so với 1/N là 0,73). Thay vì ép ra kết quả "đẹp", bài B biến chính sự khác nhau giữa các cấu hình thành đối tượng nghiên cứu.

**Thiết kế (cố định trước khi tính, ghi trong `process/decisions.md`, mục 15–18):**
- 4 neo (vốn hóa, trọng số bằng nhau, ERC, pha 50/50) × 5 quan điểm (không có, momentum, biến động thấp, tổng hợp, cụm K-means) × 2 hiệp phương sai (mẫu, Ledoit–Wolf) × 2 mức trần (có/không) = **80 danh mục**.
- **Mẫu khám phá:** 25 ngân hàng, hàng tháng, 106 bước ngoài mẫu (8/2017–5/2026).
- **Mẫu xác nhận:** 100 cổ phiếu HOSE thanh khoản nhất trong 347 mã (từ bộ dữ liệu 400 cổ phiếu mới), hàng tuần, 79 bước (2/2025–9/2026).
- **Phương pháp:** ANOVA trên Sharpe của 80 ô; khoảng tin cậy bằng bootstrap khối theo tháng cho tỷ lệ phương sai; ngưỡng "chỉ do nhiễu" bằng hoán vị nhãn; so sánh cặp có hiệu chỉnh Holm; kiểm định tương đương (±0,10 Sharpe) cho tín hiệu; kiểm định SPA của Hansen; DSR cho ô tốt nhất.

## 2. Kết quả chính

| | 25 ngân hàng (tháng) | 100 cổ phiếu (tuần) |
|---|---|---|
| Tỷ lệ phương sai Sharpe do **neo** | **78,2%** (KTC 4,8%–97,8%; ngưỡng nhiễu 9,5%) | 9,6% (1,4%–46,5%) |
| do **quan điểm** | 16,7% (1,1%–80,5%) | **77,6%** (36,1%–92,0%; ngưỡng nhiễu 11,7%) |
| do **hiệp phương sai** | 0,05% | 0,8% |
| do **mức trần** | 0,3% | 1,4% |
| Sharpe trung bình theo neo | VỐN HÓA 0,645; EW 0,747; ERC 0,735; PHA 0,709 | VỐN HÓA 0,515; EW 0,359; ERC 0,496; PHA 0,442 |
| Sharpe trung bình theo quan điểm | không 0,701; momentum 0,700; biến động thấp 0,744; tổng hợp 0,708; cụm 0,692 | không 0,244; momentum 0,255; biến động thấp 0,558; tổng hợp 0,537; cụm 0,670 |

**Các phát hiện:**
1. **Thứ tự ảnh hưởng đảo ngược giữa hai mẫu:** nhóm ngân hàng (tập trung, tương quan chéo trung bình 0,49) bị chi phối bởi neo; mẫu rộng (tương quan 0,36) bị chi phối bởi quan điểm. Giả thuyết H4 (thứ tự giống nhau) **không được ủng hộ**; nhưng khoảng tin cậy rất rộng nên bài không khẳng định hai thứ tự khác nhau có ý nghĩa thống kê.
2. **Hiệp phương sai và mức trần gần như không quan trọng** ở cả hai mẫu (H2 — Ledoit–Wolf tốt hơn mẫu — không được ủng hộ: chênh −0,002 và −0,035).
3. **Quan điểm ở ngân hàng tương đương "không có quan điểm"** trong biên ±0,10 Sharpe cho momentum, tổng hợp và cụm (H3 được ủng hộ cho ba loại này; biến động thấp chạm biên). Ở mẫu rộng, không loại nào chứng minh được tương đương, khoảng tin cậy quá rộng.
4. **Chỉ tín hiệu biến động thấp lặp lại ở mẫu độc lập:** IC xếp hạng 0,073 (t = 2,66) ở ngân hàng và 0,072 (t = 3,13) ở mẫu rộng. Momentum không lặp lại (t = 1,48 và −0,41).
5. **Không ô nào vượt 1/N có ý nghĩa:** SPA p = 0,716 (ngân hàng) và 0,624 (mẫu rộng). Ở mẫu rộng, danh mục phương sai tối thiểu (LW) đơn giản đạt Sharpe 0,943, cao hơn mọi ô BL (tốt nhất 0,855), trong khi 1/N là 0,148.
6. **Chỉ một so sánh cặp sống sót Holm:** ERC tốt hơn EW làm neo ở mẫu rộng (+0,137; p hiệu chỉnh 0,018).
7. **Chi phí:** ở mẫu rộng ô tốt nhất mất khoảng 0,25 Sharpe khi trừ 25 bps/đơn vị giao dịch (0,855 → 0,609); vòng quay chủ yếu do quan điểm quyết định.

## 3. Điều cần nói thẳng

- **Biến động thấp chỉ lặp lại trong 100 cổ phiếu thanh khoản nhất**; trên toàn bộ 347 cổ phiếu (hồi quy Fama–MacBeth, kiểm định đã đăng ký trước của Paper C) hệ số biến động không có ý nghĩa (t = −0,09). Vì vậy không nên viết "biến động thấp lặp lại trên thị trường".
- Mô phỏng Monte Carlo của bài đầu (A) chạy xong nhưng cột kích thước/độ mạnh kiểm định bị lỗi mã (p-value NA); cần chạy lại nếu dùng.

- Khoảng tin cậy của tỷ lệ phương sai rất rộng (ví dụ neo ở ngân hàng 5%–98%): chỉ nên diễn giải theo ước lượng điểm, và nói rõ H1/H5 chỉ được ủng hộ về hướng, chưa về mặt thống kê.
- Mẫu rộng chỉ có 79 tuần, một chế độ thị trường, và neo vốn hóa là **xấp xỉ bằng trọng số giá trị giao dịch** (không có vốn hóa thật).
- Lãi suất phi rủi ro được đọc từ biểu đồ trong bài cũ (sai số khoảng ±0,05 điểm %).
- Ô "tốt nhất" (ngân hàng: EW|LOWVOL|SAMPLE|nocap, Sharpe 0,805) chọn sau khi thấy kết quả, không dùng làm bằng chứng.
- H1/H5 gợi ý từ kết quả bài đầu nên không độc lập hoàn toàn; mẫu rộng là mẫu xác nhận và thiết kế không đổi sau khi xem kết quả ngân hàng.

## 4. Trạng thái các bước theo skill

Đã xong: Phase 1 (brainstorm, RQ Brief, Devil's Advocate checkpoint 1), mã R, bản thảo B. Đang làm: kiểm tra toàn vẹn Stage 2.5 (kiểm thử mã, kiểm tra nhìn trước tương lai, xác minh tham khảo), rồi review 5 vai, sửa đổi, kiểm tra cuối, định dạng cuối và bản ghi quy trình.
