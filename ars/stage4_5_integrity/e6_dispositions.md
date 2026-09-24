# E6 claim-strength drift: author dispositions (Stage 4.5)

Author event: AUTHOR-EVENT-s45-standing (explicit session user message, raw bytes retained run-local outside the repository; SHA-256 recorded in correction_round1/integrity_author_input_round1.json). The author delegated every remaining choice with the instruction to follow the skill strictly and not to ask again; each choice below follows the reviewing agent's recommendation.

Contract boundary (honest): a `claim-strength-drift-findings/1.0` finding set and the `claim_strength_drift_disposition.py` sidecar require a Revision-Evidence Bundle that starts at an integrity-PASS draft. Round 1 (v2 -> v3) was a full re-emission outside the patch chain, so the bundle cannot be built; the contract artifact is recorded as `skipped_no_revision_evidence` and the semantic review below is the supplementary review the apply reports require (`unregistered_claim_drift_review_required: true`). Every reported row has an explicit disposition; none is left open.

| Row | Source review | Location | Move | Disposition | Reason / resulting action |
|---|---|---|---|---|---|
| ADV-E6-1 | e6_semantic_review_round2.md | B0013 Introduction | dropped caveat "limits causal readings" (up) | restore | restored in integrity-correction round 1 (IL-MEDIUM-15) |
| ADV-E6-2 | e6_semantic_review_round2.md | B0013 Introduction | "the rebalancing session raised trading value" -> "trading value rose" (down, causal -> descriptive) | authorize_with_reason | The paper infers index demand from timing and a falsification test and states that its data do not identify who traded (Section 4.3); descriptive wording matches that evidence. |
| ADV-E6-3 | e6_semantic_review_round2.md | B0084 Section 4.2 | unhedged "reflects characteristics investors could observe" (up) | restore | hedged to "suggests" in round 1 (IL-MEDIUM-15) |
| ADV-E6-4 | e6_semantic_review_round2.md | B0122 Section 5.2 | "timing points to selection" for both GEE and BSR (up) | restore | restricted to GEE in round 1 (IL-MEDIUM-15) |
| ADV-E6-5 | e6_semantic_review_round2.md | B0132 Section 5.2 | "reliable ... under three of four" (up) | restore | now "significant under three of four" (IL-MEDIUM-14) |
| ADV-E6-6 | e6_semantic_review_round2.md | B0084, B0137 | portfolio qualifier dropped (up) | restore | "only the portfolio of stocks ..." restored in both blocks (IL-MEDIUM-15) |
| ADV-E6-R1-1 | reverify_round1.md | B0135 Conclusion | "scaled by index weight" -> "largest for the largest constituents" (down) | authorize_with_reason | The surge ordering rests on three-stock upper segments that the paper reads as descriptive (IL-MEDIUM-5); the descriptive wording matches Section 4.4. |
| ADV-E6-R1-2 | reverify_round1.md | B0021 Section 2.2 | "force passive funds to buy on the effective date" -> "lead index funds to buy" (down) | authorize_with_reason | Harris and Gurel (1986) measure effects after the announcement, not specifically on the effective date (IL-MINOR-2); the weaker wording is the accurate attribution. |

Derived pipeline action: every row is `restore` (already carried out and re-verified) or `authorize_with_reason`, so the checkpoint is `authorized_to_continue` once round-2 re-verification passes.
