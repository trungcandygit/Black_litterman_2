# RQ Brief and Methodology Blueprint (Stage 1, quick mode)

## Research question

**Main RQ.** Did the stocks targeted by Vietnam's FTSE Russell reclassification become more liquid than comparable HOSE stocks, and at which disclosure stage did the change occur?

**Sub-questions**
- SQ1. Does the liquidity gap between constituents and other HOSE stocks open at the announcement (7 Oct 2025), the confirmation (7 Apr 2026), or the constituent list (21 Aug 2026)?
- SQ2. Did constituents record abnormal trading value on the rebalancing session (18 Sep 2026)?
- SQ3. Does the estimated effect survive matched controls, size-by-week fixed effects, a treated-specific trend, placebo dates and a near-miss falsification group?

**FINER screen**: Feasible (data collected: 405 HOSE stocks, 2024-10-01 to 2026-09-23); Interesting (first stock-level test of a frontier-to-emerging upgrade in Vietnam); Novel (gap confirmed in Stage 1 search, bounded by quick-mode coverage); Ethical (public market data, no human subjects); Relevant (regulators, index investors, target venue Finance Research Open).

## Methodology blueprint

| Element | Choice | Justification |
|---|---|---|
| Paradigm | Positivist, quasi-experimental | Named treatment group and public event dates |
| Design | Difference-in-differences with stage-specific windows; monthly event study | Separates recognition (gradual) from price-pressure (rebalancing) channels |
| Unit | Stock-week (daily measures aggregated; weeks with at least 3 trading days) | Reduces daily noise in Amihud and spreads |
| Treatment | 27 FTSE constituents announced 21 Aug 2026 (stocks listed after Oct 2025 drop out by the pre-period filter) | Official list |
| Controls | All other HOSE stocks passing filters; matched 3:1 sample (propensity score on pre-period traded value, price, volatility) | Ho et al. (2007) |
| Outcomes | log Amihud on traded value; log trading value; Corwin-Schultz spread | Amihud (2002); Corwin & Schultz (2012); Kang & Zhang (2014) |
| Fixed effects / inference | Stock and week FE; SE clustered by stock; two-way clustering as check | Chordia et al. (2000) commonality |
| Identification checks | Joint pre-trend test; treated-specific linear trend; size-tercile x week FE; placebo date Apr 2025; near-miss group (SAB, DXG, GEE, BSR, PLX) | Roth et al. (2023) |
| Sample filters | at least 200 pre-period days, zero-volume share below 20%, median price at least VND 1,000; winsorize daily measures at 1/99 by date | Standard liquidity-study hygiene |

## Devil's Advocate checkpoint (Phase 1)

| Challenge | Severity | Response in design |
|---|---|---|
| Constituents are the largest stocks; large caps may gain liquidity for unrelated reasons (2025 rally, anticipation before October 2025). Preliminary partial-sample estimates reject parallel pre-trends. | MAJOR | Treat as the central threat: matched sample, size-by-week FE, treated-specific trend; report event-study pre-period coefficients openly; soften causal language if pre-trends persist. |
| Treatment defined by the final list is determined after part of the sample; FTSE selects on size and liquidity. | MAJOR | Selection on pre-period levels is absorbed by stock FE; matching on pre-period liquidity; near-miss group tests selection on eligibility. |
| Effective date gives three post days only. | MINOR | Frame the paper on announcement, confirmation and list stages; rebalancing-day spike as SQ2; phased inclusion flagged as future work. |
| Amihud on weekly means can be dominated by extreme days. | MINOR | Daily winsorization; trading value and spreads as complementary outcomes. |

**Verdict**: PASS with two MAJOR design conditions carried into Stage 2 (pre-trend handling; selection on eligibility).
