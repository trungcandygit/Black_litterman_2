# Response to Reviewers, round 2 (Stage 4')

Base: ars/stage4prime/manuscript_v3.anchored.md (v3 with block anchors; content identical to ars/stage2_write/manuscript_v3.md).
Revised: ars/stage4prime/manuscript_v4.md (anchored) and manuscript_v4.clean.md (anchors stripped).
Revision chain (#390/#670): roadmap_round2.json -> author_adjudication_round2.json (all 17 items will_address, author event = the author's standing instruction of 2026-09-24) -> revision_patch_round2.json (patch 1.1, 60 ops) -> ars_apply_revision_patch.py exit 0, apply report 1.3, authorization witness PASS, touched ratio 0.317, no heading or section-count change, 127 of 186 blocks byte-identical.
Honest boundaries: (1) no claim surfaces were registered, so the apply report flags unregistered_claim_drift_review_required; Stage 4.5 carries out that review. (2) The first patch emission was rejected (one op per block); the single permitted re-emission merged the three inserts into their replace ops. The applied patch was then re-emitted once more before any downstream use to replace the banned word "robust" with "reliable" in eight edited sentences; the superseded emission and output are kept in ars/stage4prime/superseded/. (3) Round 1 (v2 -> v3) was a full re-emission outside the patch chain, so a continuous Revision-Evidence Bundle from the Stage 2.5 PASS draft cannot be built.
New analyses: code/analysis_revision2.R (outputs in output/revision2/), code/figure2.R.

## Must-fix items

### REV-R2-01 (RR1 residual; DA, R1)
R. The ITT event study and its pre-trend test were unreported; headlines used the post-selected constituents; the weaker ITT confirmation price response was not stated.
A. Figure 2 now reports the ITT event study; the text states its joint pre-trend test rejects (F = 7.59, p < 0.001) because of positive deviations of 0.26 and 0.22 three and two months before the announcement, then a decline from -0.22 to -0.78. The abstract and the introduction now lead with the ITT declines (24%, 43%, 56%) beside the constituent declines. Section 4.2 and Table 4 panel B state that the ITT confirmation CAR is significant under three of four benchmarks and not against matched controls.
C. Abstract; Introduction paragraphs 1 and 7; Section 4.1 (Figure 1 paragraph and new Figure 2); Section 4.2; Section 6 paragraph 1.

### REV-R2-02 (DA NEW-1, DA NEW-3)
R. The upper/lower-bound reading and the selection argument from disclosure-date reactions did not follow.
A. Removed. Section 5.2 now says that selection on June 2026 data could favour stocks with large disclosure-date gains, that the ITT group is not exposed to this selection, and that the constituent and ITT estimates are reported side by side without either being treated as a bound. Section 3.4 describes ITT as an average over listed stocks that were and were not included.
C. Sections 3.4, 5.2 (last paragraph and takeaway), 6 (selection paragraph).

### REV-R2-03 (DA NEW-2, R1 NEW-R1-1, EIC NEW-1, RR4 residual)
R. Event windows were chosen unevenly across events; magnitudes came from one benchmark.
A. Three windows are now pre-specified for every event and all are reported for three groups under four benchmarks (Table 4, panels A to C). A CAR is called reliable when significant at 5% under all four. Magnitudes are given as ranges across benchmarks. Reliable: announcement [-1,+5] (3.9% to 7.8%, t 2.19 to 3.46) and confirmation [-1,+1] (2.7% to 4.5%, t 2.22 to 2.93). The text now states that the three-day announcement window is significant under one benchmark only, the list [-1,+5] under two of four, and the effective date under none.
C. Sections 1 (paragraph 6), 3.2, 4.2; Table 4.

## Should-fix and consider items

| Item | Response | Location |
|---|---|---|
| REV-R2-04 estimation windows | Estimation windows now exclude days -1 to +20 around every earlier disclosure (120, 98, 98, 89 days); market-model betas use the same windows. Conclusions unchanged; confirmation t rises to 2.22 to 2.93. | S 3.2, Table 4 notes |
| REV-R2-05 tranche qualifier | All effective-date statements now refer to the first 10% tranche; "months before index funds traded" replaced by "before the first index tranche took effect". | Abstract, S 1, 4.3, 4.4, 6 |
| REV-R2-06 BSR | BSR's decline came mostly after the cut-off; BSR moved from UPCoM to HOSE in January 2025 (VietnamPlus, 2024, verified); named-excluded estimates without BSR reported (-0.23, -0.46, -0.73). GEE is the single clear case of selection on rising liquidity. | S 3.1, 5.2, References |
| REV-R2-07 small-group inference | Significance marks removed for the three-stock segments and the two-stock group; estimates described as descriptive. | S 4.4, Table 6, Table 9 |
| REV-R2-08 drift test | With a constituent-specific post-announcement drift (-0.012 per week), the confirmation step remains (0.21, p = 0.035) and the list step does not (0.10, p = 0.40); H2 now holds for the confirmation only. | S 4.1, Table 8 |
| REV-R2-09 investability weights | Section 2.1 explains that the investability weight scales index weight, with FTSE's 49% illustration. | S 2.1 |
| REV-R2-10 sector and pre-funding | Dropping bank and securities-firm constituents: -0.44, -1.04, -1.40; ITT without them: -0.23, -0.52, -0.83. The pre-funding reform is discussed and listed as a limitation. | S 5.1, Table 8, S 6 |
| REV-R2-11 A-share literature | Limitation sentence now in the manuscript. | S 2.3 |
| REV-R2-12 matching weights | Matched estimates re-estimated with MatchIt weights: -0.23 (n.s.), -0.47, -0.69; with trend -0.20 (n.s.), -0.42, -0.64. Matched benchmark weighted. The announcement-stage conclusion is now stated as less certain. | Table 2, Table 8, S 4.1, 5.1, A.1 |
| REV-R2-13 policy and investor-type claims | Index-fund trading is now inferred from timing and a falsification test; implications are stated as consistent with one event; "redistributed" defined as relative. | Abstract, S 4.3, 4.4, 6 |
| REV-R2-14 labels and references | Table reference fixed (Tables 5 and 6); eligibility-pricing sentence rewritten (no list was public at the announcement); Table 9 note explains the identity with Table 2. | S 1, 4.2, 5.2, 6 |
| REV-R2-15 method wording | "Full-sample trend" wording; the two top-tercile pools (110 and 85 stocks) described separately. | S 3.2, 3.3, 5.1 |
| REV-R2-16 venue compliance | Table A.1/A.2 numbering; AI declaration uses the journal's section title and wording; access dates on web references. | Appendix, Declarations, References |
| REV-R2-17 rebalancing design | Table 5 note discloses the reference-day regression (0.62, t = 3.54) and why the window-average comparison replaced it. | Table 5 notes |

## Items carried as acknowledged limitations
- Section 4.4 heading still reads "rise with FTSE size segment"; the body and takeaway now state that the liquidity gain is not monotone across segments. The heading was not changed to avoid a structural edit in the last revision round.
- Upgrade versus pre-funding reform for the largest stocks cannot be separated (Section 6).
- Letter correction from round 1: the round-1 letter's hash note was wrong (the quoted hash was of the final v3 file), and its claim that SR7 was "recorded as a limitation" was not true of v3; both corrected here.
