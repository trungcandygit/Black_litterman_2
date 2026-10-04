# Academic Integrity Verification Report: Stage 2.5, correction round 2 (re-verification, independent)

Manuscript: `paper2/review/round1/manuscript_C_v4.md` (source `manuscript/manuscript_C.Rmd`; docx checked for list/figure rendering). Verified 2026-10-04. Files 04_/05_/06_ in `process/` not read. Recomputation used my own code (`/tmp/claude-0/s2/r2_load.R`, `r2_tab.R`, `r2_fm.R`, plus the round-1 scratch `ev.R`, `pile.R`), NA-safe, from `data/raw/*.csv`.

## Verdict: FAIL (round 2 of at most 3)

Both round-1 serious items are resolved and every table cell I recomputed reproduces. FAIL rests on three MEDIUM items, all introduced or left by the corrections (one wrong number attribution in the Section 1 attribution paragraph, one stale mislabelled number in Section 4.7, Table 7 sample sizes still unlabelled), plus minor items.

| Category | Result |
|---|---|
| Round-1 items | 2 SERIOUS resolved; MEDIUM-1 resolved, -2 partial, -3 resolved, -4 partial; MINOR 8: 5 resolved, 3 partial/not |
| Phase C recomputation | Tables 1, 3, 4, 5, 6 (all 18 rows, terciles, controls), 7, 8, abstract numbers: reproduced exactly (2 d.p.) |
| New issues | 3 MEDIUM, 5 MINOR |
| Phase E new claims | 1 MINOR_DISTORTION-level misattribution (1.87%), 1 stale label (1.79/MOM3M); no MAJOR_DISTORTION |
| Failure modes | Mode 1 RULED OUT; Mode 6 mostly cleared, residual wording only (not blocking) |

## 1. Status of each round-1 correction

| ID | Status | Evidence |
|---|---|---|
| IL-SERIOUS-1 (NA bug, Tables 5/6) | RESOLVED | Tables rebuilt from `47_da_response.R` (C16, C17). My independent NA-safe code reproduces every Table 5 row (e.g. ceiling vs 5-6.5% gap 2.66 (14.0), cc 2.32 (7.6), n 3,199/1,751; vs 3-5% cc 2.05 (6.1); floors -1.59 (-9.7), -1.66 (-11.6)) and every Table 6 row incl. tercile and control cells: ceiling terciles gap 2.59/2.77/1.52, cc vs controls 2.49/2.28/1.82 (n 832/1,102/1,166); floor terciles -0.32/-1.44/-0.91, ctrl -0.56/-1.65/-1.77 (469/685/893); control column all 2.16 (18.0) and -1.65 (-3.4); halves, crash, locked rows identical. The "identical cells" and blank second-half cells are gone. Text "raises the close-to-close ceiling effect from 1.66% to 2.16% and the floor effect from -0.69% to -1.65%, so the benchmark matters for the size of the floor effect in particular" is correct. |
| IL-SERIOUS-2 (independent replication) | RESOLVED (one number error, see N1) | "Our result is therefore consistent with theirs but is not an independent replication: it uses the same exchange, an overlapping period and, at least partly, the same data vendor family." Section 6: "it is not independent of our sample and is not peer reviewed". Abstract: "A public, non-peer-reviewed analysis whose longer sample contains our window ...". Fair against the README (404 of 405 stocks, 2016-01-04 to 2026-09-25, KBS bars cross-checked with VCI; ">= +6.5%" at-or-near ceiling, universe-mean benchmark; "None of this is tradeable at the close"). "Same vendor family" is hedged and plausible (our listing file is VCI; our bars were fetched via vnstock with the underlying source unrecorded), acceptable. No "independent replication" claim remains. |
| IL-MEDIUM-1 (Table 1 population) | RESOLVED | Table 1 and N = 178,773 reproduce exactly (calendar-adjacent returns, 347 stocks): 38/2/1,136/1,193/459/171,809/514/1,925/1,622/17/58; 1.98% (6.5-7.1%), 1.30% (negative side), 0.288%, 0.010%, 0.064% (115/178,773). Abstract and Section 2 use 178,773. Residual: Section 5 shares, see N4. |
| IL-MEDIUM-2 (event counts, captions, n) | PARTIALLY RESOLVED | Table 3 caption now states the true rule (t+1..t+5 complete, hence 3,187 < 3,220), and Tables 5 and 6 carry n. Not fixed: Table 7 still has a single "Events" column that equals the control-sample n (3,100; exact 1,583; near 1,523; streak 2,406; locked 505; floor 2,047/984/1,066/801) while its "vs market" columns use larger samples (3,199; 1,648; 1,557; 2,483; 522; 2,111; ...); neither caption nor text says so. Table 6/5 sample (t up to day 514, 3,199) vs Table 4 (3,220) vs Section 4.7 "3,207 ceiling closes" is also not explained anywhere (see N3). Corrected Table 5 close-to-close rows: 2.32 (7.6) and 2.05 (6.1) match my recomputation (round-1 suggested 2.31/2.05 on a slightly different weighting; the lagged-weight values are right). |
| IL-MEDIUM-3 (methods vs code) | RESOLVED, one wording caveat | Deviations (a)-(e) are true to the code: (a) `40_zoo.R` builds `ar5` cumulative t+1..t+5; (b) spec text in `03_brainstorm_round2.md` lists a same-stock non-event control and a multivariate survivor model, neither coded; (c) `median(d$t)` event-date split; (d) code now uses `(n-64):(n-5)` = 60 days; I reproduce MOM3M 59d t=1.55 -> 60d 1.45 and IMOM 1.53 -> 1.45; (e) same-day weights in Table 3. Caveats: (d) says the 59-day window "was corrected before the final results", but git shows the 59-day results were in the draft that went to the first integrity review (v1-v3) and the fix came after it (commit bdb55cb); say so. (e) "from 1.660% to 1.664%" mixes weights and sample: on the same 3,187 sample lagged weights give 1.667; 1.664 is the 3,199-event sample (C12). |
| IL-MEDIUM-4 (DA retrospective; A5 27-28) | PARTIALLY RESOLVED | Section 4.7 now says "retrospective, because it was run after the pre-specified results were known". But decisions.md A6 item 35 states that the next-open and control-matched outcomes "are described as such [economically primary] in Sections 4.6-4.7"; the manuscript contains no such wording (no "primary"/"economically primary"/"headline"). A5 items 27-28 (next-open becomes primary outcome, control primary benchmark) are still not recorded as "not adopted, and why" except by the A6 sentence that the close-to-close stays the headline because it was pre-specified. Fix the A6 text or add the wording to 4.6-4.7. (The abstract and 4.6 do foreground the tradable results, so the reader is not misled.) |
| IL-MINOR-1 attribution | RESOLVED | Section 1 credits the README for the 1.69%, the 3-6.5% reversal, the "close is not a market-clearing price" mechanism and non-tradeability at the close; contribution (ii) is restated as the 5-6.5% comparison with date clustering. |
| IL-MINOR-2 abstract strength | RESOLVED | Abstract: "loses 0.75% relative to the market (t = -2.7) and 0.53% relative to ... controls (t = -1.8)"; both reproduce (-0.75 (-2.7) n 3,193; -0.53 (-1.8) n 3,099). |
| IL-MINOR-3 data provenance | RESOLVED | Section 2: vnstock, VCI listing dated 24 Sept 2026, adjustment status undocumented. |
| IL-MINOR-4 tail share | RESOLVED | "0.064% beyond +/-7.1%" (115 of 178,773). |
| IL-MINOR-5 weights | RESOLVED | Deviation (e). |
| IL-MINOR-6 cost proxy | PARTIALLY RESOLVED | Caveat added, but "the small stocks that dominate limit events" is not supported by Table 6: ceiling events by liquidity tercile are 832/1,102/1,166 (most in the most liquid tercile). |
| IL-MINOR-7 editorial | PARTIALLY RESOLVED | `<U+2013>` artefacts fixed (0 remaining), Figure 3 x-axis label now visible (checked docx image), Appendix C wording fixed. Still: Section 6 in the docx is an auto-numbered list whose first item shows as list number "1)" followed by inline "(ii)...(xi)" (Rmd starts with "(i)", which pandoc turns into a list marker); Appendix B still lists `R/41`, `R/43`, `R/44` as code although their outputs (C4, C8, C9, C10) are superseded and stale tables remain in `output/tables` (C9 still shows 200,468 stock-days from `44_desc.R`, which was not fixed); "regenerate every number from saved output" is therefore too strong. |
| IL-MINOR-8 Vietnam literature | RESOLVED | Le (2012) added in Section 1 and references; see section 3. |

## 2. Independent recomputation (Task 1)

| Surface | Manuscript | Mine | Status |
|---|---|---|---|
| Table 3 (4 rows, halves) | 1.66/4.91 (3,187; 446); 1.45/4.01; -0.71/-5.33 (2,105; 319); -1.76/-4.75; halves 2.28/14.36 etc. | 1.6602/4.908; 1.4497/4.008; -0.713/-5.326; -1.760/-4.751; halves identical | OK |
| Table 4 decomposition and exact rule | 2.23 (9.8)/-0.53 (-3.5)/1.66 (4.8), n 3,220; floor -0.99 (-4.7)/0.31 (1.4); exact 2.76 (13.5)/-0.73 (-5.3), n 1,666 | 2.235 (9.75)/-0.532 (-3.46)/1.658 (4.83); -0.994 (-4.70)/0.308 (1.41); 2.758 (13.51)/-0.734 (-5.29) | OK |
| Table 1 and 347-stock shares | as above | identical | OK |
| Table 2 / 8 (MOM3M, IMOM, DVOLCHG, TURNCHG, MOM6M) | 0.123/1.45 (disc 0.87, conf 1.17); IMOM 1.45 (0.89, 1.14); lag2/8 1.39/1.74, 1.39/1.72; DVOLCHG 1.42, lag8 1.79; MDE 0.24 | identical; max |t| over the family stays 1.45 | OK |
| Table 5 (16 rows) | see above | all identical incl. n | OK |
| Table 6 (18 rows x 5 columns) | see above | all identical incl. n | OK |
| Table 7 (rule, exact, near, streak, locked, floor rows; gaps, intraday, f5 vs controls) | e.g. 2.70 (20.2), -0.50 (-6.0), -0.53 (-1.8); exact 3.19 (21.5); locked 4.39 (12.2) | identical | OK (n labelling issue, N3) |
| Abstract headline numbers | 1.66 (4.9), 3,187; -0.71 (-5.3); 2.23 (9.8), -0.53 (-3.5); 2.66 (14.0); -1.59 (-9.7); 2.70 (20.2), -0.50; -0.75 (-2.7), -0.53 (-1.8); 1.45 | all reproduce | OK |
| Section 4.7 top-10 share 34%; 816 Bonferroni; 6.8 / 14 effective tests; BH p range 2.6e-06 to 4.0e-04 | | 0.3365; floor(0.05/6.12e-5)=816; C14/C15/C3 consistent | OK |
| Intro "1.87% with a looser definition and an equal-weighted benchmark" | 1.87% | 1.87% (10.9) is our rule-based (close = high) ceiling vs an equal-weighted benchmark. With the looser definition (return >= 6.5%, no close = high) and equal weights I get 1.75% (n 3,421). | NOT as described (N1) |
| Section 4.7 "largest |t| is 1.79 at 8 lags (MOM3M ...)" | 1.79 (MOM3M) | 1.79 is DVOLCHG; MOM3M at lag 8 is 1.74 (also in the manuscript's own Table 8) | Stale label (N2) |
| Section 5 "about 1.8% ... ceiling, about 0.9% exact" | 1.8% / 0.9% | numerator is the day-61..514 window (3,207; 1,654) over all-day denominator 178,773; on all days 3,386 (1.89%) and 1,754 (0.98%) | Mis-based, small (N4) |

## 3. New claims (Task 2)

- Section 1: Le (2012) exists: Le Dinh Nghi, "Evaluating Impacts of Reduction in Fluctuation Limit on Stock Price Risks in Vietnam", Journal of Economic Development 214 (Oct 2012), pp. 116-128, GARCH (ResearchGate/Academia records). Citation and in-text description correct; page range could be added to the reference. VERIFIED.
- GitHub README claims in Section 1: 1.69%, -0.39%, 404 stocks, 2016-2026, ">= 6.5%" definition, universe-mean benchmark, non-tradeability at the close: all match the fetched README text. "Not an independent replication" wording is fair. The sentence "the inference that outsiders cannot capture the gap" is a mild extension of "None of this is tradeable at the close" but acceptable.
- Section 3.1 deviations (a)-(e): true to code (details above); caveats on (d) timing and (e) sample mixing.
- Sections 4.4-4.7: every number is traceable to C11/C16/C17/C12/C13/C14/C15 or reproduced by me; exceptions N1, N2. "Sells at the open captures 0.54 pp" is the Table 6 intraday -0.54, correct; the old 58% and 0.79 statements are gone.
- Section 6 adds the winner's-curse and selection items; consistent with 4.7.

## 4. Whole-document consistency (Task 3)

Clean: no "independent replication", no "pre-registered" in the manuscript (only "pre-specified"), no 200,468, no 2.20/-0.99, no 3,136/2,819, no 0.79, no 58%; 1.55/1.53 appear only as the stated old values in deviation (d). Stale or contradictory items remain:
- N1 (MEDIUM) Section 1: "our estimate with a looser definition and an equal-weighted benchmark is 1.87%". 1.87% uses the stricter close = high rule; the like-for-like figure is 1.75% (not in any saved table). Correct the wording (and save the 1.75 in a table/script), e.g. "with our event rule and an equal-weighted benchmark 1.87% (1.75% with their looser >= 6.5% definition)".
- N2 (MEDIUM) Section 4.7 *Power and effective tests*: "the largest absolute t-statistic is 1.79 at 8 lags (MOM3M; below 1.96)" contradicts Table 8 (MOM3M 1.74; 1.79 is DVOLCHG). Residue of the pre-correction 59-day text (old 1.88 for MOM3M). Fix to "(DVOLCHG; MOM3M 1.74)".
- N3 (MEDIUM) Table 7: single Events column = control sample; "vs market" columns use different n (e.g. 3,199 vs 3,100). Add n for both, or a note. Also add one sentence reconciling the event counts 3,187 (T3), 3,220/2,122 (T4), 3,199/2,111 (T5-6), 3,207/2,115 (4.7 attrition): the last four-to-five days and day-t+1 availability rules.
- N4 (MINOR) Section 5 shares use window numerators over full-sample denominator; use 1.9% and 1.0% (all days), or both numerators and denominators on the tt window.
- N5 (MINOR) Section 4.6 "small stocks that dominate limit events" is not supported by Table 6 (events are, if anything, concentrated in the most liquid tercile); soften.
- N6 (MINOR) Deviation (d) "corrected before the final results" should state it was corrected after the first integrity review; deviation (e) 1.660 -> 1.664 should read 1.660 -> 1.667 on the same sample (1.664 includes the sample change).
- N7 (MINOR) decisions.md A6 item 35 claims wording that is not in the manuscript (IL-MEDIUM-4); A6 item 34 says "four deviations" (manuscript lists five).
- N8 (MINOR) Appendix B / Data availability: list superseded scripts and stale tables (C4, C8, C9, C10, `41`, `43`, `44`) or remove them; fix `44_desc.R` or label C9/C10 as obsolete; Section 6 list marker "1)" in the docx (use "First, ..." or non-list text).

## 5. Failure-mode checklist (Task 4)

| Mode | Outcome | Evidence |
|---|---|---|
| 1 Implementation bug passing self-review | RULED OUT (CLEAR) | NA-safe rebuild reproduced to the digit by independent code across Tables 1, 3-8; identical-cell artefact gone; earlier look-ahead perturbation test (X identical up to t=250) still valid since `40_zoo.R` characteristics code unchanged except the window fix. |
| 2 Hallucinated citation | CLEAR | 20 round-1 references verified; Le (2012) verified. |
| 3 Hallucinated result | CLEAR | all headline numbers recomputed; only N1/N2 are mislabelled descriptions of real numbers. |
| 4 Shortcut reliance | CLEAR (flag-only) | unchanged; exact/near/streak/locked/controls all reported. |
| 5 Bug as insight | CLEAR | unchanged. |
| 6 Methodology fabrication | RULED OUT as blocking; residual wording only | deviations (a)-(e) disclosed and true to code; remaining items are N6 timing wording and Appendix B script list. Not SUSPECTED. |
| 7 Frame-lock | CLEAR | unchanged; frame explicitly non-tradable microstructure. |

No SUSPECTED blocking mode, no MAJOR_DISTORTION, no non-reproducible headline number. The FAIL is driven by MEDIUM issues N1-N3 (and partial IL-MEDIUM-2/-4).

## 6. Numbered correction list

1. Section 1 "Contributions and novelty", sentence "our estimate with a looser definition and an equal-weighted benchmark is 1.87%": correct to the like-for-like figure (1.75% for return >= 6.5%, equal-weighted; 1.87% is our stricter rule), and save the 1.75 in a table produced by `47_da_response.R` (N1).
2. Section 4.7, "Power and effective tests": replace "(MOM3M; below 1.96)" with "(DVOLCHG; MOM3M 1.74; below 1.96)" (N2).
3. Table 7 (caption and Rmd): give n for the control-based and market-based columns (or state that Events is the control sample); add a sentence explaining 3,187/3,220/3,199/3,207 (N3, IL-MEDIUM-2).
4. Section 5 "Relation to the characteristic zoo": rebase 1.8%/0.9% (all days: 1.9%/1.0%) (N4).
5. Section 4.6: remove or support "the small stocks that dominate limit events" (N5).
6. Section 3.1 (d), (e): state that the window fix followed the first integrity review; give 1.667 for the same-sample lagged-weight estimate (N6).
7. decisions.md A6 items 34-35: correct the statements about what the manuscript says (five deviations; no "primary outcome" wording) or add that wording to Sections 4.6-4.7; record that A5 items 27-28 were not adopted as headline choices and why (N7, IL-MEDIUM-4).
8. Appendix B / Data availability: mark `41`, `43`, `44` and tables C4, C8, C9, C10 as superseded or fix `44_desc.R`; weaken "regenerate every number"; fix the Section 6 list marker (N8).
9. After corrections: re-verify items 1-3 and re-run the C2 whole-document consistency check (numbers changed only locally; no re-run of tables needed beyond the 1.75 figure).

## Audit trail
Code: `/tmp/claude-0/s2/r2_load.R`, `r2_tab.R` (Tables 1/5/6/7, EW and loose-definition checks), `r2_fm.R` (Fama-MacBeth, NW lags 2/4/8, 59 vs 60 day), round-1 `ev.R` and `pile.R` re-run (Tables 3, 4, 1). README read from the round-1 raw copy (30,286 bytes). Le (2012): two WebSearch queries, ResearchGate and Academia records. git history checked for correction timing (commits 63bdc6d, 9b8644b, fbbd5d5, bdb55cb). Docx media and numbering checked.
