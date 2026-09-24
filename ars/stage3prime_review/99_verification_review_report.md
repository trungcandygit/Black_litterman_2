# Verification Review Report (Stage 3', round 2)

## Judge record
- Five seats (EIC, R1, R2, R3, DA), each a separate subagent with a fresh context, blind to other seats' outputs and to the conversation; same model family (claude-opus / anthropic). Correlated-error disclosure: role separation and fresh contexts do not remove same-family error correlation.
- Three gates per seat: Phase 1 (revision-blind, [CONTRACT-ACKNOWLEDGED]) -> Phase 2A (letter withheld, [EVIDENCE-COMMITTED]) -> Phase 2B (letter revealed, [MATRIX-COMMITTED]). Files: EIC_journal_fit.md, R1_methodology.md, R2_domain.md, R3_perspective.md, DA_devils_advocate.md.
- Contract gap disclosed: manuscript_v3 was produced by full re-emission, not the #390 patch chain, so no Revision-Evidence Bundle exists and `scripts/check_re_review_synthesis.py` cannot run (formally a G0 `manifest_incomplete` condition). The decision below is derived by hand from the committed seat matrices using the protocol's Decision Derivation table; it is not checker-verified. Venue criteria: Finance Research Open guide supplied by the author (ars/venue_criteria_FRO.md) during Stage 3'.

## Decision: Major Revision (reject_recommended: false)

Derivation:
- G0: bundle absent (disclosed above; proceeding by hand under explicit disclosure rather than aborting, because the author asked for the skill to be followed end to end and the gap is structural, not evidential).
- G1: no silent verdict changes; the only 2A->2B change (EIC SR8, MADE_WORSE -> NOT_ADDRESSED) carries ADJ-EIC-1 (scope_correction).
- G2: one dissent (R1 D-SR3-1) on a should_fix item, 1 of 16 routed items, below the ceil(N/3) bound; no must_fix dissent; no escalation exception; no pending state.
- Co-verifier divergence on RR1: R1 grades the residual should_fix, DA grades it must_fix (ITT event study and its rejected pre-trend test unreported; headline still post-selected constituents; bound reading unjustified). No cross-model adjudicator is active, so the stricter grade is kept (fail-closed).
- B3 fires: regression-attributed new issues of severity MAJOR (DA NEW-1 unjustified upper/lower-bound reading; DA NEW-2 asymmetric event-window choice, corroborated by R1 NEW-R1-1 and EIC NEW-1). B4 also fires (RR1 residual must_fix under the fail-closed grade).
- Base decision: Major Revision. No floors from escalation exceptions.

## Revision Response Checklist (final verdicts)

| Item | Class | Verifier(s) | Final verdict | Residual |
|---|---|---|---|---|
| RR1 ITT / selection | must_fix | R1, DA | PARTIALLY_ADDRESSED | must_fix (DA), should_fix (R1) |
| RR2 groups from public lists | must_fix | R2 | FULLY_ADDRESSED | none |
| RR3 portfolio CAR test | must_fix | R1, DA | PARTIALLY (R1) / FULLY (DA) | should_fix: estimation windows contain earlier event windows |
| RR4 benchmarks | must_fix | R1, DA | PARTIALLY_ADDRESSED | should_fix (DA): claims not re-scoped; consider (R1): market-model windows |
| RR5 tranche scope | must_fix | R3, DA | PARTIALLY_ADDRESSED | should_fix: three unqualified statements (Intro lines 13, 25; S 4.2) |
| RR6 FTSE cut-off dates | must_fix | R2 | PARTIALLY_ADDRESSED | should_fix: BSR claim (decline mostly after cut-off; UPCoM->HOSE Jan 2025) |
| SR1 pre-window | should_fix | R1 | FULLY_ADDRESSED | none |
| SR2 wild bootstrap | should_fix | R1 | PARTIALLY_ADDRESSED | should_fix: segment inference |
| SR3 level shifts | should_fix | R1 (dissent D-SR3-1) | PARTIALLY_ADDRESSED | should_fix: post-announcement drift alternative; list step not robust |
| SR4 free float / foreign headroom | should_fix | R2 | PARTIALLY_ADDRESSED | should_fix: weights -> passive demand -> segments |
| SR5 cost of capital | should_fix | R3 | FULLY_ADDRESSED | none |
| SR6 alternatives | should_fix | DA | PARTIALLY_ADDRESSED | should_fix: pre-funding removal, sector composition |
| SR7 A-share literature | should_fix | R2 | NOT_ADDRESSED | letter's "recorded as limitation" not in manuscript |
| SR8 abstract length | should_fix | EIC | NOT_ADDRESSED at review time; resolved by venue guide (limit 250; v3 has 209) | none after venue guide |
| EIC-W1 contribution vs ITT prices | (round-1 finding) | EIC | PARTIALLY_ADDRESSED | should_fix |
| EIC-W2 labels | (round-1 finding) | EIC | PARTIALLY_ADDRESSED | consider |

should_fix_addressed_rate = 3 of 8 addressed-or-partial... computed on final verdicts: FULLY or PARTIALLY for SR1, SR2, SR3, SR4, SR5, SR6 = 6 of 8 = 75% (< 80%, B5 would also fire).

## New issues (frozen at 2A)

| ID | Seat | Severity | Attribution | Summary |
|---|---|---|---|---|
| DA NEW-1 | DA | MAJOR | regression | "constituents = upper bound, ITT = lower bound" not justified (sign of selection bias, different populations, shared parallel-trends assumption) |
| DA NEW-2 | DA | MAJOR | regression | asymmetric event-window choice (announcement on [-1,+5], list null on [-1,+1]) |
| DA NEW-3 | DA | MAJOR | previously_missed | "disclosure-date reactions cannot come from gradual selection" does not follow |
| DA NEW-4 | DA | minor | regression | abstract says index funds traded; investor type unobserved |
| DA NEW-5 | DA | minor | previously_missed | S 4.4 takeaway contradicts non-monotone segment ordering |
| R1 NEW-R1-1 | R1 | minor | regression | uneven window choice (corroborates DA NEW-2) |
| R1 NEW-R1-2 | R1 | minor | previously_missed | matched estimates ignore MatchIt weights |
| R1 NEW-R1-3 | R1 | minor | previously_missed | two-stock group reported with clustered p-values |
| R1 NEW-R1-4 | R1 | minor | indeterminate | "pre-period trend" wording; two different top-tercile pools described identically |
| R2 NEW-R2-1 | R2 | minor | previously_missed | BSR series mixes UPCoM and HOSE before 17 Jan 2025 |
| R2 NEW-R2-2 | R2 | minor | previously_missed | same as R1 NEW-R1-3 |
| R3 NEW-R3-1 | R3 | minor | regression | "redistributed liquidity" lost its relative definition |
| R3 NEW-R3-2 | R3 | minor | regression | abstract index-fund sentence (same as DA NEW-4) |
| R3 NEW-R3-3/4 | R3 | minor | previously_missed | regulator and issuer advice outruns single-event evidence |
| R3 NEW-R3-5 | R3 | minor | previously_missed | "months before index funds traded" ignores tranche and bound caveats |
| EIC NEW-1 | EIC | minor | regression | window choice (same as DA NEW-2) |
| EIC NEW-2 | EIC | minor | regression | Intro cites Table 5 for segments (now Table 6) |
| EIC NEW-3 | EIC | minor | previously_missed | S 4.4 heading "rise with segment" vs non-monotone ordering |
| EIC NEW-4 | EIC | minor | regression | "investors first priced eligibility" before any list was public |
| EIC NEW-5 | EIC | minor | regression | Table 9 panel A note vs Table 2 column identity |
| EIC NEW-6 | EIC | minor | previously_missed | declaration placeholders |

## Stage 4' roadmap (next immutable roadmap, source-traced)

Must address:
- R2-M1 (RR1 residual, DA NEW-1, DA NEW-3, EIC-W1): report the ITT event study and its pre-trend test in the manuscript; put ITT beside constituent estimates in Abstract and Introduction; state the ITT confirmation CAR is not significant at 5%; replace the upper/lower-bound language with an explicit, assumption-stated comparison or drop it; fix the "cannot come from gradual selection" sentence.
- R2-M2 (DA NEW-2, R1 NEW-R1-1, EIC NEW-1, RR4 residual): pre-specify the same windows for every event, report all, and base claims symmetrically; say where [-1,+1] is not robust; headline magnitudes by the range across benchmarks, not the equal-weighted figure.
- R2-M3 (RR3/RR4 residual, R1): re-estimate portfolio test and market-model betas on estimation windows that exclude earlier event windows.

Should address: RR5 residual (three sentences); RR6 residual and R2 NEW-R2-1 (BSR); SR2 (segment inference: drop stars or bootstrap); SR3 (post-announcement drift test, soften list step); SR4; SR6; SR7 (limitation sentence or verified reference); R1 NEW-R1-2 (matching weights); two-stock inference (R1 NEW-R1-3/R2 NEW-R2-2); R3 NEW-R3-1..5; DA NEW-4/5; EIC NEW-2..5; rebalancing design-change note (R1 PLO-1); method-text fixes (R1 NEW-R1-4); venue items V5, V9, V11, V12 (ars/venue_criteria_FRO.md); letter corrections (hash note; SR7 claim).

Per the pipeline state machine, Stage 4' is the last revision round; items not resolved there become Acknowledged Limitations and the pipeline proceeds to Stage 4.5 without another review.
