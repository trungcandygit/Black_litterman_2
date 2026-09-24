# Phase 4b self-scoring, Phase 5a/5b, Phase 6a/6b evaluation (academic-paper full, contract-gated)

Artefact under review: `manuscript_v1.md` (revision round 1 of Phase 4b).

## Phase 4b: Writer self-scoring

## Dimension Scores

| Dim | Priority | Score | Evidence |
|---|---|---|---|
| D1 section_completeness | mandatory | pass | Sections 1 to 6, Appendix A1, Declarations, References present; no [MATERIAL GAP] marker in body; CRediT/funding placeholders are author inputs, flagged in Declarations |
| D2 citation_density | mandatory | pass | 23 references, 0 orphans in either direction (deterministic cross-check); every empirical number traced to an output file; FTSE timeline sourced to LSEG and press reports |
| D3 argument_blueprint_fidelity | mandatory | pass | C1 = §4.1, C2 = §4.1 + §5, C3 = §4.2, C4 = §4.3, C5 = §4.1 + §5; counter-argument = §3.4 + §5 |
| D4 total_word_count | high | block | Body 4,542 words vs target 7,000 (-35%); round 1 added only substantive content (segment analysis, identification assumptions, balance, spillovers); further growth would require padding, which the skill forbids |
| D5 per_section_word_count | high | warn | Sections 3 (986/1,300) and 4 (1,008+ vs 2,100 incl. new 4.4) under allocation; Section 5 582/900 |
| D6 paragraph_structure | normal | pass | Claim-first topic sentences; each results subsection ends with a Takeaway |
| D7 register_consistency | normal | pass | Mechanical gate: 0 em dashes in prose, 0 banned openers, passive voice under 3%, "significant" used only in the statistical sense, "robust" only in "cluster-robust" |

## Failure Condition Checks

| Condition | Triggered | Note |
|---|---|---|
| F1 mandatory block | no | |
| F4 mandatory warn | no | |
| F2 high-priority block | YES | D4 |
| F3 high-priority warn | YES | D5 |
| F0 all mandatory pass | yes | |

## Writer Decision

writer_decision = revise_in_phase_4b (F2). Round 1 revision applied (segment heterogeneity, identification assumptions, matching balance, spillover check, discussion). The remaining D4 gap reflects a target set at intake (7,000 words) that exceeds what the evidence needs; resolving it requires either an author decision to lower the target or new analyses, not padding. Escalated to the Stage 2 checkpoint as a configuration question.

## Phase 5a: Citation compliance (deterministic)

- In-text citations without reference entry: 0. Reference entries never cited: 0.
- All 20 scholarly references Crossref-verified (Stage 1 table plus Stereńczak et al. 2020 and Nguyen et al. 2021 verified in Stage 2). Correction: Stereńczak et al. print year 2020 (the prior paper listed 2019).
- 5 grey-literature sources (LSEG press releases 2025/2026; The Investor 2026; Viet Nam News 2025; VIR 2026): URLs retrieved during this run; content claims limited to dates and list sizes reported in those pages.

## Phase 5b: Abstract

English only (Phase 0 decision). 168 words, no citations, punchline in sentence 3, keywords 6 (none repeating the full title phrase).

## Phase 6a: Evaluator paper-blind pre-commitment (contract evaluator_full)

## Contract Paraphrase
D1 originality: the contribution statement must name a specific gap and the discussion must engage prior work substantively. D2 methodological rigor: the design must fit the question, be replicable, and disclose limits. D3 evidence sufficiency: every claim needs a citation or data; no cherry-picking. D4 argument coherence: thesis, results and conclusion align without contradiction. D5 writing quality: clear, consistent, venue-appropriate.

## Scoring Plan
### D1: originality
- dimension_id: D1; what_to_look_for: named gap (stock-level evidence on frontier-to-emerging reclassification; eligibility vs inclusion); what_triggers_block: no gap or gap restates known results; what_triggers_warn: gap bounded by a narrow search not disclosed.
### D2: methodological_rigor
- dimension_id: D2; what_to_look_for: pre-trend evidence, matched and size controls, inference with few treated clusters, limits stated; what_triggers_block: causal claims despite failed pre-trends without adjustment; what_triggers_warn: a key robustness result weakens a headline claim without acknowledgement.
### D3: evidence_sufficiency
- dimension_id: D3; what_to_look_for: every number maps to output; every factual claim cited; what_triggers_block: orphan numbers or unverifiable citations; what_triggers_warn: claim-source alignment uncertain for a cited source.
### D4: argument_coherence
- dimension_id: D4; what_to_look_for: title thesis = results = conclusion; what_triggers_block: contradiction between sections; what_triggers_warn: a result that complicates the thesis is not reconciled.
### D5: writing_quality
- dimension_id: D5; what_to_look_for: register, tables readable, consistent terminology; what_triggers_block: unreadable tables or inconsistent group names; what_triggers_warn: length far from venue norm.

criteria_binding_unavailable (no official venue criteria retrieved)

[PRE-COMMITMENT-ACKNOWLEDGED]

## Phase 6b: Evaluator paper-visible scoring

## Dimension Scores

| Dim | Score | Finding |
|---|---|---|
| D1 originality | pass | Gap stated in §1 and §2.3 with the search bound disclosed; eligibility vs inclusion separation is new relative to the cited literature |
| D2 methodological_rigor | warn | Headline Amihud result survives most checks, but the matched-sample-with-trend specification halves the announcement coefficient (p < 0.1); the paper reports this in §5 but the Introduction and Abstract still quote the unadjusted 32% announcement effect without that caveat. Near-miss group of 5 stocks; randomization inference addresses inference but not representativeness. Treatment definition of near-miss relies on press reports of FTSE lists rather than FTSE's own documents |
| D3 evidence_sufficiency | warn | Two claim-source alignments need Stage 2.5 checking: (a) "FTSE's eligibility screens rest on ... size, free float and foreign-ownership headroom (LSEG, 2026)"; the press release may not list screens; (b) watch-list start "September 2018" carries no citation |
| D4 argument_coherence | pass | Title, results and conclusion align; the segment result (largest gains for large-cap constituents) is reconciled in §4.4 and §6 rather than ignored |
| D5 writing_quality | warn | Body 4,542 words against the configured 7,000; Figure 1 legend uses raw labels ("included", "nearmiss") |

## Failure Condition Checks

| Condition | Triggered |
|---|---|
| F1 mandatory block | no (evaluator dimensions D1 to D5 carry no block) |
| F2 mandatory warn | no mandatory dimension defined as mandatory warn in this contract instance; D2/D3 warns are high priority |
| F3 high-priority block | no |
| F6 normal-priority block | no |
| F4 own scoring plan warn, no mandatory block/warn | YES |
| F5 round-2 mandatory block | no |
| F0 | no (warns present) |

## Review Body

1. (D2) Add the matched-with-trend caveat wherever the announcement-stage number appears in the Abstract and Introduction, or quote the confirmation and list stages as headline numbers.
2. (D3) Stage 2.5 must verify the LSEG (2026) claim about eligibility screens; if unsupported, cite FTSE's ground rules or drop the parenthetical citation and state the screens as the authors' description. Add a source for the 2018 watch-list start (the authors' prior study or an LSEG release).
3. (D5) Relabel Figure 1 legend ("FTSE constituents", "Near-miss eligible stocks"); decide the length target with the authors.

## Evaluator Decision

evaluator_decision = accept_with_dissent_note (F4). The draft proceeds to the Stage 2 checkpoint with three dissent notes; D2 note 1 and D5 figure label can be fixed immediately; D3 note 2 belongs to Stage 2.5; the length target is an author decision.
