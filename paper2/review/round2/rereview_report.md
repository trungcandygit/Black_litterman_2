# Stage 3' Re-review (verification mode) - Paper C, v7 vs round-1 roadmap

Reviewer: independent re-reviewer, fresh context. Inputs: `review/round1/synthesis.md`, `manuscript_C_v6.Rmd`, `review/round2/manuscript_C_v7.md` (+ `manuscript/manuscript_C.Rmd`), `response_to_reviewers.md`, `R/48_revision.R`, tables C18-C25. No manuscript or code file was edited. Reference DOI re-resolution was attempted (Crossref) and blocked by the proxy (403), so the three new references remain unverified by this reviewer.

## Recommendation: MINOR REVISION (-> Stage 4.5)

All blocking and must-fix items are either resolved or openly disclosed as limited by the environment. No new number is wrong in a way that changes a conclusion; every spot-checked figure reproduces. The remaining items need small text edits or human-only actions (external time stamp, exchange-circular sourcing, declarations, archive deposit).

## 1. Roadmap verdicts

| Item | Verdict | Evidence from v7 / checks |
|---|---|---|
| R1 confirmatory label | PARTIAL | Resolved in substance: abstract "fixed in a version-controlled project log before the results were computed (it is not an external registry entry)"; "hold-out" now "(not a strict hold-out)"; Vietnamese abstract says the same; Sec. 1 splits confirmatory vs exploratory ("The close-to-close ceiling effect is the confirmatory part and is also the part that is already public"); t+2..t+5 reported (Table 3b). Commit times and SHA-256 re-verified with git (63bdc6d 07:23:38Z, 9b8644b 07:36:19Z, hash 3d6dc7e1...effaf matches). Not done: independent external time stamp / archive deposit (stated honestly). Residual: "pre-specified" still in headings 3.1/4.2, Table 2/3/4 captions, Appendix A, Limitations (v),(vi) - defined in 3.1 as non-registered, but the response letter's "no longer say pre-specified" is not literally true (N3). |
| R2 dependence-robust inference | RESOLVED | Table 3b and Sec. 4.2: week (95) and 10-day-block (46) clusters, t reference; ceiling 5-day t 4.00 -> 3.67/3.81; floor conf-half -2.16 -> -2.22/-2.46; survival rule re-run on all 26 (C20): 4/4 survive, p_bh up to 2.6e-03. My recompute reproduces 3.673 (G=95, n=3,187). Caveat: no Driscoll-Kraay/calendar-time portfolio (stated in Limitation vii; the roadmap allowed alternatives). |
| R3 mechanism vs news | RESOLVED (fallback route) | "Rival readings" paragraph lists three; "discontinuity" replaced by "break at the limit" (only the RD citation/"regression-discontinuity design" disclaimer remain); "delayed price discovery" "as a hypothesis"; Table 5b close=high comparison; attention proxies (C24). Announcement split / placebo not possible (no data) - DECLINED_OK with rewording. Residual wording: keywords and Sec. 5 "The evidence fits delayed price discovery" are still stronger than the hypothesis status (N5). |
| R4 implications | PARTIAL | Sec. 5 "Implications, conditional on this market and window": "They do not show what the limit does to price settlement ... a regulator should read them as a description of the post-limit opening"; "not trading advice". Missing: naming the data that would test the hypotheses (order-level, investor-type, auction-rule variation) in Sec. 5 (only Limitation ii mentions order-book/investor-type data). Sec. 5 still says "single-regime sample" (N2). |
| R5 HOSE rules sourced | PARTIAL | HSC (2025) and Viet Nam News (2025) cited and openly described as "brokerage and press descriptions ... not the exchange circulars, which we did not consult". Roadmap required exchange documents; not met. Special-band audit replaced by outlier exclusion (C25), which is a different check (stated). |
| R6 KRX migration | RESOLVED (sourcing PARTIAL) | Sec. 2 and 4.8/Table 9 split at 5 May 2025; "single regime" removed from Limitation (x). Date sourced to a news article, not a circular. Split logic verified (below). |
| R7 literature | PARTIAL | Subrahmanyam (1994), Bildik & Gulay (2006), Qi (2023) added and cited; novelty paragraph rewritten and bounded. Chinese A-share and Vietnamese-journal coverage still thin (disclosed in Appendix C); DOIs not resolvable by the authors' environment either (disclosed) and not by me. |
| R8 increment over Berkman et al. | RESOLVED | Sec. 1: "the gap-then-giveback pattern alone does not point to the limit. What a price limit adds is a testable contrast" (5-6.5% risers closing at the high); abstract contributions restated. |
| R9 zoo vs limit | RESOLVED (declined shortening accepted) | Sec. 1/5: "multiplicity device and a null benchmark, not a separate finding"; link stated. Roadmap offered "motivate and shorten OR separate"; motivating satisfies it. |
| R10 reproducibility/disclosure | PARTIAL | AI-use disclosure expanded (agent roles, shared model family, no cross-model verifier, references not human-checked); data/code availability states vnstock version/retrieval dates not recorded. Not done: archive with DOI/hash, ethics/funding/COI/contribution (placeholders), "completed-verification" statement (instead an honest "not checked by a human"). Needs human action. |
| S1 floor drift | RESOLVED | Sec. 4.6: -1.23 pp vs 5-6.5% fallers at their low (t -2.8; C23 -1.225/-2.77 OK); "a post-open drift that a gap-only mechanism does not explain"; Sec. 4.8 pre-change only (C22 -1.73 vs -0.15). |
| S2 power qualifier | RESOLVED | Abstract "roughly 0.1-0.3 percentage points per week"; Sec. 5 "0.12 to 0.31" (Table 8). Conclusion carries only "(with limited power)" - acceptable. |
| S3 reference status | PARTIAL | Veeraraghavan labelled working paper (Sec. 1 and list); GitHub source still a repo URL with no archive/DOI; Le/Chen/Berkman-Lee not re-read (disclosed); DOI checks incomplete (disclosed). |
| S4 executability | RESOLVED | Sec. 4.6 "quoted open ... describe prices, not achievable fills"; locked-at-open count 522 (matches Table 6/7). |
| S5 table for -0.75% / counts | RESOLVED | Table 6b; counts 1,666/1,654/1,648/1,583 reconciled in Sec. 4.7 (C7/C11 consistent). |
| S6 floor benchmark | RESOLVED | Abstract flags "-0.71% ... depends on the benchmark and is -1.65% against same-date controls"; Limitation (xiii). Roadmap offered the flag-in-abstract alternative. |
| S7 reference distribution | RESOLVED | t reference stated; 816 -> 683 (t/date) and 125 (t/week); C21 and arithmetic reproduce (0.05/7.31e-5 = 683.9; 0.05/3.98e-4 = 125.6). |
| S8 outliers/snapshot | PARTIAL (snapshot DECLINED_OK) | Outlier exclusion done (C25): ceiling gap 2.24 -> 2.26, floor -0.97 -> -0.98; reproduced. Post-sample listing snapshot not bounded (stated as limitation). |
| S9 presentation | PARTIAL | Duplicate captions removed. Abstract is still ~420 words with >15 statistics; "shortened so one message leads" only partly met. |

## 2. New issues introduced or left by the revision

| # | Severity | Issue |
|---|---|---|
| N1 | Minor (borderline Major for the abstract) | Abstract/Conclusion say the five-day survival "is carried by day t+1" / "the five-day tests are carried by the first day". True for ceilings (t+2..t+5 = -0.24%, t -1.5), but not for floors: t+2..t+5 is -1.10% (date t -2.91, week -3.01, block -2.81), i.e. about 60% of the floor five-day effect, and it fails only the confirmation half (week t -1.14; date -1.05). Sec. 4.2 states this correctly ("some further drift"); abstract and conclusion generalise. Also Sec. 4.2 mixes a date-clustered full-sample t (-2.91) with a week-clustered half-sample t (-1.14) in one sentence. |
| N2 | Minor | Stale text: Limitations (i) and (x) say "about 21 months", but 21 Aug 2024 - 23 Sep 2026 is ~25 months (Sec. 2 itself says "month 9 of 25"); Sec. 5 still says "single-regime sample" although Limitation (x) now says it is not a stable regime. |
| N3 | Minor | "Pre-specified" retained in headings, captions, Appendix A and Limitations; defined as non-registered in 3.1 but the response letter's wording ("from 'pre-specified' to 'fixed in a log'") overstates. Code comment in `48_revision.R` still says "as written in the pre-registration"; saved C15 labels "4 pre-registered". Response letter says the abstract states "that the confirmatory result is the part already public"; the abstract does not use confirmatory/exploratory wording (Section 1 does). |
| N4 | Minor | Table 3 vs Table 3b: same events and date clustering give slightly different t (4.91/4.01/-5.33/-5.12/14.36/-11.57 vs 4.90/4.00/-5.32/-5.10/14.33/-11.52); C3 and C18 use different small-sample factors. Text then says t "falls from 4.00", while Table 3 shows 4.01. Add a footnote or use one convention. |
| N5 | Minor | Mechanism wording still stronger than the stated hypothesis status in places: keywords "delayed price discovery"; Sec. 5 "The evidence fits delayed price discovery"; conclusion "consistent with delayed price discovery at the limit". Floor volume terciles in C24 go the other way (gap -1.20, -0.97, -0.68 with rising volume) and are not reported; text reports only ceiling terciles ("rises with ... volume"). The tercile sentence is garbled ("t = 4.8 and 4.8, 4.2"; values are vol-tercile-1 t 4.83, prior-return-tercile-1 t 4.22). |
| N6 | Minor | Outlier bound drops events but leaves the outlier stock-days in the dollar-volume market benchmark; and excludes only |r|>8% (smaller unadjusted corporate-action moves are not caught). Disclosed in spirit (Sec. 2/Limitation iv), not in 4.7. |
| N7 | Minor | New references (Subrahmanyam, Bildik & Gulay, Qi) and press/brokerage pages are not DOI-verified (acknowledged in Appendix C); Appendix C's "All references were verified" overstates for Le (2012), Chen (1993), Berkman and Lee (2002) which are only abstract-checked. Citation/reference cross-check otherwise clean: every in-text citation has a list entry and vice versa (Li-Ji method is cited by name only, without a reference). |
| N8 | Minor | Response letter R5 and R6 are honest about sourcing but file R5 as "partly done" while the roadmap item (exchange documents) is effectively not done; letter R9 "done by reframing" fine. No other overstatement found. |

No Major new issue (no wrong headline number, no unsupported claim of external verification, no contradiction between abstract numbers and tables).

## 3. Numeric spot-check log (v7 vs saved tables; R = fresh recompute from `data/raw/`)

| # | v7 value | Source | Result |
|---|---|---|---|
| 1 | Ceiling t+1 mean 1.66, date t 4.90 (3b) | C18 | OK (1.660; 4.902) |
| 2 | Ceiling t+1..t+5 week t 3.67, block 3.81 | C18 | OK (3.673; 3.811) |
| 3 | Floor t+1..t+5 conf-half t -2.16/-2.22/-2.46 | C18 | OK (-2.155/-2.222/-2.464) |
| 4 | Ceiling t+2..t+5 -0.24, t -1.53/-1.11 | C18 | OK |
| 5 | Floor t+2..t+5 -1.10, t -2.91/-3.01/-2.81; halves -8.7/-1.1 | C18 | OK |
| 6 | Spec split t 2.4/13.3, 2.0/3.8, -0.8/-1.1, -2.8/-4.5, -3.9/-2.6, -2.8/-1.6 | C19 | OK |
| 7 | Adjusted p up to 2.6e-03 (week/t ref) | C20 | OK (0.00259) |
| 8 | Bonferroni program 683 / 125 / 816; p 7.3e-05, 4.0e-04 | C21 | OK |
| 9 | KRX Table 9: gap 1.65 (t 3.2, n 936) / 2.49 (17.9, 2,263), diff 0.85 (1.6); floor -0.42/-1.37, diff t -3.2; floor f5o -1.73/-0.15, diff t 2.5 | C22 | OK, all 8 rows |
| 10 | Table 5b: gap 3.14 (t 14.5, n 679); floor -1.81 (-8.7, n 722); f5o -1.23 (-2.8) | C23 | OK |
| 11 | Tercile gaps ceiling vol 1.97/2.16/2.63; prior-ret 1.41/2.18/3.16; t 4.83, 4.22 | C24 | Values OK; sentence garbled (N5) |
| 12 | Outlier: 2.26 (t 9.7) vs 2.24; floor -0.98 vs -0.97; 96 stock-days | C25, Table 1 (38+58) | OK |
| 13 | Table 5: gap 2.66 (t 14.0), intraday -0.31, floor gap -1.59 | C17 | OK |
| 14 | Table 3 adj. p range 2.6e-06 to 4.0e-04; EW 1.75 / 1.87 | C3, C11 | OK |
| 15 | Bank spread ~59 bps, 21 banks | T10 | OK (58.8, n=21) |
| 16 | Table 3 vs 3b t at date level differ by 0.01-0.05 | C3 vs C18 | Inconsistency (N4) |

Fresh recomputation (own script on `data/raw`, 347 stocks, 519 days): ceiling gap 2.2435 (n 3,199) and floor -0.9722 (n 2,111) reproduce; KRX pre/post means 1.6455/2.4909 (n 936/2,263), floor -0.4223/-1.3738 (891/1,220), floor f5o -1.7285/-0.1482 reproduce; close=high comparison diff 3.1426 pp with n=679 reproduces; outlier-excluded ceiling gap 2.2565 (n 3,169) and 96 stock-days with |r|>8% reproduce; ceiling five-day abnormal return 1.4497, week-clustered t 3.6733, G=95, n=3,187 reproduce.

## 4. Logic review of `R/48_revision.R`

- Cluster definitions: `cl1` is a one-way CR1-type estimator (sum of cluster sums, G/(G-1)); `week` uses ISO-year-week of the event date (95 and 93 clusters), `blk10` uses `t %/% 10` (46). Correct. p-values use t(G-1). Overlap of 5-day windows across adjacent weeks is mitigated only by the 10-day block (stated).
- Survival rule: BH over 26 with the four event p-values replaced by week/t-reference values and median-split half-sample t; conf-half rule uses |t|>1.96 (normal) even with ~23-47 clusters per half; the smallest margin (floor 5-day, -2.22 week, -2.46 block) still clears the t critical value (~2.01-2.07). No error that changes the result.
- KRX split: `open_date = dts[tt+1]`, `post = open_date >= "2025-05-05"`; `dts` is a character vector, so the comparison is correct (no Date-to-numeric matrix bug); events on 2 May 2025 are assigned post because their gap is measured at the 5 May open - consistent with the text. Difference t treats periods as independent (stated).
- Comparison group: `nb_up_56 & hi` = return in [5%, 6.5%) and close >= high; `dcmp` regresses on a limit dummy with date-clustered HC1 SEs. Correct and consistent with Table 5 construction (n 679 reproduced).
- Outlier exclusion: window t-5..t+5 on any |return|>8% of the same stock; benchmark unchanged (N6).
- Terciles in C24 are cut within the event sample (not the market), which is appropriate for within-event heterogeneity.

## 5. Response-letter fidelity

The letter is generally candid (declines and partials are visible). Overstatements: "no longer say pre-specified/registered" (N3); "abstract states the confirmatory result is the part already public" (it does not use that framing); R2 "done" is fair but omits that clustering cannot remove cross-week overlap (listed in Limitation vii). Abstract claims were otherwise consistent with Tables 3-9 apart from N1.

## 6. Items for Stage 4.5 / human authors

Fix N1-N5 (text only); complete DOI checks; deposit the specification file and code with an external time stamp or DOI; source HOSE rules and the 5 May 2025 date to exchange circulars; complete ethics/funding/COI/contribution declarations; record vnstock version if retrievable.
