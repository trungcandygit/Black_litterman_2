# Stage 4.5 FINAL INTEGRITY: re-verification of integrity-correction round 6 (v9 -> v10)

This is a Final Verification (Mode 2, final-check), scoped to round 6. Round 6 made 12 `replace_block` ops, touching 12 of 193 blocks. The verifier did not write the edits.
Date: 2026-09-24. Model: claude-opus-5-5, single-model (`ARS_CROSS_MODEL` is not set).

## Verdict: **PASS**

| Count | Result |
|---|---|
| IL-SERIOUS | 0 |
| IL-MEDIUM | 0 |
| IL-MINOR | 0 |
| MAJOR_DISTORTION | 0 |
| UNVERIFIABLE | 0 |
| New E6 rows (v9 -> v10) | 0 (none found by the recorded semantic review) |
| AI failure modes SUSPECTED / INSUFFICIENT EVIDENCE | 0 / 0 |

- **Round-5 items.** All six round-5 issues (IL-MINOR-1..6) are resolved, and each uses the exact fix text that reverify_round5.md recommended.
- **Round-5 E6 rows.** ADV-E6-1 was restored, and that restore is re-verified below. ADV-E6-2 is dispositioned `authorize_with_reason` with a non-blank, evidence-based reason.
- **Regression check.** 181 of the 193 blocks are byte-identical to v9. The document header before the first block is also unchanged.
- **Advisories.** Three advisory notes are outside the issue count: N-1 (the E6 disposition record), N-2 (Highlight 1) and N-3 (Table 7 note).
- **Stage 5 gate.** Under the protocol, "PASS (zero issues)" sends Stage 4.5 to Stage 5. Before the Stage 5 entry checkpoint:
  - add the N-1 binding lines to `e6_dispositions_round6.md`;
  - persist the v10 E1/E1.1 artifacts (see below);
  - rebuild `submission/` from v10.clean. `submission/` still binds v9.

## Skill load record

Before any other work, all five files were read in full with the Read tool. `integrity_verification_agent.md` has 887 lines and was read in two pages (lines 1–730 and 731–887). All five paths resolve through `/root/.claude/skills/academic-pipeline`, which is a symlink to the ARS clone in the session scratchpad.

| File (actual path) | First heading |
|---|---|
| /root/.claude/skills/academic-pipeline/SKILL.md | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| /root/.claude/skills/academic-pipeline/agents/integrity_verification_agent.md | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| /root/.claude/skills/academic-pipeline/references/integrity_review_protocol.md | `# Integrity Review Protocol (Added in v2.0)` |
| /root/.claude/skills/academic-pipeline/references/claim_verification_protocol.md | `# Claim Verification Protocol (Phase E)` |
| /root/.claude/skills/academic-pipeline/references/ai_research_failure_modes.md | `# AI Research Failure Mode Checklist` |

## Inputs and bindings

| Artifact | SHA-256 |
|---|---|
| Base: correction_round6/manuscript_v9.md | d23b6ff6ecee983ed197ec8b797d9c7e5d96d71f09f90d7a7e12384693a25385 |
| Revised: correction_round6/manuscript_v10.md | 763d5303d9ada7f09c2d4b4185ff355cdc164ee05b3edd404acc66024252e2d7 |
| Revised clean: manuscript_v10.clean.md (equals v10 with the block markers removed; checked) | 3cb8bd0b7185d5596a94ed16d3459932679f1606e023868f752ec7d6f07ef68b |
| Patch: integrity_patch_round6.json (12 ops; revision_round 8, following round 5 = 7) | abe890f379cbb52033dc8c1f9241ed775387b59d9b993a7b641a99f00b204ee4 |
| Correction list: integrity_correction_list_round6.json | 92b28e1e1d9244e9d25b8bee484c5f4d4a46b3699b0d5a3a5c695b9228e0b9b9 |
| Authorization: integrity_authorization_round6.json (binds base, issue list and patch; event AUTHOR-EVENT-r5-final, input digest 86c1e825…5513) | a42da6a752040fb470f03709886e4cfd38acb9601e5c8239fc7b757e1e420e8b |
| E1 registry for v10 (built by this verifier with `build_claim_registry.py` into the scratchpad; 235 claims; tier ALL) | 84e3b95aa7b638f87bf11ef11bfece36f3bb855969a308a183e034f792ec780f |
| E1.1 coverage for v10 (`claim_registry_coverage.py`; `--validate-report` replay: PASS) | 6382f2a302d9941873119f8262060929bf0f09a82e976143a25ff115e8590cf1 |

**E1.1 coverage on v10.**
- Status: `completed`. There are 60 candidates: 58 are `registry_span_matched` and 2 are `candidate_unregistered`.
- The 2 unregistered candidates are the same two "Accessed 24 September 2026" URL lines as in v7–v9 (The Investor 2026a and 2026b, in the reference list). Neither is a claim.
- `semantic_extraction_coverage`: `not_machine_detectable`.
- The registry has 235 claims against 234 in v9, because the splitter now breaks the new Table 7 note at "Eq. (4),". The splitter is heuristic. This is not a new claim.
- **Orchestrator action:** these two files are in the scratchpad. Copy them into `ars/stage4_5_integrity/` as `claim_registry_v10.json` and `claim_registry_coverage_v10.json` (the builder is deterministic), so that the Schema 5 binding is persisted.

**Unchanged analysis.** Round 6 changed no `code/*.R` file and no `output/*.csv` file. Every number was checked against the same result files as in round 5.

## 1. Resolution of reverify_round5 issues and E6 rows

| Item | Block | Status | v10 evidence (quoted) |
|---|---|---|---|
| IL-MINOR-1 | B0068 | RESOLVED | "positive in several months, significantly so three and two months before it (0.33 and 0.23)". In t_event_study.csv (constituent, lamihud), m = -3 is 0.329 with *p* = 0.0015 and m = -2 is 0.232 with *p* = 0.0006. Every other positive pre-period month has *p* > 0.08 (m = -6: 0.248, *p* = 0.082; m = -8: *p* = 0.216; m = -10: *p* = 0.240). So "significantly so" is true, and it is true only of those two months. The wrong ordinal is gone. |
| IL-MINOR-2 | B0136 | RESOLVED | "prices and liquidity moved with FTSE's public statements, and the first-tranche rebalancing brought a trading surge but no reliable price effect." This is consistent with Table 5 (0.794\*\*\*, SE 0.116; B0087 "0.79 … *t* = 6.84") and with the effective-date CAR. |
| IL-MINOR-3 | B0071, B0189, B0067 | RESOLVED | Figure 1: "estimated jointly with the same month interactions for named-but-excluded stocks". This matches `i(relm, treated) + i(relm, named)` in analysis_revision.R line 84. Figure 2: "never-named, never-included controls". This matches `wk[itt == 1 \| never == 1]` at line 77, with `never = itt==0 & treated==0 & named==0` at line 62. Table 3: "the split rows come from one regression with never-named, never-included controls", which matches line 74. |
| IL-MINOR-4 | B0101, B0108, B0115 | RESOLVED | Table 6: "significance marks are omitted for the three-stock segments and the last row, and other details are as in Table 2". This matches the table: the Large and Mid columns have no marks, and the last-row Small cell is "0.645 (0.150)" with no marks. Table 7: "… and other details as in Table 2". Table 8: "(one-sided randomization inference) … and other details are as in Table 2". This matches `p_one_sided = mean(ri <= obs)` at analysis_revision.R line 148. Stars are now defined, through the Table 2 note ("\*, \*\*, \*\*\* denote significance at 5%, 1% and 0.1%"), in every starred table. |
| IL-MINOR-5 | B0131, B0213, B0148 | RESOLVED | Table 9 and Table A.3: "S1–S3 as defined in Section 5.2". B0123 in §5.2 defines S1, S2 and S3 by date. Table A.2: "log trading value is the mean daily log of 1 plus traded value in VND billion". This matches `lval_pre = mean(log1p(value_bn))` (analysis.R line 46), with `value_bn` in VND billion (line 32). tA1_balance.csv has lval_pre = 5.170, which matches the table. |
| IL-MINOR-6 | B0024 | RESOLVED | "they find persistent price gains for additions and returns and trading volume that respond differently when a country changes class". Paraphrase distance is assessed in §3. |
| ADV-E6-1 (up) | B0136 | RESTORED | Restored through the IL-MINOR-2 fix. The non-response is again limited to prices, and the liquidity (trading) surge at the rebalancing is stated. This is at or below the v8 rung. v8 said "left no reliable price effect"; v10 keeps that and adds the surge fact. |
| ADV-E6-2 (down) | B0025 | AUTHORIZED | The disposition is `authorize_with_reason`. The block is unchanged in round 6. See §6 for whether the disposition is consistent with the protocol. |

## 2. Regression check on unchanged blocks

- **Apply report.** `manuscript_v10.md.apply-report.json` gives 12 ops, 181 of 193 blocks preserved byte-identical (ratio 0.9378), `touched_ratio` 0.0622, no structural flags and no fresh blocks.
- **Independent check.** Splitting v9 and v10 on the block markers gives:
  - the same 193 block IDs, in the same order;
  - an identical header before the first block;
  - exactly 12 differing blocks: B0024, B0067, B0068, B0071, B0189, B0101, B0108, B0115, B0131, B0136, B0148 and B0213.
- **Patch ownership.** The 12 blocks match the patch ops and the authorized targets one to one. Every op carries only its own IL ID in `roadmap_item_ids`.
- **Build script.** Each edit in `build_correction_round6.py` asserts that its match is unique (`count(o) == 1`). The v10 text of every block equals the fix text in reverify_round5.md character for character.
- **Token conservation.** Of the 12 ops, 6 conserve all tokens. The 6 deltas are all intended pointer tokens:
  - "2" (Table 2) in B0101, B0108 and B0115;
  - "5.2" in B0131 and B0213;
  - "1" ("1 plus") in B0148;
  - "9" removed from B0213 (the "Table 9" pointer).
  - No citation token and no protected term changed.

Result: no unchanged block regressed.

## 3. Changed blocks: numbers, pointers, citation contexts, originality

**Numbers against output/.**
- B0068: every number is unchanged from v9. The newly implied significance is verified above.
- B0136: no number was added. The "trading surge" refers to 0.794\*\*\* in t4_rebalance_reg and Table 5.
- B0148: "1 plus" is the `log1p` offset.
- The other changed blocks add no numeric claims.

**Pointers.**

| Pointer | Target | Result |
|---|---|---|
| "as in Table 2" (B0067, B0101, B0108, B0115, B0131) | B0063, the Table 2 note: FE, clustering, star thresholds | Resolves |
| "Eq. (8)", "Eq. (7)", "Eq. (4)" | Equations unchanged since round 5 | Resolves |
| "Sections 3.3 and 5.1" (B0115) | B0050 (bootstrap and RI settings); §5.1 | Resolves; the pointer is unchanged from v9 |
| "Section 5.2" (B0131, B0213) | B0121 heading, B0123 S1–S3 definitions | Resolves |
| "dashed lines as in Figure 1" (B0189) | B0071 | Resolves |

**Citation contexts (Phase B, 100% of the cited sentences in changed blocks).**

| Block | Source | v10 context | Verified source text (phaseD_originality.md; phaseAB groups) | Verdict |
|---|---|---|---|---|
| B0024 | Biktimirov & Afego 2026 | "persistent price gains for additions and returns and trading volume that respond differently when a country changes class, and they trace the gains to institutional demand rather than to trading pressure or liquidity" | "Both new and repeated additions experience persistent stock price increases … Country reclassification events exhibit distinct return and volume effects … consistent with institutional investor demand as the underlying mechanism, rather than temporary trading pressure or liquidity effects" | SUPPORTED. "Respond differently" carries the meaning of "distinct … effects". |
| B0024 | Raddatz et al. 2017; Hau et al. 2010; Burnham et al. 2018; Dong et al. 2023 | unchanged sentences | earlier verdicts (reverify_round5 B6, B13) | SUPPORTED |
| B0136 | Hegde & McDermott 2003; Biktimirov & Afego 2026 | second sentence unchanged | reverify_round5 B4, B12 | SUPPORTED |

Phase A and A3: no reference entry or in-text citation changed; the citation delta is zero in all 12 ops. The 33 of 33 verdicts and the result of 0 orphan and 0 dangling citations carry over from reverify_round5.

**Phase D: paraphrase distance of the Biktimirov & Afego clause (100% of the changed wording).**
- The abstract wording on record (phaseD_originality.md, row 14 and the source table) is "Country reclassification events exhibit distinct return and volume effects".
- v9 read "distinct return and trading-volume responses when a country changes class". That kept 4 of 5 source words in order.
- v10 reads "returns and trading volume that respond differently when a country changes class".
- The only shared lexical items are "return(s)", "volume" and "country". There is no shared run of two or more content words, and neither "distinct" nor "effects" is kept.
- The clause order differs from the source: the outcome comes first and the country event second.
- A WebSearch for the exact v10 phrase (2026-09-24) returned no match; the results covered the return–volume relation in general.
- Grade: **PARAPHRASE (cited)**. The distance is adequate, and the round-1 CLOSE_MATCH fix is fully restored.
- Residual context note, not an issue: the four-part summary still follows the abstract's order (data, additions, reclassification, mechanism), and "rather than … trading pressure or liquidity" echoes the abstract. Both are unchanged since round 1 and were graded PARAPHRASE then. That grading still holds.

The other new wording in the table and figure notes, and in B0068 and B0136, re-expresses the authors' own methods and results. It is ORIGINAL. Result: 0 CLOSE_MATCH and 0 VERBATIM.

## 4. Highlight 1 (ars/stage5_finalize/build_stage5.py, HIGHLIGHTS)

"Illiquidity of likely index stocks fell 24% to 56% after FTSE's upgrade steps" (77 characters). This is the wording that reverify_round5 suggested. Checks:
- **Numbers.** The ITT Amihud estimates are -0.268 and -0.811 (t_itt.csv; Table 3), which give 1 − e^−0.268 = 23.5% ≈ 24% and 1 − e^−0.811 = 55.6% ≈ 56%. The same figures appear in B0064 ("24%, 43% and 56%").
- **Group.** "Likely index stocks" means the ITT group of 27 preliminary-list stocks. Correct.
- **Wording.** The causal verb "cut" is gone, and "after" is temporal. This resolves the round-5 advisory.
- **Residual advisory N-2.** The figures are declines relative to never-named stocks (difference-in-differences), and the highlight does not say so. The abstract does ("Relative to never-named stocks …"). This is a highlight compression, not a distortion of direction or size. The highlight is outside the gated manuscript, so it is not counted.

## 5. E6 claim-strength drift, v9 -> v10 (12 changed blocks)

**Roadmap authority in round 6:**
- IL-MINOR-1..6 authorize the exact replacements.
- IL-MINOR-2 carries the ADV-E6-1 restore.
- No item authorizes an upward move.

| Block | Change | Rung / qualifier | Assessment |
|---|---|---|---|
| B0068 | "largest" -> "significantly so" | Descriptive to descriptive, with a significance statement. It discloses significant pre-period deviations more clearly and weakens nothing in the pre-trend caveat. The *F*-tests and the matched-sample caveat are kept. | Authorized (IL-MINOR-1). Not an upward move of any headline claim. Closed. |
| B0136 | liquidity non-response removed; trading surge stated | Down to the v8 rung (restore). The "favour … recognition channel" rung is unchanged. | Authorized (IL-MINOR-2 / ADV-E6-1 restore). Closed. |
| B0024 | reworded paraphrase | Same rung. The source attribution is kept, including "rather than … liquidity". | Authorized (IL-MINOR-6). Closed. |
| B0067, B0071, B0189, B0101, B0108, B0115, B0131, B0148, B0213 | disclosures and pointers added to notes | No claim-strength content. No caveat removed; caveats added (controls, significance-mark omissions). | Closed |

- No limitation, hedge, null result or causal caveat was removed.
- No upward move occurred.
- `STRENGTH-DRIFTED` rows: **none detected by the recorded semantic review**. This is a semantic review, not a deterministic no-drift certificate.

## 6. Consistency of e6_dispositions_round6.md with the protocol

| Row | Action | Protocol check | Result |
|---|---|---|---|
| ADV-E6-1 | `restore` | The protocol says a restore "must return through revision and a fresh integrity/E6 pass". Round 6 applied the restore, and §1 and §5 of this report are that fresh pass on the exact v10 bytes. | Consistent. The row is closed. |
| ADV-E6-2 | `authorize_with_reason` | The protocol requires a non-blank reason. The stated reason is specific: an uncited comparative claim, flagged by proofreading rule 5.10/1.6 and by stop-slop O-5, with no supporting evidence, and removing it weakens no result. It traces to AUTHOR-EVENT-r5-final, in which the author explicitly asked for the proofreading and AI-slop round that produced O-5. It is therefore not a bare "continue". The allowed actions are only restore, authorize_with_reason and pause, and the chosen action is one of them. Restoring the sentence would reinstate an unsupported claim. | Consistent in action and reason. |
| Traceability note | — | The claim that "AUTHOR-EVENT-r5-venue" refers to the venue message under AUTHOR-EVENT-r5-notes was checked. author_events_round5.md, r5-notes, contains "với cả nhớ đúng required của tạp chí nha". | Verified |

**N-1 (procedural advisory; outside the issue count).** The protocol's carrier is a `claim-strength-drift-findings/1.0` companion plus a `claim_strength_drift_disposition.py` sidecar that binds the raw event bytes. `e6_dispositions_round6.md`:
- is a Markdown record;
- does not restate the contract boundary that `e6_dispositions.md` recorded for this run: the Revision-Evidence Bundle cannot be built, because the chain began with the round-1 full re-emission (v2 -> v3) outside the patch chain;
- does not name the raw-event digest behind the ADV-E6-2 authorization.

The dispositions themselves are sound. Only the binding lines are missing. Exact text to append to `e6_dispositions_round6.md`:

> Contract boundary: as recorded in `e6_dispositions.md`, the Revision-Evidence Bundle for this run cannot be built because the patch chain begins with the round-1 full re-emission (v2 -> v3); the `claim-strength-drift-findings/1.0` artifact is therefore `skipped_no_revision_evidence`, and this table is the supplementary semantic review required by `unregistered_claim_drift_review_required: true`. Author event for ADV-E6-2: AUTHOR-EVENT-r5-final (explicit session user message; input SHA-256 86c1e8255007b56cfbd4857b0b82df7efc6e449f1dd2f9fc1078053ce79c5513, as bound in integrity_authorization_round6.json). ADV-E6-1 restore re-verified in reverify_round6.md. Derived pipeline action: `authorized_to_continue`.

## 7. AI research failure-mode checklist (round-6 changes)

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug | CLEAR | No code or output changed. Each new method disclosure matches the code line: analysis_revision.R lines 62, 74, 77, 84 and 148; analysis.R lines 32 and 46. |
| 2 Hallucinated citation | CLEAR | There is no citation delta. The Biktimirov & Afego context is SUPPORTED. |
| 3 Hallucinated result | CLEAR | No number was added. The implied significance in B0068 matches the *p*-values in t_event_study.csv. The surge in B0136 matches Table 5. |
| 4 Shortcut reliance | CLEAR | Design and identification are unchanged. |
| 5 Bug reframed as insight | CLEAR | No new "surprising" claim was added. |
| 6 Methodology fabrication | CLEAR | The three note disclosures dropped in v9 are restored, and each is traced to code. |
| 7 Frame-lock | CLEAR | Framing and scope are unchanged. |

No mode is SUSPECTED and none is INSUFFICIENT EVIDENCE, so the checklist does not block.

## 8. Issue list (sorted by severity)

### SERIOUS
None.

### MEDIUM
None.

### MINOR
None.

### Advisory (outside the issue count; no gate effect)

| ID | Location | Note | Optional exact text |
|---|---|---|---|
| N-1 | ars/stage4_5_integrity/correction_round6/e6_dispositions_round6.md | The E6 disposition record lacks the contract-boundary statement and the event digest (§6). | Append the paragraph quoted in §6. |
| N-2 | ars/stage5_finalize/build_stage5.py, HIGHLIGHTS[0] | The highlight omits "relative to never-named stocks" (§4). | "Likely index stocks' illiquidity fell 24% to 56% relative to peers after FTSE's steps" (85 characters, at the 85-character limit). |
| N-3 | B0108 (Table 7 note) | "Other details as in Table 2" could in principle carry over Table 2's "matching weights in columns 3–4". In Table 7, only column 3 is matched. The column headers ("(3) CS spread, matched" and "(4) CS spread, volatility control") and the observation counts (4,751 against 34,369) remove the ambiguity, so this is not an issue. | Only if the notes are touched again: "…, spreads in decimal units (0.0010 = 0.10 percentage points), matching weights in column 3 and other details as in Table 2." |
| ADV-E5-1 | B0013 | The search-bounded novelty claim is unchanged and remains open, as in earlier rounds. | — |

## Correction routing

1. No correction round is needed. The v10 draft passes Stage 4.5 re-verification with zero issues.
2. Orchestrator housekeeping before the Stage 5 entry checkpoint:
   1. Persist `claim_registry_v10.json` and `claim_registry_coverage_v10.json` (the SHA values are above).
   2. Append the N-1 text to `e6_dispositions_round6.md`.
   3. Optionally apply N-2.
   4. Rebuild `submission/` and `ars/stage5_finalize/work/checks.json` from `manuscript_v10.clean.md` (SHA 3cb8bd0b…f68b). They still bind v9.
3. After a Stage 4.5 PASS, the Stage 5 entry checkpoint runs #660 and then #672 against the exact v10.clean bytes.

## Tool limitation disclaimer

- Phase D uses WebSearch heuristics. It is not a substitute for Turnitin or iThenticate.
- Crossref, doi.org and publisher full texts were not fetched. Phase B relies on the verified abstract evidence retained in `phaseD_originality.md` and the phaseAB group files, plus one WebSearch on 2026-09-24 for the new B0024 wording.
- Scope is round 6 only, as dispatched. Blocks unchanged since reverify_round5 keep that report's fresh verdicts.

## Verification audit trail (round 6)

- `python3` block split of v9 and v10 gave 12 changed blocks. The diff text is quoted in §1.
- `sha256sum` was run on the v9, v10, v10.clean, patch, issue-list and authorization files. The values are in the bindings table.
- v10.clean equals v10 with the markers stripped (True).
- `output/revision/t_event_study.csv`, constituent lamihud rows m = -13..11, supplied the *p*-values quoted in §1.
- Code lines were read: analysis_revision.R lines 40–52, 62–90 and 140–150; analysis.R lines 32 and 40–50.
- `output/revision/tA1_balance.csv` gives lval_pre = 5.17038589.
- `build_claim_registry.py` gave 235 claims. `claim_registry_coverage.py` found 60 candidates, of which 2 are unregistered (the URL lines). The replay returned PASS.
- WebSearch `"returns and trading volume that respond differently when a country changes class"` (2026-09-24) found no match; the top results were general return–volume papers (ScienceDirect S1057521922001399, S1057521921002489).
- `token_conservation_round6.json` and the apply report were read. `build_correction_round6.py` was read in full.
