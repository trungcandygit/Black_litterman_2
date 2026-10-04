# Decisions log (zero-question mode; written BEFORE results were seen)

Date: 2026-10-04. All decisions below were fixed ex ante, before any out-of-sample result of the new models was computed.

1. Paper type: empirical quantitative-finance article, journal-neutral, APA-like author-date. Output: Markdown + DOCX (Pandoc). No PDF (no LaTeX engine available).
2. Citation policy: the unpublished earlier manuscript is not cited and its text is not reused. Only the classic methodological literature is cited. Network policy blocks Crossref/doi.org, so DOI verification could not be run; every reference is listed with a verification status in `process/reference_verification.md`.
3. Primary design (inherited): 25 bank stocks, monthly, 36-month rolling window, one-month-ahead OOS, 106 steps (Aug 2017 - May 2026), long-only, 30% cap, Sharpe in excess of annual 10y VGB yield.
4. Replication anchor: BL-K_IO v1 (single view, k=4, sample covariance, tau=1/36, Omega = tau P S P') is re-implemented as benchmark, not as the contribution.
5. Proposed model (BL-KMV, "multi-view, stability-weighted"): K absolute cluster views on cluster means; q_c = equilibrium + calibrated in-window score slope x cluster score deviation; Omega_c = tau p_c S p_c' / stability_c; Ledoit-Wolf constant-correlation covariance; max-Sharpe QP with cap.
6. k selection rule for the MAIN specification (fixed ex ante, uses no returns): largest k in {3..6} whose weighted mean bootstrap Jaccard stability >= 0.70, fallback k=3. Alternatives (fixed k=4, inner-window IC rule) are reported as ablations and counted as trials in the deflated Sharpe ratio.
7. Multiple-testing discipline: the number of portfolio configurations evaluated is counted in a trials ledger (output/rds/trials.rds) and used for the deflated Sharpe ratio and Hansen SPA.
8. Sharpe-difference inference: Ledoit-Wolf (2008)-type studentized circular block bootstrap, 5,000 resamples; reported for the full sample and the two regimes.
9. Regimes (inherited, fixed): P1 Aug 2017-Dec 2021; P2 Jan 2022-May 2026.
10. Broad-universe test: ~390 HOSE stocks, daily 2024-08-21..2026-09-23, weekly rebalance, equilibrium proxy = trailing dollar-volume weights (no market-cap data in raw files); explicitly low-power external-validity check.
11. Risk-free: annual 10y VGB yield by calendar year (read from authors' earlier figure; approximate) converted to monthly; sensitivity: zero and halved.
12. Honest reporting: if the proposed model does not beat benchmarks, that is reported as is.

## Amendment A1 (before any full-sample result was inspected; only the first 8 of 106 windows were smoke-tested for code errors)
13. Minimum-cluster-size guard: the admissible k set is {3..6} intersected with k <= floor(n/3) (average cluster size >= 3); when floor(n/3) < 3 (the first windows, n = 7 banks) k = 2 is used. Reason: with n = 7 and k = 5-6 the bootstrap-stability rule is trivially satisfied by singleton clusters. The rule remains return-free.

## Amendment A2 — Pivot to the factorial attribution study (Paper B), after the clustering-view study (Paper A) returned null results
Date: 2026-10-04. Trigger: user asked to brainstorm another idea given the wider data. Brainstorm, FINER scoring, RQ Brief and Devil's Advocate Checkpoint 1 are in `process/01_brainstorm_RQ_brief.md`. Paper A (clustering views) stays as a documented companion/ablation; its engine and results are reused.
14. Primary RQ: attribution of BL Sharpe variance to anchor / view / covariance / cap, with replication on the 347-stock weekly universe.
15. Factorial (fixed before computing any factorial result): anchor {CAP, EW, ERC, SHR(50/50 cap-equal)} x view {NONE, MOM, LOWVOL, COMP, CLUSTER} x covariance {SAMPLE, LW} x cap {0.30, none} = 80 cells per universe; objective = max Sharpe QP; delta for non-cap anchors from the anchor portfolio's own window return/variance (clipped [0.5,10]).
16. Views: terciles of the relevant score (MOM = z(mom); LOWVOL = -z(vol); COMP = z(mom)-z(vol)) as three absolute views with calibrated tilt (in-window slope, floored at 0) and Omega = tau p S p'/1; CLUSTER = the Paper-A BL-KMV view (stability-selected k, stability-scaled Omega).
17. Inference: circular block bootstrap over months (weights fixed) of the whole factorial -> percentile intervals for ANOVA shares and marginal contrasts (Holm); label-permutation noise-only benchmark for shares; equivalence margin 0.10 annualized Sharpe for views.
18. Hypotheses H1-H5 as in the brief; H1/H5 flagged as motivated by Paper A's results (not independent); the broad universe is the confirmation sample; no design change after viewing bank results (any change gets logged here).

## Amendment A3 — Paper C (characteristics + price limits), pre-registered 2026-10-04 before computation
19. Family of 26 primary tests, estimators, FDR/Holm/HLZ controls, discovery/confirmation split (first half of the weekly cross-sections vs second half), and survival rule fixed in `process/03_brainstorm_round2.md`. All 26 results will be reported.
20. Paper B stays as a separate manuscript; Paper C results may be linked to it in the discussion only after C is complete.
