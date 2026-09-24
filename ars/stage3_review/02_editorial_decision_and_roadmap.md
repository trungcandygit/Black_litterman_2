# Editorial Decision

## Manuscript Information
- Title: Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification
- Version: manuscript_v2.md (SHA-256 1adeb804...63c), Stage 2.5 PASS
- Configured venue: Finance Research Open (`criteria_binding_unavailable`; no official-criteria alignment claimed)
- Review round: 1 (reviewer_full, contract reviewer/reviewer_full/v2)

## Review Panel Provenance
Artifact: review_panel_provenance.json (replay-validated PASS).
| Axis | Observed |
|---|---|
| role_separated | true |
| fresh_context | false (one session context) |
| blind_to_peer_outputs | false (seats written sequentially in one context) |
| model_family_distinct | false (claude-opus) |
| provider_distinct | false (anthropic) |
| human_distinct | false (no human reviewer) |
Correlated-error disclosure (required): all model-executed review seats used one model family; role separation does not remove correlated-error risk. The same context also drafted the manuscript, so Phase 1 plans were not manuscript-blind in fact.

## Decision
### Major Revision

Mechanical derivation (contract v2):
| Dim | Priority | Eligible assessed seats | Audit verdict |
|---|---|---|---|
| D1 methodology_rigor | mandatory | R1: block | block (not fatal) |
| D2 domain_accuracy | mandatory | R2: block | block (not fatal) |
| D3 argumentative_coherence | mandatory | DA: block; R1: warn | block (not fatal) |
| D4 cross_disciplinary_relevance | high | R3: warn | warn |
| D5 writing_and_structure | normal | EIC: pass | pass |
| D6 venue_fit_and_contribution | mandatory | EIC: warn | warn |
Fired: F2 (sev 90, mandatory block) -> major_revision; F3 (sev 70) -> major_revision; F5 (sev 40) -> minor_revision. F1 not fired (no fatal block declared by any seat). Precedence by severity: F2. Decision = Major Revision.

DA CRITICAL adjudication: DA-C1 (selection on post-announcement outcomes) is VALIDATED; R1-W1 corroborates it independently of wording and the manuscript's own Section 5.2 documents the mechanism for two stocks. It is carried as Blocking Issue B1. No Accept path exists in this round, so the DA gate does not escalate.

## Blocking Issues (source order)
- B1 Treated group defined with post-treatment information (R1-W1, DA-C1). Blocks D1 and D3.
- B2 Control group includes at least nine HOSE stocks named on FTSE's preliminary eligible list (R2-W1). Blocks D2.
- B3 CAR inference ignores common event dates, and the benchmark is size-mismatched (R1-W2, R1-W3, DA-M1). Blocks D1.

## Reviewer Summary
| Seat | Signal | Key point |
|---|---|---|
| EIC | Major | Timely, well written; contribution depends on identification |
| R1 | Major | ITT on pre-announcement list; clustered-event CAR inference; benchmark; pre-window; wild bootstrap |
| R2 | Major | Control contamination by named-eligible stocks; FTSE data cut-off dates; FOL/free float |
| R3 | Minor | Scope effective-date claim to 10% tranche; cost of capital not measured |
| DA | Major (CRITICAL) | Selection can reproduce the stage pattern; price claims fragile |

## Consensus Analysis
Agreement (R1, R2, DA, EIC): treatment/control assignment must rest on pre-announcement public lists. Agreement (R1, DA): Table 3 inference must be redone. Agreement (R3, DA): effective-date claims must be scoped to the first tranche.
Disagreement: R3 judged the paper Minor; R3's dimension (D4) does not own identification, so this does not alter the mechanical outcome.

## Decision Rationale
The paper is repairable with data the authors already hold plus public FTSE lists. None of the blocking issues is fatal: an intention-to-treat group screened on 31 December 2024 data exists; calendar-time CAR tests and alternative benchmarks are standard. If the constituent effects survive these repairs, the contribution stands; if they shrink, the paper must report the smaller effects.

## Required Revisions (Must Fix)
| ID | Item | Source | Anchor |
|---|---|---|---|
| RR1 | Add an intention-to-treat analysis using the 28-stock preliminary list (screened on 31 Dec 2024 data): baseline DiD, event study, CARs. Report beside constituent results. Also a "predicted constituent" group from pre-period ranks | R1-W1, DA-C1 | S 3.1, S 3.4, T2 |
| RR2 | Rebuild groups from all public lists (Nov 2025 = 28, Apr 2026 = 32, Aug 2026 = 27); remove named-but-excluded stocks from controls; re-run T2, T7, T8; extend naming-timing test to all named-excluded HOSE stocks; appendix table of names by list | R2-W1, EIC-W2 | S 3.1, S 5.2, T8 |
| RR3 | CAR inference with a calendar-time portfolio test (pre-event estimation window) and/or Kolari-Pynnönen adjustment | R1-W2, DA-M1 | S 3.2, T3 |
| RR4 | CAR benchmarks: matched-control mean, size-tercile benchmark, market model with pre-estimated betas | R1-W3, DA-M1 | S 3.2, T3 |
| RR5 | Scope effective-date and "prices already adjusted" claims to the first 10% tranche | R3-W1, DA-M2 | Abstract, S 4.3, S 6 |
| RR6 | Frame selection evidence around FTSE's screening cut-off dates (31 Dec 2024; 31 Dec 2025) | R2-W2 | S 5.2 |

## Suggested Revisions (Should Fix)
| ID | Item | Source |
|---|---|---|
| SR1 | Pre-window sensitivity excluding July to August 2025 | R1-W4 |
| SR2 | Wild cluster bootstrap for DiD and segment coefficients; caution on three-stock segments | R1-W5 |
| SR3 | Test level shifts at confirmation and list months against a trend, or soften H2 | R1-W6 |
| SR4 | Paragraph on free float and foreign ownership limits in FTSE investability weights | R2-W3 |
| SR5 | Present cost-of-capital as motivation, not finding; note investor-type data limitation | R3-W2, R3-W3 |
| SR6 | Scope "classification events redistribute liquidity" to this event; discuss pre-funding removal and sector composition as alternatives | DA-m1, DA ignored alternatives |
| SR7 | Verified addition on stock-level MSCI A-share inclusion liquidity studies | R2-W4 |
| SR8 | Check abstract length against venue limit | EIC-W3 |

## Revision Roadmap (immutable core; author triage recorded separately)
Source-ordered items: RR1, RR2, RR3, RR4, RR5, RR6, SR1 to SR8. Each maps to a reviewer finding above; no item originates in synthesis. Author triage per item (will_address / wont_address / not_on_point) is recorded in the author-adjudication sidecar at Stage 4 entry.

## Response Letter Instructions
Point-by-point R -> A -> C format (templates/revision_response_template.md): quote each item, answer with evidence, give the changed manuscript text.

## Closing (Major Revision)
The panel sees a publishable paper once the treatment and control groups rest on pre-announcement information and the price evidence is re-tested. The revised version returns for verification review (Stage 3').
