# Integrity re-verification after the fourth set of comments (Stage 4.5, revision round 4)

Date: 2026-10-06. Verifier: independent integrity_verification_agent (Mode 2, scoped to the round-4 changes). Files checked: `manuscript/manuscript_final.Rmd` against `review/round3/manuscript_before_round4.Rmd`; rendered text (`pandoc manuscript_final.docx -t plain`, docx built 2 s after the Rmd); `R/52_reviewer_round4.R`; tables C28-C32 (plus C3, C5, C11, C12, C16, C18, C20, C22); `process/04_literature_search_log.md`, `process/08_literature_review_benchmark.md`, `process/decisions.md`. No manuscript or code file was edited.

## Verdict: FAIL (7 issues to correct, 4 advisory notes)

The new numbers are reproducible and correct, and the code logic is sound. The verdict is FAIL for these reasons: one interpretive sentence the tables do not support (the floor "gradual change"), one misstated bound (*t* ≥ 3.0 when the minimum is 2.998), an event-count mismatch in the new Table 5, and an Appendix B that describes the search more specifically than the process record documents and does not say that the AI tool ran the search.

## 1. Code review of `R/52_reviewer_round4.R` and re-run

- Re-run: I ran a scratch copy with `od` redirected to the scratchpad (inputs C3, C18 and C20 copied there) in 24 s. All five outputs, C28 to C32, are **byte-identical** to `paper2/output/tables/`.
- Event definitions (C28): the baseline definitions match `47_da_response.R` (`r_ceil` and `r_floor`; n = 3,199 and 2,111, the same as C11 and C16). `LK` (open = high = low) implies close = high = low, so the locked definition is coherent, and its n of 522 matches the earlier locked definition. The band definitions use [6.7%, 7.3%] and [−7.3%, −6.7%] as stated.
- Quarter assignment (C29): it uses `open_date = dts[tt+1]`, the opening that defines the gap, as the caption says. **Defect:** `ceiling_n` and `floor_n` are computed as `sum(rc & q == k)`. This count includes events without a finite gap, while the gap means use only the finite cases (`cl2`). The columns therefore sum to 3,207 / 2,115, not 3,199 / 2,111 (the 8 and 4 events with no day-*d*+1 open; C12). See Issue 3.
- Placebo breaks (C30): there are 16 break dates (the first trading day of each month from Jan 2025 to Apr 2026). 2025-05-05 is itself the first trading day of May 2025, so `unique()` keeps 16 dates and `pl` has 15 non-KRX dates, as the text says. Events are assigned to the post period when `open_date >= b`. The difference t is (post − pre)/sqrt(se_pre² + se_post²), with se recovered as |mean/t| from the two-way-clustered `cl2`. It reproduces the C22 KRX diff_t exactly (1.567, −3.172). It ignores covariance across periods from shared stocks (advisory A2).
- DiD (C31): `lm(y ~ D*P)` with date-clustered HC1 errors. `b["D"]` is the pre-period limit-minus-control excess and `b["D:P"]` is the change after the KRX date. The control groups (5% ≤ R < 6.5% at the high, or the mirror at the low) are disjoint from the event groups. The labels and interpretation in the CSV are correct.
- Family sensitivity (C32): `F3$p[23:26]` are the four event tests (checked against the `test` column). `pe[1:2]` are ceiling and `pe[3:4]` are floor, so the two-family split is correct. `p25` takes the two event-date `t+2..t+5` p-values from C18. `F20$p` holds the 22 characteristic p-values, which are identical to C3, plus the four week-clustered event p-values. I checked BH, Holm and Bonferroni by hand (e.g., Holm ceiling t+1 = 25 × 9.22e-7 = 2.31e-5; Bonferroni = 26 × 9.22e-7 = 2.40e-5). All are correct. One inconsistency in the 28-test family is noted in advisory A1.

## 2. Independent recomputation (base R written from the manuscript definitions; no repository code sourced)

| Quantity | Independent | Table |
|---|---|---|
| Universe, days | 347 stocks, 519 days, last 2026-09-23 | matches |
| Baseline ceiling gap (n) | 2.2435% (3,199) | C28 2.2435 (3,199) |
| Baseline floor gap (n) | −0.9722% (2,111) | C28 −0.9722 (2,111) |
| Ceiling ≥ 6.0% at high | 2.0743% (3,390) | C28 2.0743 (3,390) |
| Ceiling locked | 2.9116% (522) | C28 2.9116 (522) |
| Floor ≤ −6.5%, no close condition | −0.8218% (2,288) | C28 −0.8218 (2,288) |
| Ceiling gap 2025-Q3 | 2.9870% (624) | C29 2.9870 (624) |
| Floor gap 2025-Q2 | −0.3375% (802) | C29 −0.3375 (802) |
| Ceiling gap 2026-Q3 | 1.6100% (**239** finite) | C29 1.6100, ceiling_n **246** (Issue 3) |
| KRX split ceiling diff | 0.8454 (936 / 2,263) | C30 0.8454 |
| KRX split floor diff | −0.9515 | C30 −0.9515 |
| DiD pre excess ceiling gap | 2.9068 pp (679 controls) | C31 2.9068 (679) |
| DiD change ceiling gap | 0.3795 pp | C31 0.3795 |
| DiD pre excess floor gap | −1.6225 pp (722 controls) | C31 −1.6225 (722) |
| Max adjusted p in C32 (manual BH on C20 p) | 0.0025862 | C32 0.0025862 → "0.0026" |

Diagnostic for Issue 1: of the 802 floor events in 2025-Q2, 764 fall in April 2025, before the KRX change. Their mean gap is −0.22%, against −1.63% for the other 127 pre-change floor events and −1.37% after the change. This number is my own calculation and is not in a saved table, so it must not enter the manuscript. The suggested text below relies only on Table 5 and C30.

## 3. Claims against tables (new and changed text)

- Abstract, Introduction, Section 2 (three bounded "none/no study" statements), Conclusion: the wording is bounded and uses "consistent with". There is no causal overreach. The title is unchanged. OK, apart from the scope of "studies" (Issue 6).
- Section 4 "Samples": 3,187 / 2,105 (C18 and the Table 1 source), 3,199 / 2,111 (C16), 3,100 / 2,047 (C11 gap_ctrl) and 3,220 (C5 CEIL) all match. The vendor-adjustment clause omits the ex-date exception that Section 7 states (Issue 5).
- Multiplicity rationale: this is supported by decisions.md item 19 (the family is fixed in `03_brainstorm_round2.md`). "every signal we examined" is broader than the plan, because post hoc analyses were added (Issue 7).
- Section 5, Table 5 paragraph: 8 quarters; ceiling *t* from 2.5 to 16.8; floor negative in all quarters and significant in 7; placebo ceiling range −0.45 to 0.72 with |t| ≤ 1.4; KRX 0.85 (t = 1.6), the largest. All are correct. **The floor sentence is not supported (Issue 1).** The DiD numbers are correct. The closing clause is incomplete (Issue 2). Nothing in the paragraph claims that the placebos or the DiD identify the auction rules, and the preceding paragraph keeps "We cannot attribute the differences between the periods to the auction rules."
- Family sensitivity: six alternative definitions are listed, which matches C32. "Largest adjusted p 0.0026" is correct.
- Tick-free definitions: 2.07, 2.33, 2.35, 2.10, 2.91 and the floor range −0.79 to −2.50 are correct. **"all *t* ≥ 3.0" is false:** the locked-day *t* is 2.998, rounded up (Issue 4).
- Section 6 sentence and Table 6 call-out: OK.
- Numbering: the call-outs run Table 4 (Rmd line 190), Table 5 (199, quarterly), Table 6 (218, literature). Captions match. The later reference to Table 4 at line 229 is a valid back-reference. No figure numbering changed. No new citations were added, and the reference list is unchanged. The rendered text has no U+FFFD characters and no unevaluated inline R.
- Appendix B: the dates (4 and 5 Oct), the absence of Scopus/WoS, "about 100 records", the peer-reviewed-only rule and the exclusion of working papers and repositories all match the 04 and 08 logs. Several points do not (Issue 6). The logs do not record the specific query grid (market-name combinations, "limit hit", "band change", "attention, retail trading, sentiment, market makers"). The 04 log records MAX/lottery, low volatility, two-way clustering and regression-discontinuity queries, which the appendix omits. The search was run with the AI assistant's web search tool, which returns summaries it generates, and no page could be opened. The 04 log states that Vietnamese-language journals and further Chinese A-share studies were not searched. The search also identified a non-peer-reviewed code repository that reports a close-to-close effect after ceiling closes, so the last sentence must be limited to peer-reviewed studies.

## 4. Issues (old string is unique in the .Rmd; new string is suggested)

### Issue 1 (MAJOR: interpretation not supported by Tables 5 and C30)
The floor-gap difference is positive at all 4 placebo dates before May 2025 and negative at all 11 later dates. The KRX split itself is significant (t = −3.2). Table 5 shows no trend in the floor gap but a weak 2025-Q2. That pattern is not a "gradual change".

Old:
```
The floor-gap difference is negative at `r sum(pl$floor_gap_diff < 0)` of `r nrow(pl)` placebo dates, which points to a gradual change in the floor gap over the sample rather than a break at the platform change.
```
New:
```
The floor-gap difference is positive at the `r sum(pl$floor_gap_diff > 0 & pl$break_date < "2025-05-05")` placebo dates before the platform change and negative at all `r sum(pl$break_date > "2025-05-05")` later ones, and the split at 5 May 2025 gives `r f(C30$floor_gap_diff[C30$krx],2)` points (*t* = `r f(C30$floor_gap_diff_t[C30$krx],1)`), close to the differences at the placebo dates that follow it. Table 5 shows no trend in the floor gap; the pattern coincides with the weak floor gap in 2025-Q2 (`r f(C29$floor_gap_pct[C29$quarter == "2025-Q2"],2)`%), the quarter with the most floor events (`r fi(C29$floor_n[C29$quarter == "2025-Q2"])`), so the placebo dates cannot separate a break at the platform change from a shift specific to that quarter.
```
(If Issue 3 is fixed in the code, the 2025-Q2 floor count is unchanged at 802.)

### Issue 2 (MINOR: incomplete qualifier; "same answer" no longer accurate once Issue 1 is fixed)
Old:
```
gives the same answer (repository table C31)
```
New:
```
points the same way for the ceiling (repository table C31)
```
Old:
```
although the significance of the raw close-to-close return does.
```
New:
```
although the significance of the raw ceiling close-to-close return and of the raw floor gap does (Table 4). Like the split in Table 4, these comparisons describe timing and do not identify an effect of the auction rules.
```

### Issue 3 (MAJOR: Table 5 event counts are not the counts behind the gaps)
The C29 `ceiling_n` and `floor_n` columns count all events (3,207 / 2,115), but the gap means use the 3,199 / 2,111 events with a day-*d*+1 open, the counts the Samples paragraph gives for Tables 2-4. Example: 2026-Q3 shows 246 ceiling events, but its gap uses 239. Preferred fix (code): in `52_reviewer_round4.R`, set `ceiling_n = unname(a["n"])` and `floor_n = unname(b["n"])` and re-run. Alternatively, keep the code and amend the caption.

Old:
```
caption = "Table 5. Events and overnight gaps (percent, market-adjusted) by calendar quarter of the opening that defines the gap, with two-way-clustered *t*-statistics in parentheses. The KRX platform change falls in 2025-Q2.")
```
New:
```
caption = paste0("Table 5. Events and overnight gaps (percent, market-adjusted) by calendar quarter of the opening that defines the gap, with two-way-clustered *t*-statistics in parentheses. Event counts include all ", fi(sum(C29$ceiling_n)), " ceiling and ", fi(sum(C29$floor_n)), " floor events; the gaps use the ", fi(c16("Ceiling all","gap_mkt","n")), " and ", fi(c16("Floor all","gap_mkt","n")), " events with a day-*d*+1 open. The first and last quarters are partial. The KRX platform change falls in 2025-Q2."))
```
(If the code fix is applied instead, drop the "Event counts include ..." sentence but keep "The first and last quarters are partial.")

### Issue 4 (MAJOR: misstated bound)
The minimum ceiling-gap *t* across the C28 definitions is 2.998 (locked days), which `f(.,1)` prints as "3.0". "all *t* ≥ 3.0" is false, and it matters because the paper uses |t| = 3 as a hurdle.

Old:
```
(all *t* ≥ `r f(min(C28$t_twoway[grepl("Ceiling", C28$definition) & C28$measure == "gap_mkt"]),1)`)
```
New:
```
(all *t* above `r f(floor(10 * min(C28$t_twoway[grepl("Ceiling", C28$definition) & C28$measure == "gap_mkt"])) / 10, 1)`)
```

### Issue 5 (MINOR: inconsistent with Section 7)
Section 7 says adjustment leaves returns unchanged "except on ex-dates".

Old:
```
which proportional price adjustment by the vendor leaves unchanged;
```
New:
```
which proportional price adjustment by the vendor leaves unchanged except on ex-dates;
```

### Issue 6 (MAJOR: Appendix B must match the process record and disclose the AI search tool)
Old (the whole paragraph, unique):
```
We searched on 4 and 5 October 2026 with a general-purpose web search engine; no subscription database (Scopus or Web of Science) was available. The queries combined "price limit" or "daily price limit" with each of delayed price discovery, volatility spillover, trading interference, magnet effect, limit hit, and band change, with and without the market names Tokyo, Taiwan, Korea, Istanbul, China, ChiNext, Shanghai, Shenzhen, Vietnam, HOSE, and HNX; and "overnight returns" or "intraday returns" with attention, retail trading, sentiment, market makers, and China. Further queries covered circuit breakers, multiple testing and false discoveries in asset pricing, Fama–MacBeth standard errors, weekly return predictability, and anomalies in the Vietnamese stock market. We screened about 100 records by title and abstract and kept peer-reviewed journal articles in English whose bibliographic record we could confirm; working papers, theses, code repositories, and press items were not used as evidence, except for press and brokerage descriptions of HOSE rules (Section 3). We read records and abstracts, not full texts. Statements in this paper that no study reports a given result refer to the studies this search identified.
```
(Match the exact quote characters in the .Rmd; the rendered text shows typographic quotes.)
New:
```
We searched on 4 and 5 October 2026 with the web search tool of the AI assistant named in the Declarations; no subscription database (Scopus or Web of Science) was available, and publisher pages could not be opened. The search topics were price-limit performance (delayed price discovery, volatility spillover, trading interference, and magnet effect), price-limit band changes, price limits in Vietnam and on HOSE and HNX, overnight versus intraday returns, lottery-type (MAX) and low-volatility effects, circuit breakers, multiple testing and false discoveries in asset pricing, Fama–MacBeth and clustered standard errors, regression discontinuity, weekly return predictability, and anomalies in the Vietnamese stock market; exact query strings were not logged. We screened about 100 records by title and abstract and kept peer-reviewed journal articles in English whose bibliographic record we could confirm; working papers, theses, code repositories, and press items were not used as evidence, except for press and brokerage descriptions of HOSE rules (Section 3). Vietnamese-language journals were not searched, and the coverage of Chinese A-share studies is incomplete. We read the bibliographic records and the abstract text returned by the search tool, not full texts. Statements in this paper that no study reports a given result refer to the peer-reviewed studies this search identified.
```
Companion change in the Declarations (AI-use disclosure):

Old:
```
The authors used Claude (Anthropic) to write analysis code, draft text, and check numbers against output files.
```
New:
```
The authors used Claude (Anthropic) to run the literature searches (Appendix B), write analysis code, draft text, and check numbers against output files.
```

### Issue 7 (MINOR: scope of the multiplicity rationale)
Post hoc analyses (attention proxies, subsamples, the C28-C32 checks) were examined outside the family.

Old:
```
so the limit result pays for every signal we examined;
```
New:
```
so the limit result pays for every candidate signal in the plan;
```

## 5. Advisory notes (non-blocking; record only)

- A1. The 28-test family in C32 mixes p-value references. The two added d+2..d+5 p-values are event-date-clustered with a *t* reference (C18 `p_t_ref`), while the four event p-values come from C3, whose ceiling t+1 p of 9.2e-7 differs slightly from C18's 1.3e-6. The conclusion does not change (largest adjusted p in that family is 4.3e-4). A note in the code comment would help.
- A2. The placebo and C22 difference *t* treats the two periods as independent, although the same stocks appear in both. Positive covariance across periods would make the reported *t* conservative. The Table 4 caption already states the independence assumption; the same holds for C30.
- A3. Pre-existing and not introduced in this round: in C20 the `t_conf` and `t_disc` columns for the event rows appear swapped relative to C3 (C3 t_disc 2.28 / t_conf 14.36; C20 t_conf 13.67 / t_disc 2.16). Check whether any manuscript sentence reads C20 `t_conf`.
- A4. The response letter (item 4) says the placebos show "that the floor gap changes gradually". It should be updated in line with Issue 1.

## 6. Previous-round status
The round-3 corrections remain in place. The round-4 changes add no new references. Every new manuscript number traces to C5, C11, C16, C18, C22 or C28-C32 through inline R; none is hand-typed.
