# Stage 4.5 reproduction from raw data (Modes 1/3/6 evidence)

Date: 2026-09-24. Environment: Linux, R 4.3.3, fixest 0.14.2 (built from GitHub lrberge/fixest), MatchIt 4.5.5, data.table 1.14.10, ggplot2 (Ubuntu r-cran). Full sessionInfo in sessionInfo.txt.
Input: data/raw/*.csv (405 files, commit 8da62ce) + data/hose_listing_VCI_20260924.csv.
Scripts run in a clean copy, in order: analysis.R, analysis_extensions.R, analysis_revision2.R (evaluates analysis_revision.R), figure1.R, figure2.R. All exit 0 (logs log_*.txt).

## Result
48 of 48 output CSVs regenerated. Every coefficient, SE, t, N, CAR and descriptive matches the committed output to rtol 1e-6.
Only difference: p-values of the joint pre-trend Wald tests (output/revision/t_pretrend_wald.csv, output/table_pretrend_wald.csv). F statistics are identical to 12 digits; fixest 0.14.2 uses G-1 cluster degrees of freedom in the denominator, the author's older fixest used residual df. Under G-1 (consistent with the clustered t-tests on coefficients): full sample F = 6.66, p < 0.001; ITT F = 7.59, p < 0.001; matched sample F = 1.72, p = 0.092 (was 0.056). Conclusions unchanged; the manuscript is updated to the G-1 values and the committed CSVs are replaced by the rerun.

## Portability fixes to code
Absolute setwd()/readLines() paths to the author's Mac replaced by project-root-relative paths; figure2.R y-axis label shortened (was clipped) and figure regenerated.
