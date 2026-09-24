# Gói nộp bài: Finance Research Open (Elsevier)

Bài: **Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification**

Nguồn: bản thảo cuối (`ars/manuscript_final.md`, SHA-256 `3cb8bd0b7185d5596a94ed16d3459932679f1606e023868f752ec7d6f07ef68b`), đã qua Stage 4.5 của ARS v3.22.1 (PASS, `ars/integrity/reverify_round6.md`) và các vòng proofreading, stop-slop. Mọi file dưới đây đã điền đủ thông tin, bạn không cần sửa gì thêm.

## 1. Upload lên Editorial Manager

| File | Chọn loại file (Item type) khi upload | Ghi chú |
|---|---|---|
| `01_Title_Page.docx` | Title page (with author details) | 4 tác giả, đơn vị, tác giả liên hệ, email, ORCID, lời cảm ơn, competing interests, funding, CRediT, ethics, data availability |
| `02_Manuscript_Anonymized.docx` | Manuscript (anonymized) | File phản biện chính: Word một cột, công thức là equation của Word, bảng sửa được, không có tên tác giả |
| `03_Figures/Figure_1.pdf`, `03_Figures/Figure_2.pdf` | Figure | PDF vector; có thể thay bằng file PNG 600 dpi (rộng 4500 px) cùng tên |
| `04_Declaration_of_Competing_Interest.docx` | Declaration of interest | Đúng câu chuẩn của Elsevier. Nếu hệ thống bắt dùng declarations tool, chọn "I have nothing to declare" và tải file tool sinh ra (nội dung giống hệt) |
| `05_Replication_Package.zip` | Supplementary material | Dữ liệu gốc (405 file giá), code R, kết quả; đã ẩn danh |
| `06_Cover_Letter.docx` | Cover letter | Đã ký tên tác giả liên hệ, ngày 24/9/2026 |
| `07_Manuscript_with_Author_Details.docx` | Manuscript (with author details), nếu hệ thống yêu cầu | Title page ghép với toàn bài; dùng khi biên tập hoặc hệ thống cần bản có tên tác giả. Không gửi file này cho phản biện |
| `08_Highlights.docx` | Highlights | 5 ý, mỗi ý ≤ 85 ký tự; tên file có chữ "highlights" như tạp chí yêu cầu |

Khi điền form online: nhập 4 tác giả đúng thứ tự như title page (Nguyen Thanh Binh; Nguyen Van Trung, tác giả liên hệ; Nguyen Bach Diep; Ha Hong Hanh). Ở mục generative AI, chọn "có dùng" và dán đúng câu trong mục "Declaration of generative AI..." của bản thảo (khai Claude). APC được miễn nếu nộp trước hoặc đúng ngày **31/12/2026**.

## 2. Đã kiểm theo guide của FRO

- **Abstract:** 218 từ (giới hạn 250), không có trích dẫn, không dùng chữ viết tắt chưa định nghĩa.
- **Keywords:** 6 từ khóa, không cụm nào chứa "and" hoặc "of"; có mã JEL.
- **Thân bài:** khoảng 7.900 từ. Có 9 công thức đánh số (1)–(9).
- **Phản biện ẩn danh kép:** bản thảo không có tên, đơn vị hay lời cảm ơn; mọi thông tin tác giả nằm ở title page.
- **Bảng:**
  - dạng text sửa được, không kẻ dọc;
  - đánh số theo thứ tự được nhắc tới lần đầu, kể cả bảng phụ lục A.1–A.3;
  - mỗi bảng có câu dẫn;
  - note một câu, dòng nguồn ghi "Source: Authors' calculations.".
- **Hình:** là file riêng tên Figure_1 và Figure_2, dạng PDF vector hoặc PNG 600 dpi; chú thích hình nằm trong bản thảo.
- **Khai báo AI:** là một mục riêng, đúng tiêu đề tạp chí quy định, đặt ngay trước References.
- **Tài liệu tham khảo:** 33 tài liệu, đều được kiểm tra có thật ở Stage 4.5; có DOI khi tài liệu có DOI; tài liệu web có URL và ngày truy cập; định dạng APA 7.
- **Định dạng Word:**
  - Times New Roman 12 pt, giãn dòng đôi, lề 2,54 cm;
  - số trang ở góc trên bên phải;
  - bản thảo có đánh số dòng liên tục và căn đều hai bên;
  - toàn bộ chữ màu đen, tiêu đề đậm;
  - bảng dạng text sửa được, không kẻ dọc, chữ trong bảng giãn dòng đơn;
  - tài liệu tham khảo thụt dòng treo theo APA 7;
  - giả thuyết viết H₁–H₄;
  - công thức là equation của Word;
  - cả 6 file .docx đều qua bước kiểm tra cấu trúc OOXML (schema).
- **Tái lập kết quả:** chạy lại từ dữ liệu gốc, cả 48 file kết quả đều khớp.

## 3. Danh sách file (kích thước, SHA-256 rút gọn)

| File | Bytes | SHA-256 (16) |
|---|---|---|
| `01_Title_Page.docx` | 11,435 | `cd1170c8a8dec5b2` |
| `02_Manuscript_Anonymized.docx` | 551,332 | `0cad8ea4b7bd8407` |
| `03_Figures/Figure_1.pdf` | 22,369 | `35fae45813787fc7` |
| `03_Figures/Figure_1.png` | 388,280 | `037f315456be9bc6` |
| `03_Figures/Figure_2.pdf` | 10,560 | `5830be0f3b7f1f8b` |
| `03_Figures/Figure_2.png` | 205,590 | `e37f1462c8e5df03` |
| `04_Declaration_of_Competing_Interest.docx` | 10,588 | `97f7c142bd8e5bf7` |
| `05_Replication_Package.zip` | 3,195,237 | `2896483b4ec6a413` |
| `06_Cover_Letter.docx` | 11,427 | `1b22fcbdd8b3314c` |
| `07_Manuscript_with_Author_Details.docx` | 552,011 | `bcd717c7a1d5da41` |
| `08_Highlights.docx` | 10,589 | `83d50dafdc48944f` |
