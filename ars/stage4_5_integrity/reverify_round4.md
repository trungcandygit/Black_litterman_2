# Stage 4.5 FINAL INTEGRITY: re-verification of integrity-correction round 4 (v7 -> v8)

Verification mode: Final Verification (Mode 2, final-check), scoped to every block changed in round 4, carried out by a fresh verifier that did not write the edits.
Date: 2026-09-24. Model: claude-opus-5-5 (single-model; `ARS_CROSS_MODEL` not set).

## Verdict: **FAIL**

There are 2 IL-MEDIUM issues and 7 IL-MINOR issues. Phase B found 0 MAJOR_DISTORTION and 0 UNVERIFIABLE. E6 found 7 upward `STRENGTH-DRIFTED` rows. They sit outside the verdict count but keep the checkpoint closed until each has a disposition.

Under the verdict criteria in `integrity_verification_agent.md`, any MEDIUM means FAIL. Both MEDIUM items are wording defects in round-4 edits. A one-block correction fixes each, and no estimate needs to change.

## Skill load record

All five files were read in full with the Read tool before any other work.

| File (actual path) | First heading |
|---|---|
| /root/.claude/skills/academic-pipeline/SKILL.md | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| /root/.claude/skills/academic-pipeline/agents/integrity_verification_agent.md (887 lines, read in two pages) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| /root/.claude/skills/academic-pipeline/references/integrity_review_protocol.md | `# Integrity Review Protocol (Added in v2.0)` |
| /root/.claude/skills/academic-pipeline/references/claim_verification_protocol.md | `# Claim Verification Protocol (Phase E)` |
| /root/.claude/skills/academic-pipeline/references/ai_research_failure_modes.md | `# AI Research Failure Mode Checklist` |

## Inputs and bindings

| Artifact | SHA-256 |
|---|---|
| Base: correction_round3/manuscript_v7.md (accepted at the previous PASS) | 926a8739d8d78a8915121bbc47953f66416d8f48cd705850a0526a176cbfa2b6 |
| Revised: correction_round4/manuscript_v8.md | 4d36bbde9133c6a49d83c8ca157c202ef9c9aa1ebaa452b10557ff98ef80aeb7 |
| Revised clean: correction_round4/manuscript_v8.clean.md (equals v8.md with the block anchors stripped; checked) | 270939e4a5a9e00d1ed104eecd3c5021e334e7cdf7fb65919c6b24332d4b5c59 |
| Patch: correction_round4/integrity_patch_round4.json (121 ops; roadmap items IL-MINOR-1..6) | dde39f4be8869057015360cc9fee1f25995020c498bc62034af496cc382b3b55 |
| E1 registry: claim_registry_v8.json (built with build_claim_registry.py, 239 claims, tier ALL) | 63e4e63dda17b1b8e0dcd0796f1669421d777414428d0ccb6c1c9ec542f59cb3 |
| E1.1 coverage: claim_registry_coverage_v8.json (`--validate-report` replay: PASS) | 9ee09c341b79ca6847de6d36366c91ba9507fdc1952e7c680f3103cddf5da34a |

E1.1 status is `completed`, with 61 candidates and 2 `candidate_unregistered`. Both are "Accessed 24 September 2026" URL lines in the reference list (The Investor 2026a, 2026b), the same two as in v7. Neither is a claim. `semantic_extraction_coverage` is `not_machine_detectable`.

Round 4 made no change to `code/` apart from presentation in `code/figure1.R` and `code/figure2.R` (font size, marker size, labels, a shared y-axis). No `output/*.csv` changed. Every number was therefore checked against the unchanged result files.

## Phase A (references touched in round 4)

- No reference entry changed bibliographically. The only reference-list changes are formatting.
- All 33 entries keep their verdict from the fresh Phase A in `phaseAB_group1-3.md`, plus Burnham et al. (2018) and FTSE Russell (n.d.) from `reverify_round1.md` and `reverify_round2.md`.
- A3 ghost-citation check on v8: all 33 references are cited in the body. I checked the narrative forms by hand: Callaway and Sant'Anna (2021), Kang and Zhang (2014), Stereńczak et al. (2020), Amihud (2002), Burnham et al. (2018), Corwin and Schultz (2012), Dong et al. (2023) and Harris and Gurel (1986).
- There are 0 orphan references and 0 dangling citations.

## Phase B: citation contexts in changed blocks (100%)

Evidence is the verified abstract text recorded in `phaseAB_group1-3.md` and in `reverify_round1.md` and `reverify_round2.md` (Burnham). Where that text could not settle a context, I ran a WebSearch.

| # | Block | Source | v8 context (abridged) | Verified source text | Verdict |
|---|---|---|---|---|---|
| B1 | B0083 | Harris & Gurel 1986 | "announcement gains of more than 3% were almost fully reversed after two weeks" | "immediately after an addition is announced, prices increase by more than 3 percent, and this increase is nearly fully reversed after 2 weeks" | SUPPORTED |
| B2 | B0094 | Harris & Gurel 1986 | "find temporary price rises when index funds buy S&P 500 additions, whereas the first-tranche purchase in Vietnam left no reliable price effect" | The source measures the rise "immediately after an addition is announced". In its pre-1989 sample, the announcement and the fund purchase were not separated. ADV-E6-R1-2 already moved the manuscript away from effective-date framing. | MINOR_DISTORTION (IL-MINOR-1) |
| B3 | B0021 | Harris & Gurel 1986 | "additions lead index funds to buy, which produces temporary volume and price effects that reverse afterwards" | same as B1 | SUPPORTED (unchanged in substance) |
| B4 | B0021 | Hegde & McDermott 2003 | "narrow spreads and raise trading activity persistently, mainly through lower direct trading costs" | "sustained increase in the liquidity … due primarily to a decrease in the direct cost of transacting and a smaller decline in the asymmetric information component" | SUPPORTED. "Mainly" matches "primarily". The secondary information-asymmetry channel is omitted, which is acceptable. |
| B5 | B0105 | Hegde & McDermott 2003 | "S&P 500 additions, by contrast, gained liquidity mainly through lower direct trading costs" | same | SUPPORTED |
| B6 | B0060 | Hegde & McDermott 2003 | "resembles the sustained liquidity increase that Hegde and McDermott (2003) document after S&P 500 additions" | "sustained increase in the liquidity of the added stocks" | SUPPORTED |
| B7 | B0013 | Hegde & McDermott 2003 | "raise trading activity and narrow spreads persistently" | same | SUPPORTED |
| B8 | B0076 | Dong et al. 2023 | "parallels the short-term excess returns that Dong et al. (2023) report around the announcement of the China A-share inclusion" | "In the short term, the underlying stocks gained cumulative excess returns before and after the announcement date" | SUPPORTED |
| B9 | B0024 | Dong et al. 2023 | abnormal returns around the announcement; longer-run market quality through liquidity, turnover and price synchronization | same snippet plus "may improve market quality by influencing … synchronization and liquidity and turnover rate" | SUPPORTED (unchanged) |
| B10 | B0083 | Burnham et al. 2018 | "Our data end too soon to test for the reversal within a year that Burnham et al. (2018) find at the country level" | "reclassified markets' prices substantially overshoot between the announcement and effective dates … but largely revert within a year" | SUPPORTED |
| B11 | B0024 | Burnham et al. 2018 | "its stock prices move sharply toward the new benchmark before implementation and give back most of that move in the following year" | "prices fall when a market moves from an index with more benchmarked ownership to one with less … and vice versa" | MINOR_DISTORTION (IL-MINOR-2). Compaction turned v7's "in the direction implied by the new benchmark" into "toward the new benchmark", and prices do not move toward a benchmark. |
| B12 | B0132 | Becker-Blease & Paul 2006 | "Studies that use index additions as an exogenous liquidity shock (Becker-Blease & Paul, 2006) rely on membership not following liquidity" | "a sample of firms experiencing an exogenous liquidity shock … in the context of additions to the S&P 500" | SUPPORTED. The "rely on" clause is the authors' own inference about the design premise, marked by the semicolon, and is not attributed to the source as a finding. |
| B13 | B0022 | Becker-Blease & Paul 2006 | "S&P 500 additions with larger liquidity improvements increase capital investment" | "a positive relation between changes in capital expenditures and changes in stock liquidity" | SUPPORTED |
| B14 | B0094 | Raddatz et al. 2017 | "consistent with the two stages at which benchmark changes move fund allocations, announcement and implementation" | "not just when benchmark changes are announced, but also later, when they become effective"; "mostly when these changes are implemented" | SUPPORTED. The source weights implementation more heavily. The manuscript names both stages and does not rank them, so this is not a distortion. |
| B15 | B0097 | Raddatz et al. 2017 | "benchmark-driven foreign allocations … point the same way for the persistent effect" | Phase B context 3 (country-level allocations) | SUPPORTED, with the country-to-stock extension already recorded as a MINOR note at Stage 4.5 |
| B16 | B0015, B0017, B0024 | Raddatz et al. 2017 | benchmark weights steer allocations; classification changes flows; aggregate or country-level studies | Phase B contexts 1-2 | SUPPORTED |
| B17 | B0013, B0024, B0083, B0136 | Biktimirov & Afego 2026 | persistent price gains for frontier additions; demand not trading pressure or liquidity; "unlike Biktimirov and Afego (2026) we follow liquidity stage by stage within one market" | B4-1..3: FTSE Frontier 50, 2008-2025, 30 markets, persistent gains, demand mechanism | SUPPORTED (the contrast with their multi-country price study is accurate) |
| B18 | B0048 | Chordia et al. 2000 | "Week fixed effects absorb market-wide liquidity shocks, which co-move across stocks" | "liquidity of individual assets often moves in tandem with market liquidity" | SUPPORTED |
| B19 | B0022 | Chordia et al. 2000 | "liquidity co-moves across stocks" | same | SUPPORTED |
| B20 | B0104 | Amihud 2002 | "the Amihud ratio divides absolute returns by traded value" | definition (Phase B R1) | SUPPORTED |
| B21 | B0043, B0105 | Corwin & Schultz 2012 | Eq. (2)-(3) spread from two-day highs and lows; "loads on intraday price ranges" | B10-1..3 | SUPPORTED |
| B22 | B0043 | Kang & Zhang 2014 | "loss of accuracy … for the Amihud ratio in emerging markets with many zero-volume days" | Phase B R19 (modified measure with a non-trading adjustment; improvements in inactive markets) | SUPPORTED |
| B23 | B0024 | Hau et al. 2010 | a change in classification "can move currency values" | MSCI global index change and currency demand (Phase B R16) | SUPPORTED |
| B24 | B0018 | FTSE Russell 2026 (FAQ) | "FTSE's liquidity, size and foreign-headroom screens use the investability weight of each security" | FAQ: securities are "assessed for liquidity using its 49% investability weight" and "treated as non-constituents … for all the eligibility screens such as liquidity and minimum size". Investability-weight use is documented for the liquidity test only (v7 said "in the liquidity test"). A WebSearch on 2026-09-24 found no text that extends it to the size or foreign-headroom screens. | MINOR_DISTORTION at best. Graded IL-MEDIUM-2 as a citation-context deviation: a rule the source does not state is attributed to FTSE. |
| B25 | B0018 | FTSE Russell 2026 (FAQ) | tranches apply a fraction of the weight; 49% -> 4.9% -> 49% | tranching factors 10/30/65/100% (supported). The 49% phasing example is the authors' arithmetic, and v8 dropped v7's "(10% of 49%)" marker. | Folded into IL-MEDIUM-2 (restore the arithmetic marker) |
| B26 | other changed blocks | Shleifer 1986; Chen et al. 2004; Bekaert et al. 2007; Stereńczak et al. 2020; Nguyen et al. 2021; Brown & Warner 1985; Ho et al. 2007; Cameron et al. 2008; Roth et al. 2023; Callaway & Sant'Anna 2021; LSEG 2025/2026; FTSE Russell 2018/n.d.; press sources | contexts shortened without changing the attributed content | earlier Phase A/B verdicts | SUPPORTED. Brown & Warner stays UNVERIFIABLE_ACCESS as before. |

Phase B totals for the round-4 contexts: 23 SUPPORTED, 2 MINOR_DISTORTION (B2, B11), 1 context deviation graded MEDIUM (B24/B25), 0 MAJOR_DISTORTION, 0 UNVERIFIABLE.

## Phase C: numbers, restructured tables and cross-references

Every cell of every table in v8 and every number in the changed text blocks was checked against `output/` at the reported rounding. Significance marks were recomputed from the stored *p*-values: * below 0.05, ** below 0.01, *** below 0.001.

| Item | Source file(s) | Result |
|---|---|---|
| Table 1 | output/revision/t1_descriptives.csv | 9/9 cells match |
| Table 2, columns 1-2 (all controls) and 3-4 (weighted matched); spread columns removed | revision/t2_baseline_clean.csv (clean_lamihud, clean_lval); revision2/t_matched_weighted.csv (matched_weighted_lamihud, lval) | 24/24 estimates and SEs, marks and N match. Text "column 3" (matched Amihud, -0.23 n.s., -0.47, -0.69) is correct. Text "column 2" (trading value 0.68, 1.03, 1.19) is correct. |
| Table 3 | revision/t_itt.csv | all cells match. "62% to 72%" = 0.268/0.392, 0.554/0.888, 0.811/1.129. Split rows 0.43/0.87/1.12 and 0.11/0.25/0.53 match. |
| Table 4, panels A-B (80 cells) | revision2/t3_car_portfolio_clean_est.csv | 80/80 cells match (script cross-check). Estimation days 120/98/98/89 match the text of Eq. (6). "Up to 2.9 times" = max t_cross/t_portfolio = 6.48/2.27 = 2.85, and 6.48 and 2.27 are quoted correctly. |
| Named-but-excluded CARs, now text only | same file, group named_excluded | "2.3% to 6.2% … three of four" and "-1.4% to 0.4%, never significant" match |
| Table 5 plus the former panel B, now in text | revision/t4c_spike_test.csv; revision/t4b_rebalance_groups.csv | all match. t = 0.7945/0.1162 = 6.84. p = 0.057 and 0.007. Text 0.76 (0.12), -0.28 (0.10), 0.00 (0.15). |
| Table 6 | revision/t5_segments.csv; table7b_rebalance_by_segment.csv | 15/15 cells match. Marks only for the small segment are correct. |
| Table 7 (spread columns moved from Table 2) | revision/t6_volatility.csv; revision/t2_baseline_clean.csv (clean_cs); revision2/t_matched_weighted.csv (matched_weighted_cs); revision/t7_robustness.csv (vol_control) | all cells match. The text references column 1 (vol 0.34/0.21/0.14), column 2 (0.09-0.13 pp), column 3 (0.11-0.14 pp), column 4 (0.06/0.08/0.12) and column 5 (-0.57/-1.00/-1.20), and all are correct. |
| Table 8 (placebo, two-way, bootstrap-matched and volatility rows removed) | revision/t7_robustness.csv; revision2/t_matched_weighted.csv; revision2/t_post_drift.csv; revision2/t_sector.csv; revision/t_wild_bootstrap.csv; revision/t6_randomization_inference.csv | all cells match. The removed rows stay correct in the text: 0.04 (0.10); "<17%" (0.207/0.178 = 1.16); "at or below 0.003"; the volatility row is Table 7, column 5. "About half" = 48-59% of baseline, correct. "12% and 13%" correct. |
| Table 9, panels A-B; the former panel C is now Appendix Table A.3 | revision/t8_named_excluded.csv; revision/t8c_named_by_stock.csv; revision2/t_named_ex_bsr.csv | all match. "Significant only at 10%" (p = 0.059), "-0.23, -0.46, -0.73, only the last at 5%" and "(Appendix Table A.3)" for GEE -1.83 are correct. Panel B is cited for -0.02/-0.19/-0.30. PLX and DPM as the only W2 declines above 0.5 is correct. |
| Figure 1 and Figure 2 text | revision/t_event_study.csv; revision/t_pretrend_wald.csv; revision2/t_itt_event_study.csv | 0.33/0.23; F = 6.66; F = 1.72 (p = 0.092); -0.23/-0.62/-1.12; ITT 0.26/0.22, F = 7.59, -0.22/-0.78: all match. "July and August 2025, the two months with significant positive deviations" is correct: relm -3 (p = 0.0015) and -2 (p = 0.0006); April 2025 (0.248, p = 0.082) is not significant. That confirms the IL-MINOR-6 correction. |
| Section 5.1 text | revision/t7_robustness.csv; revision/t6_randomization_inference.csv | trend -0.0002 (0.003); lval trend 0.010 and 0.28/0.39/0.43; placebo centre -0.21: all match |
| Section 3 counts | revision/run_summary_revision.txt; code | 366, 328, 24, 14, 27, 15, 12, 16, 110, 85, 352 clusters, 48 clusters, 32 sessions (1,536/48): all consistent |
| Cross-references | v8 | Every table, column, panel, appendix-table, equation and section pointer resolves correctly. Covered: Table 2 columns 1-3; Table 7 columns 1-5; Table 9 panels A-B; Appendix Tables A.1-A.3; Figure 1 panel B; Eq. (1)-(9) cited as "Eq. (4)" and "Eq. (7)"; Section 5.1 and 5.2 pointers. |

Phase C result: 0 numeric mismatches. One traceability defect: `output/TABLE_SOURCE_MAP.md` was not updated for the restructuring (IL-MINOR-7).

## Equations (1)-(9) against the R code

| Eq. | Manuscript | Code | Result |
|---|---|---|---|
| (1) | ILLIQ = \|R\|/VAL, VAL in VND billion, R the daily log return | analysis.R: `ret = log(close/shift(close))`; `value_bn = close*1000*volume/1e9`; `illiq = abs(ret)/value_bn` | Match. v8 also fixes v7's unit inconsistency ("VND" in the text against "VND billion" in the table). |
| (2)-(3) | β = sum of two squared one-day log H/L; γ = squared log of the two-day max H over min L; α = (√(2β) − √β)/(3 − 2√2) − √(γ/(3 − 2√2)); S = max{0, 2(e^α − 1)/(1 + e^α)} | analysis.R lines 34-40: `hl`, `beta_cs = hl + shift(hl)`, `gamma_cs = log(h2/l2)^2`, `k = 3-2*sqrt(2)`, `alpha_cs`, `cs_spread = pmax(0, …)` | Match (no overnight adjustment in either) |
| Winsorizing | ILLIQ and S at the 1st/99th percentile of each day | `wins()` applied `by = date` | Match |
| (4) | Amihud = ln(mean ILLIQ); TV = ln ΣVAL; Vol = ln(mean \|R\|); weekly spread = mean S; at least 3 days and a positive Amihud | `amihud = mean(illiq_w)` then `log`; `lval = log(sum(value_bn) + 1e-6)`; `absret = mean(abs(ret))` then `log(absret)`; `ndays >= 3 & amihud > 0` | Match, except that TV carries a +1e-6 offset (see Eq. 9 and IL-MINOR-4) |
| (5) | AR = R − R_b, or the market model on the first benchmark | revision2 `car_port2`: `ar = ret - get(bmk)`; market model `lm(ret ~ ew)` over est_days | Match. The benchmarks are ew over 328 controls, match-weighted `matched_w`, `topsize` (top tercile *of never-named stocks*, 110) and market model. The v8 wording of the 110 benchmark lost that qualifier (IL-MINOR-3). |
| (6) | AR_p = mean over group; CAR = sum; t = CAR/(σ̂_p √D); estimation window -130..-11 excluding -1..+20 around earlier events | `p <- mean(ar)` by date; `sum(p$ar)`; `/(s_est*sqrt(L))`; `est_days` = setdiff(i0-130..i0-11, excl_days) | Match (120/98/98/89 days) |
| (7) | FE DiD with Constituent×P_k; Monday weeks enter on or after the disclosure date; never-named controls; stock clusters | `feols(y ~ treated:P1+P2+P3 | symbol + week, data = clean, cluster = ~symbol)`; `cut(..., "week")` gives Monday starts; `week < D_CONF` etc. | Match |
| ITT | ITT_i for the 27; all other stocks, with a never-named/never-included variant | `itt_all` (wk), `itt_pure` (itt \| never) | Match |
| (8) | Σ_{m≠-1} δ_m (Constituent × M_mw); m relative to Oct 2025 | `i(relm, treated, ref = -1)`; `relm = (year - 2025)*12 + month - 10`. The Figure 1 model adds `i(relm, named)`, as the Figure 1 note states. | Match |
| Drift | κ(Constituent × s_w), with s_w the weeks since the announcement, 0 before | revision2 line 20: `tpost = pmax(0, (week - D_ANN)/7)` | Match |
| Trend | weeks since the start of the sample | `tindex = (week - min(week))/7` | Match |
| (9) | ln VAL_id on stock and date FE plus θ1 C×Reb + θ2 C×Eff over 32 sessions | `spike()`: `lval_d = log(value_bn + 1e-6)`; `s0 = rel==0`, `s1 = rel==1`; `| symbol + date` | Match in structure. The equation omits the 1e-6 offset, which is applied to 76 zero-volume stock-sessions in the window (IL-MINOR-4). |
| Abnormal TV | log TV minus the stock mean from 60 to 6 calendar days before 21 Aug | `lval_bench = mean(lval_d[date < D_LIST - 5])`, with `date >= D_LIST - 60` | Match |

## E6 claim-strength drift (v7 -> v8; changed blocks only)

Roadmap authority for strength changes in this round:
- IL-MINOR-6 explicitly authorizes downward corrections in B0007, B0112, B0116, B0135 and B0136.
- IL-MINOR-1 to IL-MINOR-5 authorize editorial compaction, new equations and literature comparisons. None of them authorizes a change in strength.

`STRENGTH-DRIFTED` rows (unauthorized). These are checkpoint-closing. Each needs `restore`, `authorize_with_reason` or `pause`.

| ID | Round | Block | Prior rung -> current rung (or dropped qualifier) | Ops claimed | Direction |
|---|---|---|---|---|---|
| ADV-E6-1 | 4 | B0003 Abstract, last sentence | "came with FTSE's disclosures, before the first index tranche took effect" (a verifiable timing fact) -> "before index funds bought" (a claim about unobserved investor behaviour; §6 concedes that "the price data do not identify investor type") | IL-MINOR-1, -3 | up |
| ADV-E6-2 | 4 | B0060 §4.1 | new: "most of it appeared … months before index funds traded" (same unobserved-behaviour claim) | IL-MINOR-1, -2, -3, -4 | up |
| ADV-E6-3 | 4 | B0013 Introduction, first finding | dropped "beyond a gradual post-announcement drift", and the constituent-only step result moved onto the ITT group (see IL-MEDIUM-1) | IL-MINOR-1, -2, -3 | up |
| ADV-E6-4 | 4 | B0098 §4.4 | "This ordering is consistent with H4, although the two upper segments contain three stocks each" -> "…, consistent with H4" (caveat dropped from the H4 claim) | IL-MINOR-2, -3 | up |
| ADV-E6-5 | 4 | B0135 §6 | "only the confirmation gain lasted, under three of four benchmarks" -> "only the confirmation gain lasted" | IL-MINOR-1, -2, -3, -6 (IL-MINOR-6 covers only the "no price change" wording) | up |
| ADV-E6-6 | 4 | B0132 §5.2 | dropped "The constituent estimates combine the upgrade's effect with FTSE's selection; the ITT estimates average the effect over listed stocks that were and were not included. We report both and treat neither as a bound on the other." (§6 B0141 keeps only "side by side") | IL-MINOR-2, -3, -4 | up (interpretive caveat dropped) |
| ADV-E6-7 | 4 | B0025 §2.3 | dropped "Beyond Dong et al. (2023), we did not locate a verified stock-level study of liquidity around the MSCI inclusion of China A-shares, so our comparison with that episode rests on their evidence alone", while B0076 adds a new Dong comparison | IL-MINOR-2, -3 | up (scope caveat dropped) |

Downward moves, all recorded and closed:
- Authorized by IL-MINOR-6:
  - B0007: "raised" -> "improved".
  - B0112: "of similar size in every specification" -> "except … about half as large".
  - B0116: "largest positive deviations" -> "significant positive deviations" (a factual correction, confirmed in Phase C).
  - B0135 and B0136: "no price change" and "prices had already adjusted" -> "no reliable price effect".
  - B0136: "the 2025 and 2026 decisions mattered" -> "were followed by liquidity gains".
- Downward, not explicitly authorized, and harmless:
  - B0093: "That absence is a direct falsification test" -> "where a general rise in trading would have shown up".
  - B0102 (removed Takeaway): "Rising trading value … drove the fall in illiquidity" removed.
  - These should be recorded as `authorize_with_reason`: a weaker claim matches the evidence.

E6 contract note: as in earlier rounds, the rows are rendered here. The `claim-strength-drift-findings/1.0` companion and the disposition sidecar belong to the orchestrator and author step.

## Deleted content (limitations, unfavourable results, caveats)

- Named-but-excluded CAR table (v7 Table 4 panel C) removed. The text keeps the announcement-week and confirmation ranges. Not kept: the named-but-excluded [0,+20] announcement CARs, which are significant under two benchmarks (8.7%, t = 2.04 matched; 5.8%, t = 2.18 large never-named). v7 did not discuss them either, the conclusions do not rest on them, and they remain in `output/revision2/t3_car_portfolio_clean_est.csv`. Note only.
- Reference-session alternative (0.62, t = 3.54) removed. It is a smaller but still significant surge estimate, the conclusion is unaffected, and `output/revision/t4_rebalance_reg.csv` keeps it. Note only.
- "Evidence concerns the first tranche; 2027 tranches may carry larger demand" removed from §4.3. The limitation is still in §6. OK.
- The "we list it as a limitation" pointer for the pre-funding reform was removed. The limitation is still in §6. OK.
- Dong scope caveat (ADV-E6-7) and constituent/ITT bound caveat (ADV-E6-6) removed. See E6.
- Three-stock caveat removed from the H4 claim (ADV-E6-4). §4.4 still reads the segment illiquidity estimates as descriptive, and §6 keeps the caveat for illiquidity only.
- §6 limitations paragraph: all five limitations are kept (survivorship, three post-effective days and first tranche only, investor type, the pre-funding reform and the BSR venue, press-reported lists).
- References: all 33 are still cited. No orphan and no dangling citation.

## Phase D: originality (100% of the new or reworded citation sentences)

| Sentence | Check | Grade |
|---|---|---|
| Harris & Gurel "announcement gains of more than 3% were almost fully reversed after two weeks" | WebSearch exact phrase: no match. Against the abstract, "fully reversed after 2/two weeks" is a 4-word overlap in a cited attribution. | PARAPHRASE (cited) |
| Becker-Blease & Paul "use index additions as an exogenous liquidity shock … rely on membership not following liquidity" | WebSearch: no match. "Exogenous liquidity shock" is a 3-word technical term. | ORIGINAL / PARAPHRASE |
| Burnham "reversal within a year … at the country level" | Against "largely revert within a year": 3 function words shared, cited | PARAPHRASE (paraphrase distance adequate) |
| Burnham B0024 "move sharply toward the new benchmark … give back most of that move in the following year" | shares at most "prices"/"year" with the abstract | PARAPHRASE (wording issue is IL-MINOR-2, not originality) |
| Dong "short-term excess returns around the announcement" | against "In the short term … cumulative excess returns before and after the announcement date" | PARAPHRASE (cited) |
| Hegde & McDermott "mainly through lower direct trading costs" | against "due primarily to a decrease in the direct cost of transacting" | PARAPHRASE (cited) |
| Raddatz "two stages … announcement and implementation" | against "when announced … when they become effective" | PARAPHRASE (cited) |
| Other reworded paragraphs | compressions of the authors' own v7 text (graded at Stage 4.5); no new external wording | ORIGINAL |

Result: 0 CLOSE_MATCH and 0 VERBATIM. Tool limitation: WebSearch heuristics are not Turnitin or iThenticate.

## AI research failure-mode checklist (round-4 changes)

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug | CLEAR | No analysis code changed; figure scripts changed presentation only. All reported numbers equal the unchanged CSVs. |
| 2 Hallucinated citation | CLEAR | No new references. All 33 were VERIFIED earlier. The context issues (IL-MEDIUM-2, IL-MINOR-1, IL-MINOR-2) are Phase B findings, not fabrications. |
| 3 Hallucinated result | CLEAR | 100% of the numbers in changed blocks trace to output/ (Phase C). The four new text numbers (0.15, 0.47, 0.69, 3%) are traced. |
| 4 Shortcut reliance | CLEAR | No change to design or identification |
| 5 Bug reframed as insight | CLEAR | No new "surprising" claims. The B0116 correction weakens a claim. |
| 6 Methodology fabrication | CLEAR, with notes | Eq. (1)-(9) match the code. Two disclosure gaps: the log offset (IL-MINOR-4) and the benchmark tercile qualifier (IL-MINOR-3). The intro misattribution (IL-MEDIUM-1) is a claim-support issue, not fabrication. |
| 7 Frame-lock | CLEAR | Scope and framing unchanged |

No mode is SUSPECTED and none is INSUFFICIENT EVIDENCE, so the failure-mode checklist does not block.

## Issue list (sorted by severity)

### SERIOUS
None.

### MEDIUM (must fix)

| ID | Block | Issue | Evidence | Exact proposed fix |
|---|---|---|---|---|
| IL-MEDIUM-1 | B0013 (Introduction, "First, …") | The ITT sentence is credited with "a discrete step at the confirmation but not at the list", cited to Tables 2 and 3. The drift/step test was run only for constituents (revision2/t_post_drift.csv); no ITT step test exists. Neither table contains the test. Unadjusted, the ITT estimates do step at the list (-0.55 -> -0.81), and the ITT event study shows no discrete jump at the confirmation (-0.33 in March 2026 -> -0.39 in April 2026; Figure 2). The v7 qualifier "beyond a gradual post-announcement drift" was dropped. | t_post_drift.csv; t_itt.csv; revision2/t_itt_event_study.csv | Replace the sentence with: "First, ITT illiquidity fell by 0.27, 0.55 and 0.81 log points across the three windows, about two thirds of the constituent declines (Tables 2 and 3); for constituents, the confirmation brought a discrete step beyond a gradual post-announcement drift, and the constituent list did not (Section 4.1)." |
| IL-MEDIUM-2 | B0018 (§2.1) | Citation-context deviation (FTSE Russell, 2026). v8 says FTSE's "liquidity, size and foreign-headroom screens use the investability weight". The verified FAQ text documents investability-weight use in the liquidity test only (v7: "in the liquidity test"). v8 also dropped the "(10% of 49%)" marker that flagged the 4.9% example as the authors' arithmetic (the Stage 4.5 Phase B R13 #8 concern). | phaseAB_group2.md R13 (fact table and Phase B #7-8); WebSearch 2026-09-24 found no supporting text | Replace the sentence from "FTSE's liquidity, size …" to the end of the example with: "FTSE screens Vietnamese securities as non-constituents on liquidity, minimum size and foreign headroom and, in the liquidity test, uses each security's investability weight, which reflects free float and foreign-ownership limits (FTSE Russell, 2026). The same weight scales index weight, and each tranche applies a fraction of it: a security with a 49% investability weight enters at 4.9% after the first tranche (10% of 49%) and at 49% after the last, so index weight and passive demand rise with free-float market capitalization." |

### MINOR (recommended fix)

| ID | Block | Issue | Exact proposed fix |
|---|---|---|---|
| IL-MINOR-1 | B0094 (§4.3) | Harris & Gurel MINOR_DISTORTION. The source measures the rise "immediately after an addition is announced", and its sample does not separate the announcement from the fund purchase, so "when index funds buy" re-creates the framing corrected in ADV-E6-R1-2. | "Harris and Gurel (1986) find temporary price rises immediately after S&P 500 additions are announced, which they attribute to index-fund buying pressure; in Vietnam, the first-tranche purchase itself left no reliable price effect." |
| IL-MINOR-2 | B0024 (§2.3) | Burnham MINOR_DISTORTION: "move sharply toward the new benchmark". Prices move in the direction implied by the change in benchmarked ownership, not toward a benchmark. | Replace "move sharply toward the new benchmark before implementation" with "move sharply in the direction implied by the new benchmark before implementation". |
| IL-MINOR-3 | B0203 (§3.2; v7 B0044) | The benchmark lost its qualifier. "The 110 never-named stocks in the top tercile of pre-period trading value" conflicts on its face with §3.3's "85 never-named stocks in the top tercile … among all 366 stocks". The code (top_ctrl) uses the tercile among never-named stocks. | "…the equal-weighted mean of the 110 never-named stocks in the top tercile of pre-period trading value among never-named stocks, …" |
| IL-MINOR-4 | B0200 Eq. (4) and B0208 Eq. (9) | The equations state ln ΣVAL and ln VAL. The code uses log(VAL + 10^-6), which applies to 76 zero-volume stock-sessions in the Eq. (9) window (raw data count) and to any zero-value week. | After Eq. (9) add: "Following the code, we add 10^-6 VND billion to traded value before taking logs in Eq. (4) and Eq. (9), so that zero-volume sessions enter the sample." Alternatively, write $\ln(\mathrm{VAL}_{id} + 10^{-6})$ in both equations. |
| IL-MINOR-5 | B0112 (§5.1) | "The coefficients remain negative in every specification; they are of similar size except …" does not cover the two ITT rows. The ITT row without banks is about 57-74% of the constituent baseline, and a reader would compare it to the baseline. | "…they are of similar size except in the weighted matched sample with a trend and the drift specification, where they are about half as large (the ITT row compares with Table 3)." |
| IL-MINOR-6 | B0107 (Table 7) | Columns (2) and (4) share the header "CS spread", and column (5) is labelled "Amihud" with no hint of the control. The note resolves this, but the table does not read on its own. | Headers: "(4) CS spread, volatility control" and "(5) Amihud, volatility control". |
| IL-MINOR-7 | output/TABLE_SOURCE_MAP.md (project traceability rule) | The map was not updated for round 4:<br>• Table 7 now draws on revision/t2_baseline_clean.csv (clean_cs) and revision2/t_matched_weighted.csv (matched_weighted_cs).<br>• Appendix Table A.3 (revision/t8c_named_by_stock.csv) is missing.<br>• Text-only numbers have no row: the named-but-excluded CARs (revision2/t3_car_portfolio_clean_est.csv) and the former Table 5 panel B (revision/t4b_rebalance_groups.csv).<br>• The Table 2 row still implies spread columns. | Update the rows:<br>• Table 7: add t2_baseline_clean.csv (clean_cs) and t_matched_weighted.csv (matched_weighted_cs).<br>• Add "Table A.3: output/revision/t8c_named_by_stock.csv (analysis_revision.R)".<br>• Add "Text §4.2 named-but-excluded CARs: output/revision2/t3_car_portfolio_clean_est.csv (group named_excluded)".<br>• Add "Text §4.3 abnormal trading value: output/revision/t4b_rebalance_groups.csv". |

### Advisory (outside the issue count)
- ADV-E6-1..7 (above) keep the checkpoint closed until each row has an author disposition. Recommendations:
  - ADV-E6-1 and ADV-E6-2: restore. Replace with "before index funds had to buy" (B0003) and "months before index funds had to trade" (B0060).
  - ADV-E6-3: restore via IL-MEDIUM-1.
  - ADV-E6-4: restore by appending ", although the two upper segments contain three stocks each".
  - ADV-E6-5: restore with "and only the confirmation gain lasted, under three of four benchmarks".
  - ADV-E6-6: restore one sentence at the end of B0132: "The constituent estimates combine the upgrade's effect with FTSE's selection, and the ITT estimates average it over listed stocks that were and were not included, so we treat neither as a bound on the other."
  - ADV-E6-7: `authorize_with_reason` is defensible, because the new Dong comparison is about returns, which Dong et al. study directly. Otherwise restore the caveat as a clause in B0076.
- ADV-E5-1 (novelty claim, now in B0023) keeps its search-bounded wording and stays open as before.

## Correction routing

- Fix IL-MEDIUM-1 and IL-MEDIUM-2 (and preferably IL-MINOR-1..7) in integrity-correction round 5, citing these IDs in `roadmap_item_ids`.
- Record E6 dispositions for ADV-E6-1..7.
- Re-verify the touched blocks.
- Stage 5 entry requires PASS on the corrected draft.
- This round-4 re-verification counts toward the Stage 4.5 FAIL-loop budget per `pipeline_state_machine.md`, which the orchestrator tracks.

## Tool limitation disclaimer

Phase D uses WebSearch heuristics and is not professional plagiarism software. Crossref, doi.org and publisher sites were blocked. Phase B relies on the abstract and snippet evidence retained in the Stage 4.5 Phase A/B files, plus one WebSearch for the FTSE FAQ screens, which did not surface supporting text.
