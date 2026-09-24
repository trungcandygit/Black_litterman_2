# Stage 3' Verification Re-Review: R3 Perspective Reviewer

Seat: R3 Perspective (frozen Round-1 card: "Policy economist at a securities regulator / development finance institution"; focus "practical and policy implications, adjacent-field accessibility (D4)").
Routed items: RR5 (must_fix), SR5 (should_fix).
Protocol: re_review_mode_protocol.md, Three-Gate Orchestration (#576 Spec B).
Inputs read in Phase 1 (Round-1 artifacts only): ars/stage3_review/02_editorial_decision_and_roadmap.md; ars/stage3_review/01_phase2_reviewer_reports.md; ars/stage3_review/00_phase0_config_and_phase1_precommitment.md. No revised-manuscript bytes, metadata, diff or Response Letter were opened before this section was saved.

## Phase 1 pre-commitment

Note on inheritance: the Round-1 roadmap carries no separate Schema 7 `verification_criteria` column and the decision letter carries no separate per-item "Acceptance criteria" block. The inherited criterion is therefore the roadmap item text (verbatim) plus the remedy text of the source findings it cites (verbatim). Letter ref for RR5 derived from must_fix order: R5 (fifth must_fix row).

### RR5 (must_fix)

- item_id: RR5
- obligation_class: must_fix
- source_reviewer: "R3-W1, DA-M2"; source_reviewer_labels: [R3, DA]
- letter_item_ref: R5
- inherited_criterion:
  - roadmap / letter_text: "Scope effective-date and \"prices already adjusted\" claims to the first 10% tranche" (Anchor: "Abstract, S 4.3, S 6").
  - R3-W1: "The effective date carried only the first tranche, 10% of the applicable weight; 90% arrives in March, June and September 2027 [S 2.1]. \"The effective date added nothing\" and \"index funds ... found prices already adjusted\" [Abstract; S 4.3; S 6] should be scoped to the first tranche. Remedy: rephrase and add the tranche caveat where the claim is made."
  - DA-M2: "\"effective date added nothing\" overgeneralises from the 10% first tranche [Abstract, S 6]."
- operationalization.fully_addressed: In the revised manuscript, every statement that the effective date produced no (or no additional) liquidity/price effect, and every statement that index/passive funds "found prices already adjusted" (or equivalent wording), is either (a) explicitly qualified in the same sentence or immediately adjacent sentence as referring to the first tranche (10% of the applicable weight), or (b) removed. This must hold at each location where the claim is made, at minimum the Abstract, the effective-date results discussion (S 4.3 or its successor), and the Conclusion/implications (S 6 or its successor), plus any other location (Introduction, hypothesis statement, figure/table notes) where an unqualified version of the claim appears. The manuscript states somewhere reader-visible that the remaining ~90% of weight is scheduled for later tranches (March, June, September 2027) that fall outside the sample, so the effect of the later tranches is untested. No sentence generalises the first-tranche null to "the effective date" or "inclusion" as a whole.
- operationalization.partially_addressed: The tranche caveat is added at some but not all claim locations (e.g., scoped in S 4.3 but the Abstract or S 6 still says the effective date "added nothing" or that funds "found prices already adjusted" without qualification); or the caveat appears only in a limitations paragraph/footnote while the headline sentences remain unscoped; or the 10% figure is mentioned but the later-tranche untested status is not stated.
- operationalization.made_worse_discriminator: The revision strengthens or spreads the unscoped claim relative to v2: e.g., new or stronger wording that inclusion/the effective date has no effect in general, the unscoped claim added to new locations (title, highlights, policy implications, Introduction) without the tranche qualifier, or the tranche fact (10% first tranche; 90% in 2027) removed or misstated (e.g., stated as the full weight) where v2 had it.
- expected_change_surface (hypothesis only): Abstract; S 4.3 effective-date results; S 6 conclusion/implications; possibly S 1 Introduction contribution paragraph, S 2.1 tranche description, S 2.4 hypothesis wording, and the limitations paragraph.
- equivalence_policy: allowed

### SR5 (should_fix, lighter form)

- item_id: SR5
- obligation_class: should_fix
- source_reviewer: "R3-W2, R3-W3"; source_reviewer_labels: [R3]
- inherited_criterion:
  - roadmap: "Present cost-of-capital as motivation, not finding; note investor-type data limitation"
  - R3-W2: "Cost-of-capital implications for issuers [S 1; S 6] are inferred, not measured. Remedy: present as a motivation citing Bekaert et al. (2007), not as a finding."
  - R3-W3: "The recognition-channel reading lacks investor-type evidence; foreign net buying data (published by the exchange) would test it directly. Remedy: acknowledge in the limitations or add if obtainable."
- operationalization.fully_addressed: Two parts, both required. (1) Every cost-of-capital statement for issuers (at minimum S 1 and S 6 or their successors, plus the Abstract if present there) is framed as motivation, prior evidence, or a conjectured implication attributed to prior literature (e.g., Bekaert et al., 2007 or equivalent), and no sentence presents a lower cost of capital, cheaper equity financing, or valuation gain for issuers as a result of this paper's estimates; OR the paper actually measures a cost-of-capital proxy and reports it as a finding with evidence. (2) The manuscript states, in the limitations or the discussion of the recognition/foreign-investor channel, that investor-type (e.g., foreign vs domestic, or foreign net buying) data are not used, so the recognition-channel reading is not directly tested; OR it adds investor-type evidence and reports it.
- expected_change_surface (hypothesis only): S 1 Introduction (motivation/contribution); S 6 conclusion/policy implications; limitations paragraph (S 5 or S 6); S 2.2 channel discussion.
- equivalence_policy: allowed

### NewStandardRecord
None. The inherited criteria are operable as written.

[CONTRACT-ACKNOWLEDGED]

## Phase 2A evidence verdicts

Inputs added at this gate: ars/stage2_write/manuscript_v2.md (original, 409 lines) and ars/stage2_write/manuscript_v3.md (revised, 476 lines). No Response Letter, adjudication sidecar or other Stage 3' output was opened. Anchors use `[v3 S x.y ¶/line n]` (line numbers of manuscript_v3.md) with verbatim quotation; the comparison with v2 is by direct reading of both files (no separate patch/apply report was supplied to this seat).

### RR5 (must_fix): PARTIALLY_ADDRESSED

- applied_criterion: precommitted (Phase 1 RR5 operationalization)
- verdict: PARTIALLY_ADDRESSED
- evidence_anchor (scoped, satisfying the pattern):
  - [v3 Abstract, line 5]: "the constituent list and the first 10% index tranche added no reliable price effect."
  - [v3 S 2.1 ¶1, line 33]: "Inclusion is phased in four tranches that add 10%, 20%, 35% and 35% of the applicable index weight on 21 September 2026, 22 March 2027, 21 June 2027 and 20 September 2027 ... The effective date we study therefore carried only the first tenth of the eventual index weight."
  - [v3 S 2.4 H3, line 59]: "the first index tranche added no further price effect."
  - [v3 S 4.3 ¶3, line 234]: "Because the first tranche carried only 10% of the eventual index weight, this evidence concerns the first tranche; the three later tranches in 2027 may carry larger demand."
  - [v3 S 4.3 Takeaway, line 236]: "Index funds concentrated their first-tranche demand in one session ... and prices had already adjusted by then."
  - [v3 S 6 ¶1, line 364]: "The first index tranche added a trading surge at the rebalancing close ... and no price change."
  - [v3 S 6 ¶2, line 366]: "the index funds that the first tranche obliged to buy found prices already adjusted."
  - [v3 S 6 limits, line 376]: "the first tranche carried 10% of the eventual weight, so the analysis cannot evaluate the three tranches of 2027."
- evidence_anchor (unscoped instances remaining):
  - [v3 S 1 ¶1, line 13]: "On the effective date, prices did not move; the trace of index membership was a one-session trading surge at the rebalancing close." (no tranche qualifier in the sentence or paragraph; the paragraph also frames the surge as "the trace of index membership" generally)
  - [v3 S 1 ¶7, line 25]: "the constituent list and the effective date produced no reliable price effect (Table 4)."
  - [v3 S 4.2 ¶1, line 168]: "The constituent list and the effective date produced no reliable price effect".
- change_summary: v2's unscoped "the effective date added nothing" (S 4.2 takeaway) and "index funds that the reclassification obliged to buy found prices already adjusted" (S 6) were removed or rewritten to name the first (10%) tranche in the Abstract, H3, S 4.3 and S 6, the S 2.1 tranche paragraph now states that the effective date carried one tenth of the weight, and S 4.3 and the limitations paragraph add that the 2027 tranches are untested; three effective-date null statements (Intro ¶1, Intro contribution paragraph, S 4.2 opening) still carry no tranche qualifier.
- residual_gap: The Introduction's lead paragraph (line 13) and contribution paragraph (line 25), and the S 4.2 results sentence (line 168), state the effective-date price null without the first-tranche / 10% qualifier in the same or adjacent sentence. Under the committed operationalization this is the "caveat added at some but not all claim locations" pattern. The core remedy in R3-W1 and DA-M2 (Abstract, S 4.3, S 6, and removal of "added nothing") is met, and the S 2.1 statement makes the qualifier available to a careful reader, so the remainder is three sentence-level insertions ("the first, 10% tranche on the effective date").
- residual_obligation_class: should_fix
- made_worse check: not met. The tranche fact is kept, stated more prominently (S 2.1, Abstract), and no new unscoped generalisation to "inclusion" as a whole was added.
- verified_by: R3 (Perspective)

### SR5 (should_fix): FULLY_ADDRESSED

- applied_criterion: precommitted (Phase 1 SR5 lighter form)
- verdict: FULLY_ADDRESSED
- evidence_anchor:
  - Part (1), cost of capital as motivation: [v3 S 1 ¶2, line 15]: "Whether the promised liquidity reaches individual stocks ... bears on issuers' cost of capital, because liquidity is priced in emerging markets (Bekaert et al., 2007)." (motivation, attributed to prior literature). [v3 S 2.3 ¶2, line 49]: "A reclassification that improves liquidity for a subset of stocks could therefore shift their cost of capital relative to the rest of the market; we do not measure that shift here." [v3 Abstract; S 6 lines 364-376]: no statement that the estimates show a lower cost of capital; the S 6 issuer implication (line 374) speaks of "benefits" concentrating in holdable stocks, not of cost of capital.
  - Part (2), investor-type limitation: [v3 S 6 limits, line 376]: "The price data do not identify investor type, so we cannot observe whether foreign investors drove the gains. ... adding foreign-flow data would test ... whether foreign trading drives them."
- change_summary: v3 adds "we do not measure that shift here" to the S 2.3 cost-of-capital sentence and removes v2's "and the recognition channel has more room to operate" from the same paragraph; the Intro motivation sentence and the investor-type limitation sentence are carried over from v2 unchanged.
- note (non-verdict): part (2) was already present in v2 (v2 line 326), so the Round-1 R3-W3 remedy was partly satisfied before revision; v3 does not tie that limitation explicitly to the "favour the recognition channel" sentence (line 366), but the committed pattern (limitation stated in the limitations paragraph) is met.
- verified_by: R3 (Perspective)

### Dissents / escalation exceptions
None.

## New issues

Read of full v3 as a regulator / development-finance policy reader. Scope: implications that outrun evidence, accessibility to non-specialists, overgeneralisation from one event, likely policy misreadings.

### NEW-R3-1: "Redistributed liquidity" now lacks its relative-measure definition and sits beside a no-spillover assumption
- description: S 6 tells readers that "the classification event redistributed liquidity toward likely index stocks, and index averages diluted that redistribution." A regulator will read "redistributed" as liquidity taken from never-named (mostly small) stocks, a distributional harm claim with policy weight. The DiD estimates are relative, and the paper does not show an absolute loss for never-named stocks (the randomization placebo in S 4.1 shows large never-named stocks also became more liquid). In v2, S 3.4 defined the estimand for this purpose: "Under either reading, the estimate measures how the upgrade redistributed liquidity toward constituents." The revision deleted that sentence and now asserts that removing named-but-excluded stocks "prevents the most likely spillover channel ... from contaminating it" (v3 line 115), i.e. it assumes no spillover. Without a spillover there is no redistribution, only a relative gain, so the S 6 wording is now unsupported and internally in tension with S 3.4.
- location_anchor: [v3 S 6 ¶4, line 370]; [v3 S 3.4 third assumption, line 115]
- severity: minor
- confidence: 3/5
- competence_basis: D4 policy-implication accuracy; how a securities regulator would read a distributional claim.
- attribution: regression
- attribution_evidence: v2 line 107 (S 3.4) contained the defining sentence "Under either reading, the estimate measures how the upgrade redistributed liquidity toward constituents, the quantity that matters for issuers and regulators"; v3 line 115 replaces it with the no-spillover claim, while v3 line 370 keeps the "redistributed" conclusion. The inconsistency arises from the revision's edit to S 3.4.
- nearest_roadmap_item: SR6
- non_match_rationale: SR6 asks to scope "classification events redistribute liquidity" to this one event and to discuss pre-funding removal and sector composition. v3 does scope it ("In Vietnam's case"). This issue concerns a different defect: whether "redistribution" is supported at all, given that the revision removed the relative-estimand definition and adopted a no-spillover assumption. Scoping to one event does not fix it.

### NEW-R3-2: The Abstract presents index-fund trading as observed when the paper has no investor-type data
- description: The revised Abstract states "Index funds traded the constituents heavily at the rebalancing close, but not the stocks FTSE named and then excluded." The paper observes aggregate volume only; S 6 limits (line 376) says "The price data do not identify investor type." Attributing the volume to index funds is an inference from timing (a reasonable one), but the Abstract states it as an observed fact about a specific investor class. Non-specialist policy readers who quote the Abstract would cite it as measured passive-fund flow.
- location_anchor: [v3 Abstract, line 5]; contrast [v3 S 6 limits, line 376]
- severity: minor
- confidence: 3/5
- competence_basis: D4 accessibility to non-specialists; Abstract-level claim hygiene for policy audiences.
- attribution: regression
- attribution_evidence: v2 Abstract (v2 line 5) said "only a one-session trading surge at rebalancing that rose with index weight", with no investor-class attribution; the index-fund sentence is new in the v3 Abstract. (The body already had the inference in v2, in the S 4.3 takeaway "Index funds concentrated their demand in one session", so the regression is limited to promoting it to the Abstract as fact.)
- nearest_roadmap_item: SR5
- non_match_rationale: SR5 asks for an investor-type data limitation to be noted, and v3 notes it in S 6. This issue is about a separate Abstract claim that the limitation contradicts. SR5's committed pattern does not cover how the Abstract words the rebalancing result.

### NEW-R3-3: The regulator implication ("rewards clear and early communication") outruns a single-event design
- description: S 6 advises regulators that "the liquidity and price dividend of an upgrade arrives with credible announcements, which rewards clear and early communication of reclassification steps." The design has one event and no variation in how clearly or early information was communicated. It cannot show that clearer or earlier communication produces a larger or faster dividend, only that effects clustered at disclosure dates for this event. In addition, the price gains are measured with constituent estimates described as upper bounds (S 5.2), and 90% of passive weight is still to come. A regulator could read this sentence as evidence-based guidance on disclosure policy.
- location_anchor: [v3 S 6 ¶6, line 374]
- severity: minor
- confidence: 4/5
- competence_basis: D4 core: policy implications follow from evidence.
- attribution: previously_missed
- attribution_evidence: identical sentence in v2 S 6 (v2 line 324, "For regulators, the liquidity and price dividend of an upgrade arrives with credible announcements, which rewards clear and early communication of reclassification steps."); unchanged in v3 line 374. Round-1 R3 did not flag it.
- nearest_roadmap_item: SR6
- non_match_rationale: SR6 targets the "redistribute liquidity" generalisation and alternative explanations (pre-funding removal, sector composition). It does not reach the regulator-communication prescription.

### NEW-R3-4: The issuer implication on free float and foreign-ownership headroom is not tested in the paper
- description: S 6 says the concentration of benefits "strengthens the case for measures that raise free float and foreign-ownership headroom, which enter FTSE's investability and foreign-headroom screens." The paper does not relate free float or foreign headroom to any estimated gain. Its own evidence complicates the claim: named-but-excluded stocks (which passed FTSE's eligibility screens) gained in the announcement week and, for GEE/BSR, in liquidity. For a regulator this reads as support for relaxing foreign-ownership limits. The sentence also has a stacked relative clause ("..., which strengthens ..., which enter ...") that hurts readability.
- location_anchor: [v3 S 6 ¶6, line 374]
- severity: minor
- confidence: 3/5
- competence_basis: D4 policy implications and institutional context (FOL policy is a live regulatory lever in Vietnam).
- attribution: previously_missed
- attribution_evidence: v2 S 6 (v2 line 324) already read "strengthens the case for measures that raise free float and foreign-ownership headroom"; v3 adds only the trailing clause "which enter FTSE's investability and foreign-headroom screens". The unsupported prescription predates the revision, and the added clause describes institutional fact rather than creating the overreach.
- nearest_roadmap_item: SR4
- non_match_rationale: SR4 asked for a descriptive paragraph on free float and FOL in FTSE investability weights (institutional context in S 2.1). It did not address whether the S 6 policy prescription is supported by the estimates.

### NEW-R3-5: The headline timing claim ("gains arrived ... months before index funds traded") reads as a complete, causal account
- description: The Abstract's last sentence, Intro ¶1 and S 6 ¶1 say the upgrade "delivered its liquidity gains months before any index fund traded". Two qualifications in the paper do not reach these headline sentences: (i) index funds have so far traded only the 10% first tranche, and (ii) the constituent magnitudes are, by the paper's own reading, upper bounds affected by selection (S 5.2, S 6 ¶5). A policy reader will take "the upgrade delivered" plus the 59%/68% figures as the causal dividend of the upgrade, completed before passive buying. This overlaps RR5 in spirit but is a distinct timing and completeness claim, not an effective-date null.
- location_anchor: [v3 Abstract, line 5, final sentence]; [v3 S 1 ¶1, line 13]; [v3 S 6 ¶1, line 364]
- severity: minor
- confidence: 3/5
- competence_basis: D4 non-specialist misreading of headline claims.
- attribution: previously_missed
- attribution_evidence: v2 Abstract (line 5) "Vietnam's upgrade delivered its liquidity and price gains at disclosure, months before index funds traded"; v2 Intro line 13 and S 6 line 316 carry the same claim. v3 keeps it with minor rewording.
- nearest_roadmap_item: RR5
- non_match_rationale: RR5's inherited criterion covers the effective-date null ("added nothing") and "prices already adjusted" claims. It does not cover the positive timing claim that the gains arrived before index-fund trading, or the pairing of that claim with upper-bound constituent magnitudes.

[EVIDENCE-COMMITTED]

## Phase 2B traceability matrix

Letter read: ars/stage4_revise/response_to_reviewers_round1.md (lines 33-36 for RR5; summary-table row at line 51 for SR5). Treated as untrusted author-written persuasion. Phase 2A verdicts and new issues above are unchanged.

| item | obligation | 2A verdict | authors_claim | final verdict | adjustment_id / basis | evidence anchor |
|---|---|---|---|---|---|---|
| RR5 | must_fix | PARTIALLY_ADDRESSED (residual: should_fix) | "Agreed. We now state the tranche schedule with its source and scope every effective-date statement to the first tranche." Change locations given: S 2.1; Abstract; S 4.3 last paragraph; S 6 limitations. | PARTIALLY_ADDRESSED (residual: should_fix) | none (no change from 2A) | Scoped: [v3 Abstract line 5], [v3 S 2.1 line 33], [v3 S 4.3 line 234], [v3 S 6 line 376]. Still unscoped: [v3 S 1 line 13] "On the effective date, prices did not move"; [v3 S 1 line 25] "the constituent list and the effective date produced no reliable price effect"; [v3 S 4.2 line 168] "The constituent list and the effective date produced no reliable price effect" |
| SR5 | should_fix | FULLY_ADDRESSED | "Cost of capital now stated as motivation ('we do not measure that shift here'); investor-type limitation retained." Locations: S 2.3, S 6. | FULLY_ADDRESSED | none (no change from 2A) | [v3 S 2.3 line 49] "we do not measure that shift here"; [v3 S 1 line 15] (motivation, Bekaert et al., 2007); [v3 S 6 line 376] "The price data do not identify investor type" |

Claim-vs-manuscript consistency:
- RR5: INCONSISTENT in part. Every location the letter points to exists in v3 and matches the quoted text, and 2A had already credited all of them. The claim that "every effective-date statement" is scoped is false for three sentences: v3 lines 13, 25 and 168. The letter does not mention these locations, so there is no author pointer to follow. It gives no rebuttal on the merits and no scope correction (the item's target is the same one used in 2A). No admissible adjustment basis applies, so the verdict stays PARTIALLY_ADDRESSED with a should_fix residual.
- SR5: CONSISTENT. The quoted phrase appears at v3 line 49, and "investor-type limitation retained" is accurate: the sentence is unchanged from v2 line 326 at v3 line 376.

Adjustment records: none.

## Post-letter observations

(Decision-inert; these seed the next round only.)
- PLO-R3-1: The RR5 response says "every effective-date statement" is scoped, which overstates the revision. A one-phrase edit at v3 lines 13, 25 and 168 (e.g., "the effective date, which carried the first 10% tranche,") would make the claim true and close RR5.
- PLO-R3-2: The letter does not address NEW-R3-2 (the index-fund attribution in the Abstract) or the loss of the relative-redistribution sentence behind NEW-R3-1. Neither is visible from the letter, which confirms these were side effects of the revision and not deliberate author choices. This is recorded only; it does not change the frozen attribution.

[MATRIX-COMMITTED]
