# Map from manuscript tables and figures to the output files that produce them

All files are produced by the scripts in `code/` from `data/raw/` (run from the project root; see ars/stage4_5_integrity/repro/REPRO_REPORT.md).

| Manuscript item | Output file(s) | Script |
|---|---|---|
| Table 1 | output/revision/t1_descriptives.csv | code/analysis_revision.R |
| Table 2 | output/revision/t2_baseline_clean.csv; output/revision2/t_matched_weighted.csv | analysis_revision.R; analysis_revision2.R |
| Table 3 | output/revision/t_itt.csv | analysis_revision.R |
| Figure 1 | output/revision/t_event_study.csv (pre-trend tests: output/revision/t_pretrend_wald.csv) | analysis_revision.R; figure1.R |
| Figure 2 | output/revision2/t_itt_event_study.csv | analysis_revision2.R; figure2.R |
| Table 4 | output/revision2/t3_car_portfolio_clean_est.csv | analysis_revision2.R |
| Table 5 | output/revision/t4c_spike_test.csv; output/revision/t4b_rebalance_groups.csv (reference-day regression: output/revision/t4_rebalance_reg.csv) | analysis_revision.R |
| Table 6 | output/revision/t5_segments.csv; output/table7b_rebalance_by_segment.csv | analysis_revision.R; analysis.R |
| Table 7 | output/revision/t6_volatility.csv; output/revision/t7_robustness.csv | analysis_revision.R |
| Table 8 | output/revision/t7_robustness.csv; output/revision2/t_matched_weighted.csv; output/revision2/t_post_drift.csv; output/revision2/t_sector.csv; output/revision/t_wild_bootstrap.csv; output/revision/t6_randomization_inference.csv | analysis_revision.R; analysis_revision2.R |
| Table 9 | output/revision/t8_named_excluded.csv; output/revision/t8c_named_by_stock.csv; output/revision2/t_named_ex_bsr.csv | analysis_revision.R; analysis_revision2.R |
| Table A.1 | output/revision/tA1_balance.csv | analysis_revision.R |
