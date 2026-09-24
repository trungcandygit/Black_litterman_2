"""Stage 5 packaging: anonymized replication package (supplementary material) + submission README.

Run after build_stage5.py and convert.py.
"""
import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "submission"
ZIP = OUT / "Supplementary_Replication_Package.zip"

REPL_README = """# Replication package

Manuscript: "Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification" (submitted to Finance Research Open; anonymized for review).

## Contents
- `data/raw/*.csv`: daily open, high, low, close and volume for the 405 common stocks listed on HOSE on 24 September 2026, 1 October 2024 to 23 September 2026, downloaded with the open-source `vnstock` library (VCI source); `data/hose_listing_VCI_20260924.csv` lists the universe; `fetch_prices.py` is the download script.
- `code/`: R scripts that produce every table and figure.
- `output/`: the result files the scripts write; `output/TABLE_SOURCE_MAP.md` maps each manuscript table and figure to its file.

## How to reproduce
Run from the package root (R >= 4.3; packages data.table, fixest, MatchIt, ggplot2):

    Rscript code/analysis.R
    Rscript code/analysis_extensions.R
    Rscript code/analysis_revision2.R      # also evaluates code/analysis_revision.R
    Rscript code/figure1.R
    Rscript code/figure2.R

A clean re-run (R 4.3.3, fixest 0.14.2, MatchIt 4.5.5, data.table 1.14.10) reproduces all 48 output tables to a relative tolerance of 1e-6. Joint pre-trend Wald p-values use the number of stock clusters minus one as denominator degrees of freedom (fixest >= 0.14 default); older fixest versions report p-values with residual degrees of freedom (F statistics identical).

## Data terms
Prices and volumes are public market data retrieved through vnstock from VCI. Users should check the data provider's terms before redistributing the raw files.
"""


def add_tree(z, src, arc):
    for p in sorted(src.rglob("*")):
        if p.is_file() and p.name != ".DS_Store":
            z.write(p, f"{arc}/{p.relative_to(src)}")


with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("README.md", REPL_README)
    add_tree(z, ROOT / "code", "code")
    add_tree(z, ROOT / "data" / "raw", "data/raw")
    z.write(ROOT / "data" / "hose_listing_VCI_20260924.csv", "data/hose_listing_VCI_20260924.csv")
    z.write(ROOT / "fetch_prices.py", "fetch_prices.py")
    for p in sorted((ROOT / "output").rglob("*")):
        if p.is_file() and p.name != ".DS_Store" and not p.name.endswith("_log.txt"):
            z.write(p, f"output/{p.relative_to(ROOT / 'output')}")

(OUT / "manuscript_anonymized.md").unlink(missing_ok=True)

files = sorted(p for p in OUT.rglob("*") if p.is_file() and p.name != "README_NOP_BAI.md")
manifest = "\n".join(f"| `{p.relative_to(OUT)}` | {p.stat().st_size:,} | `{hashlib.sha256(p.read_bytes()).hexdigest()[:16]}` |" for p in files)

SRC_MD = ROOT / "ars/stage4_5_integrity/correction_round5/manuscript_v9.clean.md"
SRC_SHA = hashlib.sha256(SRC_MD.read_bytes()).hexdigest()
README = f"""# Gói nộp bài: Finance Research Open (Elsevier)

Bài: **Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification**

Nguồn: bản thảo cuối v9 (`ars/stage4_5_integrity/correction_round5/manuscript_v9.clean.md`, SHA-256 `{SRC_SHA}`), đã qua Stage 4.5 của ARS v3.22.1 và các vòng proofreading, stop-slop. Mọi file dưới đây đã điền đủ thông tin, bạn không cần sửa gì thêm.

## 1. Upload lên Editorial Manager

| File | Chọn loại file (Item type) | Ghi chú |
|---|---|---|
| `manuscript_anonymized.docx` | Manuscript (anonymized) | Bản Word một cột; công thức là equation của Word; bảng sửa được; không có tên tác giả |
| `title_page.docx` | Title page (with author details) | 4 tác giả, đơn vị, tác giả liên hệ, email, ORCID, lời cảm ơn, competing interests, funding, CRediT, data availability |
| `declaration_of_competing_interest.docx` | Declaration of interest | Đúng câu chuẩn của Elsevier "no known competing financial interests...". Nếu hệ thống bắt dùng declarations tool, chọn "I have nothing to declare" và tải file tool sinh ra lên (nội dung giống hệt file này) |
| `highlights.docx` | Highlights | 5 ý, mỗi ý ≤ 85 ký tự |
| `figures/Figure_1.pdf`, `figures/Figure_2.pdf` | Figure | PDF vector. Có thể thay bằng PNG 600 dpi (rộng 4500 px) cùng tên |
| `cover_letter.docx` | Cover letter | Đã ký tên tác giả liên hệ, ngày 24/9/2026 |
| `Supplementary_Replication_Package.zip` | Supplementary material | Dữ liệu gốc (405 file giá), code R, kết quả; đã ẩn danh |
| `manuscript_anonymized.tex` + `manuscript_anonymized.pdf` | (không bắt buộc) | Bản LaTeX (elsarticle) và PDF để đọc soát; chỉ nộp nếu muốn dùng LaTeX thay cho Word |

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
- **Tái lập kết quả:** chạy lại từ dữ liệu gốc, cả 48 file kết quả đều khớp.

## 3. Danh sách file (kích thước, SHA-256 rút gọn)

| File | Bytes | SHA-256 (16) |
|---|---|---|
{manifest}
"""
(OUT / "README_NOP_BAI.md").write_text(README)
print(README[-2000:])
