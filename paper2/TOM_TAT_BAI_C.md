# Tóm tắt bản thảo C — "Closing at the limit" (giá trần/giá sàn HOSE)

Bản cuối: `paper2/final/Paper_C_Closing_at_the_limit.docx` (và `.md`, `.Rmd`). Mọi số trong bài lấy từ `paper2/output/tables/C1–C25` do R sinh ra.

## Ý tưởng
Cổ phiếu đóng cửa ở giá trần/giá sàn trên HOSE thì ngày hôm sau chuyện gì xảy ra, bao nhiêu là khoảng trống giá qua đêm so với biến động trong phiên, và nhà đầu tư bên ngoài có hưởng được không? Kết hợp với 22 đặc trưng giá–khối lượng trong một họ 26 kiểm định có kiểm soát FDR.

## Kết quả chính (347 cổ phiếu, 8/2024–9/2026)
- 0/22 đặc trưng sống sót (độ mạnh kiểm định thấp: chỉ loại trừ được hệ số khoảng 0,1–0,3 điểm % mỗi tuần). 4/4 kiểm định giá trần/sàn sống sót, kể cả khi gom cụm theo tuần/khối 10 ngày.
- Giá trần: lợi suất bất thường ngày kế tiếp +1,66%, toàn bộ là khoảng trống qua đêm (+2,2%), rồi đảo chiều trong phiên (−0,5%). Giá sàn: −0,71% (−1,65% so với nhóm đối chứng).
- Khoảng trống lớn hơn 2,66 điểm % so với cổ phiếu tăng 5–6,5% (và 3,14 điểm % khi nhóm so sánh cũng đóng cửa ở mức cao nhất ngày).
- Mua ở giá mở cửa kế tiếp và giữ 5 ngày: −0,75% (t = −2,7) so với thị trường: không có lợi nhuận cho nhà đầu tư bên ngoài.

## Điều cần nói thẳng
- Hiệu ứng đóng cửa–đóng cửa ở giá trần đã có trong một phân tích công khai (GitHub, chưa bình duyệt), mẫu dài hơn bao gồm cả giai đoạn này; phần mới là phân rã qua đêm/trong phiên và so sánh với biến động dưới giá trần, và phần này là post hoc.
- Kiểm định 5 ngày với giá trần chủ yếu do ngày t+1; ở giá sàn, t+2..t+5 thêm phần trôi giá nhưng không qua nửa mẫu xác nhận.
- Cơ chế (nhu cầu bị chặn hay tin tức/chú ý hay đấu giá mở cửa) chưa phân biệt được: khoảng trống lớn hơn khi khối lượng lớn và đà tăng trước đó mạnh.
- "Đăng ký trước" chỉ là nhật ký có kiểm soát phiên bản (commit 63bdc6d, trước commit mã/kết quả đầu tiên 13 phút), không phải đăng ký bên ngoài; cần dấu thời gian độc lập trước khi nộp.
- Mẫu ~25 tháng, một sàn, có đổi hệ thống KRX ngày 5/5/2025; luật HOSE lấy từ trang môi giới/báo chí, chưa kiểm tra thông tư của sàn.
- Dự án chọn bài này trong 3 bản thảo/14 ý tưởng (winner's curse).

## Quy trình
Đã chạy: brainstorm, kiểm tra toàn vẹn 2.5 (nhiều vòng), review 5 vai + tổng hợp biên tập (Major Revision), sửa đổi, re-review (Minor), kiểm tra toàn vẹn cuối 4.5 (PASS), hoàn thiện. Các lệch quy trình và việc cần bạn làm: `paper2/process/07_pipeline_process_summary.md`.
