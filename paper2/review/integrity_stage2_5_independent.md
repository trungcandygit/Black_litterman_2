# Academic Integrity Verification Report (Stage 2.5, Mode 1, independent)

Manuscript: `paper2/review/round1/manuscript_C_v3.md` (source `paper2/manuscript/manuscript_C.Rmd`). Verified 2026-10-04. Files 04_/05_/06_ in `process/` were not read. All recomputation used my own code in the scratchpad (not the author's scripts), from `data/raw/*.csv`.

## Verification Mode
Initial Verification (Stage 2.5, pre-review).

## Verdict
**FAIL**

Reasons (any one suffices under the task rule): (1) one MAJOR_DISTORTION ("independent replication" of the GitHub result); (2) Failure Mode 1 (implementation bug passing self-review) SUSPECTED, with evidence: NA-propagation in `R/41_limits_robust.R` silently truncates the samples behind the Table 6 liquidity-tercile rows, Table 6 control column, and the close-to-close rows of Tables 5 and 6; (3) Failure Mode 6 SUSPECTED (low severity: Methods text differs from code/log in three places). All headline numbers (abstract, Tables 2, 3, 4, 7, 8, Table 1 counts) were reproduced exactly. All 20 references exist and are bibliographically correct. No hallucinated reference.

## Verification Summary

| Category | Total | Passed | Issues |
|---|---|---|---|
| Reference existence | 20 (19 literature + 1 GitHub) | 20 | 0 |
| Bibliographic accuracy | 20 | 20 | 0 |
| Ghost citations | -- | -- | 0 orphan / 0 dangling |
| Citation context (Phase B) | 14 contexts (>=30%) | 13 | 1 (GitHub "independent replication") |
| Statistical/data surfaces (Phase C) | 12 surfaces recomputed | 8 reproduced exactly | 4 (Table 6 tercile/control columns; Table 5/6 close-to-close n; Table 1 / abstract stock-day denominator; Table 7 "Events" column) |
| Internal consistency | -- | Fail | 4 inconsistencies (see M1, S3, M4, M6) |
| Originality D1 | 9 passages web-searched + n-gram vs README and sibling manuscripts | 9 | 0 CLOSE_MATCH / VERBATIM |
| Self-plagiarism D2 | author names not supplied (placeholder) | not run for names | sibling manuscripts A/B overlap = 2% (boilerplate and references only) |
| Claim verification (E) | 22 registered claims; 19 HIGH-IMPACT (100%) + 3 RANDOM | see E table | 1 MAJOR_DISTORTION, 3 MINOR_DISTORTION |

## Phase A: Reference verification (A0 not available; A1/A2 by WebSearch, audit trail below)

| # | Reference | Verdict | Evidence (source) |
|---|---|---|---|
| 1 | Amihud 2002, JFM 5(1) 31-56 | VERIFIED | Penn-hosted PDF / ResearchGate: JFM 5 (2002) 31-56 |
| 2 | Bali, Cakici, Whitelaw 2011, JFE 99(2) 427-446 | VERIFIED | NYU Stern PDF; SCIRP |
| 3 | Benjamini & Hochberg 1995, JRSS-B 57(1) 289-300, doi 10.1111/j.2517-6161.1995.tb02031.x | VERIFIED | Wiley/RSS page |
| 4 | Berkman & Lee 2002, PBFJ 10(5) 517-530 | VERIFIED | search results (abstract: limit-hit stocks show more price continuations) |
| 5 | Berkman, Koch, Tuttle, Zhang 2012, JFQA 47(4) 715-741 | VERIFIED | SSRN 1625495 / Missouri State repository; doi 10.1017/S0022109012000270 |
| 6 | Brennan 1986, JFE 16(2) 213-233 | VERIFIED | search results (Brennan RePEc listing and citing literature) |
| 7 | Cameron, Gelbach, Miller 2011, JBES 29(2) 238-249 | VERIFIED | IDEAS RePEc v29y2011i2p238-249 |
| 8 | Chen 1993, PBFJ 1(2) 139-153 | VERIFIED | IDEAS pacfin v1y1993i2p139-153; ScienceDirect 0927538X93900053 |
| 9 | Cho, Russell, Tiao, Tsay 2003, JEF 10(1-2) 133-168 | VERIFIED | Semantic Scholar record; JEF 10(1) 133-168 |
| 10 | Corwin & Schultz 2012, JF 67(2) 719-760 | VERIFIED | Wiley; EconPapers |
| 11 | Fama & MacBeth 1973, JPE 81(3) 607-636 | VERIFIED | IDEAS ucp jpolec v81y1973i3p607-36 |
| 12 | Harvey, Liu, Zhu 2016, RFS 29(1) 5-68 | VERIFIED | NBER WP 20592 / RFS (the log's "recalled" caveat can be removed) |
| 13 | Holm 1979, SJS 6(2) 65-70 | VERIFIED | Semantic Scholar; JSTOR record |
| 14 | Imbens & Lemieux 2008, J Econometrics 142(2) 615-635 | VERIFIED | IDEAS eee econom v142y2008i2p615-635 |
| 15 | Kim & Rhee 1997, JF 52(2) 885-901 | VERIFIED | Wiley page |
| 16 | Lou, Polk, Skouras 2019, JFE 134(1) 192-213 | VERIFIED | IDEAS / EconPapers |
| 17 | Newey & West 1987, Econometrica 55(3) 703-708 | VERIFIED | IDEAS ecm emetrp v55y1987i3p703-08; Econometric Society (the log's "recalled" caveat can be removed) |
| 18 | Parkinson 1980, J Business 53(1) 61-65 | VERIFIED | IDEAS ucp jnlbus v53y1980i1p61-65 |
| 19 | Veeraraghavan, Nguyen (Mai Truc Thi), Truong 2007, SSRN 1009042 | VERIFIED | papers.ssrn.com abstract_id=1009042 (Madhu Veeraraghavan, Mai Truc Thi Nguyen, Cameron Truong; 20th AFBC 2007) |
| 20 | tungtran0911 (2026), GitHub vn-equity-factors | VERIFIED exists (fetched raw README); see Phase B/E for context errors | README: 1.694% (t=39.47) "At or near the ceiling (>= +6.5%)", n=26,705; +3% to +6.5%: -0.388%; sample 2016-01-04 to 2026-09-25; 887,291 bars for 404 of 405 stocks |

Ghost-citation check: all 20 entries are cited in the body and every in-text citation maps to the list (Brennan; Kim & Rhee; Chen; Berkman & Lee; Cho et al.; Veeraraghavan et al.; tungtran0911; Benjamini & Hochberg; Harvey et al.; Berkman et al.; Bali et al.; Parkinson; Amihud; Corwin & Schultz; Fama & MacBeth; Newey & West; Holm; Cameron et al.; Imbens & Lemieux; Lou et al.).

## Phase B: Citation context (14 contexts checked, 70% of 20)
Supported: Kim & Rhee (support for all three critical hypotheses); Chen 1993 (serial correlation inversely related to limit range); Berkman & Lee (more frequent continuations after limit hits); Cho et al. (acceleration toward the upper bound, weaker toward the lower); Veeraraghavan et al. (momentum, volume, price limits, Vietnam 2000-2006); Berkman et al. 2012 (overnight gains then intraday reversal, retail-attention stocks, high net retail buying at the open); Lou et al. (overnight vs intraday persistence, investor heterogeneity); Brennan (futures price-limit theory); Harvey et al. (|t|=3); Benjamini-Hochberg; Cameron et al.; Imbens-Lemieux (RD plotting practice); Bali et al. (MAX); Corwin-Schultz.
Not supported as written: tungtran0911 used as "independent replication" and "longer sample ... independent public analysis" (see E-claim 14 / S2). The two numbers (1.69%, -0.39%) and the 2016-2026 sample are correct.

## Phase C: independent recomputation (own code; raw CSVs; window from 2024-08-21, 519 dates, 347 stocks with >=95% non-missing close)

| Surface | Manuscript | My recomputation | Status |
|---|---|---|---|
| Ceiling t+1 mean, t, n, dates (Table 3) | 1.66%, 4.91, 3,187, 446 | 1.6602, 4.908, 3,187, 446 (same-day weights); 1.667, 4.92 with strictly lagged weights | Reproduced |
| Ceiling t+1..t+5; floor t+1; floor t+1..t+5 | 1.45/4.01; -0.71/-5.33 (2,105, 319); -1.76/-4.75 | 1.4497/4.008; -0.713/-5.326 (2,105, 319); -1.760/-4.751; halves 2.28/14.36, -2.97/-5.12 | Reproduced |
| Decomposition (Table 4): ceiling gap/intraday/cc | 2.23 (two-way t 9.8) / -0.53 (-3.5) / 1.66 (4.8); n 3,220, 335 stocks | 2.235 (9.75) / -0.532 (-3.46) / 1.658 (4.83); 3,220, 335 | Reproduced |
| Floor gap/intraday | -0.99 (-4.7) / 0.31 (1.4); n 2,122 | -0.994 (-4.70) / 0.308 (1.41); 2,122 | Reproduced |
| Exact tick rule ceiling | 2.76 (13.5) / -0.73 (-5.3) / 1.97 (7.0); n 1,666 | 2.758 (13.51) / -0.734 (-5.29) / 1.972 (7.01); 1,666 | Reproduced |
| Pile-up (Table 1) | 200,468 stock-days; 2.21% in 6.5-7.1%, etc. | Reproduced exactly only if ALL 405 files are used with consecutive-observation returns (200,468). For the 347 analysed stocks: 178,773 calendar-adjacent returns (C13 agrees) or 179,140 consecutive; 1.98% in 6.5-7.1%, 0.288% in 6.0-6.5%, 0.010% in 7.1-8.0% | Counts reproduced, but wrong population (S3) |
| Fama-MacBeth slopes, NW(4) t (own panel code; same sample screens, 79 cross-sections) | REV1W 0.034/0.41; LNDVOL 0.024/0.27; MAX -0.001/-0.02; AMIHUD -0.022/-0.26; MOM6M 0.094/1.12; MOM3M 0.131/1.55; disc/conf t as in Table 2 | Identical to the digit for all six, including discovery/confirmation t; MOM3M lag 2/8: 1.49/1.88; MDE 0.236 | Reproduced. Note MOM3M window is 59 days, not 60 (M5) |
| Table 5 first block (ceiling vs 5-6.5% up): gap, intraday, 5-day-from-open | 2.67 (13.7); -0.34 (-2.2); -0.06 (-0.2); n 3,136/1,696 | 2.67 (13.71); -0.34 (-2.21); -0.06 (-0.23); 3,136/1,696; vs 3-5%: 2.40 (11.35), -0.32, -0.47 (-2.29) | Reproduced |
| Table 5 close-to-close rows | 2.29 (6.7), n 2,819/1,480; 2.00 (5.4) | NA-safe market gives 2.31 (7.4) and 2.05 (6.0) on all 3,136 events | Sample silently truncated (S1/M2) |
| Section 4.6: -0.55 (t -3.7), -0.79 (t -3.7), 58% negative intraday, 3,136 events | as stated | -0.55 (-3.73), -0.79 (-3.73), 58.4%, 3,136 | Reproduced (date-clustered) |
| Table 6: all, halves, crash-excluded, locked/not locked (gap, intraday) | e.g. locked 2.91 (3.0)/-1.30 (-6.0); not locked 2.14 (16.3)/-0.41 (-4.2) | Reproduced (locked n=516, not locked 2,620) | Reproduced |
| Table 6: liquidity-tercile rows, control column | tercile gaps 3.38/3.30/1.88; controls 2.20 (11.6) in "all" and "first half"; floors -0.99 | Published rows rest on only 451 ceiling events (131/166/154), all with t between day 164 and 232, and on 29/23/17 floor events. NA-safe full-sample ceiling terciles: gap 2.78 (15.5), 2.91 (19.2), 1.45 (6.5); floor terciles gap -0.28 (-1.1), -1.92 (-6.3), -0.76 (-4.7) | NOT reproducible as described (S1) |
| Table 7 / abstract: gap vs controls 2.70 (20.2), intraday -0.50 (-6.0), vs market 2.24 (9.7), cc vs controls, equal-weighted 2.38 | as stated | 2.697 (20.17); -0.496 (-6.00); 2.244 (9.72); floor -1.754 (-4.00), 0.136; ceiling cc vs ctrl 2.162 (18.0); floor cc vs ctrl -1.651 (-3.37) | Reproduced |
| Section 4.7 attrition (8 and 4 missing next day; <0.01 pp) | as stated | C12 values 1.664 vs 1.658; -0.6917 vs -0.6919 | Consistent with saved table |
| 59 bp bank Corwin-Schultz proxy | about 59 | 58.8 | Reproduced |
| C14 lag sensitivity, MDE; C15 (816 = floor(0.05/6.12e-5)); BH range 2.6e-06 to 4.0e-04 | as stated | Consistent with C3/C14/C15 and my MOM3M checks | Reproduced |
| Rmd vs v3.md | -- | knit of the Rmd equals v3.md except caption markup, so v3.md has no hand edits | OK |

Hand-typed results in the Rmd that do not come from saved tables: Table 1 caption "200,468"; "about 0.05%" (counts only the upside tail: 96 stock-days; both tails 147 = 0.073%); "1.69%" and "0.39%" (GitHub, correct); "21 banks" (correct); "14 candidate ideas", "three manuscripts" (match the brainstorm log); "115 trading days", "79", "39/40" (correct); conclusion "+1.7%" (correct). The "58%" figure and the attrition counts are computed from saved rds/CSV.

Look-ahead audit. (i) Characteristics: the code uses only rows <= t. I confirmed this empirically with the author's own panels: in `zoo_panel_LA.rds` (future data scrambled after day ~250) X is bit-identical for all 27 cross-sections up to t=250 and first differs at t=255, while Y differs from t=250; my independent construction also uses only <= t. (ii) Event definition uses day t only; outcomes begin at t+1. (iii) Mild forward-looking sample selection, not outcome leakage: the characteristic sample requires non-missing returns on t+1..t+5, and Table 3 requires complete t+1..t+5, so events/stocks that halt are dropped conditional on the future (C12 shows next-day attrition is negligible: 8/4 events; t+5 attrition is not tabulated). (iv) Table 3 benchmark weights use the 60-day average dollar volume ending on day t+1 (same day as the return), not "trailing"; with strictly lagged weights the result is 1.667 versus 1.660, so immaterial. (v) `41_limits_robust.R` conditions the market and control sets on finite t+5 close (future availability): immaterial.

Root cause of S1 (code): in `R/41_limits_robust.R`, `mk_cc1 <- sum(wm[okm] * Rd[t+1, okm])` returns NA on any date when any weighted stock has no next-day return (317 of 3,136 ceiling events lose `ar_cc1`); `tert_of()` uses `mean(a[nonev] <= a[s])` with `a` containing NA (stocks with an incomplete 60-day window), so the tercile (and therefore `ar_cc1_ctrl`, and tercile subsetting) is NA on every date except 164-232; `cl()` then drops non-finite rows silently, and the manuscript tables do not print n.

## Phase D: Originality
D1: 9 distinctive passages (intro, novelty, discussion, implications, investor paragraph, benchmark paragraph, title) searched with quotes; no verbatim or close match anywhere. Direct comparison with the verbatim GitHub README: no shared 8-word sequence; the only 6-word overlaps are generic ("closes at its ceiling", "Ho Chi Minh Stock Exchange"). Grades: 9 ORIGINAL (100%). Overlap with the README is therefore of ideas and numbers, not text. It is acknowledged for the numbers (1.69%, -0.39%, 2016-2026, not peer reviewed, Section 1), but not for: the unfilled-order mechanism ("the stock closes at the limit with orders unfilled on one side, and that imbalance carries into the next session"), the statement that the close-to-close continuation is not tradeable at the close, and the ceiling versus +3% to +6.5% one-session comparison (README section 4.4, "the sign flips at the band"). See M7.
D2: authors are placeholders; the web search for author history could not run. Sibling manuscripts of the same project (`manuscript.Rmd`, `manuscript_B.Rmd`): 2% of tokens in >=12-word matches, all AI-use boilerplate and shared references. No self-plagiarism.
Tool limitation: WebSearch heuristic, not Turnitin/iThenticate.

| Grade | Paragraphs | Share |
|---|---|---|
| ORIGINAL | 9 | 100% |
| COMMON_KNOWLEDGE / PARAPHRASE / CLOSE_MATCH / VERBATIM | 0 | 0% |

## Phase E: Claim verification (HIGH-IMPACT = 100%, plus RANDOM sentinel)

| # | Claim (location) | Tier | Verdict | Evidence |
|---|---|---|---|---|
| 1 | Ceiling next-day AR 1.66%, t=4.9, 3,187 events; floor -0.71%, t=-5.3 (abstract, Table 3) | HIGH | SUPPORTED | exact recomputation |
| 2 | 0/22 characteristics survive; largest |t|=1.55 (abstract, 4.1) | HIGH | SUPPORTED | independently reproduced slopes and t for 6 characteristics; C3 BH p; none has p_bh<0.05 |
| 3 | 4/4 limit tests survive BH, same sign in both halves, confirmation |t|>1.96 (4.2) | HIGH | SUPPORTED | halves reproduced; floor t+1..t+5 second half -2.16 is marginal; note event "halves" split at the median event date, not at the 39/40-week split used for characteristics (M5) |
| 4 | Ceiling effect "entirely an overnight gap" 2.23% (t 9.8), intraday -0.53% (t -3.5) (abstract, 4.3) | HIGH | SUPPORTED | reproduced |
| 5 | Gap 2.67 pp larger than 5-6.5% movers (t 13.7); floors 1.58 lower (t -9.5) (abstract, 4.4, Table 5) | HIGH | SUPPORTED | reproduced 2.67/13.71 |
| 6 | Gap vs same-date same-liquidity controls 2.70% (t 20.2), intraday -0.50%; persist for exact hits and first day of streak (abstract, Table 7) | HIGH | SUPPORTED | reproduced exactly; first-day-of-streak rule-based intraday vs market is only -0.38 (t -1.9), but vs controls -0.31 (t -3.7) |
| 7 | Buying at next open and holding to 5th close loses 0.79% vs market (t -3.7) (abstract) | HIGH | MINOR_DISTORTION | the number is right (date-clustered); the two-way t is -2.7 (-0.75, Table 7) and vs controls the shortfall is -0.53 (t -1.8, not significant). The abstract states an unqualified loss; body text (4.7) correctly calls it benchmark-sensitive |
| 8 | 347 stocks, 200,468 stock-days (abstract, Table 1, Section 2) | HIGH | MINOR_DISTORTION | 200,468 is the all-405-file count; the 347-stock sample has 178,773 (S3) |
| 9 | Exact tick rule: gap 2.76% (t 13.5), intraday -0.73%; pre-specified rule "understates the exact-limit effect" (4.3) | HIGH | SUPPORTED | reproduced |
| 10 | Table 1: pile-up consistent with a 7% limit (2.21% in 6.5-7.1% vs 0.37% and 0.011%) | HIGH | SUPPORTED (qualitatively) | holds for 347 stocks too (1.98% vs 0.29% vs 0.01%); percentages need re-basing (S3) |
| 11 | Robustness "in each liquidity tercile"; control leaves cc effect "essentially unchanged (2.20% ceilings, -0.99% floors)"; floor insignificant in least liquid tercile (t 0.6) (4.5) | HIGH | MINOR_DISTORTION (numbers non-reproducible; verdict is SERIOUS under C-phase) | truncated samples (S1). Correct control-based values from Table 7/C11: ceiling cc vs controls 2.16 (vs 1.66 vs market, i.e. 30% larger), floor -1.65 (vs -0.69, i.e. 2.4 times larger): not "unchanged" for floors. Qualitative tercile conclusion (low-liquidity floor effect insignificant) survives (cc t about 0.4) |
| 12 | 58% of ceiling events have negative intraday AR; sells at open capture 0.55 pp (4.6) | HIGH | SUPPORTED | 58.4%, -0.55 |
| 13 | Dollar-volume benchmark concentrated: top-10 average 34% (4.7) | HIGH | SUPPORTED | C13 0.3365 |
| 14 | tungtran0911 reports 1.69%/-0.39%; "our estimate is close to theirs, which serves as an independent replication"; "a longer sample ... is partly supplied by the independent public analysis" (Section 1, Section 6 (i)) | HIGH | **MAJOR_DISTORTION** | The README's sample (2016-01-04 to 2026-09-25) contains the entire 21-month window of this study; same 405-stock currently-listed HOSE universe (404 of 405 downloaded); its price series is cross-checked against VCI, and the listing file used here is VCI-sourced (`data/hose_listing_VCI_20260924.csv`), so "different data feed" is at best partial; this study's 3,207 ceiling events are about 12% of the README's 26,705; different event definition (">= +6.5%", no close=high requirement) and different benchmark (equal-weighted universe mean, whereas the manuscript uses a dollar-volume-weighted market; the manuscript's own equal-weighted figure is 1.87%); different return convention (entry timing). It is corroboration on an overlapping sample, not independent replication |
| 15 | Four event tests survive Bonferroni for a programme of up to 816 tests (4.7) | HIGH | SUPPORTED | 0.05/6.12e-5 = 816 |
| 16 | Effective number of tests 6.8 (participation ratio) and 14 (Li-Ji); MDE 0.12-0.31 (4.7, Table 8) | HIGH | SUPPORTED | formulas in `47_da_response.R` correct; MDE reproduced (0.236 for MOM3M) |
| 17 | "Pre-specified" family fixed in a time-stamped log before computation (3.1) | HIGH (methods-critical) | SUPPORTED with caveat | git commit of A3 at 07:23:38, before the earliest C4-C9 outputs (07:25-07:27); analysis scripts and C1-C3 were first committed/regenerated later (07:33-07:36), so the pre-registration covers text, not code, and cannot be verified beyond local git metadata. The log's A5 items 27-28 and rule 22 were later overridden without disclosure (M4) |
| 18 | Discontinuity: "inside the band monotone and negative; at the limit the relation breaks" (4.4) | HIGH | SUPPORTED | C5 bins; non-limit beyond-6.5% bin has gap 0.05 (n=212), so the break coincides with the close=high condition (disclosed as association) |
| 19 | Costs: bank Corwin-Schultz about 59 bp (4.6) | HIGH | SUPPORTED, weak relevance | 58.8; banks are large caps, not typical limit-hit stocks |
| 20 | 7% limit "understood ... (public exchange guides)" (2) | RANDOM | SUPPORTED | consistent with HOSE rules and the pile-up |
| 21 | Veeraraghavan 2000-2006 study (1) | RANDOM | SUPPORTED | SSRN abstract |
| 22 | "advocates argue limits ... counter overreaction" attributed to Kim & Rhee (1) | RANDOM | MINOR_DISTORTION (negligible) | abstract states advocates claim lower volatility and no trading interference; "overreaction" is Brennan-era rationale |

Registry coverage: E1.1 mechanical coverage tool not run (no registry artifact exists); semantic extraction coverage = not_machine_detectable. Evidence-row artifacts are not produced (no dispatch evidence folder named).

### Advisory rows (not issues, never gate)
- ADV-E4-1 (scope): Section 5 "Implications" for regulators ("the limit does not settle the price on the limit day") and "for investors" generalise beyond one exchange, 21 months, a single bull regime and non-causal evidence (the manuscript itself disclaims causality in 4.4). Options: proceed open / accept with justification.
- ADV-E5-1 (novelty): "To our knowledge, among the sources our search reached (Appendix C), no peer-reviewed study documents ..." is search-bounded in wording, but the manuscript states no database list, date range, or `last_searched_at`; Appendix C points to a log not in the manuscript. Classification: UNRESOLVED. Prior work on HOSE price limits exists that is not cited or discussed (Le Dinh Nghi 2012, Journal of Economic Development, on fluctuation-limit reduction in Vietnam, found in my search); the README already contains the ceiling vs 3-6.5% contrast, so novelty (ii) is partly pre-empted.

## Issue List (sorted by severity)

### SERIOUS (must fix)
| ID | # | Category | Location | Issue | Correct / required action |
|---|---|---|---|---|---|
| IL-SERIOUS-1 | 1 | Data / implementation bug (Mode 1) | Table 6 (tercile rows, last column), Section 4.5 text on terciles and controls; `R/41_limits_robust.R` `mk_cc1`, `tert_of`, `ctrl_cc1` | NA propagation silently restricts these cells to 451 of 3,136 ceiling events (all between day 164 and 232) and 69 of 2,088 floor events (29/23/17). "All" and "first half" rows show identical control numbers (2.20 (11.6); -0.99 (-2.4)) and second-half cells are blank. Tercile gaps 3.38/3.30/1.88 and floor tercile numbers do not describe the full sample | Make market/tercile/control calculations NA-safe (`na.rm`, per-stock availability), regenerate C4, print n in each cell. Full-sample ceiling terciles: gap 2.78 (15.5), 2.91 (19.2), 1.45 (6.5); floor terciles gap -0.28 (-1.1), -1.92 (-6.3), -0.76 (-4.7); floor lowest tercile cc vs market 0.10 (0.4). Replace the Table 6 control column by the Table 7 / C11 values (ceiling cc vs controls 2.16, floor -1.65) and rewrite the sentence "leaves the close-to-close effect essentially unchanged (2.20%, -0.99%)" (floors change by a factor of 2.4) |
| IL-SERIOUS-2 | 2 | Citation context / overclaim | Section 1 "Contributions" last sentences ("serves as an independent replication"; "from a different data feed"); Section 6 (i) ("independent public analysis") | See E-claim 14 | Replace by: "A public, non-peer-reviewed analysis on an overlapping universe and a longer period (2016-2026, KBS data cross-checked against VCI), using a looser event definition (>= +6.5%) and an equal-weighted benchmark, reports 1.69%; this is consistent with, but not independent of, our estimate (our window lies inside theirs). Like-for-like benchmark: our equal-weighted close-to-close is 1.87% (C11)." Delete "independent replication" in Sections 1 and 6 |

### MEDIUM (must fix)
| ID | # | Category | Location | Issue | Correction |
|---|---|---|---|---|---|
| IL-MEDIUM-1 | 3 | Internal consistency / population | Abstract ("347 stocks ... 200,468 stock-days"); Table 1 caption and Section 2 percentages; Section 5 (1.6% ceilings, 0.8% exact); `R/44_desc.R` (no 95% filter) | 200,468 stock-days is the all-405-stock total; the analysed 347 stocks have 178,773 (C13). `nstockdays <- sum(PILE$n)` feeds Section 5 shares, so they are also mis-based | Rebuild Table 1 for the 347 stocks (1.98% in 6.5-7.1%, 0.29% in 6.0-6.5%, 0.010% in 7.1-8.0%; counts 38/2/1,136/1,193/459/171,809/514/1,925/1,622/17/58 on calendar-adjacent returns, N=178,773), update abstract, Table 1 caption, Section 2 and Section 5 (about 1.8% ceilings by rule, 0.9% exact). Alternatively state that Table 1 covers all 405 files |
| IL-MEDIUM-2 | 4 | Internal consistency | Table 3 caption; Tables 5, 6, 7 | The stated reason for differing event counts is wrong: Table 4 has MORE events (3,220) than Table 3 (3,187) because Table 3 requires returns t+1..t+5; Table 5/6 close-to-close n=2,819 (not 3,136) arises from IL-SERIOUS-1's NA bug; Table 7 "Events" column shows the controls sample (3,100) while "vs market" columns use 3,199; benchmark weights also differ (same-day in Table 3, lagged elsewhere) | Rewrite caption with the true sample rules; print n per column in Tables 5-7. Corrected Table 5 close-to-close rows: 2.31 (7.4) and 2.05 (6.0) |
| IL-MEDIUM-3 | 5 | Methods vs code/log | Section 3.1 | (a) Pre-registration says event outcomes "t+1, t+2..t+5"; implemented and reported as t+1 and t+1..t+5. (b) Pre-registered same-stock/date-matched control and a multivariate survivor model are not implemented or mentioned. (c) The event "first half/second half" used in the survival rule splits at the median event date (day 248 for ceilings), whereas characteristics split at weeks 39/40 (day about 315); not stated. (d) MOM3M is described as "60-day return skipping 5 days" but the code spans 59 days (60-day version: slope 0.123, t 1.45; still insignificant) | State each deviation in 3.1 or fix the code; define how event halves are formed |
| IL-MEDIUM-4 | 6 | Transparency | Section 4.7 first paragraph; Section 3.1/Appendix A | The DA report says explicitly it was retrospective (run after outcomes were known) and not a true Checkpoint 1; the manuscript calls it an "independent devil's-advocate review of the pre-specified design" without that caveat. The decisions log (A5 items 27-28) states that the tradable next-open outcome becomes the primary outcome and the same-date control becomes the primary benchmark, and rule 22 made advancement conditional on tradability; the manuscript still headlines close-to-close versus the dollar-volume market and does not mention the advancement-rule override | Add the retrospective caveat; either follow A5 (headline the next-open and control-based figures) or record in `decisions.md` that A5 27-28 were not adopted and why |

### MINOR (recommended now; must fix at Stage 4.5)
| ID | # | Category | Location | Issue | Suggestion |
|---|---|---|---|---|---|
| IL-MINOR-1 | 7 | Attribution | Sections 1, 4.6, 5 | README already gives the unfilled-order mechanism, the non-tradability statement and the ceiling vs 3-6.5% contrast; only the two numbers are credited | Credit these points explicitly; temper contribution (ii) |
| IL-MINOR-2 | 8 | Abstract claim strength | Abstract, penultimate sentence | "loses 0.79% (t=-3.7)" omits that two-way t is -2.7 and vs controls -0.53 (t -1.8) | Add "benchmark-sensitive" or report the control-based figure |
| IL-MINOR-3 | 9 | Data provenance | Section 2 | Source, vendor, retrieval date and adjustment status are not stated (files fetched with vnstock; listing from VCI on 2026-09-24); "the vendor" is never named | State source and date |
| IL-MINOR-4 | 10 | Descriptive | Section 2 | "Returns beyond 7.1% ... about 0.05%" counts only upside (96 stock-days); both tails 147 = 0.073% | Fix |
| IL-MINOR-5 | 11 | Method note | Table 3 | benchmark weights use dollar volume through t+1 (same-day), contrary to "trailing" | Use lagged weights (result 1.667) or state it |
| IL-MINOR-6 | 12 | Cost proxy | Section 4.6 | 59 bp is from 21 large banks; ceiling stocks are mostly smaller names | Qualify or compute from ceiling stocks |
| IL-MINOR-7 | 13 | Editorial | Rendered v3.md; Declarations; Appendix B/C | `<U+2013>` artefacts in captions; list numbering "1)" in Section 6; "C1-C10" vs C1-C15 and T10 actually used; "(`process`: C12)"; Figure 3 x-axis label clipped; Appendix C still says Harvey et al. and Newey-West need verification (now verified); Appendix B says "pre-registration" while Section 3.1 says internal log only | Fix |
| IL-MINOR-8 | 14 | Literature | Section 1 | Vietnam price-limit literature omitted (e.g., Le Dinh Nghi 2012) | Add or justify |

## AI Research Failure Mode Checklist

| Mode | Outcome | Evidence | Blocks? |
|---|---|---|---|
| 1 Implementation bug passing self-review | **SUSPECTED** | NA-propagation in `41_limits_robust.R` (IL-SERIOUS-1): Table 6 terciles and control column use 14% / 3% of events; Table 5/6 close-to-close lose 317 events; "identical" cells in Table 6 were not caught. Headline surfaces reproduced exactly and no look-ahead found (perturbation test passes) | Yes |
| 2 Hallucinated citation | RULED OUT (CLEAR) | 20/20 verified; contexts correct except the overclaim handled as a claim distortion (IL-SERIOUS-2) | No |
| 3 Hallucinated experimental result | CLEAR for headline numbers | every number in the abstract, Tables 2, 3, 4, 7, 8 recomputed from raw CSVs; only Table 6 tercile/control cells are non-reproducible and are explained by Mode 1 | No |
| 4 Shortcut reliance | CLEAR (flag-only) | exact tick hits, near-hits, first-day-of-streak, locked days, controls, 3-5% and 5-6.5% comparators all reported; remaining concern: discontinuity coincides with the close=high selection (non-limit beyond-6.5% bin has no gap), already acknowledged as association | No |
| 5 Bug reframed as insight | CLEAR | the gap-then-reversal pattern was predicted by the DA and appears in prior literature and the README, and was reproduced independently; not a first-run surprise | No |
| 6 Methodology fabrication | **SUSPECTED (low)** | Methods text differs from code/log in horizon wording, unimplemented pre-registered control, undefined event halves, MOM3M 59 vs 60 days (IL-MEDIUM-3); "Seeds are fixed" is trivially true (no stochastic step in 40-45). Data source not named | Yes (per protocol), cheap to fix |
| 7 Frame-lock | CLEAR | the log shows the frame was revised after the DA (tradability, controls, microstructure reading); manuscript frames result as non-tradable microstructure pattern | No |

## Tool Limitation Disclaimer
Phase D uses WebSearch heuristics and is not professional plagiarism detection software; coverage is limited to publicly searchable text; sampling 9 of about 25 body paragraphs (36%). Reference verification used WebSearch results from publisher/IDEAS/RePEc/NBER/SSRN/Semantic Scholar pages because doi.org/Crossref and arXiv are blocked; the Semantic Scholar API (A0) was not available. Pre-registration timing was assessed only from local git and file metadata.

## Verification Audit Trail (condensed)
- Refs: one query per reference of the form `author year "title" journal vol(issue) pages`; results listed in the Phase A table. Veeraraghavan: SSRN 1009042. Chen 1993 abstract: IDEAS/ScienceDirect. Berkman & Lee 2002 abstract via search results. Cho et al. via Semantic Scholar.
- GitHub: WebFetch of the repo page and `curl` of raw README (30,286 bytes). Quoted lines: "a stock that closes at its ceiling gains a further 1.69% the next session (t = 39), while one that rises 3% to 6.5% gives back 0.39% (t = -23)"; table row "At or near the ceiling (>= +6.5%) | 26,705 | +1.694% | +39.47"; "Next-session return of each stock relative to that session's universe mean"; data "887,291 bars for 404 of 405 stocks ... 2016-01-04 to 2026-09-25"; "Against a second provider (VCI) over 767,923 overlapping stock-days".
- Code: scripts in scratchpad `load.R`, `ev.R`, `pile.R`, `fm.R`, `t5.R`, `ctrl.R`, `cs.R`, `e1.R`; knit comparison of Rmd vs v3.md; `zoo_panel` vs `zoo_panel_LA` perturbation test.
- Originality: 9 quoted-sentence searches (no hits); n-gram overlap vs README (max 6 words) and vs sibling manuscripts (2%, boilerplate).

## Numbered correction list (exact locations)
1. Table 6, last column and tercile rows; Section 4.5 sentences on terciles/controls; `R/41_limits_robust.R` (IL-SERIOUS-1). Regenerate C4 NA-safe; print n.
2. Section 1 "Contributions" last sentence and Section 6 (i): remove "independent replication/independent public analysis"; describe overlap and definition/benchmark differences (IL-SERIOUS-2).
3. Abstract, Table 1 caption, Section 2 and Section 5 percentages: rebase on 347 stocks (178,773 stock-days) or relabel as 405-stock figures; fix `44_desc.R` (IL-MEDIUM-1).
4. Table 3 caption and Tables 5-7: correct the stated reasons for differing n, add n columns; update Table 5 close-to-close (2.31, 2.05) (IL-MEDIUM-2).
5. Section 3.1: disclose horizon wording, unimplemented pre-registered control, event half definition, MOM3M 59 days (IL-MEDIUM-3).
6. Section 4.7 intro and `decisions.md`: add DA retrospective caveat; reconcile A5 items 27-28 and rule 22 with manuscript headline choices (IL-MEDIUM-4).
7. Attribution of README mechanism/contrast (IL-MINOR-1); abstract wording on the tradable loss (IL-MINOR-2); data provenance in Section 2 (IL-MINOR-3); 0.05% tail statement (IL-MINOR-4); benchmark-weight wording (IL-MINOR-5); bank-cost relevance (IL-MINOR-6); editorial items (IL-MINOR-7); Vietnam price-limit literature (IL-MINOR-8).
8. Re-verification after fixes: re-run C1-C15, regenerate the Rmd, re-verify Tables 5-7, Table 1, abstract, and Section 5 counts (C2 whole-document consistency check required because the corrections change numbers).
