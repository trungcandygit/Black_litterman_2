# Verification Review Report: Stage 3' re-review, round 3

Manuscript: `paper2/manuscript/manuscript_final.Rmd` (rendered `manuscript_final.docx`, same time stamp 02:38, so the rendered text read is current).
Comparison base: `paper2/review/round3/manuscript_before_round3.Rmd`.
Roadmap for this round: `review/round3/method_fidelity_audit.md` (items 1-37, lists B and C) and `review/round3/style_round1.md` (applied).
Earlier verification inputs: `review/round2/rereview_stage4b.md`, `review/integrity_stage4_5_final_v2.md`.
Code read line by line: `paper2/R/40_zoo.R`, `42_rd.R`, `47_da_response.R`, `48_revision.R`, `49_final_figures.R`, `50_sample_description.R`. Tables read: `paper2/output/tables/C1, C2, C3, C5, C9b, C11, C13, C14, C15, C16, C17, C18, C20, C21, C22, C23, C24, C25, C26`. Evidence file: `paper2/process/08_literature_review_benchmark.md`.
No manuscript, code or output file was edited. Three read-only diagnostics were run from the scratchpad (they source lines 1-21 of `47_da_response.R` and write nothing to the project). Their results are described in NEW-1 and are not proposed for the text unless they are first saved as an R output.

## Judge Record (#539)

- **Verification judge**: Claude Opus 5.5 (claude-opus-5-5), fresh context. This judge did not write the paper or the revision.
- **Round-1 panel provenance**: not supplied (no `review-panel-provenance/1.0` artifact in `paper2/review/`). Status: unavailable; all six axes `unknown`.
- **Blind cross-model pass**: not_configured. The run-level same-family disclosure applies (below).
- **Pre-committed criteria**: none as a hashed Phase-1 artifact. Criteria were fixed before reading the revised text: the acceptance test for each audit item is the audit's own "exact new string" or an equivalent statement that matches the code.
- **Prompt/rubric surfaces**: `academic-pipeline/SKILL.md` (Stage 3'), `academic-paper-reviewer/SKILL.md` (Re-Review Mode) and `references/re_review_mode_protocol.md` (Decision Derivation, New-Issue Attribution, output format).
- **Reviewer configuration**: `[YARDSTICK-REGENERATED: original manuscript — no Round-1 Reviewer Configuration Cards exist for round 3; the roadmap is the method-fidelity audit plus the style report]`.
- **Routing**: `[ROUTING-DEGRADED: no round-1 cards]`. The judge took one methodology-plus-domain seat, as the brief asked.
- **Apply-report chain**: not_run_no_reports.
- **Contract deviation (disclosed)**: there is no input manifest, author-adjudication sidecar or revision-evidence bundle for this round, so `scripts/check_re_review_synthesis.py` could not be run. Under the contract this is `manifest_incomplete`. The decision below is therefore advisory: it applies the Decision Derivation rules by hand. The orchestrator should record the deviation in `paper2/process/decisions.md`, as with earlier rounds, and must not present it as a checker-verified outcome.
- **Evidence seen by the judge**: revised manuscript (Rmd and rendered docx), original pre-round-3 manuscript, both roadmap documents, code, saved tables, evidence file, earlier re-review and integrity report. No response letter exists for this round.
- **Judging budget**: about 30 tool calls.

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

## Decision

**Minor Revision** (advisory; see the contract deviation above). B5 applies because the revision introduced minor regressions (NEW-3 to NEW-6) and one should_fix item is only partly addressed. No must_fix item is open.

The two Major-severity findings (NEW-1, NEW-2) are `previously_missed`: both were already in the manuscript before round 3. Under the goalpost guard they do not move the decision, but they travel with the paper to Stage 4' / 4.5 and should be fixed before submission. Both are text-level fixes. NEW-1 also needs one small saved diagnostic if the authors want to quote numbers.

## Revision Response Checklist (method-fidelity audit = roadmap of this round)

### must_fix: the MISMATCH items

| Ref | Original finding | Response status | Revision location | Verified? | Quality assessment |
|---|---|---|---|---|---|
| A4 | Weights through *d*+1 for all of Table 1 was wrong; weekly weights not stated | FULLY_ADDRESSED | §4 "Abnormal returns subtract…" | ✅ | Matches `40_zoo.R:56-57`, `48:7-8`, `47:26`, `40:25`. |
| A5/A30/C3 | Exact hits not restricted to events | FULLY_ADDRESSED | `47_da_response.R:21`; §4; C11, C13 regenerated 02:36 | ✅ | `ex_ceil & r_ceil`. Now 1,642 + 1,557 = 3,199 ceiling and 1,025 + 1,086 = 2,111 floor events (C11), which equals the "All" rows. C13 exact counts 1,648 / 1,027 ≤ rule-based 3,207 / 2,115. `48_revision.R` sources lines 1-44 of 47, so it inherits the restriction, but none of C18-C25 uses `ex_*`, so those older outputs are not stale. |
| A13/C2 | Date clustering "without G/(G−1)" misdescribed Table 1 | FULLY_ADDRESSED | §4 Inference | ✅ | Family p-values: `clus` (no factor, normal; `40:63,66`). Table 1: `cl1` with factor (`48:15`). Bonferroni: `cl1` with *t*(G−1) (`48:16,36-37`). |
| A14 | Table 1 caption | FULLY_ADDRESSED (grammar slip, NEW-6) | Table 1 caption | ✅ | — |
| A22/C1 | Survival rule compared with the full-sample sign | FULLY_ADDRESSED | §4 Multiplicity | ✅ | `sign(t_disc) == sign(t_conf)` (`40:73`, `48:34`). |

### should_fix: the IMPRECISE items

| Ref | Original finding | Response status | Notes |
|---|---|---|---|
| A2 | Event window not stated | FULLY_ADDRESSED | "from day 61 … to five days before its end" = `61:(nd-5)`. |
| A3 | Eq. (2) details | FULLY_ADDRESSED | Full 60-day history (`colMeans` without `na.rm`), rescaling over stocks with a return, dollar volume = close × volume. |
| A6 | τ clash, guards, tolerance | FULLY_ADDRESSED | δ for tick; 1e-9 guards; 1e-6 tolerance. |
| A9 | *G* clash | FULLY_ADDRESSED | GAP/INTRA. |
| A10 | Market counterpart of the components | FULLY_ADDRESSED | Matches `wm()` (`47:26`) and the F5O benchmark. |
| A11 | Control benchmark | FULLY_ADDRESSED | Matches `ctrl()` (`47:28-31`): equal-weighted, cut-offs from controls, at least 30 controls. |
| A15 | Two-way variance | FULLY_ADDRESSED | Matches `cl2` (`47:40-41`). The 20-observation minimum is not stated; no reported cell is affected. |
| A16 | HC1 factor | FULLY_ADDRESSED | `vcovCL(type="HC1")`: G/(G−1)·(N−1)/(N−K), K = 2. |
| A17/C4/C6 | "79 weeks", dependent variable, filters, Φ | PARTIALLY_ADDRESSED (residual: should_fix) | Dependent variable, filters (`40:23-24`), ties and Φ⁻¹ are now correct. The new wording of the periods contradicts itself (NEW-4). |
| A18 | NW details, *t*(78) | FULLY_ADDRESSED | `NeweyWest(lag=4, prewhite=FALSE)`, `pt(df = n_weeks − 1)`. |
| A19 | Momentum windows, IMOM | FULLY_ADDRESSED | `idxM3` = 60 days and `idxM6` = 110 days, both ending at τ−5; IMOM = ∏(1+r−m)−1. Appendix A added. |
| A21 | BH wording | FULLY_ADDRESSED | — |
| A23 | p_max definition | FULLY_ADDRESSED | C21 rows 2-3, 5-6. |
| A24 | Index clashes | FULLY_ADDRESSED | Events indexed by *e* in the Inference paragraph; Eq. (8) uses *r*, *s*; Eq. (2) uses *l*. |
| A26 | Stray comma | FULLY_ADDRESSED | — |
| A35 | Figure 2 caption | FULLY_ADDRESSED | Matches `42_rd.R:12,14,18,23` (window to nd−1, bins (6.5%, 10%], no factor, ±1.96). |
| A36 | Tercile and crash definitions | FULLY_ADDRESSED | Table 2 caption; `ter_t`, `mk_t` (`47:73-76`). |

### consider

| Ref | Comment | Status |
|---|---|---|
| A1, A37 | Optional reproducibility note; abstract benchmark | Not adopted. Acceptable: C2 1.660 and C16 1.664 both round to 1.7. |
| B1-B14 | Undescribed computations | B2, B3, B4, B5, B6, B7 and B13 are now in §4 or Appendix A. B11 is covered. B8, B10, B12 and B14 belong in a replication README (see NEW-11). |

should_fix_addressed_rate = 17/17 counted as FULLY or PARTIALLY addressed = 100%.

## New Issues

Attribution follows the protocol: `regression` = introduced by the round-3 revision; `previously_missed` = already in `manuscript_before_round3.Rmd`.

### Major severity

**NEW-1 (previously_missed; Major). "Near hits" are mostly limit closes on vendor-adjusted prices, not closes below the limit, so the claim "the effect grows as the close approaches the limit" is unsupported.**

Evidence. These are read-only diagnostics on the same data, using the code's own definitions from `47_da_response.R` lines 1-21:
- For near-hit ceilings (rule-based but not exact; 1,559 in the event window), the day-*d* return has the same distribution as for exact hits: median 6.89% against 6.90%, 5th percentile 6.61% against 6.67%. Near hits are therefore not smaller moves.
- About 80% of near-hit closes are not multiples of the tick size, against 0% of exact hits. Only 33% of their reference prices lie on the tick grid. In 850 of the 1,559 cases, the close is within half a tick of the computed limit price.
- For stocks priced at 10 thousand dong or more, only 26% (2024), 31% (2025) and 57% (2026) of all closes lie on the 0.05/0.10 tick grid. With two-decimal prices and no adjustment this share would be close to 100%. This is the signature of backward adjustment for later corporate actions.
- Near hits are 62% of rule-based ceilings with a reference price of 10 or more, but only 23% of those below 10, where the 0.01 tick equals the data's resolution. The exact/near split is therefore confounded with price level and with later corporate actions.

Consequences. (i) The proportional adjustment leaves the rule-based events (R ≥ 6.5%, C = H), locked days (O = H = L = C) and all returns except ex-date returns unchanged, so the main results are unaffected. (ii) The exact-hit and near-hit rows of Table 2, the "first day of a streak of exact hits" result, and the sentence that the effect "grows as the close approaches the limit" do not measure distance to the limit. (iii) Limitation (iv) understates the issue ("may adjust").

Required changes (exact strings). If the authors want numbers in the text, they must first save the diagnostic as an R output (e.g. `51_tick_grid.R` → `C27_tick_grid.csv` with: share of closes on the tick grid by year and price class; near-hit share by price class; quantiles of R for exact and near hits) and quote it inline. The replacements below contain no numbers.

1. §5, Table 2 paragraph.
   OLD: `` Near hits show a smaller gap (`r f(c11("Ceiling: near-hit (rule-based, not exact)","gap_mkt"),2)`%) and no significant intraday return, so the effect grows as the close approaches the limit. ``
   NEW: `` Near hits show a smaller gap (`r f(c11("Ceiling: near-hit (rule-based, not exact)","gap_mkt"),2)`%) and no significant intraday return. Their day-*d* returns are as large as those of exact hits, and many of their closes are not multiples of the tick size, which points to later price adjustment by the vendor rather than to closes below the limit. The split is therefore weighted toward higher-priced stocks, where the tick is coarser, and we do not read the difference as a gradient toward the limit. ``
2. §5, summary paragraph.
   OLD: `The ceiling effect survives alternative benchmarks, clusters, and definitions, grows as the close approaches the limit, and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture.`
   NEW: `The ceiling effect survives alternative benchmarks, clusters, and event definitions and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture.`
3. §7, limitation (iv).
   OLD: `(iv) The vendor may adjust prices for corporate actions in ways that affect event classification, and the listing snapshot excludes earlier delistings.`
   NEW: `(iv) The vendor appears to adjust earlier prices for later corporate actions: many closes of stocks priced at 10 thousand dong or more are not multiples of the tick size. Proportional adjustment leaves returns (except on ex-dates), the close-at-high event rule, and locked days unchanged, but it makes the exact-hit classification of Equation (3) unreliable, so we treat exact and near hits as a data check rather than as a measure of distance to the limit. The listing snapshot also excludes earlier delistings.`
4. §4, last sentence of "Returns and events".
   OLD: `Events that do not meet Equation (3) are near hits.`
   NEW: `Events whose close differs from the limit price of Equation (3) are near hits; Section 7 explains why this split depends on how the vendor adjusts prices.`

**NEW-2 (previously_missed; Major). The novelty claim about the overnight/intraday split contradicts the paper's own literature review.**

Quotes. §1: "none of the studies we reviewed splits the next-day return after a limit close into the overnight gap and the trading session that follows". §2: "Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits reverses during the following trading day, the timing pattern we test on HOSE … None of these studies splits the next-day return into the overnight gap and the session that follows." Table 5 then calls Huang et al. "Same timing: positive gap, partial intraday reversal". The evidence file (entry 4) records Huang et al.'s finding qualitatively ("overnight overreaction after daily limit hits … is corrected the following day"), with no magnitudes. A referee will read the §1/§2 claims as false. What the evidence supports is that no reviewed study quantifies the split against a benchmark.

Exact changes:
1. §1. OLD: `However, none of the studies we reviewed splits the next-day return after a limit close into the overnight gap and the trading session that follows, none places`
   NEW: `However, none of the studies we reviewed measures the overnight gap and the intraday return after a limit close against a market or control benchmark (Huang et al., 2001, describe an overnight overreaction after limit hits in Taiwan that is corrected on the following day, but the records we could access give no magnitudes), none places`
2. §1, contributions. OLD: `First, we decompose the next-day abnormal return after limit closes into an overnight gap and an intraday return, and show that the ceiling effect is a gap of`
   NEW: `First, we measure the overnight gap and the intraday return after limit closes, a pattern that Huang et al. (2001) describe qualitatively for Taiwan, and show that the ceiling effect is a gap of`
3. §2. OLD: `None of these studies splits the next-day return into the overnight gap and the session that follows.`
   NEW: `Apart from the qualitative account of Huang et al. (2001), none of these studies splits the next-day return into the overnight gap and the session that follows, and none reports its size.`

### Minor severity

**NEW-3 (regression; Minor). Broken character in the Figure 1 caption of both docx files.** The rendered caption reads "Corwin<U+2013>Schultz spread" (present in `manuscript_final.docx` and `manuscript_final_styled.docx`). The en dash inside the `fig.cap` chunk option is not converted.
OLD (fig1 `fig.cap`): `CSSPREAD, Corwin–Schultz spread;` NEW: `CSSPREAD, Corwin and Schultz spread;`

**NEW-4 (regression; Minor; residual of A17). The period definition contradicts itself.** The sample "from the 120th trading day onward" cannot have a first week that "ends on the 120th trading day". In the code, day 120 is the first formation day, and the first holding period is days 121-125 (`ts <- seq(120, nd - 5, by = 5)`, nd = 519 per C26, so the formation days are 120, 125, …, 510).
OLD: `We divide the sample from the 120th trading day onward into $T = 79$ non-overlapping five-trading-day periods, which we call weeks $\tau = 1, \dots, T$; the first week ends on the 120th trading day, so that every lookback is complete.`
NEW: `We form cross-sections every five trading days, on trading days 120, 125, and so on to day 510, which gives $T = 79$ formation dates, which we call weeks $\tau = 1, \dots, T$, each followed by a non-overlapping five-day holding period. The first formation date is the 120th trading day, so that every lookback is complete.`

**NEW-5 (regression; Minor). "They" has no antecedent in the Bonferroni paragraph.** (The pre-round-3 text named "the four event tests".)
OLD: `we compute $m_{\text{max}}$ from Section 4. They survive a Bonferroni correction at 5%`
NEW: `we compute $m_{\text{max}}$ from Section 4. All four event tests survive a Bonferroni correction at 5%`

**NEW-6 (regression; Minor). Table 1 caption: a semicolon creates a fragment, and the reference distribution differs from §4.** §4 says all Table 1 *t*-statistics use a *t*(G−1) reference. The caption limits this to week and 10-day.
OLD: `10-day block; each with a G/(G − 1) correction, where G is the number of clusters; we judge the week and 10-day statistics against a *t* distribution with G − 1 degrees of freedom.`
NEW: `10-day block, each with a G/(G − 1) correction, where G is the number of clusters; we judge all three against a *t* distribution with G − 1 degrees of freedom.` (both minus signs U+2212, as in the Rmd)

**NEW-7 (regression; Minor). The new generalization in §2 does not fit Chen et al. (2019), Lin et al. (2023) or Zeng et al. (2024).** These studies condition on limit-hit days or sort stocks by limit exposure; they do not "compare markets or periods".
OLD: `These designs compare markets or periods; ours conditions on individual limit closes within one band regime.`
NEW: `The band-change studies compare periods, and the cross-sectional studies sort stocks by their exposure to limits; we condition on individual limit closes within one band regime and measure the return that follows.`

**NEW-8 (previously_missed; Minor). The platform-change summary overstates stability.** Table 4: before the change, the ceiling close-to-close return is 0.83% (*t* = 1.0) and the floor gap −0.42% (*t* = −1.9). Neither is significant at 5%, and 71% of ceiling events fall after the change. "Both periods show the main pattern" hides this.
OLD: `Both periods show the main pattern, and the split cannot isolate an effect of the auction rules.`
NEW: `` Both periods show a positive ceiling gap followed by an intraday reversal, but before the change neither the ceiling close-to-close return (*t* = `r f(c22("Ceiling","cc1_mkt","pre_t"),1)`) nor the floor gap (*t* = `r f(c22("Floor","gap_mkt","pre_t"),1)`) is significant at the 5% level, so the full-sample significance rests mainly on the post-change events. The split cannot isolate an effect of the auction rules. ``
Also: OLD `The floor gap is larger after the move (` NEW `The floor gap is more negative after the move (`.

**NEW-9 (previously_missed; Minor). The H1 sentence overreaches.** The characteristics are weekly five-day slopes with limited power (the paper's own §5 and §6). "Information … that none of the 22 characteristics carries" is not shown.
OLD: `These tests support H1: limit closes carry information about the next day that none of the 22 characteristics carries.`
NEW: `These tests support H1: limit closes predict the next day's abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon.`

**NEW-10 (previously_missed; Minor). Attribution precision (evidence file entries 22 and 24; §6 scope).**
- OLD: `and Zeng et al. (2024) relate the frequency of limit hits to lower future returns.` NEW: `and Zeng et al. (2024) relate the frequency of upper-limit hits to lower future returns.` Table 5 cell, OLD: `Stocks with large limit exposure, or frequent limit hits, earn lower future returns` NEW: `Stocks with large limit exposure, or frequent upper-limit hits, earn lower future returns`. The evidence says "frequently hit the upper limit".
- OLD: `Liang and Hu (2025) forecast limit hits but leave returns after the hit unexamined.` NEW: `Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit.` The evidence file holds a search record only.
- §6. OLD: `on HOSE the continuation arrives at the next opening and ends after the first day.` NEW: `on HOSE the continuation after ceiling closes arrives at the next opening and ends after the first day.` Floors show later drift (C18: *d*+2 to *d*+5 −1.10%, *t* = −2.91).

**NEW-11 (previously_missed; Minor). Appendix A precision.**
- OLD: `and DOWNVOL is the root mean square of negative daily returns.` NEW: `and DOWNVOL is the square root of the mean of $\min(r, 0)^2$ over the same 60 days, so days with positive returns enter as zeros.` (`40_zoo.R:32`)
- OLD: `a regression of those returns on the market return.` NEW: `a regression of those returns on the dollar-volume-weighted return of the stocks in that week's cross-section, with weights at the formation day.` (`40_zoo.R:25`)

**NEW-12 (previously_missed; Minor). *p*-values printed in R's e-notation ("2.6e-06", "7.3e-05").** These are not journal style.
OLD: `` adjusted *p*-values from `r formatC(min(FAM$p_bh[23:26]), format = "e", digits = 1)` to `r formatC(max(FAM$p_bh[23:26]), format = "e", digits = 1)`) `` NEW: `` adjusted *p*-values of at most `r formatC(max(FAM$p_bh[23:26]), format = "f", digits = 4)`) ``
OLD: `` (largest *p*-values `r formatC(c21(2), format = "e", digits = 1)` and `r formatC(c21(3), format = "e", digits = 1)`, *t* reference) `` NEW: `` (largest *p*-values `r formatC(c21(2), format = "f", digits = 5)` and `r formatC(c21(3), format = "f", digits = 5)`, *t* reference) ``

**NEW-13 (previously_missed; Minor; replication package, not text).** There is no single entry point for the Paper C scripts: `paper2/R/run_all.R` does not exist, although the project rules require one. The order is 40 → 42 → 47 → 48 → 49 → 50, and 47 needs `rds/zoo_panel.rds` from 40. `48_revision.R` runs `readLines(".../47_da_response.R")[1:44]`. Any edit that shifts lines in 47 silently changes what 48 runs (round 3 changed line 21; the inherited lines still end at the `groups` list, so the output is unaffected this time). Recommended: a `run_all_C.R`, and a shared `47a_prep.R` that both scripts source. Process consistency: evidence-file entry 2 (Berkman and Lee) still says "abstract not retrieved", while `integrity_stage4_5_final_v2.md` records abstract-level verification. Update the entry.

## Numeric spot-check log (manuscript value → saved source → verdict)

All values were read from the rendered docx and compared with the CSV value under the manuscript's rounding (`formatC`, half-up away from ties).

| Location | Manuscript | Source | Check |
|---|---|---|---|
| Abstract | 347 stocks | `nstocks`; C26 row 3 = 347 | ✅ |
| Abstract | next-day AR 1.7% | C2 ceiling t+1 1.6602 | ✅ |
| Abstract | gap 2.2%, reversal 0.5% | C16 Ceiling all gap 2.2435, intraday −0.5354 | ✅ |
| Abstract | 2.7 pp vs 5-6.5% | C17 2.6582 | ✅ |
| Abstract | buyer loses 0.7% | C11 Ceiling rule-based f5o −0.7486 | ✅ |
| §1 | 2.0% / 1.4% of stock-days | C13 3,207/156,653 = 2.047%; 2,115/156,653 = 1.350% | ✅ |
| §1 | reverses 24% | 0.5354/2.2435 = 23.9% | ✅ |
| §3 | 743 rows, 405 files, 519 days, 347 kept, 178,773 stock-days | C26 rows 2, 1, 4, 3; ΣC9b n = 178,773 = C26 row 5 | ✅ |
| §3 | mean 0.018%, median 0.00%, SD 2.10% | C26 0.01788, 0, 2.0982 | ✅ |
| §3 | median 2.6, mean 51.2 billion dong | C26 2,557.7 and 51,226.3 million (DV = thousand-dong price × shares, /1000) | ✅ |
| §3 | 18 sectors, 15% | C26 18, 14.99 | ✅ |
| §3 | 1.98%, 1.30%, 0.29% | C9b 1.0768+0.9073; 0.6354+0.6673; 0.2875 | ✅ |
| §5 | 3,187 on 446 dates; 2,105 on 319 | C2 | ✅ |
| §5 | max |t| 1.45 (MOM3M, IMOM); conf. 1.17, 1.14 | C1 1.452/1.448; 1.168/1.145 | ✅ |
| §5 | VOL −0.09, IVOL −0.54, MAX −0.02 | C1 | ✅ |
| §5 | 18 of 22 net spreads negative | C1 count | ✅ |
| §5 | MDE 0.12-0.31; lag-8 max 1.79; excl. illiquid 1.62 | C14, C1 | ✅ |
| §5 | Table 1 values 1.66, 1.45, −0.71, −1.76; BH 2.6e-06 to 4.0e-04 | C2, C3 p_bh | ✅ |
| §5 | floor 5-day week second-half *t* −2.22 (smallest margin) | C18 (others 13.67, 4.95, −4.57) | ✅ |
| §5 | *d*+2 to *d*+5: −0.24 (−1.53), −1.10 (−2.91), conf. −1.14 | C18 | ✅ |
| Table 1 | all 6 rows × 6 columns | C18 | ✅ |
| §5 | gap 2.24 (9.7), intraday −0.54 (−3.5), floor −0.97 (−4.6), 0.30 | C16 | ✅ |
| §5 | exact 2.79, streak exact 2.39, near 1.67 | C11 (new) 2.7856, 2.3892, 1.6719 | ✅ |
| §5 | tercile 3 1.52; ctrl gap 2.70; floor ctrl cc −1.65; 740 of 2,111; *t* −1.0 | C16, C11 | ✅ |
| §5 | f5o −0.75 (−2.7), ctrl −0.53 (−1.8), giveback 0.54, 522 locked, floor f5o −0.82 (−1.7) | C11, C16 | ✅ |
| Table 2 | 16 rows × 5 columns | C11 (exact, near, ctrl rows), C16 (others) | ✅ (exact 1,642 / near 1,557; floor 1,025 / 1,086) |
| §5 | Table 3 text 2.66 (14.0), 0.31, 1.59 (−9.7), 3.14 (14.5), 1.81, 2.40, 1.14 | C17, C23 | ✅ |
| Table 3 | 8 rows × 5 columns | C17, C23 | ✅ |
| §5 | attention 1.97/2.16/2.63; 1.41/2.18/3.16; *t* 4.8, 4.2; floor −1.20 to −0.68 | C24 | ✅ |
| §5 | KRX 1.65/2.49 (1.6); −0.42/−1.37 (−3.2); 0.64; −1.73/−0.15; 71%, 58% | C22 (2,263/3,199; 1,220/2,111) | ✅ |
| Table 4 | 8 rows | C22 | ✅ |
| §5 | 96 stock-days; 2.24→2.26; −0.97→−0.98 | C9b (38+58); C25 | ✅ |
| §5 | 683, 125; 7.3e-05, 4.0e-04 | C21 rows 5, 6, 2, 3 | ✅ |
| §6 | "about two" / "about one" pp at the open; 2.0%; −0.75% | C16, C13, C11 | ✅ |
| §8 | 1.7, 2.2, 0.5, 2.7, 3.1, −1.0, 0.7 | C2, C16, C17, C23, C11 | ✅ |
| Fig. 2 | 3,220 ceiling events (window to nd−1) | C5 | consistent with caption ✅ |

No number in the text, tables or captions disagrees with a saved output. All are inline R references; none is hand-typed.

## Equation and method verification (Section 4, Appendix A)

| Item | Code | Verdict |
|---|---|---|
| Eq. (1) | `Rd <- rbind(NA, Cc[-1,]/Cc[-nd,] - 1)` | MATCH |
| Event rule, window | `40:59`, `47:19`, `61:(nd-5)` | MATCH |
| Eq. (2) and set of stocks | `40:14,56`; `48:7` | MATCH |
| Weight timing by table | `40:56-57`, `47:26`, `40:25` | MATCH |
| Eq. (3), δ, guards, tolerance, previous close | `47:16-18` | MATCH |
| Exact hit ⊂ event | `47:21` | MATCH (but see NEW-1 on meaning) |
| Eq. (4) | `40:57,62`, `48:8,12` | MATCH |
| Eq. (5) and abnormal components | `47:14,37` | MATCH |
| Next-open buyer benchmark | `F5O - wm(F5O)` | MATCH |
| Control benchmark | `47:28-31` | MATCH |
| Eq. (6) | `48:15` | MATCH |
| Family p-values without factor, normal | `40:63,66` | MATCH |
| Two-way variance, 1e-12 floor | `47:40-41` | MATCH |
| Regression, HC1 factor | `47:85-86`, `48:49-50` | MATCH |
| Weekly cross-section filters | `40:23-24` | MATCH; period wording NEW-4 |
| Rank normal scores, ties | `40:19` | MATCH |
| Dependent variable | `40:38` | MATCH |
| Eq. (7), NW(4) Bartlett, no prewhitening, *t*(78) | `40:42-43,53` | MATCH |
| MDE = 2.8 × SE | `47:61` | MATCH |
| Quintile spread and cost (Appendix A) | `40:46-50` | MATCH (first-week cost zero not stated; trivial) |
| Eq. (8), Holm, |*t*| = 3 | `40:72` | MATCH |
| Survival rule, halves | `40:45,64,73-74`; `48:18-22` | MATCH |
| Bonferroni bound | `48:36-37` | MATCH |
| Appendix A characteristics | `40:26-37` | MATCH except DOWNVOL and the BETA/IVOL market (NEW-11) |
| Sample description | `50:8-15` | MATCH |

## Cross-reference and consistency check

- H1-H4 are stated in §2 and resolved in §5: H1 (Table 1 paragraph; wording NEW-9), H2 (Table 2), H3 (Table 3, after the close-at-high comparison), H4 (next-open paragraph). The summary "support H1 to H4" is consistent. H3 and H4 were reworded in round 3, and the resolutions match the new wording.
- Abstract, §1 contributions and §8 agree on every number and on the hedged mechanism statement.
- Section references (1-8), Tables 1-5, Figures 1-2, Equations (1)-(8) and Appendix A are all cited and exist. "Equation (2)" in the Table 2 caption is correct (crash days use `mk_t` with weights through *d*).
- No internal-process language in the manuscript (searched for stage, pipeline, reviewer, round, integrity, README, post hoc, checkpoint). The "Analysis plan" paragraph and the Declarations are appropriate disclosures. The analysis-plan commit 63bdc6d exists (2026-10-04 07:23) and predates the first commit of `40_zoo.R` (07:36).

## Literature claims (against the evidence file)

No UNVERIFIED magnitude appears: Lou "2% per month", Hendershott, the Chen et al. (2019) percentages and the Qiao-Dam 14 bp are all absent. Kim and Rhee, Bildik and Gülay, Chen (1993), Cho et al., Kim and Limpaphayom, Deb et al. (2013), Qi, Zhang, Jia, Lien, Kim and Jun, Chen et al. (2019), Lin et al., Kelly and Clark, Berkman et al. (2012), Aboody, Lou, Akbas, Bogousslavsky, Lu, Qiao and Dam, Qiu, Jones, Harvey et al., Harvey and Liu, Chordia (3.38 as "near 3.4"), Hou (65% of 452) and Huang et al. (2023) agree with their entries. Exceptions: NEW-2 (Huang et al. 2001 versus the novelty claim), NEW-7 (generalization), NEW-10 (Zeng "upper-limit", Liang and Hu). Berkman and Lee (2002) is stated conservatively and agrees with the integrity report's abstract-level check, though not yet with evidence-file entry 2 (NEW-13).

## Decision Rationale

All five must_fix items (A4, A5, A13, A14, A22) are FULLY_ADDRESSED and verified against the code, and the exact-hit code change propagated correctly to C11, C13 and the text. should_fix_addressed_rate = 100%, with one PARTIALLY_ADDRESSED item (A17) whose residual is should_fix. New regression-attributed issues are all minor (NEW-3 to NEW-7), so B5 gives **Minor Revision**. B1-B4 do not fire. NEW-1 and NEW-2 are previously_missed and do not enter Step 2 (goalpost guard). They are recorded for Stage 4' / 4.5. No escalation-exception class (research_integrity, fatal_validity, and so on) applies: NEW-1 affects one robustness split and one sentence, not the headline estimates.

## Publishability assessment (whole paper)

Judgment: after the text fixes above, the paper is publishable in a good field journal (emerging-markets finance or market microstructure). It would most likely receive a minor or major revision from referees, not acceptance as is. Strengths: a clean and fully reproducible event design; every number tied to saved output; a careful separation of the gap, the intraday return and next-open tradability; a comparison with near-limit and close-at-high movers that strengthens H3; inference that is unusually transparent (three cluster schemes, *t* references, two-way clustering, a Bonferroni bound); candid limitations.

Remaining substantive weaknesses that a demanding referee will raise (known disclosed items such as the short sample and the lack of news or order-book data are not repeated here):
1. **Data quality of the price files (NEW-1).** Evidence of backward adjustment means that any tick-based analysis is unreliable. The authors should say so in the data section, not only in limitations.
2. **Novelty is narrower than §1 claims (NEW-2).** The decomposition pattern is known qualitatively from Taiwan (Huang et al., 2001) and for attention stocks in general (Berkman et al., 2012). The contribution is a careful benchmarked measurement on HOSE, plus the near-limit comparison and the tradability result. The paper should be framed that way.
3. **The 26-test family does little work.** The four event tests have |*t*| of 4 to 5 and would pass BH on their own. The 22 weekly characteristic slopes test a different hypothesis at a different horizon, with low power (MDE 0.12-0.31 pp per week). "All four survive a family in which no characteristic survives" is therefore close to mechanical. The Bonferroni bound (m_max = 683 with date clusters, 125 with week clusters) is the more informative multiplicity statement and could carry the third contribution.
4. **Regime dependence.** 71% of ceiling events and most of the statistical strength come after the May 2025 platform change. Before it, the ceiling close-to-close effect is insignificant (*t* = 1.0) and so is the floor gap (*t* = −1.9) (NEW-8). Referees will read this as more than a "short sample" caveat.
5. **Overlapping five-day windows of the same stock (streaks).** In Table 1 and in the family, these are handled only through date, week and block clustering. The 10-day block result (*t* = 3.81 for the ceiling five-day CAR) mostly answers this. One sentence saying so would pre-empt the question.

## Residual Issues (Acknowledged Limitations if not fixed at Stage 4')

- NEW-1 and NEW-2 should be fixed rather than acknowledged, since each is a short text change.
- NEW-13 (replication entry point, fragile line-number sourcing) should be fixed in the replication package before the data and code statement is final.
- Weakness 3 (role of the 26-test family) can stay as an author choice, provided the third contribution is not described as stronger than the evidence.
