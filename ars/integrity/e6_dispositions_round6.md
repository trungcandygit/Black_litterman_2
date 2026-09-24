# E6 claim-strength dispositions for reverify_round5.md

| Row | Block | Direction | Disposition | Basis |
|---|---|---|---|---|
| ADV-E6-1 | B0136 | up | restore | Round 6 applies the IL-MINOR-2 fix. The sentence now keeps the 0.79 rebalancing surge: "…and the first-tranche rebalancing brought a trading surge but no reliable price effect." |
| ADV-E6-2 | B0025 | down | authorize_with_reason | The removed sentence was an uncited comparative claim ("benchmark-tracking foreign money changes the investor base more than an S&P 500 addition does"). It was flagged by the final proofreading report (WARN, rule 5.10/1.6) and by the stop-slop audit (O-5). No evidence in the paper or in the verified sources supports it, and removing it weakens no result. The author's standing decision for this run is to fix integrity findings without being asked (user_decisions in ars/pipeline_state.json; AUTHOR-EVENT-r5-final). |

Traceability note (reverify_round5.md): "AUTHOR-EVENT-r5-venue", cited by integrity_correction_list_round5.json IL-MINOR-4, refers to the venue message recorded verbatim under AUTHOR-EVENT-r5-notes ("với cả nhớ đúng required của tạp chí nha"). The round-5 author input bound IL-MINOR-4 to AUTHOR-EVENT-r5-notes, which is the event that was hashed.

Contract boundary: as recorded in `e6_dispositions.md`, the Revision-Evidence Bundle for this run cannot be built because the patch chain begins with the round-1 full re-emission (v2 -> v3); the `claim-strength-drift-findings/1.0` artifact is therefore `skipped_no_revision_evidence`, and this table is the supplementary semantic review required by `unregistered_claim_drift_review_required: true`. Author event for ADV-E6-2: AUTHOR-EVENT-r5-final (explicit session user message; input SHA-256 86c1e8255007b56cfbd4857b0b82df7efc6e449f1dd2f9fc1078053ce79c5513, as bound in integrity_authorization_round6.json). ADV-E6-1 restore re-verified in reverify_round6.md. Derived pipeline action: `authorized_to_continue`.
