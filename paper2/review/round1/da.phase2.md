contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "an unverifiable methodological label"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

**Steel-man first.** The paper is candid about most of its weak points. It labels the decomposition, the comparison groups and the robustness work as post hoc, lists the specification-versus-implementation deviations, reports a null family of 22 characteristics together with a power table, and concedes that its own near-limit and benchmark results are heterogeneous. The central empirical regularity is large and survives every definition and benchmark tried: after a ceiling close the abnormal return is concentrated in the overnight gap, and an outside buyer at the next open has no positive abnormal return. With date-clustered t-statistics between 10 and 20 for the gap, this finding does not depend on luck, and the Benjamini-Hochberg arithmetic in the text is internally consistent (a largest event p-value of 6.1e-05 gives an adjusted 4.0e-04 over 26 tests). The attack below therefore targets what the paper infers from that regularity and how it labels its own evidence, not the existence of the gap.

**Strongest counter-argument.** A rival reader would say the paper has documented an ordinary information-and-attention continuation and attached a regulatory story to it. A stock that closes at its ceiling is, by construction, the stock with the strongest same-day net buying, the freshest news and the most retail attention. Its next opening is high because that information and attention persist overnight, and the intraday giveback is the familiar overnight-gain-then-reversal signature that the authors themselves cite from U.S. data (Berkman et al., 2012), where no price limit exists. The data cannot separate "the limit delayed discovery" from "the same pressure would have produced a gap without a limit", because there is a single 7% band, no market or period without it, no variation in band width, and no order-book data. The decisive comparison, ceiling closers against stocks that moved 5 to 6.5%, differs in more than the limit: the event rule requires the close to equal the day's high while the comparison groups carry no such condition, and the near-hit rows of Table 7 (not at the limit, yet a gap of 1.67%, t = 6.4) show that a large gap appears without a limit hit. The "discontinuity" and "attached to the limit itself" language is then stronger than an association supports, and the paper's own caveat in Section 4.4 says as much.

**Evidence status of the label "pre-specified".** The family was fixed in an internal time-stamped log that no outside party can inspect, after earlier manuscripts on related data had been completed and after this idea was selected from 14 candidates following two null projects. The body states this plainly (Section 3.1, Section 4.7). The abstract still speaks of a "hold-out half-sample", which Limitation (viii) retracts ("not a strict hold-out"), and the Vietnamese abstract says the hypotheses were registered in advance, which Section 3.1 denies. The contrast "0 of 22 survive, 4 of 4 survive" is presented as a pre-registered result when its status is author-attested.

**Headline-number traceability.** The ceiling next-day figures trace to Table 3 (1.66%, date-clustered t = 4.91) and Table 4 (two-way t = 4.8 to 9.8). The abstract's -0.75% (t = -2.7) tradable five-day shortfall against the market appears in Section 4.6 text and in no table, so its clustering scheme cannot be checked from the tables. The controls-based -0.53% has t = -1.8 and is nevertheless reported as a loss in the abstract; Table 5 shows ceiling versus 5 to 6.5% risers at -0.02 (t = -0.1) from the next open to the fifth close, so "no profit" is supported but "loses" is stronger than the evidence at the stated benchmark.

**Institutional premises.** The 7% band is "understood to be" the rule from "public exchange guides" and is checked only through the return pile-up in Table 1, which leaves 115 stock-days beyond 7.1% unexplained; tick sizes and the reference-price rule behind the exact-limit results are assumed (Limitation iii); the vendor does not document corporate-action adjustment. The paper does not discuss how the opening price is formed or any settlement constraint, although its mechanism rests on the next open absorbing queued orders. The only Vietnamese comparator for the close-to-close effect is a non-peer-reviewed GitHub analysis with overlapping data, and the reference check relied on web search because the DOI resolver and Crossref were unavailable (Appendix C).

**Other points worth noting, below the table threshold.** The Introduction says the family-wide frame "answers the objection" of a large effect found after a long search, yet Section 4.7 concedes a winner's-curse bias across three manuscripts and 14 candidate ideas, and the Bonferroni bound addresses existence rather than effect size. The floor effect is benchmark-sensitive (-0.69% against the market, -1.65% against controls), and for the lowest liquidity tercile it is not distinguishable from zero in close-to-close terms (0.06%, t = 0.2). The regulator implication ("the limit does not settle the price") is stated without any measurement of the benefits the limit is meant to deliver.

**Severity calibration.** I find no singleton rejection-level defect. The central gap result is large, robust and traceable, and the weaknesses concern the mechanism claimed, the evidential status of the label, and the fragility of one headline test. The field-norm gate does not apply: none of the rows below rests on a claim about what the field should do.

#### CRITICAL

| # | Dimension | Issue Description | Evidence Anchor | Confidence |
|---|-----------|-------------------|-----------------|------------|

#### MAJOR

| # | Dimension | Issue Description | Evidence Anchor | Confidence |
|---|-----------|-------------------|-----------------|------------|
| M1 | D3 argumentative_coherence | The pre-specified status that structures the whole contrast (22 null, 4 of 4 significant) rests on an internal, non-independent, author-attested log, and the Vietnamese abstract describes the hypotheses as registered in advance, contradicting Section 3.1 which says there is no external registry entry. | text: Vietnamese abstract (Tóm tắt) "một họ 26 giả thuyết đã đăng ký trước" | 4 (direct textual contradiction; registry practice is within competence) |
| M2 | D3 argumentative_coherence | The headline contrast between limit closes and 5 to 6.5% moves is confounded: the event rule requires the close to equal the day's high but the comparison groups are not described as meeting that condition, so a strong-close effect is not separated from a limit effect. | absence: Table 5 and Section 4.4 comparison design — expected comparison groups matched on closing at the day's high; checked Table 5 caption, Section 3.2 item (d), Section 4.4 text, Table 7 near-hit rows | 3 (inferred from what the text does not state; code not visible) |
| M3 | D3 argumentative_coherence | The inference from a gap after limit closes to delayed price discovery attributable to the limit is not separated from continuation of news, order imbalance and retail attention, as the paper itself concedes; there is a single band and no counterfactual market or period. | text: Section 4.4 "stocks that reach the limit may differ in news content" | 4 (design limitation is explicit in the text) |
| M4 | D3 argumentative_coherence | The claim that all four limit tests survive depends, at the floor five-day horizon, on a confirmation-half t-statistic barely above the 1.96 cut-off under date clustering that Limitation (vii) says may understate dependence; episode-level dependence could flip survival for that test. | table: Table 3, row floor t+1..t+5, column t (second half) = -2.16 | 4 (arithmetic read directly from the table) |
| M5 | D3 argumentative_coherence | The mechanism that the next opening absorbs what the limit blocked fits ceilings, but after floor closes prices keep falling from the next open through day 5, a pattern the single-mechanism narrative and the conclusion do not address. | table: Table 5, row floor vs 5-6.5% down, outcome Next open to day-5 close, difference -1.01 pp (t = -2.6) | 4 (read directly from the table) |
