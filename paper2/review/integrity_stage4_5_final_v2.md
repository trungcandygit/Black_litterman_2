# Stage 4.5 Final Integrity Check, Mode 2 (final verification), v2

Manuscript under test: `paper2/manuscript/manuscript_final.Rmd` (rendered `manuscript_final.docx`, same timestamp, read via pandoc). Verifier: independent integrity_verification_agent, fresh context. No manuscript or code file was edited. R/46 was run from a scratch copy (output redirected; the repo process file was not touched). Scope: PASS applies only to the registered populations (49 reference entries, all citation contexts in Sections 1, 2, 5, 6 and Table 5, all numbers in the text and Tables 1-5, E1 high-impact claims). It is not a certificate of global correctness.

## Verdict: FAIL

Counts: MAJOR_DISTORTION 1 (N1); UNVERIFIABLE 0; MINOR_DISTORTION / minor items 11 (listed separately); UNVERIFIABLE_ACCESS notes 4.

The single blocking item is a priority claim in Section 6 ("to our knowledge, the first for this market") that the authors' own search log contradicts. It is a one-sentence text fix. Everything else passes: all 49 references exist, the six re-review MAJOR items (M1-M6) are resolved, no number is wrong, the independent recomputation reproduces every headline figure.

## Blocking issue

**N1 (MAJOR_DISTORTION, novelty/priority claim, Phase E).** Section 6: "Our estimates of +1.7% for the ceiling, +2.2% for the gap, and −0.5% for the intraday return are, to our knowledge, the first for this market." The project's own log (`process/04_literature_search_log.md`, line 8, and `06_integrity_stage2_5_C.md`) records that a public repository, `tungtran0911/vn-equity-factors` (grey literature, not peer reviewed, 404 HOSE stocks), reports the next-session abnormal return after a ceiling close of +1.694% (t = 39.47), -0.388% after a 3-6.5% rise, and -0.225% after a floor close, and the log states "Consequence: no 'first to document' claim". I confirmed this session by web search that the repository exists and that its README states the 1.69% / 0.39% figures and the mechanism "closes at the limit with orders unfilled on one side, and that imbalance carries into the next session". The earlier Stage 4.5 report (v1) found the precedent acknowledged in the abstract and introduction; the current version dropped the acknowledgement but kept an unbounded "first". The Section 5 sentence "A stock that closes at its ceiling carries a queue of unfilled buy orders into the night" states the same mechanism without attribution (no copied wording was found; the overlap is in the idea, so this is an attribution point, not plagiarism). E5 classification: UNRESOLVED/contradicted by the authors' own record. The close-to-close sign is therefore not new for HOSE; the gap/intraday split, the near-limit comparison and the multiplicity family remain the new parts (and those are bounded correctly in Section 1).
Fix (text only): bound the sentence ("the first in the peer-reviewed literature we found; a public non-peer-reviewed analysis reports a close-to-close next-session return of about 1.7% for HOSE ceilings (cite or name it)") and, if kept, attribute the unfilled-order mechanism. No re-analysis needed.

## Phase A: references (49 entries; every one searched this session)

DOI resolver is blocked, so DOIs were checked against publisher/index URLs returned by search (ScienceDirect pii strings, Wiley, Cambridge, OUP, JSTOR, IDEAS).
All 49 entries: VERIFIED (exist; authors, year, title, journal, volume, issue, pages match). No NOT_FOUND, no MISMATCH. Cross-match by script (surname plus year of each reference found in the body) found no orphan; all in-text author-year citations resolve to an entry.
Audit trail, top results: Kim and Rhee, Bildik and Gülay, Subrahmanyam, Chen H. et al., Qi, Harvey and Liu, Corwin and Schultz, Gutierrez and Kelley, Benjamini and Hochberg, Kelly and Clark, Amihud, Bali et al., Akbas et al., Berkman et al., Lou et al., Harvey et al., Chen Y.-M. (publisher page `0927538X93900053`, DOI string `0927-538X(93)90005-3` matches), Chen T. et al. (ScienceDirect `S0304407618301799`, DOI shown by search), Cho et al. (ScienceDirect `S0927539802000245` equals DOI `S0927-5398(02)00024-5`), Berkman and Lee (ScienceDirect `S0927538X02000409` equals DOI `S0927-538X(02)00040-9`; earlier M1/M4 concern resolved), Jia et al. (`S1544612323010875`, article number 104715 consistent), Zeng et al. (`S1544612323011753`, vol 60, 104803 consistent), Qi (PLOS URL contains `journal.pone.0287548`), Huang et al. 2001 (IDEAS `reveco/v10y2001i3p263-288`), Lien (IDEAS `pacfin/v55y2019icp239-258`), Lin et al. (IDEAS `jbfina/v150y2023ics0378426623000432`), Liang and Hu (Wiley `for.3197`), Jones et al. (Cambridge, JFQA 60(1) 68-104), Qiu et al. (ScienceDirect `S0275531925000327`), Qiao and Dam (JFM 50, 100534), Lu et al. (ScienceDirect `S0304405X23000491`), Huang X. et al. (PBFJ 82, article 102176), Kim and Jun (T&F, 26(7)), Kim and Limpaphayom, Deb et al., Kodres and O'Brien, Greenwald and Stein, Holm, Fama and MacBeth, Newey and West, Parkinson, Petersen, Hou et al., Chordia et al., Brennan, Aboody et al., Bogousslavsky, Zhang et al. (IDEAS `pacfin/v74y2022ics0927538x22000737`).
DOI strings in the manuscript with no direct DOI display but consistent publisher identifiers: Jia et al. 2024 and Zeng et al. 2024 (pii and article number match). No DOI contradicted any record. No reference carries a DOI the evidence file flagged as unseen and that I could not match.
HSC (2025) and Viet Nam News (2025): both pages exist in search; fetch blocked (access note A1).

## Phase B: citation contexts (100% of Sections 1, 2, 5, 6 and Table 5)

Every attribution matches the abstract or record returned by search. Specific points:
- Berkman and Lee (2002): abstract-level (search summary of the abstract): spillover, price continuations after limit hits, trading activity the day after, widening raises volatility. The manuscript now says only "examine volatility and trading activity around a revision of the limit system" and Table 5 says "different question": supported, conservative. Abstract-level only.
- Huang et al. (2001): SECONDARY-DESCRIPTION-ONLY (IDEAS record summary: "price continuations for the overnight period following limit moves and price reversals for the subsequent trading time period", Taiwan 1990-1996). Section 2, Section 5 and Table 5 ("Same timing: positive gap, partial intraday reversal") stay inside that text. The Table 5 caption discloses the "records we could access" basis. Not a distortion.
- Kim and Rhee ("find support ... in Tokyo", Table 5), Lou et al. ("continuation in both periods with offsetting cross-period reversal"), Akbas et al. and Lu et al. (clienteles/market makers), Qi (market-quality outcome, "different outcome"), Qiao and Dam (negative average overnight return, "all Chinese stocks"), Kim and Limpaphayom ("more likely to hit limits"), Chen (1993) ("which implies a delay"): all fixed as the re-review asked and all consistent with the records.
- Others checked and matching: Brennan, Kodres and O'Brien, Greenwald and Stein, Subrahmanyam, Chen H. et al., Bildik and Gülay, Cho et al., Deb et al., Zhang et al., Jia et al., Lien et al., Kim and Jun, Chen T. et al., Lin et al., Liang and Hu, Kelly and Clark, Berkman et al., Aboody et al., Bogousslavsky, Qiu et al., Jones et al., Harvey et al. (t above 3.0), Harvey and Liu, Chordia et al. (3.38, "near 3.4"), Hou et al. (65% of 452 fail 1.96), Petersen, Gutierrez and Kelley, Huang X. et al.
- No UNVERIFIED magnitude from the evidence file (Chen T. 2.44%/2.59%/83.6%, Lou "2% per month", Hendershott 14/-15 bp) appears in the text. No unverified source (Hendershott, Le, Veeraraghavan, Gao et al., Tang, Aktas, GitHub) is cited.

## Phase C: statistical and data surfaces

R/46_verify_C.R (scratch copy): T1-T6 all PASS (look-ahead difference 0; MOM3M slope 0.12287 equals table; ceiling t+1 1.66022% on 3,187 events equals table; gap + intraday - close-to-close = 0.046 pp; 4 of 26 survive).
Independent recomputation from `data/raw` with fresh long-format scripts (`scratchpad/ind.R`, `ind2.R`; no repository code sourced):

| # | Quantity | Manuscript/table | Recomputed |
|---|---|---|---|
| 1 | Files; trading days; first/last date | 405; 519; 21 Aug 2024 to 23 Sep 2026 | 405; 519; 2024-08-21 to 2026-09-23 |
| 2 | Stocks kept (>= 95% closes); stock-days with a return | 347; 178,773 | 347; 178,773 |
| 3 | Mean / SD / median daily return (%) | 0.018; 2.10; 0.00 | 0.01788; 2.0982; 0 |
| 4 | Median / mean dollar volume (million VND, all stock-days with a price) | 2.6 bn; 51.2 bn | 2,557.7; 51,226 |
| 5 | Sector codes; largest share | 18; 15% | 18; 14.99% |
| 6 | Pile-up +6.5 to +7.1, -7.1 to -6.5, +6.0 to +6.5 (%) | 1.98; 1.30; 0.29 | 1.984; 1.303; 0.288 |
| 7 | Returns beyond ±8% | 96 | 96 |
| 8 | Window ceilings / floors / denominator | 3,207; 2,115; 156,653 (2.0%, 1.4%) | 3,207; 2,115; 156,653 |
| 9 | Ceiling t+1 and t+1..t+5, date-clustered | 1.66 (t 4.90), 1.45 (t 4.00), 3,187 events, 446 dates | 1.660 (4.908), 1.450 (4.008), 3,187, 446 |
| 10 | Floor t+1 and t+1..t+5 | -0.71 (t -5.32), -1.76 (t -4.74), 2,105, 319 dates | -0.713 (-5.326), -1.760 (-4.751), 2,105, 319 |
| 11 | Ceiling gap / intraday (lagged weights, events to nd-5) | 2.24; -0.54; 3,199 | 2.2435; -0.5354; 3,199 |
| 12 | Floor gap / intraday | -0.97; 0.30; 2,111 | -0.9722; 0.3040; 2,111 |
| 13 | Ceiling vs 5-6.5% rises, gap | 2.66 (t 14.0); 1,751 comparison days | 2.658 (13.998); 1,751 |
| 14 | Floor vs 5-6.5% falls, gap | -1.59 (t -9.7); 1,522 | -1.587 (-9.687); 1,522 |
| 15 | KRX split events (ceiling; floor) | 936 / 2,263; 891 / 1,220 | 936 / 2,263; 891 / 1,220 |

Table-to-text and CSV checks: C1/C3/C14/C16/C17/C18/C20/C21/C22/C23/C24/C25/C26 against the abstract, Sections 3, 5, 6, 8 and Tables 1-5: all agree (BH p 2.6e-06 to 4.0e-04 for the four event tests; week-clustered survive rule TRUE for all four; largest |t| 1.45 (MOM3M 1.452, IMOM 1.448), confirmation t 1.17/1.14; lag-8 largest 1.79; MDE 0.12-0.31; 18 of 22 spreads negative after 25 bp; Bonferroni bounds 683 and 125; tercile gaps 1.97/2.16/2.63 and 1.41/2.18/3.16, t 4.8 and 4.2; floor volume terciles -1.20 to -0.68; outlier exclusion 2.24 to 2.26 and -0.97 to -0.98). Abstract arithmetic: 2.2 - 0.5 = 1.7, −0.7% (−0.749) by the fifth close. Plan-deviation statements in Section 4 were checked against commit 63bdc6d (decile spreads, multivariate model and same-stock control planned and not run; second horizon ambiguous; half split): disclosed correctly. Timestamps (63bdc6d before first analysis code) were verified in v1 and are unchanged. The earlier M2/M1 text defects of v1 (garbled tercile sentence, 522 count) no longer occur: the 522 is now described as locked all day.
Not recomputed from raw this pass: the Fama-MacBeth full family (only covered by R/46 T2 and the v1 independent run) and the open-to-day-5 means (covered in v1).

## Phase D: originality

100% of new or modified paragraphs (Sections 2, 3, 5, 6) checked by distinctive-phrase search: no verbatim match to any web source. The README of tungtran0911 shares the mechanism, not the wording (see N1). No self-plagiarism: the earlier BL-K_IO manuscript is neither cited nor reused; no earlier-paper text surfaced. Section 2 sentences track the abstracts only in the cited findings.

## Phase E: claims

All E1 high-impact claims verified against saved tables and the recomputation above: abstract (every number), H1-H4 (Section 5 labels each: H1 after the 5-day paragraph, H2 after Table 2 decomposition, H3 after Table 3, H4 in the buyer paragraph; "Taken together ... support H1 to H4" is consistent with the numbers: H4 is supported by a significantly negative open-to-day-5 return, -0.75, t -2.7), conclusion (1.7 / 2.2 / 0.5 / 2.7 / 3.1 / 0.75), the hedged mechanism language (three rival readings, no causal claim, no efficiency claim), Table 5 relations. Benchmark table: the comparison states no source reports a matching quantity; no magnitude is compared; none uses the UNVERIFIED numbers.
Scope-conformance (E4, advisory, not an issue): claims stay inside one exchange, 25 months, no news/order-book data. Novelty (E5, advisory): Section 1 and Section 2 statements are correctly bounded ("to our knowledge, none of the studies we reviewed", "we found no peer-reviewed study"); the Section 6 sentence is not (N1).

## Re-review (stage 4b) fix verification

M1 Berkman and Lee: fixed (conservative wording; DOI now matches the ScienceDirect identifier). M2 Kim and Rhee: fixed. M3 Lou: fixed (clientele to Akbas and Lu). M4 DOIs: all matched or consistent with publisher identifiers (see Phase A). M5a Qi: fixed (different outcome; floor weaker, benchmark-dependent). M5b Qiao and Dam: fixed (China only). M6 abstract: fixed (-0.7% by the fifth close). m1 Hendershott removed; m2 fixed; m3 caption plus the Huang record basis disclosed; m4 fixed; m5 Le removed; m6 data-source wording improved; m7 denominator fixed; m8 "Section 6" fixed; m9 H labels added and "26 tests" used; m10 repeated sentence removed from Section 4 (a milder repeat of the 2.0% share remains, item n5); m11 GARCH removed, T+1 defined (VCI and HSC remain, item n10); m12 "in our event window" stated (item n5); m13 fixed; m14 Asia claim removed, wider-band listing claim moved to Limitations; m15 Section 6 opens with the rival readings; m16 fixed; m17 largely fixed (item n8). No regression found. No internal-process language in the text (grep for pipeline, stage, round, reviewer, agent, paper A/B/C, "surprisingly": none; the AI-use disclosure, the analysis-plan paragraph and the repository statement are legitimate transparency).

## 7-mode AI failure checklist

1 Implementation bug passing self-review: CLEAR (R/46 T1-T6 pass; 15 groups reproduced from raw independently). 2 Hallucinated citation: CLEAR (49 of 49 exist and match). 3 Hallucinated result: CLEAR (every table value traces to a saved CSV; 15 recomputed). 4 Shortcut reliance: CLEAR (close = high comparison, benchmark, outlier, exact-hit and platform-split checks present; limits disclosed). 5 Bug reframed as insight: CLEAR (no surprise language; headline result reproduced from raw). 6 Methodology fabrication: CLEAR with note (Methods match code and data; weights note n2; plan deviations disclosed). 7 Frame-lock: CLEAR for the research frame; the novelty framing in Section 6 is the one residue of an earlier frame ("first") and is N1.

## Minor and note items (not blocking under the registered-population rule; at Stage 4.5 the protocol asks for them to be fixed)

- n1 (MINOR_DISTORTION). Introduction and Section 6: "about 2.0% of stock-days ... close at the upper limit (the ceiling)" counts rule-based ceilings (return >= 6.5% and close = high). Only 1,654 of 3,207 are exact tick-rule limit hits (1.06% of 156,653, C13); about half are the "near hits" of Table 2. Say "at or near the upper limit" or give both shares.
- n2. Section 3 says the market return uses weights from the trailing 60-day average dollar volume; Tables 1, C2, C3 use a window that includes day d+1 itself (recomputed: ceiling 1.660 vs 1.667 with strictly lagged weights), while Table 2 and Table 3 use weights lagged to day d. Immaterial for results; the text should say which window each table uses.
- n3. Zeng et al. (2024): the current abstract concerns the net price-limit hitting ratio (upper minus lower hits); Section 2 and Table 5 say "stocks that hit the upper limit often earn lower future returns" and "frequent upper-limit hits". Align to "high net limit-hit ratios".
- n4. Hou et al. (2020) 65% figure applies with microcaps mitigated (value-weighted, NYSE breakpoints); add the condition in Section 2 or Table 5.
- n5. Intro rates (2.0% / 1.4%, event-window denominator 156,653) differ from Section 3 rates (1.98% / 1.30%, all 178,773 stock-days, +6.5 to +7.1 band); the 2.0% statement is repeated in Section 6. State the denominator once and drop the repeat.
- n6. Lu et al. (2023): the abstract stresses fast arbitrageurs, cream-skimming risk and information asymmetry at the open; "inventory of market makers" is a looser paraphrase.
- n7. Data and code availability lists R scripts 40-49 and C-tables; Section 3 statistics come from `R/50_sample_description.R` and table C26.
- n8. Section 2 final sentence of the overnight paragraph ("The overnight studies measure returns on all stocks") follows Jones et al., a retail-trading study, not an overnight study.
- n9. The planned liquidity-screen robustness (bottom 20% excluded; `t_excl_illiq` saved in C1) is neither reported nor listed among departures from the plan.
- n10. VCI and HSC are not defined in the text; Huang X. et al. (2023) and Lin et al. (2023) entries lack the article number (102176 for Huang X.).
- n11 (process only). R/46 T5 prints "pre-registered sample"; the manuscript correctly avoids that word.

## Access-limited notes (UNVERIFIABLE_ACCESS; never block)

- A1. HSC (2025) and Viet Nam News (2025): pages not fetchable (egress block). Search summaries confirm the 5 May 2025 launch and that ATO/ATC orders lose priority over limit orders (HSC; Viet Nam News is consistent). The 7% band, "reference price = previous close on normal days" and "the band stayed unchanged" (cited to HSC) were not found in the HSC record returned; the 7% band appears in broker guides (TCBS) and the return distribution fits it. The manuscript already calls these assumptions and says no primary document was consulted.
- A2. Huang et al. (2001) and Berkman and Lee (2002) were verified through search-returned abstract summaries (IDEAS, ScienceDirect) only; no full text.
- A3. Qiao and Dam (2020) "T+1 lowers opening prices" rests on the abstract summary.
- A4. Tick sizes and sessions after the KRX move are unverified assumptions (disclosed in Section 3 and Limitations).

## Comparison with Stage 4.5 v1 and Stage 3' re-review

All v1 items (M1 522 count, M2 tercile garble, M3 log gap, m1-m8) are resolved or irrelevant to this version. Re-review M1-M6 and m1-m17 are resolved (above). One new defect arises in this version: N1 (the acknowledgement of the HOSE precedent was removed while the priority claim stayed).

## Required to reach PASS

Fix N1 (bound or remove "the first for this market"; attribute the unfilled-order mechanism or cite the precedent). Then re-verify that sentence only. Fixing n1-n10 is recommended at the same time because Stage 4.5 counts minor items.
