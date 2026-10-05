# Stage 3' re-review (verification mode): revision for literature review, data source, and comparison with reviewed studies

Reviewed: `paper2/manuscript/manuscript_final.Rmd` and rendered docx (docx timestamp matches the Rmd, so the text read is current). Evidence file: `paper2/process/08_literature_review_benchmark.md` (the authority for what each source says). Data: `data/`, `paper2/output/tables/`. Method: attribution check of every cited finding against the evidence file; reference/citation cross-match; independent recomputation in R from `data/raw`; table-to-text cross-check; cross-reference and consistency read. Nothing was edited. Re-review is evidence-first: each item below was checked against the files, not against the author's statement of what was done.

## 1. Status of the three requests

| Request | Verdict | Evidence |
|---|---|---|
| (1) Clear, separate literature review with recent strong studies | Resolved, with attribution defects | Section 2 is a standalone section with Theory / Classic evidence / Recent band-change and investor-level evidence / Overnight-intraday / Multiple testing / Gap and hypotheses. About 35 sources, a majority from 2018 to 2025 (Chen et al. 2019, Qi 2023, Zhang 2022, Jia 2024, Zeng 2024, Lin 2023, Liang and Hu 2025, Lou 2019, Akbas 2022, Lu 2023, Qiu 2025, Jones 2025, Chen H. 2024). No GitHub/SSRN/NBER/blog source appears (grep and reference list checked; the excluded Gao et al. NBER, Veeraraghavan SSRN and the GitHub repository are absent). Defects: M1 to M4 below (three findings attributed beyond what the evidence file records, DOIs not in the evidence file). |
| (2) Clear data-source description | Resolved (two small imprecisions) | Section 3 "Data source" matches the files: vnstock 4.0.4 (`data/fetch_stdout.txt`: "Current: 4.0.4"), VCI, retrieved 24 Sept 2026, listing file 743 rows (`wc` gives 743 data rows; 405 STOCK, 314 CW, 21 ETF, 3 unit trust; all exchange code HSX), 405 files (405 in `data/raw` and `fetch_log.txt`), 519 days 21 Aug 2024 to 23 Sep 2026 (recomputed: 519, 2024-08-21, 2026-09-23), 347 kept (recomputed 347). Limits stated (no corporate-action adjustment documentation, no market cap/order book/investor type/news). Imprecisions: m6, m7. |
| (3) Comparison of every result group with reviewed studies, incl. Table 5 | Partial | Table 5 exists with 11 rows and a candid "no comparable magnitude" statement (consistent with evidence file Section 2 and with our tables). Comparisons are present for: the 22-characteristic null (Hou, Harvey, Chordia, Huang X.), the ceiling/floor tests (Berkman and Lee, Kim and Rhee, Qi), the decomposition (Berkman 2012, Lou, Akbas, Huang 2001, Chen 2019, Qiao and Dam), the discontinuity contrast (Cho, Chen H. 2024), and the KRX split (Lien, Kim and Jun, Qi, Zhang). Not resolved: the comparison for the tradability result (H4; next-open buyer) and for the hypotheses as such has no study to compare to and is not stated as such; two comparisons are not fair to our own numbers (M5); Table 5 row for Berkman and Lee and Kim and Rhee rests on attributions the evidence file does not support (M1, M2). |

## 2. Issues by severity

### Major (text-only fixes; no re-analysis needed)

**M1. Berkman and Lee (2002): finding and DOI are not supported by the evidence file.**
Quotes: Section 2 "Berkman and Lee (2002) report more continuations after limit hits in Korea"; Section 5 "matches the more frequent continuation after limit hits that Berkman and Lee (2002) report for Korea"; Section 6 "Berkman and Lee (2002) report more continuation after limit hits in Korea"; Table 5 row "Berkman and Lee (2002) | Korea; limit revision | More frequent continuation after limit hits | Same direction; no magnitude comparison". Evidence file entry 2 and Section 4A: "Bibliographic record only; abstract not retrieved; finding not stated here. Status: record-level only", "No DOI seen". The reference list nevertheless carries `https://doi.org/10.1016/S0927-538X(02)00040-9`. "limit revision" in Table 5 appears nowhere in the evidence file. (An earlier gate file, `review/integrity_stage2_5_independent.md` line 34, says an abstract "limit-hit stocks show more price continuations" was seen, but it contradicts the later evidence file, and the same file set records Berkman and Lee as "abstract/bibliographic level only".)
Fix: either read the paper (or a retrievable abstract) and record the verbatim abstract in the evidence file before keeping the claim, or soften every instance to "Berkman and Lee (2002) study the Korean limits" and delete the Table 5 finding and the "limit revision" setting; delete the DOI unless resolved. Three places plus Table 5 must change together.

**M2. Kim and Rhee (1997) credited with a finding the evidence file does not record.**
Quote (Section 6): "Kim and Rhee (1997) read return continuation after limit hits as delayed price discovery". Evidence entry 1: the record says only that their evidence supports all three hypotheses (volatility spillover, delayed price discovery, trading interference); it does not mention return continuation. Table 5 "Same direction: ceiling closes are followed by a significant return the next day" likewise implies a continuation result that Kim and Rhee are not recorded as reporting. Section 5's "fits the delayed price discovery of Kim and Rhee (1997)" is acceptable (hypothesis label only).
Fix: "Kim and Rhee (1997) find support for delayed price discovery, among other hypotheses, in Tokyo"; Table 5 relation: "Delayed price discovery is one of three hypotheses they support; ours is a return-based check of that hypothesis, with no volatility test".

**M3. Lou, Polk and Skouras (2019) credited with a heterogeneous-trader explanation that the evidence file attributes to other papers.**
Quotes (Section 6): "Lou et al. (2019) show that overnight and intraday returns have different persistence and that heterogeneous traders can explain the difference"; "Lou et al. (2019) trace the split between overnight and intraday returns to heterogeneous traders." Evidence entry 29 records continuation in both periods with an offsetting cross-period reversal, profits earned "entirely overnight or entirely intraday"; the clientele/noise-trader versus arbitrageur account is recorded for Akbas et al. (2022, entry 32) and the market-maker channel for Lu et al. (2023, entry 33). "Different persistence" also misstates "strong continuation in both periods".
Fix: attribute the clientele argument to Akbas et al. (2022) and Lu et al. (2023), and describe Lou et al. as "overnight and intraday continuation with an offsetting cross-period reversal".

**M4. DOIs present in the reference list that the evidence file does not show (verifiability rule: DOIs only where the record shows them).**
Evidence file shows "No DOI seen" or carries them only "from the 04 log, not re-retrieved" for: Berkman and Lee (2002); Chen Y.-M. (1993) (`10.1016/0927-538X(93)90005-3`); Berkman et al. (2012); Lou et al. (2019); Harvey, Liu and Zhu (2016) (`10.1093/rfs/hhv059`). The 04 log lists Harvey et al. as "AUTHOR-SUPPLIED or recalled; NOT re-verified", and records that the DOI resolver and Crossref were unreachable; the DOIs for Amihud, Bali et al., Benjamini and Hochberg, Corwin and Schultz, Fama and MacBeth, Newey and West, Parkinson also have no recorded verification step in the files read. Berkman 2012 and Lou 2019 DOIs appear in later gate files (`integrity_stage2_5_independent.md`, `citation_audit_phase5a.md`), so they have some trail; Berkman and Lee and Chen 1993 do not (first appear in the pre-4b manuscript).
Fix: resolve each DOI (doi.org or Crossref) outside the blocked proxy or remove it; record the check in the evidence file.

**M5. Two comparisons are not fair to our own results.**
(a) Quote (Section 5): "The floor result echoes the stronger lower-limit effects that Qi (2023) finds on ChiNext." and Table 5 Qi row "Same direction at both limits". Qi's record concerns price, volume and volatility hypotheses ("more serious negative effects when lower limits are hit"), not signed returns, so "same direction" has no referent; and in our own tables the next-day effect is weaker at the floor than at the ceiling (close-to-close −0.71 vs +1.66, gap −0.97 vs +2.24; Tables 1, 2), the floor result is benchmark-dependent (−0.69 vs −1.65, Table 2), and only the five-day effect is larger at the floor (−1.76 vs +1.45). Fix: "Qi (2023) finds stronger effects on market quality at the lower limit; our floor results are not stronger than the ceiling results at day d+1 and depend on the benchmark" or drop the echo claim; change Table 5 relation to "Different outcome (market quality); no direct comparison".
(b) Quote (Section 5): "so the ceiling gap does not reflect a general overnight pattern in emerging markets". Qiao and Dam (2020) cover China A-shares only, and a single contrast does not support a statement about emerging markets. Fix: "does not reflect the negative average overnight return that Qiao and Dam document for China".

**M6 (abstract vs results). The abstract's tradability claim contradicts the body.**
Quote (Abstract): "A buyer at the next open earns nothing from it." Section 5 reports −0.75% through the fifth close (t = −2.7) and −0.53% against controls (t = −1.8); the Conclusion says "earns −0.75%". "Nothing" is not what a significantly negative estimate shows, and the Conclusion and abstract disagree. Fix: "A buyer at the next open earns no part of it (−0.75% by the fifth close against the market)".

### Minor

m1. Hendershott, Livdan and Rösch (2020): "link overnight and intraday returns to market beta" (Section 2). The evidence file has the beta statement only from a secondary snippet (abstract not displayed). Fix: "study overnight and intraday returns in an asset-pricing framework", or read the abstract before keeping the beta link.

m2. Kim and Limpaphayom (2000): Quote "small, volatile, high-volume stocks account for most limit hits". Record: such stocks "are more likely to hit limits". "Account for most" is a magnitude not recorded. Fix: "are more likely to hit limits".

m3. Huang, Fu and Ke (2001) is secondary-description only (evidence entry 4: "secondary description, abstract not displayed"), yet the Table 5 caption says columns summarize "each source as stated in its abstract or record", and Section 5 states "it matches the correction ... that Huang et al. (2001) report". Fix: add "(as described in a secondary record)" in the table cell or confirm the abstract; keep qualitative wording.

m4. Huang et al. (2023): Quote (Section 2) "they report no post-limit return" and (Section 5) "our null does not contradict theirs". The first is an inference from a record the evidence file calls "reports no post-limit-hit return" but the abstract was not read in full. Fix: "we found no post-limit return in their abstract".

m5. Le (2012) is not in the 08 evidence file (verified only in `integrity_stage2_5_round2.md`, from ResearchGate/Academia records). Its peer-review status in a Vietnamese journal is not established, and the manuscript uses it as support for "studies the effect of a narrower limit on stock price risk with GARCH". Fix: add it to the evidence file with source and abstract text, or label it a local journal paper.

m6. Data section: "The retrieval returned 405 HOSE stock files with 519 trading days from 21 August 2024" is imprecise. The files hold the last 519 records per stock (13 files have fewer, e.g. AAN 86, LPS 24), and 14+ files contain rows dated before 21 Aug 2024 (e.g. ASG 114 rows, first 2024-03-01) that the analysis discards (5,544 rows before 21 Aug 2024 in total). Fix: "each file holds up to 519 daily records; the analysis uses the 519 market trading days from 21 August 2024 and drops earlier rows; 13 stocks have fewer records". Also say that 405 is the count of STOCK-type rows in the 743-row listing.

m7. Data section: "the median stock-day has a dollar volume of 2.6 billion dong and the mean is 51.2 billion dong" are computed over all stock-days with a price, not over the 178,773 stock-days with a return that the previous sentence names (return-day subset gives 2.58 and 51.3). Immaterial, but align the denominator wording.

m8. Cross-reference error: Section 5 final paragraph, "What the evidence does not settle is why the gap arises, and Section 5 returns to that question." This is in Section 5; it should read Section 6.

m9. Hypotheses H1 to H4 are never referred to again after Section 2 (H1 recurs once in Section 4). Results (Sections 5 to 8) do not say which hypothesis each result supports, so the reader cannot check the claim in the abstract against the hypotheses. Fix: add labels in Section 5 ("H1 is supported ... H3 ...") and a sentence in the Conclusion. Also the abstract's "26 hypotheses" collides with "four hypotheses" in Section 2; use "26 tests".

m10. Repeated claims: "The 22 characteristics give a benchmark for H1 ... more credible than a single large estimate" appears verbatim in Section 2 and Section 4; "about 2.0% of stock-days ... close at the ceiling" in Section 1 and Section 6; the 65% of 452 result in Sections 2, 5 and Table 5; "none of these studies reports ... overnight and intraday parts" four times. Delete the Section 4 sentence and the Section 6 repeat; keep one statement of the gap.

m11. Undefined abbreviations on first use: T+1 (Section 2), GARCH (Section 2), VCI (Section 3), HSC (in-text, defined only in the reference list), HNX not used. Define or drop.

m12. Intro and Section 3 give different limit shares for the same facts: "about 2.0% ... ceiling and about 1.4% at the floor" (event-window denominator 156,653; 2,115/156,653 = 1.35%, and Table 1's own floor count 2,105 gives 1.34%, which rounds to 1.3%) versus "1.98% ... 1.30%" (all 178,773 stock-days, +6.5% to +7.1% band). State the denominator in the introduction or use 1.3%.

m13. Section 5: "After floor closes, prices keep falling from the next open to the fifth close (Table 2)". Table 2 shows −0.82 (t = −1.7) against the market and −0.36 (t = −0.6) against controls; neither is significant. Fix: "point estimates stay negative but are not significant".

m14. Section 1: "many exchanges in Asia keep them for every listed stock" and Section 3 "allows a wider band on the first trading day of a new listing (HSC, 2025)" are not recorded in the evidence file for the cited source (evidence file 4B records HNX 30% for newly listed per broker guides, and says primary text was not opened). The Declarations already disclose that institutional facts were not checked against primary documents; add the source or hedge. Likewise "the band stayed unchanged" at the KRX move is not recorded for HSC.

m15. Section 6 opens "The evidence is consistent with delayed price discovery", while Section 5 states that three readings fit and the data cannot separate them, and the abstract says the same. Fix: open Section 6 with the three-reading statement.

m16. Chen (1993): "which he reads as a delay": the author's gender is not in the record. Use "which is read as a delay".

m17. Section 2, Chinese-evidence sentence ends "These studies measure overnight returns on all stocks and none conditions on a limit close", but the list includes Jones et al. (2025), which is a retail-trading study and not an overnight-return study. Reorder.

### Passed checks (no issue found)
- Every other attribution checked in Sections 1, 2, 5, 6 and Table 5 agrees with the evidence file: Brennan; Kodres and O'Brien; Greenwald and Stein; Subrahmanyam; Chen H. et al. (2024); Bildik and Gülay; Chen T. et al. (2019; none of the UNVERIFIED numbers 2.44%, 2.59%, 83.6% is used); Cho et al.; Deb et al. (2013); Qi; Zhang; Jia; Lien; Kim and Jun; Lin; Zeng; Liang and Hu; Kelly and Clark; Berkman et al. (2012); Aboody; Akbas; Bogousslavsky; Lu; Qiao and Dam; Qiu; Harvey et al.; Harvey and Liu; Chordia (3.38 given as "near 3.4"); Hou (65% of 452, 1.96); Petersen; Gutierrez and Kelley. The UNVERIFIED magnitudes (Lou "2% per month", Hendershott 14/-15 bp, Chen et al. numbers) are not in the manuscript.
- Citation/reference cross-match: every in-text citation has a reference entry and every reference is cited (checked by reading both lists; 47 entries). No unsupported DOI beyond M4.
- No non-peer-reviewed scholarly source is used as evidence. HSC (2025) and Viet Nam News (2025) are used only for institutional facts and are labelled as web page and news article.
- Section 1 to 8 numbering consistent; only cross-reference error is m8.
- Process leakage: no mention of reviewers, agents, pipeline, rounds or stages in the manuscript text. The analysis-plan and version-control sentences (Section 4) and the Claude disclosure are legitimate transparency statements; the repository path, commit and `paper2/R/40 to 49` appear only in the Data and code availability statement. The Rmd setup chunk has a local absolute path but it is not rendered.
- Hypotheses versus results: the numbers support H1 (both signs, both horizons), H2 (ceiling and floor gaps carry the day-d+1 effect), H3 (Table 3), H4 (ceiling, open to day 5 −0.75%); the only wording problem is M6.

## 3. Numeric spot-check log

Independent recomputation in R from `data/raw` (restricted to 2024-08-21 onward; 347 stocks kept with at least 95% non-missing closes; returns defined only where the close exists on two consecutive market trading days). Script in the session scratchpad (`chk.R`); no project file changed.

| # | Statistic | Manuscript / C26 | Recomputed | Result |
|---|---|---|---|---|
| 1 | Files in `data/raw`; listing rows | 405; 743 | 405; 743 (405 STOCK) | Match |
| 2 | Trading days, first and last date | 519; 21 Aug 2024 to 23 Sep 2026 | 519; 2024-08-21; 2026-09-23 | Match |
| 3 | Stocks kept (at least 95% closes) | 347 | 347 | Match |
| 4 | Stock-days with a return | 178,773 | 178,773 | Match |
| 5 | Mean daily return (%) | 0.018 (0.01788) | 0.01788 | Match |
| 6 | SD of daily return (%) | 2.10 (2.0982) | 2.0982 | Match |
| 7 | Median daily return | 0.00 | 0 | Match |
| 8 | Sectors (2-digit ICB among kept); largest share | 18; 15% (14.986) | 18; 14.986% | Match |
| 9 | Median and mean dollar volume (million VND) | 2,557.7; 51,226 | 2,557.7; 51,226 over all stock-days with a price (2,582; 51,349 on return days only) | Match, denominator note m7 |
| 10 | Pile-up shares: +6.5 to +7.1; -7.1 to -6.5; +6.0 to +6.5 (%) | 1.98; 1.30; 0.29 | 1.984; 1.303; 0.2875 | Match |
| 11 | Returns beyond ±8% | 96 | 96 | Match |

Text-to-table checks (CSV values): Table 1 versus C2/C3/C20 (1.66, 1.45; -0.71, -1.76; halves 2.2/13.7 and -12.3/-2.2; BH p from 2.6e-06 to 4.0e-04) match; events 3,187/446 dates, 2,105/319 dates match; Table 2 versus C16 (2.24, -0.54, 1.66, 2.70, 522 locked, tercile 1.52, floor tercile t = -0.97) match; Table 3 versus C17/C23 (2.66, 14.0, 3.14, -1.59, -1.81, 2.40, -1.14) match; Table 4 versus C22 (1.65, 2.49, 0.85, -0.42, -1.37, -0.95, 0.64, -1.73, -0.15; 71% and 58% shares) match; C24 terciles (1.97, 2.16, 2.63; 1.41, 2.18, 3.16; floor -1.20 to -0.68) match; C1/C14: largest full-sample |t| 1.45 (3-month 1.452, idiosyncratic 1.448), conf t 1.17/1.14, lag-8 largest 1.79, MDE 0.12 to 0.31, 18 of 22 negative after 25 bp (4 positive: MOM3M, MOM6M, IMOM, LNDVOL), none reaches 1.96, all match; C21 (683 and 125 tests; 7.3e-05, 4.0e-04) and C25 (2.24 to 2.26; -0.97 to -0.98) match. No numeric discrepancy found; the issues above are attribution, wording and consistency.

## 4. Recommendation

**Major Revision (text-only; no re-analysis, no new computation).** The data section, the numbers and the structure of Sections 2 and 5 are sound, and the candid "no comparable magnitude" framing is correct. But the request-3 comparisons contain attributions that the evidence file does not support (Berkman and Lee finding and DOI, Kim and Rhee continuation, Lou heterogeneous traders), unresolved DOIs, and one unfair comparison (Qi), plus an abstract statement that contradicts the body. Under the pipeline rule these are integrity-relevant and must be fixed before Stage 4.5. If M1 to M6 are fixed as suggested and m8 and m9 corrected, the paper moves to Accept for this round; the remaining minor items can be handled in the Stage 4.5 pass.
