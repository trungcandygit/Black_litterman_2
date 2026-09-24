# Stage 4.5 FINAL INTEGRITY: re-verification of integrity-correction round 5 (v8 -> v9)

This is a Final Verification (Mode 2, final-check). It covers every block changed in round 5 (81 `replace_block` ops, 81 of 193 blocks). The verifier did not write the edits.
Date: 2026-09-24. Model: claude-opus-5-5, single-model (`ARS_CROSS_MODEL` is not set).

## Verdict: **PASS WITH NOTES**

| Count | Result |
|---|---|
| IL-SERIOUS | 0 |
| IL-MEDIUM | 0 |
| IL-MINOR | 6 |
| MAJOR_DISTORTION | 0 |
| UNVERIFIABLE | 0 |

- **Round-4 items.** All nine round-4 issues (IL-MEDIUM-1, IL-MEDIUM-2 and IL-MINOR-1..7) are resolved. All seven round-4 E6 rows (ADV-E6-1..7) were restored.
- **New E6 rows.** Two new E6 rows exist, one moving the claim up (ADV-E6-1) and one moving it down (ADV-E6-2). E6 rows do not count toward the verdict. They do close the checkpoint until each row has a disposition.
- **Stage 5 gate.**
  - The pipeline state machine (`SKILL.md`, item 8) sends Stage 4.5 to Stage 5 only on a "PASS (zero issues)".
  - The six MINOR items are one-line fixes, and none changes an estimate.
  - Under the standing author decision (fix, never override), the recommended route is:
    1. Correction round 6 fixes IL-MINOR-1..6 and restores ADV-E6-1.
    2. A targeted re-verification of the touched blocks follows.
    3. After that, Stage 5 entry.

## Skill load record

Before any other work, all five files were read in full with the Read tool. `integrity_verification_agent.md` has 887 lines and was read in two pages.

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
| Base: correction_round5/manuscript_v8.md | 4d36bbde9133c6a49d83c8ca157c202ef9c9aa1ebaa452b10557ff98ef80aeb7 |
| Revised: correction_round5/manuscript_v9.md | d23b6ff6ecee983ed197ec8b797d9c7e5d96d71f09f90d7a7e12384693a25385 |
| Revised clean: manuscript_v9.clean.md (byte-identical to v9_preview.clean.md) | d0b8fd66f1eb44cdd1edbf175cf715c53d89fa42edff97946ae93a9942e79f97 |
| Patch: integrity_patch_round5.json (81 ops; roadmap items IL-MEDIUM-1, IL-MEDIUM-2, IL-MINOR-1..4) | 8272f6e2a68a717c507b8011f17057dc0fcba94bef885fc25e48cb5c782f305c |
| E1 registry: claim_registry_v9.json (built with build_claim_registry.py; 234 claims; tier ALL) | 415b98a879ebaaf4d13742d462f6fd250f8426d287e0deb9e0fd770ca8d6fc9d |
| E1.1 coverage: claim_registry_coverage_v9.json (`--validate-report` replay: PASS) | 44c5de1f6b5a351765d2b10226c991c25b1a8165167979feba6e14f5a2d9d7c3 |

**E1.1 coverage.**
- Status: `completed`. There are 60 candidates, of which 2 are `candidate_unregistered`.
- The 2 unregistered candidates are the same two "Accessed 24 September 2026" URL lines as in v7 and v8 (The Investor 2026a and 2026b, in the reference list). Neither is a claim.
- `semantic_extraction_coverage`: `not_machine_detectable`.

**Unchanged analysis.** No `code/*.R` file and no `output/*.csv` changed after v8. Every number was checked against the same result files as in round 4.

**Rendered submission.**
- `submission/manuscript_anonymized.md` equals v9.clean, apart from typographic minus signs.
- `ars/stage5_finalize/work/checks.json` binds the v9.clean SHA.
- The LaTeX log has two overfull boxes of 2.0 pt and 1.0 pt: a page-output box, and the header of Table A.2. Both are negligible.
- Pages 11, 12 and 15 of the PDF were rendered and inspected. Eqs. (2)–(4), (6) and (9) set within the margins, and the aligned splits render correctly.

**Author event labels.**
- `author_events_round5.md` holds AUTHOR-EVENT-r5-final and AUTHOR-EVENT-r5-notes.
- IL-MINOR-4 of the correction list also cites "AUTHOR-EVENT-r5-venue". That label has no entry in the events file, although the authorization binds IL-MINOR-4 to the r5 events that do exist.
- This is a traceability note for the orchestrator. It is not a manuscript issue.

## 1. Resolution of reverify_round4 issues and E6 rows

| Item | Block | Status | v9 evidence (quoted) |
|---|---|---|---|
| IL-MEDIUM-1 | B0013 | RESOLVED | "First, the illiquidity of the ITT group fell by 0.27, 0.55 and 0.81 log points across the three windows, about two thirds of the constituent declines; for constituents, the confirmation brought a discrete step beyond a gradual post-announcement drift, and the constituent list did not (Section 4.1)." The pointer "(Tables 2 and 3)" became "(Section 4.1)" to meet the venue rule. Section 4.1 holds both tables and the drift test. |
| IL-MEDIUM-2 | B0018 | RESOLVED | "FTSE applies liquidity, minimum-size and foreign-headroom screens, and in the liquidity test it uses the investability weight of each security … (FTSE Russell, 2026) … A security with a 49% investability weight thus enters at 4.9% after the first tranche (10% of 49%)". The arithmetic marker is back, and "thus" marks the example as the authors' own calculation. |
| IL-MINOR-1 | B0094 | RESOLVED | "Harris and Gurel (1986), by contrast, find price rises immediately after S&P 500 additions are announced, which they attribute to index-fund buying pressure." |
| IL-MINOR-2 | B0024 | RESOLVED | "its stock prices move sharply in the direction implied by the new benchmark before implementation" |
| IL-MINOR-3 | B0203 | RESOLVED | "the 110 never-named stocks in the top tercile of pre-period trading value among never-named stocks". This matches `top_ctrl` in the code. |
| IL-MINOR-4 | B0200, B0208 | RESOLVED | Eq. (4) reads "$\mathrm{TV}_{iw} = \ln(\sum \mathrm{VAL}_{it} + 10^{-6})$" and Eq. (9) reads "$\ln(\mathrm{VAL}_{it} + 10^{-6})$". Both match analysis.R lines 59, 136 and 191. |
| IL-MINOR-5 | B0112 | RESOLVED | "… where they are about half as large (the ITT row compares with Table 3)." |
| IL-MINOR-6 | B0107 | RESOLVED | Headers now read "(4) CS spread, volatility control" and "(5) Amihud, volatility control". |
| IL-MINOR-7 | output/TABLE_SOURCE_MAP.md | RESOLVED | Table 7 lists all three source files. Table A.3 has its own row. The named-but-excluded CARs appear under Table 4 and t4b under Table 5. Numbering follows v9 (A.1 lists, A.2 tA1_balance.csv, A.3 t8c). |
| ADV-E6-1 | B0003 | RESTORED | "The liquidity and price responses came with FTSE's disclosures, before index funds had to buy." |
| ADV-E6-2 | B0060 | RESTORED, and lower than the recommended fix | "… months before the 18 September rebalancing". This states a verifiable timing fact instead of investor behaviour. |
| ADV-E6-3 | B0013 | RESTORED | Restored through IL-MEDIUM-1 (see above). |
| ADV-E6-4 | B0098 | RESTORED | "…, consistent with H4, although the two upper segments contain three stocks each." |
| ADV-E6-5 | B0135 | RESTORED | "and only the confirmation gain lasted, under three of four benchmarks." |
| ADV-E6-6 | B0132 | RESTORED (substance) | "We report both sets of estimates and treat neither as a bound on the other." The explanatory clause ("combine … with FTSE's selection; … average …") is carried by the block's preceding sentences and by B0064. |
| ADV-E6-7 | B0024 | RESTORED | "(Dong et al., 2023); beyond that study, we did not locate a stock-level study of liquidity around the China A-share inclusion." |

## 2. Phase A and Phase B

**Phase A.**
- Round 5 changed no reference entry.
- All 33 references keep their earlier fresh verdicts: `phaseAB_group1-3.md`, plus Burnham et al. (2018) from `reverify_round1.md`.
- A3 on v9: every one of the 33 entries is cited in the body. There are 0 orphan references and 0 dangling citations. Cameron et al. (2008) is now cited in B0050 because the note of Table 8 was cut.

**Phase B.** All 100% of the changed sentences that cite a source were checked against the verified evidence text in phaseAB_group1-3 and reverify_round1/4, plus one WebSearch for Hegde and McDermott.

| # | Block | Source | v9 context | Verified source text | Verdict |
|---|---|---|---|---|---|
| B1 | B0009 | Biktimirov & Afego 2026 | "In frontier markets, index additions raise prices persistently, and Biktimirov and Afego (2026) attribute the gains to institutional demand." | "persistent stock price increases … consistent with institutional investor demand as the underlying mechanism" (B4-1) | SUPPORTED |
| B2 | B0024 | Biktimirov & Afego 2026 | "find persistent price gains for additions and distinct return and trading-volume responses when a country changes class, and they trace the gains to institutional demand rather than to trading pressure or liquidity" | "Country reclassification events exhibit distinct return and volume effects"; "rather than temporary trading pressure or liquidity effects" | SUPPORTED in content. Paraphrase distance regressed (see Phase D and IL-MINOR-6). |
| B3 | B0083 | Biktimirov & Afego 2026 | "persistent gains of frontier-market index additions" | B4-1 | SUPPORTED (unchanged) |
| B4 | B0136 | Biktimirov & Afego 2026 | "index effects reflect investor demand rather than liquidity alone" | B4-3 | SUPPORTED. Stop-slop O-6 points out that this wording differs from B0024. The difference is not a distortion, because this wording is the weaker one. |
| B5 | B0013 | Biktimirov & Afego 2026 | "unlike Biktimirov and Afego (2026) we follow liquidity stage by stage within one market" | multi-country price study | SUPPORTED |
| B6 | B0024 | Burnham et al. 2018 | "move sharply in the direction implied by the new benchmark before implementation and give back most of that move in the following year" | "reclassified markets' prices substantially overshoot between the announcement date and the effective date … but largely revert within a year"; "prices fall when a market moves from an index with more benchmarked ownership to one with less … and vice versa" | SUPPORTED |
| B7 | B0009, B0083 | Burnham et al. 2018 | country-level flows or indices; "reversal within a year … at the country level" | same | SUPPORTED |
| B8 | B0083 | Harris & Gurel 1986 | "S&P 500 additions gained more than 3% on the announcement, and the gain was almost fully reversed after two weeks" | "prices increase by more than 3 percent, and this increase is nearly fully reversed after 2 weeks" | SUPPORTED |
| B9 | B0094 | Harris & Gurel 1986 | "find price rises immediately after S&P 500 additions are announced, which they attribute to index-fund buying pressure" | "immediately after an addition is announced …"; the title reports price pressures | SUPPORTED. "By contrast" now links an announcement-time finding to a non-response on the Vietnamese effective date. The contrast is loose but not misattributed. |
| B10 | B0021 | Harris & Gurel; Shleifer; Chen et al. | as in v8, split into three sentences | earlier verdicts | SUPPORTED |
| B11 | B0021 | Hegde & McDermott 2003 | "attribute the persistent liquidity gains of S&P 500 additions mainly to lower direct trading costs" | "due primarily to a decrease in the direct cost of transacting" (WebSearch 2026-09-24, ScienceDirect abstract) | SUPPORTED |
| B12 | B0009, B0060, B0105, B0136 | Hegde & McDermott 2003 | spreads and activity persistently; sustained increase; "whose liquidity gain came mainly through lower direct trading costs" | same | SUPPORTED |
| B13 | B0024 | Dong et al. 2023 | as in v8, plus the restored scope clause | B8/B9 of round 4 | SUPPORTED |
| B14 | B0076 | Dong et al. 2023 | unchanged sentence | same | SUPPORTED |
| B15 | B0018 | FTSE Russell 2026 (FAQ); FTSE Russell n.d.; press | screens and liquidity-test weight; the tranche arithmetic is the authors' own | R13 fact table: "assessed for liquidity using its 49% investability weight"; "for all the eligibility screens such as liquidity and minimum size"; investability weight is "the more restrictive of free float and any applicable foreign ownership restriction" | SUPPORTED |
| B16 | B0094, B0097 | Raddatz et al. 2017 | "two stages … announcement and implementation"; "suggest the same ordering for the persistent liquidity effect" | Phase B contexts; the country-to-stock extension is already a MINOR note | SUPPORTED |
| B17 | B0050 | Cameron et al. 2008 | "wild cluster bootstrap with restricted residuals, Rademacher weights and 999 draws (Cameron et al., 2008)" | wild cluster bootstrap-t with the null imposed and Rademacher weights (earlier verdict). The 999 draws are the authors' setting, and code line 153 has `B = 999`. | SUPPORTED |
| B18 | B0049 | Roth et al. 2023 | monthly event study | earlier verdict | SUPPORTED |
| B19 | B0025 | Bekaert et al. 2007; Stereńczak et al. 2020; Nguyen et al. 2021 | split sentences; the uncited retail-investor claim is removed | earlier verdicts | SUPPORTED |
| B20 | B0012, B0203 | Brown & Warner 1985 | portfolio test for common event dates | earlier verdict (UNVERIFIABLE_ACCESS for the full text) | SUPPORTED / UNVERIFIABLE_ACCESS as before |
| B21 | B0054, B0192 | FTSE Russell 2018; LSEG 2025/2026 | unchanged content | earlier verdicts | SUPPORTED |
| B22 | B0035, B0123 | VietnamPlus 2024 | "which provides a reason other than liquidity" | earlier verdict | SUPPORTED |
| B23 | B0132 | Becker-Blease & Paul 2006 | unchanged | round-4 B12 | SUPPORTED |
| B24 | B0104 | Amihud 2002 | definition | earlier verdict | SUPPORTED |
| B25 | B0105, B0043 | Corwin & Schultz 2012; Kang & Zhang 2014 | unchanged | earlier verdicts | SUPPORTED |
| B26 | B0050 | Ho et al. 2007; Callaway & Sant'Anna 2021 | unchanged | earlier verdicts | SUPPORTED |

Phase B totals: 0 MAJOR_DISTORTION, 0 UNVERIFIABLE and 0 MINOR_DISTORTION. The Brown & Warner full text stays UNVERIFIABLE_ACCESS, which is a note and not an issue.

**Paraphrase distance.**
- **Burnham et al.** The v9 sentence shares only "prices" and "year" with the abstract. The overshoot-and-revert structure is re-expressed. PARAPHRASE, and the distance is adequate.
- **Biktimirov & Afego.** Stop-slop F-12 changed "separate" back to "distinct". The clause now reads "distinct return and trading-volume responses", against the source's "distinct return and volume effects": four of the five source words appear in order.
  - The passage still follows the abstract's order: data, additions, reclassification, mechanism.
  - This undoes part of the round-1 fix for a CLOSE_MATCH (IL-MEDIUM-12 there).
  - Grade: PARAPHRASE (borderline), recorded as IL-MINOR-6.

## 3. Phase C: numbers, tables, cross-references and venue order

| Item | Source file(s) | Result |
|---|---|---|
| All table cells in changed table blocks (B0066, B0100, B0107, B0114, B0128, B0144/B0147, B0212) | same CSVs as round 4 | A script diff of every numeric token between v8 and v9 found no cell value changed. The only removals are the Table 3 observation column (34,666 and 35,752), "2026" in a row label, and "352 clusters" in the Table 8 bootstrap row. Table A.2 (v9 B0147) equals v8 Table A.1 (B0144) token for token. |
| Numbers added in text (token-conservation ADV-REV-1..38) | code; CSVs | 999 draws (analysis_revision.R line 153); m from -13 to 11 with the week of 30 September 2024 (analysis.R line 71 gives relm = -13 for the week starting Monday 30 Sep 2024; t_event_study.csv holds relm -13..11); 10^-6 (analysis.R lines 59 and 136); 18 September; section pointers 3.2, 3.3, 4.1–4.4, 5.1, 5.2. All are correct. |
| S1–S3 (B0123) | analysis_revision.R lines 102–104 | W1 = week ≥ 7 Oct 2025 and ≤ 31 Dec 2025; W2 = after 31 Dec and before 7 Apr 2026; W3 = on or after 7 Apr 2026; weeks are keyed on their Monday start date. This matches "S1 from 7 October to 31 December 2025 … S2 from 1 January to 6 April 2026; and S3 from 7 April 2026", "assigning weeks by their start date". |
| B0141 / B0076 "two sessions after the effective date" | data end 23 Sep 2026 (Wednesday); effective date 21 Sep | The two sessions are 22 and 23 September. Correct. This fixes v8's "three trading days". |
| B0192 sector counts | analysis_revision2.R lines 29–31 | 8 banks and 5 brokers among the constituents make 13 of 24, leaving 11. VCB, STB, SHB and EIB plus SSI, VCI, VIX and VND make 8 of the 27 ITT stocks, leaving 19. "Which also include EIB" is correct. |
| **B0068 "largest three and two months before it (0.33 and 0.23)"** | output/revision/t_event_study.csv (constituent, lamihud) | **Incorrect ordinal.** The pre-period coefficients are 0.329 at m = -3, **0.248 at m = -6 (April 2025)** and 0.232 at m = -2. The 0.23 value is the third largest, not the second. Stop-slop F-32 introduced this by replacing "most clearly". The same error class ("largest positive deviations") was corrected in an earlier round. See IL-MINOR-1. |
| Cross-references | v9 | Every table, column, panel, section, equation and appendix-table pointer resolves. Checked: A.1 (lists) in §2.1 and §3.1; A.2 (balance) in §3.3; A.3 (stock-level) in §5.2; B0210 appendix lead-in; Table 2 columns 1–3; Table 7 columns 1–5; Table 9 panels A–B; Figure 1 panels A–B; "Section 3.2" benchmarks in the Table 4 note; "Sections 3.3 and 5.1" in the Table 8 note; "Section 4.1" in B0192 (placebo centre -0.21); "Section 5.2" in B0035. |
| **Venue rule: tables numbered in order of first citation** | v9, in reading order | **PASS.** The first citations run: Table A.1 (line 33), Table 1 (67), Table A.2 (121), Table 2 (139), Table 3 (152), Figure 1 (166), Figure 2 (166), Table 4 (186), Table 5 (228), Table 6 (246), Table 7 (262), Table 8 (282), Table 9 (316), Table A.3 (318). Both the main series and the appendix series are in order. The introduction no longer cites any table. |

Phase C result: 1 data-description error (B0068) and 0 numeric mismatches.

## 4. Equations (2)–(9) against the R code

| Eq. | v9 | Code | Result |
|---|---|---|---|
| (2) | φ = sum of squared log H/L over days t−1 and t; ψ = squared log of the two-day max H over the two-day min L | analysis.R lines 35–37: `hl = log(high/low)^2`, `beta_cs = hl + shift(hl)`, `gamma_cs = log(h2/l2)^2` | Match. The renaming to φ and ψ removes the clash with α_i and β_k. |
| (3) | η = (√(2φ) − √φ)/(3 − 2√2) − √(ψ/(3 − 2√2)); S = max{0, 2(e^η − 1)/(1 + e^η)} | lines 38–40: `k`, `alpha_cs`, `cs_spread = pmax(0, …)` | Match |
| (4) | Amihud = ln(mean ILLIQ); TV = ln(ΣVAL + 10^−6); Vol = ln(mean \|R\|) | line 59 onward: `lval = log(sum(value_bn) + 1e-6)`; filter `ndays >= 3 & amihud > 0` | Match |
| (5) | unchanged | revision2 `car_port2` | Match |
| (6) | trading-day index s relative to the disclosure (s = 0); AR_ps = mean over g; CAR = Σ_{s=τ1}^{τ2}; t = CAR/(σ̂_p√D); τ1, τ2 and D defined | portfolio mean by date; `sum`; `s_est*sqrt(L)`; est_days = −130..−11 minus the windows of earlier events | Match. Using AR_is in Eq. (6), with AR_it defined in Eq. (5), is consistent with the stated re-indexing. |
| (7) | unchanged | `feols(... treated:P1+P2+P3 | symbol + week, cluster = ~symbol)` | Match |
| (8) | M_mw = 1 if week w **starts** in month m; m from −13 (week of 30 Sep 2024) to 11; m = −1 omitted | `relm = (year(week) − 2025)*12 + month(week) − 10`, with `week` the Monday date; `ref = −1`; the CSV spans −13..11 | Match |
| Drift / trend | unchanged | `tpost`, `tindex` | Match |
| (9) | ln(VAL_it + 10^−6) = α_i + λ_t + θ1 C×Reb_t + θ2 C×Eff_t + u_it; λ_t, Reb, Eff and u defined | analysis_revision.R lines 255–256: `lval_d = log(value_bn + 1e-6)`, `treated:s0 + treated:s1 | symbol + date` | Match |
| Bootstrap text (B0050) | restricted residuals, Rademacher weights, 999 draws | `wcb()`: the column under test is dropped to impose the null (WCR), `sample(c(-1, 1))`, `B = 999` | Match |

## 5. E6 claim-strength drift (v8 -> v9, changed blocks)

**Roadmap authority for strength changes in round 5:**
- IL-MINOR-1 authorizes restoring the v7 rung for ADV-E6-1..7.
- IL-MINOR-3 authorizes stop-slop O-1..O-4, O-6 and O-7 as downward moves. It also covers F-26, which the audit had flagged as a possible claim change.
- IL-MINOR-2 authorizes the proofreading corrections, including the H3 linkage and the correction to "two sessions".
- No item authorizes an upward move.
- The authorized list leaves out O-5.

**`STRENGTH-DRIFTED` rows.** These close the checkpoint, and each row needs `restore`, `authorize_with_reason` or `pause`.

| ID | Round | Claim location | Prior rung -> current rung (or dropped qualifier) | Roadmap items the op claimed | Direction |
|---|---|---|---|---|---|
| ADV-E6-1 | 5 | B0136, §6 ¶2, first sentence | v8: "prices and liquidity moved with FTSE's public statements, and the first-tranche rebalancing left no reliable price effect". The non-response was limited to prices. v9: "prices and liquidity moved with FTSE's public statements **rather than with the first-tranche rebalancing**". This extends the non-response to liquidity, which contradicts the 0.79 log-point trading surge at the rebalancing close (Table 5; B0087, B0135). The paper defines liquidity as price impact and trading activity (B0105). Stop-slop F-4 is the origin, and it was marked "no claim change". | IL-MINOR-2, IL-MINOR-3, IL-MINOR-4 | up |
| ADV-E6-2 | 5 | B0025, §2.3 ¶2 | Removed: "Where domestic retail investors dominate turnover, benchmark-tracking foreign money changes the investor base more than an S&P 500 addition does." This was an uncited comparative claim, stop-slop O-5, which the authorized list omits. | IL-MINOR-2, IL-MINOR-3, IL-MINOR-4 | down |

Recommendations:
- **ADV-E6-1:** `restore`. Use the text given under IL-MINOR-2.
- **ADV-E6-2:** `authorize_with_reason`. Suggested reason: "The removed sentence was an uncited comparative claim, and removing it matches the evidence."

**Moves recorded and closed.** Each is authorized, and each was checked against the evidence.
- **O-1, B0007.** "at each step" became "from the announcement … onward". This is consistent with B0060: there is no discrete step at the list (0.10, *p* = 0.40), and the announcement effects are significant in the full sample and for the ITT group.
- **O-2, B0135.** "brought … at" became "came with". The wording is no longer causal, consistent with B0013 and B0132.
- **O-3 and O-4, B0094.**
  - "they bought" became "they were to buy". Per FTSE Russell (2026) and VIR (2026), implementation was at the close of 18 September.
  - "Prices did not respond" became "Prices showed no reliable change". The effective-date CAR lies between -0.5% and 0.9% and is never significant.
- **O-6, B0136.** "demand and liquidity moved together" became "prices and liquidity moved together". Prices and liquidity are observed, and the investor type is not (B0141).
- **O-7, B0138.** "revise" became "qualify", and "diluted" became "could have diluted". There is no re-estimate of the index-level result.
- **F-26, B0136.** The general claim about a "frontier-to-emerging upgrade" was narrowed to "the Vietnamese upgrade … FTSE announced it months in advance". Down, and consistent with the evidence.
- **B0094.** New clause: "and with the second half of H3". This is a proofreading item (IL-MINOR-2). It sits at the "consistent with" rung, and the effective-date CAR is not significant, so it is supported.
- **B0060.** The round-4 ADV-E6-2 restore landed below the recommended wording ("months before the 18 September rebalancing"). Down.
- **Compaction of repeated facts (IL-MINOR-3), neutral:**
  - B0009 drops "rather than trading pressure or liquidity changes"; the full contrast is kept in B0024.
  - B0122 drops "GEE, whose timing points to selection …"; this is kept in B0123 and B0132.
  - B0192 replaces "(-0.21 against -1.13)" with "(Section 4.1)"; the numbers remain in §4.1 and §6.
- **B0010.** "; we also drop" became "We therefore drop" (stop-slop F-6). This is a design connector, not a change in claim strength. Excluding named stocks keeps stocks that were themselves screened on liquidity out of the comparison group, which is coherent with the sentence before it. Note only.

**Stop-slop moves checked against the evidence.** None of O-1 to O-7 contradicts the evidence:
- O-1 to O-4, O-6 and O-7 are covered in the list above.
- O-5 is ADV-E6-2.
- O-8 is applied: the Figure 1 note now names panels A and B.

**Deleted limitations and caveats.**
- All five §6 limitations are kept in B0141: survivorship; data ending two sessions after the effective date with only the first tranche; investor type; the pre-funding reform; the BSR venue and press-reported lists.
- The §5.1 caveat on the announcement stage is kept in B0116, which is unchanged.
- Nothing else of this kind was removed.

**E6 contract note.** As in earlier rounds, the rows are rendered here. The `claim-strength-drift-findings/1.0` companion and the disposition sidecar belong to the orchestrator and author step.

## 6. Table and figure notes: interpretability after compaction

Each note is now one sentence plus the source line. A table was checked as interpretable if its stars, units, abbreviations, control group and window definitions can be recovered from the note, or from a pointer in the note.

| Item | Stars defined or referenced | Other checks | Status |
|---|---|---|---|
| Table 1 | no stars | Amihud via Eq. (1), whose text gives VND billion; CS via Eqs. (2)–(3) | OK |
| Table 2 | defined ("\*, \*\*, \*\*\* denote significance at 5%, 1% and 0.1%") | clustering, FE, matching weights | OK |
| Table 3 | "other details are as in Table 2" | The v8 note stated that the split rows use never-named, never-included controls. v9 dropped this, and the text does not give it. analysis_revision.R line 74 uses `itt == 1 | never == 1`. | IL-MINOR-3 |
| Figure 1 | n/a | Panels are named. The named-but-excluded series comes from Eq. (8) augmented with `i(relm, named)` (analysis_revision.R line 84). v8's note said so; v9's does not, and Eq. (8) has only Constituent. | IL-MINOR-3 |
| Figure 2 | n/a | The comparison group is never-named, never-included stocks (line 77). v8 said so; v9 does not. The default ITT specification in B0049 uses all other stocks, so a reader would assume the wrong group. | IL-MINOR-3 |
| Table 4 | no stars | percent, trading-day windows, portfolio *t*, benchmarks via Section 3.2 | OK |
| Table 5 | "other details as in Table 2" | | OK |
| **Table 6** | **stars in the Small column; no definition and no Table 2 reference** | The note says marks are omitted for the three-stock segments, but the last row also has no marks for the 18-stock segment (0.645, SE 0.150). This was already flagged at proofreading. | IL-MINOR-4 |
| **Table 7** | **stars in every column; no definition, no Table 2 reference, no statement of standard errors or clustering** | units given | IL-MINOR-4 |
| **Table 8** | **stars; no definition or Table 2 reference** | "one-sided" dropped from the RI row, but it remains in the §4.1 text; "(11)" and "(19)" follow the group-size convention of Table 3 | IL-MINOR-4 |
| Table 9 | "other details as in Table 2" | S1–S3 are not defined in the note. The v8 note pointed to Section 5.2; v9 has no pointer. | IL-MINOR-5 |
| Table A.1 | n/a | sources given | OK |
| Table A.2 | no stars | "Log trading value" (constituents 5.170) is the mean daily log(1 + VAL), which differs from Table 1's weekly log trading value (6.82). v8's note gave the definition; v9 dropped it. | IL-MINOR-5 |
| Table A.3 | no stars | "S1–S3 as in Table 9". Table 9 does not define them; Section 5.2 does. | IL-MINOR-5 |

Proofreading's round-2 summary said "Stars are defined in Table 2 and referenced in every other starred table". That was true of v8 and is no longer true of Tables 6, 7 and 8. The fixes below keep each note to one sentence.

## 7. Phase D: originality of the new or reworded sentences (100%)

| Sentence | Check | Grade |
|---|---|---|
| B0024 Biktimirov "distinct return and trading-volume responses when a country changes class" | WebSearch for the exact phrase found no match. Compared with the abstract ("exhibit distinct return and volume effects"), 4 of 5 words appear in order, and the passage follows the abstract's order. | PARAPHRASE, borderline (IL-MINOR-6) |
| B0021 Hegde "attribute the persistent liquidity gains of S&P 500 additions mainly to lower direct trading costs" | WebSearch for the exact phrase found no match. Compared with "due primarily to a decrease in the direct cost of transacting", 2 words are shared. | PARAPHRASE (cited) |
| B0083 Harris & Gurel "gained more than 3% on the announcement … almost fully reversed after two weeks" | Compared with the abstract: "more than 3 percent … nearly fully reversed after 2 weeks" | PARAPHRASE (cited). This is the round-4 wording, restructured. |
| B0094 Harris & Gurel "price rises immediately after S&P 500 additions are announced" | The round-4 proposed text; 3 words shared ("immediately after … announced") | PARAPHRASE (cited) |
| B0024 Burnham "in the direction implied by the new benchmark" | This is v7 wording, already graded | PARAPHRASE |
| B0136 "prices and liquidity moved with FTSE's public statements rather than with the first-tranche rebalancing" | WebSearch found no match | ORIGINAL |
| Other reworded paragraphs (splits, notes, methods detail) | These compress the authors' own v8 text and add no external wording | ORIGINAL |

Result: 0 CLOSE_MATCH and 0 VERBATIM. D2 (self-plagiarism) was not run, because the author names and the earlier study are not in the repository, as noted in earlier rounds.

Tool limitation: Phase D uses WebSearch heuristics and is not professional plagiarism software such as Turnitin or iThenticate.

## 8. AI research failure-mode checklist (round-5 changes)

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug | CLEAR | No change to code or output after v8. The new method statements (φ, ψ, η; the 10^−6 offset; the m range; WCR with Rademacher weights and 999 draws; S1–S3) match the code line for line (§4). |
| 2 Hallucinated citation | CLEAR | No reference was added or changed. 33 of 33 are cited, with 0 orphans and 0 dangling citations. |
| 3 Hallucinated result | CLEAR, with a note | Every table cell is unchanged from verified v8. One ordinal description of real coefficients is wrong (B0068, IL-MINOR-1). This is not a fabricated number. |
| 4 Shortcut reliance | CLEAR | Design and identification are unchanged. |
| 5 Bug reframed as insight | CLEAR | No new "surprising" claim was introduced. |
| 6 Methodology fabrication | CLEAR, with notes | The Methods text matches the code. Compacting the notes removed three disclosures that v8 had: the Figure 1 named-series interactions, and the never-named, never-included controls for Figure 2 and the Table 3 split rows (IL-MINOR-3). These are omissions, not fabrications. |
| 7 Frame-lock | CLEAR | Framing and scope are unchanged. |

No mode is SUSPECTED and none is INSUFFICIENT EVIDENCE, so the checklist does not block.

## 9. Issue list (sorted by severity)

### SERIOUS
None.

### MEDIUM
None.

### MINOR (recommended fix; the Stage 5 gate expects zero issues)

| ID | # | Category | Location | Issue and evidence | Exact fix text |
|---|---|---|---|---|---|
| IL-MINOR-1 | 1 | Data description (C2) | B0068, §4.1 | "positive in several months, largest three and two months before it (0.33 and 0.23)". t_event_study.csv has 0.329 (m = -3), 0.248 (m = -6, April 2025) and 0.232 (m = -2), so 0.23 is not the second largest. Stop-slop F-32 introduced this. | Replace "largest three and two months before it (0.33 and 0.23)" with "significantly so three and two months before it (0.33 and 0.23)". |
| IL-MINOR-2 | 1 | Internal consistency; E6 up (ADV-E6-1) | B0136, §6 ¶2 | "prices and liquidity moved with FTSE's public statements rather than with the first-tranche rebalancing" contradicts the trading surge at the rebalancing close (0.79, t = 6.84; B0087), which B0135 states one sentence earlier. | "These findings favour the recognition channel over the price-pressure channel as the source of lasting effects: prices and liquidity moved with FTSE's public statements, and the first-tranche rebalancing brought a trading surge but no reliable price effect." |
| IL-MINOR-3 | 1 | Methods disclosure in notes (Mode 6) | B0071 (Figure 1), B0189 (Figure 2), B0067 (Table 3) | The compacted notes dropped the model and control group that v8 stated. Figure 1: named-but-excluded interactions (analysis_revision.R line 84). Figure 2 and the Table 3 split rows: never-named, never-included controls (lines 74 and 77). | B0071: "*Note*: Coefficients $\delta_m$ of Eq. (8), estimated jointly with the same month interactions for named-but-excluded stocks, with 95% confidence intervals (panel A: log Amihud; panel B: log trading value); dashed lines mark the announcement, confirmation and list months. Source: Authors' calculations." B0189: "*Note*: Eq. (8) for log Amihud with $\mathrm{ITT}_i$ in place of $\mathrm{Constituent}_i$, never-named, never-included controls and 95% confidence intervals; dashed lines as in Figure 1. Source: Authors' calculations." B0067: "*Notes*: Log Amihud unless stated; the split rows come from one regression with never-named, never-included controls, and other details are as in Table 2. Source: Authors' calculations." |
| IL-MINOR-4 | 1 | Table interpretability (stars) | B0101 (Table 6), B0108 (Table 7), B0115 (Table 8) | Stars appear in these tables, but no note defines them or points to Table 2. The Table 6 note also misstates where marks are omitted: the last row has none for the Small column. | B0101: "*Notes*: Eq. (7) with segment-by-window interactions; the last row reports the mean (standard error), significance marks are omitted for the three-stock segments and the last row, and other details are as in Table 2. Source: Authors' calculations." B0108: "*Notes*: Eq. (7), with volatility $\mathrm{Vol}_{iw}$ from Eq. (4), spreads in decimal units (0.0010 = 0.10 percentage points) and other details as in Table 2. Source: Authors' calculations." B0115: "*Notes*: Dependent variable log Amihud; the excluded stocks and the inference settings (one-sided randomization inference) are given in Sections 3.3 and 5.1, and other details are as in Table 2. Source: Authors' calculations." |
| IL-MINOR-5 | 1 | Table interpretability (definitions and pointers) | B0131 (Table 9), B0213 (Table A.3), B0148 (Table A.2) | S1–S3 are undefined in the Table 9 note, and the Table A.3 note points to Table 9, which does not define them. Table A.2's "Log trading value" (5.170) is the mean daily log(1 + VAL) (analysis.R line 46). It differs from Table 1's weekly measure (6.82), and the definition was dropped. | B0131: "*Notes*: One regression per panel on all 366 stocks, relative to never-named stocks, with S1–S3 as defined in Section 5.2, point estimates only for the two-stock row and other details as in Table 2. Source: Authors' calculations." B0213: replace "with S1–S3 as in Table 9" with "with S1–S3 as defined in Section 5.2". B0148: "*Notes*: Pre-period means (log trading value is the mean daily log of 1 plus traded value in VND billion) and standardized mean differences (SMD); log price and volatility stay above 0.10 after matching, so the matched estimates are paired with the size-by-week and trend specifications. Source: Authors' calculations." |
| IL-MINOR-6 | 1 | Originality (Phase D, borderline paraphrase) | B0024, §2.3 | Stop-slop F-12 changed "separate" to "distinct", restoring the source's wording ("distinct return and volume effects"). This partly reverses the round-1 CLOSE_MATCH fix. | Replace "and distinct return and trading-volume responses when a country changes class" with "and returns and trading volume that respond differently when a country changes class". |

### Advisory (outside the issue count)
- **ADV-E6-1 and ADV-E6-2.** See §5. Both need an author disposition before the checkpoint can advance. ADV-E6-1 is resolved by applying the IL-MINOR-2 fix.
- **ADV-E5-1.** The search-bounded novelty claim in B0013 is unchanged and remains open as before.
- **Outside the v9 changed-block scope.**
  - `submission/highlights.docx` bullet 1 reads "Vietnam's FTSE upgrade cut illiquidity of likely index stocks by 24% to 56%". This is causal wording, stronger than the manuscript's "fell … relative to never-named stocks".
  - Suggested wording: "Illiquidity of likely index stocks fell 24% to 56% after FTSE's upgrade steps" (77 characters).
- **Traceability.** "AUTHOR-EVENT-r5-venue" is cited in the correction list but missing from `author_events_round5.md`. The orchestrator should add the verbatim event or change the citation to r5-notes.

## Correction routing

1. Apply IL-MINOR-1..6 in integrity-correction round 6, with these IDs in `roadmap_item_ids`. Each fix replaces one block, and no estimate or table cell changes.
2. Record the E6 dispositions: ADV-E6-1 `restore` (through IL-MINOR-2) and ADV-E6-2 `authorize_with_reason`.
3. Re-verify only the touched blocks, then rebuild `submission/` from the new exact draft.
4. Stage 5 entry requires PASS with zero issues on that draft.

## Tool limitation disclaimer

- Phase D uses WebSearch heuristics. It is not a substitute for Turnitin or iThenticate.
- Crossref, doi.org and publisher full texts were not fetched. Phase B relies on the verified abstract and snippet evidence retained in the Stage 4.5 files, plus one WebSearch on 2026-09-24 that confirmed the Hegde and McDermott (2003) abstract wording.
