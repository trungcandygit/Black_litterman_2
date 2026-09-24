# E6 Claim-Strength Drift — Supplementary Semantic Review, Round 2 (v3 -> v4)

Agent: `integrity_verification_agent`, Stage 4.5 FINAL CHECK, Phase E6 (#569)
Date: 2026-09-24
Detector: semantic, model-mediated (claude-opus-5-5). This is not a deterministic no-drift certificate, and it does not certify complete recall.

## Skill load record

All four files were read verbatim with the Read tool from ARS v3.22.1 at `/tmp/claude-0/-home-user-B-i-FTSE2/88a51032-601f-5b56-b6d6-c6001a62ef1c/scratchpad/academic-research-skills`:

| File | First heading |
|---|---|
| `academic-pipeline/SKILL.md` | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| `academic-pipeline/agents/integrity_verification_agent.md` (§E6 at lines 605-611) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| `academic-pipeline/references/claim_verification_protocol.md` (§E6 at lines 122-204, read in full) | `# Claim Verification Protocol (Phase E)` |
| `shared/references/claim_strength_ladder.md` | `# Claim-Strength Ladder` |

## Scope and boundary

- **Contract artifact.** The contract `claim-strength-drift-findings/1.0` artifact is recorded separately as skipped. Round 1 (v2 -> v3) was a full re-emission outside the patch chain, so no continuous Revision-Evidence Bundle can be built. This file is the supplementary semantic review that the apply report requires (`authorization_witness.unregistered_claim_drift_review_required: true`; `registered_claim_surfaces_checked: 0`; `claim_surface_round2.json` has `surfaces: []`). It is not a schema-valid E6 finding set, and `scripts/claim_strength_drift_disposition.py` cannot bind it. The rows below still need an explicit author disposition (`restore` / `authorize_with_reason` / `pause`) before Stage 5. There is no `proceed open`.
- **Inputs.** The inputs are `ars/stage4prime/authority/revision_patch_round2.json` (patch 1.1, 60 ops, all `claim_strength_changes: []`) and `manuscript_v3.anchored.md`, the pre-round draft. Old text was taken from it by block anchor. The other inputs are `manuscript_v4.md` and `.clean.md`, `roadmap_round2.json` (REV-R2-01..17), `author_adjudication_round2.json` (every `claim_strength_authorizations` is `[]`), `response_to_reviewers_round2.md` and `superseded/revision_patch_round2.first_emission.json`.
- **Authorization rule.** A move counts as authorized only when a roadmap item's description explicitly asks for that strength change. Touching the block is not enough. When the authorizing item is not among the op's `roadmap_item_ids`, the row still counts as AUTHORIZED_MOVE and carries the note "unclaimed". That is a traceability defect, not drift.
- **Evidence standard used for "reliable".** The paper defines the term in B0012, B0044 and B0082: a CAR is reliable only if it is significant at 5% under all four benchmarks (|t| ≥ 1.96). I checked every Table 4 cell (panels A to C) against that rule.

## Table of all 60 ops

Direction: "down" = weaker, more hedged or narrower; "up" = stronger or a qualifier dropped; "—" = no claim move (labels, notes, methods, references, data tables whose significance changes are the authorized re-estimates).

| Op | Block | Roadmap items (claimed) | Moved? / direction | Authorized by | Verdict |
|---|---|---|---|---|---|
| 0 | B0003 (Abstract) | 01, 13 | Yes, down: removed "so the gains do not merely reflect FTSE picking stocks that were already improving"; "Index funds traded the constituents heavily" -> "Trading value surged"; "months before index funds traded" -> "before the first index tranche took effect"; single CARs -> ranges across benchmarks | REV-R2-01 (ITT pre-trend rejects), REV-R2-13 (investor-type), REV-R2-05 (tranche qualifier, unclaimed), REV-R2-03 (ranges, unclaimed) | AUTHORIZED_MOVE |
| 1 | B0007 (Intro ¶1) | 01, 05 | Yes, down: "delivered its liquidity gains months before any index fund traded" -> "raised the liquidity of likely index stocks before the first index tranche took effect"; ITT leads; "the trace of index membership was a one-session trading surge" -> "trading value surged ... for included stocks only" | REV-R2-05, REV-R2-01, REV-R2-13 (index-fund attribution, unclaimed) | AUTHORIZED_MOVE |
| 2 | B0012 (Intro) | 03 | — (adds pre-specified windows and a stricter definition of "reliable") | REV-R2-03 | NO_MOVE |
| 3 | B0013 (Intro, contribution) | 14, 01, 05 | Yes, several. (a) down: list step dropped ("confirmation brought a discrete step ... the constituent list did not"); (b) persistence qualified "under three of four"; (c) "two stocks" -> "GEE"; **(d) up: causal caveat "This last result limits causal readings of the constituent estimates" deleted**; **(e) down: "the rebalancing session raised constituents' trading value" -> "trading value rose"** | (a) REV-R2-08 (unclaimed); (b) REV-R2-03 (unclaimed); (c) REV-R2-06 (unclaimed); (d) none; (e) none | **STRENGTH-DRIFTED** (ADV-E6-1, ADV-E6-2) |
| 4 | B0018 (2.1) | 16, 09 | Yes, new claim: the investability weight scales index weight, "and the passive demand it attracts, therefore rises with its free-float market capitalization" | REV-R2-09 (explicitly requests this explanation) | AUTHORIZED_MOVE |
| 5 | B0025 (2.3) | 11 | Yes, down: A-share literature limitation added | REV-R2-11 | AUTHORIZED_MOVE |
| 6 | B0035 (3.1) | 16, 06 | Yes, down: BSR two-venue caveat added | REV-R2-06 | AUTHORIZED_MOVE |
| 7 | B0044 (3.2) | 03, 04, 15 | — (method: weights, pools, estimation-window exclusions, reliability definition) | REV-R2-03/04/15 | NO_MOVE |
| 8 | B0050 (3.3) | 16, 12, 15 | — (method: matching weights, pool definition) | REV-R2-12/15 | NO_MOVE |
| 9 | B0057 (3.4) | 02 | Yes, down: lower-bound reading "they understate the effect of inclusion" removed; ITT described as an average | REV-R2-02 | AUTHORIZED_MOVE |
| 10 | B0060 (4.1) | 08, 12 | Yes, down: weighted matched announcement estimate added as not significant; "The steps are significant ... supports H2" -> H2 holds for the confirmation only | REV-R2-12, REV-R2-08 | AUTHORIZED_MOVE |
| 11 | B0062 (Table 2) | 12 | Yes, down: re-estimated weighted matched columns, announcement loses significance | REV-R2-12 | AUTHORIZED_MOVE |
| 12 | B0063 (Table 2 notes) | 12 | — | REV-R2-12 | NO_MOVE |
| 13 | B0068 (4.1, Fig. 1 text) | 01 | Yes, down: ITT pre-trend test rejection disclosed (F = 7.59, p < 0.001) | REV-R2-01 | AUTHORIZED_MOVE |
| 14 | B0071 insert (Figure 2) | 01 | — (new figure and note) | REV-R2-01 | NO_MOVE |
| 15 | B0076 (4.2) | 03 | Yes, down: "survive every benchmark" -> the defined reliability test; single-benchmark figures -> ranges; three-day announcement result (1 of 4) and list [-1,+5] result (2 of 4) now disclosed. Checked: the reliability claim is correct for the announcement [-1,+5] and confirmation [-1,+1] windows | REV-R2-03 | AUTHORIZED_MOVE (see numeric observation O-1) |
| 16 | B0079 (Table 4 A) | 03, 04 | — (re-estimated cells) | REV-R2-03/04/12 | NO_MOVE |
| 17 | B0080 (Panel B label) | 03 | — | REV-R2-03 | NO_MOVE |
| 18 | B0081 (Table 4 B, C) | 03, 04 | — (four benchmarks for ITT; new panel C) | REV-R2-03/04 | NO_MOVE |
| 19 | B0082 (Table 4 notes) | 03, 04 | — | REV-R2-03/04 | NO_MOVE |
| 20 | B0083 (4.2) | 03 | Yes, down: persistence qualified "under three of the four benchmarks"; "fits" -> "is consistent with" (same bottom rung) | REV-R2-03 | AUTHORIZED_MOVE |
| 21 | B0084 (4.2, panels B/C) | 03, 14, 01 | Yes. (a) down: "Prices thus responded first to eligibility and then to the likelihood of inclusion" removed; (b) ITT and excluded groups given as ranges with benchmark counts; **(c) up, new claim: the announcement-week gain "reflects characteristics investors could observe, such as size and liquidity, rather than the lists themselves"** | (a) REV-R2-14; (b) REV-R2-03, REV-R2-01; (c) none | **STRENGTH-DRIFTED** (ADV-E6-3) (see also O-2) |
| 22 | B0085 (4.2 Takeaway) | 03 | Yes, qualified: "under every benchmark" (true for the reliable windows); "persisted under three of four"; "later disclosures added little" -> "no reliable price effect" (true under the definition) | REV-R2-03 | AUTHORIZED_MOVE |
| 23 | B0093 (Table 5 notes) | 17 | — (discloses the reference-day design and its 0.62 result) | REV-R2-17 | NO_MOVE |
| 24 | B0094 (4.3) | 05, 13 | Yes, down: "the signature of the price-pressure channel" -> "matches the trading that funds ... had to do"; added "Our data do not identify who traded, so we infer index demand"; "active investors" -> "other investors" | REV-R2-13 | AUTHORIZED_MOVE (numeric O-1) |
| 25 | B0095 (4.3 Takeaway) | 05, 13 | Yes, down: "Index funds concentrated their ... demand" -> "Trading concentrated ... as index demand would imply" | REV-R2-13 | AUTHORIZED_MOVE |
| 26 | B0098 (4.4) | 07 | Yes, down: three-stock segment estimates reported without significance marks and read as descriptive | REV-R2-07 | AUTHORIZED_MOVE (O-4) |
| 27 | B0100 (Table 6) | 07 | Yes, down: significance marks removed for the large and mid segments | REV-R2-07 | AUTHORIZED_MOVE |
| 28 | B0101 (Table 6 notes) | 07 | — | REV-R2-07 | NO_MOVE |
| 29 | B0102 (4.4 Takeaway) | 05, 13 | Yes, down: "Index weight sets the size ... of the liquidity gain" -> the gain "does not rise monotonically across segments"; tranche qualifier. "sets" -> "scales" (same rung) | REV-R2-13 (S4.4 takeaway), REV-R2-05 | AUTHORIZED_MOVE (O-4) |
| 30 | B0114 (Table 8) | 12, 10 | Yes, down: weighted matched-with-trend announcement estimate not significant; drift and sector rows added | REV-R2-12, REV-R2-10, REV-R2-08 | AUTHORIZED_MOVE |
| 31 | B0115 (Table 8 notes) | 12, 10 | — | REV-R2-12/10 | NO_MOVE |
| 32 | B0116 (5.1) | 12 | Yes, down: "all significant at 5%" -> announcement not significant; new hedge "treat it as less certain than the later stages" | REV-R2-12 | AUTHORIZED_MOVE |
| 33 | B0118 (5.1) | 15 | — (the trend is described as fitted over the full sample; "association" kept) | REV-R2-15 | NO_MOVE |
| 34 | B0119 (5.1) | 12, 10 | Yes, down: scope qualifier "unweighted matched sample" added; sector robustness and pre-funding limitation added | REV-R2-12, REV-R2-10 | AUTHORIZED_MOVE |
| 35 | B0122 (5.2) | 06 | Down (excl.-BSR estimates added), but **the retained sentence "Their gains are concentrated in two stocks, and the timing of those gains points to selection" now overstates the evidence in v4 B0123 (BSR improved mostly after the cut-off)** | REV-R2-06 authorizes narrowing the BSR claim, and the narrowing was not carried here | **STRENGTH-DRIFTED** (ADV-E6-4) |
| 36 | B0123 (5.2) | 06 | Yes, down: GEE is the only clear case; BSR's gain came after the cut-off; an alternative (venue) reason is given | REV-R2-06 | AUTHORIZED_MOVE |
| 37 | B0128 (Table 9) | 07, 06 | Yes, down: two-stock row shows point estimates only | REV-R2-07 | AUTHORIZED_MOVE |
| 38 | B0131 (Table 9 notes) | 14, 07, 06 | — | REV-R2-14/07 | NO_MOVE |
| 39 | B0132 (5.2) | 02 | Down: upper/lower-bound reading, the "cannot produce" selection argument and the trend-survival point removed; "at least two" -> "at least one" (REV-R2-06, unclaimed). **Up, new claim: ITT shows "a reliable announcement-week price response under three of four benchmarks"** | Down moves: REV-R2-02, REV-R2-06. "reliable": none; it contradicts the paper's own definition | **STRENGTH-DRIFTED** (ADV-E6-5) |
| 40 | B0133 (5.2 Takeaway) | 02 | Yes, down: "selection does not explain the liquidity response" -> "does not account for the whole liquidity response" | REV-R2-02 | AUTHORIZED_MOVE |
| 41 | B0135 (6 ¶1) | 01, 05 | Yes, down: tranche qualifier; "likely index stocks"; CAR ranges; the list-stage step is now gradual (REV-R2-08, unclaimed). The volatility-control sentence was removed; that deletes supporting evidence but moves no claim's rung | REV-R2-05, REV-R2-01, REV-R2-03/08 (unclaimed) | AUTHORIZED_MOVE (O-5) |
| 42 | B0136 (6) | 13 | Yes, down: "Investors acted on ... index funds ... found prices already adjusted" -> "Prices and liquidity moved with FTSE's public statements" | REV-R2-13 | AUTHORIZED_MOVE |
| 43 | B0137 (6) | 14, 13 | Down: "Investors first priced eligibility and then the likelihood of inclusion" removed; the announcement-week reading is hedged ("which suggests"). **Up: "only the portfolio of stocks that went on to be included gained" -> "only stocks that went on to be included gained" (unit-of-analysis qualifier dropped)** | Down: REV-R2-14. Dropped qualifier: none | **STRENGTH-DRIFTED** (ADV-E6-6) |
| 44 | B0138 (6) | 13 | Yes, down: "redistributed liquidity" -> "shifted liquidity ... relative to the rest of the market" plus the caveat "we do not test whether other stocks lost liquidity in absolute terms" | REV-R2-13 | AUTHORIZED_MOVE (O-4) |
| 45 | B0139 (6) | 02 | Yes, down: upper/lower-bound reading removed | REV-R2-02 | AUTHORIZED_MOVE |
| 46 | B0140 (6, implications) | 13 | Yes, down: "both drawn from a single event"; causal caveat "one event cannot show that earlier communication causes larger gains"; "we do not test whether raising them would change an issuer's outcome" | REV-R2-13 | AUTHORIZED_MOVE |
| 47 | B0141 (6, limits) | 10 | Yes, down: pre-funding and BSR limitations added | REV-R2-10, REV-R2-06 (BSR, unclaimed) | AUTHORIZED_MOVE |
| 48 | B0143 | 16 | — (label A1 -> A.1) | REV-R2-16 | NO_MOVE |
| 49 | B0145 | 12 | — (note on matching weights) | REV-R2-12 | NO_MOVE |
| 50 | B0146 | 16 | — (label) | REV-R2-16 | NO_MOVE |
| 51 | B0155 | 16 | — (AI declaration wording) | REV-R2-16 | NO_MOVE |
| 52 | B0168 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 53 | B0169 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 54 | B0176 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 55 | B0177 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 56 | B0183 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 57 | B0184 | 16 | — (access date) | REV-R2-16 | NO_MOVE |
| 58 | B0185 | 16, 06 | — (access date; new VietnamPlus reference entry) | REV-R2-16, REV-R2-06 | NO_MOVE |
| 59 | B0186 | 16 | — (access date) | REV-R2-16 | NO_MOVE |

Totals: 60 ops. 26 NO_MOVE, 29 AUTHORIZED_MOVE, 5 STRENGTH-DRIFTED (5 ops, 6 findings: ops 3, 21, 35, 39, 43). The label, access-date, notes and method ops (the NO_MOVE rows) carry no claim that moved. Every other op was compared sentence by sentence.

Traceability (not drift): ops 0, 1, 3, 39, 41 and 47 carry strength changes whose authority is a roadmap item the op does not list in `roadmap_item_ids`. The main cases are REV-R2-08 carried into B0013 and B0135, REV-R2-06 into B0013, B0132 and B0141, and REV-R2-03 into B0003 and B0013. The content is what the roadmap asked for, but the op-to-item mapping is incomplete.

## STRENGTH-DRIFTED rows

### ADV-E6-1 — dropped causal caveat (Introduction)
- **Claim location:** B0013, §1 Introduction, contribution paragraph, last sentence (op 3, round 2).
- **Prior -> current:** "This last result **limits causal readings of the constituent estimates** and is the reason we report intention-to-treat effects beside them." -> "This last result is why we report intention-to-treat effects beside the constituent effects." A design-based causal caveat was dropped.
- **Roadmap items claimed:** REV-R2-14, REV-R2-01, REV-R2-05.
- **Direction:** up.
- **Why unauthorized:** no item asks for this caveat to be weakened. REV-R2-01 strengthens the ITT side and REV-R2-02 removes the bound reading, but neither removes the warning that selection limits causal readings of the constituent estimates. v4 B0132 still says "The constituent estimates combine the upgrade's effect with FTSE's selection", so the Introduction now carries less caution than §5.2. (REV-R2-01's evidence anchor quotes the new wording as if it were v3 text. v3 does not contain it.)
- **Recommendation: restore.** For example: "This last result limits causal readings of the constituent estimates and is why we report intention-to-treat effects beside them."

### ADV-E6-2 — causal verb weakened (Introduction)
- **Claim location:** B0013, §1, "Third" finding (op 3, round 2).
- **Prior -> current:** "the rebalancing session **raised** constituents' trading value by 0.79 log points" (causal, affects rung) -> "trading value **rose** by 0.79 log points ... at the rebalancing close" (descriptive).
- **Roadmap items claimed:** REV-R2-14, REV-R2-01, REV-R2-05.
- **Direction:** down.
- **Why unauthorized:** REV-R2-14 covers the table reference ("Tables 5 and 6"), not the verb. REV-R2-13 targets investor-type attribution; this sentence attributes the change to the session, not to an investor type. The ladder treats a silent weakening as drift. The §4.3 heading (untouched) still says "The rebalancing session produced a trading surge".
- **Recommendation: authorize_with_reason** if the author wants the more conservative reading. A reason could be: "descriptive verb consistent with B0094 'Our data do not identify who traded'". Otherwise restore "raised".

### ADV-E6-3 — new interpretive claim above the evidence (§4.2)
- **Claim location:** B0084, §4.2, the paragraph under Table 4 panels B/C (op 21, round 2).
- **Prior -> current:** the prior text said "Prices thus responded first to eligibility and then to the likelihood of inclusion". Removing it is authorized by REV-R2-14. The new text says the announcement-week gain "**reflects** characteristics investors could observe, such as size and liquidity, **rather than** the lists themselves". That attributes the gain to a mechanism (causal, affects/determines rung). The paper does not test size or liquidity as the channel. The parallel Discussion sentence in v4 B0137 puts the same idea at the lowest rung: "which **suggests** that investors used observable size and liquidity to anticipate eligibility".
- **Roadmap items claimed:** REV-R2-03, REV-R2-14, REV-R2-01.
- **Direction:** up (a new claim, stronger than the evidence and than B0137).
- **Why unauthorized:** REV-R2-14 authorizes correcting the eligibility-pricing claim. It does not authorize replacing it with an untested causal attribution.
- **Recommendation: restore to a hedged rung** through revision. For example: "... so the announcement-week gain of stocks that later appeared on the lists cannot reflect the lists themselves; it is consistent with investors anticipating eligibility from observable characteristics such as size and liquidity." That matches B0137.

### ADV-E6-4 — retained selection claim contradicted by this round's BSR evidence (§5.2)
- **Claim location:** B0122, §5.2, first paragraph, last sentence (op 35, round 2; the block was touched and this sentence was kept).
- **Prior -> current:** the sentence is unchanged: "Their gains are concentrated in two stocks, and the timing of those gains **points to selection**." The same round's B0123 now says BSR "improved mostly after the cut-off" and gives "a reason other than liquidity for its later addition". The response letter says "GEE is the single clear case of selection on rising liquidity". B0132 and B0013 were narrowed to "at least one stock" and "GEE".
- **Roadmap items claimed:** REV-R2-06.
- **Direction:** up relative to the v4 evidence. The authorized narrowing to one stock (REV-R2-06: "BSR claim overstated") was not carried into this sentence, so it now asserts selection timing for both stocks.
- **Recommendation: restore consistency** through revision. For example: "Their gains are concentrated in two stocks, GEE and BSR; GEE's timing points to selection, while BSR's gain came mostly after FTSE's cut-off (below)."

### ADV-E6-5 — "reliable" used where the paper's definition is not met (§5.2)
- **Claim location:** B0132, §5.2, selection paragraph, fourth sentence (op 39, round 2).
- **Prior -> current:** the v3 text had no price claim here. In the superseded first emission the new sentence read "a **robust** announcement-week price response under three of four benchmarks". The post-hoc banned-word swap changed it to "a **reliable** announcement-week price response under three of four benchmarks". v4 defines "reliable" in B0012, B0044 and B0082 as significant at 5% under **all four** benchmarks. The ITT announcement-week CAR (Table 4 panel B, [-1,+5]) has t = 3.97, 1.91, 3.72 and 3.75, so the matched benchmark fails. B0084 itself says "significant under three of four benchmarks (the matched benchmark gives t = 1.91)".
- **Roadmap items claimed:** REV-R2-02.
- **Direction:** up. The sentence gives the result the paper's defined top evidential status, which the paper's own table shows it does not have.
- **Why unauthorized:** REV-R2-03 sets the reliability standard and asks for symmetric claims. No item authorizes calling a three-of-four result reliable. The other seven robust -> reliable swaps (B0003, B0012, B0013 twice, B0044, B0076, B0082, B0085) were checked against Table 4, and each is correct under the definition.
- **Recommendation: restore** to wording outside the defined term. For example: "an announcement-week price response significant under three of four benchmarks (Table 4, panel B)".

### ADV-E6-6 — dropped unit-of-analysis qualifier (Discussion; repeated in §4.2)
- **Claim location:** B0137, §6, "how the market learned" paragraph, last sentence (op 43, round 2). The same unqualified wording is newly introduced in B0084 (op 21): "only stocks that went on to be included gained".
- **Prior -> current:** "At the confirmation, only **the portfolio of** stocks that went on to be included gained." -> "At the confirmation, once the preliminary list was public, only stocks that went on to be included gained." The qualifier dropped is the evidence's unit: equal-weighted portfolio CARs, not stock-level gains. The preceding sentence in the same new block keeps "gained **as a group**", so the loss is inconsistent within the block.
- **Roadmap items claimed:** REV-R2-14, REV-R2-13.
- **Direction:** up. It can be read as a stock-by-stock claim. The ITT portfolio, 12 of whose 27 stocks were not included, also gained at the confirmation under three of four benchmarks, so an unqualified stock-level reading is not supported.
- **Recommendation: restore** "the portfolio of" or "as a group" in B0137, and add the same qualifier in B0084.

## Observations outside the E6 verdict (not drift rows; routed to the appropriate phase)

- **O-1 (numeric, #570 / Phase C).** B0076 and B0094 give the effective-date three-day CAR as "between -0.5% and 1.0%". Table 4 panel A shows a maximum of 0.9% (matched, t = 0.88).
- **O-2 (numeric, Phase C).** B0084 says named-but-excluded stocks "gained 2.3% to 6.3% in the announcement week". Table 4 panel C [-1,+5] shows 6.2%, 2.3%, 4.7% and 5.9%, so the maximum is 6.2%.
- **O-3 (untouched block carried forward).** B0064, §4.1, was not touched: "The ITT estimates in Table 3 confirm that the decline is not an artefact of FTSE's later choice." It now sits next to the new disclosure that the ITT joint pre-trend test rejects (B0068). E6 cannot flag an untouched block, but the reviewer or author should decide whether "confirm" still fits.
- **O-4 (heading or claim asserts more than the body; pre-existing and not moved).** The §4.4 heading (B0096, untouched; recorded as an acknowledged limitation in the response letter) says "The gains and the rebalancing surge rise with FTSE size segment", while the body says the liquidity gain is not monotone. B0098 keeps "This supports H4", and B0102 keeps "Index weight scales the rebalancing trade", which was "sets" in v3, the same rung. Both rest on three-stock segment means that B0098 itself calls descriptive. B0138 keeps "suggests that investors weighted their attention by expected index weight" (hedged). None of these is a round-2 move, but the author should consider them.
- **O-5 (conclusion hedge parity).** B0135's "only the confirmation gain lasted" carries no "under three of four benchmarks" qualifier. B0083 and B0085 have it. v3 had the same wording, so this is not a move, but it is asymmetric under REV-R2-03.
- **O-6 (new background attribution; Phase B/C citation-context check).** B0119 says "LSEG (2026) credits the removal of pre-funding requirements for foreign investors for Vietnam's upgrade." This is a new attribution to the 7 April 2026 press release and needs a source-context check. The same applies to the new VietnamPlus (2024) venue dates in B0035 and B0123, and to the FTSE (2026) 49% illustration in B0018.

## Required disposition

The six rows ADV-E6-1..6 close the Stage 4.5 checkpoint until each has an explicit author choice (`restore` / `authorize_with_reason` with a non-blank reason / `pause`). A generic "continue" does not clear them. Any `restore` goes back through revision (patch round 3 or an integrity-correction op), followed by a fresh integrity/E6 pass on the new exact draft. The manuscript was not edited by this review.
