# Stage 3 REVIEW, Phase 0 and Phase 1 pre-commitment (academic-paper-reviewer v1.11.1, mode full, contract reviewer/reviewer_full/v2)

Manuscript: ars/stage2_write/manuscript_v2.md (SHA-256 1adeb80492a7007f9cbac68e2000894baeb79cbc900c1f9a581e9904076d163c at Stage 2.5 PASS; the review reads these bytes and does not edit them, per Iron Rule 6).
Criteria binding: `criteria_binding_unavailable` (no author-confirmed ReviewTargetContext; the panel makes no claim of official Finance Research Open criteria alignment).

## Phase 0: field analysis
- Primary discipline: empirical finance, market microstructure (liquidity, index effects).
- Secondary: international finance (market classification, benchmark-driven flows), emerging/frontier markets.
- Paradigm: quantitative, quasi-experimental (difference-in-differences, event study, CARs).
- Target venue: Finance Research Open (Elsevier, open access, broad empirical finance, short-to-medium articles).
- Maturity: complete draft, integrity-verified.

## Reviewer Configuration Cards
| Seat | Identity | Focus |
|---|---|---|
| EIC (Journal-Fit Reviewer) | Handling editor at a broad empirical-finance journal who handles index-effect and emerging-market papers | fit, contribution, presentation (D5, D6) |
| R1 Methodology | Econometrician in event studies and DiD with few treated clusters | identification, inference, event-study statistics (D1, D3) |
| R2 Domain | Researcher on index inclusion and market reclassification (MSCI/FTSE), familiar with Vietnam's market structure | literature, institutional accuracy, index mechanics (D2) |
| R3 Perspective | Policy economist at a securities regulator / development finance institution | practical and policy implications, adjacent-field accessibility (D4) |
| DA Devil's Advocate | fixed seat | strongest counter-argument, logic chain (D3) |

## Phase 1 pre-commitment (contract paraphrase + scoring plans)
Blindness disclosure: all seats executed in the same context that drafted the manuscript, so Phase 1 was not manuscript-blind in fact. The plans below are written against the contract text only and are frozen before the Phase 2 reports; provenance records `peer_outputs_visible: true` and `fresh_context: false`.

Contract paraphrase: D1 methodology rigor (mandatory, R1), D2 domain accuracy (mandatory, R2), D3 argumentative coherence (mandatory, DA owner, R1 eligible), D4 cross-disciplinary relevance (high, R3), D5 writing and structure (normal, EIC), D6 venue fit and contribution (mandatory, EIC). F1 fatal mandatory block -> reject; F2 mandatory block -> major; F3 two mandatory warns -> major; F4 high block -> major; F5 any warn -> minor; F0 all pass -> accept.

| Dim | Seat | what_to_look_for | block | warn | fatal |
|---|---|---|---|---|---|
| D1 | R1 | treatment defined on pre-period information; parallel-trend evidence; inference valid for 24 treated units and a common event date; benchmark suited to large caps | a headline estimate rests on an invalid test or on a treatment group defined with post-treatment outcomes, repairable with available data | a robustness gap that does not overturn a headline | the design cannot identify the estimand with any available data |
| D2 | R2 | index mechanics (eligibility screens, data cut-off dates, tranches), treatment/control assignment consistent with public lists, prior work represented correctly | control or treatment group misassigned relative to public FTSE lists, or index mechanics misdescribed in a way that changes estimates | missing institutional detail or literature that a specialist expects | the event studied is misidentified |
| D3 | DA, R1 | thesis follows from estimates; alternative explanations addressed; claims scoped to evidence | the central thesis has a live alternative explanation the paper cannot currently exclude | overreach in one or more secondary claims | thesis contradicted by the paper's own results |
| D4 | R3 | policy implications follow from evidence; accessible to non-specialists | policy claims contradict evidence | implications outrun evidence or omit key institutional context | n/a (high priority) |
| D5 | EIC | structure, tables, figure, conventions | unreadable tables or inconsistent terminology | fixable clarity issues | n/a |
| D6 | EIC | named gap, timeliness, significance for readership | no contribution beyond known results | contribution depends on unresolved identification | not finance / out of scope |

[PRE-COMMITMENT-ACKNOWLEDGED]
