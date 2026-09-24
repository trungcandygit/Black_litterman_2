# Research Brief

**Title**: Stock-level liquidity effects of Vietnam's FTSE Russell reclassification from frontier to secondary emerging status
**Date**: 2026-09-24
**Mode**: Quick Research Brief (ARS deep-research, Stage 1 of academic-pipeline run ftse2-20260924-01)
**AI Disclosure**: This brief was produced with AI-assisted research tools. Every reference below was checked against its Crossref record (see `bibliography_verified.md`); four DOIs recalled from memory resolved to unrelated papers and were replaced by the correct records before inclusion.

---

## Executive Summary

Index inclusion raises trading activity and narrows spreads in developed markets, and benchmark membership steers international capital flows. Evidence for frontier markets is weaker: an index effect on prices appears, but liquidity responses are inconsistent. No stock-level causal study yet separates the liquidity response of stocks that a frontier-to-emerging upgrade targets from market-wide trends. Vietnam's FTSE Russell upgrade provides the setting: four public dates (announcement, confirmation, constituent list, effective date) and a named group of 27 constituents among roughly 400 HOSE stocks. The brief recommends a stock-level difference-in-differences design with matched controls, an event study with explicit pre-trend diagnostics, and liquidity measured by the Amihud ratio on traded value and the Corwin-Schultz spread.

---

## Background & Research Question

### Context

Market classification decides which benchmark families a country's stocks can enter. Because mutual funds allocate across countries with reference to benchmark weights, changes in benchmark composition move capital into and out of the affected markets (Raddatz et al., 2017). An MSCI index change even moved currency values through this channel (Hau et al., 2010). At the stock level, additions to the S&P 500 produce price and volume effects (Harris & Gurel, 1986; Shleifer, 1986) and a lasting improvement in liquidity (Hegde & McDermott, 2003).

Frontier markets may not share this pattern. Biktimirov and Afego (2026) study FTSE Frontier 50 reconstitutions across frontier markets and report a price effect without a reliable link to liquidity. Vietnam, a retail-dominated market, was reclassified by FTSE Russell in a sequence of public steps: an announcement on 7 October 2025, confirmation on 7 April 2026, the list of 27 constituents on 21 August 2026, and an effective date of 21 September 2026 with phased inclusion to September 2027.

### Research Question

> Did the stocks targeted by Vietnam's FTSE Russell reclassification become more liquid than comparable HOSE stocks, and at which disclosure stage did the change occur?

### Scope

- **In scope**: HOSE common stocks, October 2024 to September 2026; liquidity (Amihud ratio on traded value, trading value, Corwin-Schultz spread); announcement, confirmation, constituent-list and rebalancing windows.
- **Out of scope**: price effects and returns as primary outcomes; the phased-inclusion tranches after September 2026 (not yet observable); foreign-flow data (not available in the price feed); HNX and UPCoM stocks other than the UPCoM-listed constituent MCH.

---

## Key Findings

### Finding 1: Index inclusion improves stock liquidity in developed markets
S&P 500 additions narrow spreads and raise trading activity, and the effect persists (Hegde & McDermott, 2003). Added firms with larger liquidity gains also raise investment (Becker-Blease & Paul, 2006), and FTSE 100 deletions show the mirror effect (Gregoriou & Nguyen, 2010). The price literature splits between temporary price pressure (Harris & Gurel, 1986) and a lasting shift in demand or investor awareness (Shleifer, 1986; Chen et al., 2004).

**Evidence strength**: Strong (repeated quasi-experimental evidence, top-tier journals)
**Source(s)**: Harris & Gurel (1986); Shleifer (1986); Hegde & McDermott (2003); Chen et al. (2004); Becker-Blease & Paul (2006); Gregoriou & Nguyen (2010)

### Finding 2: Benchmark membership moves international capital
Mutual-fund country allocations follow benchmark weights, so a reclassification shifts flows (Raddatz et al., 2017; Hau et al., 2010). The MSCI inclusion of China A-shares improved market quality through liquidity and price synchronization channels (Dong et al., 2023).

**Evidence strength**: Strong for the flow channel; Moderate for liquidity in large emerging markets
**Source(s)**: Raddatz et al. (2017); Hau et al. (2010); Dong et al. (2023)

### Finding 3: Frontier-market evidence on liquidity is weak or mixed
In frontier markets the index effect on prices persists, but measures of liquidity other than volume show no reliable relation to abnormal returns (Biktimirov & Afego, 2026). Liquidity is priced in emerging markets (Bekaert et al., 2007), so a liquidity response to reclassification would matter for the cost of capital.

**Evidence strength**: Emerging (few studies, heterogeneous settings)
**Source(s)**: Biktimirov & Afego (2026); Bekaert et al. (2007)

### Finding 4: Measurement and identification tools are established
The Amihud (2002) ratio must use traded value; Kang and Zhang (2014) evaluate liquidity proxies for emerging markets. Corwin and Schultz (2012) derive spreads from daily high and low prices. For identification, Roth et al. (2023) set current standards for pre-trend testing in difference-in-differences; with a single common treatment date, the staggered-adoption corrections of Callaway and Sant'Anna (2021) are not required, and matching on pre-treatment covariates reduces model dependence (Ho et al., 2007). Liquidity co-moves across stocks (Chordia et al., 2000), which argues for week fixed effects.

**Evidence strength**: Strong (methodological standards)
**Source(s)**: Amihud (2002); Kang & Zhang (2014); Corwin & Schultz (2012); Roth et al. (2023); Callaway & Sant'Anna (2021); Ho et al. (2007); Chordia et al. (2000)

---

## Analysis & Implications

### What This Means

The literature predicts a liquidity gain for index entrants but leaves open whether it appears in a frontier market that moves up a classification, and when. The recognition and information channel (Hegde & McDermott, 2003; Chen et al., 2004) predicts a gradual improvement from the announcement; the price-pressure channel (Harris & Gurel, 1986) predicts a volume spike at rebalancing. Vietnam's sequence of public dates lets one design separate the two.

The main threat is size-related trends: constituents are the largest HOSE stocks, and large stocks may gain liquidity for reasons unrelated to FTSE, including anticipation before October 2025. Preliminary estimates on a partial sample (not for citation) already reject parallel pre-trends, so the design must treat this threat as central.

### Recommendations
1. Estimate stage-specific DiD effects with stock and week fixed effects and stock-clustered errors; report an event study with a joint pre-trend test (Roth et al., 2023).
2. Add matched controls on pre-period traded value, price and volatility (Ho et al., 2007), size-tercile-by-week fixed effects, and a treated-specific linear trend as sensitivity checks; report all, including unfavorable ones.
3. Use the five near-miss stocks (named on FTSE eligibility lists but excluded) as a falsification group, and a placebo date inside the pre-period.

---

## Limitations
- Search covered Crossref records and the prior paper's verified corpus; no systematic database search (Scopus, Web of Science) was run in quick mode.
- Stock-level evidence on frontier-to-emerging reclassification is thin; Finding 3 rests mainly on one study.
- Post-effective-date data cover three trading days, so the brief cannot inform the phased-inclusion period.
- AI-assisted analysis: four initially recalled DOIs were wrong and were corrected; all claims about cited papers are limited to their titles, abstracts and the prior paper's verified summaries.

---

## References

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56. https://doi.org/10.1016/S1386-4181(01)00024-6

Becker-Blease, J. R., & Paul, D. L. (2006). Stock liquidity and investment opportunities: Evidence from index additions. *Financial Management, 35*(3), 35–51. https://doi.org/10.1111/j.1755-053X.2006.tb00146.x

Bekaert, G., Harvey, C. R., & Lundblad, C. (2007). Liquidity and expected returns: Lessons from emerging markets. *Review of Financial Studies, 20*(6), 1783–1831. https://doi.org/10.1093/rfs/hhm030

Biktimirov, E. N., & Afego, P. N. (2026). Is there an index effect in frontier markets? *International Review of Economics & Finance, 110*, 105562. https://doi.org/10.1016/j.iref.2026.105562

Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. https://doi.org/10.1016/j.jeconom.2020.12.001

Chen, H., Noronha, G., & Singal, V. (2004). The price response to S&P 500 index additions and deletions: Evidence of asymmetry and a new explanation. *The Journal of Finance, 59*(4), 1901–1930. https://doi.org/10.1111/j.1540-6261.2004.00683.x

Chordia, T., Roll, R., & Subrahmanyam, A. (2000). Commonality in liquidity. *Journal of Financial Economics, 56*(1), 3–28. https://doi.org/10.1016/S0304-405X(99)00057-4

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x

Dong, S., Zheng, J., Jia, H., & Zhang, Z. (2023). Impact of capital market internationalization on stock markets: Evidence from the inclusion of China A-shares in the MSCI Emerging Markets Index. *Research in International Business and Finance, 66*, 101989. https://doi.org/10.1016/j.ribaf.2023.101989

Gregoriou, A., & Nguyen, N. D. (2010). Stock liquidity and investment opportunities: New evidence from FTSE 100 index deletions. *Journal of International Financial Markets, Institutions and Money, 20*(3), 267–274. https://doi.org/10.1016/j.intfin.2010.03.005

Harris, L., & Gurel, E. (1986). Price and volume effects associated with changes in the S&P 500 list: New evidence for the existence of price pressures. *The Journal of Finance, 41*(4), 815–829. https://doi.org/10.1111/j.1540-6261.1986.tb04550.x

Hau, H., Massa, M., & Peress, J. (2010). Do demand curves for currencies slope down? Evidence from the MSCI global index change. *Review of Financial Studies, 23*(4), 1681–1717. https://doi.org/10.1093/rfs/hhp095

Hegde, S. P., & McDermott, J. B. (2003). The liquidity effects of revisions to the S&P 500 index: An empirical analysis. *Journal of Financial Markets, 6*(3), 413–459. https://doi.org/10.1016/S1386-4181(02)00046-0

Ho, D. E., Imai, K., King, G., & Stuart, E. A. (2007). Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference. *Political Analysis, 15*(3), 199–236. https://doi.org/10.1093/pan/mpl013

Kang, W., & Zhang, H. (2014). Measuring liquidity in emerging markets. *Pacific-Basin Finance Journal, 27*, 49–71. https://doi.org/10.1016/j.pacfin.2014.02.001

Raddatz, C., Schmukler, S. L., & Williams, T. (2017). International asset allocations and capital flows: The benchmark effect. *Journal of International Economics, 108*, 413–430. https://doi.org/10.1016/j.jinteco.2017.06.007

Roth, J., Sant'Anna, P. H. C., Bilinski, A., & Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. *Journal of Econometrics, 235*(2), 2218–2244. https://doi.org/10.1016/j.jeconom.2023.03.008

Shleifer, A. (1986). Do demand curves for stocks slope down? *The Journal of Finance, 41*(3), 579–590. https://doi.org/10.1111/j.1540-6261.1986.tb04518.x
