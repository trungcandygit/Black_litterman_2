# Do price limits delay price discovery? Overnight gaps after limit closes in Vietnam

Data, code and output tables for the article (PLOS ONE submission).

- `data/raw/`: daily open, high, low, close and volume of HOSE-listed stocks (vnstock 4.0.4, source VCI, retrieved 24 September 2026); `data/hose_listing_VCI_20260924.csv` is the listing file and `data/fetch_log.txt` the retrieval log.
- `paper2/R/`: R scripts. `run_all.R` runs them in order; the paths at the top of each script point to the repository root and must be edited to your local copy. R 4.3.3 (packages sandwich 3.1.0, lmtest, ggplot2).
- `paper2/output/tables/`: output tables (CSV) behind every number in the article; `paper2/output/figures/`: the two figures.
- `paper2/final/PLOS_ONE/`: the submission files (manuscript, figures, supporting information, cover letter).
