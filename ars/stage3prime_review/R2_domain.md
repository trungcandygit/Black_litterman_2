# Stage 3' Verification Re-Review: R2 Domain seat

Seat: R2 Domain (frozen Round-1 card: researcher on index inclusion and market reclassification (MSCI/FTSE), familiar with Vietnam's market structure; dimension D2).
Routed items: RR2, RR6 (must_fix); SR4, SR7 (should_fix).
Provenance disclosure: single model family (claude-opus), same model family as the drafting and Round-1 seats; this seat has not read other Stage 3' seat outputs, the Response to Reviewers, or the author adjudication sidecar.

## Phase 1 pre-commitment

Inputs used: ars/stage3_review/02_editorial_decision_and_roadmap.md; ars/stage3_review/01_phase2_reviewer_reports.md (R2 report; EIC-W2); ars/stage3_review/00_phase0_config_and_phase1_precommitment.md. No manuscript (original or revised) and no revision metadata were read before this section was saved.

Note on inherited criterion format: the Round-1 roadmap is a prose table without separate Schema-7 `verification_criteria` fields. The inherited criterion is therefore the roadmap item text (verbatim) plus the source finding's remedy text (verbatim). The letter's Required Revisions table is the Acceptance-criteria block; the letter ref is derived from must_fix roadmap order (RR1..RR6 -> R1..R6).

---

### RR2 (must_fix)

- item_id: RR2
- obligation_class: must_fix
- source_reviewer (verbatim): "R2-W1, EIC-W2"
- source_reviewer_labels: [R2, EIC] (R2-W1 -> R2, EIC-W2 -> EIC after em-dash/hyphen tail stripping); routed seat: R2 (first non-DA label).
- inherited_criterion:
  - roadmap / letter_text (letter_item_ref R2): "Rebuild groups from all public lists (Nov 2025 = 28, Apr 2026 = 32, Aug 2026 = 27); remove named-but-excluded stocks from controls; re-run T2, T7, T8; extend naming-timing test to all named-excluded HOSE stocks; appendix table of names by list" (Anchor: S 3.1, S 5.2, T8)
  - source finding R2-W1 remedy: "rebuild groups from the full public lists (Nov 2025 list of 28, Apr 2026 list of 32, Aug 2026 constituents), re-run Tables 2, 7 and 8 with named-but-excluded stocks removed from controls, and extend the naming-timing test to all of them."
  - source finding EIC-W2 remedy: "an appendix table of names by list (Nov 2025, Apr 2026, Aug 2026) and sample status."
- operationalization.fully_addressed: ALL of the following are present in the revised manuscript and its code/outputs:
  (a) The group definitions in Section 3.1 (or equivalent) are built from the three public FTSE lists (Nov 2025 preliminary, Apr 2026 list, Aug 2026 constituents/review list), and every HOSE stock appearing on any list but not a constituent is classed as named-but-excluded (or otherwise removed from the control group), including at minimum KBC, KDH, FRT, DGC, EIB, DPM, PDR, DIG, KDC.
  (b) The control group used in the baseline DiD (T2 equivalent), robustness (T7 equivalent) and named-excluded/near-miss analysis (T8 equivalent) excludes all named-but-excluded stocks, and those tables are re-estimated (numbers changed or explicitly reported as re-run on the clean control).
  (c) The naming-timing (near-miss) test is extended from the original five stocks to all named-but-excluded HOSE stocks in the sample (stocks that are not in the sample, e.g., non-HOSE or insufficient data, are stated with reason).
  (d) An appendix table lists every stock named on each public list, with list membership per list and sample status (constituent / named-excluded / not in sample, reason).
  (e) The stock assignments in (a)-(d) match the public lists (checked against the cited public sources) and the code lists (nov_list / apr_list / constituents) implement the table without discrepancy. Counts reported in text match counts in the table and code.
- operationalization.partially_addressed: The groups are rebuilt and the control group is cleaned for the baseline, but one or more of: (i) T7 or T8 not re-run on the clean control; (ii) naming-timing test extended to only some named-excluded stocks without stated reason; (iii) appendix table missing or lacks one list or sample status; (iv) a small number (one to three) of assignment discrepancies against the public lists that do not change the headline estimates materially; (v) text/table/code counts inconsistent in a way that is clerical rather than substantive.
- operationalization.made_worse_discriminator: The revision introduces new misassignment relative to the public lists (e.g., a named-eligible stock is moved INTO the control group or a non-named stock is labelled named), the appendix table misreports public-list membership in a way that changes group composition used in estimation, the control group ends up containing more named-eligible stocks than in the original, or the revision asserts list membership/counts that contradict the cited sources.
- expected_change_surface: Section 3.1 (sample and groups); Section 5.2 (near-miss / naming-timing); Tables 2, 7, 8 (and any new named-excluded tables); a new appendix table of names by list; code list definitions (nov_list, apr_list, constituents) in the analysis script and matching output CSVs.
- equivalence_policy: allowed

### RR6 (must_fix)

- item_id: RR6
- obligation_class: must_fix
- source_reviewer (verbatim): "R2-W2"
- source_reviewer_labels: [R2]; routed seat: R2.
- inherited_criterion:
  - roadmap / letter_text (letter_item_ref R6): "Frame selection evidence around FTSE's screening cut-off dates (31 Dec 2024; 31 Dec 2025)" (Anchor: S 5.2)
  - source finding R2-W2 remedy: "state the cut-off dates and frame Section 5.2 around them." Context: "The Nov 2025 list used data as of 31 Dec 2024 and the Apr 2026 list data as of 31 Dec 2025 [EXT]. These dates turn the 'selection follows liquidity' discussion [S 5.2] into a testable statement: GEE and BSR improved in October to December 2025, inside the window FTSE screened for the April list."
- operationalization.fully_addressed: The revised manuscript (a) states the screening data cut-off dates for each list (Nov 2025 list: data as of 31 Dec 2024; Apr 2026 list: data as of 31 Dec 2025), correctly and with a citation to a public source that supports them; (b) Section 5.2 (or its successor) organizes the selection discussion around these dates, i.e., it distinguishes liquidity changes before vs. inside each screening window and states which stocks' pre-inclusion improvements fall inside the window FTSE screened (e.g., GEE, BSR in Oct-Dec 2025), so the "selection follows liquidity" claim becomes an explicit, testable timing statement; (c) any claims about what the cut-off implies (e.g., that the Nov 2025 list is pre-announcement information) are consistent with the dates.
- operationalization.partially_addressed: The dates are stated but the Section 5.2 argument is not organized around them (mentioned in passing only); or only one of the two cut-offs is stated; or the dates are stated without a supporting source; or the timing framing is present but applied to only some of the relevant stocks.
- operationalization.made_worse_discriminator: The revision states wrong cut-off dates (contradicting the FTSE/public sources), or attributes a cut-off to the wrong list, or uses the cut-offs to draw a conclusion the timing does not support (e.g., treating post-cut-off liquidity as screened information), or cites a source that does not contain the cut-off claim.
- expected_change_surface: Section 5.2; possibly Section 2.1 (timeline) and Section 3.1 (ITT group definition referencing the 31 Dec 2024 cut-off); references list.
- equivalence_policy: allowed

### SR4 (should_fix, lighter form)

- item_id: SR4
- obligation_class: should_fix
- source_reviewer (verbatim): "R2-W3"; labels [R2]; routed seat R2.
- inherited_criterion: roadmap: "Paragraph on free float and foreign ownership limits in FTSE investability weights". Source remedy R2-W3: "one paragraph in Section 2.1 from FTSE's documents." Context: "FTSE's investability weights depend on free float and foreign headroom; readers need this to interpret segment results."
- operationalization.fully_addressed: A paragraph (Section 2.1 or equivalent) explains that FTSE index weights are adjusted for free float and for foreign ownership limits/foreign headroom, that these determine investable weight (and hence passive demand per stock), cites an FTSE document (or equivalent primary/public source) that actually supports the statements, and links the point to interpreting stock-level/segment results. Statements must be accurate against the cited source.
- expected_change_surface: Section 2.1; possibly Section 4 segment discussion; references.
- equivalence_policy: allowed

### SR7 (should_fix, lighter form)

- item_id: SR7
- obligation_class: should_fix
- source_reviewer (verbatim): "R2-W4"; labels [R2]; routed seat R2.
- inherited_criterion: roadmap: "Verified addition on stock-level MSCI A-share inclusion liquidity studies". Source R2-W4: "The literature on MSCI's inclusion of China A-shares has stock-level liquidity studies beyond Dong et al. (2023); a short, verified addition would strengthen Section 2.3. Any added reference must pass integrity verification."
- operationalization.fully_addressed: Section 2.3 (or equivalent literature section) adds at least one real, correctly cited stock-level study of liquidity (or trading) effects of MSCI's China A-share inclusion, beyond Dong et al. (2023); the reference appears in the reference list with correct bibliographic details; the manuscript's characterisation of the study's findings is accurate; and the addition is connected to the paper's argument (not a bare citation).
- expected_change_surface: Section 2.3; reference list.
- equivalence_policy: allowed

### NewStandardRecords
None. (No inherited criterion was judged materially incomplete; no escalation requested.)

[CONTRACT-ACKNOWLEDGED]

---

## Phase 2A evidence verdicts

Inputs read at this phase: ars/stage2_write/manuscript_v2.md (original), ars/stage2_write/manuscript_v3.md (revised), code/analysis_revision.R, code/analysis.R (treated27 definition only), output/revision/{run_summary_revision.txt, t1_descriptives.csv, t8_named_excluded.csv, t8c_named_by_stock.csv}, data/raw/{BSR,GEE}.csv (date coverage only). Response to Reviewers and author adjudication sidecar NOT read. No patch/apply report was supplied, so change_summary comes from comparing v2 and v3 directly.

Anchor grammar: [v3 S x.y ¶n] = revised manuscript section and paragraph; [v3 T n] = table; [EXT: ...] = public source checked 2026-09-24.

### External verification log (institutional facts)

| Fact in manuscript | Where | Source checked | Result |
|---|---|---|---|
| Vietnam added to watch list Sept 2018 | v3 S2.1 ¶1 | FTSE Russell (2018) PDF p.3: "Vietnam is currently classified as a Frontier market and is being added to the Watch List for possible reclassification as Secondary Emerging." | Supported |
| 7 Oct 2025 announcement, effective 21 Sep 2026, interim review March 2026 | v3 S2.1 ¶1 | LSEG press release 7 Oct 2025 | Supported |
| 7 Apr 2026 confirmation, meets all criteria, effective date kept | v3 S2.1 ¶1 | LSEG press release 7 Apr 2026 | Supported |
| Four tranches 10/20/35/35% on 21 Sep 2026, 22 Mar, 21 Jun, 20 Sep 2027 | v3 S2.1 ¶1 | FTSE FAQ v1.3 (Aug 2026) Q4/Q5 | Supported |
| Preliminary 28-name list, data as of 31 Dec 2024, appeared Nov 2025 | v3 S2.1 ¶2; T A2 | Viet Nam News 13 Nov 2025 ("This preliminary list is based on data as of December 31, 2024"); The Investor 4 Mar 2026 (28 tickers + "data as of December 31, 2024") | Supported. All 28 tickers match `nov_list` exactly. Note: The Investor's 11 Nov 2025 article (d17585, not cited) wrongly says all 28 are HOSE-listed. HUT (Tasco) is on HNX, so the manuscript's HUT treatment is correct. |
| April 2026 list of 32, data as of 31 Dec 2025; PLX dropped; BID, FPT, NVL, GEE, BSR added | v3 S2.1 ¶2; T A2 | The Investor 8 Apr 2026 | Supported. The article lists 32 names consistent with `apr_list` = Nov list minus PLX plus 5. The press text misspells two tickers ("DIC" for DIC Corp = DIG; "DPR" for Phat Dat = PDR); the company names confirm the manuscript's DIG/PDR reading. |
| 21 Aug 2026 review, 27 names, data cut-off 30 June 2026, effective after close 18 Sep 2026 | v3 S2.1 ¶2; S1 ¶5; S3.4 | FTSE FAQ Q6 ("data cut-off as of 30 June 2026"), Q9 (published Friday 21 August 2026); VIR 22 Aug 2026 (after close 18 Sep) | Supported. The FAQ Q6 table of 27 names matches `treated27` exactly (Gelex Group = GEX; Masan Consumer = MCH; Vietnam Maritime CB = MSB; Southeast Asia CB = SSB; Techcom Securities = TCX; Vinpearl = VPL; VPS Securities = VCK). |
| Screens as non-constituents on liquidity, minimum size, foreign headroom; liquidity test uses investability weight (free float) | v3 S2.1 ¶2 | FTSE FAQ Q11, Q12, Q15 (and Q5's "investability weight (free float)") | Supported |
| Segments: Large VCB, VIC, VHM; Mid BID, VPB, HPG | v3 S4.4 | FTSE FAQ Q6; VIR 22 Aug 2026 | Supported |
| HUT trades on the Hanoi exchange | v3 S3.1 ¶2; T A2 | HNX/Vietstock/CafeF listings | Supported |

### RR2 (must_fix) — verdict: FULLY_ADDRESSED

- applied_criterion: precommitted (Phase-1 operationalization RR2 (a)-(e))
- verified_by: R2
- evidence_anchor:
  - (a) [v3 S3.1 ¶2]: groups are built from "FTSE's public lists (Appendix Table A2)"; 14 HOSE named-but-excluded stocks are listed (BSR, DGC, DIG, DPM, DXG, EIB, FRT, GEE, KBC, KDC, KDH, PDR, PLX, SAB), plus HUT noted as off-HOSE. All nine Round-1 names (KBC, KDH, FRT, DGC, EIB, DPM, PDR, DIG, KDC) are included.
  - (b) [v3 T2 notes] "named-but-excluded stocks removed" (N = 34,369 = 35,752 − 14 stocks' weeks); [v3 T8] robustness is on the clean control (N = 34,369); [v3 T9] replaces old T8. Code: `clean <- wk[named == 0]` (analysis_revision.R l.41), and robustness uses `clean`. The T2 numbers changed from v2 (the control was 337 stocks in v2; it is 328 never-named stocks in v3). The CSV t2 matches the run summary (−0.3915/−0.8884/−1.1287).
  - (c) [v3 S5.2; T9 panels A–C]: the naming-timing test now covers all 14 HOSE named-excluded stocks. HUT's absence is explained (HNX).
  - (d) [v3 T A2]: names by list (Nov later-constituents 15; Nov not included 12 + HUT; April additions and removal; constituents on neither list), with in-sample status for TCX/VCK/VPL and HUT.
  - (e) Code `nov_list`, `apr_list` and `treated27` match the public lists (see verification log). The run summary gives groups of 328/24/14, matching T1 and the text. The ITT count of 27 is 15 + 12, consistent with A2.
- change_summary: The 5-stock "near-miss" group and the 337-stock control of v2 are replaced by a 14-stock named-but-excluded group built from the Nov 2025, Apr 2026 and Aug 2026 public lists. Baseline, robustness and naming-timing tables are re-estimated on 328 never-named controls, and a names-by-list appendix table is added.
- Residual observations (non-blocking, not residual gaps):
  - Table A2 shows the April list as a delta, not a full list of 32, and it has no explicit sample-status column for every row. Both can be derived from the table and the text.

### RR6 (must_fix) — verdict: PARTIALLY_ADDRESSED

- applied_criterion: precommitted (Phase-1 operationalization RR6 (a)-(c))
- verified_by: R2
- evidence_anchor:
  - (a) Met. [v3 S2.1 ¶2] states both cut-offs (31 Dec 2024 for the Nov 2025 list; 31 Dec 2025 for the April 2026 list), citing Viet Nam News (2025) and The Investor (2026a, 2026b). It also adds the 30 June 2026 cut-off for the final list (FTSE Russell, 2026). All three are verified against the sources. The 31 Dec 2024 cut-off is also used in [v3 S1 ¶4–5], [v3 S3.4 ¶5] and the [v3 T3 notes].
  - (b) Largely met. [v3 S5.2 ¶2] and [v3 T9 panel B] re-cut the windows at the cut-off: W1 runs from 7 Oct to 31 Dec 2025, "inside the data FTSE screened for the April list"; W2 runs from 1 Jan to 6 Apr 2026; W3 starts 7 Apr 2026. The section reports that the GEE+BSR illiquidity fell by 1.15 inside W1 (p = 0.024) and that GEE fell by 1.83 before the cut-off [v3 T9 panel C].
  - (c) Not fully met. The concluding claim in [v3 S5.2 ¶3], "at least two stocks became eligible after their liquidity rose during the screening window", treats BSR like GEE. The paper's own [v3 T9 panel C] shows otherwise:
    - BSR's W1 change is −0.39. Its large decline (−1.68) falls in W2, after the 31 Dec 2025 cut-off, so it lies outside the data FTSE screened for the April list.
    - The p = 0.024 for the two-stock W1 estimate is driven by GEE (−1.83).
    - The cut-off framing also leaves out an institutional fact that bears directly on BSR. BSR traded on UPCoM until 6 Jan 2025 and first traded on HOSE on 17 Jan 2025 [EXT: VietnamPlus/Viet Nam News, 30 Dec 2024; confirmed in data/raw/BSR.csv, which has a gap from 7 to 16 Jan 2025]. So BSR was not exchange-listed on HOSE at the 31 Dec 2024 cut-off for the November list. Its absence from that list, and its appearance on the April list, has a listing-venue explanation that the "selection follows liquidity" reading does not address.
  - Made-worse check: no wrong dates, no cut-off assigned to the wrong list, no unsupported source. The BSR overstatement was already present in v2 ("GEE and BSR ... before any report named them"). v3's cut-off framing makes the gap visible but does not introduce it. So this is not MADE_WORSE.
- change_summary: Section 5.2 is reorganized around FTSE's screening cut-offs (windows now split at 31 Dec 2025 instead of the press-report dates), and the cut-off dates are stated and sourced in Sections 1, 2.1 and 3.4.
- residual_gap: Section 5.2's selection conclusion must match the cut-off evidence stock by stock. Either restrict the "liquidity rose inside the screening window" claim to GEE, or state that BSR's decline is mostly after the 31 Dec 2025 cut-off. In addition, note BSR's transfer from UPCoM to HOSE on 17 Jan 2025, after the 31 Dec 2024 cut-off, as an alternative, venue-based reason for its absence from the November list.
- residual_obligation_class: should_fix

### SR4 (should_fix) — verdict: PARTIALLY_ADDRESSED

- applied_criterion: precommitted (lighter form)
- verified_by: R2
- evidence_anchor: [v3 S2.1 ¶2] "FTSE screened Vietnamese securities as non-constituents on its liquidity, minimum-size and foreign-headroom screens, using each security's investability weight (free float) in the liquidity test (FTSE Russell, 2026)." [v3 S6 ¶5] adds "free float and foreign-ownership headroom, which enter FTSE's investability and foreign-headroom screens." The statements are accurate against FAQ Q11, Q12 and Q15.
- change_summary: One sourced sentence on FTSE's eligibility screens (liquidity, size, foreign headroom, investability weight) is added to Section 2.1, and the conclusion sentence is linked to it.
- residual_gap: The committed pattern asks for a paragraph explaining that FTSE index weights, and so passive demand per stock, scale with investable market capitalisation: capitalisation times the investability weight (free float, restricted by foreign-ownership limits/headroom). That point is missing. FAQ Q5 illustrates it with a 49% investability weight phased in 4.90%/14.70%/31.85%/49.00%. The revision also does not link the point to the segment results in [v3 S4.4], which still says only that "Index weights ... rise with capitalization". v3 describes eligibility screens, not the determination of weights.
- residual_obligation_class: should_fix

### SR7 (should_fix) — verdict: NOT_ADDRESSED

- applied_criterion: precommitted (lighter form)
- verified_by: R2
- evidence_anchor: [v3 S2.3 ¶1] still cites only Dong et al. (2023) for MSCI's China A-share inclusion. The reference-list diff (v2 to v3) adds only Brown & Warner (1985), Cameron et al. (2008) and The Investor (2026a). No stock-level A-share inclusion liquidity study was added.
- change_summary: Section 2.3 wording changed ("weaker" to "thinner"; "and a pre-determined treatment list"), with no new A-share literature.
- residual_gap: n/a (NOT_ADDRESSED)

---

## New issues

### NEW-R2-1 — BSR's UPCoM-to-HOSE listing transfer inside the sample and before the list cut-offs is not disclosed
- description: The sample is described as "common stocks listed on HOSE ... from 1 October 2024" [v3 S3.1 ¶1]. BSR traded on UPCoM until 6 Jan 2025 and moved to HOSE on 17 Jan 2025 [EXT: VietnamPlus, 30 Dec 2024; bsr.com.vn]. data/raw/BSR.csv contains the UPCoM history from 2024 onward, so BSR's pre-announcement baseline mixes two trading venues.
  - This matters for the domain reading of Section 5.2. The venue change occurred after the 31 Dec 2024 cut-off for the November list, which gives a non-liquidity reason for BSR's absence from that list and its later addition.
  - For context, GEE moved from UPCoM to HOSE on 14 Aug 2024, which is before the sample start, so GEE's own series is HOSE-only. Whether FTSE's liquidity-test seasoning rules affected GEE at the Dec 2024 cut-off is CANNOT_VERIFY from the sources checked.
- location_anchor: [v3 S3.1 ¶1]; [v3 S5.2 ¶2–3]; [v3 T9 panels B–C]
- severity: minor. It bounds one of two stocks in a secondary selection argument. Headline constituent and ITT estimates are unaffected, because BSR is excluded from both treatment and control.
- found_by: R2; confidence 4/5; competence basis: Vietnam market-structure knowledge, verified against public listing notices and the raw data file.
- attribution: previously_missed. BSR is in the v2 sample and the v2 near-miss group, and the v2 S5.2 argument ("GEE and BSR ... improved before any report named them") has the same omission. This is anchored in both [v2 S3.1; v2 S5.2 ¶2] and [v3 S3.1; v3 S5.2].
- nearest_roadmap_item: RR6
- non_match_rationale: RR6's criterion concerns stating and framing FTSE's screening cut-off dates. It does not cover the listing-venue history of individual stocks or the sample-construction description. The part of this issue that bears on the RR6 claim is recorded as RR6's residual gap. The venue-mixing in BSR's pre-period series and the undisclosed sample-definition exception are separate.

### NEW-R2-2 — Two-stock clustered inference reported as significant in Table 9 panel B
- description: The "Added Apr 2026, not included: GEE, BSR" row reports stock-clustered SEs and significance stars (W2: −1.666, SE 0.058; the underlying CSV gives p = 3.5e-95). The text cites p = 0.024 for W1. With two treated clusters, conventional clustered inference is not valid. Panel C shows the W1 result is driven by GEE alone. The row should be presented descriptively, or with inference suited to few treated clusters.
- location_anchor: [v3 T9 panel B, row 3]; [v3 S5.2 ¶2] "(p = 0.024)"
- severity: minor
- found_by: R2 (out of the seat's primary competence; flagged for the methodology seat); confidence 4/5.
- attribution: previously_missed. v2 T8 panel B reported the same two-stock row with stars (−1.507***, SE 0.171).
- nearest_roadmap_item: SR2
- non_match_rationale: SR2 asks for a wild cluster bootstrap for the DiD and segment coefficients and for caution on three-stock segments (Tables 5/6 in v2). It does not name the two-stock late-named group in the selection table. v3 applies the caution to the segments [v3 S4.4] but not to Table 9.

### Misrepresented-source check
- No misrepresented institutional source found in Sections 2.1, 3.1, 4.4 or 5.2. Every dated or numbered claim was verified (see the log above).
- Literature in Section 2.3 is unchanged from Round 1 apart from wording, and no new characterisation was introduced to check.
- One minor sourcing note: v3 cites The Investor (2026a, 4 March 2026) as the source for a list that "appeared in November 2025". The claim is supported together with Viet Nam News (13 Nov 2025), and the contemporaneous Investor article is dated 11 Nov 2025. This is not a defect.

### Escalation exceptions / dissents
None.

[EVIDENCE-COMMITTED]

---

## Phase 2B traceability matrix

Inputs added at this phase: ars/stage4_revise/response_to_reviewers_round1.md, read as untrusted author-authored persuasion. The author adjudication sidecar and other seats' Stage 3' files were not read. The Phase 2A verdicts and the new-issue set (NEW-R2-1, NEW-R2-2) are frozen and are reproduced here without change.

| item | obligation | 2A verdict | authors_claim (letter, paraphrased with quoted core) | claim vs manuscript | final verdict | adjustment_id / basis | evidence anchor |
|---|---|---|---|---|---|---|---|
| RR2 | must_fix | FULLY_ADDRESSED | "We rebuilt all groups from the three public lists: 24 constituents, 14 named-but-excluded stocks, 328 never-named controls." Baseline estimates "barely move (-0.392, -0.888, -1.129 vs -0.391, -0.884, -1.120 before)". Naming-timing test covers all 14; new Table A2. | Consistent. The group sizes match [v3 S3.1 ¶2], [v3 T1] and run_summary_revision.txt. The "before" figures match v2 Table 2 col. 1 (-0.391/-0.884/-1.120), and the "after" figures match [v3 T2 col. 1]. [v3 T9] covers all 14 stocks, and [v3 T A2] is present. | FULLY_ADDRESSED | none (no change) | [v3 S3.1 ¶2]; [v3 T2]; [v3 T8]; [v3 T9]; [v3 T A2] |
| RR6 | must_fix | PARTIALLY_ADDRESSED (residual: should_fix) | "Section 5.2 now uses windows keyed to the cut-off: W1 = announcement to 31 December 2025. GEE and BSR became less illiquid by 1.15 log points in W1 (p = 0.024), inside the screened window; the twelve November-named excluded stocks changed by -0.02." | Consistent as far as it goes: the figures match [v3 S5.2 ¶2] and [v3 T9 panel B]. The letter does not address the stock-level split: BSR's W1 change is -0.39 and its -1.68 falls after the cut-off [v3 T9 panel C]. It also does not mention BSR's UPCoM-to-HOSE transfer after the 31 Dec 2024 cut-off. The letter points to no manuscript text that resolves the residual gap. | PARTIALLY_ADDRESSED (residual_obligation_class: should_fix) | none (no change) | [v3 S2.1 ¶2]; [v3 S5.2 ¶2–3]; [v3 T9 panels B–C] |
| SR4 | should_fix | PARTIALLY_ADDRESSED (residual: should_fix) | "Added from FTSE's FAQ: Vietnamese securities screened as non-constituents on liquidity and minimum size, investability weight (free float) used in the liquidity test, foreign headroom screened." Located at S 2.1 para 2 and S 6. | Consistent: the letter describes exactly the sentence found at 2A. It claims nothing about how index weights are set or about the link to the segment results, so the letter supplies no new manuscript evidence. | PARTIALLY_ADDRESSED (residual_obligation_class: should_fix) | none (no change) | [v3 S2.1 ¶2]; [v3 S6 ¶5]; [v3 S4.4 ¶1] (unchanged link) |
| SR7 | should_fix | NOT_ADDRESSED | "Not added: we did not identify a stock-level liquidity study we could verify within this round; adding an unverified reference would violate the paper's citation-verification standard. Dong et al. (2023) remains the cited A-share study. Recorded as a limitation of the literature review." | Partly inconsistent. The non-addition is accurate: no new reference appears in the v2-to-v3 reference diff. The claim that it is "recorded as a limitation of the literature review" cannot be located in v3. The only bounded-search statement, "in a search bounded to Crossref records and the literature cited here" [v3 S2.3 ¶1], is already in v2. It concerns frontier-to-emerging reclassification studies, not A-share liquidity studies. [v3 S6 ¶6] (limitations) does not mention it either. | NOT_ADDRESSED | none (valid_rebuttal assessed and rejected; see below) | [v3 S2.3 ¶1]; [v3 S6 ¶6]; reference list |

### SR7 valid_rebuttal assessment (on the merits)
- The Round-1 finding (R2-W4) was substantive: stock-level liquidity studies of MSCI's China A-share inclusion exist beyond Dong et al. (2023), and a verified addition would strengthen Section 2.3.
- A valid rebuttal must show on the merits that the finding is wrong or does not apply. For example, it could show that no such studies exist, or that they are irrelevant to the paper's argument.
- The authors' reason is a process constraint: "could not verify within this round". It does not dispute that such studies exist, and it does not argue that they are irrelevant.
- The integrity rule the authors invoke is sound. Declining to add an unverified reference is the correct behaviour, and it is recorded here as good practice.
- However, R2-W4 itself required that "any added reference must pass integrity verification". Verification was part of the criterion, not an obstacle to it.
- A process constraint does not rebut the finding. The claimed mitigation (a recorded limitation) is not in the manuscript.
- Result: the rebuttal is not valid. No upgrade is made, and the verdict stays NOT_ADDRESSED.

### Commitment-axis notes (verdict-orthogonal)
- SR7: the letter commits to "recorded as a limitation of the literature review". No manuscript text carries this commitment, so it counts as acknowledgment only / not located. This is recorded for the commitment ledger and does not affect the verdict.

### Adjustment records
None. Every final verdict equals its Phase 2A verdict.

## Post-letter observations
(Decision-inert; seeds for the next round.)

- PLO-R2-1 (SR7): the letter says the omission is "recorded as a limitation of the literature review", but no such statement exists in v3. If SR7 remains unaddressed, the minimal fix is one sentence in Section 2.3 or Section 6 saying that the A-share inclusion literature cited is limited to Dong et al. (2023).
- PLO-R2-2 (RR6): the letter repeats the pooled GEE+BSR W1 figure (1.15, p = 0.024) as evidence that both stocks improved "inside the screened window". This is the same framing that 2A identified as the residual gap, so the author's own account of the change shows the overstatement too. Nothing new is added.
- PLO-R2-3 (letter header): the letter states that the v3 SHA-256 it quotes predates "the final abstract wording edit" and that "the file on disk is authoritative". The orchestrator's input manifest should bind to the on-disk hash of manuscript_v3.md, not the one quoted in the letter.

[MATRIX-COMMITTED]
