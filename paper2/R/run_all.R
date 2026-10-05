# run_all.R -- single entry point for the price-limit paper (Paper C).
# Runs every script that produces a number, table or figure in manuscript_final.Rmd, in dependency order,
# then renders the manuscript. Seeds are fixed inside each script. Run from any directory:
#   Rscript /home/user/Black_litterman_2/paper2/R/run_all.R
root <- "/home/user/Black_litterman_2/paper2"
steps <- c(
  "40_zoo.R",                  # 22 characteristics, Fama-MacBeth, 4 event tests, family control (C1-C3)
  "42_rd.R",                   # binned next-day returns for Figure 2 (C5) and exact-tick checks (C6, C7)
  "47_da_response.R",          # decomposition, benchmarks, controls, comparisons, subsamples (C9b, C11-C17)
  "48_revision.R",             # week/block clustering, specified split, KRX split, attention proxies, outliers (C18-C25)
  "50_sample_description.R",   # sample statistics for Section 3 (C26)
  "51_tick_grid_diagnostic.R", # vendor price adjustment diagnostic (C27)
  "49_final_figures.R",        # Figures 1 and 2
  "46_verify_C.R")             # verification tests T1-T6
for (s in steps) { cat("==>", s, "\n"); t0 <- Sys.time(); status <- system2("Rscript", file.path(root, "R", s), stdout = FALSE, stderr = FALSE)
  if (status != 0) stop("script failed: ", s); cat("    done in", format(round(Sys.time() - t0, 1)), "\n") }
# 48_revision.R reuses the data preparation in lines 1-44 of 47_da_response.R; keep those lines stable.
rmarkdown::render(file.path(root, "manuscript", "manuscript_final.Rmd"), "word_document", quiet = TRUE)
system2("python3", c(file.path(root, "manuscript", "style_docx.py"), "tab", file.path(root, "manuscript", "manuscript_final.docx"), file.path(root, "manuscript", "manuscript_final_styled.docx")))
cat("manuscript rendered\n")
