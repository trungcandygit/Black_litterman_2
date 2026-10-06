#!/bin/bash
# Build the Multidisciplinary Science Journal package from manuscript_final.Rmd and the journal template
set -e
cd "$(dirname "$0")"
python3 build_msj.py
Rscript -e "rmarkdown::render('manuscript_msj.Rmd', quiet=TRUE)" >/dev/null 2>&1
Rscript -e "rmarkdown::render('S1_supplementary.Rmd', quiet=TRUE)" >/dev/null 2>&1
python3 fill_template.py msj_template.docx manuscript_msj.docx manuscript_msj_template.docx
python3 - <<'P'
from docx import Document
from docx.shared import Pt
d = Document("S1_supplementary.docx")
for p in d.paragraphs:
    p.paragraph_format.line_spacing = 1.0; p.paragraph_format.alignment = 3
    for r in p.runs: r.font.name = "Calibri"; r.font.size = Pt(10); r.font.bold = False
d.save("S1_supplementary.docx")
P
O=../../final/MSJ; mkdir -p $O
cp manuscript_msj_template.docx $O/Manuscript_MSJ.docx
cp S1_supplementary.docx $O/Supplementary_Material_S1.docx
python3 -c "
from PIL import Image
for s,d in (('F1_characteristics','Figure1'),('F2_break_at_limit','Figure2')):
    Image.open('../../output/figures/'+s+'.png').convert('RGB').save('$O/'+d+'.tif', compression='tiff_lzw', dpi=(300,300))"
