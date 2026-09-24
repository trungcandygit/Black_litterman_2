# Stage 2.5 INTEGRITY report (pre-review, Mode 1): manuscript_v2.md
Run ftse2-20260924-01. Date 2026-09-24. Final artefact SHA-256: 1adeb80492a7007f9cbac68e2000894baeb79cbc900c1f9a581e9904076d163c

## Verdict: PASS after 1 correction round (round 1 = FAIL with 9 correctable issues, all fixed and re-verified)

## Phase A: references (100% of 27 registered)
- 20 scholarly DOIs re-queried fresh on Crossref (crossref_recheck.tsv): author, year, journal, volume, issue, pages match; co-author lists checked for 9 multi-author entries. 20/20 OK.
- 7 grey-literature sources fetched: LSEG 2025 (7 Oct 2025, effective 21 Sep 2026 subject to March 2026 interim review), LSEG 2026 (7 Apr 2026, meets all criteria), VIR (22 Aug 2026; 27 stocks; large VCB/VIC/VHM, mid BID/VPB/HPG, small 21), The Investor (8 Apr 2026; 32 stocks; GEE, BSR new; PLX removed), Viet Nam News (13 Nov 2025; 28 stocks; SAB, DXG named), FTSE Russell 2018 (published 26 Sep 2018; Vietnam added to Watch List), FTSE Russell 2026 FAQ v1.3 (tranches 10/20/35/35% on 21 Sep 2026, 22 Mar 2027, 21 Jun 2027, 20 Sep 2027; review published Fri 21 Aug 2026). 7/7 exist.
- Ghost citations: 0. Uncited references: 0.

## Phase B: citation context (checked 12 of 25 citing sentences = 48%, all high-specificity paraphrases)
Issues found and fixed:
B1 tranche schedule attributed to LSEG (2026); release contains no schedule -> re-attributed to FTSE Russell (2026) FAQ with exact dates.
B2 "On 7 April 2026 ... fixed the effective date": date already set 7 Oct 2025 -> rewritten (announcement set date subject to interim review; confirmation kept it). Section 2.1 para 2 aligned.
B3 watch-list start Sept 2018 uncited -> FTSE Russell (2018) added.
B4 Biktimirov & Afego (2026) paraphrased as "no reliable liquidity link"; abstract attributes effects to institutional demand rather than trading pressure or liquidity, and reports reclassification-event effects -> intro, 2.3 and 6 rewritten; novelty claim now acknowledges their reclassification results.
B5 Kang & Zhang (2014) paraphrase overstated -> now states their zero-volume critique and our filter.
B6 Dong et al. (2023) -> now includes announcement abnormal returns; "may improve" wording respected.
B7 Raddatz et al. (2017) "concentrate in heaviest weights" beyond source -> "follow benchmark weights".
B8 PLX naming date lacked a source in text -> The Investor (2026) cited (PLX removed from November list).

## Phase C: data (100% of registered numeric surfaces)
All coefficients, SEs, stars, t, N in Tables 1-8, A1 and prose re-matched to output/*.csv (incl. 22/22 CAR rows). Earlier Stage 2 fixes retained (Vingroup 3 stocks; abnormal-value benchmark window). New fixes:
C1 winsorizing described as "each daily measure"; code winsorizes Amihud and CS only -> corrected.
C2 weekly filter omitted "positive Amihud" condition -> added. Window assignment rule (Monday weeks, window starts first full week on/after disclosure) and list-release hour caveat added from code and FTSE FAQ.

## Phase D: originality
8-gram overlap with the authors' earlier FTSE paper (submission_files, 9,416 words): 5 of 7,425 (0.07%), all boilerplate (exchange name, funding statement). No issue.

## Phase E: claims (100% high-impact + sentinel)
E1 abstract closing sentence generalised to all market upgrades from one case -> restricted to Vietnam's upgrade.
Causal-language scan: remaining causal verbs refer to measured decompositions or quoted hypotheses. Takeaway "X, not Y" antithesis rewritten. Announcement-stage estimate carries caveat in abstract, intro, 5.1, 5.2.
Novelty (#548, advisory): bounded claim ("search bounded to Crossref records and the literature cited here") now acknowledges Biktimirov & Afego's reclassification-event results. Scope conformance (#547, advisory): within RQ.

## AI Research Failure Mode Checklist (7 modes)
| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug | CLEAR | Code read against every method sentence; 3 earlier bugs fixed in Stage 2 (IDate, coef name, eval cutoff); coefficient names and windows verified; weekly/period rules checked in analysis.R l.58-67 |
| 2 Hallucinated citation | CLEAR | 27/27 references verified (Phase A); 4 wrong DOIs caught in Stage 1 stay corrected |
| 3 Hallucinated result | CLEAR | 100% numbers traced to CSV (Phase C) |
| 4 Shortcut reliance | CLEAR | Unfavourable results reported: matched+trend weakens announcement stage; trading-value pre-trend; spreads rise; near-miss selection |
| 5 Bug reframed as insight | CLEAR | The two surprising findings (rising CS spread; near-miss reverse selection) are not claimed as insights beyond the data; per-stock descriptives agree with regressions |
| 6 Methodology fabrication | CLEAR after C1/C2 | Methods text now matches code |
| 7 Frame-lock | CLEAR | Framing A abandoned when naming-timing test contradicted it (decision memo, user decision A') |
No mode SUSPECTED or INSUFFICIENT EVIDENCE -> no block.

## Metrics after corrections
Prose body 5,338 words (6,9xx incl. tables); abstract 183 words; references 27; em dashes 0; banned words 0.
