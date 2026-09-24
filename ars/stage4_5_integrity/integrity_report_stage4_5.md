# Academic Integrity Verification Report: Stage 4.5 FINAL INTEGRITY

Run ftse2-20260924-01 · ARS academic-pipeline v3.22.1 (commit 6234edf) · executed 2026-09-24

## Verification Mode
Final Verification (Mode 2), fresh from-scratch pass on the Stage 4' draft, followed by the correction process (3 rounds; the maximum the protocol allows).

## Verdict
**PASS**: zero SERIOUS, zero MEDIUM, zero MAJOR_DISTORTION, zero UNVERIFIABLE on the accepted draft; the last MINOR item (N2-1) was corrected in round 3.

Accepted draft: `ars/stage4_5_integrity/correction_round3/manuscript_v7.clean.md`, SHA-256 `3331a4dea23bb7dddeabf4ca4d82ea4a60b12937637d1fe89374c93d4f7d132c` (anchored twin `manuscript_v7.md`).

## Verdict trajectory

| Pass | Draft | Verdict | Issues | Report |
|---|---|---|---|---|
| Fresh pass | v4 (Stage 4') | FAIL | 2 SERIOUS, 15 MEDIUM, 10 MINOR (+6 E6 drift rows) | phaseAB_group1-3.md, phaseD_originality.md, e6_semantic_review_round2.md, this report (Phase C) |
| Correction round 1 | v4 -> v5 (33 ops) | FAIL | 24/27 resolved, 3 MINOR partial; 2 new MEDIUM (GEIS version, Burnham close match); 2 E6 rows | reverify_round1.md |
| Correction round 2 | v5 -> v6 (9 ops) | PASS WITH NOTES | 6/6 resolved; 1 MINOR (reference date style) | reverify_round2.md |
| Correction round 3 | v6 -> v7 (13 ops) | PASS | MINOR N2-1 resolved; author-flagged table/figure source notes changed to "Authors' calculations" (file map moved to output/TABLE_SOURCE_MAP.md) | deterministic checks below |

Round 3 verification (deterministic): token-conservation shows no numeric, citation or protected-term delta in any of the 13 ops; outside the 13 edited notes/reference, v7 is byte-identical to v6; no `output/` path and no "Retrieved ... from" remains; claim registry rebuilt on v7 (250 claims) and coverage replay PASS.

## Verification Summary

| Category | Total | Passed | Issues (fresh pass) | Status on v7 |
|---|---|---|---|---|
| Reference existence (A1) | 31 + 2 added | 33 | 0 NOT_FOUND / 0 MISMATCH | PASS |
| Bibliographic accuracy (A2) | 33 | 33 | 1 SERIOUS provisional (Biktimirov & Afego DOI unconfirmed live; confirmed from raw Crossref record + ScienceDirect PII), 3 MEDIUM (FAQ version; LSEG titles x2) | PASS |
| Ghost citations (A3) | -- | -- | 0 orphan / 0 dangling | PASS (33 refs) |
| Citation context (B, 100%) | 73 contexts | all | 2 MAJOR_DISTORTION (Gregoriou & Nguyen; Hegde & McDermott), 7 UNVERIFIABLE_ACCESS/MEDIUM, 12 MINOR | PASS |
| Statistical data (C1/C2, 100%) | every numeric surface; Table 4 120/120 cells | all | 3 prose-vs-table errors (6.3%, 1.0%, 0.14-0.20), 1 df-convention p-value, heading overstatement | PASS |
| Reproduction from raw data | 48 output CSVs | 48 | 0 (p-value convention only) | PASS (repro/REPRO_REPORT.md) |
| Originality (D1, 72.2% of paragraphs; 100% of revised) | 52 of 72 | 51 | 1 CLOSE_MATCH (Biktimirov & Afego abstract); 1 new in round 1 (Burnham) | PASS |
| Self-plagiarism (D2) | -- | -- | not performed: author names not supplied, earlier paper not in repository | NOTED |
| Claim verification (E, 100% of registry) | 250 registered claims (v7) | -- | resolved via B/C; semantic extraction coverage `not_machine_detectable` | PASS |

## Phase E: Claim Verification Results

- Claim Registry: `claim_registry_v7.json` (`claim-registry/1.0`), draft binding `3331a4de…132c`, 250 claims, tier ALL.
- Coverage report (#737): `claim_registry_coverage_v7.json`, replay-validated PASS; candidate-unregistered count 2 (both reference-list URLs, not claims); semantic extraction coverage: `not_machine_detectable`.
- Evidence rows (#656): not persisted as `evidence_row/1.0` objects in this run (the evidence is recorded as quoted source snippets in the Phase A/B audit trails); disclosed as a carrier gap, not as successful evidence.
- E4 scope-conformance advisory: no SCOPE-BROADENED rows (claims restricted to Vietnam's upgrade and HOSE stocks).
- E5 novelty classification: ADV-E5-1, §2.3 "No study we know of, in a search bounded to Crossref records and the literature cited here, estimates the stock-level liquidity effect of a frontier-to-emerging reclassification with a comparison group and a pre-determined treatment list" -> SUPPORTED_WITHIN_SEARCH wording; nearest prior work now acknowledged (Biktimirov & Afego, 2026; Burnham et al., 2018; Dong et al., 2023). Open advisory, does not gate.
- E6 claim-strength drift: 8 rows (ADV-E6-1..6 from round 2; ADV-E6-R1-1..2 from correction round 1), every row disposed (5 restore, 3 authorize_with_reason) in `e6_dispositions.md`; none detected in correction rounds 2 and 3. Contract boundary: no Revision-Evidence Bundle can be built for this run (round 1 was a full re-emission), so the `claim-strength-drift-findings/1.0` artifact is `skipped_no_revision_evidence` and the semantic review is the supplementary review the apply reports require.
- Token-conservation advisory (#570): reports for Stage 4' and all three correction rounds (`token_conservation_round2.json` in stage4_5_integrity/, and correction_round{1,2,3}/token_conservation_round*.json); every delta is claimed by an issue ID.

## AI Research Failure Mode Checklist
See `failure_mode_checklist_stage4_5.md`: all 7 modes CLEAR (Mode 1/3 backed by full reproduction from raw data). No block.

## Stage 2.5 comparison
All Stage 2.5 fixes (B1-B8, C1-C2, E1) remain in place in v7. Two Stage 2.5 PASS items were found wrong by this fresh pass (Gregoriou & Nguyen context; the FAQ version/date), which is why Stage 4.5 re-verifies from scratch.

## Stage 3' traceability sidecar
Stage 3' ran with 5 independent seats but the #576 checker was not runnable (no Revision-Evidence Bundle), so no frozen `previously_missed`/`indeterminate` sidecar exists; the Stage 3' residual items were carried through Stage 4' as acknowledged limitations (Section 6) and were re-checked here as ordinary claims.

## Issue List
All IL-* items from the fresh pass and correction rounds are listed with descriptions and targets in `correction_round1/integrity_correction_list_round1.json` (27), `correction_round2/integrity_correction_list_round2.json` (6) and `correction_round3/integrity_correction_list_round3.json` (2). Open items on v7: none.

## Tool Limitation Disclaimer
Crossref, doi.org, OpenAlex, Semantic Scholar, publisher sites (ScienceDirect, Wiley, T&F), lseg.com and ftserussell.com were blocked by the environment's egress policy (A0 = API_UNAVAILABLE). Verification rests on WebSearch results (titles, abstracts, snippets, index listings) and on the raw Crossref JSON saved at Stage 1 (`ars/stage1_research/cr_*.json`). Full texts were not read; context verdicts that depend on body text are UNVERIFIABLE_ACCESS where the abstract was consistent. The originality check is heuristic WebSearch comparison (72.2% sample, 100% of revised paragraphs), not iThenticate/Turnitin; run the journal's similarity check before submission.

## Verification Audit Trail
Per-reference queries, top URLs, confirmed fields and source quotes: `phaseAB_group1.md` (R1-R11), `phaseAB_group2.md` (R12-R21), `phaseAB_group3.md` (R22-R31), `reverify_round1.md` and `reverify_round2.md` (added/changed references). Phase C audit: 120 Table 4 cells and all other tables matched to CSVs by script; reproduction logs in `repro/`.
