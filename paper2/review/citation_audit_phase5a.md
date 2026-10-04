## Citation Audit Report

Manuscript: `paper2/review/round1/manuscript_C_v1.md` (HOSE price limits; APA 7.0 author-date)
Agent: citation_compliance_agent (Phase 5a). The manuscript was NOT modified; corrections are given as exact strings below.
Evidence boundary: this audit is text-only. No DOI was resolved and no online lookup was performed. DOI resolution and source existence are "unchecked" (left to the integrity agent).

### Summary
| Metric | Count |
|--------|-------|
| Total in-text citations (instances) | 26 (17 distinct sources) |
| Total reference list entries | 17 |
| Orphan in-text citations (no ref) | 0 |
| Orphan references (no in-text) | 0 |
| Format errors (deterministic; correction supplied below) | 6 |
| Format errors (flagged for review) | 2 (see Flagged items F1, F2) |
| Missing DOIs (journal articles) | 7 of 14 journal articles |
| Self-citation ratio | 0% (the manuscript's own authors are not cited; the GitHub repository is third-party) |
| Sources from last 5 years (2021-2026) | 5.9% (1/17: tungtran0911, 2026) |
| Sources older than 10 years | 14/17 (82%); mostly seminal methods or price-limit literature, see F5 |

### Checklist results (PASS/FAIL per item)
| # | Item | Result | Notes |
|---|------|--------|-------|
| 1 | Every in-text citation has a reference entry | PASS | 0 orphans |
| 2 | Every reference entry is cited in text | PASS | 0 orphans |
| 3 | Author names and years match between text and list | PASS | All 17 pairs match (matrix below) |
| 4 | "et al." usage (APA 7: 3+ authors, from first citation) | FAIL | "Veeraraghavan, Nguyen and Truong (2007)" in Section 1 (3 authors) should be "Veeraraghavan et al. (2007)". All other 3+ author citations are correct (Cho et al., Berkman et al., Bali et al., Harvey et al., Cameron et al., Lou et al.) |
| 5 | Ampersand / "and" usage | PASS | "&" in parentheticals (Kim & Rhee, 1997; Benjamini & Hochberg, 1995; Imbens & Lemieux, 2008); "and" in narrative (Kim and Rhee; Berkman and Lee; Corwin and Schultz; Fama and MacBeth; Newey and West). All reference entries use ", &" correctly |
| 6 | Multiple-work parenthetical in alphabetical order | FAIL | "(Harvey et al., 2016; Benjamini & Hochberg, 1995)" should be "(Benjamini & Hochberg, 1995; Harvey et al., 2016)" |
| 7 | Narrative year after first mention | FAIL (minor) | Section 4.1: "the Harvey et al. threshold of 3" has no year. APA allows omitting the year only within the same paragraph as the first narrative citation; Section 3.1 is a different paragraph. Use "the Harvey et al. (2016) threshold of 3" |
| 8 | Reference list alphabetical order | FAIL | "Bali, Cakici, & Whitelaw (2011)" is placed after "Berkman ..." and "Benjamini ...". Bali precedes Benjamini (Ba < Be). Other order checks pass (Berkman, Koch (2012) before Berkman, Lee (2002) is correct by second author; Cameron < Chen < Cho; Newey < tungtran0911 < Veeraraghavan) |
| 9 | DOI format (https://doi.org/..., no dx.doi.org, no "DOI:" prefix, no trailing period) | PASS | All 10 DOIs present are in the https://doi.org/ form with no trailing period |
| 10 | DOI presence | FAIL (flag only, non-blocking) | 7 journal articles have no DOI: Bali et al. (2011), Berkman et al. (2012), Berkman & Lee (2002), Chen (1993), Cho et al. (2003), Imbens & Lemieux (2008), Newey & West (1987). The manuscript's DOI coverage is inconsistent (10 of 17 entries have one). Resolution of existing DOIs is unchecked |
| 11 | Article titles in sentence case; journal titles in Title Case and italic; volume italic; issue in parentheses; en-dash page ranges | PASS | Harvey et al. leading ellipsis title is acceptable. Journal name "The Journal of Finance" keeps "The" consistently in both JF entries |
| 12 | Journal/volume/year plausibility | PASS | Volumes and years are internally consistent: JFE 99 (2011), 16 (1986), 134 (2019); JF 67 (2012), 52 (1997); JFQA 47 (2012); PBFJ 1 (1993), 10 (2002); JEF 10 (2003); JBES 29 (2011); JPE 81 (1973); RFS 29 (2016); Econometrica 55 (1987); J. Econometrics 142 (2008); JRSS-B 57 (1995). No out-of-range volumes or page ranges seen |
| 13 | Grey literature: GitHub repository (tungtran0911, 2026) | FAIL | Non-APA elements: "(accessed 4 October 2026)" after the URL; descriptor "[Source code and analysis, GitHub repository; not peer reviewed]"; no publisher/platform element. See correction C4 |
| 14 | Grey literature: SSRN working paper (Veeraraghavan et al., 2007) | FAIL | APA 7 puts the series number in parentheses after the italic title and names "Social Science Research Network" as the publisher; "[Working paper]. SSRN." is not the prescribed form. See correction C5. Bibliographic data also flagged for verification (F1) |
| 15 | Self-citation ratio <= 15% | PASS | 0% |
| 16 | Over-citation (>5 in one sentence) | PASS | Maximum is 4 citations in one sentence (Section 1, sentence on Kim & Rhee, Chen, Berkman & Lee, Cho et al.) |
| 17 | Retraction / Expression-of-Concern screen | NOT PERFORMED | No database lookup was made. All 14 journal articles are well-known publications of the kind expected in this literature; no retraction is known to this auditor, but this is not a verification |

### Cross-reference matrix
| Author, Year | In-text (n) | In RefList | Status |
|---|---|---|---|
| Bali et al., 2011 | 1 | Yes | OK |
| Benjamini & Hochberg, 1995 | 2 (1 narrative-method mention w/o cite) | Yes | OK |
| Berkman et al., 2012 | 3 | Yes | OK |
| Berkman & Lee, 2002 | 2 | Yes | OK |
| Brennan, 1986 | 1 | Yes | OK |
| Cameron et al., 2011 | 1 | Yes | OK |
| Chen, 1993 | 1 | Yes | OK |
| Cho et al., 2003 | 1 | Yes | OK |
| Corwin & Schultz, 2012 | 1 | Yes | OK |
| Fama & MacBeth, 1973 | 1 | Yes | OK |
| Harvey et al., 2016 | 3 (incl. year-less mention in 4.1) | Yes | OK (see item 7) |
| Imbens & Lemieux, 2008 | 1 | Yes | OK |
| Kim & Rhee, 1997 | 3 | Yes | OK |
| Lou et al., 2019 | 1 | Yes | OK |
| Newey & West, 1987 | 1 | Yes | OK |
| tungtran0911, 2026 | 4 | Yes | OK |
| Veeraraghavan, Nguyen & Truong, 2007 | 1 | Yes | in-text et al. error (item 4) |

### Corrections Made
Per the task, nothing was changed in the manuscript. These are the corrections to apply.

| # | Location | Original | Corrected | Rule basis |
|---|----------|----------|-----------|-----------|
| C1 | Section 1, para 1 (Vietnam evidence sentence) | Veeraraghavan, Nguyen and Truong (2007) study momentum... | Veeraraghavan et al. (2007) study momentum... | APA 7: 3+ authors use "et al." from first citation |
| C2 | Section 1, para 2 (FDR sentence) | (Harvey et al., 2016; Benjamini & Hochberg, 1995) | (Benjamini & Hochberg, 1995; Harvey et al., 2016) | APA 7: multiple works in one parenthesis in alphabetical order |
| C3 | Reference list order | Bali entry placed after Berkman entries | Bali entry moved to the first position, before Benjamini | APA 7: alphabetical by first-author surname |
| C4 | Reference "tungtran0911" | tungtran0911. (2026). *vn-equity-factors* \[Source code and analysis, GitHub repository; not peer reviewed\]. <https://github.com/tungtran0911/vn-equity-factors> (accessed 4 October 2026) | tungtran0911. (2026). *vn-equity-factors* \[Source code\]. GitHub. Retrieved October 4, 2026, from https://github.com/tungtran0911/vn-equity-factors | APA 7 software/repository form; retrieval date placed before the URL ("Retrieved Month day, year, from URL") and justified because repository content changes; the "not peer reviewed" caveat already appears in the running text (Section 1) and need not be in the reference |
| C5 | Reference "Veeraraghavan" | Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price discovery and momentum strategies: Evidence from Vietnam* \[Working paper\]. SSRN. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1009042> | Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price discovery and momentum strategies: Evidence from Vietnam* (SSRN Scholarly Paper No. 1009042). Social Science Research Network. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1009042 | APA 7 working paper on SSRN. Use the https://doi.org/10.2139/ssrn.1009042 form instead of the URL only if the resolver confirms it (unchecked here). The series number is taken from the abstract_id in the supplied URL, so it is only as good as that URL (see F1) |
| C6 | Section 4.1, para 1 | the Harvey et al. threshold of 3 | the Harvey et al. (2016) threshold of 3 | APA 7: year at first narrative mention in each paragraph |

### Items Flagged for Review
| # | Location | Issue | Suggested action |
|---|----------|-------|------------------|
| F1 | Veeraraghavan, Nguyen & Truong (2007), SSRN 1009042 | Highest-risk entry: a Vietnam-specific working paper by three authors whose title and SSRN identifier are not independently corroborated in the manuscript. Appendix C itself states that some references in the verification log are "author-supplied or recalled". Nothing in the text is internally inconsistent (sample 2000-2006, year 2007), but the title, author initials ("M. T. T."), year, and abstract_id should be matched against the SSRN record | Route to the integrity agent for existence and metadata check. If the SSRN record differs, replace the entry and re-check the Section 1 claim ("momentum and price limits ... 2000-2006") |
| F2 | tungtran0911 (2026) repository | Pseudonymous GitHub username as author; claims (1.69% ceiling effect; 3-6.5% give-back of 0.39%; sample 2016-2026) are cited as an independent replication in the contributions paragraph and in Limitations. Not peer reviewed | Keep the authorship as the username (APA allows this); verify the repository and the quoted figures against the repository files; consider pinning a commit hash or release in the reference because repository content may change |
| F3 | Missing DOIs (7 entries) | Flag only; non-blocking. All seven items are journal articles that normally carry a DOI. This auditor believes the following DOIs are right but has not resolved them, so they are NOT in the corrected reference list or the error count: Imbens & Lemieux (2008) 10.1016/j.jeconom.2007.05.001; Newey & West (1987) 10.2307/1913610; Bali et al. (2011) 10.1016/j.jfineco.2010.08.014; Berkman et al. (2012) 10.1017/S0022109012000373. For Berkman & Lee (2002), Chen (1993) and Cho et al. (2003) the DOI should be looked up | Resolve each DOI, then add as https://doi.org/... with no trailing period |
| F4 | Section 3.1, methods named without citation | Holm adjustment, Parkinson range volatility, Amihud illiquidity are named but not cited (the manuscript's own Benjamini-Hochberg/Holm line cites only BH in Section 1). Not orphans, but a reader will expect sources, especially for characteristics defined in a "pre-registered family" | Optional: add Holm (1979), Parkinson (1980), Amihud (2002), and an author-date entry for each; if the authors choose not to, state in the text that these are standard definitions |
| F5 | Source currency | 14 of 17 sources are more than 10 years old and the only post-2019 source is a non-peer-reviewed repository (2026). For a theory/method paper this is tolerated (older share can reach 40%, but here it is 82%), and the price-limit literature is genuinely dated. Peer-reviewed work after 2019 on price limits, overnight returns, or Vietnamese retail trading is absent | Optional: add recent peer-reviewed sources on price limits and on Vietnam; the novelty claim in Section 1 ("no peer-reviewed study documents ... for HOSE") makes recent literature particularly relevant |
| F6 | Reference list sorting note | tungtran0911 is a lowercase username filed under "t", between Newey and Veeraraghavan. This is correct under APA letter-by-letter sorting | None |
| F7 | Non-citation internal paths | `process/...`, `R/...`, `paper2/...` file paths in Sections 3, Appendices, Declarations are not citations; ignored here | None |

### Corrected Reference List
(Alphabetical; C3, C4, C5 applied. DOIs not added where unresolved; see F3.)

Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. *Journal of Financial Economics, 99*(2), 427–446.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological), 57*(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). Paying attention: Overnight returns and the hidden cost of buying at the open. *Journal of Financial and Quantitative Analysis, 47*(4), 715–741.

Berkman, H., & Lee, J. B. T. (2002). The effectiveness of price limits in an emerging market: Evidence from the Korean Stock Exchange. *Pacific-Basin Finance Journal, 10*(5), 517–530.

Brennan, M. J. (1986). A theory of price limits in futures markets. *Journal of Financial Economics, 16*(2), 213–233. https://doi.org/10.1016/0304-405X(86)90061-9

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2011). Robust inference with multiway clustering. *Journal of Business & Economic Statistics, 29*(2), 238–249. https://doi.org/10.1198/jbes.2010.07136

Chen, Y.-M. (1993). Price limits and stock market volatility in Taiwan. *Pacific-Basin Finance Journal, 1*(2), 139–153.

Cho, D. D., Russell, J., Tiao, G. C., & Tsay, R. S. (2003). The magnet effect of price limits: Evidence from high-frequency data on Taiwan Stock Exchange. *Journal of Empirical Finance, 10*(1–2), 133–168.

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x

Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium: Empirical tests. *Journal of Political Economy, 81*(3), 607–636. https://doi.org/10.1086/260061

Harvey, C. R., Liu, Y., & Zhu, H. (2016). …and the cross-section of expected returns. *The Review of Financial Studies, 29*(1), 5–68. https://doi.org/10.1093/rfs/hhv059

Imbens, G. W., & Lemieux, T. (2008). Regression discontinuity designs: A guide to practice. *Journal of Econometrics, 142*(2), 615–635.

Kim, K. A., & Rhee, S. G. (1997). Price limit performance: Evidence from the Tokyo Stock Exchange. *The Journal of Finance, 52*(2), 885–901. https://doi.org/10.1111/j.1540-6261.1997.tb04827.x

Lou, D., Polk, C., & Skouras, S. (2019). A tug of war: Overnight versus intraday expected returns. *Journal of Financial Economics, 134*(1), 192–213. https://doi.org/10.1016/j.jfineco.2019.03.011

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica, 55*(3), 703–708.

tungtran0911. (2026). *vn-equity-factors* [Source code]. GitHub. Retrieved October 4, 2026, from https://github.com/tungtran0911/vn-equity-factors

Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price discovery and momentum strategies: Evidence from Vietnam* (SSRN Scholarly Paper No. 1009042). Social Science Research Network. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1009042

### Overall verdict
FAIL on format compliance (6 deterministic corrections C1-C6 outstanding; 0 orphans in either direction; 7 missing DOIs flagged, non-blocking). After applying C1-C6, the list is format-compliant, provided that F1 (existence/metadata of the Veeraraghavan et al. SSRN paper) and F2 (the repository figures) are cleared by the integrity agent.
