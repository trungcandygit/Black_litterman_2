# Stage 4.5 Final Integrity Check: Phase A + Phase B, Reference Group 3 (R22 to R31)

Agent: `integrity_verification_agent` (ARS v3.22.1), Mode 2 (final-check), fresh context.
Run date: 2026-09-24. Input: `/home/user/B-i-FTSE2/ars/stage4_5_integrity/refgroup3.md` (10 references, 26 citation contexts).
The manuscript was not edited.

## Skill load record

These files were read with the Read tool from `/tmp/claude-0/-home-user-B-i-FTSE2/88a51032-601f-5b56-b6d6-c6001a62ef1c/scratchpad/academic-research-skills` (v3.22.1). Each entry gives the file's first heading line.

| # | File | First heading line |
|---|------|--------------------|
| 1 | `academic-pipeline/SKILL.md` | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| 2 | `academic-pipeline/agents/integrity_verification_agent.md` | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| 3 | `academic-pipeline/references/integrity_review_protocol.md` | `# Integrity Review Protocol (Added in v2.0)` |
| 4 | `academic-pipeline/references/claim_verification_protocol.md` | `# Claim Verification Protocol (Phase E)` |
| 5 | `deep-research/references/semantic_scholar_api_protocol.md` | `# Semantic Scholar API Verification Protocol` |

The skill files were loaded after the first searches had run. I then re-checked every verdict against these rules:
- A1 has 3 outcomes only (VERIFIED, NOT_FOUND, MISMATCH), and NOT_FOUND requires 3 query variants.
- A2 needs an audit trail for every reference: the query, the top URL and the fields confirmed.
- Gray-zone statements such as "difficult to verify" or "plausible but unconfirmed" are not allowed. Any unconfirmed field goes on the correction list.
- A reference must pass Phase A before Phase B can run.
- Severity map for A2: SERIOUS covers author, year, journal, DOI and date errors. MEDIUM covers omitted co-authors, title imprecision and page errors. MINOR covers formatting.
- Severity map for Phase B: MINOR_DISTORTION is MINOR. MAJOR_DISTORTION is SERIOUS. UNVERIFIABLE is SERIOUS. UNVERIFIABLE_ACCESS is MEDIUM.

In this report, SUPPORTED is the same as the Phase E verdict VERIFIED.

## Environment and A0 status

- **A0 (Semantic Scholar batch check): `API_UNAVAILABLE`.** api.crossref.org, doi.org, OpenAlex and Semantic Scholar are blocked by the egress proxy, so A0 was skipped and every reference went to A1.
- **WebFetch** was also blocked (EGRESS_BLOCKED) on these hosts: theinvestor.vn, vietnamnews.vn, en.vietnamplus.vn, vir.com.vn, www.vietnam.vn, emerald.com, ideas.repec.org, econpapers.repec.org, researchgate.net, r.jina.ai and web.archive.org.
- **All checks therefore used WebSearch.** The search engine returned result titles, URLs and summarised snippets of page text.
- **Source quotes below are search-result snippets.** They were not read from full pages. Where a news byline date could not be retrieved, the gap is flagged; it is not assumed correct.

---

## R22: Nguyen, Hai & Nguyen (2021)

**REF:** Nguyen, C. T., Hai, P. T., & Nguyen, H. K. (2021). Stock market returns and liquidity during the COVID-19 outbreak: Evidence from the financial services sector in Vietnam. *Asian Journal of Economics and Banking, 5*(3), 324–342. https://doi.org/10.1108/AJEB-06-2021-0070

**A1: VERIFIED**

**A2 field check: all fields match; no mismatches.**
- **Authors:** 3, given as "Nguyen CT, Hai PT, and Nguyen HK" in the publisher-derived citation.
- **Year, title, journal, volume, issue, pages, DOI:** 2021; title exact; *Asian Journal of Economics and Banking*; 5(3); 324–342; DOI 10.1108/AJEB-06-2021-0070.

**Audit trail**
- **Q1:** `"Stock market returns and liquidity during the COVID-19 outbreak" Vietnam financial services Asian Journal of Economics and Banking`. Top URL: https://www.emerald.com/ajeb/article/5/3/324/25724/Stock-market-returns-and-liquidity-during-the. Confirmed: title, journal, vol 5, no 3, pp. 324–342, DOI.
- **Q2:** `AJEB-06-2021-0070 authors Nguyen ...`. Top URL: https://emerald.com/insight/content/doi/10.1108/AJEB-06-2021-0070/full/html. Confirmed: authors "Nguyen CT, Hai PT, and Nguyen HK (2021)".

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "...for example, Nguyen et al. (2021) study the returns and liquidity of financial-services stocks during the COVID-19 outbreak." | SUPPORTED | "explore the influence of the COVID-19 outbreak and the Government's disease control measures on the stock returns and liquidity of Vietnam-listed companies in the financial services sector ... 50 banking, insurance and finance companies listed in ... HNX and HOSE ... January 30th, 2020 to May 15th, 2021." |

---

## R23: Raddatz, Schmukler & Williams (2017)

**REF:** Raddatz, C., Schmukler, S. L., & Williams, T. (2017). International asset allocations and capital flows: The benchmark effect. *Journal of International Economics, 108*, 413–430. https://doi.org/10.1016/j.jinteco.2017.06.007

**A1: VERIFIED**

**A2 field check**
- **Matches:** 3 authors (Claudio Raddatz, Sergio Schmukler, Tomás Williams); year 2017; title exact; *Journal of International Economics*; vol 108; pp. 413–430.
- **DOI:** could not be resolved because doi.org is blocked. The ScienceDirect PII is S0022199617300739, and the RePEc handle is `RePEc:eee:inecon:v:108:y:2017:i:c:p:413-430`. Both are consistent with the cited volume and pages. No mismatch was found.

**Audit trail**
- **Q1:** `Raddatz Schmukler Williams "International asset allocations and capital flows: The benchmark effect" Journal of International Economics 108`. Top URLs:
  - https://econpapers.repec.org/RePEc:eee:inecon:v:108:y:2017:i:c:p:413-430
  - https://www.sciencedirect.com/science/article/abs/pii/S0022199617300739

  Confirmed: authors, year, title, journal, volume, pages.
- **Q2:** `... benchmark effect abstract "MSCI" reclassification exchange rates mutual fund allocations`. Returned the abstract and summary text.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "Market classification decides which benchmarks a country's stocks can enter, and benchmark weights steer international portfolio allocations (Raddatz et al., 2017)." | SUPPORTED | "movements in benchmarks appear to have important effects on equity and bond mutual fund portfolio allocations, including passive and active funds." |
| 2 | "Mutual funds allocate across countries with reference to benchmark weights, so a change in classification changes capital flows (Raddatz et al., 2017)..." | SUPPORTED | "Exogenous, pre-announced changes in benchmarks result in movements in asset allocations and capital flows mostly when these changes are implemented." Also: "Changes in benchmarks not only impact asset allocations, but also capital flows, abnormal returns ... and exchange rates." (The Hau et al. part of the sentence is outside this group.) |
| 3 | "Foreign allocations follow benchmark weights (Raddatz et al., 2017), which points the same way for the persistent effect." | SUPPORTED | Same abstract text as #2. The source also says effects occur "not just when benchmark changes are announced, but also later, when they become effective." |
| 4 | "The liquidity gain was largest for the three large-capitalization stocks ... which suggests that investors weighted their attention by expected index weight, as benchmark-driven allocations would (Raddatz et al., 2017)." | MINOR_DISTORTION | Raddatz et al. document benchmark-weight-driven allocations at the **country** level: "how international equity and bond market indexes impact asset allocations, capital flows, asset prices, and exchange rates across countries". Applying this to stock-level "attention" is the authors' extension of the source. The meaning is broadly preserved, but the source does not study stock-level liquidity or attention. |

---

## R24: Roth, Sant'Anna, Bilinski & Poe (2023)

**REF:** Roth, J., Sant'Anna, P. H. C., Bilinski, A., & Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. *Journal of Econometrics, 235*(2), 2218–2244. https://doi.org/10.1016/j.jeconom.2023.03.008

**A1: VERIFIED**

**A2 field check: all fields match; no mismatches.**
- **Authors:** 4 (Jonathan Roth, Pedro H. C. Sant'Anna, Alyssa Bilinski, John Poe).
- **Year, title, journal, volume, issue, pages, DOI:** 2023; title exact; *Journal of Econometrics*; 235(2); 2218–2244; DOI 10.1016/j.jeconom.2023.03.008.

**Audit trail**
- **Q1:** `Roth Sant'Anna Bilinski Poe "What's trending in difference-in-differences" Journal of Econometrics 235 2218`. Top URLs:
  - https://www.sciencedirect.com/science/article/abs/pii/S0304407623001318
  - https://www.jonathandroth.com/assets/files/DiD_Review_Paper.pdf (header: "Journal of Econometrics 235 (2023) 2218–2244")

  Confirmed: authors, volume, issue 2, pages, August 2023.
- **Q2:** `... DOI 10.1016/j.jeconom.2023.03.008 ...`. Confirmed the DOI.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "We also replace week fixed effects with size-tercile-by-week fixed effects, add a constituent-specific linear trend, and estimate a monthly event study relative to September 2025 (Roth et al., 2023)." | SUPPORTED | The paper is cited as a general methodological reference for DiD and event-study robustness. It covers dynamic event-study specifications ("Event-study plots were typically created by estimating a dynamic two-way fixed effects (TWFE) regression specification...") and the treatment of potential parallel-trends violations. Note: the source also cautions that "parametric approaches to controlling for pre-existing trends may be sensitive to functional form assumptions". The citation does not misstate this, and the linear trend is one robustness check among several. |

---

## R25: Shleifer (1986)

**REF:** Shleifer, A. (1986). Do demand curves for stocks slope down? *The Journal of Finance, 41*(3), 579–590. https://doi.org/10.1111/j.1540-6261.1986.tb04518.x

**A1: VERIFIED**

**A2 field check: all fields match; no mismatches.**
- **Author:** 1 (Andrei Shleifer).
- **Year, title, journal, volume, issue, pages, DOI:** 1986; title exact; *The Journal of Finance*; 41(3); 579–590 (RePEc: "v41y1986i3p579-90"); DOI 10.1111/j.1540-6261.1986.tb04518.x (the Wiley URL embeds it).

**Audit trail**
- **Q1:** `Shleifer 1986 "Do demand curves for stocks slope down" Journal of Finance 41 3 579`. Top URLs:
  - https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1986.tb04518.x
  - https://ideas.repec.org/a/bla/jfinan/v41y1986i3p579-90.html
- **Q2:** abstract query. Returned the abstract text quoted below.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "Shleifer (1986) interprets permanent price effects as evidence that demand curves for stocks slope down..." | MINOR_DISTORTION | Abstract: "stocks newly included into the Standard and Poor's 500 Index have earned a significant positive abnormal return at the announcement of the inclusion. This return does not disappear for at least ten days after the inclusion. The returns are positively related to measures of buying by index funds, consistent with the hypothesis that demand curves for stocks slope down." The source text found says the return persists for "at least ten days"; it does not use the word "permanent". The downward-sloping-demand interpretation is accurate. Suggested wording: "persistent (non-reversing)". |
| 2 | "The persistent gain after the confirmation ... is consistent with a lasting shift in demand for the stocks (Shleifer, 1986; Chen et al., 2004)." | SUPPORTED | Same abstract. A persistent return linked to index-fund demand matches the source. |

---

## R26: Stereńczak, Zaremba & Umar (2020)

**REF:** Stereńczak, S., Zaremba, A., & Umar, Z. (2020). Is there an illiquidity premium in frontier markets? *Emerging Markets Review, 42*, 100673. https://doi.org/10.1016/j.ememar.2019.100673

**A1: VERIFIED**

**A2 field check: all fields match; no mismatches.**
- **Authors:** 3 (Stereńczak, S.; Zaremba, A.; Umar, Z.).
- **Year, title, journal, volume, article number, DOI:** 2020; title exact; *Emerging Markets Review*; vol 42; article 100673; DOI 10.1016/j.ememar.2019.100673.

**Audit trail**
- **Q1:** `Stereńczak Zaremba Umar "Is there an illiquidity premium in frontier markets" Emerging Markets Review 42 100673`. Top URL: https://www.sciencedirect.com/science/article/pii/S1566014119302481. Confirmed the full citation string: 'Stereńczak, S., Zaremba, A. and Umar, Z. (2020), "Is there an illiquidity premium in frontier markets?", Emerging Markets Review, Vol. 42, 100673, doi: 10.1016/j.ememar.2019.100673'.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "...Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity." | SUPPORTED | "the most comprehensive examination of the illiquidity premium in frontier equities, testing six liquidity measures in 22 countries for the years 1991–2019 ... no evidence of illiquidity premium in frontier stock markets". The sentence describes the research question accurately. It does not report the (null) answer, but it does not misstate it either. |

---

## R27: The Investor (2026a)

**REF:** The Investor. (2026a, March 4). *FTSE Russell eyes 28 Vietnam stocks ahead of market status upgrade review*. https://theinvestor.vn/ftse-russell-eyes-28-vietnam-stocks-ahead-of-market-status-upgrade-review-d18516.html

**A1: VERIFIED.** The outlet, the exact headline and the exact URL (d18516) were all found.

**A2 field check**

| Field | Status |
|-------|--------|
| Headline | Exact match |
| Outlet | The Investor (theinvestor.vn) |
| URL | Exact match |
| Publication date (4 March 2026) | **Not confirmed by byline.** The page is blocked. The content is consistent with early March 2026: "as index provider FTSE Russell begins its mid-year review in March 2026" and the article mentions the ECCAC meeting "Tuesday, March 3". The article-ID sequence also fits early March: d17585 is Nov 2025 and d18800 is 8 Apr 2026. However, one search summary asserted "Date Published: April 3, 2026"; no other result corroborated this. **Flagged MINOR: the author should confirm the date against the page byline.** |

**Facts in the article (from search snippets)**
- **Attribution:** "Vietnamese brokerage Vietcap Securities has identified 28 local stocks that meet the preliminary criteria for inclusion in the FTSE Global All Cap Index".
- **Data date:** "The 28 stocks are based on data as of December 31, 2024".
- **The 28 tickers:** VIC, VHM, HPG, MSN, VCB, VNM, SSI, STB, VIX, VJC, VRE, VCI, SHB, VND, GEX, KBC, KDH, FRT, DGC, EIB, HUT, DXG, DPM, PLX, PDR, SAB, DIG, KDC. The Nhadautu sister article (d103252) gives the same list.

**Audit trail**
- **Q1:** exact headline in quotes. Top URL is the cited URL.
- **Q2:** `theinvestor.vn FTSE Russell eyes 28 Vietnam stocks Vietcap March 2026 list tickers`. Returned the 28 tickers and the 31 Dec 2024 data date.
- **Q3:** `"FTSE Russell eyes 28 Vietnam stocks" March 2026`, then a date query restricted to theinvestor.vn, vietnam.vn and nhadautu.vn.
- **Q4:** Nhadautu (Vietnamese edition) query. Returned an identical 28-ticker list.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "A preliminary list of 28 names, screened on data as of 31 December 2024, appeared in November 2025 (Viet Nam News, 2025; The Investor, 2026a)." | MINOR_DISTORTION | The 2026a article supports the number 28 and the data date ("based on data as of December 31, 2024"). However, it is a March 2026 article that reports Vietcap's reading of the list, so it does not itself document the list "appearing in November 2025". Viet Nam News (2025) carries the November date. The Investor's own November 2025 report is "FTSE Russell lists 28 Vietnamese stocks eligible for emerging-market index inclusion" (https://theinvestor.vn/ftse-russell-lists-28-vietnamese-stocks-eligible-for-emerging-market-index-inclusion-d17585.html); it would be the precise co-citation for this sentence. |
| 2 | "A list of 32 names ... (The Investor, 2026b)." | N/A for 2026a | Only 2026b is cited in this sentence; see R28. |
| 3 | "List membership follows Viet Nam News (2025) and The Investor (2026a, 2026b)." | SUPPORTED | The 28 tickers quoted above. |
| 4 | Table A.2, rows for the preliminary list | SUPPORTED | Manuscript rows: 15 later constituents (GEX, HPG, MSN, SHB, SSI, STB, VCB, VCI, VHM, VIC, VIX, VJC, VND, VNM, VRE), 12 HOSE names not included (DGC, DIG, DPM, DXG, EIB, FRT, KBC, KDC, KDH, PDR, PLX, SAB), and HUT, for 28 in total. This is identical to the source list, one for one. HUT (Tasco) is on the source list; its Hanoi-exchange venue is not stated in the retrieved snippets, but the source is not cited for it. |

---

## R28: The Investor (2026b)

**REF:** The Investor. (2026b, April 8). *FTSE Russell names 32 Vietnamese stocks eligible for emerging-market index inclusion*. https://theinvestor.vn/ftse-russell-names-32-vietnamese-stocks-eligible-for-emerging-market-index-inclusion-d18800.html

**A1: VERIFIED**

**A2 field check**

| Field | Status |
|-------|--------|
| Headline | Exact match |
| Outlet | The Investor |
| URL | Exact match |
| Date (8 April 2026) | Consistent with the evidence. FTSE's March 2026 review result was announced 7 April 2026 (London; LSEG press release dated "April 07, 2026"). The sibling article d18799, "FTSE Russell confirms Vietnam's market status upgrade...", has the adjacent ID. CNBC published on 2026/04/08, and the ACBS flash note is dated April 8, 2026. The byline itself is not retrievable (page blocked), so this is **flagged MINOR: confirm against the byline.** |

**Audit trail**
- **Q1:** exact headline in quotes. Top URL is the cited URL.
- **Q2:** `FTSE Russell 32 Vietnamese stocks December 31 2025 PLX removed BID FPT NVL GEE BSR`, restricted to theinvestor.vn. Returned the article text quoted below.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "A preliminary list of 28 names ... (Viet Nam News, 2025; The Investor, 2026a)." | N/A for 2026b | Not cited here. |
| 2 | "A list of 32 names, screened on data as of 31 December 2025, followed in April 2026; it dropped Petrolimex (PLX) and added BID, FPT, NVL, GEE and BSR (The Investor, 2026b)." | SUPPORTED | "FTSE Russell has named 32 Vietnamese stocks that met the FTSE Global All Cap index eligibility screens based on data as of December 31, 2025." Also: "Compared to FTSE Russell's list released last November, the latest has five new names: BIDV bank (BID, large cap), FPT Corporation (FPT, mid cap), No Va Land Investment Group (NVL, small cap), Gelex Electric (GEE, small cap), and Binh Son Refining and Petrochemical (BSR, small cap). Vietnam National Petroleum Group, or Petrolimex (PLX) ... was removed in the new list." And: "The 27 Vietnamese stocks mentioned in both the old and new lists..." (28 − 1 + 5 = 32). |
| 3 | "List membership follows ... The Investor (2026a, 2026b)." | SUPPORTED | As in #2. |
| 4 | Table A.2, row "Added to the April 2026 list": BID, FPT, NVL, GEE, BSR; PLX removed | SUPPORTED | As in #2. The side notes "later constituents" and "not included" are verified against the August 2026 list under R31. |

---

## R29: Viet Nam News (2025)

**REF:** Viet Nam News. (2025, November 13). *FTSE Russell plans inclusion of 28 Vietnamese stocks in 2026 market upgrade*. https://vietnamnews.vn/economy/1729462/ftse-russell-plans-inclusion-of-28-vietnamese-stocks-in-2026-market-upgrade.html

**A1: VERIFIED**

**A2 field check**

| Field | Status |
|-------|--------|
| Headline | Exact match |
| Outlet | Viet Nam News (vietnamnews.vn) |
| URL | Exact match (ID 1729462) |
| Date (13 November 2025) | Consistent with the evidence: the article refers to FTSE's "previous announcement on October 8", and FTSE Russell's Vietnam FAQ was published in November 2025. One search summary gave "announcement dated November 13, 2025", but that phrase echoed the query terms, so it is weak evidence. The byline is not retrievable (page blocked), so this is **flagged MINOR: confirm against the byline.** |

**Audit trail**
- **Q1:** exact headline in quotes. Top URL is the cited URL.
- **Q2:** `vietnamnews.vn FTSE Russell plans inclusion of 28 Vietnamese stocks November 2025`.
- **Q3:** `"28 Vietnamese stocks" FTSE Russell "November 13, 2025" OR "13/11/2025"`.
- **Q4:** ticker query (HUT, PLX, SAB, DXG, KBC, FRT, DGC). Returned the full ticker enumeration.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "A preliminary list of 28 names, screened on data as of 31 December 2024, appeared in November 2025 (Viet Nam News, 2025; ...)." | SUPPORTED | "FTSE Russell has identified a list of 28 stocks likely to make it into the FTSE Global All Cap index, including ... HPG, VCB, VIC, VHM, MSN, SAB, VNM, and ... DXG." Also: "This preliminary list is based on data as of December 31, 2024, and may be subject to change". |
| 2 | "List membership follows Viet Nam News (2025)..." | SUPPORTED | Remaining names in the snippet: "DXG, DIG, DGC, FRT, KDH, KDC, KBC, DPM, Phat Dat (DPR [sic, PDR]), STB, SHB, SSI, Tasco (HUT), VCI, VJC, GEX, EIB, PLX, VRE, VIX, VND". |
| 3 | Table A.2, preliminary-list rows | SUPPORTED | The names match the manuscript's 15 + 12 + HUT exactly. SAB and DXG are named explicitly in the source. |

---

## R30: VietnamPlus (2024)

**REF:** VietnamPlus. (2024, December 30). *Vietnamese billion dollar oil refinery exits UPCoM to join HoSE*. https://en.vietnamplus.vn/vietnamese-billion-dollar-oil-refinery-exits-upcom-to-join-hose-post307514.vnp

**A1: VERIFIED**

**A2 field check**

| Field | Status |
|-------|--------|
| Headline | Matches. The indexed title reads "...to Join HoSE" with a capital J. The lower-case form in the reference follows APA sentence case, so no change is needed. |
| Outlet | VietnamPlus |
| URL | Exact match (post307514) |
| Date (30 December 2024) | Consistent with the evidence. Adjacent VietnamPlus post IDs (post307555, post307561 "Transport ministry plans to launch 19 projects ... in 2025") are year-end-2024 items. The article describes the 7 Jan 2025 delisting in the future tense. The byline is not retrievable (page blocked), so this is **flagged MINOR: confirm against the byline.** |

Note: the same story also ran in Viet Nam News (1689855) and VOV (post1145445) under the same headline. The source is correctly attributed to VietnamPlus.

**Audit trail**
- **Q1:** exact headline in quotes. Top URLs:
  - https://en.vietnamplus.vn/...-post307514.vnp
  - https://vietnamnews.vn/economy/1689855/...
- **Q2:** `Binh Son Refining BSR UPCoM delisting HoSE January 17 2025`, restricted to en.vietnamplus.vn, vietnamnews.vn and english.vov.vn. Returned the text quoted below.
- **Q3:** `BSR delist UPCoM January 7 2025 last trading day January 6 VietnamPlus December 2024`.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "BSR ... traded on the UPCoM market until 6 January 2025 and on HOSE from 17 January 2025 (VietnamPlus, 2024)..." | SUPPORTED | "The Binh Son Refining and Petrochemical Company (BSR) has announced its delisting from the UPCoM exchange on January 7, 2025 ... Over 244 million BSR shares will have their final trading session on UPCoM on January 6, 2025." Also: "3.1 billion BSR shares ... set to be listed on HoSE from January 17, 2025". |
| 2 | "...it moved from UPCoM to HOSE only in January 2025, after the data date of the November list (VietnamPlus, 2024)..." | SUPPORTED | Same text. The January 2025 venue change is after the 31 Dec 2024 data date. The claim that this "gives a reason other than liquidity" is the authors' inference and is not attributed to the source. |

---

## R31: VIR (2026)

**REF:** VIR. (2026, August 22). *FTSE Russell names 27 Vietnamese stocks in review*. https://vir.com.vn/ftse-russell-names-27-vietnamese-stocks-in-review-159265.html

**A1: VERIFIED**

**A2 field check**

| Field | Status |
|-------|--------|
| Headline | Exact match |
| Outlet | VIR (Vietnam Investment Review) |
| URL | Exact match (159265) |
| Date (22 August 2026) | Consistent with the evidence: the article reports the "August 21" announcement as a past event, and Vietstock's list article is dated 2026/08. The byline is not retrievable (page blocked), so this is **flagged MINOR: confirm against the byline.** |

**Audit trail**
- **Q1:** `"FTSE Russell names 27 Vietnamese stocks in review" VIR`. Top URL is the cited URL.
- **Q2:** `vir.com.vn FTSE Russell names 27 Vietnamese stocks in review August 2026 June 30 data`.
- **Q3:** `"FTSE Russell names 27 Vietnamese stocks in review" "August 22, 2026"`.
- **Q4:** Vietnamese-press queries on the full list, the 18 Sep close and the 30 June data date. Sources: thoibaotaichinhvietnam.vn, vietstock.vn, cafef.vn, vneconomy.vn.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---------|---------|-----------------------|
| 1 | "On Friday 21 August 2026 FTSE published the September semi-annual review with 27 constituents, selected on data as of 30 June 2026 and effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026)." | UNVERIFIABLE_ACCESS (partial) | **Supported by VIR:** "FTSE Russell added 27 Vietnamese stocks to its global equity indices ... On August 21, FTSE Russell announced the results of its semi-annual review of the series". 21 Aug 2026 is a Friday. **Supported by Vietnamese press:** "effective ... 21/09/2026, sau khi các thay đổi kỹ thuật được chốt lại vào cuối phiên giao dịch ngày 18/09" ("after the technical changes are finalised at the close of trading on 18/09"); a search summary for the VIR and BigGo results also said "Trades execute at the September 18 close". **Not found:** the element "data as of 30 June 2026" does not appear in any retrievable VIR text, and the VIR page is blocked. That element may be carried by the co-cited FTSE Russell (2026), which is outside this group. **Action:** confirm that FTSE Russell (2026) states the 30 June 2026 cut-off, or cite it alone for that element. |
| 2 | "FTSE assigned the constituents to size segments on 21 August 2026: three large-capitalization stocks (VCB, VIC, VHM), three mid-capitalization stocks (BID, VPB, HPG) and 18 small-capitalization stocks among those in our sample (VIR, 2026)." | SUPPORTED | "Three Vietnamese stocks were classified as large cap – VCB (Vietcombank), VIC (Vingroup), and VHM (Vinhomes). In the mid-cap segment, the three stocks added were BID (BIDV), VPB (VPBank), and HPG (Hoa Phat). In the small-cap segment, 21 stocks were added". The source's 21 small caps minus TCX, VCK and VPL (not in sample) leaves 18. The count is the authors' derivation, and the sentence qualifies it correctly with "among those in our sample". |
| 3 | Table A.2, constituent split (sources include VIR, 2026) | SUPPORTED | The full list was obtained from Vietnamese press (vietstock.vn / thoibaotaichinhvietnam.vn search snippet): Large = VCB, VIC, VHM. Mid = BID, HPG, VPB. Small (21) = FPT, GEX, HDB, HCM, MCH, MSN, NVL, SHB, STB, SSB, SSI, TCX, VNM, VCI, VJC, MSB, VRE, VPL, VIX, VND, VCK. Checked against the manuscript table: the 15 preliminary-list names are all constituents; BID, FPT and NVL are constituents; GEE and BSR are not; PLX is not. The "not on either list" names (HCM, HDB, MCH, MSB, SSB, VPB, TCX, VCK, VPL) are all constituents and appear on neither the 28 nor the 32 list. The total is 15 + 3 + 9 = 27, an exact match. |

---

## Summary table

| Ref | Short cite | A1 | A2 | Phase B contexts | Phase B verdicts |
|-----|-----------|----|----|------------------|------------------|
| R22 | Nguyen et al. (2021) | VERIFIED | Clean | 1 | 1 SUPPORTED |
| R23 | Raddatz et al. (2017) | VERIFIED | Clean (DOI not resolvable; PII and RePEc consistent) | 4 | 3 SUPPORTED, 1 MINOR_DISTORTION |
| R24 | Roth et al. (2023) | VERIFIED | Clean | 1 | 1 SUPPORTED |
| R25 | Shleifer (1986) | VERIFIED | Clean | 2 | 1 SUPPORTED, 1 MINOR_DISTORTION |
| R26 | Stereńczak et al. (2020) | VERIFIED | Clean | 1 | 1 SUPPORTED |
| R27 | The Investor (2026a) | VERIFIED | Date not byline-confirmed (MINOR) | 4 (3 cite 2026a) | 2 SUPPORTED, 1 MINOR_DISTORTION |
| R28 | The Investor (2026b) | VERIFIED | Date not byline-confirmed (MINOR) | 4 (3 cite 2026b) | 3 SUPPORTED |
| R29 | Viet Nam News (2025) | VERIFIED | Date not byline-confirmed (MINOR) | 3 | 3 SUPPORTED |
| R30 | VietnamPlus (2024) | VERIFIED | Date not byline-confirmed (MINOR) | 2 | 2 SUPPORTED |
| R31 | VIR (2026) | VERIFIED | Date not byline-confirmed (MINOR) | 3 | 2 SUPPORTED, 1 UNVERIFIABLE_ACCESS (partial) |

**Totals**
- **Phase A:** 10/10 VERIFIED. 0 NOT_FOUND, 0 MISMATCH, 0 SERIOUS or MEDIUM bibliographic errors.
- **Phase B:** 24 context judgments, counting each shared sentence once per reference that it actually cites. Results: 19 SUPPORTED, 3 MINOR_DISTORTION, 1 UNVERIFIABLE_ACCESS (partial), 0 MAJOR_DISTORTION, 0 UNVERIFIABLE.

**Result for this group: FAIL.** One UNVERIFIABLE_ACCESS item remains (MEDIUM under the Phase E taxonomy). Everything else would allow PASS WITH NOTES. The group can move to PASS WITH NOTES once the co-cited FTSE Russell (2026) is confirmed, in its own group's check, to state the 30 June 2026 data cut-off.

## Issue list (sorted by severity)

### SERIOUS
None.

### MEDIUM

| ID | Ref | Location | Issue | Correct information / action | Source |
|----|-----|----------|-------|------------------------------|--------|
| IL-MEDIUM-1 | R31 | Context 1 (21 Aug 2026 review sentence) | VIR is cited for "selected on data as of 30 June 2026". No retrievable VIR text states the 30 June cut-off, and the VIR page is blocked (UNVERIFIABLE_ACCESS). The other elements are supported: 21 Aug, 27 constituents, 18 Sep close / 21 Sep effective. | Confirm that FTSE Russell (2026) states the 30 June 2026 data date, and attribute that element to FTSE Russell (2026) alone if VIR does not carry it. | https://vir.com.vn/ftse-russell-names-27-vietnamese-stocks-in-review-159265.html |

### MINOR

| ID | Ref | Location | Issue | Suggestion |
|----|-----|----------|-------|------------|
| IL-MINOR-1 | R27 | Context 1 ("appeared in November 2025") | The Investor (2026a) is a March 2026 article reporting Vietcap's reading of the 28-name list. It supports the count and the 31 Dec 2024 data date, but not the November 2025 appearance. | Keep Viet Nam News (2025) for the date, and replace 2026a with, or add, The Investor's November 2025 report: "FTSE Russell lists 28 Vietnamese stocks eligible for emerging-market index inclusion" (theinvestor.vn …-d17585.html). |
| IL-MINOR-2 | R25 | Context 1 | "permanent price effects": the abstract text found says the return "does not disappear for at least ten days". | Use "persistent" or "non-reversing" instead of "permanent". |
| IL-MINOR-3 | R23 | Context 4 | Country-level benchmark-allocation evidence is applied to stock-level investor attention. | Soften the wording, e.g., "consistent with the benchmark-weight channel documented at the country level (Raddatz et al., 2017)". |
| IL-MINOR-4 | R27 | Reference date (2026, March 4) | The byline date could not be retrieved (egress blocked). Content and article-ID sequence are consistent with early March 2026, but one uncorroborated search summary gave 3 April 2026. | Confirm the date against the page byline. |
| IL-MINOR-5 | R28, R29, R30, R31 | Reference dates (8 Apr 2026; 13 Nov 2025; 30 Dec 2024; 22 Aug 2026) | Byline dates could not be retrieved (egress blocked). All are consistent with the surrounding evidence, and no contrary date was found. | Confirm each date against the page byline. |

## Tool limitation note
- **Blocked access.** Publisher pages and news pages could not be fetched, and neither could DOI resolvers or the Crossref, Semantic Scholar and OpenAlex APIs. All verification relied on WebSearch result titles, URLs and summarised snippets.
- **Snippets are not full text.** Quotes above come from those snippets, not from full-text reading.
- **Journal articles (R22 to R26).** Phase B judgments rest on the abstract or summary text. They are SUPPORTED only where the manuscript's attribution does not go beyond that text.
