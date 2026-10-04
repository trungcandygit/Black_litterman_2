# Stage 2.5 integrity re-check, round 4 (narrow, beyond the three-round cap)

Role: integrity_verification_agent. Scope: only U1-U6 of integrity_stage2_5_round3.md, plus a v5-vs-v6 diff check. Manuscript: review/round1/manuscript_C_v6.md (source manuscript_C.Rmd, which carries the same edits). Files 04_/05_/06_ in paper2/process/ were not read. No project file was modified (R/46 was run from a scratch copy whose output path was redirected to /tmp, so process/05_verification_tests_C.txt was not overwritten).

## Verdict: PASS

All six items RESOLVED. No new stale or contradictory number. Two non-blocking notes (N1, N2).

## U1: deviation (e), lagged weights in Tables 4 to 8: RESOLVED
Text now reads "...and lagged weights are used in Tables 4 to 8." Code check of market-return weighting:
- Table 3 (R/40_zoo.R l.56, 63): mk_all[t+1] uses adv60(t+1), i.e. dollar volume through the outcome day t+1. Same-day weights, as stated.
- Table 4 (R/42_rd.R l.12-14): adv is the 60-day average through day t, applied to day t+1 outcomes. Lagged.
- Tables 5, 6, 7 (R/47_da_response.R l.14, 26): adv through day t applied to t+1 outcomes (wm, ctrl, beta). Lagged. The crash flag in Table 6 uses mk_t with adv[t-60], weights through t-1. Lagged.
- Table 8 (Fama-MacBeth lag sensitivity) uses no event market return. The statement is true (no table in 4 to 8 uses same-day weights) but Table 8 has no market-weighting to be lagged (N1).
Captions of Tables 5 and 6 say "lagged" and now agree with Section 3.1.

## U2: Table 7 caption: RESOLVED
Now "3,199 of these with a next-day price" (C12: 8 ceiling events lack a next-day price; 3,207 - 8 = 3,199; market return is defined for all days). Correct.

## U3: "event window" definition and denominator: RESOLVED
v6 adds (Section 3.1, after the deviations paragraph): "The event window runs from trading day 61 (so that 60 days of trailing dollar volume exist) to five trading days before the last day; stock-days outside it are not events." Section 5 uses the term as defined. C13: stock-days in the window with a return = 156,653 (days 61 to nd-5, matching R/47 tt <- 61:(nd-5)); 3,207/156,653 = 2.05% ("about 2.0%"), 1,654/156,653 = 1.06% ("about 1.1%"). Consistent. (The figure 156,653 itself is not printed in the manuscript, only in C13; not a defect.)

## U4: NA-safe streak flags: RESOLVED
R/47 l.22-23: shift1 sets NA to FALSE, streak() uses `%in% TRUE`, first window row forced FALSE. My own code (scratch indep.R, built from raw CSVs, loops over days, own event definitions; previous-day status NA = not an event; day 61 excluded from streak groups; market = trailing-60-day dollar-volume weights through t; controls = same-date non-event, same liquidity tercile; two-way clustered t) gives:

| Group | n market / ctrl (mine) | gap mkt | gap ctrl | intraday mkt | intraday ctrl | open-to-day-5 vs ctrl |
|---|---|---|---|---|---|---|
| Ceiling streak, rule-based | 2,480 / 2,403 | 1.833 (8.23) | 2.366 (15.57) | -0.380 (-1.88) | -0.314 (-3.82) | -0.429 (-1.63) |
| Ceiling streak, exact | 1,287 / 1,232 | 2.373 (12.21) | 2.854 (19.32) | -0.545 (-3.07) | -0.533 (-4.94) | -0.728 (-2.14) |
| Floor streak, exact | 831 / 801 | -1.043 (-4.70) | -1.723 (-4.17) | 0.216 (0.87) | 0.073 (0.32) | -0.619 (-0.95) |
| Floor streak, rule-based (not in Table 7) | 1,629 / 1,585 | -0.728 (-3.83) | -1.541 (-3.21) | 0.147 (0.59) | 0.017 (0.09) | -0.276 (-0.36) |

Table 7 v6 rows (2,480/2,403 1.83 2.37 -0.38 -0.31 -0.43; 1,287/1,232 2.37 2.85 -0.55 -0.53 -0.73; 831/801 -1.04 -1.72 0.22 0.07 -0.62) and their t-statistics (8.2, 15.6, -1.9, -3.8, -1.6; 12.2, 19.3, -3.1, -4.9, -2.1; -4.7, -4.2, 0.9, 0.3, -0.9) match my numbers, and match C11 to full precision. The non-streak rows also reproduce (rule-based ceiling 3,199/3,100, 2.244, 2.697, -0.535, -0.496, -0.527; exact ceiling 1,648/1,583, 2.771, 3.188, -0.735, -0.741, -0.884). The v5 values were the NA-dropping ones (n 2,483/1,281/830, up to 0.02 pp off), as round 3 found. Caveat: my control construction follows the specified definition, so it independently re-implements, not independently designs, the tercile rule.

## U5: R/46_verify_C.R and SUPERSEDED_ scripts: RESOLVED
- R/46_verify_C.R now reads tables/SUPERSEDED_C10_event_counts.csv. I ran it (scratch copy, output redirected): T1 to T6 all complete and print PASS (T3 reproduces 1.66022% on 3,187 events; T5 prints ceilings 3,136 / floors 2,088 from the superseded file, labelled as a post hoc sample, PASS).
- Appendix B lists `R/46_verify_C.R` (verification tests) and says 47 contains the NA-safe Tables 1, 5, 6 and 7.
- R/41, R/43, R/44 now write SUPERSEDED_C4_limits_robustness.csv, SUPERSEDED_C8_discontinuity.csv, SUPERSEDED_C9_pileup.csv and SUPERSEDED_C10_event_counts.csv (grep of write.csv); the unprefixed names no longer exist in output/tables.

## U6: conclusion wording: RESOLVED
v6: "entirely through an overnight gap of 2.2%, which is 2.7 percentage points larger than for stocks that rose 5-6.5% without hitting the limit". Gap 2.23 (vs market) and difference 2.66 (Table 5) match the tables.

## v5 vs v6 diff
Changed lines: Section 3.1 deviation (e) text + new event-window sentence; Table 7 caption (both copies); six Table 7 cells in the streak rows; the "Overlapping events" sentence in 4.7 (2.38 -> 2.37 for the exact-streak gap; t = 12.2 and -0.55 unchanged); conclusion; Appendix B. A multiset comparison of every number in the file confirms the only numeric changes are 2,483->2,480, 2,406->2,403, 1,281->1,287, 1,233->1,232, 830->831, 2.38->2.37, 2.86->2.85, -0.41->-0.43, -0.71->-0.73, 0.21->0.22, 15.5->15.6, t-values 3.7->3.8 and 0.8->0.9, plus the new 2.2% in the conclusion. All are explained by the A8 streak fix. The abstract is unchanged v5 to v6: its statements about the first day of a streak are non-numeric and remain true. No stale occurrence of an old streak value remains (grep of 2.38 in the exact-streak context, 2,483, 1,281, 2,406, 1,233, 830, 2.86). The Rmd carries the same edits (grep).

## Notes (non-blocking)
- N1: Section 3.1 (e) "Tables 4 to 8" includes Table 8, which has no event market return; harmless, "Tables 4 to 7" would be tighter.
- N2: The 156,653 denominator appears only in C13, not in the manuscript text.

No new issue found. Failure modes: none triggered; no MAJOR_DISTORTION; the A8 protocol note (cap exceeded without an explicit user decision) is disclosed in decisions.md and should be reviewed by the user.
