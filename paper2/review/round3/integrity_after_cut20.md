# Integrity re-verification after the 20% cut (Stage 4.5, narrow scope)

Date: 2026-10-06. Verifier: independent integrity verification agent (academic-pipeline `integrity_verification_agent.md`, `integrity_review_protocol.md` Stage 4.5). Scope: only what the 65 edits in `cut20_edits.md` could break. The manuscript and code were not edited.

## Verdict: FAIL (fixable; 8 required string fixes, 4 recommended)

The cut introduced no numerical errors and no citation or reference mismatches. It did break three items, all from compression: two claims were strengthened past their source or data (R1, R2), and the bounded novelty statement was widened (R3). Five more required fixes cover a misattribution, two dropped qualifiers, one methods-code mismatch, and the lost formation-week disambiguation (R4-R8). Applying R1-R8 verbatim should allow a PASS without another full check. A spot check of the edited sentences is enough.

## What was checked and how

- **Edit fidelity.** Applying the 65 old→new pairs of `cut20_edits.md` to `manuscript_before_cut20.Rmd` gives a file byte-identical to `manuscript_final.Rmd`. Each old string occurred exactly once. Nothing else changed.
- **Rendered docx is current.** It was rendered at the same time as the Rmd, and the abstract and all other edited text appear in `pandoc ... -t plain`. Both figures are embedded (`rId24.png`, `rId27.png`).
- **Inline numbers (check 2).** The cut added no new inline R expression; the set of new expressions is empty. It removed 7 expression instances, all repeats. Every remaining expression is identical to the version that passed Stage 4.5. Rendered values were spot-checked against `output/tables/` and all match:
  - C27: 25/31/58/100%; 62% and 23%; 83%; medians 6.89 (near) and 6.90 (exact), with the correct attribution.
  - C21: 683 and 125; p_max 0.00007 and 0.00040.
  - C14: MDE 0.12-0.31; lag-8 maximum 1.79.
  - C1: maximum |t_nw| 1.45; maximum |t_disc| 1.29; maximum |t_conf| 2.77, so "none reaches |t| = 3 in any sample or 1.96 in the full sample" is supported. Excluding illiquid stocks, the maximum is 1.62.
  - Table 4 shares: 71% (2263/3199) and 58% (1220/2111).
  - Tables 1-4: all prose values match the rendered tables.
- **Citations ↔ references (check 5).** All 51 references are cited, and every in-text author-year has a reference entry (script check on the rendered text). Bali et al. (2011), Parkinson (1980), Amihud (2002) and Corwin and Schultz (2012) are now cited only in Appendix A, which is fine. No broken characters were found: no U+FFFD, no "NA"/"NaN"/"Inf", and the Unicode subscripts and dashes render correctly.
- **Call-outs (check 5).** Figures 1-2 and Tables 1-5 are each called out before the exhibit. Table 3 is first mentioned in Section 4.
- **Captions (check 5).** The shortened captions for Figures 1-2 and Tables 1-5 remain accurate. Figure 1 says "Appendix A defines the labels", and Appendix A defines all 22. On the Table 2 caption, see M4.
- **Required content (check 3).** All of the following survive:
  - H1 ("These tests support H₁"), H2 ("as H₂ predicts"), H3 ("which supports H₃"), H4 ("which supports H₄"), and the summary "support H₁ to H₄".
  - The near-hit / vendor-adjustment reading with its C27 numbers, in Section 5 and limitation (iv). See R2 for one distortion.
  - The bounded novelty statement against Huang et al. (2001): Introduction P2, contributions, and the Section 2 gap. See R3 for the Section 6 widening.
  - The platform-change caveat: pre-change t = 1.0 and −1.9, "rests mainly on post-change events", and "cannot attribute ... to the auction rules".
  - The analysis-plan disclosure: no registry, four departures, the exploratory list, H2-H4 marked exploratory, and screening / effect sizes possibly overstated.
  - Limitations (i)-(viii). The delisting caveat is kept in (iv).
  - The AI-use statement and the data and code statement.
- **Section 4 (check 4).** Equations (2)-(8) are each referenced by number. Equation (3) is now referenced only in Section 7. Equation (1) is not referenced by number; this predates the cut (see M3). The symbols are mostly defined; see M1 and M2. The methods were checked against `R/40_zoo.R`, `R/42_rd.R` and `R/47_da_response.R`:
  - ±1e-9 inside floor and ceiling: ✓.
  - The 115-day lookback with returns, opens and closes complete: ✓.
  - BETA market weights at the formation day: ✓.
  - The trade-day filter is `>= 50` in the code, but the text now says "50 of the last 60" (R7).
  - The HC1 `vcovCL` and the two-way bound of 1e-12: ✓.
  - The formation-week vs calendar-week disambiguation was removed by E26 (R8).
- **Literature fidelity (check 1).** Every compressed Section 2 sentence and every Table 5 cell was checked against `process/08_literature_review_benchmark.md`. Each remains consistent except Kodres and O'Brien (R5), Zeng et al. (R4) and the Hou et al. Table 5 cell (R6).

## Required fixes (each old string is unique in `manuscript_final.Rmd`)

**R1 (E38; claim strengthened: the unobserved mechanism is stated as fact).** The pre-cut text hedged ("may carry a queue of unfilled buy orders"). The data have no order book (limitation ii says "we infer the unfilled-demand mechanism").
- OLD: `Unfilled buy orders carried into the night and any overnight news set the opening price, and the intraday reversal suggests that part of that price reflects transient demand.`
- NEW: `A stock that closes at its ceiling may carry unfilled buy orders into the night; those orders and any overnight news would set the opening price, and the intraday reversal suggests that part of that price reflects transient demand.`

**R2 (E39; data distortion).** The new text says the vendor adjustment is "concentrated in higher-priced stocks". C27 cannot show this. The below-10 check is uninformative because the 0.01 tick equals the file resolution, as limitation (iv) itself says. What is concentrated in higher-priced stocks is the near-hit classification (62% vs 23%).
- OLD: `This points to later price adjustment by the vendor, concentrated in higher-priced stocks with coarser ticks, rather than to closes below the limit, so we do not read the difference as a gradient toward the limit.`
- NEW: `This points to later price adjustment by the vendor rather than to closes below the limit. The split is therefore weighted toward higher-priced stocks, where the tick is coarser, and we do not read the difference as a gradient toward the limit.`

**R3 (E54; novelty widened beyond the reviewed set).** "No earlier study" is an unbounded claim. The pre-cut sentence was scoped to the sources in Table 5 and to specific outcomes. Huang et al. (2001) do describe post-limit returns, though qualitatively.
- OLD: `No earlier study reports post-limit returns in a form that matches ours, so Table 5 compares signs, timing, and mechanism.`
- NEW: `None of the studies we reviewed reports the next-day abnormal return, overnight gap, or intraday return after a limit close in a form that matches ours, so Table 5 compares signs, timing, and mechanism.`

**R4 (E9; attribution moved to the wrong study).** "as do" attaches Lin et al.'s attention and retail-concentration findings to Zeng et al. (2024). The benchmark record for Zeng et al. reports only lower future returns, explained by overreacted trading.
- OLD: `as do stocks with frequent upper-limit hits (Zeng et al., 2024).`
- NEW: `and stocks with frequent upper-limit hits also earn lower future returns (Zeng et al., 2024).`

**R5 (E7; source qualifiers dropped).** The benchmark record says "judiciously chosen price limits" that "partially insure implementation risk".
- OLD: `Kodres and O'Brien (1994) show that limits can be Pareto superior when fundamental news drives prices because they insure traders against implementation risk`
- NEW: `Kodres and O'Brien (1994) show that well-chosen limits can be Pareto superior when fundamental news drives prices because they partly insure traders against implementation risk`

**R6 (E56; condition dropped from a Table 5 cell).** Hou et al.'s 65% holds with microcaps mitigated; the Section 2 text keeps this condition.
- OLD: `"65% of 452 anomalies fail the 1.96 hurdle; a new factor needs *t* above 3.0"`
- NEW: `"With microcaps mitigated, 65% of 452 anomalies fail the 1.96 hurdle; a new factor needs *t* above 3.0"`

**R7 (E26; text no longer matches the code).** `40_zoo.R` line 23 uses `colSums(Vv[w60, ] > 0) >= 50`, but the text says "50 of the last 60".
- OLD: `trades on 50 of the last 60 days`
- NEW: `trades on at least 50 of the last 60 days`

**R8 (E26; formation weeks vs calendar-week clusters).** The parenthetical that kept the two apart ("they differ from the calendar weeks used for clustering") was deleted. "Weeks" now names both the τ periods (the "first 39 weeks") and the ISO-week clusters ("t (week)"), so the definition must be explicit.
- OLD: `$T = 79$ formation weeks $\tau$, each followed`
- NEW: `$T = 79$ formation weeks $\tau$ (five-trading-day periods, not the calendar weeks used for clustering), each followed`

## Recommended fixes (not verdict-determining)

**M1 (E25; symbols not defined).** E25 dropped the definitions of $\alpha$, $u_e$ and the $D_e = 0$ group.
- OLD: `where $D_e = 1$ for limit closes, with`
- NEW: `where $D_e = 1$ for limit closes and 0 for the comparison moves, $\alpha$ is the intercept, and $u_e$ is the error, with`

**M2 (E27; symbols not defined).** E27 dropped the definition of $\varepsilon_{i,\tau}$, and $\gamma_\tau$ was never defined.
- OLD: `with weekly intercept $a_\tau$.`
- NEW: `with weekly intercept $a_\tau$, slope $\gamma_\tau$, and residual $\varepsilon_{i,\tau}$.`

**M3 (predates the cut).** Equation (1) is never referenced by number, also true of the pre-cut version.
- OLD: `A ceiling event has $R_{i,d} \geq 0.065$`
- NEW: `A ceiling event has a return (Equation (1)) of $R_{i,d} \geq 0.065$`

**M4 (E41; caption lost the event-count note).** Table 2 lists 3,199 ceiling and 2,111 floor events, against 3,187 and 2,105 in Table 1. The removed caption sentence explained the difference.
- OLD: `Close-to-close need not equal the sum of the components because returns compound.`
- NEW: `Close-to-close need not equal the sum of the components because returns compound. Events are the stock-days that meet the event definition and have the stated return.`

## Not an integrity issue; no action

- In E30, "terciles" now covers the liquidity terciles as well as the volume and prior-return terciles. This labels more analyses as exploratory, which is conservative.
- In E62, the investor sentence drops the number ("lost money against the market"). The number appears in the abstract, Section 5 and the conclusion.
- In E59, the Section 6 platform sentence no longer repeats "cannot isolate the auction rules". Section 5 keeps the full caveat.

## Application of R1-R8 and M1-M4 (author-agent, 6 October 2026)
All twelve replacement strings above were applied verbatim to `manuscript/manuscript_final.Rmd` (each old string matched exactly once). The re-rendered docx contains each new string exactly once (presence check by grep on the plain-text rendering). Rendered length: about 8,160 words. This application check was done by the author-agent, not by a fresh verifier; the verifier's report states that applying R1-R8 verbatim is sufficient for PASS after a spot check of those sentences.
