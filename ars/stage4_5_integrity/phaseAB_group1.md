# Stage 4.5 Final Integrity Check: Phase A + Phase B, Reference Group 1 (R1 to R11)

Agent: `integrity_verification_agent` (ARS academic-research-skills v3.22.1), Mode 2 (final-check), fresh context
Input: `ars/stage4_5_integrity/refgroup1.md`
Executed: 2026-09-24
Scope: Phase A (A0, A1, A2) and Phase B (B1, 100% of registered contexts) for R1 to R11 only. A3 ghost-citation check, Phases C, D and E, and the failure-mode checklist are outside this group task.

## Skill load record

Files read in full with the Read tool before the verdicts below were finalised. Each is listed with its first heading line.

| # | File (ARS root = scratchpad/academic-research-skills, v3.22.1, commit 6234edf) | First heading line |
|---|---|---|
| 1 | academic-pipeline/SKILL.md | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| 2 | academic-pipeline/agents/integrity_verification_agent.md | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| 3 | academic-pipeline/references/integrity_review_protocol.md | `# Integrity Review Protocol (Added in v2.0)` |
| 4 | academic-pipeline/references/claim_verification_protocol.md | `# Claim Verification Protocol (Phase E)` |
| 5 | deep-research/references/semantic_scholar_api_protocol.md | `# Semantic Scholar API Verification Protocol` |

After loading, every verdict was re-checked against these rules:
- A1 has 3 values only (VERIFIED, NOT_FOUND, MISMATCH), and NOT_FOUND needs 3 query variants.
- A2 enforcement: each reference has an audit trail with the query, the top URL and the fields confirmed.
- The gray-zone prohibition applies: nothing is left "plausible but unconfirmed" without being flagged.
- Phase B is run only after a Phase A verdict exists.
- The severity map is SERIOUS / MEDIUM / MINOR, and the claim-verdict severities are MINOR_DISTORTION = MINOR, MAJOR_DISTORTION = SERIOUS, UNVERIFIABLE_ACCESS = MEDIUM.

## Environment and A0 status

- **A0 (Semantic Scholar batch check): `API_UNAVAILABLE` / `[S2-API-UNAVAILABLE]`.** The egress proxy refused CONNECT with 403 to api.semanticscholar.org, api.crossref.org, api.openalex.org and doi.org. This was confirmed live on 2026-09-24 through the `__agentproxy/status` recentRelayFailures list and a curl test. A1 therefore ran on every reference.
- **WebFetch** to publisher and repository pages was also blocked by egress policy. This covered www.sciencedirect.com, onlinelibrary.wiley.com, ideas.repec.org, leeds-faculty.colorado.edu and www.cis.upenn.edu. No full text could be retrieved. All evidence comes from WebSearch result pages: titles, URLs and the snippets and abstracts that the search tool returned. Quotes in Phase B are those snippets. Where a snippet paraphrases a source, the quote is labelled "search snippet".
- No verdict relies on model memory.

---

## R1. Amihud (2002)

**REF:** Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56. https://doi.org/10.1016/S1386-4181(01)00024-6

- **A1: VERIFIED**
- **A2:** All fields match. Author: 1, Y. Amihud. Year 2002. Title exact. Journal *Journal of Financial Markets*. Vol 5, issue 1, pp. 31–56. The DOI resolves to this article. No mismatches.
- **Audit trail:**
  - Q1: `Amihud 2002 "Illiquidity and stock returns: cross-section and time-series effects" Journal of Financial Markets 5 31-56`. Top URL: https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf (header "Journal of Financial Markets 5 (2002) 31–56 Illiquidity and stock returns:"). Also SSRN 1295244.
  - Q2: `Amihud 2002 Journal of Financial Markets volume 5 issue 1 doi ...`. URL: https://ideas.repec.org/a/eee/finmar/v5y2002i1p31-56.html (handle encodes v5, 2002, i1, pp. 31–56).
  - Q3: `"10.1016/S1386-4181(01)00024-6" Amihud`. URL: https://www.sciencedirect.com/science/article/abs/pii/S1386418101000246. Result: "DOI 10.1016/S1386-4181(01)00024-6 … Journal of Financial Markets, volume 5, number 1, pages 31–56 (2002)."
  - Fields confirmed: author, year, title, journal, volume, issue, pages, DOI.

**Phase B**

| # | Context (abridged) | Verdict | Source text relied on |
|---|---|---|---|
| B1-1 | "the Amihud (2002) illiquidity of the 27 stocks … fell … by 43% … and by 56% …" | **SUPPORTED** (the citation attributes only the measure; 27 / 43% / 56% are the manuscript's own estimates and belong to Phase C/E, not to Amihud) | Search snippet: "The paper's illiquidity measure (ILLIQ) is calculated as the average over the year of the daily ratio of the stock's absolute return to its dollar trading volume." |
| B1-2 | "The Amihud (2002) ratio for stock i on day t is ILLIQ_it = \|R_it\| / VAL_it, where R_it is the log return and VAL_it the traded value." | **MINOR_DISTORTION** (MINOR) | Search snippet (DOI query): "the daily ratio of absolute stock return to dollar volume". Snippet (Q2): "ILLIQ is the average for year y of the daily ratio of absolute return to the dollar volume of stock." Amihud defines R as the daily stock return, not the log return, and aggregates daily ratios to an annual average. Using the log return and traded value in VND is the manuscript's own adaptation. The meaning is preserved, but the adaptation is presented as Amihud's definition. Suggested fix: "Following Amihud (2002), we measure daily illiquidity as … where R_it is the (log) return …". |

---

## R2. Becker-Blease & Paul (2006)

**REF:** Becker-Blease, J. R., & Paul, D. L. (2006). Stock liquidity and investment opportunities: Evidence from index additions. *Financial Management, 35*(3), 35–51. https://doi.org/10.1111/j.1755-053X.2006.tb00146.x

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 2, John R. Becker-Blease and Donna L. Paul, so the initials J. R. and D. L. are correct. Year 2006. Title exact. *Financial Management*, 35(3), 35–51. The DOI matches the Wiley URL. No mismatches.
- **Audit trail:**
  - Q1: `Becker-Blease Paul 2006 "Stock liquidity and investment opportunities: Evidence from index additions" Financial Management`. Top URLs: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=405842 and https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1755-053X.2006.tb00146.x. Result: "Financial Management, volume 35, issue 3, 2006 … DOI: 10.1111/j.1755-053X.2006.tb00146.x".
  - Q2: `Becker-Blease Paul "Financial Management" 35 3 2006 pages 35-51 …`. Result: "published in Financial Management, volume 35, pages 35-51."
  - Fields confirmed: authors, year, title, journal, volume, issue, pages, DOI.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B2-1 | "added firms with larger liquidity gains invest more (Becker-Blease & Paul, 2006)" | **SUPPORTED** | Abstract snippet: "examine the relation between stock liquidity and investment opportunities in a sample of firms experiencing an exogenous liquidity shock, finding a positive relation between changes in capital expenditures and changes in stock liquidity"; snippet: "in the context of additions to the S&P 500 stock index, over the time period of 1980–2000." |
| B2-2 | "firms added to the S&P 500 with larger liquidity improvements increase capital investment" (the Gregoriou & Nguyen part belongs to another group) | **SUPPORTED** | Same as above. |

---

## R3. Bekaert, Harvey & Lundblad (2007)

**REF:** Bekaert, G., Harvey, C. R., & Lundblad, C. (2007). Liquidity and expected returns: Lessons from emerging markets. *Review of Financial Studies, 20*(6), 1783–1831. https://doi.org/10.1093/rfs/hhm030

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 3, Geert Bekaert, Campbell R. Harvey and Christian T. Lundblad. The reference gives "Lundblad, C.". SSRN shows "Christian T.", so the middle initial is omitted. This is acceptable in APA and is **not an issue**. Year 2007. Title exact. *RFS* 20(6), 1783–1831. DOI 10.1093/rfs/hhm030 confirmed.
- **Audit trail:**
  - Q1: `Bekaert Harvey Lundblad 2007 "Liquidity and expected returns: Lessons from emerging markets" Review of Financial Studies 20 6`. Top URL: https://academic.oup.com/rfs/article-abstract/20/6/1783/1575135. Result: "Review of Financial Studies, Vol. 20(6), pages 1783-1831, in November 2007."
  - Q2: `"10.1093/rfs/hhm030" Bekaert Harvey Lundblad`. Result: "DOI 10.1093/rfs/hhm030 … The Review of Financial Studies, Volume 20, Issue 6, pages 1783–1831 (2007)."
  - Q3 (abstract): `… "local market liquidity" "partially segmented" …`. URL: https://www.nber.org/papers/w11413.
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B3-1 | "liquidity is priced in emerging markets (Bekaert et al., 2007)" | **SUPPORTED** | Snippet: "Unexpected liquidity shocks are positively correlated with contemporaneous return shocks … consistent with liquidity being a priced factor." |
| B3-2 | "local market liquidity predicts returns in emerging markets, where segmentation from global capital is only partial" | **SUPPORTED** | Snippet: "Local market liquidity is an important driver of expected returns in emerging markets, and the liberalization process has not fully eliminated its impact"; "their liquidity measure significantly predicts future returns"; "the model differentiates between integrated and segmented countries and time periods." |

---

## R4. Biktimirov & Afego (2026)

**REF:** Biktimirov, E. N., & Afego, P. N. (2026). Is there an index effect in frontier markets? *International Review of Economics & Finance, 110*, 105562. https://doi.org/10.1016/j.iref.2026.105562

- **A1: VERIFIED** (the work exists). Confirmed: title "Is there an index effect in frontier markets?", authors "Biktimirov, Ernest N. & Afego, Pyemo N." (2 authors, initials match), journal *International Review of Economics & Finance*, year 2026, and ScienceDirect PII S1059056026006751. ISSN 1059-0560 is IREF's ISSN, which is consistent.
- **A2:**
  - Author, year, title and journal are confirmed.
  - **Volume 110, article number 105562 and DOI 10.1016/j.iref.2026.105562 could not be confirmed by a fresh check.**
  - Five query variants were run. The exact-DOI query `"10.1016/j.iref.2026.105562"` returned no page that carries this DOI; the search tool reported "unable to find a specific article with the DOI". No source contradicted the values either.
  - Publisher, Crossref and doi.org access was blocked (A0 = API_UNAVAILABLE, and WebFetch to ScienceDirect was blocked).
  - Under the gray-zone rule this cannot be left as "plausible". It is logged as **IL-SERIOUS-1 (DOI / volume / article number unconfirmed; severity class = DOI field)**. It stays open until someone checks it against the ScienceDirect record for PII S1059056026006751.
  - *Supplementary comparison only (the protocol's "compare with Stage 2.5" step, not relied on for the fresh verdict):* `ars/stage2_5_integrity/crossref_recheck.tsv` holds a Crossref record captured at Stage 2.5 for 10.1016/j.iref.2026.105562 with status OK, Biktimirov, 2026, vol 110, article 105562 and this title. The cited values agree with that record. The item is therefore expected to close on a single publisher-page check, and no change to the reference is proposed.
- **Audit trail:**
  - Q1: `Biktimirov Afego "Is there an index effect in frontier markets" International Review of Economics & Finance`. Top URL: https://ideas.repec.org/s/eee/reveco.html (IREF series listing). Confirmed title, authors, journal and study period.
  - Q2: `"Is there an index effect in frontier markets" Biktimirov Afego sciencedirect 105562`. Surfaced PII S1059056026006751. The article number was not confirmed.
  - Q3: `"10.1016/j.iref.2026.105562"`. No match.
  - Q4: `… volume 110 …`. Result: "published in … September 2026"; the volume was not shown.
  - Q5: `"S1059056026006751"`. URL: https://sciencedirect.com/science/article/pii/S1059056026006751 exists, but its metadata was not shown.
  - Q6: `Biktimirov Afego frontier markets index effect doi 10.1016/j.iref.2026`. Confirmed authors, title and journal only.

**Phase B** (allowed because A1 = VERIFIED)

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B4-1 | "In frontier markets, index additions raise prices persistently, and the evidence points to institutional demand rather than trading pressure or liquidity changes as the cause" | **SUPPORTED** | Abstract snippet: "Both new and repeated additions experience persistent stock price increases, while deletions generally face persistent declines … The results are consistent with institutional investor demand as the underlying mechanism, rather than temporary trading pressure or liquidity effects, lending support to the downward-sloping demand curve hypothesis." |
| B4-2 | "study changes to the FTSE Frontier 50 Index from 2008 to 2025" | **SUPPORTED** (the dates match exactly) | Snippet: "examines short-term stock market reactions to changes in the FTSE Frontier 50 Index from 2008 to 2025 across 30 frontier markets in Africa, Asia, Europe, and South America." |
| B4-3 | "frontier-market evidence that index effects reflect investor demand rather than liquidity alone" | **SUPPORTED** (the paraphrase is weaker than the source, which excludes liquidity effects, so it does not overstate) | Same abstract snippet as B4-1. |

---

## R5. Brown & Warner (1985)

**REF:** Brown, S. J., & Warner, J. B. (1985). Using daily stock returns: The case of event studies. *Journal of Financial Economics, 14*(1), 3–31. https://doi.org/10.1016/0304-405X(85)90042-X

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 2, S. J. Brown and J. B. Warner. Year 1985. Title exact; some indexes render it as "Using daily stock returns. The case of event studies", which is only punctuation. *JFE* 14(1), 3–31. The ScienceDirect PII 0304405X8590042X corresponds to DOI 10.1016/0304-405X(85)90042-X. No mismatches.
- **Audit trail:**
  - Q1: `Brown Warner 1985 "Using daily stock returns: The case of event studies" Journal of Financial Economics 14 3-31`. Top URLs: https://www.sciencedirect.com/science/article/abs/pii/0304405X8590042X, https://ideas.repec.org/a/eee/jfinec/v14y1985i1p3-31.html and https://leeds-faculty.colorado.edu/bhagat/brownwarner1985.pdf ("Journal of Financial Economics 14 (1985) 3-31"). Result: "Vol. 14(1), pages 3-31 in January 1985."
  - Q2: `… "crude dependence adjustment" …`. URL: https://www.eventstudytools.com/significance-tests.
  - Q3: `… cumulative excess returns multi-day interval … "square root" …`. The full-text PDF was listed but the fetch was blocked.
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B5-1 | "test cumulative abnormal returns at the portfolio level, which accounts for the common event dates (Brown & Warner, 1985)" | **SUPPORTED** | Abstract snippet: "tests ignoring cross-sectional dependence can be well-specified and have higher power than tests which account for potential dependence." Secondary snippet: "The 'crude dependence adjustment' (CDA) test by Brown and Warner, 1985 … A time-series standard error estimates the spread of the portfolio's daily abnormal return over the estimation window … collapsing cross-firm dependence into one number." B&W treat the portfolio (CDA) test as the dependence-adjusted test, so the attribution is accurate. |
| B5-2 | "dividing the portfolio CAR by the standard deviation of daily portfolio abnormal returns in an estimation window, scaled by the square root of the window length (Brown & Warner, 1985)" | **UNVERIFIABLE_ACCESS** (MEDIUM) | The first half is corroborated by the CDA snippet above: "time-series standard error … of the portfolio's daily abnormal return over the estimation window … used by the crude dependence adjusted t-test". The sqrt(window-length) scaling of a multi-day CAR is not in any retrieved snippet or abstract, and the full text (Colorado PDF, ScienceDirect) was egress-blocked. The abstract is consistent. Recommend checking the B&W (1985) appendix, or citing a source that states the multi-day scaling explicitly. |
| B5-3 | "Portfolio t = CAR divided by the standard deviation … times the square root of the window length (Brown & Warner, 1985)" | **UNVERIFIABLE_ACCESS** (MEDIUM) | Same basis as B5-2. Note: as written, "divided by the standard deviation … times the square root of the window length" should be read as CAR / (σ·√L). Algebraically the sentence could also be read as (CAR/σ)·√L. This is a manuscript clarity point (MINOR) and does not concern the source. |

---

## R6. Callaway & Sant'Anna (2021)

**REF:** Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. https://doi.org/10.1016/j.jeconom.2020.12.001

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 2, Brantly Callaway and Pedro H. C. Sant'Anna. Year 2021. Title exact; the publisher capitalises it as "Difference-in-Differences with multiple time periods", which is sentence case and fine. *J. Econometrics* 225(2), 200–230. DOI 10.1016/j.jeconom.2020.12.001 confirmed.
- **Audit trail:**
  - Q1: `Callaway Sant'Anna 2021 "Difference-in-differences with multiple time periods" Journal of Econometrics 225 2 200-230`. Top URLs: https://ideas.repec.org/a/eee/econom/v225y2021i2p200-230.html and https://www.sciencedirect.com/science/article/abs/pii/S0304407620303948. Result: "volume 225(2), pages 200-230 … The DOI for the journal publication is 10.1016/j.jeconom.2020.12.001."
  - Q2: `Callaway Sant'Anna 2021 two-way fixed effects "negative weights" staggered …`. URL: https://psantanna.com/csdid/articles/why-not-twfe.html.
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B6-1 | "the specification has no staggered adoption, and the TWFE estimator does not suffer the negative-weighting problem that motivates Callaway and Sant'Anna (2021)" | **SUPPORTED** | Abstract snippet: "identification, estimation, and inference procedures for treatment effect parameters using DiD with (i) multiple time periods, (ii) variation in treatment timing …". Snippet from the authors' csdid documentation (psantanna.com): "When treatment timing is staggered and effects differ across cohorts or over time, the coefficient in a TWFE regression is a weighted average of many 2×2 comparisons, and some of those weights are negative … TWFE uses already-treated units as comparison units." Note: the formal negative-weights decomposition is usually credited to Goodman-Bacon (2021) and de Chaisemartin & D'Haultfœuille (2020). Saying the problem "motivates" C&S is accurate as written. |

---

## R7. Cameron, Gelbach & Miller (2008)

**REF:** Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics, 90*(3), 414–427. https://doi.org/10.1162/rest.90.3.414

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 3, A. Colin Cameron, Jonah B. Gelbach and Douglas L. Miller. Year 2008. Title exact. *REStat* 90(3), 414–427. DOI 10.1162/rest.90.3.414 confirmed. One secondary snippet (a Stata features page) prints "90: 417–427". The publisher (MIT Press), RePEc and EconPapers all give 414–427, so the reference is correct.
- **Audit trail:**
  - Q1: `Cameron Gelbach Miller 2008 "Bootstrap-based improvements for inference with clustered errors" Review of Economics and Statistics 90 3 414-427`. Top URLs: https://direct.mit.edu/rest/article/90/3/414/57731/ and https://ideas.repec.org/a/tpr/restat/v90y2008i3p414-427.html. Result: "vol. 90(3), pages 414-427, August."
  - Q2: `"10.1162/rest.90.3.414" Cameron Gelbach Miller`. URL: https://www.mitpressjournals.org/doi/pdf/10.1162/rest.90.3.414.
  - Q3: `… wild cluster bootstrap-t Rademacher weights impose null restricted residuals`.
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B7-1 | "For inference with 24 treated stocks, we report a wild cluster bootstrap (Cameron et al., 2008) and randomization inference …" | **SUPPORTED** (the citation attributes only the method) | Abstract snippet: "Standard asymptotic tests can over-reject … with few (five to thirty) clusters. The authors investigate more accurate inference using cluster bootstrap-t procedures that provide asymptotic refinement." Note for the authors: CGM study few *clusters*, whereas the manuscript's concern is few *treated* clusters. The attribution of the method is still correct. |
| B7-2 | "Wild cluster bootstrap: restricted residuals, Rademacher weights (Cameron et al., 2008)" | **SUPPORTED** (secondary corroboration; primary full text not fetched) | Snippet: "The WCR (wild cluster restricted) variant imposes the null hypothesis when generating bootstrap residuals … the variant recommended by Cameron, Gelbach & Miller. Rademacher weights take values +/-1 with equal probability." |

---

## R8. Chen, Noronha & Singal (2004)

**REF:** Chen, H., Noronha, G., & Singal, V. (2004). The price response to S&P 500 index additions and deletions: Evidence of asymmetry and a new explanation. *The Journal of Finance, 59*(4), 1901–1930. https://doi.org/10.1111/j.1540-6261.2004.00683.x

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 3, Honghui Chen, Gregory Noronha and Vijay Singal; the author order on the Wiley record is Chen, Noronha, Singal, which matches. Year 2004. Title exact. *JF* 59(4). DOI 10.1111/j.1540-6261.2004.00683.x matches the Wiley URL. Pages 1901–1930 were confirmed by the search result ("The correct page range is 1901-1930"). One aggregated citation string gives 1901–1929. This is a secondary variant and does not count as a mismatch.
- **Audit trail:**
  - Q1: `Chen Noronha Singal 2004 "The price response to S&P 500 index additions and deletions: Evidence of asymmetry and a new explanation" Journal of Finance 59 4`. Top URL: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2004.00683.x.
  - Q2: `Chen Noronha Singal "Journal of Finance" 2004 59 1901-1930 OR 1901-1929 …`. Result: "volume 59, pages 1901-1930."
  - Q3: `ideas.repec.org jfinan v59y2004i4p1901 …`. Not indexed on IDEAS.
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B8-1 | "Chen et al. (2004) find asymmetric effects of additions and deletions that fit a gain in investor awareness" | **SUPPORTED** | Abstract snippet: "there is a permanent increase in the price of added firms but no permanent decline for deleted firms … changes in investor awareness contribute to the asymmetric price effects of S&P 500 index additions and deletions." |
| B8-2 | "The persistent gain after the confirmation … is consistent with a lasting shift in demand for the stocks (Shleifer, 1986; Chen et al., 2004)" | **SUPPORTED** | The same snippet: a permanent price increase for additions, explained by awareness-driven demand. |

---

## R9. Chordia, Roll & Subrahmanyam (2000)

**REF:** Chordia, T., Roll, R., & Subrahmanyam, A. (2000). Commonality in liquidity. *Journal of Financial Economics, 56*(1), 3–28. https://doi.org/10.1016/S0304-405X(99)00057-4

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 3; the published order is Chordia, Roll, Subrahmanyam, as in the reference. SSRN lists them in a different order, which is an SSRN display artefact. Year 2000. Title exact. *JFE* 56, 3–28. DOI 10.1016/S0304-405X(99)00057-4 confirmed. Issue 1 is consistent with pp. 3–28 at the start of volume 56. No mismatches.
- **Audit trail:**
  - Q1: `Chordia Roll Subrahmanyam 2000 "Commonality in liquidity" Journal of Financial Economics 56 1 3-28`. Top URLs: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=155187 and https://www.oalib.com/references/15313632. The latter shows "Journal of Financial Economics, 56, 3-28. http://dx.doi.org/10.1016/S0304-405X(99)00057-4".
  - Fields confirmed: authors, year, title, journal, volume, pages, DOI.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B9-1 | "Liquidity co-moves across stocks (Chordia et al., 2000)" | **SUPPORTED** | Snippet: "examines whether quoted spreads, quoted depth, and effective spreads co-move with market- and industry-wide liquidity … the liquidity of individual assets often moves in tandem with market liquidity." (The context string in refgroup1.md carries trailing heading text, "### 2.3 …". That is an extraction artefact and not a manuscript issue.) |

---

## R10. Corwin & Schultz (2012)

**REF:** Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 2, Shane A. Corwin and Paul H. Schultz. The reference gives "Schultz, P." without the middle initial H. APA-acceptable and not an issue. Year 2012. Title exact. *JF* 67(2), 719–760. DOI confirmed.
- **Audit trail:**
  - Q1: `Corwin Schultz 2012 "A simple way to estimate bid-ask spreads from daily high and low prices" Journal of Finance 67 2 719-760`. Top URLs: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2012.01729.x and https://ideas.repec.org/a/bla/jfinan/v67y2012i2p719-760.html.
  - Q2: `Corwin Schultz 2012 negative two-day spread estimates set to zero …`. URLs: https://sites.nd.edu/scorwin/files/2019/11/Dealing-with-Negative-Values.pdf and https://ba-odegaard.no/… (lecture notes).
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B10-1 | "we also report … the Corwin and Schultz (2012) high-low spread" | **SUPPORTED** | Snippet: "The authors develop a bid-ask spread estimator from daily high and low prices." |
| B10-2 | "CS is the Corwin and Schultz (2012) spread." | **SUPPORTED** | Same. |
| B10-3 | "We compute the Corwin and Schultz (2012) spread from two-day high and low prices and set negative estimates to zero." | **SUPPORTED** | Snippet: "when high-low price ratios are estimated over two days, the variance is twice as large but the bid-ask spread component is unchanged"; snippet: "The two-day corrected version involves setting negative two-day estimates … to zero … similar to what Corwin and Schultz (2012) applied." |
| B10-4 | "The Corwin and Schultz (2012) spread did not narrow: it rose by 0.09 to 0.13 percentage points …" | **SUPPORTED** (the citation names only the measure; the figures are the manuscript's own results and belong to Phase C/E) | Same as B10-1. |

---

## R11. Dong, Zheng, Jia & Zhang (2023)

**REF:** Dong, S., Zheng, J., Jia, H., & Zhang, Z. (2023). Impact of capital market internationalization on stock markets: Evidence from the inclusion of China A-shares in the MSCI Emerging Markets Index. *Research in International Business and Finance, 66*, 101989. https://doi.org/10.1016/j.ribaf.2023.101989

- **A1: VERIFIED**
- **A2:** All fields match. Authors: 4, Shizheng Dong, Jianming Zheng, Haoyang Jia and Zili Zhang, so the initials S., J., H. and Z. are correct. Year 2023. Title exact. *RIBAF* vol. 66 (October 2023). DOI 10.1016/j.ribaf.2023.101989 confirmed, which gives article number 101989. The IDEAS handle `v66y2023ics0275531923001150` confirms vol. 66.
- **Audit trail:**
  - Q1: `Dong Zheng Jia Zhang 2023 "Impact of capital market internationalization on stock markets" MSCI China A-shares Research in International Business and Finance 101989`. Top URLs: https://www.sciencedirect.com/science/article/abs/pii/S0275531923001150 and https://ideas.repec.org/a/eee/riibaf/v66y2023ics0275531923001150.html.
  - Q2: `… "Research in International Business and Finance" 66 "101989"`. Confirmed that Vol 66 is October 2023.
  - Q3: `"inclusion of China A-shares in the MSCI Emerging Markets Index" Dong 2023 "101989" OR "ribaf.2023.101989"`. Result: "Volume 66, with DOI: 10.1016/j.ribaf.2023.101989."
  - Fields confirmed: all fields.

**Phase B**

| # | Context | Verdict | Source text relied on |
|---|---|---|---|
| B11-1 | "the included stocks earned abnormal returns around the announcement, and market quality changed over the longer run through liquidity, turnover and price synchronization" | **SUPPORTED** | Abstract snippet: "In the short term, the underlying stocks gained cumulative excess returns before and after the announcement date … presenting a significant index effect. In the long run, including A-shares in the index may improve market quality by influencing stock market synchronization and liquidity and turnover rate." (The source hedges with "may improve". The manuscript says "changed", which is neutral and not an overstatement.) |
| B11-2 | "Beyond Dong et al. (2023), we did not locate a verified stock-level study of liquidity around the MSCI inclusion of China A-shares …" | **SUPPORTED** as an attribution (Dong et al. do study liquidity around the inclusion) | Same snippet. *Advisory (E5-type absence claim, not scored here):* the search in this run surfaced related RIBAF, Finance Research Letters and Economics Letters work on the MSCI A-share inclusion, including "Benchmark effects from the inclusion of Chinese A-shares in the MSCI EM index" (Economics Letters, PII S016517652200180X). Its liquidity content was not examined. The sentence is already search-bounded ("we did not locate"), so it is acceptable, but the Phase E / E5 owner should check it. |

---

## Summary table

| Ref | A0 | A1 | A2 | Phase B contexts | Phase B verdicts |
|---|---|---|---|---|---|
| R1 Amihud 2002 | API_UNAVAILABLE | VERIFIED | OK | 2 | 1 SUPPORTED, 1 MINOR_DISTORTION |
| R2 Becker-Blease & Paul 2006 | API_UNAVAILABLE | VERIFIED | OK | 2 | 2 SUPPORTED |
| R3 Bekaert et al. 2007 | API_UNAVAILABLE | VERIFIED | OK | 2 | 2 SUPPORTED |
| R4 Biktimirov & Afego 2026 | API_UNAVAILABLE | VERIFIED | **Vol/art. no./DOI unconfirmed (IL-SERIOUS-1, open)** | 3 | 3 SUPPORTED |
| R5 Brown & Warner 1985 | API_UNAVAILABLE | VERIFIED | OK | 3 | 1 SUPPORTED, 2 UNVERIFIABLE_ACCESS |
| R6 Callaway & Sant'Anna 2021 | API_UNAVAILABLE | VERIFIED | OK | 1 | 1 SUPPORTED |
| R7 Cameron et al. 2008 | API_UNAVAILABLE | VERIFIED | OK | 2 | 2 SUPPORTED |
| R8 Chen et al. 2004 | API_UNAVAILABLE | VERIFIED | OK | 2 | 2 SUPPORTED |
| R9 Chordia et al. 2000 | API_UNAVAILABLE | VERIFIED | OK | 1 | 1 SUPPORTED |
| R10 Corwin & Schultz 2012 | API_UNAVAILABLE | VERIFIED | OK | 4 | 4 SUPPORTED |
| R11 Dong et al. 2023 | API_UNAVAILABLE | VERIFIED | OK | 2 | 2 SUPPORTED |
| **Total** | | **11/11 VERIFIED; 0 NOT_FOUND; 0 MISMATCH** | **10 clean, 1 open** | **24** | **21 SUPPORTED, 1 MINOR_DISTORTION, 2 UNVERIFIABLE_ACCESS, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE** (sum = 24) |

## Issue list (sorted by severity)

### SERIOUS
| ID | # | Category | Location | Issue | Correct information / action | Source |
|---|---|---|---|---|---|---|
| IL-SERIOUS-1 | 1 | Reference (A2: DOI / volume / article number) | R4, Biktimirov & Afego (2026) | Existence, authors, title, journal and year are VERIFIED. Volume 110, article 105562 and DOI 10.1016/j.iref.2026.105562 could **not be confirmed in a fresh check**: the exact-DOI web query found no match, and Crossref, doi.org and ScienceDirect were blocked. No contradicting value was found. It is logged as SERIOUS only because the DOI field falls in that class and the gray-zone rule forbids leaving it unconfirmed. | Check the ScienceDirect record for PII S1059056026006751 and confirm vol., article no. and DOI. The Stage 2.5 Crossref capture (`ars/stage2_5_integrity/crossref_recheck.tsv`) agrees with the cited values, so no edit is expected. Close this item once it is confirmed. | https://sciencedirect.com/science/article/pii/S1059056026006751 ; https://ideas.repec.org/s/eee/reveco.html |

### MEDIUM
| ID | # | Category | Location | Issue | Correct information / action | Source |
|---|---|---|---|---|---|---|
| IL-MEDIUM-1 | 1 | Citation context (UNVERIFIABLE_ACCESS) | R5 context B5-2 (Methods: CAR test) | Scaling the portfolio CAR test by sqrt(window length) is attributed to Brown & Warner (1985). The CDA portfolio-SD part is corroborated, but the multi-day scaling was not found in any accessible text (full text blocked). | Check the B&W (1985) appendix. If the scaling is not stated there, reword as "following the crude dependence adjustment of Brown & Warner (1985), extended to multi-day windows by scaling with √L" and/or add a source that states it. | https://www.eventstudytools.com/significance-tests ; https://www.sciencedirect.com/science/article/abs/pii/0304405X8590042X |
| IL-MEDIUM-2 | 2 | Citation context (UNVERIFIABLE_ACCESS) | R5 context B5-3 (formula note) | Same basis as IL-MEDIUM-1. | Same action. | Same |

(UNVERIFIABLE_ACCESS carries MEDIUM severity in the claim-verdict taxonomy. Under the agent's Verdict Criteria table it is listed with the notes that do not block PASS WITH NOTES. The orchestrator should apply the rule it uses for the Stage 4.5 zero-issue gate.)

### MINOR
| ID | # | Category | Location | Issue | Suggestion |
|---|---|---|---|---|---|
| IL-MINOR-1 | 1 | Citation context (MINOR_DISTORTION) | R1 context B1-2 (Methods: Amihud definition) | "The Amihud (2002) ratio … where R_it is the log return and VAL_it the traded value" presents the manuscript's adaptation (log return, VND traded value, daily ratio) as Amihud's definition. Amihud uses the absolute daily return over dollar volume, averaged over the year. | "Following Amihud (2002), daily illiquidity is ILLIQ_it = \|R_it\|/VAL_it, where we use the log return R_it and traded value VAL_it in VND." |
| IL-MINOR-2 | 2 | Manuscript clarity (not a source issue) | R5 context B5-3 | "CAR divided by the standard deviation … times the square root of the window length" could be read either way. | Write t = CAR / (σ̂_AR · √L). |

### Advisory (not issues)
- R7 B7-1: CGM (2008) address few clusters; the manuscript's setting is few *treated* clusters. The attribution is correct. The authors may wish to add a reference on few-treated-cluster inference.
- R11 B11-2: this is a search-bounded absence claim. Related MSCI A-share inclusion papers exist (e.g., Economics Letters PII S016517652200180X), and their liquidity content was not checked here. Route to Phase E / E5.

## Group verdict (Phase A + B, R1 to R11)

**FAIL (provisional), resting only on IL-SERIOUS-1, which is an unconfirmed field and not a detected error.** When the publisher check confirms R4's vol. 110 / 105562 / DOI, this group becomes **PASS WITH NOTES**. The notes would be 1 MINOR_DISTORTION, 2 UNVERIFIABLE_ACCESS and 1 clarity MINOR. No fabricated reference, no mismatch and no MAJOR_DISTORTION was found.

## Tool limitation disclaimer

Crossref, doi.org, OpenAlex and Semantic Scholar were blocked. Publisher and repository pages were also blocked for WebFetch. Verification therefore used WebSearch result metadata and abstract snippets only; no full texts were read. Phase B verdicts on methods details (B5-2, B5-3, B7-2 and B10-3) rest on abstracts or secondary descriptions, as marked.
