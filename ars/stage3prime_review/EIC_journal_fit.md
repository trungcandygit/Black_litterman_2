# Stage 3' Verification Re-Review: EIC (Journal-Fit Reviewer) seat

Seat: EIC, Journal-Fit Reviewer (handling editor, broad empirical-finance journal; configured venue Finance Research Open, `criteria_binding_unavailable`). Frozen Round-1 card: fit, contribution, presentation (D5, D6).
Protocol: re_review_mode_protocol.md, Three-Gate Orchestration (#576 Spec B).
Inputs read in Phase 1: ars/stage3_review/00_phase0_config_and_phase1_precommitment.md, 01_phase2_reviewer_reports.md (EIC section and shared findings), 02_editorial_decision_and_roadmap.md. No manuscript, diff, response letter, adjudication sidecar, other Stage 3' output, or conversation log was read.
Note on criterion source: the Round-1 roadmap has no separate Schema 7 `verification_criteria` field; the roadmap item text (verbatim) plus the source finding text is taken as the inherited criterion. SR8 is should_fix, so there is no letter Acceptance-criteria block (letter blocks cover must_fix only).

## Phase 1 pre-commitment

### SR8 (should_fix): abstract length
- item_id: SR8
- obligation_class: should_fix
- source_reviewer: "EIC-W3"; source_reviewer_labels: [EIC]
- inherited_criterion: roadmap: "Check abstract length against venue limit". Source finding EIC-W3: "Abstract is 183 words; check the venue limit and drop the fourth-to-last sentence if needed."
- operationalization.fully_addressed: The revised abstract is shorter than the Round-1 183 words and is within a conventional Elsevier finance-journal abstract limit (at most about 150 words is the operating reading, since no binding venue limit is recorded; a count at or below 150 counts as FULLY_ADDRESSED, a reduction that still leaves it above 150 but clearly shortened with no redundant sentence counts as PARTIALLY_ADDRESSED). The abstract must still state the question, design, main finding with magnitude, and scope, and must not contain a claim contradicted by the body. An unchanged abstract of about 183 words or longer = NOT_ADDRESSED; a longer or less accurate abstract = MADE_WORSE (generic should_fix discriminator).
- expected_change_surface: Abstract (front matter); possibly the title page / highlights if present.
- equivalence_policy: allowed

### EIC-W1 (verification of presentation; routed from D6 warn; substantively owned by RR1/DA-C1)
- item_id: EIC-W1 (presentation check; nearest roadmap items RR1, RR2)
- inherited_criterion: EIC-W1: "Contribution hinges on identification that is still open. The stage decomposition is the paper's one idea [S 1, para 6]; if selection explains the stage pattern, the contribution reduces to a descriptive account. Remedy: the identification repairs in R1/DA." Roadmap RR1: "Add an intention-to-treat analysis using the 28-stock preliminary list (screened on 31 Dec 2024 data): baseline DiD, event study, CARs. Report beside constituent results."
- operationalization.fully_addressed (presentation layer only; the econometric adequacy of RR1 is verified by R1/DA): the revised Introduction and Abstract state one contribution (the stage decomposition or a clearly named replacement), and that contribution is explicitly tied to estimates on a group defined from pre-announcement information (an ITT / preliminary-list group) reported beside or instead of the constituent group; the paper states what the ITT results imply for the stage pattern (survives, shrinks, or disappears) and scales its contribution claim to that result. Headline numbers in Abstract and Introduction match the tables that carry the pre-announcement-defined group.
- expected_change_surface: Abstract; Introduction contribution paragraph (S 1, para 6 area); Section 3.1 (sample/groups); Table 2 and new ITT columns/tables; Conclusion.
- equivalence_policy: allowed

### EIC-W2 (verification of presentation; routed from D5 minor; owned by RR2)
- item_id: EIC-W2 (presentation check; nearest roadmap item RR2)
- inherited_criterion: EIC-W2: "Section 5.2 near-miss analysis and Section 4 tables use two different group definitions of 'eligible' without a table that lists every stock named on each public list. Remedy: an appendix table of names by list (Nov 2025, Apr 2026, Aug 2026) and sample status." Roadmap RR2 (part): "appendix table of names by list".
- operationalization.fully_addressed: an appendix table lists every stock named on each public FTSE list (Nov 2025, Apr 2026, Aug 2026) with its sample status (treated / ITT / control / excluded); one set of group names is defined once (Section 3) and used identically in Section 4 tables, Section 5.2, and the appendix, so a reader can map any stock to its group without ambiguity.
- expected_change_surface: new appendix table; Section 3.1 group definitions; Section 5.2; notes of Section 4 tables.
- equivalence_policy: allowed

No NewStandardRecord. No escalation requested.

[CONTRACT-ACKNOWLEDGED]

## Phase 2A evidence verdicts

Inputs added at Phase 2A: ars/stage2_write/manuscript_v2.md (original) and ars/stage2_write/manuscript_v3.md (revised). No response letter, adjudication sidecar, other Stage 3' output or log was read. Word counts below are `wc -w` on the markdown source (abstract: text between "## Abstract" and "**Keywords"; body: Section 1 to the Appendix heading, table rows excluded, headings and table notes included).

### SR8 (should_fix): abstract length
- verdict: **MADE_WORSE**
- applied_criterion: precommitted (Phase 1 SR8 fully_addressed; generic should_fix discriminator)
- evidence_anchor: manuscript_v3.md, Abstract (line 5); compare manuscript_v2.md, Abstract (line 5).
- change_summary: The abstract grew from 183 words (v2) to 209 words (v3): the revision added two sentences on the intention-to-treat group and a long semicolon-joined price sentence. It did not drop the fourth-to-last sentence as Round 1 suggested and did not move toward the 150-word operating limit.
- note: Content quality improved: the abstract now states why the ITT group exists and reports its magnitudes (43%, 56%), which are checked against Table 3 (exp(-0.554)-1 = -42.5%; exp(-0.811)-1 = -55.6%). But this item is about length, and the length is worse. Suggested fix (advisory): about 150 words by (a) cutting the first sentence to a clause, (b) merging the two ITT sentences, and (c) dropping "and a test that allows for event-date clustering". Under the protocol, a should_fix MADE_WORSE sets a Minor Revision floor (B5) and counts against should_fix_addressed_rate.
- verified_by: EIC (Journal-Fit Reviewer)

### EIC-W1 (presentation check; roadmap owner RR1, verified on substance by R1/DA)
- verdict: **PARTIALLY_ADDRESSED**
- applied_criterion: precommitted (Phase 1 EIC-W1 fully_addressed, presentation layer)
- evidence_anchor: manuscript_v3.md S 1 para 7 ("The paper makes one contribution: ... with treatment defined on information available before the upgrade"); S 1 paras 4 and 5 (preliminary list, 30 June 2026 selection data); S 3.4 "Fourth" assumption; Table 3; Table 4 Panel B; S 5.2 closing paragraph (constituent estimates read as upper bounds, ITT as lower bounds); S 6 para 1.
- change_summary: v3 ties the single contribution to a pre-announcement-defined treatment. It adds ITT, predicted-constituent and included/not-included split estimates (Table 3) and ITT CARs (Table 4 Panel B), states that ITT liquidity effects are about two thirds of the constituent effects, and presents constituent and ITT estimates as upper and lower bounds. Headline liquidity percentages in the Abstract, Introduction and Conclusion match Tables 2 and 3.
- residual_gap: The contribution sentence claims a stage decomposition of both liquidity and price effects "with treatment defined on information available before the upgrade". On prices, the pre-defined group does not carry the confirmation-stage result at 5%: ITT confirmation [-1,+1] CAR is 3.1% (t = 1.86) against never-named stocks and 2.2% (t = 1.83) against large stocks, and [0,+20] is significant only against the large-stock benchmark (t = 2.38 vs 1.57). The Abstract reports only the constituent price effects ("both gains hold under four benchmarks") and does not say that the pre-defined group's confirmation-stage price effect is weaker. Section 4.2 frames the weaker confirmation effect as investors learning, but the contribution claim is not scaled to it. Needed: one clause in the Abstract and the contribution paragraph that limits the pre-defined-treatment claim to liquidity plus the announcement-week price effect, or that reports the ITT confirmation estimate directly.
- residual_obligation_class: should_fix
- scope note: EIC-W1 is not a separate roadmap item. This verdict covers presentation only and does not pass judgment on RR1's econometric adequacy, which R1/DA verify.
- verified_by: EIC (Journal-Fit Reviewer)

### EIC-W2 (presentation check; roadmap owner RR2)
- verdict: **PARTIALLY_ADDRESSED**
- applied_criterion: precommitted (Phase 1 EIC-W2 fully_addressed)
- evidence_anchor: manuscript_v3.md Appendix Table A2 ("Stocks by FTSE list"); S 3.1 para 2 (group definitions); S 2.1 para 2 (pointer to Table A2); Table 1, Table 9 row labels; S 4.1 heading; S 4.1 and S 5.2 Takeaways; H1 and H3 (S 2.4).
- change_summary: v3 adds Table A2, which lists the preliminary (Nov 2025) names split by later inclusion, the April 2026 additions and removal, and the constituents on neither list (in sample and not in sample). This lets a reader rebuild all 27 constituents (15 + 3 + 6 + 3) and all 14 named-but-excluded HOSE stocks (12 + GEE, BSR). Section 3.1 now defines one set of groups (constituents, named-but-excluded, never-named, ITT), and "near-miss" (11 uses in v2) is gone. This removes the two competing definitions of "eligible" that Round 1 flagged.
- residual_gap: Group labels still vary. "Likely constituents" means the final constituents in the S 4.1 heading (whose table, Table 2, uses final constituents) and in H3, but means the ITT group in the S 4.1 and S 5.2 Takeaways. The named-but-excluded group appears as "Named on eligible lists, not included" (Table 1), "Named-excluded" (Tables 4B and 9), "stocks FTSE named and then excluded" (Abstract) and "stocks FTSE had named and passed over" (S 4.3). H1 still says "other HOSE stocks" while the design compares against never-named stocks. Needed: one label per group, used everywhere; either drop "likely constituents" or reserve it for the ITT group.
- residual_obligation_class: consider
- verified_by: EIC (Journal-Fit Reviewer)

### Editorial assessment of the revised manuscript (EIC, D5/D6)
- **Structure.** The IMRaD-style order is unchanged and sound (setting, design, results by stage, robustness and selection, conclusion). Each results subsection opens with its claim and ends with a Takeaway. The new material (ITT, portfolio CAR tests, named-excluded selection panels) goes where a reader expects it. Section 5.2 now reads as a bounding argument, not a caveat, which serves the paper.
- **Length.** Body prose is about 6,700 words (v2: about 5,700), with 9 main tables, 1 figure and 2 appendix tables. This is acceptable for a broad open-access empirical finance venue. No binding Finance Research Open limit is on record (`criteria_binding_unavailable`), so the authors should check the current guide for authors. Growth is justified by the identification repairs. Tables 5 and 6 could merge, since both report the rebalancing surge by group, if a table cap applies.
- **Table 4 readability.** Two panels, 17 data rows, up to seven columns. It is readable because each column is one benchmark and the portfolio t sits beside each CAR. Two presentation weaknesses: it has no significance markers (the reader must compare each t with 1.96), and the text's headline windows differ by event ([-1,+5] for the announcement, [-1,+1] for the confirmation), which the table makes visible but the text does not justify (NEW-1). The cross-sectional t column is well used to show why clustering-robust inference matters.
- **Table 9 readability.** Three panels. Panel B's window definitions sit in the panel title, which is good. Panel C is a 14-row descriptive list and would be easier to scan sorted by first-named date and then by W2 change, with the two April additions visually set apart (they are already listed first). Panel A's constituent column raises a sample-definition question (NEW-5).
- **Terminology and group names.** Much better than v2; residual variation is recorded under EIC-W2.
- **Abstract.** Informative and now states the identification logic, but too long (209 words; SR8). The price sentence packs three claims and a robustness statement into one sentence.
- **Single contribution.** Clear and stated once (S 1 para 7), now tied to a pre-determined treatment. The scaling gap on the price side is recorded under EIC-W1.
- **Fit.** Good fit for a broad open-access finance venue. The topic is timely (the event ended in September 2026), the design is transparent, and the paper is accessible to non-specialists. The Declarations still contain author placeholders (NEW-6).

## New issues

- **NEW-1**
  - description: The headline announcement-price window changed from [-1,+1] (v2 Abstract: 3.3%) to [-1,+5] (v3 Abstract, S 1, S 4.2, S 6: 7.8%), while the confirmation headline stays at [-1,+1]. Under the new portfolio test, the announcement [-1,+1] CAR is significant only against the equal-weighted never-named benchmark (t = 2.27) and not against the matched (0.93), large-stock (1.54) or market-model (1.85) benchmarks. Yet the Abstract says both headline gains "hold under four benchmarks". The claim is literally true for the windows chosen, but the text never gives a pre-stated reason for using different windows for different events. A reader will read this as window selection.
  - location: manuscript_v3.md Abstract; S 4.2 para 1; Table 4 Panel A; S 6 para 1
  - severity: minor
  - found_by: EIC
  - confidence: 4/5
  - competence_basis: presentation and claim-to-table consistency (D5/D6); the inferential weight belongs to R1
  - attribution: regression
  - attribution_evidence: v2 Abstract and S 4.2 headlined the announcement [-1,+1] CAR (3.3%) and gave the same window for every event ("3% to 5% around each disclosure", v2 S 6 para 1). The per-event window choice and the "four benchmarks" claim first appear in v3.
  - nearest_roadmap_item: RR3/RR4
  - non_match_rationale: RR3 and RR4 require clustering-robust inference and alternative benchmarks, which v3 supplies. Neither addresses the choice of headline window per event, which the revision introduced when it moved the headline.

- **NEW-2**
  - description: Wrong cross-reference. The Introduction's third finding cites "(Table 5)" for the rise of the rebalancing surge with FTSE size segment; the segment results are in Table 6.
  - location: manuscript_v3.md S 1 para 7 ("Third, ... rising with FTSE size segment ... (Table 5)")
  - severity: minor
  - found_by: EIC
  - confidence: 5/5
  - competence_basis: presentation (D5)
  - attribution: regression
  - attribution_evidence: v2 S 1 cited "(Tables 4 and 5)", which was correct under v2 numbering (Table 5 = segments). Inserting the ITT table renumbered the tables, and this reference was not updated.
  - nearest_roadmap_item: RR2
  - non_match_rationale: RR2 covers group rebuilding and an appendix table. It does not cover cross-reference integrity after renumbering.

- **NEW-3**
  - description: The heading of S 4.4, "The gains and the rebalancing surge rise with FTSE size segment", contradicts its own text for the liquidity gains ("The ordering between mid and small stocks does not follow size"; mid-cap -0.20/-0.63/-0.82 against small-cap -0.39/-0.85/-1.00). S 4.4's Takeaway ("Index weight sets the size ... of the liquidity gain") and S 6 para 4 repeat the overreach. Only the rebalancing surge is monotone in segment.
  - location: manuscript_v3.md S 4.4 heading and Takeaway; Table 6; S 6 para 4
  - severity: minor
  - found_by: EIC
  - confidence: 5/5
  - competence_basis: claim-to-table consistency (D5)
  - attribution: previously_missed
  - attribution_evidence: The same heading and the same "does not follow size" sentence are in v2 S 4.4 (line 201 ff.) with Table 5; Round 1 did not flag it.
  - nearest_roadmap_item: SR2
  - non_match_rationale: SR2 asks for bootstrap inference and caution on three-stock segments. It does not address a heading that asserts a monotone ordering the table does not show.

- **NEW-4**
  - description: New interpretive claim: "Prices thus responded first to eligibility and then to the likelihood of inclusion" (S 4.2) and "In the announcement week, the portfolio of stocks on FTSE's eligible lists gained whether or not FTSE later included them ... Investors first priced eligibility" (S 6 para 3). No eligibility list was public in the announcement week: the preliminary list appeared in November 2025 and the April list in April 2026 (S 2.1). The named-excluded portfolio also includes GEE and BSR, first named in April 2026. The announcement-week gain of that portfolio therefore cannot reflect priced eligibility. At most it reflects predictable eligibility (size or liquidity), which the paper would need to argue.
  - location: manuscript_v3.md S 4.2 last paragraph before the Takeaway; S 6 para 3
  - severity: minor
  - found_by: EIC
  - confidence: 4/5
  - competence_basis: argumentative coherence as it bears on the contribution narrative (D6); DA/R2 own the substance
  - attribution: regression
  - attribution_evidence: v2 S 4.2 said "Near-miss stocks show no significant abnormal return in any window" and made no eligibility-pricing claim. The claim and the Table 4 Panel B evidence behind it are new in v3.
  - nearest_roadmap_item: RR6
  - non_match_rationale: RR6 asks that selection evidence be framed around FTSE's screening cut-off dates. It does not cover a price-learning interpretation that ignores list publication dates.

- **NEW-5**
  - description: Table 9 Panel A reports the constituent log Amihud coefficients and standard errors as identical to three decimals to Table 2 column 1 (-0.392 (0.098), -0.888 (0.124), -1.129 (0.178)). Table 2 is estimated without the named-but-excluded stocks (34,369 observations), but the Table 9 note says Panels A and B are "one regression each ... on all 366 stocks". Adding 14 stocks with their own window interactions changes the week fixed effects through their pre-period weeks, so exact equality is unexpected. Either the column was copied from Table 2 or the note misstates the sample. The note or the column needs correcting.
  - location: manuscript_v3.md Table 9 Panel A and Notes; Table 2
  - severity: minor
  - found_by: EIC
  - confidence: 3/5
  - competence_basis: table-note consistency (D5); the estimation check belongs to R1 or the integrity stage
  - attribution: regression
  - attribution_evidence: v2 Table 8 Panel A had one column (near-miss group only) and no constituent column. The juxtaposed constituent column and the "all 366 stocks" note are new in v3.
  - nearest_roadmap_item: RR2
  - non_match_rationale: RR2 asks for re-running T8 with rebuilt groups. It does not cover internal consistency between a new comparison column and its note.

- **NEW-6**
  - description: The Declarations still carry author placeholders ("[To be supplied by the authors before submission.]" for CRediT; "[Authors to confirm.]" for funding and competing interests). Submission to an Elsevier open-access journal needs these completed.
  - location: manuscript_v3.md Declarations
  - severity: minor
  - found_by: EIC
  - confidence: 5/5
  - competence_basis: venue submission readiness (D6)
  - attribution: previously_missed
  - attribution_evidence: The same placeholders are in v2 Declarations; Round 1 did not flag them.
  - nearest_roadmap_item: SR8
  - non_match_rationale: SR8 concerns abstract length only, not back-matter completeness.

No escalation exception. No dissent record.

[EVIDENCE-COMMITTED]

## Phase 2B traceability matrix

Inputs added at Phase 2B: ars/stage4_revise/response_to_reviewers_round1.md, read as untrusted author-authored persuasion. The committed Phase 2A verdicts and the NEW-1 to NEW-6 set above are unchanged. No other reviewer's Stage 3' file and no adjudication sidecar was read.

| item | obligation | 2A verdict | authors_claim | final verdict | adjustment_id / basis | evidence anchor |
|---|---|---|---|---|---|---|
| SR8 | should_fix | MADE_WORSE | "Abstract is about 200 words; within common Elsevier limits (250). Authors to confirm the venue limit at submission." (Suggested revisions table) | NOT_ADDRESSED | ADJ-EIC-1 / scope_correction | manuscript_v3.md Abstract (line 5): 209 words, no shortening; no venue-limit statement anywhere in the manuscript |
| EIC-W1 (presentation; roadmap owner RR1) | should_fix-level residual (not a separate roadmap item) | PARTIALLY_ADDRESSED | RR1: ITT estimates for 27 preliminary-list stocks; "Abstract and Introduction report ITT magnitudes"; constituent estimates read as upper bounds and ITT as lower bounds; ITT announcement-week CAR 7.5% (t = 3.97) | PARTIALLY_ADDRESSED | none | S 1 para 7; Table 3; Table 4 Panel B (ITT confirmation [-1,+1] t = 1.86 / 1.83); Abstract |
| EIC-W2 (presentation; roadmap owner RR2) | consider-level residual | PARTIALLY_ADDRESSED | RR2: three groups rebuilt from the public lists (24 / 14 / 328); comparison group relabelled "never-named"; Table 9 extended to 14 stocks; new Appendix Table A2 listing stocks by list | PARTIALLY_ADDRESSED | none | Table A2; S 3.1 para 2; S 4.1 heading and Takeaway; Table 1 and Table 9 row labels |

### Claim-vs-manuscript consistency

- **SR8.** The claim is partly inaccurate and the check is not done. The abstract is 209 words, not "about 200". The 250-word figure is a generic "common Elsevier" number, not a verified Finance Research Open limit; the configuration records `criteria_binding_unavailable`. The letter defers the check ("Authors to confirm the venue limit at submission"), so the check the item asks for has not been performed.
- **EIC-W1.** The claims match the manuscript. Table 3, the S 3.4 wording, the S 5.2 bounds sentence and the ITT magnitudes in the Abstract and Introduction are all present as described. The letter says nothing about the pre-fixed (ITT) group's confirmation-stage price effect or about scaling the price half of the contribution claim, so it locates no evidence that would close the committed residual gap.
- **EIC-W2.** The claims match the manuscript: Table A2, the three groups and the "never-named" relabelling are present. The letter does not address label consistency across sections, so the committed residual gap ("likely constituents" used for two different groups; four labels for the named-but-excluded group) stands.

### Adjustment records

- **ADJ-EIC-1**
  - item: SR8
  - from: MADE_WORSE
  - to: NOT_ADDRESSED
  - basis: scope_correction
  - rationale:
    - **The 2A reading had the wrong target.** The inherited criterion is "Check abstract length against venue limit". The Round-1 finding made shortening conditional: "check the venue limit and drop the fourth-to-last sentence if needed". My Phase 1 operationalization added a roughly 150-word working limit that is not in the inherited criterion; I should have recorded it only as an advisory NewStandardRecord. The 2A MADE_WORSE verdict judged the 183 to 209 growth against that added 150-word target.
    - **Re-verification against the correct target.** The item's subject is compliance with the venue limit. That limit is not bound in this round and is not established by the manuscript or by verified evidence, so the lengthening cannot be shown to degrade compliance. MADE_WORSE is therefore not established.
    - **Why NOT_ADDRESSED and not better.** The manuscript shows no venue-limit check, and the letter itself defers the check to submission. The item is NOT_ADDRESSED; it is not FULLY or PARTIALLY addressed.
    - **What the upgrade does not rest on.** It does not rest on the letter's 250-word assertion, which remains unverified.
  - effect: SR8 still counts against should_fix_addressed_rate. It no longer gives its own B5 trigger through "should_fix MADE_WORSE". The regression-attributed minor new issues (NEW-1, 2, 4, 5) set the same Minor floor independently.
  - evidence_anchor: manuscript_v3.md Abstract (line 5), 209 words; inherited criterion text in ars/stage3_review/02_editorial_decision_and_roadmap.md (SR8) and 01_phase2_reviewer_reports.md (EIC-W3).
  - source_ref: none (forbidden for this basis)

No other adjustments. No valid_rebuttal was booked; none of the routed items has Round-1 severity `critical`.

## Post-letter observations

These are decision-inert and seed the next round.

1. **Announcement window was chosen after seeing robustness results (bears on frozen NEW-1).** RR4's answer says: "The announcement [-1,+1] CAR is not robust (t 0.93 with matched controls), so we now describe the announcement effect over the week [-1,+5]." This confirms that the headline window was picked after the robustness results were known. The manuscript does not disclose this (S 4.2 and the Abstract give no reason for using different windows for the announcement and the confirmation). R1 should weigh it. At minimum the manuscript should report the [-1,+1] announcement result next to the headline and state why a week-long window fits a Tuesday announcement that was conditional on a later review.
2. **Manuscript hash.** The letter gives the manuscript_v3.md hash as "5c9bc9cb...fe6 before the final abstract wording edit; the file on disk is authoritative". The SHA-256 of the file on disk is 5c9bc9cb0c3c6fec67d1edc6755e1157f7cd20e09b5888df2c6ae6df031cdfe6, which matches the quoted prefix and suffix. Either the "final abstract wording edit" changed no bytes, or the letter's statement is stale. The orchestrator should confirm the input-manifest hash binding (G0) against the on-disk bytes.
3. **"About 200" versus 209.** SR8's answer understates the abstract's length (209 words by `wc -w`). This is minor, but it is a claim-accuracy slip in the letter.
4. **Phase 1 self-disclosure.** The SR8 Phase-1 record added a numeric threshold (about 150 words) beyond the inherited criterion, contrary to the `new_standard` boundary. ADJ-EIC-1 corrects the effect on the verdict. Future rounds should carry any venue-limit number only as an advisory NewStandardRecord, or bind it through a confirmed ReviewTargetContext.
5. **SR2 versus the S 4.4 heading.** The letter's SR2 answer says segment estimates are "described as descriptive given three-stock segments". The body text does this, but the S 4.4 heading and Takeaway still assert that gains rise with segment. This bears on frozen NEW-3 (previously_missed).
6. **RR3 consistency check.** The letter says the constituent-list price claim was withdrawn from the Abstract and Introduction. The manuscript matches: both now say the list "added no reliable price effect" / "produced no reliable price effect". Panel A's [-1,+5] list CARs sit near the 5% threshold (t = 1.99 and 2.02 under two benchmarks), so "no reliable" is defensible but borderline; R1 may want the wording tied to the [-1,+1] window.

[MATRIX-COMMITTED]
