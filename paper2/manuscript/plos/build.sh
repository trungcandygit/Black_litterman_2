#!/bin/bash
# Build the PLOS ONE submission files from manuscript_final.Rmd
set -e
cd "$(dirname "$0")"
python3 build_plos.py
python3 style_plos.py ref ../reference.docx plos_reference.docx
for f in manuscript_plos S1_Appendix; do Rscript -e "rmarkdown::render('$f.Rmd', quiet=TRUE)" >/dev/null 2>&1; done
python3 style_plos.py tab manuscript_plos.docx manuscript_plos_final.docx
python3 style_plos.py tab S1_Appendix.docx S1_Appendix_final.docx
Rscript -e "rmarkdown::render('cover_letter.Rmd', quiet=TRUE)" >/dev/null 2>&1
P=../../final/PLOS_ONE; mkdir -p $P
cp manuscript_plos_final.docx $P/Manuscript_PLOS_ONE.docx; cp S1_Appendix_final.docx $P/S1_Appendix.docx; cp cover_letter.docx $P/Cover_letter.docx
python3 -c "
from PIL import Image
for s,d in (('F1_characteristics','Fig1'),('F2_break_at_limit','Fig2')):
    Image.open('../../output/figures/'+s+'.png').convert('RGB').save('$P/'+d+'.tif', compression='tiff_lzw', dpi=(300,300))"
(cd ../../output/tables && rm -f ../../final/PLOS_ONE/S1_File.zip && zip -q ../../final/PLOS_ONE/S1_File.zip C*.csv)
