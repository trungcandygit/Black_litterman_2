# Gói nộp bài cho Finance Research Open (Elsevier)

Bài: **Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification**
Được dựng tự động bằng ARS v3.22.1 (Stage 5, format-convert) từ bản thảo đã qua Stage 4.5 FINAL INTEGRITY (PASS): `ars/stage4_5_integrity/correction_round3/manuscript_v7.clean.md`, SHA-256 `3331a4dea23bb7dddeabf4ca4d82ea4a60b12937637d1fe89374c93d4f7d132c`.

## 1. Việc BẠN còn phải làm trước khi bấm Submit

Đã điền sẵn trong `title_page.docx` theo thông tin bạn gửi: 4 tác giả (Nguyen Thanh Binh, Nguyen Van Trung*, Nguyen Bach Diep, Ha Hong Hanh; đã bỏ Le Hong Minh), đơn vị a/b, tác giả liên hệ, email, ORCID, Acknowledgements "None", competing interests, funding, CRediT. Thư gửi biên tập (`cover_letter.docx`) đã ký tên tác giả liên hệ.

1. **CRediT**: kiểm lại vai của từng người cho *đúng bài FTSE này*. Phần CRediT bạn gửi là của bài Sales-Based REM. Khi bỏ Le Hong Minh, các vai Methodology, Software, Formal analysis của anh ấy không còn ai nhận thêm; hiện chúng do Nguyen Van Trung và Nguyen Bach Diep đảm nhận, đúng như danh sách bạn gửi.
2. **Nhập đúng thứ tự 4 tác giả** trên Editorial Manager, khớp với title page (tạp chí không cho đổi tác giả sau khi nộp).
3. **Competing interests**: vào declarations tool của Elsevier, chọn "I have nothing to declare", tải file Word nó sinh ra và upload.
4. **AI declaration**: bài này khai **Claude (Anthropic)**, vì đã dùng cho code, viết, mô phỏng review và kiểm tra tài liệu. **Không** đổi thành "Gemini … improve language" như bài kia; khai sai là vi phạm chính sách AI của Elsevier.
5. **Data availability**: nên đưa `Supplementary_Replication_Package.zip` lên Mendeley Data hoặc Zenodo để lấy DOI rồi thay câu trong title page. **Không** đưa link GitHub cá nhân vào bản thảo ẩn danh.
6. Giữ nguyên chữ "highlights" trong tên file `highlights.docx`.
7. Chạy iThenticate hoặc Turnitin nếu có điều kiện. Phase D của ARS chỉ là kiểm tra heuristic bằng WebSearch.
8. APC được miễn cho bài nộp trước hoặc đúng ngày **31/12/2026**.
9. Đọc lại toàn bộ `manuscript_anonymized.docx` và `ars/stage4_5_integrity/integrity_report_stage4_5.md` trước khi nộp. Tác giả chịu trách nhiệm cuối cùng.

## 2. File nào upload vào mục nào trên Editorial Manager

| File | Loại file khi upload | Ghi chú |
|---|---|---|
| `manuscript_anonymized.docx` | Manuscript (anonymized) | Bản chính để review: Word một cột, bảng dạng text sửa được, công thức là equation Word gốc, không có thông tin tác giả |
| `manuscript_anonymized.tex` + `figures/Figure_1.png`, `figures/Figure_2.png` | (tùy chọn) LaTeX source | Chỉ cần nếu muốn nộp bằng LaTeX thay cho Word; template elsarticle |
| `manuscript_anonymized.pdf` | không bắt buộc | PDF biên dịch từ LaTeX để bạn đọc soát; hệ thống tự tạo PDF riêng |
| `title_page.docx` | Title page (with author details) | Đã điền 4 tác giả; kiểm lại CRediT (mục 1.1) |
| `highlights.docx` | Highlights | 5 ý, mỗi ý ≤ 85 ký tự (đã kiểm) |
| `figures/Figure_1.pdf` (vector) hoặc `figures/Figure_1.png` (600 dpi, rộng 4500 px) | Figure | Chú thích hình nằm trong bản thảo |
| `figures/Figure_2.pdf` hoặc `figures/Figure_2.png` | Figure | |
| `cover_letter.docx` | Cover letter | Đã ký tên tác giả liên hệ, ngày 24/9/2026 (sửa ngày nếu nộp muộn hơn) |
| File Word từ declarations tool | Declaration of interest | Bạn tự tạo (mục 1.3) |
| `Supplementary_Replication_Package.zip` | Supplementary material | Dữ liệu gốc, code R, kết quả; đã ẩn danh. Nên đổi thành link DOI (mục 1.5) |

## 3. Đã kiểm theo guide của FRO

- Abstract 210 từ (≤ 250), không có trích dẫn; 6 keyword, không keyword nào chứa "and"/"of"; có mã JEL.
- Ẩn danh kép: bản thảo không có tên, đơn vị, lời cảm ơn hay link định danh; CRediT, competing interests và acknowledgements đã chuyển sang title page.
- Mục "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process" là một section riêng, nằm ngay trước References, đúng mẫu câu của tạp chí.
- Bảng là text sửa được, đánh số theo thứ tự xuất hiện, ghi chú đặt dưới bảng, không kẻ dọc; bảng phụ lục đánh số Table A.1, A.2; nguồn bảng ghi "Authors' calculations".
- Tài liệu tham khảo: 33 tài liệu, đều được kiểm tra có thật ở Stage 4.5; có DOI khi tài liệu có DOI; tài liệu web có URL và ngày truy cập; định dạng APA 7.
- Hình: file riêng, đặt tên Figure_1/Figure_2, bản vector PDF và PNG 600 dpi rộng hơn 2244 px.
- Kết quả tái lập được từ dữ liệu gốc: 48/48 file kết quả khớp (xem `ars/stage4_5_integrity/repro/REPRO_REPORT.md`).

## 4. Danh sách file (kích thước, SHA-256 rút gọn)

| File | Bytes | SHA-256 (16) |
|---|---|---|
| `Supplementary_Replication_Package.zip` | 3,139,416 | `b8f86aa55a6ac4c4` |
| `cover_letter.docx` | 11,541 | `72bb351a45576b98` |
| `figures/Figure_1.pdf` | 22,327 | `5ef9aede226577b1` |
| `figures/Figure_1.png` | 343,150 | `e97958bd4a9110c9` |
| `figures/Figure_2.pdf` | 11,358 | `5cac4f17a63c2fef` |
| `figures/Figure_2.png` | 196,301 | `1bfd06f06fa19a6f` |
| `highlights.docx` | 10,708 | `7cf062f74c00dee7` |
| `manuscript_anonymized.docx` | 495,860 | `3296a841aa5d8b3c` |
| `manuscript_anonymized.pdf` | 671,546 | `510004fe9a036692` |
| `manuscript_anonymized.tex` | 90,935 | `b0b6fe39fdba0018` |
| `title_page.docx` | 11,548 | `5c1ae1db63ea5591` |
