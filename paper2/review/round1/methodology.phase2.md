contract_role: methodology
## Dimension Scores

### D1: methodology_rigor

score: warn
trigger: "Dependence-robust inference, benchmark choice, event definition or split design is reported incompletely or only partly justified"

### D2: domain_accuracy

score: not_assessed

### D3: argumentative_coherence

score: warn
trigger: "Some conclusions are phrased more strongly than the evidence supports"

### D4: cross_disciplinary_relevance

score: not_assessed

### D5: writing_and_structure

score: not_assessed

### D6: venue_fit_and_contribution

score: not_assessed

## Review Body

Scope and method. This review covers methodological rigor (D1) and the methodology-eligible part of argumentative coherence (D3) for a generic Q1/Q2 finance journal; no venue criteria are invoked and no venue-fit claim is made. I checked the manuscript's headline numbers against the saved tables and code in `paper2/` (Tables 2 and 3 tie exactly to the saved tables C1, C2 and C3; the event counts 3,220, 3,207, 3,199 and 3,187 are reconciled in the Table 7 caption and the code; the 79 weekly decisions follow from days 120 to 514 in steps of five; the Bonferroni bound of 816 and the largest event p-value of 6.1e-05 reproduce from the saved tables only under a normal reference distribution; minimum detectable slopes are consistent with the reported slopes and t-statistics). Several concerns listed in my configuration card did not materialise on checking: the survival rule is coded uniformly for all 26 tests, and CSSPREAD and RANGEVOL (confirmation-half t of -2.77 and -2.35, with sign opposite to the discovery half) fail the full-sample BH step in any case, so they do not bear on the 0-of-22 claim. Dollar counts, the 3,187 versus 3,220 difference and the weekly-block arithmetic are explained in the text or the code.

Overall assessment. The study is a careful short-sample event study with unusually candid disclosure of post hoc steps and specification deviations. The central descriptive finding, a large positive overnight gap after ceiling closes and a negative gap after floor closes in this sample, is supported by several cuts that do not depend on one clustering or benchmark choice. The weaknesses concern (i) the inference behind the formal "4 of 4 survive" statement at the t+1..t+5 horizon, (ii) the weight carried by the word "pre-specified" and by the family-wide frame, and (iii) the strength of the mechanism and "discontinuity" language. None of these, as far as I can determine, would overturn the existence of the gap on re-analysis, so I score both dimensions warn rather than block.

### S1: Candid disclosure of specification deviations and post hoc status

**Evidence Anchor**: text: §3.1 "it is not an external registry entry"

The manuscript separates pre-specified from post hoc analyses (Appendix A, Section 3.2), lists five deviations (a) to (e) between specification and implementation, discloses the 59-day versus 60-day correction, and states that the earlier project manuscripts make the specification not independent. This is above the norm for the field and makes the remaining concerns auditable.

### S2: Uniform survival rule and multiplicity control with power disclosure

**Evidence Anchor**: table: Table 8, minimum detectable slope column and Newey-West lag sensitivity

The BH, Holm and HLZ thresholds are applied across all 26 tests with one survival rule (verified in `paper2/R/40_zoo.R`), Newey-West lag sensitivity is shown for all 22 characteristics, and minimum detectable slopes and effective number of tests are reported, which tempers the null claim.

### S3: Definition, benchmark and clustering stress tests of the event result

**Evidence Anchor**: table: Table 7, rows exact tick-rule hit, near-hit and first day of streak

The gap result is repeated under an exact tick-rule definition, near-hit versus exact-hit contrast, streak starts, locked-day split, liquidity terciles, a same-date matched control and two-way clustering (Tables 4 to 7). The overnight gap keeps its sign and large t-statistic throughout, which supports the descriptive core.

### W1: Inference for the t+1..t+5 tests and the "4 of 4 survive" statement rests on date-only clustering with overlapping windows

**Severity**: Major
**Evidence Anchor**: table: Table 3, row ceiling t+1..t+5 (t 4.01, first half 1.78, second half 6.82) and row floor t+1..t+5 (second half -2.16)
**Confidence**: 4 — I read the clustering code (`clus()` sums residuals by event date only) and recomputed pooled-versus-half standard errors; I did not re-run the estimation on the raw data.

The headline survival test uses standard errors clustered on the event date alone (code and Section 3.1). Five-day windows from events on adjacent dates share four days of returns and the same market shocks, so the date totals are serially dependent. Two-way clustering is reported only for the one-day outcome, post hoc, and no calendar-block, HAC-over-dates or calendar-time portfolio alternative is given for the five-day outcome. The half-sample statistics show strong heterogeneity of cluster variance: ceiling t+1 has t of 2.28 in the first half and 14.36 in the second, and floor t+1..t+5 has -11.57 in the first and -2.16 in the second. (Recomputing the pooled standard error from the Table 6 halves gives a pooled t near 5, so these figures are internally coherent; they indicate that the first-half standard error is dominated by a few dates or episodes.) The "survives" rule requires a confirmation-half |t| above 1.96, and the floor five-day test clears that bar by only 0.2 of a t-unit under the unadjusted clustering. Section 6 (vii) concedes that dependence may exceed what date and stock clustering allows. The existence of the one-day gap is unlikely to depend on this, but the abstract's "4 of the 4 limit tests survive" for the nested t+1..t+5 horizons does. A block bootstrap by calendar week or a Driscoll-Kraay style estimate for both horizons, with the survival rule re-evaluated, is what would settle it.

### W2: The "pre-specified" and family-wide frame carries more weight than an internal log can bear

**Severity**: Major
**Evidence Anchor**: text: §3.1 "it is not an external registry entry"
**Confidence**: 4 — based on the manuscript's own statements and the process references it cites, which I did not open.

The abstract and conclusion state the family of 26 as pre-specified. The manuscript itself states that the specification lives in an internal log, that two earlier manuscripts on related data had already been completed, that this paper was chosen from 14 candidate ideas after two nulls, and that its event-horizon definition (t+1..t+5 instead of the specified t+2..t+5) and its split rule for event tests (median event date instead of weeks 39 and 40) differ from the specification. The log is cited by file name and is not available to readers. In that situation the label is best read as "fixed by the authors before this computation" rather than as a registered ex ante design. The family-wide frame protects against the 22 characteristics being a snapshot of a larger search, but it does not remove the selection of the limit idea itself; the Bonferroni bound for "up to 816" project-wide tests in Section 4.7 is an arbitrary program size and bounds false discoveries without bounding the winner's-curse bias, as the authors acknowledge. The result for the specified horizon t+2..t+5 is not reported, so the reader cannot see whether the substitution mattered. I would ask for the abstract to say "specified in an internal log before computation", for the log to be deposited with timestamps or hashes, and for the originally specified t+2..t+5 test to be shown next to the implemented one.

### W3: Mechanism and "discontinuity" language outruns a design with no limit-free counterfactual and no news control

**Severity**: Major
**Evidence Anchor**: text: §5 "This points to a mechanism attached to the constraint and is the main reason we describe the result as a discontinuity."
**Confidence**: 4 — the design is fully described in the manuscript; this is a judgement about what it identifies.

Section 4.4 correctly calls the contrast "an association around a rule-based threshold, not a randomized or exact regression-discontinuity design", and states that limit-reaching stocks may differ in news content. The discussion then uses the same contrast as the main support for a mechanism "attached to the constraint", and Section 5 draws a regulatory implication that "the limit does not settle the price on the limit day". The evidence consists of a binned plot and a difference against stocks that moved 5-6.5% (Table 5), with no bandwidth, local polynomial fit, manipulation test, or covariate balance. Stocks that close at the ceiling plausibly differ from stocks that close 1% below it in news intensity, attention and order imbalance, which are exactly the alternative that the delayed-price-discovery reading must be distinguished from. Table 5 itself shows that from the next open to day 5 the ceiling group does not differ from the 5-6.5% group (-0.02, t = -0.1), which means the later drift is generic. No discriminating evidence is offered, such as announcement dates, or comparison with the same stocks on days without a binding limit or with a different limit regime. The descriptive claim (large gap at limit closes, not tradable at the open) is supported; the mechanism and policy wording should be reduced to "consistent with".

### W4: Event p-values use a normal reference while the characteristic p-values use a t reference, and the reference is not stated

**Severity**: Minor
**Evidence Anchor**: text: §4.7 "all four event tests would still survive a Bonferroni correction at 5% for a project-wide family of up to 816 tests"
**Confidence**: 4 — verified in `paper2/R/40_zoo.R` (event p-values by `pnorm`, characteristic p-values by `pt` with 78 df) and by recomputation.

The manuscript states neither the df nor the reference distribution for the date-clustered t-statistics. In the code the event p-values come from a normal reference. With 446 date clusters, a t reference with 445 df gives about 7.1e-05 instead of 6.1e-05 for the weakest event test (t = 4.01), and the largest program size for which all four survive Bonferroni falls from 816 to about 700. The four tests still pass the BH threshold by a wide margin, so the main claim is unaffected, but the figure of 816 is sensitive to a choice the paper does not disclose, and the 26-test BH step mixes two reference distributions. The corresponding arithmetic receipts (AR1, AR2) are not computable from the reported values for that reason.

### W5: The abnormal return benchmark is a dollar-volume-weighted market without size or beta adjustment, and the floor magnitude depends on it

**Severity**: Minor
**Evidence Anchor**: table: Table 6, row Floor all, columns Close-to-close vs market (-0.69) and Close-to-close vs controls (-1.65)
**Confidence**: 4 — the dependence is shown in the manuscript's own table and text.

The authors report that the benchmark matters (floor close-to-close -0.69% versus -1.65%; ceiling 1.66% versus 2.16%) and that floor events concentrate on market-wide down days where beta is relevant (740 of 2,111 floor events survive excluding days with a market fall above 2%). The control group is matched on liquidity tercile only. The headline floor figure of -0.71% in the abstract therefore depends on an unadjusted benchmark choice that the abstract does not flag. A beta- and size-matched control or a market-model abnormal return would make the floor effect interpretable.

### W6: The abstract's null for 22 characteristics is stated without the power qualifier that the body supplies

**Severity**: Minor
**Evidence Anchor**: text: Abstract "0 of the 22 characteristics survive"
**Confidence**: 4 — compared the abstract with Section 4.1 and Table 8.

Section 4.7 reports that the minimum detectable slope at 80% power lies between 0.12 and 0.31 percentage points per week per standard deviation, and that the effective number of tests is about 6.8 to 14. Several observed slopes (for example MOM3M 0.123) are inside that range, so "0 survive" cannot be read as evidence of no effect. The abstract and conclusion state the null without this limit; a clause stating the detectable-effect scale would keep the abstract consistent with the body.

### W7: Return outliers beyond the limit band and a snapshot universe are acknowledged but not examined

**Severity**: Minor
**Evidence Anchor**: table: Table 1, rows below -8.0% (38 stock-days) and above 8.0% (58 stock-days)
**Confidence**: 3 — the cause of these returns cannot be determined from the manuscript.

With a 7% band, 96 stock-days with a close-to-close return beyond 8% in absolute value suggest unadjusted corporate-action prices or listing-day effects, and the vendor does not document adjustment. The universe is a listing snapshot dated after the sample, so delisted stocks are absent; floor events are plausibly over-represented among stocks that later delisted. Both are disclosed in Sections 2, 4.7 and 6, but neither is bounded, for instance by dropping those stock-days or events within five days of them and re-estimating.

### W8: A headline tradability number has no table in the manuscript

**Severity**: Minor
**Evidence Anchor**: absence: Abstract and §4.6 — expected a table reporting the -0.75% (t = -2.7) next-open-to-day-5 return against the market; checked Tables 3 to 8 and Appendix A
**Confidence**: 4 — the number exists in the saved table C11, but not in the manuscript.

The abstract and Section 4.6 report -0.75% (t = -2.7) from the next open to the fifth close relative to the market. Tables 5 and 7 show only the contrast against the comparison group and against same-date controls. Exact-tick ceiling counts also differ across Table 4 (1,666), Table 7 (1,648) and the saved universe table (1,654) with only part of the difference explained in the Table 7 caption. These are traceability gaps only; I found no numerical conflict.

### W9: Data and code availability does not provide the raw data or a retrieval manifest

**Severity**: Minor
**Evidence Anchor**: absence: Data and code availability — expected a raw-data deposit or retrieval manifest with the vnstock version and download date; checked Section 2, Declarations, Appendix B
**Confidence**: 3 — I could read the raw files in the repository, but the manuscript does not tell an external reader where they are.

Code and derived tables are referenced, but the daily files, the vnstock version, the retrieval date and the process logs cited for pre-specification are not deposited. A third party therefore cannot rebuild the sample filter (95% non-missing) or check the internal log.

Coherence note for D3 (the questions, not a reviewer verdict on the paper). The conclusions otherwise stay within what the tests license: the overnight gap exceeds the total close-to-close effect, so "entirely an overnight gap" is arithmetically right; tradability is correctly stated as benchmark-sensitive; and the manuscript separates the four nested tests into two effective tests. The remaining D3 concerns are W3 and W6.

## Arithmetic Receipts

### AR1

procedure_id: p_from_test_statistic
evidence_anchor: text: §4.7 "the largest event p-value is 6.1e-05"
reported_inputs: t = 4.01 (Table 3, ceiling t+1..t+5, date-clustered, 446 dates, 3,187 events, smallest absolute t among the four event tests); largest event p-value 6.1e-05; no df stated; no tail stated
assumptions: none beyond the paper; the test family is taken from the column label t (date-clustered); df, reference distribution and tail are not licensed by the paper
derivation: A p-value requires a df for a t statistic; none is reported, and the paper does not say whether a normal or a t reference was used, so no p was derived
derived_value_or_range: none
comparison_rule: not applied because a required input is missing
status: not_computable
not_computable_reason: missing_reported_value
tail_convention: unstated

### AR2

procedure_id: p_from_test_statistic
evidence_anchor: text: §4.2 "adjusted p-values between 2.6e-06 and 4.0e-04"
reported_inputs: Benjamini-Hochberg adjusted p-values between 2.6e-06 and 4.0e-04 for the four event tests among 26 tests; the 22 characteristic p-values are not reported in the paper
assumptions: none beyond the paper; the unadjusted p-values of all 26 tests and their ranks are not given
derivation: A BH-adjusted p-value depends on the full ordered set of 26 raw p-values, of which the paper reports only the largest event value, so the adjustment cannot be reproduced from the reported values
derived_value_or_range: none
comparison_rule: not applied because the adjustment procedure inputs are incomplete
status: not_computable
not_computable_reason: nonstandard_p_procedure
tail_convention: unstated
