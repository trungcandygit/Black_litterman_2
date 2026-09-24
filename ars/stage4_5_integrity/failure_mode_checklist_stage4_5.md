# AI Research Failure Mode Checklist, Stage 4.5 (ARS v3.22.1, references/ai_research_failure_modes.md)

Run ftse2-20260924-01. Draft under check: ars/stage4_5_integrity/correction_round1/manuscript_v5.clean.md (SHA-256 a1783491551fbec22f4f2f745cf4ba045e1ce1295aacf779d61a239fbadde377).
Rule at 4.5: re-run all 7 modes; any SUSPECTED, or INSUFFICIENT EVIDENCE on Modes 1/3/5/6, blocks.

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug passing self-review | CLEAR | All six R scripts re-run from raw data (405 files) in a clean environment (R 4.3.3, fixest 0.14.2, MatchIt 4.5.5); all exit 0; 48/48 output CSVs reproduce every coefficient, SE, N and CAR to rtol 1e-6 (repro/REPRO_REPORT.md). The only difference (pre-trend Wald p-values) is a documented degrees-of-freedom convention, not a bug; the manuscript now reports the G-1 values. No suspiciously round effects; SEs vary across specifications. |
| 2 Hallucinated citation | CLEAR | 31/31 registered references VERIFIED in a fresh Phase A (three independent agents, WebSearch audit trail, A0 APIs blocked). Two new references added in correction round 1 (Burnham et al., 2018; FTSE Russell, 2025) verified in re-verification. Bibliographic fixes: LSEG titles, FAQ version. Context distortions (Gregoriou & Nguyen; Hegde & McDermott) fixed. |
| 3 Hallucinated result | CLEAR | Phase C traced 100% of numeric surfaces to output CSVs (Table 4: 120/120 cells); the CSVs themselves reproduced from raw data. Three prose numbers that disagreed with their own tables (6.3%, 1.0%, 0.14-0.20) were corrected. |
| 4 Shortcut reliance | CLEAR | Design threats are tested rather than assumed: ITT on a pre-announcement list, named-but-excluded falsification group, randomization inference on 85 large never-named stocks, size-by-week FE, matched weights, sector exclusion, post-announcement drift, placebo date. Remaining confound (pre-funding reform for the largest stocks) disclosed as a limitation. |
| 5 Bug reframed as insight | CLEAR | Surprising results (rising Corwin-Schultz spread; positive pre-period deviations; GEE selection) are reported as limitations or selection evidence, not as findings; the spread rise is attributed to volatility and the claims are restricted to price impact and trading activity. All reproduce from raw data. |
| 6 Methodology fabrication | CLEAR | Methods text checked against code in Stage 2.5 and again here; Data availability now lists all six scripts and software versions; the CAR test statistic is described exactly as coded (portfolio sigma times sqrt(L)), with the sqrt(L) scaling stated as the paper's assumption rather than attributed. |
| 7 Frame-lock | CLEAR | Framing changed from A to A' when the naming-timing test contradicted it (Stage 2 decision memo); two review rounds narrowed claims (bound reading removed, H2 restricted to the confirmation); Section 4.4 heading narrowed in correction round 1. |

No mode SUSPECTED or INSUFFICIENT EVIDENCE: no block.
