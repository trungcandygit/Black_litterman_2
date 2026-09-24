# Phase 4b round 2 / 5a / 5b / 6b re-scoring: manuscript_v2.md (framing A')

## Number-grounding audit (master skill axiom 7)
Every coefficient, SE, star, t-statistic and count in Tables 1-8 and A1 re-checked against output/*.csv on 2026-09-24. Two corrections applied:
1. Vingroup exclusion: code drops VIC, VHM, VRE, VPL, but VPL is not in the sample (listed after Oct 2025), so three stocks drop (35,259 -> 34,962). Text said "four"; fixed.
2. Rebalancing abnormal trading value benchmark: code uses each stock's mean daily log value from D_LIST-60 to D_LIST-6 calendar days; text said "mean before the list announcement"; made precise in Table 4B and Table 5 notes.
Derived numbers checked: exp(0.805)-1 = 124%; drop-Vin change at most 10.9%; two-way SE inflation at most 16%; RI placebo mean P3 -0.223 = one fifth of -1.120; exp(-0.884)-1 = -59%, exp(-1.120)-1 = -67%.

## Writer Dimension Scores
| Dim | Priority | Score | Evidence |
|---|---|---|---|
| D1 section_completeness | mandatory | pass | Sections 1-6, Appendix A1, Declarations, References; CRediT/funding placeholders are author inputs |
| D2 citation_density | mandatory | pass | 25 references, 0 uncited entries, 0 in-text citations without entry (script check; flagged hits were dates and compound names) |
| D3 argument_blueprint_fidelity | mandatory | pass | A' thesis: H1 = 4.1, H2 = 4.1 + Fig 1, H3 = 4.2, H4 = 4.3 + 4.4; selection counter-argument = 3.4 + 5.2 |
| D4 total_word_count | high | warn | Prose body 5,109 words (excl. tables/notes); 6,773 incl. tables, appendix, declarations; target 7,000. Up from 4,542; gap closed by substantive content (CARs, volatility, selection test), no padding |
| D5 per_section_word_count | high | pass | Results and robustness now carry the added analyses |
| D6 paragraph_structure | normal | pass | Claim-first headings; every results subsection ends with a Takeaway |
| D7 register_consistency | normal | pass | 0 em dashes in prose (en dashes only in reference page ranges); banned-word grep 0 hits after fixing "robust" in the abstract; passive constructions 6 in 187 sentences |

Failure checks: F1 no, F4 no, F2 no, F3 yes (D4 warn), F0 yes. writer_decision = proceed_with_warn (D4 depends on whether 7,000 counts tables; author to confirm).

## Phase 5a: citations unchanged from v1 plus none added; all 20 scholarly DOIs Crossref-verified in Stage 1/2. Grey literature (5) to be content-verified in Stage 2.5.
## Phase 5b: abstract 181 words, punchline in sentence 2, no citations, 6 keywords.

## Phase 6b re-score against the Phase 6a scoring plan (unchanged pre-commitment)
| Dim | Score | Finding |
|---|---|---|
| D1 originality | pass | Stage decomposition of stock-level liquidity and price effects; search bound disclosed in 2.3 |
| D2 methodological_rigor | pass | Round-1 warn resolved: abstract and intro now caveat the announcement-stage estimate; selection test reported openly (5.2) |
| D3 evidence_sufficiency | warn | Stage 2.5 must verify: FTSE watch-list start September 2018 (uncited); tranche schedule 10/20/35/35 and effective date attributed to LSEG (2026); segment assignment of VCB/VIC/VHM and BID/VPB/HPG attributed to VIR (2026); naming dates from press reports |
| D4 argument_coherence | pass | Title question answered in 6; near-miss evidence reconciled as a selection bound, not contradicted |
| D5 writing_quality | pass | Figure labels fixed; length close to target if tables count |

evaluator_decision = accept_with_dissent_note (F4: D3 warn routed to Stage 2.5).
