---
title: "Hồ sơ quá trình tạo bài báo"
subtitle: "Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification"
date: "24/9/2026"
---

# 1. Thông tin bài báo

- **Tên bài**: Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification
- **Tạp chí mục tiêu**: Finance Research Open (Elsevier, truy cập mở; miễn APC cho bài nộp trước hoặc đúng ngày 31/12/2026). Tác giả chọn từ danh sách rút gọn gồm 4 tạp chí.
- **Lần chạy**: `ftse2-20260924-01`, bộ Academic Research Skills (ARS) academic-pipeline v3.22.1, vào từ Stage 1, chạy đủ cả 10 stage.
- **Bản thảo cuối**: `ars/stage4_5_integrity/correction_round3/manuscript_v7.clean.md` (SHA-256 `3331a4de…132c`). Khoảng 8.500 từ gồm cả ghi chú; 9 bảng và 2 bảng phụ lục; 2 hình; 33 tài liệu tham khảo đã kiểm chứng.
- **Sản phẩm** (thư mục `submission/`):
  - bản thảo ẩn danh: DOCX có công thức dạng equation Word gốc, cùng mã nguồn LaTeX elsarticle và bản PDF đã biên dịch;
  - trang bìa (title page), highlights, thư gửi biên tập;
  - Figure_1 và Figure_2, mỗi hình có bản PDF vector và PNG 600 dpi;
  - gói tái lập đã ẩn danh: 405 file dữ liệu gốc, code R, 48 bảng kết quả;
  - hướng dẫn nộp bài bằng tiếng Việt (`README_NOP_BAI.md`).

# 2. Quá trình theo từng stage

| Stage | Skill / mode | Đầu vào | Đầu ra | Quyết định chính (lời tác giả, nguyên văn) |
|---|---|---|---|---|
| Intake | academic-pipeline | bản nháp một số mục, code R, dữ liệu dở dang, bản red-team của bài FTSE trước | bắt đầu từ Stage 1 | "run stages sequentially per ARS" |
| 1 RESEARCH | deep-research, quick | research brief, câu hỏi nghiên cứu | RQ brief, thiết kế phương pháp, danh mục tài liệu đã kiểm (23) | Phát hiện 4 DOI "nhớ nhầm" trỏ sang bài không liên quan và đã sửa; Devil's Advocate chuyển 2 điều kiện thiết kế MAJOR sang Stage 2 |
| 2 WRITE | academic-paper, full | gói Stage 1 | bản v1, rồi v2 (khung A′) | Duyệt cấu hình: "ok tiếp đi"; giữ mục tiêu 7.000 từ: "b"; khung A thất bại ở kiểm định thời điểm được nêu tên (cơ chế chống frame-lock), tác giả giao quyền chọn: "cái nào dễ đăng nhất mạnh nhất" → A′ (lấy nhóm thành phần làm trọng tâm) |
| 2.5 INTEGRITY | integrity_verification_agent, Mode 1 | v2 | PASS sau 1 vòng sửa (11 lỗi) | "theo skill bai tot nhat la duoc" |
| 3 REVIEW | academic-paper-reviewer, full (5 reviewer) | v2 | Major Revision; lỗi chặn: B1 chọn nhóm xử lý, B2 nhiễm nhóm đối chứng, B3 suy luận CAR | tác giả xác nhận; yêu cầu review dùng agent độc lập |
| 4 REVISE | academic-paper, revision (viết lại toàn bộ) | roadmap | v3 và thư phản hồi; phân tích mới (ITT, CAR danh mục, wild bootstrap, randomization inference) | "just fix it, no questions" |
| 3′ RE-REVIEW | academic-paper-reviewer, re-review (5 subagent độc lập, ngữ cảnh mới, 3 cổng) | v3 | Major Revision (DA NEW-1/NEW-2; phần còn lại của RR1 giữ mức must_fix theo nguyên tắc fail-closed) | "cu lam theo skill" |
| 4′ RE-REVISE | academic-paper, revision (patch #390 1.1) | roadmap vòng 2 (17 mục) | v4 (60 op, 127/186 block giữ nguyên từng byte) | chỉ thị thường trực: "tu gio cu lam theo skill. Dung hoi gi nua" |
| 4.5 FINAL INTEGRITY | integrity_verification_agent, Mode 2 | v4 | kiểm tra mới từ đầu ra FAIL, sau 3 vòng sửa đạt PASS (v7); tái lập toàn bộ từ dữ liệu gốc | phiên này: "force dùng skill này toàn bộ"; "bắt buộc load skill mỗi khi làm task gì đó"; "không hỏi lại … tuân thủ tuyệt đối theo skill"; "source ghi kiểu author caculation.. chứ" |
| 5 FINALIZE | academic-paper, format-convert | v7 | gói nộp FRO | "file msword có hiển thị được công thức toán dạng latex mà … update luôn"; cung cấp đầy đủ guide for authors của FRO |
| 6 PROCESS SUMMARY | orchestrator | toàn bộ lần chạy | hồ sơ này (EN và VI) | cặp ngôn ngữ Việt và Anh (quyết định thường trực) |

# 3. Chi tiết các vòng lặp

**Stage 3 (vòng 1).** 5 vai reviewer tách biệt nhưng chạy trong cùng một ngữ cảnh. Điều này đã được công bố: các reviewer không "mù" với nhau và cùng họ mô hình. Quyết định Major Revision được suy ra cơ học (F2: dimension bắt buộc bị chặn). Ba lỗi chặn:
- nhóm xử lý được định nghĩa bằng thông tin sau xử lý, vì FTSE chọn danh sách thành phần theo dữ liệu giữa năm 2026;
- nhóm đối chứng chứa các cổ phiếu FTSE đã nêu tên là đủ điều kiện;
- suy luận CAR bỏ qua việc các sự kiện trùng ngày và dùng benchmark lệch về quy mô.

**Stage 4.** Bổ sung:
- nhóm intention-to-treat (ITT) sàng lọc trên dữ liệu 2024;
- dựng lại các nhóm từ danh sách công khai của FTSE;
- kiểm định CAR danh mục với 4 benchmark;
- wild cluster bootstrap và randomization inference.

Giới hạn cần nói rõ: v3 được viết lại toàn bộ, nằm ngoài chuỗi patch, nên về sau không dựng được Revision-Evidence Bundle.

**Stage 3′ (vòng 2).** 5 subagent với ngữ cảnh mới, không thấy kết quả của nhau, chạy giao thức 3 cổng. Kết quả:
- RR2, SR1 và SR5 được xử lý đầy đủ; RR1 (ITT) mới xử lý một phần;
- chính bản sửa đưa vào 2 lỗi MAJOR mới: một cách đọc cận trên/cận dưới không có cơ sở, và cửa sổ sự kiện chọn không đồng đều giữa các sự kiện.

Script kiểm #576 không chạy được do thiếu bundle, nên quyết định được suy ra bằng tay và có công bố rõ.

**Stage 4′.** Xử lý 17 mục roadmap qua chuỗi patch #390:
- cửa sổ sự kiện định trước và giống nhau cho mọi sự kiện;
- quy tắc "reliable": có ý nghĩa ở mức 5% dưới cả 4 benchmark;
- độ lớn hiệu ứng báo dưới dạng khoảng;
- event study cho nhóm ITT, báo cả kiểm định pre-trend bị bác bỏ;
- ước lượng matched có trọng số, kiểm định drift, kiểm tra theo ngành, kiểm tra việc BSR chuyển sàn.

**Stage 4.5.** Lần kiểm tra mới từ đầu phát hiện những gì 4 lần kiểm trước đã bỏ sót:
- 2 ngữ cảnh trích dẫn mâu thuẫn với nguồn (Gregoriou & Nguyen, 2010; Hegde & McDermott, 2003);
- 3 con số trong bài lệch với chính bảng của nó;
- 1 tiêu đề mục nói mạnh hơn nội dung;
- 6 chỗ độ mạnh claim bị trôi do sửa ở Stage 4′;
- 2 tên thông cáo báo chí sai; 1 phiên bản FAQ không kiểm chứng được;
- 1 câu gần như chép nguyên abstract;
- thiếu nghiên cứu gần nhất (Burnham, Gakidis & Wurgler, 2018).

Toàn bộ script R được chạy lại từ dữ liệu gốc, 48/48 bảng kết quả tái lập được. Ba vòng sửa (33, 9 và 13 op) đưa kết luận từ FAIL lên PASS. Riêng việc đổi nguồn bảng sang "Authors' calculations" ở vòng 3 là do tác giả phát hiện.

**Stage 5.**
- Tách bản ẩn danh kép; công thức là equation Word gốc.
- LaTeX elsarticle biên dịch bằng XeLaTeX (host bundle của tectonic bị chặn trong môi trường này).
- Hình và highlights đúng chuẩn FRO; có gói tái lập.

Hai lỗi chuyển đổi được phát hiện nhờ render ra để xem: abstract bị cắt trong PDF do dấu % chưa escape, và dấu sao ý nghĩa bị biến thành chữ nghiêng. Cả hai đã sửa trước khi đóng gói.

# 4. Tóm tắt mô hình tương tác

| Chỉ số | Giá trị |
|---|---|
| Số stage đã chạy | 10/10 (1, 2, 2.5, 3, 4, 3′, 4′, 4.5, 5, 6) |
| Số vòng review | 2 (Stage 3: 5 reviewer; Stage 3′: 5 subagent độc lập) |
| Số lần kiểm tra integrity | Stage 2.5 (1 vòng sửa); Stage 4.5 (kiểm tra mới, 3 vòng sửa, 2 lần kiểm lại độc lập) |
| Số op patch do script apply tất định thực hiện | 60 (Stage 4′), cộng 33, 9 và 13 (các vòng sửa Stage 4.5) |
| Tài liệu tham khảo | 23 (Stage 2), rồi 25, 27, 29, 31, cuối cùng 33; tất cả đã kiểm chứng |
| Can thiệp của tác giả làm thay đổi kết quả (phiên này) | bắt buộc dùng skill và mọi agent phải load skill; cung cấp dữ liệu gốc; cung cấp guide đầy đủ của tạp chí; yêu cầu equation Word gốc; yêu cầu nguồn bảng ghi "Authors' calculations" |
| Quyết định ở checkpoint tác giả giao cho AI | chọn khung bài (Stage 2) và toàn bộ checkpoint MANDATORY còn lại (chỉ thị thường trực) |
| Số khuyến nghị của AI bị tác giả bác | 0 |
| Số lỗi của AI do tác giả phát hiện | 2 (agent chưa load skill; nguồn bảng ghi đường dẫn file) |

# 5. Các quyết định chính của tác giả (theo thời gian)

1. Chạy toàn bộ pipeline ARS từ Stage 1, tuần tự.
2. Chọn Finance Research Open từ danh sách 4 tạp chí.
3. Duyệt cấu hình ("ok tiếp đi"); giữ mục tiêu 7.000 từ và bổ sung phân tích ("b").
4. Giao quyền chọn khung bài sau khi khung A thất bại: "cái nào dễ đăng nhất mạnh nhất" (→ A′).
5. Yêu cầu agent độc lập cho vòng re-review.
6. Giao thường trực mọi checkpoint còn lại: "tu gio cu lam theo skill. Dung hoi gi nua".
7. Bắt buộc dùng đầy đủ skill ARS và mọi task, kể cả mọi subagent, phải load skill ("bắt buộc load skill mỗi khi làm task gì đó").
8. Đưa dữ liệu gốc lên repo để tái lập kết quả (sau khi gỡ quy tắc chặn trong .gitignore).
9. Cung cấp guide đầy đủ của FRO và yêu cầu một thư mục sẵn sàng để nộp.
10. Yêu cầu equation Word gốc và nguồn bảng ghi "Authors' calculations".

# 6. Bài học rút ra

1. **Lần kiểm tra integrity cuối từ đầu là đáng công.** Stage 2.5 và hai vòng review đều cho qua những trích dẫn mâu thuẫn với nguồn; chỉ lần kiểm Stage 4.5 làm lại từ đầu mới bắt được. Không bao giờ hạ Stage 4.5 xuống thành "kiểm lại các lỗi đã biết".
2. **Chính việc sửa bài sinh ra lỗi.** Sáu chỗ trôi độ mạnh claim và ba con số lệch đều do các chỉnh sửa ở Stage 4′. Rà E6 và đối chiếu lại số liệu sau mỗi vòng sửa là bắt buộc, không phải tùy chọn.
3. **Giữ chuỗi patch ngay từ vòng sửa đầu tiên.** Việc viết lại toàn bộ ở Stage 4 khiến không dựng được Revision-Evidence Bundle, nên script #576 và hợp đồng E6 chính thức không chạy được về sau. Hãy dùng patch #390 từ vòng 1.
4. **Tái lập từ dữ liệu gốc, không chỉ đối chiếu với output đã lưu.** Khớp bài với CSV chưa chứng minh code và dữ liệu hiện tại vẫn sinh ra CSV đó. Lần chạy lại còn phát hiện một quy ước p-value phụ thuộc phiên bản gói.
5. **Đưa quy ước của tạp chí vào cấu hình từ sớm.** Quy ước ghi nguồn bảng và định dạng công thức chỉ lộ ra ở Stage 5; guide for authors đầy đủ nên có ngay từ Phase 0.
6. **Subagent cần đọc chính file skill, không phải bản tóm tắt.** Việc tác giả bắt buộc load skill cho mọi task đã vá một lỗ hổng có thật.

# 7. Quỹ đạo độ sâu cộng tác (collaboration_depth_agent, toàn pipeline, chỉ mang tính tham khảo)

### Ghi nhận nạp skill

Các tệp đã được đọc toàn văn bằng công cụ Read ngay khi bắt đầu lượt này (ARS v3.22.1, bản sao cục bộ `academic-research-skills/` trong scratchpad của phiên):

| Tệp | Tiêu đề đầu tiên | Phạm vi đọc |
|---|---|---|
| `academic-pipeline/agents/collaboration_depth_agent.md` (agent v1.0.0) | `# Collaboration Depth Agent — Observer of User-AI Collaboration Mode` | toàn văn |
| `shared/collaboration_depth_rubric.md` (rubric_version 1.0.1) | `# Collaboration Depth Rubric` | toàn văn |
| `academic-pipeline/references/process_summary_protocol.md` | `# Stage 6: Process Summary Protocol (Added in v2.4)` | Bước 2b của Workflow và mục loại trừ ngay sau bước đó |

Chấm điểm chéo mô hình: biến `ARS_CROSS_MODEL` chưa được đặt, nên không chạy mô hình thứ hai và không có dữ liệu nào được gửi ra ngoài phiên này. Báo cáo này chỉ gồm điểm của mô hình chính và không có cờ `cross_model_divergence`.

### Cơ sở bằng chứng và giới hạn

- **Giai đoạn 1 đến 4' (phiên trước).** Không có hội thoại gốc của phiên đó. Bằng chứng duy nhất là các quyết định đã ghi trong `ars/pipeline_state.json` → `user_decisions`, được trích dẫn ở đây là **UD1 đến UD13** theo thứ tự trong tệp. Một số mục trích nguyên văn lời người dùng (UD3 đến UD6, UD8, UD11, UD12). Các mục khác là bản diễn giải của orchestrator (UD1, UD2, UD9, UD10), và một vài trích dẫn đã mất dấu tiếng Việt. UD7 là ghi chú của AI, không phải hành động của người dùng. Có một trích dẫn nguyên văn lấy từ sản phẩm Giai đoạn 4 (`ars/stage4_revise/author_adjudication_round1.json`, trường `author_instruction`). Quyết định đã ghi có thể phản ánh thiếu mức cảnh giác, vì một nhận xét phản biện nói trong hội thoại có thể không bao giờ được ghi vào state. Do đó, điểm theo giai đoạn của các giai đoạn này có độ tin cậy thấp hơn điểm của Giai đoạn 4.5 đến 6.
- **Giai đoạn 4.5 đến 6 (phiên này).** Tệp `ars/stage6_process/session_2026-09-24b_user_messages.md` chứa 15 tin nhắn của người dùng, được trích dẫn là **M1 đến M15**. M5 và M14 là người dùng lặp lại văn bản của AI, M7 là log terminal (một dòng chứa thông tin xác thực đã bị xoá), và M8 lạc đề (credit tính toán). Không có văn bản gốc các lượt của AI, nên khi người dùng phản ứng với điều gì đó, nội dung được phản ứng (ví dụ điều AI đã đề xuất trước M9, M11 và M12) được suy ra từ lời người dùng và các ghi chú phía AI trong tệp.
- **Quy tắc cửa sổ tối thiểu.** Đặc tả agent yêu cầu báo `insufficient_evidence` cho mọi cửa sổ giai đoạn có ít hơn 5 lượt người dùng. Các Giai đoạn 1, 2.5, 3, 3', 4, 4' và 5 đều dưới ngưỡng này. Các dòng của chúng dưới đây mô tả điều quan sát được nhưng không có điểm số. Để có điểm số, cửa sổ được gộp khi bằng chứng cho phép: một cửa sổ gộp phiên trước (UD1 đến UD13) và hai cửa sổ trong phiên này.
- Lượt này chỉ chấm phía người dùng của sự cộng tác. Nó không đánh giá chất lượng bài báo, và tách biệt với phần Đánh giá Chất lượng Cộng tác của Giai đoạn 6.


### Quỹ đạo độ sâu cộng tác (tham khảo, Wang & Zhang 2026)

#### Tóm tắt theo giai đoạn

| Giai đoạn | Vùng | DI | CV | CR | Ghi chú |
|---|---|---|---|---|---|
| 1 Nghiên cứu | insufficient_evidence | insufficient_evidence | insufficient_evidence | insufficient_evidence | 2 mục diễn giải. Toàn bộ pipeline được giao ngay từ đầu: "run stages sequentially per ARS" (UD1), "continue to Stage 2 (full)" (UD2). Không ghi nhận câu hỏi nào về bản tóm tắt nghiên cứu, câu hỏi nghiên cứu, hay 4 DOI sai mà pipeline đã phát hiện. Danh sách rút gọn bốn tạp chí do người dùng đưa ra (`target_venue.chosen_from`). |
| 2 Viết | Vùng 2 — Nông (dạng giao việc cam kết) | 9/10 | 2/10 | 3/10 | Chấp nhận cấu hình bằng "ok tiếp đi" (UD3). Chuyển từ Giai đoạn 2 sang 2.5 bằng "theo skill bai tot nhat la duoc" (UD8). Trao quyền tự chạy qua đêm: "cứ làm theo skill nha . tôi đi ngủ đây" (UD5). Khi khung A không vượt qua kiểm định thời điểm nêu tên, lựa chọn khung cũng được giao nốt: "cái nào dễ đăng nhất mạnh nhất" (UD6). Một quyết định mang tính phán đoán của con người: "b", giữ mục tiêu 7.000 từ và bổ sung phân tích (UD4). |
| 2.5 Liêm chính | insufficient_evidence | insufficient_evidence | insufficient_evidence | insufficient_evidence | 1 mục diễn giải: "User confirmed Stage 2.5 PASS" (UD9). Không ghi nhận câu hỏi nào về 11 lỗi đã tìm thấy và sửa. |
| 3 Phản biện | insufficient_evidence | insufficient_evidence | insufficient_evidence | insufficient_evidence | UD10, "just fix it, no questions". Nguyên văn trong hồ sơ Giai đoạn 4: "lam theo skill. Khong hoi lai de toi di ngu. sao cho bai san pham la chinh chu nhat". Cả 14 mục trong lộ trình sửa đều được phân loại `will_address`, tác giả không phản bác mục nào. |
| 3' Phản biện lại | insufficient_evidence | insufficient_evidence | insufficient_evidence | insufficient_evidence | Khoảnh khắc cảnh giác rõ nhất của phiên trước: "review must use independent agents" (UD10, diễn giải). Người dùng phản bác cách AI đã tổ chức phản biện, và Giai đoạn 3' được làm lại với 5 subagent độc lập, không thấy kết quả của nhau. Sau đó quyết định Major Revision được chấp nhận bằng "cu lam theo skill" (UD11). |
| 4 / 4' Sửa bài | insufficient_evidence | insufficient_evidence | insufficient_evidence | insufficient_evidence | Giao thường trực các điểm kiểm tra BẮT BUỘC còn lại: "tu gio cu lam theo skill. Dung hoi gi nua. De toi yen tam giao cho ban va di ngu" (UD12). Không ghi nhận phản ứng nào với các lỗi hồi quy (DA NEW-1/NEW-2) hay với thư phản hồi phản biện. |
| **1 đến 4' gộp** (UD1 đến UD13) | **Vùng 2 — Nông (dạng giao việc cam kết)** | **9/10** | **2/10** | **2/10** | Độ tin cậy thấp (chỉ có quyết định đã ghi). |
| 4.5 Liêm chính cuối (M1 đến M10) | Vùng 2 — Nông (dạng giao việc cam kết) | 9/10 | 3/10 | 2/10 | Cảnh giác về quy trình, tức là skill có được dùng không: "agent có dùng skill không đó" (M2). Câu hỏi này phát hiện một lỗ hổng thật: các agent kiểm chứng đã được giao việc với quy tắc diễn giải lại thay vì đọc skill. Lần duy nhất người dùng thách thức kế hoạch của AI là để phản đối việc chạy lại một bước kiểm tra: "các file hiện có là khớp mà ... sao phải chạy lại" (M9). Người dùng cung cấp hướng dẫn tác giả của FRO và dữ liệu gốc (M6, M7, M10). |
| 5 Hoàn thiện + 6 Quy trình (M11 đến M15, gộp) | Vùng 2 — Trung bình (định tính kèm theo: cảnh giác về cách trình bày đầu ra, tái phân bổ thấp) | 9/10 | 4/10 | 2/10 | Phát hiện và yêu cầu sửa hai lỗi cụ thể trong đầu ra của AI. Hiển thị công thức trong Word: "file msword có hiển thị được công thức toán dạng latex mà ... update luôn" (M11). Ghi chú nguồn của bảng: "source ghi kiểu author caculation.. chứ. sao lại ghi từ file nào" (M12). M13 đến M15 là kiểm tra việc dùng skill, không phải kiểm tra nội dung. |

DI = Cường độ giao việc (Delegation Intensity), CV = Cảnh giác nhận thức (Cognitive Vigilance), CR = Tái phân bổ nhận thức (Cognitive Reallocation). Dải điểm: 0 đến 3 thấp, 4 đến 6 trung bình, 7 đến 10 cao.

**Toàn pipeline (gộp toàn bộ bằng chứng): Vùng 2 — Nông (dạng giao việc cam kết). DI 9/10, CV 3/10, CR 2/10.**

#### Nhận xét toàn pipeline

Việc giao việc nhất quán theo từng nhiệm vụ trọn vẹn và có cam kết, từ lúc bắt đầu đến Giai đoạn 6: giao trọn giai đoạn, giao cả những lượt chạy qua đêm, và cuối cùng giao luôn quyền quyết định tại các điểm kiểm tra BẮT BUỘC ("Chạy Không hỏi", M3; "KHÔNG HỎI LẠI, TÔI ĐI NGỦ ĐÂY", M10). Đây là mô thức ngược với kiểu "hỏi vụn vặt, rời rạc". Điểm thấp nằm ở hai chiều còn lại. Cả bằng chứng đã ghi lẫn bằng chứng trong phiên đều không cho thấy người dùng hỏi một nhận định, con số, ước lượng hay trích dẫn nào đến từ đâu. Quyết định nghiên cứu thực chất duy nhất là đổi khung sau khi khung A không vượt qua chính kiểm định của nó, và quyết định này được giao cho AI với tiêu chí khả năng đăng bài (UD6) thay vì được người dùng tự cân nhắc. Sự cảnh giác của người dùng chủ yếu hướng vào quy trình, tức là skill có được nạp không và các agent phản biện có độc lập không (UD10, M2, M13 đến M15). Sự cảnh giác về quy trình này là thật và đã định hình pipeline: nó dẫn tới việc thiết kế lại Giai đoạn 3' và việc các agent được yêu cầu đọc lại tệp skill. Cảnh giác ở cấp nội dung chỉ xuất hiện ở Giai đoạn 5, và chỉ về cách trình bày (M11, M12). Hình dạng chỉ thay đổi ở một dịch chuyển nhỏ đó, từ kiểm tra quy trình sang kiểm tra cách trình bày vào cuối lượt chạy. Điều không thay đổi là tái phân bổ: năng lực được giải phóng nhờ giao việc, theo chính lời người dùng, được dùng để nghỉ ngơi ("tôi đi ngủ", UD5, M10). Không có dấu hiệu nào về việc người dùng định khung lại vấn đề, đưa ra phản lập luận hay tổng hợp nguyên gốc ở bất kỳ đâu trong hồ sơ. Theo quy tắc tổng hợp của rubric, đây là Vùng 2 theo đường "giao việc mà không tái phân bổ", chứ không phải do dùng AI rời rạc.

#### Trọng tâm gợi ý cho các phiên ARS sau

- Bạn có thể giữ lại cho mình một hai quyết định thực chất ngay cả khi giao hết phần còn lại. Ví dụ, tại ngã rẽ về khung (UD6), bạn có thể đọc bản ghi nhớ quyết định một trang (`DECISION_MEMO_framing_round2.md`) và nói trong một câu vì sao chọn A' chứ không phải B, dựa trên điều bạn tin về cách FTSE chọn cổ phiếu. Làm vậy sẽ biến một lựa chọn được giao thành một khoảnh khắc tái phân bổ mà không làm chậm lượt chạy qua đêm.
- Bạn có thể áp dụng kiểu kiểm tra bạn vẫn làm với quy trình (M2, "agent có dùng skill không đó") cho cả nội dung nghiên cứu. Chỉ một câu hỏi ở mỗi điểm kiểm tra, chẳng hạn "con số này lấy từ bảng nào?" hay "vì sao cửa sổ ±1 ngày là cửa sổ đúng?", đã được tính là cảnh giác trên chiều mà bài báo gốc xác định là tác động mạnh nhất (β = 0,437). Lượt kiểm tra liêm chính cuối cùng của chính pipeline đã phát hiện 2 lỗi NGHIÊM TRỌNG và 15 lỗi TRUNG BÌNH lọt qua các điểm kiểm tra trước đó mà người dùng đã xác nhận (UD9, UD11). Những điểm kiểm tra đó là chỗ tự nhiên để đặt câu hỏi như vậy.
- Khi bạn phản đối một kế hoạch kiểm chứng, như ở M9 ("sao phải chạy lại"), bạn có thể yêu cầu AI nói rõ bước kiểm tra bổ sung đó sẽ phát hiện được gì trước khi bạn quyết định. Như vậy bạn vẫn giữ được sự phản biện nhưng dựa trên bằng chứng. Lượt chạy tái lập đầu tiên trong phiên này thực tế đã hỏng mà không báo lỗi và phải chạy lại.
- Bạn có thể nêu rõ cách phân công ngay từ đầu ("bạn lo X; tôi sẽ quyết Y và kiểm tra Z"). Rubric coi đây là tín hiệu giao việc mạnh nhất vì nó nói rõ con người giữ lại phần nào, còn ở đây không phần nào được nêu (UD1, M3).

Rubric: shared/collaboration_depth_rubric.md (phiên bản 1.0.1; mẫu của agent ghi 1.0)
Nguồn: Wang, S., & Zhang, H. (2026). IJETHE 23:11. DOI 10.1186/s41239-026-00585-x
Chỉ mang tính tham khảo. Không phản ánh chất lượng bài báo (xem phần Đánh giá Chất lượng Cộng tác của Giai đoạn 6) hay năng lực của người dùng.


### Phụ lục: bảng chấm điểm (bằng chứng và liệt kê ngược bắt buộc)

#### Cường độ giao việc: 9/10 (Cao)

Bằng chứng ủng hộ (cần ít nhất 2 cho mức Cao):
- UD5: "cứ làm theo skill nha . tôi đi ngủ đây." Giao trọn giai đoạn qua đêm, các điểm kiểm tra không bắt buộc được coi là "tiếp tục".
- UD12: "tu gio cu lam theo skill. Dung hoi gi nua. De toi yen tam giao cho ban va di ngu." Giao thường trực mọi giai đoạn còn lại, kể cả các điểm kiểm tra BẮT BUỘC.
- M3 và M10: "Chạy Không hỏi", "cứ làm tới khi nào xong hết theo skill thì thôi", kèm việc giao trọn một sản phẩm (thư mục hồ sơ nộp cho FRO).
- UD6: ngay cả lựa chọn khung cũng được giao ("cái nào dễ đăng nhất mạnh nhất").

Chỗ có thể sâu hơn (liệt kê ngược):
- Không có kế hoạch phân công ngay từ đầu nói rõ người dùng giữ lại phần nào (UD1; M3 chỉ nêu ràng buộc: nạp skill, tuân thủ tuyệt đối).
- Việc giao việc đi vào cả quyền quyết định (khung ở UD6, các điểm kiểm tra BẮT BUỘC ở UD12 và M10), không chỉ các loại nhiệm vụ. Rubric vẫn tính đây là giao việc cao, nhưng vì không có phần nào được nêu là giữ lại, năng lực được giải phóng không có đích đến rõ ràng. Đó là lý do điểm là 9 chứ không phải 10, và nó liên quan trực tiếp đến điểm CR thấp.

#### Cảnh giác nhận thức: 3/10 toàn bộ (Thấp). 1 đến 4' gộp 2/10; Giai đoạn 4.5 3/10; Giai đoạn 5 và 6 4/10

Các biểu hiện cảnh giác quan sát được (toàn bộ):
- UD10: "review must use independent agents". Phản bác cách AI tổ chức phản biện, dẫn đến thiết kế lại (cấp quy trình).
- M2: "agent có dùng skill không đó. bắt buộc load skill...". Phát hiện một lỗ hổng thật, vì các agent kiểm chứng đã được giao việc với quy tắc diễn giải lại (cấp quy trình). M13 đến M15 lặp lại cùng kiểu kiểm tra này.
- M11: chỉ ra rằng Word hiển thị được công thức kiểu LaTeX và yêu cầu cập nhật. Người dùng phát hiện một quyết định trong đầu ra của AI (cấp trình bày).
- M12: "source ghi kiểu author caculation.. chứ. sao lại ghi từ file nào". Người dùng phát hiện lỗi trong ghi chú nguồn của bảng (cấp trình bày và quy ước).
- M4 và M6: kiểm tra xem dữ liệu gốc đã thực sự lên kho mã chưa (cấp hậu cần dữ liệu).

Bằng chứng cảnh giác thấp và chỗ có thể sâu hơn (liệt kê ngược):
- UD6: ngã rẽ về khung là điểm duy nhất mà chính bằng chứng của pipeline mâu thuẫn với luận điểm đang dùng, và người dùng không hỏi gì về kết quả kiểm định thời điểm nêu tên hay về các phương án. Lựa chọn được giao đi với tiêu chí khả năng đăng bài.
- UD9 và UD11: kết quả PASS của Giai đoạn 2.5 và quyết định Major Revision của Giai đoạn 3' được chấp nhận mà không có câu hỏi nào được ghi lại. Cả 14 mục trong lộ trình Giai đoạn 3 được chấp nhận là `will_address`, không phản bác ý kiến phản biện nào.
- M9: lần duy nhất trong phiên này người dùng thách thức một kế hoạch về nội dung của AI là để đòi kiểm chứng ít hơn ("sao phải chạy lại"). Rubric vẫn tính việc phản bác, nhưng lần phản bác này nhằm vào một bước kiểm tra chứ không nhằm vào một nhận định chưa được kiểm chứng.
- Trong cả hai phiên: không ghi nhận yêu cầu nào đòi giải thích một nguồn, con số, ước lượng hay lập luận. Theo định nghĩa của rubric ("User never asks 'where does this claim come from?'"), điều đó đặt cảnh giác cấp nội dung vào dải thấp. Điểm trung bình của Giai đoạn 5 và 6 chỉ phản ánh hai lần phát hiện ở cấp trình bày.

#### Tái phân bổ nhận thức: 2/10 (Thấp)

Những đóng góp quan sát được mà chỉ con người mới đưa ra được:
- Danh sách rút gọn bốn tạp chí (`target_venue.chosen_from`) và hướng dẫn tác giả của FRO (M10), cả hai là bối cảnh chỉ tác giả nắm.
- UD4 "b": giữ mục tiêu 7.000 từ và yêu cầu thêm phân tích. Đây là một phán đoán về phạm vi, và kết quả phía sau là các phân tích mới (kiểm định hoán vị ngẫu nhiên, khác biệt theo nhóm quy mô).
- M6 và M7: lấy và đẩy dữ liệu gốc lên kho (hậu cần, không phải suy luận bậc cao).
- Tài liệu đầu vào có một bản phản biện (red-team) và kế hoạch nâng cấp cho bài báo trước (`materials_at_intake`). Hồ sơ không ghi ai là tác giả, nên chỉ ghi nhận mà không chấm điểm.

Chỗ có thể sâu hơn (liệt kê ngược):
- UD6: sự sụp đổ của khung A là điểm duy nhất mời gọi việc định khung lại ("nhìn kết quả của bạn, giờ tôi nghĩ câu hỏi nghiên cứu là..."). Người dùng đưa ra một tiêu chí mục tiêu thay vì một quan điểm về câu hỏi nghiên cứu.
- UD5, UD12 và M10: năng lực được giải phóng nhờ giao việc được dùng rõ ràng để nghỉ ngơi, và không có lượt nào sau đó quay lại bàn về khung, giả định hay lập luận. Đóng góp của người dùng chủ yếu là điều phối, ràng buộc và hậu cần.

#### Tổng hợp Vùng

- Điểm gộp: DI 9, CV 3, CR 2. CV dưới 4 trong khi AI đang được dùng tích cực, nên quy tắc của rubric cho ra Vùng 2. Mô tả chuẩn của Vùng 2 ghi giao việc "Thấp–Trung bình", nhưng DI ở đây cao, nên nhãn có thêm định tính "dạng giao việc cam kết". Điều này tương ứng với câu của rubric "giao việc mà không tái phân bổ là Vùng 2".
- Giai đoạn 5 và 6 (DI 9, CV 4, CR 2): DI và CV đều ít nhất 4, nhưng không phải cả ba đều ít nhất 7, nên nhánh "mọi tổ hợp khác" của quy tắc cho ra Vùng 2 kèm định tính ("Trung bình").
- Điều kiện kích hoạt kiểm tra lại: không có đề xuất Vùng 3, và tổng điểm 14/30 không vượt quá 24, nên không kích hoạt kiểm tra lại.
- Chéo mô hình: không chạy (`ARS_CROSS_MODEL` chưa đặt), nên không có cờ chênh lệch.

# 8. Báo cáo tự đánh giá của AI

*Lưu ý: báo cáo này do chính AI được đánh giá viết ra; hãy đọc với nhận thức đó.*

```
+--------------------------------------------------+
|  AI Self-Reflection Report                        |
+--------------------------------------------------+
|  Tỉ lệ nhượng bộ của DA       không được ghi log  |
|  (không lưu tag [DA-DECISION]/[DA-REBUTTAL];      |
|   ở Stage 3' mức must_fix của DA được giữ thay    |
|   vì mức nhẹ hơn của R1: 0 lần nhượng bộ)         |
|  Nhượng bộ liên tiếp của DA   không thấy          |
|  Checkpoint được giao cho AI  5 MANDATORY/FULL    |
|  (2.5 và 3' do tác giả xác nhận; 4.5, cổng vào    |
|   Stage 5 và hoàn tất Stage 5 đi qua theo chỉ     |
|   thị thường trực của tác giả)                    |
|  Tác giả bác khuyến nghị      0                   |
|  Cảnh báo sức khỏe hội thoại  0 (không ghi log)   |
|  Chuyển chế độ ý định         0 (không có Socratic)|
|  Bất đồng giữa các mô hình    n/a (không bật)     |
+--------------------------------------------------+
```

**Tóm tắt hành vi.** AI đi hết pipeline và các cổng kiểm soát đã làm đúng việc, nhưng phần lớn là muộn. Những lỗi quan trọng (dẫn sai nguồn, số trong bài lệch với bảng, claim bị trôi) lọt qua Stage 2.5 và hai vòng review, và chỉ bị bắt ở lần kiểm Stage 4.5 làm lại từ đầu. Khi tác giả giao checkpoint, AI vẫn giữ nguyên các FAIL của integrity, không tự vượt qua. AI cũng công bố mọi chỗ không đáp ứng đủ hợp đồng (không có Revision-Evidence Bundle, API bị chặn, không dùng được tectonic) thay vì trình bày tuân thủ một phần như tuân thủ đầy đủ.

**Rủi ro xu nịnh (sycophancy): TRUNG BÌNH** (mức sàng lọc, không phải chẩn đoán). Các chỉ số nhượng bộ không được ghi log nên không hoàn tất được phép sàng lọc, và việc giao checkpoint đã bỏ đi bước con người rà soát ở các cổng integrity. Tác giả nên tự đọc các phát hiện của Stage 4.5 và bản thảo cuối trước khi nộp.

**Sự cố frame-lock.** Phát hiện 1 lần: khung A ("eligibility, not inclusion") thất bại ở kiểm định thời điểm được nêu tên tại Stage 2; pipeline dừng lại và đổi sang khung A′. Không chạy kiểm tra chéo mô hình, nên không loại trừ được khả năng có frame-lock chưa bị phát hiện.

**Mô hình hội tụ.** Không có stage Socratic nào (Stage 1 chạy chế độ quick), nên không áp dụng.

**Những gì AI làm sai.**

- Giao việc cho 3 agent kiểm tài liệu đầu tiên bằng bản tóm tắt quy tắc thay vì file skill; đã sửa sau khi tác giả chất vấn.
- Báo với tác giả rằng agent E6 đã xong khi nó chưa xong; đã đính chính ở tin nhắn kế tiếp.
- Lần chạy tái lập đầu tiên lỗi âm thầm (thiếu `/usr/bin/time`, exit 127) và phải chạy lại.
- Các stage trước (Stage 2.5 và bản viết lại ở Stage 4) để lọt 2 trích dẫn mâu thuẫn với nguồn và 1 con số matched cũ; chỉnh sửa ở Stage 4′ đưa thêm 2 lỗi số liệu và 6 chỗ trôi độ mạnh claim.
- Vòng sửa đầu tiên sinh thêm 2 lỗi MEDIUM mới: sai phiên bản ground rules; một câu gần chép nguyên abstract của Burnham et al.
- Ghi chú bảng dẫn đường dẫn file nội bộ thay vì "Authors' calculations"; tác giả phát hiện.
- Bản LaTeX ở Stage 5 lúc đầu cắt cụt abstract (dấu % chưa escape) và biến dấu sao ý nghĩa thành chữ nghiêng; phát hiện nhờ render trước khi giao.
- Evidence rows (#656) không được lưu thành đối tượng theo schema; bằng chứng chỉ có dưới dạng trích đoạn trong audit trail.

**Nhật ký 7 mode lỗi AI.**

| Mode | Trạng thái cuối ở 4.5 | Lịch sử |
|---|---|---|
| 1 Lỗi code | CLEAR | Stage 2 sửa 3 lỗi (kiểu ngày, tên hệ số, mốc cắt khi đánh giá); Stage 4.5 tái lập 48/48 output từ dữ liệu gốc |
| 2 Trích dẫn bịa | CLEAR | Stage 1 bắt 4 DOI nhớ nhầm trỏ sang bài không liên quan; Stage 4.5 kiểm 33/33 tài liệu, sửa 2 ngữ cảnh dẫn sai và 2 tên sai |
| 3 Kết quả bịa | CLEAR (không có cờ) | mọi con số truy về output đã tái lập |
| 4 Dựa vào lối tắt | CLEAR (không có cờ) | các mối đe dọa do chọn mẫu đều được kiểm (ITT, nhóm bị loại, randomization inference) |
| 5 Biến lỗi thành phát hiện | CLEAR (không có cờ) | kết quả bất ngờ được báo như giới hạn |
| 6 Bịa phương pháp | CLEAR | Stage 2.5 thấy 2 câu phương pháp không khớp code (winsorize, bộ lọc tuần) và đã sửa; Stage 4.5 sửa tuyên bố dữ liệu và cách gán nguồn cho kiểm định CAR |
| 7 Frame-lock | CLEAR | phát hiện ở Stage 2 (khung A), giải quyết bằng khung A′ theo quyết định được tác giả giao |

Không có mode nào bị override.

# 9. Đánh giá chất lượng cộng tác

```
+--------------------------------------------------+
|  Collaboration Quality Score: 64/100              |
+--------------------------------------------------+
|  Định hướng                 [#######   ] 70       |
|  Đóng góp trí tuệ           [#####     ] 52       |
|  Kiểm soát chất lượng       [######    ] 63       |
|  Kỷ luật lặp                [#######   ] 72       |
|  Hiệu quả giao việc         [#####     ] 55       |
|  Học hỏi về quy trình       [#######   ] 74       |
+--------------------------------------------------+
```

**Tổng: 64/100 (Khá).** Tác giả đặt hướng rõ ràng và siết kỷ luật quy trình rất chặt, nhờ đó bắt được các lỗ hổng thật. Nhưng phần lớn các phán đoán thực chất, gồm cả chọn khung bài và mọi checkpoint integrity, đã được giao cho AI.

**Điều làm tốt.**

- Siết phương pháp: "force dùng skill này toàn bộ" và "bắt buộc load skill mỗi khi làm task gì đó" làm lộ ra việc các subagent chỉ làm theo bản tóm tắt quy tắc. Việc sửa lỗ hổng này nâng chất lượng mọi lần kiểm sau đó.
- Đòi reviewer độc lập cho Stage 3′ ("review must use independent agents"), nhờ đó có hội đồng ngữ cảnh mới phát hiện hai lỗi do vòng sửa đầu gây ra.
- Bắt những lỗi trình bày mà reviewer sẽ để ý: "source ghi kiểu author caculation.. chứ", và yêu cầu equation Word gốc.
- Đưa dữ liệu lên: đẩy dữ liệu gốc cho phép tái lập toàn bộ, là bằng chứng mạnh nhất chống lại Mode 1 và Mode 3.

**Cơ hội bị bỏ lỡ.**

- Quyết định khung bài ("cái nào dễ đăng nhất mạnh nhất") và mọi checkpoint integrity đều được giao; tác giả chưa đọc các phát hiện của Stage 4.5 hay bản thảo cuối trước khi gói nộp được dựng.
- Guide của tạp chí, tên tác giả và bài báo trước đến muộn hoặc không có, nên không chạy được kiểm tra tự đạo văn (D2), và quy ước của tạp chí chỉ lộ ra ở Stage 5.
- Tác giả hỏi vì sao cần tái lập ("các file hiện có là khớp mà … sao phải chạy lại") thay vì chủ động yêu cầu; chính lần tái lập đó phát hiện p-value phụ thuộc phiên bản.

**Khuyến nghị cho lần sau.**

1. Đọc toàn bộ báo cáo integrity Stage 4.5 và bản thảo cuối trước khi nộp. Việc kiểm của AI có giới hạn: API bị chặn, không đọc được toàn văn.
2. Tự ra quyết định khung bài khi pipeline dừng để hỏi, và nói rõ đóng góp nào bạn sẽ bảo vệ trước reviewer.
3. Cung cấp guide đầy đủ của tạp chí, danh sách tác giả và bài báo liên quan trước đó ngay từ intake.
4. Đưa dữ liệu gốc (hoặc đường dẫn tới nó) lên repo từ phiên đầu, để lần kiểm integrity nào cũng tái lập được.
5. Giữ chuỗi patch #390 từ vòng sửa đầu tiên; yêu cầu rõ điều này nếu một stage đề nghị viết lại toàn bộ.

**Giá trị do con người và do AI đóng góp.**
- Từ tác giả: câu hỏi nghiên cứu, dữ liệu và code nền, lựa chọn tạp chí, việc đòi quy trình đầy đủ và độc lập (điều giúp các vòng review và integrity phát hiện được lỗi), dữ liệu gốc để tái lập, và hai sửa đổi về trình bày.
- Từ AI: kiểm tra tài liệu và trích dẫn, các phân tích bổ sung khi sửa bài, viết và sửa văn bản, các phát hiện và sửa lỗi integrity, đóng gói.

Phán đoán khoa học về việc bảo vệ khung bài nào đã được giao cho AI. Vì vậy luận điểm chính của bài được định hình bởi khuyến nghị của AI chứ không phải quyết định của tác giả.
