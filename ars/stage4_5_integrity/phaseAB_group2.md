# Stage 4.5 Final Integrity Check: Phase A + Phase B, Reference Group 2 (R12 to R21)

Agent: `integrity_verification_agent` (ARS academic-research-skills v3.22.1), Mode 2 (final-check), fresh context
Run date: 2026-09-24
Input: `/home/user/B-i-FTSE2/ars/stage4_5_integrity/refgroup2.md`
Scope: Phase A (A0/A1/A2) for 10 references; Phase B for 100% of the 25 registered citation contexts in this group. The manuscript was not edited.

## Skill load record

Each file was read with the Read tool from the ARS root `/tmp/claude-0/-home-user-B-i-FTSE2/88a51032-601f-5b56-b6d6-c6001a62ef1c/scratchpad/academic-research-skills` (git HEAD `6234edf`):

| # | File | First heading line |
|---|------|--------------------|
| 1 | `academic-pipeline/SKILL.md` | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| 2 | `academic-pipeline/agents/integrity_verification_agent.md` (all 887 lines) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| 3 | `academic-pipeline/references/integrity_review_protocol.md` | `# Integrity Review Protocol (Added in v2.0)` |
| 4 | `academic-pipeline/references/claim_verification_protocol.md` | `# Claim Verification Protocol (Phase E)` |
| 5 | `deep-research/references/semantic_scholar_api_protocol.md` | `# Semantic Scholar API Verification Protocol` |

Rules applied from these files:
- A1 accepts only VERIFIED, NOT_FOUND or MISMATCH, and requires 3 query variants before NOT_FOUND.
- Every reference has an A2 audit trail (query, top URL, fields confirmed).
- No gray-zone verdicts are used.
- Phase B runs only on references that have an explicit Phase A verdict.
- Severity map. A2: SERIOUS = author/year/journal/DOI error; MEDIUM = omitted co-author, title imprecision or page error; MINOR = formatting or dead URL. Phase B: MAJOR_DISTORTION = SERIOUS, UNVERIFIABLE = SERIOUS, UNVERIFIABLE_ACCESS = MEDIUM, MINOR_DISTORTION = MINOR.

## Environment and method

- **A0: `API_UNAVAILABLE` for all 10 references.** The proxy returned 403 on CONNECT to `api.crossref.org`, `api.openalex.org` and `api.semanticscholar.org` (proxy status log, 2026-09-24 07:44–07:45Z), so A0 was skipped. A1 ran by WebSearch for every reference.
- **WebFetch could not reach any host tried.** The egress proxy blocked `www.lseg.com`, `research.ftserussell.com`, `ideas.repec.org`, `vir.com.vn`, `theinvestor.vn`, `en.vietnamplus.vn`, `acbs.com.vn`, `blogs.duanemorris.com` and `www.mondaq.com`. As a result, all source text below comes from WebSearch result snippets: publisher abstract text, index-page snippets and news summaries. No full text was retrieved.
- Retrieved content was treated as data. None of it contained instructions aimed at the verifier.

---

## R12: FTSE Russell (2018), *FTSE classification of markets: September 2018*

**A1: VERIFIED**

**A2 field check**

| Field | Reference | Found | Status |
|---|---|---|---|
| Author | FTSE Russell | FTSE Russell | OK |
| Date | 2018-09-26 | Annual Country Classification Review published 26 September 2018 | OK |
| Title | FTSE classification of markets: September 2018 | PDF title "FTSE Classification of Markets" (research.ftserussell.com/products/downloads/FTSE-Country-Classification-Update-2018.pdf); LSEG-hosted copy indexed as "ftse country classification update 2018" | OK. The ": September 2018" subtitle is descriptive (MINOR formatting only, optional) |
| URL | lseg.com/.../ftse-country-classification-update-2018.pdf | Same URL is indexed by the search engine; the host is blocked from here, so it could not be opened | OK (indexed) |

**Audit trail**
- Q1 "FTSE Russell September 2018 country classification Vietnam added watch list secondary emerging". Top URLs: vietnamplus.vn/ftse-russell-adds-vietnam-to-watch-list-for-reclassification/139155.vnp and the lseg.com 2018 PDF.
- Q2 `"FTSE Equity Country Classification" "September 2018 Annual Announcement"`.
- Q3 `FTSE Russell "Annual Country Classification Review" September 2018 Vietnam "Secondary Emerging" watch list Argentina Tanzania`. Top URL: research.ftserussell.com/products/downloads/FTSE-Country-Classification-Update-2018.pdf, title "FTSE Classification of Markets".
- Fields confirmed: issuer, date 26 Sep 2018, title, and the Vietnam watch-list content.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| 1 | "FTSE Russell added Vietnam to its watch list for possible reclassification in September 2018 (FTSE Russell, 2018)." | SUPPORTED | "Vietnam is currently classified as a Frontier market and is being added to the watch list for possible reclassification as Secondary Emerging." Review "published on September 26, 2018 … new additions to the Watch List including Argentina, Tanzania, and Vietnam." |
| 2 | "Vietnam sat on the FTSE watch list for seven years (FTSE Russell, 2018)…" | MINOR_DISTORTION | The 2018 document supports only the start of the watch-list period. The end point (the 7 Oct 2025 decision) comes from LSEG (2025), so the seven-year duration cannot be attributed to FTSE Russell (2018) alone. Fix: cite "(FTSE Russell, 2018; LSEG, 2025)". |

---

## R13: FTSE Russell (2026, August), *Reclassification of Vietnam from frontier to secondary emerging market status: FAQ* (Version 1.3)

**A1: VERIFIED.** The document exists at the cited URL with this title. Search indexes the PDF as "ftse faq document vietnam reclassification" and as "lseg.com/en/ftse-russell April 2026 Reclassification of…". The FTSE notice is titled "Reclassification of Vietnam to Secondary Emerging Market Status FAQ" (research.ftserussell.com notice id=2619334).

**A2 field check**

| Field | Reference | Found | Status |
|---|---|---|---|
| Author | FTSE Russell | FTSE Russell | OK |
| Title | Reclassification of Vietnam from frontier to secondary emerging market status: Frequently asked questions | "Reclassification of Vietnam from Frontier to Secondary Emerging Market Status - FAQ" | OK |
| Version / date | Version 1.3, August 2026 | Independently indexed versions: **v1.0 (November 2025)** and **v1.2 ("updated copy of the FAQ (v 1.2)", effective 20 April 2026)**. The PDF at the cited URL is indexed with the header "**April 2026**". Five query variants found no trace of v1.3 or an August 2026 date. | **MEDIUM**: version and date not confirmed. The author must check the version and date on the downloaded copy. If it is v1.3, keep the reference and archive the copy. Otherwise correct to "(2026, April) … (Version 1.2)". |
| URL | lseg.com/.../ftse-faq-document-vietnam-reclassification.pdf | Indexed at the same URL | OK |

**Audit trail**
- Q1 "FTSE Russell Vietnam reclassification FAQ … tranches 10% 20% 35% 35% investability weight". Top URL: the lseg.com FAQ PDF. Confirmed: tranches 10/20/35/35 and tranching factors 10/30/65/100%.
- Q2 `"Reclassification of Vietnam from Frontier to Secondary Emerging Market Status" "Frequently Asked Questions"`. Found: the FAQ title, v1.0 November 2025, and the notice at research.ftserussell.com id=2619334.
- Q3 `FTSE Russell Vietnam FAQ "version 1.3" OR "v1.3" August 2026`. Found: v1.0 (Nov 2025) and v1.2 (effective 20 Apr 2026). No v1.3.
- Q4 "FTSE Russell Vietnam FAQ updated August 2026 final list …". Found: v1.2 only.
- Q5 `"investability weight of 49%" FTSE`. Top hit: the FAQ PDF, indexed as "lseg.com/en/ftse-russell April 2026 Reclassification of".
- Fact queries: tranche dates 22 Mar 2027, 21 Jun 2027, 20 Sep 2027; 27 constituents; implementation after the close of 18 Sep; the 30 June cut-off; screens.

**Grey-literature fact check (items in the dispatch)**

| Fact attributed | Result | Source |
|---|---|---|
| Announcement 7 Oct 2025 | Confirmed | LSEG 7 Oct 2025 press release, via WebSearch snippet |
| Confirmation 7 Apr 2026 | Confirmed | LSEG 7 Apr 2026 press release, via WebSearch snippet |
| Effective 21 Sep 2026 | Confirmed ("effective from the open on Monday 21 September 2026") | LSEG 7 Apr 2026 |
| Tranches 10/20/35/35% on 21 Sep 2026, 22 Mar 2027, 21 Jun 2027, 20 Sep 2027 | Confirmed: "21 September 2026: 10% inclusion, 22 March 2027: additional 20% (cumulative 30%), 21 June 2027: additional 35% (cumulative 65%), and 20 September 2027: additional 35% (cumulative 100%)". FAQ tranching factors are 10/30/65/100%. | Duane Morris/Conventus summaries; FAQ snippet |
| Interim review March 2026 | Confirmed | FAQ snippet: "effective from the September 2026 semi-annual review subject to an interim assessment in March 2026" |
| Final list published Friday 21 Aug 2026 | Confirmed: "The final list … will be published on Friday 21 August 2026 and they will be screened based on Vietnam securities being non-constituents" | FAQ snippet |
| 27 constituents | Confirmed ("FTSE Russell names 27 Vietnamese stocks in review"; "A total of 27 Vietnamese stocks were added") | VIR; theinvestor.vn |
| Effective after the close of 18 Sep 2026 | Confirmed: "implemented after the close of trading on September 18 and became effective on September 21, 2026" | WebSearch summary of theinvestor.vn/VIR |
| Selection on data as of 30 June 2026 | **Not directly confirmed.** Consistent with the GEIS rule that the September-review liquidity period ends on the last business day of June (30 June 2026 is a Tuesday). No retrieved snippet of the FAQ states "30 June 2026". | GEIS rule snippet |
| Investability-weight screening | Confirmed: "if a security has an investability weight of 49% on the final day of the liquidity-testing period, it will be assessed for liquidity using its 49% investability weight". Also: "Vietnamese securities will be treated as non-constituents … for all the eligibility screens such as liquidity and minimum size". | FAQ PDF snippet |
| 49% investability weight phased in at 4.9% after the first tranche | **Not found.** The FAQ's only indexed 49% example concerns liquidity testing, not tranche phasing. 4.9% = 49% × 10% is correct arithmetic under the tranche factors, but no text was found showing that the FAQ presents this as its own illustration. | The FAQ's 49% example appears in its snippet only as a liquidity-testing example |

**Phase B**

| # | Context (abridged) | Verdict | Source text / basis |
|---|---|---|---|
| 1 | Abstract: four public steps between Oct 2025 and Sep 2026 | SUPPORTED | The dates for all four steps are confirmed above |
| 2 | Amihud results sentence: "27 stocks FTSE had screened as eligible on 2024 data"; confirmation April 2026; constituents named August 2026 | SUPPORTED (FTSE facts only; the estimates are the paper's own) | Preliminary list Nov 2025 on 31 Dec 2024 data: "FTSE Russell lists 28 Vietnamese stocks eligible" (theinvestor.vn). 28 = 27 on HOSE + HUT on HNX, which matches the table. The April 2026 and 21 Aug 2026 dates are confirmed. |
| 3 | Four dated steps: 7 Oct 2025, 7 Apr 2026, 21 Aug 2026, 21 Sep 2026 | SUPPORTED | As above |
| 4 | "FTSE selected the final constituents on data as of 30 June 2026 (FTSE Russell, 2026)" | UNVERIFIABLE_ACCESS | FAQ full text could not be retrieved. The date is consistent with the GEIS September-review liquidity period ending on the last business day of June, but no retrieved FAQ text states the date. |
| 5 | Tranches 10/20/35/35% on 21 Sep 2026, 22 Mar 2027, 21 Jun 2027, 20 Sep 2027 | SUPPORTED | "The investability weight added in each tranche is: 10%, 20%, 35%, and 35%, with corresponding tranching factors of 10%, 30%, 65%, and 100%", plus the dates quoted above |
| 6 | 21 Aug 2026 publication; 27 constituents; data as of 30 June 2026; effective after the close of 18 Sep 2026 | UNVERIFIABLE_ACCESS (on the 30 June element only; the other elements are SUPPORTED) | See the fact table |
| 7 | Screens on liquidity, minimum size and foreign headroom as non-constituents, "using each security's investability weight (free float) in the liquidity test" | MINOR_DISTORTION | The screens and investability-weight use are supported ("assessed for liquidity using its 49% investability weight"; "treated as non-constituents … for all the eligibility screens such as liquidity and minimum size"). However, FTSE defines investability weight as "the more restrictive of free float and any applicable foreign ownership restriction". Glossing it as "(free float)" is inaccurate for Vietnam, where foreign ownership limits often bind. Fix: "(free float, capped by the foreign-ownership limit)". |
| 8 | "FTSE's own illustration phases in a security with a 49% investability weight at 4.9% after the first tranche and at 49% after the last (FTSE Russell, 2026)" | UNVERIFIABLE_ACCESS (**elevated risk**) | The only indexed 49% example in the FAQ is a liquidity-testing illustration. No text shows FTSE presenting a 4.9%/49% phasing example. Fix: the author must quote the FAQ passage and page, or reword as the authors' own calculation ("under the 10% tranching factor, a security with a 49% investability weight enters at 4.9%…") without attributing the illustration to FTSE. |
| 9 | Table "Stocks by FTSE list" (sources include FTSE Russell, 2026) | UNVERIFIABLE_ACCESS | Only partly confirmed: VCB, VIC, VHM (large cap) and BID, VPB, HPG (mid cap) are among the 27; the 28-stock (Nov 2025) and 32-stock (Apr 2026) eligible lists exist (theinvestor.vn). The full ticker-level membership could not be retrieved. |

---

## R14: Gregoriou & Nguyen (2010), *Journal of International Financial Markets, Institutions and Money*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Gregoriou, A.; Nguyen, N. D. (2 authors)
- Year: 2010
- Title: "Stock liquidity and investment opportunities: New evidence from FTSE 100 index deletions"
- Journal, volume, issue and pages: JIFMIM 20(3), 267–274
- DOI: 10.1016/j.intfin.2010.03.005

**Audit trail**
- Q1: full title + authors + journal. Top URLs: sciencedirect.com/science/article/abs/pii/S1042443110000089 and repository.mdx.ac.uk/item/82605, confirming all fields and the DOI.
- Q2: abstract terms "exogenous liquidity shock".
- Q3: `"Gregoriou and Nguyen (2010)" … find`.
- Q4: "findings contradict" query.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| 1 | "Becker-Blease and Paul (2006) find that firms added to the S&P 500 with larger liquidity improvements increase capital investment, and Gregoriou and Nguyen (2010) find the mirror pattern for FTSE 100 deletions." | **MAJOR_DISTORTION** | Four independent search summaries of the paper and its citing literature agree that G&N find no association. "Gregoriou and Nguyen (2010) find that index deletions do not have a significant impact on corporate investment opportunities, whereas Becker-Blease and Paul (2006) find strong evidence…". "They find no statistical association between stock liquidity and investment opportunities … firms should still be able to borrow at the same cost of capital even after a negative liquidity shock". "Somewhat surprisingly, their findings contradict the extensively reported positive relationship between liquidity and investment opportunities for the US equity market." The manuscript states the opposite. Fix: "…whereas Gregoriou and Nguyen (2010) find no significant effect of FTSE 100 deletions on investment." |

---

## R15: Harris & Gurel (1986), *The Journal of Finance*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Harris, L.; Gurel, E. (2 authors)
- Year: 1986
- Title: "Price and volume effects associated with changes in the S&P 500 list: New evidence for the existence of price pressures"
- Journal, volume, issue and pages: JF 41(4), 815–829 (afajof.org lists Volume 41, Issue 4, September 1986)
- DOI: 10.1111/j.1540-6261.1986.tb04550.x (Wiley)

**Audit trail**
- Q1: full title + journal/volume. Top URL: onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1986.tb04550.x, confirming all fields. Also IDEAS v41y1986i4p815-29.
- Q2: abstract phrases.

**Phase B.** Source abstract: "Attempts to identify price pressures caused by large transactions may be inconclusive if the transactions convey new information … addressed through an examination of prices and volume surrounding changes in the composition of the S&P 500 … The results are consistent with the price-pressure hypothesis: immediately after an addition is announced, prices increase by more than 3 percent, and this increase is nearly fully reversed after 2 weeks."

| # | Context | Verdict | Basis |
|---|---|---|---|
| 1 | "additions force passive funds to buy on the effective date, which produces temporary volume and price effects that reverse afterwards (Harris & Gurel, 1986)" | MINOR_DISTORTION | Temporary price and volume effects that reverse, and the index-fund demand channel, are supported. However, H&G measure the effect "immediately after an addition is announced". In their pre-1989 sample, announcement and effective date were not separated, so "on the effective date" is not what the source isolates. Suggest "around the change" instead of "on the effective date". |
| 2 | "The fading after the first, conditional announcement is consistent with temporary price pressure (Harris & Gurel, 1986)." | SUPPORTED | Reversal after about 2 weeks is the price-pressure signature |
| 3 | "…funds tracking FTSE benchmarks … bought the first tranche … at the closing price of 18 September … (Harris & Gurel, 1986)" | MINOR_DISTORTION | H&G supports only the general mechanism (index-fund rebalancing creates price pressure). The Vietnam and FTSE specifics (18 September close, first tranche) are not in H&G and should be attributed to FTSE Russell (2026)/VIR (2026), with H&G cited for the mechanism only. |

---

## R16: Hau, Massa & Peress (2010), *Review of Financial Studies*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Hau, H.; Massa, M.; Peress, J. (3 authors)
- Year: 2010
- Title: "Do demand curves for currencies slope down? Evidence from the MSCI global index change"
- Journal, volume, issue and pages: RFS 23(4), 1681–1717
- DOI: 10.1093/rfs/hhp095

**Audit trail**
- Q1: full title + journal. Top URLs: academic.oup.com/rfs/article-abstract/23/4/1681/1590573 and IDEAS v23y2010i4p1681-1717.
- Q2: `"10.1093/rfs/hhp095"`. Journal prefix only.
- Q3: title + "doi hhp095". Confirmed DOI https://doi.org/10.1093/rfs/hhp095, Vol 23 Issue 4, April 2010, pp. 1681–1717.

**Phase B**

| # | Context | Verdict | Source text |
|---|---|---|---|
| 1 | "…an MSCI index change even moved currency values through this channel (Hau et al., 2010)" | SUPPORTED | "…exchange rate effect of a major redefinition of the MSCI Global Equity Index in 2001 and 2002 … produced strong exogenous equity flows by index funds. Countries with a relatively increasing equity representation experienced a relative currency appreciation upon announcement of the index change." |

---

## R17: Hegde & McDermott (2003), *Journal of Financial Markets*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Hegde, S. P.; McDermott, J. B. (2 authors). Journal citations are given in this order ("Hegde, S.P and J.B. McDermott, 2003"). The SSRN working paper lists McDermott first, which is not an error for the journal version.
- Year: 2003
- Title: "The liquidity effects of revisions to the S&P 500 index: An empirical analysis"
- Journal, volume, issue and pages: JFM 6(3), 413–459
- DOI: 10.1016/S1386-4181(02)00046-0

**Audit trail**
- Q1: full title + journal. Top URL: sciencedirect.com/science/article/abs/pii/S1386418102000460. Abstract retrieved.
- Q2: `"Hegde, S. P., & McDermott, J. B. (2003)"`. Author order confirmed.
- Q3: `"10.1016/S1386-4181(02)00046-0"`. DOI resolves to this article, JFM 6(3) 413–459.
- Q4: horizon query ("months after addition").

**Phase B.** Source abstract: "Using a recent sample of S&P 500 additions, we find a sustained increase in the liquidity of the added stocks. The improvement in the liquidity of added stocks is due primarily to a decrease in the direct cost of transacting and a smaller decline in the asymmetric information component … the liquidity of deleted stocks declines over the three months following deletion." Secondary description of the results: "median quoted and effective spreads decrease and the median quoted depth, trading volume and trade frequencies increase over three months following listing."

| # | Context | Verdict | Basis |
|---|---|---|---|
| 1 | "additions to the S&P 500 raise trading activity and narrow spreads **for years** (Hegde & McDermott, 2003)" | **MAJOR_DISTORTION** | The source documents a "sustained" increase measured over roughly three months after addition. No retrieved text supports a multi-year horizon, so "for years" exaggerates the source. Fix: replace with "persistently" or "for at least three months". |
| 2 | "…narrow spreads and raise trading activity persistently, which they attribute to more information and more trading interest." | MINOR_DISTORTION | "Persistently" is supported ("sustained"). The attribution is loosely paraphrased: the authors attribute the improvement "primarily to a decrease in the direct cost of transacting and a smaller decline in the asymmetric information component". Suggest "which they trace mainly to lower direct trading costs and, secondarily, to less information asymmetry". |
| 3 | "developed-market studies that find lasting liquidity gains after inclusion (Hegde & McDermott, 2003)" | SUPPORTED | "sustained increase in the liquidity of the added stocks" |

---

## R18: Ho, Imai, King & Stuart (2007), *Political Analysis*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Ho, D. E.; Imai, K.; King, G.; Stuart, E. A. (4 authors)
- Year: 2007
- Title: "Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference"
- Journal, volume, issue and pages: Political Analysis 15(3), 199–236
- DOI: 10.1093/pan/mpl013

**Audit trail**
- Q1: full title + authors + journal. Top URLs: cambridge.org Political Analysis article page, gking.harvard.edu, SSRN 1081983, which confirm the fields.
- Q2: `"10.1093/pan/mpl013"`. Confirms the DOI maps to this article, 15(3) 199–236.

**Phase B**

| # | Context | Verdict | Source text |
|---|---|---|---|
| 1 | Matched sample: 3 nearest-neighbour propensity-score controls, with replacement, with matching weights (Ho et al., 2007) | SUPPORTED | The source proposes "to preprocess data with matching and then apply parametric techniques … more accurate and considerably less model-dependent causal inferences" (implemented in MatchIt). The citation is a methodological reference for matching as preprocessing. The specific design (3:1, with replacement, weights) is the authors' own choice and is not attributed to the source as a finding. |

---

## R19: Kang & Zhang (2014), *Pacific-Basin Finance Journal*

**A1: VERIFIED**

**A2 field check**: every field matches. No issues.
- Authors: Kang, W.; Zhang, H. (Wenjin Kang, Huiping Zhang; 2 authors)
- Year: 2014
- Title: "Measuring liquidity in emerging markets"
- Journal, volume and pages: PBFJ 27, 49–71
- DOI: 10.1016/j.pacfin.2014.02.001

**Audit trail**
- Q1: title + journal. Top URLs: sciencedirect.com/science/article/abs/pii/S0927538X14000195 and IDEAS v27y2014icp49-71.
- Q2: title + DOI. Confirms DOI 10.1016/j.pacfin.2014.02.001 and vol. 27, pp. 49–71. Also SSRN 2326380 (Wenjin Kang, Huiping Zhang).

**Phase B**

| # | Context | Verdict | Source text |
|---|---|---|---|
| 1 | "Kang and Zhang (2014) show that the Amihud ratio loses accuracy in emerging markets where many days have zero volume, and propose an adjustment" | SUPPORTED | "The authors propose a modified version of the Amihud illiquidity measure, AdjILLIQ, which combines the virtues of the original Amihud ratio and the non-trading-frequency measure … exhibits higher correlation with spread and price impact than other existing low-frequency liquidity measures … particularly significant improvements in inactively-traded markets and low-turnover stocks." The measure includes a zero-volume adjustment. |

---

## R20: LSEG (2025, October 7), *FTSE Russell country classification: September 2025 review* [Press release]

**A1: VERIFIED.** The press release exists at the cited URL with the date October 07, 2025.

**A2 field check**

| Field | Reference | Found | Status |
|---|---|---|---|
| Author | LSEG | LSEG media centre (FTSE Russell) | OK |
| Date | 2025-10-07 | "October 07, 2025" | OK |
| Title | FTSE Russell country classification: September 2025 review | "**FTSE Russell announces results of September 2025 semi-annual country classification review for equities and fixed income**" | **MEDIUM**: title imprecision. The reference title reads like a paraphrase of the URL slug. Correct to the actual headline. |
| URL | lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025 | Indexed at this URL | OK |

**Audit trail**
- Q1: "LSEG press release 7 October 2025 … Vietnam Secondary Emerging effective 21 September 2026 interim review March 2026". Top URL: the lseg.com press release. Content confirmed.
- Q2: "lseg.com media-centre press release October 07 2025 … headline title". Headline confirmed.

**Phase B**

| # | Context | Verdict | Source text |
|---|---|---|---|
| 1 | "On 7 October 2025 it announced that Vietnam would move from frontier to secondary emerging status with effect from 21 September 2026, subject to an interim review in March 2026 (LSEG, 2025)." | SUPPORTED | "Vietnam will be reclassified from Frontier to Secondary Emerging market status with an effective date of Monday 21 September 2026 subject to an interim review in March 2026." |

---

## R21: LSEG (2026, April 7), *FTSE Russell announces results of the March 2026 semi-annual country classification review* [Press release]

**A1: VERIFIED**

**A2 field check**

| Field | Reference | Found | Status |
|---|---|---|---|
| Author | LSEG | LSEG media centre | OK |
| Date | 2026-04-07 | "April 07, 2026" | OK |
| Title | FTSE Russell announces results of the March 2026 semi-annual country classification review | "**FTSE Russell announces results of March 2026 semi-annual country classification review for equities and fixed income**" (Mondo Visione reprint; LSEG URL slug "...-review-equities-fixed-income") | **MEDIUM**: title imprecision. The reference adds "the" and omits "for equities and fixed income". |
| URL | lseg.com/.../ftse-russell-announces-results-march-2026-semi-annual-country-classification-review-equities-fixed-income | Indexed at this URL | OK |

**Audit trail**
- Q1: "LSEG press release 7 April 2026 … Vietnam pre-funding criteria". Top URLs: the lseg.com press release, theinvestor.vn and VIR. Content confirmed.
- Q2: "FTSE Russell April 7 2026 confirms Vietnam … 'meets all' criteria prefunding".
- Q3: exact title in quotes. Top URL: mondovisione.com reprint with the full headline.

**Phase B**

| # | Context | Verdict | Source text |
|---|---|---|---|
| 1 | "On 7 October 2025 it announced … (LSEG, 2025)." | N/A for R21 | This sentence cites LSEG (2025), which is R20, and is verified under R20. It is listed under R21 by the context-mapping script. No R21 issue. |
| 2 | "On 7 April 2026 it confirmed that Vietnam met all criteria for secondary emerging status and kept the effective date (LSEG, 2026)." | SUPPORTED | "FTSE Russell confirms that Vietnam meets all criteria for Secondary Emerging market status under the FTSE Equity Country Classification Framework." "…confirmed the reclassification … effective from the open on Monday 21 September 2026." |
| 3 | "LSEG (2026) credits the removal of pre-funding requirements for foreign investors for Vietnam's upgrade, and that reform applies to every stock foreign investors can buy." | MINOR_DISTORTION | "FTSE Russell recognized the progress made by the Vietnamese market authorities in evolving market infrastructure, including the removal of the prefunding requirement for Foreign Institutional Investors through the implementation of a non-prefunding model and the establishment of a formal process for handling failed trades." The March assessment itself turned on "progress in enabling access to global brokers". The source names pre-funding removal as one of several reforms, and for foreign institutional investors specifically, not as the sole credited cause. The second clause ("applies to every stock") is the authors' inference and is not attributed to the source. Suggest "credits, among other reforms, the removal of pre-funding for foreign institutional investors". |

---

## Summary table

| Ref | A0 | A1 | A2 issues | Phase B verdicts |
|---|---|---|---|---|
| R12 FTSE Russell 2018 | API_UNAVAILABLE | VERIFIED | none (optional MINOR: subtitle) | 1 SUPPORTED, 1 MINOR_DISTORTION |
| R13 FTSE Russell 2026 FAQ | API_UNAVAILABLE | VERIFIED | MEDIUM: version 1.3 / Aug 2026 not confirmed (indexed: v1.2, April 2026) | 3 SUPPORTED, 1 SUPPORTED-in-part, 1 MINOR_DISTORTION, 4 UNVERIFIABLE_ACCESS (ctx 4, 6, 8, 9) |
| R14 Gregoriou & Nguyen 2010 | API_UNAVAILABLE | VERIFIED | none | **1 MAJOR_DISTORTION** |
| R15 Harris & Gurel 1986 | API_UNAVAILABLE | VERIFIED | none | 1 SUPPORTED, 2 MINOR_DISTORTION |
| R16 Hau et al. 2010 | API_UNAVAILABLE | VERIFIED | none | 1 SUPPORTED |
| R17 Hegde & McDermott 2003 | API_UNAVAILABLE | VERIFIED | none | **1 MAJOR_DISTORTION**, 1 MINOR_DISTORTION, 1 SUPPORTED |
| R18 Ho et al. 2007 | API_UNAVAILABLE | VERIFIED | none | 1 SUPPORTED |
| R19 Kang & Zhang 2014 | API_UNAVAILABLE | VERIFIED | none | 1 SUPPORTED |
| R20 LSEG 2025 | API_UNAVAILABLE | VERIFIED | MEDIUM: title | 1 SUPPORTED |
| R21 LSEG 2026 | API_UNAVAILABLE | VERIFIED | MEDIUM: title | 1 SUPPORTED, 1 MINOR_DISTORTION, 1 N/A (context belongs to R20) |

Totals:
- A1: 10/10 VERIFIED; 0 NOT_FOUND; 0 MISMATCH.
- A2: 3 MEDIUM; 0 SERIOUS.
- Phase B: 25 contexts. 12 SUPPORTED (R13 ctx6 is supported except for its 30 June element and is counted as UNVERIFIABLE_ACCESS), 2 MAJOR_DISTORTION, 7 MINOR_DISTORTION, 4 UNVERIFIABLE_ACCESS (R13 ctx 4, 6, 8, 9; ctx 6 only on the 30 June element), 1 N/A (R21 ctx1 belongs to R20).

**Group verdict: FAIL.** The group has 2 MAJOR_DISTORTION findings and 7 MEDIUM findings (3 from A2 and 4 UNVERIFIABLE_ACCESS contexts).

## Issue list (sorted by severity)

### SERIOUS (must fix)

| ID | Category | Location | Issue | Correct information | Source |
|---|---|---|---|---|---|
| IL-SERIOUS-1 | Citation context (MAJOR_DISTORTION) | Sentence citing Becker-Blease & Paul (2006) and Gregoriou & Nguyen (2010) | Says G&N "find the mirror pattern for FTSE 100 deletions". G&N find no significant effect of liquidity on investment after deletion. | "…whereas Gregoriou and Nguyen (2010) find no significant effect of FTSE 100 deletions on firm investment." | sciencedirect.com/science/article/abs/pii/S1042443110000089; repository.mdx.ac.uk/item/82605 |
| IL-SERIOUS-2 | Citation context (MAJOR_DISTORTION) | Sentence "additions to the S&P 500 raise trading activity and narrow spreads for years (Hegde & McDermott, 2003)" | "For years" exaggerates the source, which reports a "sustained" increase measured over roughly three months after addition. | Replace "for years" with "persistently" or "for at least three months after addition". | sciencedirect.com/science/article/abs/pii/S1386418102000460 |

### MEDIUM (must fix)

| ID | Category | Location | Issue | Correct information | Source |
|---|---|---|---|---|---|
| IL-MEDIUM-1 | Bibliographic (version/date) | Reference R13 | "Version 1.3, August 2026" not confirmable; the indexed versions are v1.0 (Nov 2025) and v1.2 (effective 20 Apr 2026, PDF header "April 2026") | Verify against the downloaded copy. If it is not v1.3, use "(2026, April) … (Version 1.2)". | lseg.com FAQ PDF (search index); research.ftserussell.com notice id=2619334 |
| IL-MEDIUM-2 | Bibliographic (title) | Reference R20 | Title paraphrased | "FTSE Russell announces results of September 2025 semi-annual country classification review for equities and fixed income" | lseg.com press release, 7 Oct 2025 |
| IL-MEDIUM-3 | Bibliographic (title) | Reference R21 | Title adds "the" and omits "for equities and fixed income" | "FTSE Russell announces results of March 2026 semi-annual country classification review for equities and fixed income" | mondovisione.com reprint; lseg.com slug |
| IL-MEDIUM-4 | Citation context (UNVERIFIABLE_ACCESS, elevated risk) | "FTSE's own illustration phases in … 49% investability weight at 4.9% after the first tranche…" | No FAQ text found showing this phasing illustration. The FAQ's indexed 49% example is about liquidity testing. | Quote the FAQ passage and page, or present it as the authors' own calculation from the 10% tranching factor. | lseg.com FAQ PDF snippet |
| IL-MEDIUM-5 | Citation context (UNVERIFIABLE_ACCESS) | "selected the final constituents on data as of 30 June 2026 (FTSE Russell, 2026)" | Date not seen in retrieved FAQ text. It is consistent with the GEIS September-review liquidity period (ends on the last business day of June). | Confirm in the FAQ or cite the GEIS ground rules. | GEIS rule snippet |
| IL-MEDIUM-6 | Citation context (UNVERIFIABLE_ACCESS) | "…selected on data as of 30 June 2026 and effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026)" | The 30 June element is not confirmed. The 21 Aug publication, 27 constituents and 18 Sep close are confirmed. | As IL-MEDIUM-5 | as above |
| IL-MEDIUM-7 | Citation context (UNVERIFIABLE_ACCESS) | Table "Stocks by FTSE list" | Ticker-level membership only partly confirmed (VCB, VIC, VHM, BID, VPB, HPG; 28- and 32-stock eligible lists exist) | Confirm against the FTSE 21 Aug 2026 constituent notice | theinvestor.vn; vir.com.vn |

### MINOR (recommended fix)

| ID | Category | Location | Issue | Suggestion |
|---|---|---|---|---|
| IL-MINOR-1 | Context | "sat on the FTSE watch list for seven years (FTSE Russell, 2018)" | The 2018 document gives only the start of the period | Cite "(FTSE Russell, 2018; LSEG, 2025)" |
| IL-MINOR-2 | Context | "investability weight (free float)" | Investability weight is the more restrictive of free float and the foreign-ownership limit | "(free float, capped by the foreign-ownership limit)" |
| IL-MINOR-3 | Context | "passive funds … buy on the effective date … (Harris & Gurel, 1986)" | H&G measure the effect after announcement; their sample does not separate the effective date | "around the index change" |
| IL-MINOR-4 | Context | "funds tracking FTSE benchmarks … closing price of 18 September … (Harris & Gurel, 1986)" | Vietnam-specific facts are attributed to H&G | Cite FTSE Russell (2026)/VIR (2026) for the facts and H&G for the mechanism |
| IL-MINOR-5 | Context | "…which they attribute to more information and more trading interest" (Hegde & McDermott) | Loose paraphrase | "mainly to lower direct trading costs and, secondarily, to lower information asymmetry" |
| IL-MINOR-6 | Context | "LSEG (2026) credits the removal of pre-funding requirements for foreign investors for Vietnam's upgrade" | The source lists pre-funding removal (for foreign institutional investors) among several reforms, plus the global-broker-access assessment | "credits, among other reforms, the removal of pre-funding for foreign institutional investors" |
| IL-MINOR-7 | Bibliographic (formatting, optional) | Reference R12 | Document title is "FTSE Classification of Markets"; ": September 2018" is a descriptive subtitle | Optional: "FTSE classification of markets [September 2018 annual country classification review]" |

## Tool limitation note

- **Phase B rests on search snippets.** WebFetch was blocked for every publisher and news host tried, so the verdicts rely on abstract text and search-engine snippets of the cited sources.
- **What a reachable copy of the FTSE FAQ would settle.** The FAQ's full text was never retrieved. If the author has a downloaded copy, reading it resolves IL-MEDIUM-1 and IL-MEDIUM-4 to IL-MEDIUM-7 directly.
- **The two MAJOR_DISTORTION findings rest on consistent evidence.** Several independent snippets agree on each, including the publisher abstract (Hegde & McDermott) and multiple citing-literature summaries (Gregoriou & Nguyen).
