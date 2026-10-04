# Editorial Decision Package

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Run disclosures: `criteria_binding_unavailable` (no target venue chosen; no venue-alignment claim is made; panel framed as a generic Q1/Q2 finance journal). No cross-model decision check was run (`ARS_CROSS_MODEL` not configured). No review-panel-provenance artifact was supplied to this synthesizer, so no independence claim is made about the five seats; all six provenance axes are `unknown`. The synthesizer adds no review comments of its own; every roadmap item below traces to a card finding.

## Mechanical audit (v3.6.2 Sprint Contract Synthesizer Protocol, contract `reviewer/reviewer_full/v2`)

Scoring matrix (assessed eligible seats only; `not_assessed` excluded from numerator and denominator):

| Dim | Priority | Eligible seats assessed | Scores | Verdict |
|---|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology | warn | warn |
| D2 domain_accuracy | mandatory | domain | warn | warn |
| D3 argumentative_coherence | mandatory | da, methodology | warn, warn | warn |
| D4 cross_disciplinary_relevance | high | perspective | warn | warn |
| D5 writing_and_structure | normal | eic | warn | warn |
| D6 venue_fit_and_contribution | mandatory | eic | warn | warn |

No seat declared a block or a fatal block. F1 (any mandatory fatal) and F2 (any mandatory block) do not fire. F3 (two or more mandatory dimensions at warn or worse, quantifier majority) fires: four mandatory dimensions (D1, D2, D3, D6) are warn, and the majority threshold is met in each (D3: both eligible seats). F4 (any high-priority block) does not fire. F5 (any dimension warn or worse) fires. F0 does not fire. Highest severity among fired conditions: F3 (70) over F5 (40), action `editorial_decision=major_revision`.

dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

The Devil's Advocate card has an empty CRITICAL table, so there are no DA CRITICAL IDs to adjudicate and the DA line is empty. The mechanical decision is not `accept`, so no DA-versus-accept marker applies. The DA's five MAJOR rows (M1 to M5) are tracked below; they are visible in the roadmap and are not counted in the consensus denominator.

---

## Part 1: Editorial Decision Letter

Dear Author(s),

Thank you for submitting your manuscript, "Closing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange" (about 5,000 words, 6 tables, 3 figures), for review. It was reviewed by five role-separated seats: a Journal-Fit Reviewer (EIC), three Peer Reviewers (Methodology, Domain, Perspective) and a Devil's Advocate. The panel is configured for a generic Q1/Q2 finance journal because no venue has been chosen.

### Decision: Major Revision

### Consensus Analysis

Consensus is counted per sub-claim over the four non-DA seats (denominator always 4). A seat that did not speak to a sub-claim is `not-mentioned` and is neither agreement nor opposition. Severity and confidence are transported from the cards.

#### Points of Agreement (Consensus)

No sub-claim reached [CONSENSUS-4] without a severity dispute. The agreed positions are:

- [CONSENSUS-3] **The "pre-specified" status cannot be verified externally and carries the weight of the headline contrast (SC-1).** Raised by the Journal-Fit Reviewer (W1), Methodology (W2) and Perspective (W1); the Domain seat is silent on this sub-claim as a verifiability point (it addresses wording only, SC-3). The Devil's Advocate corroborates (M1). Transported severity: Major (all three).
- **Severity SPLITs.** The wording, mechanism, policy, institutional and reproducibility items below were each raised by three or four seats but with different severities. Under the disposition precedence they are SPLITs, arbitrated below.
- Corroborated findings (two seats, no conflict): abstract states "0 of 22 survive" without the power qualifier the body supplies (SC-14: Methodology W6, Journal-Fit W3); declarations are unfinished and verification is still stated as pending (SC-15: Journal-Fit W5, Perspective W2); reference status and verification are uneven and the GitHub source needs a durable citation (SC-18: Domain W7, Journal-Fit W5).
- All seats note, as strengths, the candid separation of pre-specified and post hoc analyses, the bounded novelty claim against the public GitHub analysis, and the tabulated Appendix A. These strengths are not in dispute.

#### Points of Disagreement (SPLITs and arbitration)

Every SPLIT here is a severity disagreement with a compatible remedy. No seat argues that any of these is not a real problem. None of the SPLITs changes the mechanical decision, which is already fixed by F3.

- **Wording of "pre-specified", "registered" and "hold-out" in the abstracts (SC-3).** Journal-Fit (W1, W6), Methodology (W2) and Perspective (W1) rate it Major or Minor within their parents; Domain (W8) rates the terminology Minor. The Vietnamese abstract's "đã đăng ký trước" contradicts Section 3.1 (Journal-Fit W6, DA M1).
  - **Editor's Resolution:** Treat as one required item, folded into the SC-1 reframing (REV-1). Rationale: the remedy is identical across seats, the cost is sentence-level, and the textual contradiction between the Vietnamese abstract and Section 3.1 is directly observable (Confidence 3 to 5 across seats). Severity carried: Major from the driving finding (Methodology W2).
- **Mechanism: news selection and delayed price discovery not separated from unfilled demand (SC-5).** Methodology (W3) and Domain (W1) rate it Major; Perspective (W4) rates it Minor and proposes a cheaper partial check (an attention or lottery-proxy split). DA M3 corroborates at MAJOR.
  - **Editor's Resolution:** Major. Rationale (evidence first, expertise first): the Domain seat's microstructure argument (limit-hit stocks are selected on information arrival) and the paper's own Section 4.4 caveat both support it, and it bears directly on the abstract's mechanism wording. Perspective's remedy is compatible and is adopted as one of the acceptable analyses. A rewording fallback ("consistent with" in place of mechanism language) is allowed only if the analyses cannot be done.
- **Regulatory and investor implications go beyond the evidence (SC-8).** Perspective (W3) and Methodology (W3, within a Major parent) rate it Major; Journal-Fit (W4) and Domain (W6) rate it Minor.
  - **Editor's Resolution:** Required, sentence-level rewording, not new analysis. Rationale: four seats, plus the paper's own statement that it makes no causal claim, agree the Section 5 wording overreaches; the disagreement is only about weight. Severity carried: Major (Perspective W3, the driving finding), with the Minor ratings recorded.
- **HOSE institutional facts assumed, not sourced (SC-9).** Domain (W2) rates it Major; Perspective (W5) and Journal-Fit (W4, partial) rate it Minor.
  - **Editor's Resolution:** Major. Rationale (expertise first): the Domain seat identifies the assumptions as load-bearing for the exact tick-rule event definition and sourced the 7% band and tick table independently; the fix is cheap. Severity carried: Major (Domain W2).
- **Internal logs, code and data not available to readers (SC-16).** Perspective (W2) rates it Major; Journal-Fit (W5) and Methodology (W9) rate it Minor.
  - **Editor's Resolution:** Required as a single reproducibility-package item (REV-12). Rationale: the pre-specification credibility problem (SC-1) depends on the same deposit, and the cost is archival, not analytical. Severity carried: Major (Perspective W2).

No other disagreement exists. In particular, the Journal-Fit Reviewer's praise of the AI-use declaration's specificity does not contradict Perspective's request for model version and human-check detail (SC-17); the two are compatible and Journal-Fit is recorded as silent on that sub-claim.

### Decision Rationale

Every seat that assessed a dimension (all four mandatory dimensions, the high-priority dimension and the normal-priority dimension) scores warn; none scores block and none declares a fatal defect. The Devil's Advocate finds no CRITICAL issue and states that no singleton rejection-level defect exists. Methodology independently re-checked the headline numbers against saved tables and code and found them internally consistent, and the central descriptive result (a large overnight gap after ceiling closes, not capturable by an outside buyer at the next open) is supported across definitions and clustering choices. Reject is therefore not warranted.

Accept or Minor Revision is also not warranted. The contract's F3 condition fires because the methodology, domain, argument and venue-fit dimensions are each at warn, and the cards identify several Major issues that require new analysis, not rewording. First, the pre-specified label cannot be verified externally and anchors both the abstract and the contrast between 22 null and 4 surviving tests, while the new content is post hoc. Second, the survival of the nested t+1..t+5 tests rests on date-only clustering with overlapping windows, and the floor test clears the cut-off narrowly. Third, the mechanism and policy readings are not separated from news selection and are stated more strongly than an association supports. Fourth, core HOSE rules are assumed, and a platform migration inside the sample is not mentioned. Fifth, the incremental contribution over Berkman et al. (2012) and the public analysis is modest and the literature base is thin.

Both the existence of the gap and the paper's candour are strengths worth preserving. The revision should re-establish what the paper confirms, what it explores, and what it can say about mechanism, and should be re-reviewed. The panel did not resolve whether the revised contribution will reach a leading field-journal bar; that depends on the outcome of the new analyses.

### Blocking Issues (0-3, immutable source order)

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | The "pre-specified" label is unverifiable, leads the abstract, and covers the least novel result | EIC, R1, R3 (DA M1) | text: Section 3.1 "it is not an external registry entry" | REV-1 |
| R2 | Inference for the nested t+1..t+5 tests ("4 of 4 survive") rests on date-only clustering with overlapping windows | R1 (DA M4) | table: Table 3, row ceiling t+1..t+5 (t 4.01, first half 1.78, second half 6.82) and row floor t+1..t+5 (second half -2.16) | REV-3 |
| R3 | Mechanism ("unfilled demand", "discontinuity") is not separated from news selection and overreaches an association | R1, R2, R3 (DA M3) | text: Section 4.4 "stocks that reach the limit may differ in news content" | REV-4 |

---

## Part 2: Revision Roadmap

> Items are in immutable source order (by first sub-claim). `R<n>` and `S<n>` are transport references, not ranks. `Needs` states whether the item needs new analysis or rewording. This roadmap is a reviewer-owned core only; author triage is collected later in a separate sidecar.

### Sub-claim inventory (Step 1b)

| sub_claim_id | parent weakness | EIC | R1 | R2 | R3 | DA | Disposition |
|---|---|---|---|---|---|---|---|
| SC-1 | Pre-specified label unverifiable externally | raised (W1) | raised (W2) | not-mentioned | raised (W1) | M1 | CONSENSUS-3 (R2 silent) |
| SC-2 | Originally specified t+2..t+5 horizon not reported next to implemented t+1..t+5 | not-mentioned | raised (W2) | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-3 | Abstract wording ("pre-specified", Vietnamese "registered", "hold-out") | raised (W1, W6) | raised (W2) | disputed on severity (W8, Minor) | raised (W1) | M1 | SPLIT (arbitrated) |
| SC-4 | t+1..t+5 inference, date-only clustering, floor test narrow | not-mentioned | raised (W1) | not-mentioned | not-mentioned | M4 | single-reviewer |
| SC-5 | Mechanism not separated from news selection and attention | not-mentioned | raised (W3) | raised (W1) | disputed on severity (W4, Minor) | M3 | SPLIT (arbitrated) |
| SC-6 | Comparison is not a formal discontinuity design; no strong-close or covariate matching | not-mentioned | raised (W3) | not-mentioned | not-mentioned | M2 | single-reviewer |
| SC-7 | Floor-side drift after next open not addressed by the single mechanism | not-mentioned | not-mentioned | not-mentioned | not-mentioned | M5 | DA-only (tracked outside consensus) |
| SC-8 | Regulatory and investor implications exceed evidence | disputed on severity (W4, Minor) | raised (W3) | disputed on severity (W6, Minor) | raised (W3) | not-mentioned | SPLIT (arbitrated) |
| SC-9 | HOSE institutional facts assumed, not sourced | disputed on severity (W4, Minor) | not-mentioned | raised (W2) | disputed on severity (W5, Minor) | not-mentioned | SPLIT (arbitrated) |
| SC-10 | KRX platform migration (5 May 2025) omitted; "single regime" inaccurate | not-mentioned | not-mentioned | raised (W3) | not-mentioned | not-mentioned | single-reviewer |
| SC-11 | Literature coverage thin (price-limit theory, A-share, Vietnam) | not-mentioned | not-mentioned | raised (W4) | not-mentioned | not-mentioned | single-reviewer |
| SC-12 | Incremental contribution modest over Berkman et al. (2012) and public analysis | raised (W2) | not-mentioned | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-13 | Characteristic null and limit finding read as two papers | raised (W3) | not-mentioned | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-14 | Abstract "0 of 22" lacks power qualifier | raised (W3, power note) | raised (W6) | not-mentioned | not-mentioned | not-mentioned | corroborated (2) |
| SC-15 | Declarations placeholders; verification stated as pending | raised (W5) | not-mentioned | not-mentioned | raised (W2) | not-mentioned | corroborated (2) |
| SC-16 | Internal logs, code, raw data and retrieval manifest not available to readers | raised (W5, Minor) | raised (W9, Minor) | not-mentioned | disputed on severity (W2, Major) | not-mentioned | SPLIT (arbitrated) |
| SC-17 | AI-use disclosure lacks model version and human-check detail | not-mentioned | not-mentioned | not-mentioned | raised (W2) | not-mentioned | single-reviewer |
| SC-18 | Reference status and verification uneven; GitHub source needs durable citation | raised (W5) | not-mentioned | raised (W7) | not-mentioned | not-mentioned | corroborated (2) |
| SC-19 | Executability of the next open and wording of tradable shortfall | not-mentioned | not-mentioned | raised (W5) | not-mentioned | traceability note | single-reviewer |
| SC-20 | Headline -0.75% (t = -2.7) has no table | not-mentioned | raised (W8) | not-mentioned | not-mentioned | traceability note | single-reviewer |
| SC-21 | Floor magnitude depends on unadjusted dollar-volume benchmark | not-mentioned | raised (W5) | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-22 | Event p-values use a normal reference; Bonferroni 816 sensitive | not-mentioned | raised (W4) | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-23 | Outliers beyond the band and snapshot universe not bounded | not-mentioned | raised (W7) | not-mentioned | not-mentioned | not-mentioned | single-reviewer |
| SC-24 | Presentation: duplicated table captions; long abstract with eleven numbers | raised (unscored note) | not-mentioned | not-mentioned | not-mentioned | not-mentioned | single-reviewer |

Severity and confidence are transported per row below. No card lacked per-finding severity or confidence tags, so no `[SEVERITY-SOURCE]` or `[CONFIDENCE-SOURCE]` fallback tags apply. The Domain card tags its severity per finding and gives a norm basis for W2; the Perspective card omits per-finding confidence on W4 and W5, which are single-line Minor items.

### Required Revisions (Must Fix)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 (REV-1) | Reframe the confirmatory status. State in abstract, introduction and conclusion that the family was "specified in an internal log before computation", not registered. Say which finding is confirmatory, which exploratory, and which the contribution rests on. Deposit the log and code at the specification commit with a hash or third-party time-stamp, flagged as retrospective. Remove the English/Vietnamese contradiction ("đã đăng ký trước") and the abstract's "hold-out" wording. Report the originally specified t+2..t+5 test beside the implemented t+1..t+5. | SC-1, SC-2, SC-3 | Major (EIC W1, R1 W2, R3 W1) | text: Section 3.1 "it is not an external registry entry" | 4 (EIC W1, R1 W2, R3 W1) | EIC, R1, R3 (DA M1) | must_fix | section (abstract, Sections 1, 3.1, 5, Vietnamese abstract) plus re_analysis (t+2..t+5 re-run) | claim_scope_change: confirmatory label |
| R2 (REV-3) | Re-evaluate survival of the t+1..t+5 tests for ceiling and floor with dependence-robust inference: calendar-week block bootstrap or Driscoll-Kraay (or calendar-time portfolio), alongside the date-clustered figures. Re-apply the stated survival rule and revise "4 of 4 survive" if any test fails. | SC-4 | Major (R1 W1) | table: Table 3, row ceiling t+1..t+5 (t 4.01, first half 1.78, second half 6.82) and row floor t+1..t+5 (second half -2.16) | 4 (R1 W1; DA M4 corroborates) | R1 (DA M4) | must_fix | re_analysis (Table 3, Section 4.2) | claim_scope_change: survival statement |
| R3 (REV-4) | Separate the unfilled-demand reading from news selection and attention, or downgrade it. Acceptable analyses: split the gap by same-day or next-morning announcement; test an attention or lottery proxy already in the family (MAX, LIMITFREQ); a news-free placebo of equal-size gainers; a comparison group conditioned on closing at the day's high; and a statement of binned-comparison limits (bandwidth, balance). If not done, reword mechanism and "discontinuity" language to "consistent with", in abstract and headings. | SC-5, SC-6 | Major (R1 W3, R2 W1); Minor (R3 W4) | text: Section 4.4 "stocks that reach the limit may differ in news content" | 4 (R1 W3, R2 W1) | R1, R2, R3 (DA M2, M3) | must_fix | re_analysis (new splits and controls) with rewording fallback | claim_scope_change: mechanism wording |
| R4 (REV-6) | Recast the Section 5 regulatory and investor implications as hypotheses conditional on this market and window, name the data that would test them (order-level, investor-type, auction-rule variation), and state that no welfare or investor-protection conclusion is drawn. Remove "the limit does not settle the price" as a finding. | SC-8 | Major (R3 W3); Minor (EIC W4, R2 W6) | text: Section 5 "For investors, it argues against chasing limit-up stocks at the open" | 4 (R3 W3, R2 W6) | R3, R1, EIC, R2 | must_fix | section (Section 5, Section 4.6 wording) | claim_scope_change: implications |
| R5 (REV-7) | Source the HOSE rules from exchange documents: the +/-7% band, tick table, reference-price rule including corporate-action days, first-day and resumed-trading bands, auction rules, short-sale and settlement rules. Check whether any events fall under special bands (the 0.064% of stock-days beyond +/-7.1%). Rebuild the exact tick-rule count only if the sourced rules differ. | SC-9 | Major (R2 W2); Minor (R3 W5, EIC W4) | text: Section 2 "(public exchange guides; we treat this as an assumption and check it against the data)" | 4 (R2 W2) | R2, R3, EIC | must_fix | section plus small re_analysis (band and event audit) | none: factual sourcing |
| R6 (REV-8) | State the platform history and the 5 May 2025 migration to the KRX system with the auction-priority change (source to the exchange circular, not press), split the gap and giveback at the migration date, and replace "single market regime". | SC-10 | Major (R2 W3) | text: Section 6 (x) "The sample is a single market regime on one exchange." | 3 (R2 W3; date sourced to press reports) | R2 | must_fix | re_analysis (pre/post split) plus sentence | none |
| R7 (REV-9) | Broaden the literature search (price-limit theory, Chinese A-share price-limit studies, Vietnamese band studies, overnight-return work beyond Berkman et al. 2012) and rewrite the novelty paragraph as a short critical synthesis within the search bound. The panel's search leads are unverified and must be located and verified by the authors, not cited from the cards. | SC-11 | Major (R2 W4) | absence: Section 1 and References, expected price-limit theory beyond Brennan (1986), A-share studies, fuller Vietnamese literature | 3 (R2 W4) | R2 | must_fix | section (Section 1, References) | none |
| R8 (REV-10) | State why applying the overnight-then-giveback signature to a limit adds knowledge beyond Berkman et al. (2012) and the public analysis (for example, a prediction the limit mechanism makes and the U.S. mechanism does not), or position the paper as a focused market-structure note. | SC-12 | Major (EIC W2) | text: Abstract "our contributions are the overnight-intraday decomposition, the comparison with moves just below the limit, and the multiple-testing frame" | 3 (EIC W2) | EIC | must_fix | section (abstract, Sections 1 and 5) | claim_scope_change: contribution statement |
| R9 (REV-11) | Either motivate the 22-characteristic family as an explicit multiplicity device for the limit result and shorten it, or separate the two messages; state the link between them. | SC-13 | Major (EIC W3) | text: Section 5 "The limit result stands out because every other characteristic in the same family is null." | 3 (EIC W3) | EIC | must_fix | section (structure of Sections 1, 4.1, 5) | none |
| R10 (REV-13) | Complete the reproducibility and disclosure package: finish the ethics, funding, competing-interest and author-contribution declarations; deposit code, derived tables, the specification log and cited process logs in a public archive with a DOI or hash; report the vnstock version, retrieval date and price-adjustment status; extend the AI-use disclosure with model and version, tasks delegated and human checks performed; replace the "responsible for verifying before submission" wording with a completed-verification statement. | SC-15, SC-16, SC-17 | Major (R3 W2); Minor (EIC W5, R1 W9) | text: Declarations "the authors are responsible for verifying all choices, results and references before submission" | 4 (R3 W2); 5 (EIC W5) | R3, EIC, R1 | must_fix | other (archive deposit) plus section (Declarations, Data and code availability) | none |

### Suggested Revisions (Should Fix)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 (REV-5) | Address in the text why prices keep falling from the next open to day 5 after floor closes when the single mechanism explains ceilings; report or discuss the asymmetry. | SC-7 | MAJOR (DA M5) | table: Table 5, row floor vs 5-6.5% down, outcome Next open to day-5 close, difference -1.01 pp (t = -2.6) | 4 (DA M5) | DA | should_fix | section (Section 4.4 and 5) | none |
| S2 (REV-12) | Add a clause to the abstract and conclusion stating the detectable-effect scale (0.12 to 0.31 percentage points per week) beside "0 of 22 survive". | SC-14 | Minor (R1 W6) | text: Abstract "0 of the 22 characteristics survive" | 4 (R1 W6) | R1, EIC | should_fix | sentence (abstract, conclusion) | none |
| S3 (REV-14) | Verify Le (2012), Chen (1993) and Berkman and Lee (2002) descriptions against originals; label Veeraraghavan et al. (2007) as a working paper in the text; cite the GitHub analysis durably (archive or DOI); complete DOI or equivalent checks per the project integrity gate. | SC-18 | Minor (R2 W7, EIC W5) | text: Appendix C "All references were verified against records returned by web search" | 3 (R2 W7) | R2, EIC | should_fix | section (References, Appendix C) | none |
| S4 (REV-15) | State that the tradable return is measured at the quoted open, not at achievable fills; report how often a ceiling stock is buyable at the open (522 locked days noted); keep "no profit" language at the market-benchmark and controls-benchmark evidence level. | SC-19 | Minor (R2 W5) | text: Section 4.6 "A stock that closes at its ceiling typically cannot be bought at that close" | 3 (R2 W5) | R2 | should_fix | sentence plus small re_analysis | none |
| S5 (REV-16) | Add a table for the -0.75% (t = -2.7) next-open-to-day-5 result with its clustering scheme; reconcile exact-tick ceiling counts across Tables 4, 7 and the saved universe table. | SC-20 | Minor (R1 W8) | absence: Abstract and Section 4.6, expected a table reporting the -0.75% (t = -2.7) return against the market; checked Tables 3 to 8 and Appendix A | 4 (R1 W8) | R1 (DA traceability note) | should_fix | section (new table) | none |
| S6 (REV-17) | Add a beta- and size-matched control or market-model abnormal return for the floor effect, or flag in the abstract that the -0.71% floor figure depends on the unadjusted benchmark. | SC-21 | Minor (R1 W5) | table: Table 6, row Floor all, columns Close-to-close vs market (-0.69) and Close-to-close vs controls (-1.65) | 4 (R1 W5) | R1 | should_fix | re_analysis (or sentence if flagged only) | none |
| S7 (REV-18) | State the reference distribution and degrees of freedom for the date-clustered statistics; recompute event p-values and the Bonferroni program size (816) under a t reference, or justify the normal reference. | SC-22 | Minor (R1 W4) | text: Section 4.7 "all four event tests would still survive a Bonferroni correction at 5% for a project-wide family of up to 816 tests" | 4 (R1 W4) | R1 | should_fix | re_analysis (recompute p-values) | none |
| S8 (REV-19) | Bound the effect of returns beyond +/-8% (96 stock-days) and of the post-sample listing snapshot, by dropping those stock-days and events within five days and re-estimating. | SC-23 | Minor (R1 W7) | table: Table 1, rows below -8.0% (38 stock-days) and above 8.0% (58 stock-days) | 3 (R1 W7) | R1 | should_fix | re_analysis (robustness) | none |
| S9 (REV-20) | Remove the duplicate table captions (above and below each table) and shorten the abstract so one message leads. | SC-24 | Minor (unscored EIC note) | text: EIC card "Further presentation points, not scored as findings" | 3 (EIC note) | EIC | consider | sentence | none |

### Source-Traceability Checklist

- [ ] R1 (REV-1) - obligation `must_fix`: reframe confirmatory status; deposit time-stamped log; report t+2..t+5; fix abstract contradictions
- [ ] R2 (REV-3) - obligation `must_fix`: dependence-robust inference for t+1..t+5; re-apply survival rule
- [ ] R3 (REV-4) - obligation `must_fix`: separate mechanism from news selection or reword; comparison-group design
- [ ] S1 (REV-5) - obligation `should_fix`: floor-side drift versus single-mechanism narrative
- [ ] R4 (REV-6) - obligation `must_fix`: recast regulatory and investor implications
- [ ] R5 (REV-7) - obligation `must_fix`: source HOSE rules; special-band audit
- [ ] R6 (REV-8) - obligation `must_fix`: KRX migration and pre/post split
- [ ] R7 (REV-9) - obligation `must_fix`: broaden and verify literature; rewrite novelty paragraph
- [ ] R8 (REV-10) - obligation `must_fix`: state incremental contribution over Berkman et al. and public analysis
- [ ] R9 (REV-11) - obligation `must_fix`: resolve the zoo-versus-limit structure
- [ ] S2 (REV-12) - obligation `should_fix`: power qualifier beside "0 of 22"
- [ ] R10 (REV-13) - obligation `must_fix`: declarations, deposit, vendor and AI-use disclosure
- [ ] S3 (REV-14) - obligation `should_fix`: reference verification and status labels
- [ ] S4 (REV-15) - obligation `should_fix`: executability at the open
- [ ] S5 (REV-16) - obligation `should_fix`: tabulate -0.75% result; reconcile counts
- [ ] S6 (REV-17) - obligation `should_fix`: floor benchmark sensitivity
- [ ] S7 (REV-18) - obligation `should_fix`: reference distribution for p-values
- [ ] S8 (REV-19) - obligation `should_fix`: outlier and snapshot bounds
- [ ] S9 (REV-20) - obligation `consider`: presentation fixes

### Needs new analysis versus rewording

- New analysis: REV-1 (t+2..t+5 re-run), REV-3, REV-4 (with rewording fallback), REV-7 (event audit, small), REV-8, REV-16, REV-17, REV-18, REV-19.
- Rewording or sourcing only: REV-1 (labels), REV-5, REV-6, REV-9, REV-10, REV-11, REV-12, REV-13 (archive and disclosure), REV-14, REV-15 (mostly), REV-20.

### Response Letter Template

Respond to every item above using `templates/revision_response_template.md`. A declined item must remain visible with its reason.

---

## Part 3: Reviewer Report Summary (Appendix)

### Journal-Fit Review Report Summary
- Recommendation: preliminary signal Major Revision (EIC does not decide); D5 warn, D6 warn | Confidence: per-finding 3 to 5
- Key Point: candid, bounded paper whose confirmatory label supports its least novel result, while the novel decomposition is post hoc and the contribution is modest.

### Reviewer 1 (Methodology) Summary
- Recommendation: D1 warn, D3 warn | Confidence: per-finding 3 to 4
- Key Point: numbers tie to saved outputs and the gap is robust; the "4 of 4 survive" statement, the "pre-specified" weight, and the mechanism wording need dependence-robust inference, disclosure and softening.

### Reviewer 2 (Domain) Summary
- Recommendation: D2 warn | Confidence: per-finding 3 to 4
- Key Point: empirical core is plausible, but HOSE rules are unsourced, the 2025 KRX migration is omitted, news-based rivals are not separated, and the literature is thin.

### Reviewer 3 (Perspective) Summary
- Recommendation: D4 warn | Confidence: per-finding 4 where stated
- Key Point: pre-specification is unverifiable, AI-use and evidence trail are too thin for replication, and regulatory and investor readings exceed the association.

### Devil's Advocate Summary
- Recommendation: N/A - findings only
- Key Challenge: No unresolved Critical challenge; five MAJOR rows (M1 to M5) track the unverifiable label, a confounded comparison group, unseparated news selection, a narrow floor five-day test, and the floor-side drift not covered by the mechanism.
