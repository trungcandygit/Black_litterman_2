**Abstract.** Daily price limits aim to cool markets but can delay price discovery. Few studies trace prices after limit closes in emerging markets, and none we know of tests the limit against other candidate signals. For 347 stocks on the Ho Chi Minh Stock Exchange from August 2024 to September 2026, we run 26 tests under false-discovery-rate control: four price-limit event tests and 22 price- and volume-based characteristics. All four limit tests survive; none of the 22 lower-powered characteristic tests does. After a ceiling close, the next-day abnormal return of 1.7% is an overnight gap of 2.2% less an intraday reversal of 0.5%, and the gap exceeds that after rises of 5% to 6.5% by 2.7 percentage points. A buyer at the next open loses 0.7% against the market by the fifth close. Delayed price discovery fits the pattern, but so do news and attention; without news or order-book data we cannot separate them.

**Keywords:** price limits; overnight returns; multiple testing; market microstructure; Vietnam

**JEL classification:** G14; G15; G18

# 1. Introduction

A daily price limit stops a stock from moving beyond a fixed band within one trading day. Exchanges in Tokyo, Taipei, Seoul, Shenzhen, and Ho Chi Minh City have used limits to cool markets after large shocks, and economists ask whether a limit protects prices or postpones their adjustment. The question is sharpest where limit closes are common and call auctions set the opening and closing prices. The Ho Chi Minh Stock Exchange (HOSE) has both features: one 7% band applies to all stocks, and about 2.0% of stock-days in our event window close at the upper limit (a ceiling close; Section 4) and about 1.4% at the lower limit (a floor close).

Studies of band changes document effects on volatility, liquidity, and crash risk (Jia et al., 2024; Lien et al., 2019; Qi, 2023), and account-level data show that large investors buy on the limit day and sell on the next (Chen et al., 2019). Of the studies we reviewed, only Huang et al. (2001) describe the overnight-then-intraday pattern after limit hits, and the records we could access give no magnitudes. None measures the overnight gap and the intraday return after a limit close against a benchmark, places the limit result in a family of tests that controls for the other price-based signals a researcher could have examined, or examines the 2025 move of HOSE to a new trading platform.

We estimate the abnormal return after ceiling and floor closes on HOSE, split it into the overnight gap and the intraday return, and test whether an outside buyer can capture it. We place the four limit tests in a family of 26 tests with 22 price- and volume-based characteristics and control the false discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).

We make three contributions. First, we measure the overnight gap and the intraday return after limit closes, a pattern that Huang et al. (2001) describe qualitatively for Taiwan, and show that the ceiling effect is a gap of 2.2% of which the following session reverses 24%. Second, we show that the ceiling gap is 2.7 percentage points larger than after rises of 5% to 6.5% that stop short of the limit, and that the contrast survives when the comparison stocks also close at their daily high. Third, we show that all four limit tests survive a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open loses 0.7% against the market by the fifth close. We also split the events at the 2025 platform change.

Section 2 reviews the literature, Sections 3 and 4 describe the data and design, Section 5 reports results, Section 6 discusses them, and Sections 7 and 8 give limitations and conclusions.

# 2. Related literature and hypotheses

**Theory.** Models predict protection or distortion, depending on the source of the shock. Brennan (1986) rationalizes limits in futures markets, Kodres and O’Brien (1994) show that limits can be Pareto superior when fundamental news drives prices because they insure traders against implementation risk, and Greenwald and Stein (1991) link crashes to imperfect transactional mechanisms. Subrahmanyam (1994) shows that halts can advance trades in time and raise price variability, and in the model of Chen et al. (2024) volatility rises as the price nears a circuit breaker, a magnet effect. A limit that only delays adjustment leaves a predictable next-day continuation, which the return after a limit close can reveal.

**Classic evidence.** Kim and Rhee (1997) find support in Tokyo for three criticisms of limits: they spill volatility into later days, delay price discovery, and interfere with trading. Bildik and Gülay (2006) find the same in Istanbul, with stronger evidence from price locks than from limit moves alone. Chen (1993) finds that serial correlation falls as the Taiwanese limit widens, which implies delayed adjustment under the narrower limit, and Berkman and Lee (2002) examine volatility and trading activity around a revision of the Korean limit system. Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits reverses during the following day, the timing pattern we test. Cho et al. (2003) find a magnet effect: prices accelerate toward the upper limit in five-minute Taiwanese data. Kim and Limpaphayom (2000) show that small, volatile, high-volume stocks hit limits more often, and Deb et al. (2013) argue that rigid limits in Tokyo can disrupt price discovery and liquidity provision.

**Band changes and investor-level data.** After ChiNext widened its band from 10% to 20% in August 2020, Qi (2023) confirms delayed price discovery, volatility spillover, and trading interference, stronger at the lower limit and with no magnet effect; Zhang et al. (2022) find higher liquidity, volatility, and probability of informed trading; and Jia et al. (2024) find lower crash risk. Wider bands raised spreads and intraday volatility but improved execution quality in Taiwan (Lien et al., 2019) and raised intraday realized variance in Korea (Kim & Jun, 2019). In Shenzhen account data, large investors buy on the day a stock hits the 10% upper limit and sell the next day, and their limit-day net buying predicts stronger long-run reversal (Chen et al., 2019). Stocks with large limit exposure attract attention and earn lower future returns, most where retail investors hold many shares (Lin et al., 2023), as do stocks with frequent upper-limit hits (Zeng et al., 2024). Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit.

**Overnight and intraday returns.** Kelly and Clark (2011) show for index funds that overnight and intraday returns differ. In U.S. stocks, positive overnight returns are followed by intraday reversals, concentrated among stocks with recent retail attention (Berkman et al., 2012). Aboody et al. (2018) tie overnight persistence to sentiment, Lou et al. (2019) find overnight and intraday continuation with an offsetting cross-period reversal, Akbas et al. (2022) find that persistent positive-overnight, negative-daytime patterns predict higher returns, Bogousslavsky (2021) links the split to margin and lending costs, and Lu et al. (2023) link it to market makers who absorb retail imbalances near the open. In China, overnight returns are negative on average, which Qiao and Dam (2020) link to the T+1 rule that bars selling shares on the day of purchase; the lottery-like anomaly arises mainly overnight (Gu et al., 2025); day-night anomalies concentrate at the open and close (Qiu et al., 2025); and small retail investors show weak stock selection (Jones et al., 2025).

**Multiple testing and weekly regressions.** Harvey et al. (2016) argue that a new factor needs a *t*-statistic above 3.0, Harvey and Liu (2020) tie the hurdle to a chosen FDR, Chordia et al. (2020) put multiple-testing thresholds for cross-sectional regressions near 3.4, and Hou et al. (2020) find that, with microcaps mitigated, 65% of 452 anomalies fail the single-test hurdle of 1.96. Petersen (2009) compares standard-error estimators for panel data, which motivates our alternative clusters, and Gutierrez and Kelley (2008) study weekly returns, the frequency of our regressions. For Vietnam, Huang et al. (2023) find a size effect and an earnings-to-price effect; we found no peer-reviewed study of post-limit returns on HOSE.

**Gap and hypotheses.** These studies compare band regimes, sort stocks by limit exposure, or split overnight and intraday returns for all stocks. Only Huang et al. (2001) link limit hits to the overnight-intraday split, and none controls for multiple testing or uses the 2025 platform change. If a limit delays price discovery, a ceiling close predicts a positive next-day abnormal return and a floor close a negative one (H<sub>1</sub>). If the opening auction absorbs the blocked demand, the effect concentrates in the overnight gap (H<sub>2</sub>). If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of similar size that stop short of the limit (H<sub>3</sub>). An investor who buys at the next open earns no positive abnormal return through the fifth trading day (H<sub>4</sub>). A limit effect that survives the screen applied to all 22 characteristics is more credible than a single large estimate.

# 3. Data and institutional setting

**Data source.** On 24 September 2026, we downloaded daily open, high, low, close, and volume series for all HOSE-listed stocks with the vnstock Python library (version 4.0.4; source Vietcap Securities, VCI). A listing file from the same source and date (743 rows, all instrument types) defines the universe. The retrieval returned 405 HOSE stock files with records through 23 September 2026, and we use the 519 trading days from 21 August 2024. Prices are in thousand dong. The vendor does not document corporate-action adjustment, and the files contain no market capitalization, order book, investor type, or news.

**Sample.** We keep the 347 stocks with at least 95% non-missing closes, 178,773 stock-days in all. The daily close-to-close return has a mean of 0.018%, a median of 0.00%, and a standard deviation of 2.10%. Dollar volume (price times shares traded, in dong) is skewed, with a median of 2.6 billion dong per stock-day and a mean of 51.2 billion. The stocks span 18 two-digit Industry Classification Benchmark sectors; the largest holds 15% of them.

**Institutional setting.** HOSE sets a daily price limit of 7% around the reference price, the previous close on normal trading days (Ho Chi Minh City Securities Corporation \[HSC\], 2025). On 5 May 2025, HOSE moved to the trading platform of the Korea Exchange (KRX). The band stayed unchanged, but at-the-open and at-the-close orders lost their priority over limit orders in the opening and closing call auctions (HSC, 2025; Viet Nam News, 2025), whose prices define our events and gaps. Treating the band, tick sizes, and reference-price rule as assumptions, we check the band against the data: 1.98% of stock-days fall between +6.5% and +7.1% and 1.30% between −7.1% and −6.5%, against 0.29% between +6.0% and +6.5%, a pile-up consistent with a 7% band.

# 4. Design

**Returns and events.** For stock $i$ on trading day $d$, $C_{i,d}$, $O_{i,d}$, $H_{i,d}$, and $L_{i,d}$ are the close, open, high, and low prices, and the close-to-close return is

$$R_{i,d} = \frac{C_{i,d}}{C_{i,d - 1}} - 1.\quad\quad\text{(1)}$$

A ceiling event has $R_{i,d} \geq 0.065$ and $C_{i,d} = H_{i,d}$, and a floor event has $R_{i,d} \leq - 0.065$ and $C_{i,d} = L_{i,d}$. The event window runs from day 61, once a 60-day volume history exists, to five days before the sample end. The market return weights stocks by dollar volume,

$$R_{d}^{\text{mkt}} = \sum_{j}^{}w_{j,d}\, R_{j,d},\quad\quad w_{j,d} = \frac{{\overline{V}}_{j,d}}{\sum_{l}^{}{\overline{V}}_{l,d}},\quad\quad\text{(2)}$$

where $j$ and $l$ run over stocks with a day-$d$ return and a full 60-day history, and ${\overline{V}}_{j,d}$ is the mean dollar volume of stock $j$ over the 60 trading days through day $d$.

**Exact hits.** An exact hit is an event whose close equals the limit price (within $10^{- 6}$ thousand dong),

$$P_{i,d}^{\text{ceiling}} = \left\lfloor \frac{1.07\, C_{i,d - 1}}{\delta} \right\rfloor\delta,\quad\quad P_{i,d}^{\text{floor}} = \left\lceil \frac{0.93\, C_{i,d - 1}}{\delta} \right\rceil\delta,\quad\quad\text{(3)}$$

where $\lfloor \cdot \rfloor$ and $\lceil \cdot \rceil$ round down and up (after adding and subtracting $10^{- 9}$, respectively, against floating-point error), and the tick $\delta$ is 0.01, 0.05, or 0.10 thousand dong for reference prices $C_{i,d - 1}$ below 10, from 10 to below 50, and from 50 upward. Other events are near hits (see Section 7 on vendor price adjustment).

**Outcomes.** The abnormal return (AR) on day $d + 1$ and the cumulative abnormal return (CAR) over days $d + 1$ to $d + 5$ are

$${AR}_{i,d} = R_{i,d + 1} - R_{d + 1}^{\text{mkt}},\quad\quad{CAR}_{i,d} = \prod_{k = 1}^{5}\left( 1 + R_{i,d + k} \right) - \prod_{k = 1}^{5}\left( 1 + R_{d + k}^{\text{mkt}} \right),\quad\quad\text{(4)}$$

where each $R_{d + k}^{\text{mkt}}$ uses weights through day $d + k$ (Table 1). The day-$d + 1$ return splits into the overnight gap and the intraday return,

$${GAP}_{i,d} = \frac{O_{i,d + 1}}{C_{i,d}} - 1,\quad\quad{INTRA}_{i,d} = \frac{C_{i,d + 1}}{O_{i,d + 1}} - 1,\quad\quad 1 + R_{i,d + 1} = \left( 1 + {GAP}_{i,d} \right)\left( 1 + {INTRA}_{i,d} \right),\quad\quad\text{(5)}$$

and abnormal values subtract the market counterpart of each component, the same-interval return across stocks weighted with $w_{j,d}$, known at the event close. A buyer at the next open earns $C_{i,d + 5}/O_{i,d + 1} - 1$ less the buy-and-hold market return $\sum_{j}^{}w_{j,d}\,\left( C_{j,d + 5}/O_{j,d + 1} - 1 \right)$. The control benchmark is the equal-weighted mean same-interval return of control stocks (absolute day-$d$ return below 6.5%) in the event stock’s tercile of ${\overline{V}}_{i,d}$ on that date; dates with fewer than 30 control stocks have no benchmark.

**Inference.** For $N$ events $e$, each a stock-day pair, with outcome $y_{e}$ and mean $\overline{y} = N^{- 1}\sum_{e}^{}y_{e}$, the cluster-robust variance is

$$\widehat{Var}\left( \overline{y} \right) = \frac{1}{N^{2}} \cdot \frac{G}{G - 1}\sum_{g = 1}^{G}\left( \sum_{e \in g}^{}\left( y_{e} - \overline{y} \right) \right)^{2},\quad\quad\text{(6)}$$

where $g = 1,\ldots,G$ indexes clusters: event dates, ISO calendar weeks, or blocks of ten consecutive trading days. The family *p*-values of the four event tests use Equation (6) with event-date clusters, omit $G/(G - 1)$, and take a normal reference; Table 1 *t*-statistics include the factor and use a *t* reference with $G - 1$ degrees of freedom. Two-way clustering by date and stock follows Cameron et al. (2011), without the factor and with the variance bounded below at $10^{- 12}$. Table 3 reports $\widehat{\beta}$ from $y_{e} = \alpha + \beta D_{e} + u_{e}$, where $D_{e} = 1$ for limit closes, with date-clustered HC1 standard errors (R package *sandwich*).

**Characteristics.** We form cross-sections on trading days 120 (so that every lookback is complete), 125, and so on to 510: $T = 79$ formation weeks $\tau$, each followed by a non-overlapping five-day holding period. Each week we rank-normalize each characteristic $x_{i,\tau}$ across the $n_{\tau}$ stocks with complete data (all 115 days of the longest lookback, trades on 50 of the last 60 days, and next-five-day returns) as $z_{i,\tau} = \Phi^{- 1}\left( \left( rank\left( x_{i,\tau} \right) - 0.5 \right)/n_{\tau} \right)$, with ties at average ranks and $\Phi^{- 1}$ the inverse standard normal distribution function. The outcome $y_{i,\tau}$ is the stock’s compounded return over the next five trading days minus the $\overline{V}$-weighted average five-day return of these stocks. The Fama and MacBeth (1973) regressions are

$$y_{i,\tau} = a_{\tau} + \gamma_{\tau}\, z_{i,\tau} + \varepsilon_{i,\tau},\quad\quad\widehat{\gamma} = \frac{1}{T}\sum_{\tau = 1}^{T}{\widehat{\gamma}}_{\tau},\quad\quad\text{(7)}$$

with weekly intercept $a_{\tau}$. The *t*-statistic of $\widehat{\gamma}$ uses Newey and West (1987) standard errors (four lags, Bartlett weights, no prewhitening) and 78 degrees of freedom. Appendix A defines the 22 momentum, reversal, risk, liquidity, volume, and intraday characteristics. We also report long–short spreads between the extreme quintiles, before and after a cost of 25 basis points per unit of traded value. The minimum detectable effect at 80% power and a 5% two-sided level is $\text{MDE} = (1.96 + 0.84)\,\widehat{\text{SE}}\left( \widehat{\gamma} \right) \approx 2.8\,\widehat{\text{SE}}\left( \widehat{\gamma} \right)$, with $\widehat{\text{SE}}$ the Newey–West standard error.

**Multiplicity and survival.** The family has $m = 26$ tests: 22 characteristics and the ceiling and floor tests at the two horizons of Equation (4). With *p*-values ordered as $p_{(1)} \leq \ldots \leq p_{(m)}$, the Benjamini–Hochberg (BH) adjusted *p*-value at rank $r$ is

$${\widetilde{p}}_{(r)} = \min_{s \geq r}\left\{ \min\left( 1,\frac{m}{s}\, p_{(s)} \right) \right\},\quad\quad\text{(8)}$$

and we also report Holm (1979) adjustments and the \|*t*\| = 3 hurdle of Harvey et al. (2016). A test survives if $\widetilde{p} < 0.05$, which controls the FDR at 5%; if its signs agree in the discovery half (the first 39 weeks, or events up to the median event date) and the confirmation half; and if its confirmation-half \|*t*\| exceeds 1.96. Lookbacks overlap the discovery half, so the confirmation half is not a strict hold-out, and the weekly regressions (from day 120) and event window (from day 61) cover different spans.

**Analysis plan.** We fixed the family, estimators, multiplicity control, and survival rule in a written analysis plan before computing results. A version-control time stamp dates the plan before the first analysis code, but no external registry holds it and we had examined related data in earlier work, so it gives no independent confirmation. We departed from it by reading its ambiguous second horizon as days *d*+1 to *d*+5 (not *d*+2 to *d*+5), splitting event halves at the median event date (not weeks 39 and 40), reporting quintile rather than decile spreads, and omitting its same-stock control and multivariate model. Analyses added after the first results are exploratory, and the tests of H<sub>2</sub> to H<sub>4</sub> rest on them: the decomposition, next-open returns, control group, sub-limit comparison, exact hits, two-way clustering, subsamples, terciles, platform split, and outlier exclusion. We also screened several candidate ideas on the same data before choosing this one, so effect sizes may be overstated.

# 5. Results

The event sample holds 3,187 ceiling events on 446 dates and 2,105 floor events on 319 dates. Limit closes cluster in market episodes, so our standard errors allow dependence across dates, weeks, 10-day blocks, and stocks.

Figure 1 plots the *t*-statistics of the 22 slopes $\widehat{\gamma}$ in Equation (7): none reaches \|*t*\| = 3 in any sample or 1.96 in the full sample, and none survives the BH control. The largest full-sample \|*t*\| is 1.45, for 3-month and idiosyncratic momentum (confirmation-half *t* of 1.17 and 1.14). After the 25-basis-point cost, 18 of the 22 long–short quintile spreads are negative. With 79 weekly cross-sections, the MDE at 80% power is 0.12 to 0.31 percentage points per week per standard deviation, so the null excludes only large effects. With eight Newey–West lags the largest \|*t*\| is 1.79, and dropping the least liquid 20% of stocks leaves it at 1.62.

Without market capitalization or accounting data, we cannot test the size and earnings-to-price effects that Huang et al. (2023) find in Vietnam, so our null does not contradict theirs. A short sample, which leaves a premium of a tenth of a percentage point per week below the MDE, and limits that censor the highs and lows of range-based characteristics can each produce the null, and we draw no conclusion about market efficiency from it.

<img src="media/rId24.png" style="width:6.29167in;height:4.45256in" alt="Figure 1. t-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half (first 39 weeks), and the confirmation half, ordered by absolute full-sample t. Appendix A defines the labels. Dashed lines mark |t| = 1.96 and dotted lines |t| = 3." />

Figure 1. *t*-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half (first 39 weeks), and the confirmation half, ordered by absolute full-sample *t*. Appendix A defines the labels. Dashed lines mark \|*t*\| = 1.96 and dotted lines \|*t*\| = 3.

Table 1 reports the event tests. Ceiling closes earn a market-adjusted return of 1.66% on day *d*+1 and 1.45% over days *d*+1 to *d*+5, and floor closes earn −0.71% and −1.76%. All four tests survive the BH control (Equation (8); adjusted *p*-values of at most 0.0004), keep their signs in both halves, and exceed \|*t*\| = 1.96 in the confirmation half. Clustering by calendar week or 10-day block, with a *t* reference, leaves all four significant. The floor five-day test clears the confirmation criterion by the smallest margin (*t* = −2.22 with week clusters), and all four tests survive the rule re-applied with week-clustered statistics.

For ceilings, the five-day result comes from the first day: over days *d*+2 to *d*+5 the ceiling return is −0.24% (*t* = −1.53). After floor closes, days *d*+2 to *d*+5 add −1.10% (*t* = −2.91), but the confirmation-half week-clustered *t* is −1.14. With days *d*+2 to *d*+5 as the second horizon, the ceiling test would fail and the floor test would fail the confirmation criterion. Ceiling closes carry a one-day effect, and floor closes a one-day effect plus some later drift. These tests support H<sub>1</sub>: limit closes predict the next day’s abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon.

Table 1. Market-adjusted returns (percent) after ceiling and floor closes. *t* (date), *t* (week), and *t* (10-day) cluster by event date, calendar week, and 10-day block, with the factor *G*/(*G* − 1) for *G* clusters and a *t* reference with *G* − 1 degrees of freedom. *t* (halves) gives week-clustered statistics for the first and second half of event dates. Events require complete returns for days *d*+1 to *d*+5.

| **Event** | **Horizon**    | **Mean (%)** | ***t* (date)** | ***t* (week)** | ***t* (10-day)** | ***t* (halves)** | **Events** |
|-----------|----------------|--------------|----------------|----------------|------------------|------------------|------------|
| Ceiling   | *d*+1          | 1.66         | 4.90           | 4.67           | 4.61             | 2.2 / 13.7       | 3,187      |
| Ceiling   | *d*+1 to *d*+5 | 1.45         | 4.00           | 3.67           | 3.81             | 1.7 / 5.0        | 3,187      |
| Ceiling   | *d*+2 to *d*+5 | −0.24        | −1.53          | −1.11          | −1.25            | −1.1 / −0.4      | 3,187      |
| Floor     | *d*+1          | −0.71        | −5.32          | −4.66          | −6.25            | −2.7 / −4.6      | 2,105      |
| Floor     | *d*+1 to *d*+5 | −1.76        | −4.74          | −4.80          | −4.92            | −12.3 / −2.2     | 2,105      |
| Floor     | *d*+2 to *d*+5 | −1.10        | −2.91          | −3.01          | −2.81            | −8.7 / −1.1      | 2,105      |

Table 2 decomposes the next-day return as in Equation (5). After a ceiling close the overnight gap is 2.24% (two-way-clustered *t* = 9.7) and the intraday return is −0.54% (*t* = −3.5): the session reverses about 24% of the gap, and the close-to-close effect is positive because the gap exceeds the giveback. The effect sits in the opening auction, as H<sub>2</sub> predicts. Unfilled buy orders carried into the night and any overnight news set the opening price, and the intraday reversal suggests that part of that price reflects transient demand.

After a floor close the gap is −0.97% (*t* = −4.6) and the intraday return is a weak reversal of 0.30%. The ceiling gap holds for exact limit hits (2.79%) and for the first day of a streak of exact hits (2.39%). Near hits show a smaller gap (1.67%) and no significant intraday return, but their median day-*d* return is 6.89% against 6.90% for exact hits, and 83% of their closes are not multiples of the tick size. This points to later price adjustment by the vendor, concentrated in higher-priced stocks with coarser ticks, rather than to closes below the limit, so we do not read the difference as a gradient toward the limit. The gap appears in both halves of the sample, on days locked at one price from open to close, and, for ceilings, in each tercile of 60-day average dollar volume (1.52% in the most liquid). Against same-date controls the ceiling gap is 2.70% and the floor close-to-close return −1.65%, so the floor effect depends on the benchmark. Floor events cluster on market-wide down days (740 of 2,111 remain without days on which the market fell more than 2%), and the floor gap is not significant in the least liquid tercile (*t* = −1.0).

An outside buyer cannot capture the close-to-close continuation: a buyer who wants a stock at its ceiling joins a queue at the close, so the first obtainable price is the next open, which already contains the gap. From that open the ceiling return through the fifth close is −0.75% against the market (*t* = −2.7) and −0.53% against same-date controls (*t* = −1.8), which supports H<sub>4</sub>; a holder who sells at the next open avoids the intraday giveback. These figures use quoted prices and ignore achievable fills: 522 ceiling events were locked at one price all day, and some of these stocks opened at the limit the next day, where a buyer may be rationed. After floor closes, prices fall a further 0.82% from the next open to the fifth close against the market (*t* = −1.7), which is not significant at the 5% level.

Table 2. Next-day abnormal returns (percent) by component and sample, with two-way-clustered *t*-statistics in parentheses. Benchmarks are the dollar-volume-weighted market (weights lagged to day *d*) or same-date control stocks in the same liquidity tercile (Section 4). Open to day *d*+5 runs from the day-*d*+1 open to the day-*d*+5 close. Crash days have a market return (Equation (2)) below −2%. Close-to-close need not equal the sum of the components because returns compound.

| **Sample**                        | **Events** | **Overnight gap** | **Intraday** | **Close-to-close** | **Open to day *d*+5** |
|-----------------------------------|------------|-------------------|--------------|--------------------|-----------------------|
| Ceiling closes                    |            |                   |              |                    |                       |
| All, vs market                    | 3,199      | 2.24 (9.7)        | −0.54 (−3.5) | 1.66 (4.8)         | −0.75 (−2.7)          |
| All, vs same-date controls        | 3,100      | 2.70 (20.2)       | −0.50 (−6.0) | 2.16 (18.0)        | −0.53 (−1.8)          |
| Exact limit hit                   | 1,642      | 2.79 (13.8)       | −0.74 (−5.3) | 2.00 (7.1)         | −1.02 (−3.0)          |
| Near hit                          | 1,557      | 1.67 (6.4)        | −0.32 (−1.6) | 1.31 (3.1)         | −0.46 (−1.3)          |
| Locked all day                    | 522        | 2.91 (3.0)        | −1.30 (−5.9) | 1.54 (1.4)         | −0.76 (−1.5)          |
| First half of sample              | 1,615      | 2.24 (5.4)        | −0.77 (−3.3) | 1.42 (2.3)         | −1.13 (−2.9)          |
| Second half of sample             | 1,584      | 2.25 (13.0)       | −0.29 (−2.5) | 1.91 (11.3)        | −0.36 (−1.2)          |
| Excluding days with market \< −2% | 3,125      | 2.24 (9.6)        | −0.53 (−3.4) | 1.67 (4.7)         | −0.70 (−2.6)          |
| Floor closes                      |            |                   |              |                    |                       |
| All, vs market                    | 2,111      | −0.97 (−4.6)      | 0.30 (1.4)   | −0.69 (−4.8)       | −0.82 (−1.7)          |
| All, vs same-date controls        | 2,047      | −1.75 (−4.0)      | 0.14 (0.6)   | −1.65 (−3.4)       | −0.36 (−0.6)          |
| Exact limit hit                   | 1,025      | −1.30 (−5.1)      | 0.41 (1.7)   | −0.93 (−5.7)       | −0.98 (−1.9)          |
| Near hit                          | 1,086      | −0.66 (−3.7)      | 0.20 (0.9)   | −0.47 (−2.9)       | −0.66 (−1.4)          |
| Locked all day                    | 260        | −2.50 (−4.8)      | 1.11 (2.4)   | −1.44 (−3.4)       | −3.91 (−3.0)          |
| First half of sample              | 1,059      | −0.55 (−2.4)      | −0.09 (−0.3) | −0.63 (−2.9)       | −1.69 (−5.1)          |
| Second half of sample             | 1,052      | −1.40 (−6.5)      | 0.70 (4.9)   | −0.75 (−4.3)       | 0.07 (0.1)            |
| Excluding days with market \< −2% | 740        | −1.83 (−8.7)      | 0.90 (5.3)   | −0.99 (−4.5)       | −0.81 (−1.7)          |

Figure 2 plots the three next-day measures against the size of the day-*d* move. Inside the band the close-to-close relation is negative, a short-term reversal. At the limit the relation breaks, and the overnight gap jumps up at the ceiling and down at the floor.

<img src="media/rId27.png" style="width:6.29167in;height:2.71026in" alt="Figure 2. Next-day abnormal return (overnight gap, intraday, and close-to-close) by the size of the day-d move. Circles are 1-percentage-point bins inside the band, triangles are ceiling and floor events, and squares are other moves of 6.5% to 10% in absolute value. Bars show 95% confidence intervals clustered by date (normal reference, no small-sample factor). Market weights are lagged to day d; the figure uses event days up to the second-to-last trading day." />

Figure 2. Next-day abnormal return (overnight gap, intraday, and close-to-close) by the size of the day-*d* move. Circles are 1-percentage-point bins inside the band, triangles are ceiling and floor events, and squares are other moves of 6.5% to 10% in absolute value. Bars show 95% confidence intervals clustered by date (normal reference, no small-sample factor). Market weights are lagged to day *d*; the figure uses event days up to the second-to-last trading day.

Table 3 quantifies the break. Ceiling closers have a gap 2.66 percentage points larger than stocks that rose 5% to 6.5% (*t* = 14.0) and an intraday return 0.31 points lower. Floor closers have a gap 1.59 points lower than stocks that fell 5% to 6.5% (*t* = −9.7). Because the event rule requires a close at the day’s high (low), we repeat the comparison with stocks that also closed there. The ceiling gap is then 3.14 points larger (*t* = 14.5) and the floor gap 1.81 points lower, so a strong close does not explain the contrast, which supports H<sub>3</sub>. Against 3% to 5% moves, the ceiling gap is 2.40 percentage points larger and the floor gap 1.14 points lower. The comparison is an association around a rule-based threshold, and we make no regression-discontinuity claim: the design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.

Table 3. Differences in next-day abnormal returns (percentage points) between limit closes and same-direction moves of 3–5% or 5–6.5% that did not close at the limit, with date-clustered *t*-statistics in parentheses. Returns are market-adjusted with lagged weights.

| **Contrast**                        | **Overnight gap** | **Intraday** | **Close-to-close** | **Open to day *d*+5** | **Comparison stock-days** |
|-------------------------------------|-------------------|--------------|--------------------|-----------------------|---------------------------|
| Ceiling vs 5–6.5% rises             | 2.66 (14.0)       | −0.31 (−2.1) | 2.32 (7.6)         | −0.02 (−0.1)          | 1,751                     |
| same, comparison closes at its high | 3.14 (14.5)       | −0.66 (−3.4) | 2.47 (7.2)         | −0.49 (−1.5)          | 679                       |
| Ceiling vs 3–5% rises               | 2.40 (11.6)       | −0.32 (−2.2) | 2.05 (6.1)         | −0.45 (−2.2)          | 5,932                     |
| same, comparison closes at its high | 2.81 (13.1)       | −0.61 (−3.8) | 2.17 (6.4)         | −0.64 (−2.7)          | 1,795                     |
| Floor vs 5–6.5% falls               | −1.59 (−9.7)      | −0.07 (−0.3) | −1.66 (−11.6)      | −1.01 (−2.6)          | 1,522                     |
| same, comparison closes at its low  | −1.81 (−8.7)      | −0.13 (−0.6) | −1.95 (−10.7)      | −1.23 (−2.8)          | 722                       |
| Floor vs 3–5% falls                 | −1.14 (−6.4)      | 0.14 (0.6)   | −1.01 (−7.5)       | −0.90 (−2.2)          | 5,237                     |
| same, comparison closes at its low  | −1.35 (−7.4)      | 0.18 (0.8)   | −1.19 (−8.0)       | −1.06 (−2.5)          | 2,228                     |

Three readings fit the pattern, and our data do not separate them: (1) demand or supply that the limit blocked on day *d* clears at the next opening, the delayed price discovery of Kim and Rhee (1997); (2) news and retail attention persist overnight and produce the overnight gain and intraday reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit; and (3) the opening auction overshoots and corrects within the day. Lacking announcements, order books, and limit-free stock-days, we run two partial checks. First, the ceiling gap rises across terciles of day-*d* volume relative to its prior 60-day mean (1.97%, 2.16%, and 2.63%) and of the prior 20-day return (1.41%, 2.18%, and 3.16%), which fits readings (1) and (2) alike, and stays positive and significant in the lowest tercile of each proxy (*t* = 4.8 and 4.2). For floors the gap moves from −1.20% to −0.68% across volume terciles and is not monotone in the prior return, so the attention reading does not carry over. Second, the comparison with stocks that closed at their high removes selection on the shape of the close but not on news. The intraday giveback fits readings (2) and (3) at least as well as permanent price discovery, so “break at the limit” is a description and delayed price discovery one hypothesis. Testing the magnet effect (Chen et al., 2024; Cho et al., 2003) needs intraday prices, which we lack.

Table 4 splits the events at 5 May 2025, when HOSE moved to the KRX platform.

Table 4. Next-day abnormal returns (percent) before and after the move to the KRX platform on 5 May 2025, with two-way-clustered *t*-statistics in parentheses. The split uses the date of the opening that defines the gap; the difference *t*-statistic treats the periods as independent.

| **Event** | **Outcome**       | **Before the change** | **After the change** | **Difference** | **Events (before / after)** |
|-----------|-------------------|-----------------------|----------------------|----------------|-----------------------------|
| Ceiling   | Overnight gap     | 1.65 (3.2)            | 2.49 (17.9)          | 0.85 (1.6)     | 936 / 2,263                 |
| Ceiling   | Intraday          | −0.77 (−2.0)          | −0.44 (−4.3)         | 0.34 (0.8)     | 936 / 2,263                 |
| Ceiling   | Close-to-close    | 0.83 (1.0)            | 2.01 (14.6)          | 1.18 (1.3)     | 936 / 2,263                 |
| Ceiling   | Open to day *d*+5 | −0.71 (−1.3)          | −0.77 (−2.5)         | −0.06 (−0.1)   | 936 / 2,257                 |
| Floor     | Overnight gap     | −0.42 (−1.9)          | −1.37 (−7.0)         | −0.95 (−3.2)   | 891 / 1,220                 |
| Floor     | Intraday          | −0.15 (−0.4)          | 0.64 (4.6)           | 0.79 (2.0)     | 891 / 1,220                 |
| Floor     | Close-to-close    | −0.57 (−2.3)          | −0.78 (−5.0)         | −0.21 (−0.7)   | 891 / 1,220                 |
| Floor     | Open to day *d*+5 | −1.73 (−4.7)          | −0.15 (−0.3)         | 1.58 (2.5)     | 891 / 1,217                 |

The ceiling gap, followed by an intraday reversal, appears in both periods (1.65% before and 2.49% after; difference *t* = 1.6). The floor gap is more negative after the move (−0.42% before, −1.37% after; difference *t* = −3.2), the intraday return after floor closes turns positive (0.64%), and the floor drift from the next open to day *d*+5 exists only before the move (−1.73% before, −0.15% after). The change coincides with a different market period, and the post-change sample holds 71% of the ceiling events and 58% of the floor events. Before the change neither the ceiling close-to-close return (*t* = 1.0) nor the floor gap (*t* = −1.9) is significant at the 5% level, so the full-sample significance rests mainly on post-change events. We cannot attribute the differences between the periods to the auction rules.

Returns beyond ±8%, which a 7% band does not allow, occur on 96 stock-days and may reflect unadjusted corporate actions or listing-day bands. Dropping every event within five trading days of such a return moves the ceiling gap from 2.24% to 2.26% and the floor gap from −0.97% to −0.98%; the outlier days stay in the market benchmark.

To bound the effect of a wider search, let $p_{\text{max}}$ be the largest event-test *p*-value computed with the factor $G/(G - 1)$ and a *t* reference. All four event tests survive a Bonferroni correction at 5% in families of up to $m_{\text{max}} = \lfloor 0.05/p_{\text{max}}\rfloor$ tests: 683 with date clusters and 125 with calendar-week clusters ($p_{\text{max}}$ of 0.00007 and 0.00040). The bound limits false discoveries but leaves the upward bias in effect sizes untouched.

The results support H<sub>1</sub> to H<sub>4</sub>. The ceiling effect survives alternative benchmarks, clusters, and event definitions and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture. The floor effect combines a gap with drift that appears only before the 2025 platform change, and its size depends on the benchmark.

# 6. Discussion

Our decomposition adds timing to the evidence of Kim and Rhee (1997): on HOSE the continuation after ceiling closes arrives at the next opening and ends after the first day, and the intraday giveback is a one-day analogue of the cross-period reversal in Lou et al. (2019). A pure attention reading must explain the contrast with stocks that moved almost as far, including those that also closed at their high, and a gap-only reading cannot explain the pre-change post-open drift after floor closes.

No earlier study reports post-limit returns in a form that matches ours, so Table 5 compares signs, timing, and mechanism.

Table 5. Comparison with earlier studies. Findings are as reported in each source’s abstract or in the records we could access.

| **Study**                               | **Setting**              | **Reported finding**                                                                                | **Relation to our result**                                                                                                      |
|-----------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Kim and Rhee (1997)                     | Tokyo; limit hits        | Volatility spillover, delayed price discovery, and trading interference                             | Ceiling next-day return consistent with delayed price discovery; spillover and interference not tested                          |
| Berkman and Lee (2002)                  | Korea; limit revision    | Volatility and trading activity around the revision                                                 | Different question                                                                                                              |
| Huang et al. (2001)                     | Taiwan; limit hits       | Overnight overreaction after limit hits corrected the next day                                      | Same timing: positive gap, partial intraday reversal                                                                            |
| Cho et al. (2003)                       | Taiwan; five-minute data | Prices accelerate toward the upper limit                                                            | Not tested; no intraday prices                                                                                                  |
| Chen et al. (2019)                      | Shenzhen; accounts       | Large investors buy on the limit day and sell the next; their net buying predicts long-run reversal | Consistent with our intraday reversal; no account identities                                                                    |
| Qi (2023)                               | ChiNext; band 10% to 20% | Delayed price discovery, spillover, and interference, stronger at the lower limit; no magnet effect | Different outcome (market quality); here both limit closes carry a next-day return, the floor effect depending on the benchmark |
| Lin et al. (2023); Zeng et al. (2024)   | China; cross-section     | Large limit exposure or frequent upper-limit hits predict lower returns                             | Different horizon; a one-day gain can coexist with later reversal, which we do not measure                                      |
| Berkman et al. (2012)                   | U.S.; intraday data      | Overnight gains, intraday reversals, concentrated in high-attention stocks                          | Same signs; the gap also rises with volume and prior return                                                                     |
| Lou et al. (2019)                       | U.S.; stock returns      | Overnight and intraday continuation, offsetting cross-period reversal                               | Gap-then-reversal has the sign of that cross-period reversal at one day                                                         |
| Qiao and Dam (2020)                     | China A-shares           | Negative average overnight return; T+1 rule lowers opening prices                                   | Opposite sign: positive overnight return after ceiling closes                                                                   |
| Hou et al. (2020); Harvey et al. (2016) | U.S.; anomalies          | 65% of 452 anomalies fail the 1.96 hurdle; a new factor needs *t* above 3.0                         | None of our 22 characteristics reaches 1.96 in the full sample                                                                  |

A 7% band leaves room for a large overnight gap, so the opening auction may do much of the adjustment that a wider band would allow on day *d*. The floor results after at-the-open orders lost priority (Table 4) fit auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time; a band change on HOSE, like the ChiNext widening that Qi (2023) studies, would give a natural experiment.

The volume and prior-return results also fit an attention channel in which the limit amplifies demand: a stock at its ceiling may appear on screens and rankings the next morning, and a queue at the limit may signal excess demand. With noise traders overnight, arbitrageurs by day, and market makers absorbing retail imbalances near the open (Akbas et al., 2022; Lu et al., 2023), a limit would add a visible, rule-based trigger to an attention mechanism that operates without limits.

Ceiling closes cover about 2.0% of stock-days in the event window, and the low-powered characteristic null says little about the cross-section, so we make no claim that limit closes explain the cross-section of returns.

The estimates describe what follows limit closes on HOSE in 2024 to 2026. They cannot show what the limit does to price discovery: the band does not vary, no period lacks a limit, and we measure none of the benefits a limit is meant to deliver. For investors, buying ceiling stocks at the quoted next open lost money against the market by the fifth close, excluding costs and rationing at the open.

# 7. Limitations

1)  The sample covers 519 trading days on one exchange, with one platform change and a period of market stress. (ii) Without order-book, investor-type, announcement, or news data, we infer the unfilled-demand mechanism and cannot separate it from selection on news. (iii) The 7% band, reference price, and platform change come from brokerage and press descriptions, checked against returns but not against exchange circulars; tick sizes, reference prices on corporate-action days, and wider bands for first-day listings and resumed trading are assumptions. (iv) The vendor appears to adjust earlier prices for later corporate actions. For stocks priced at 10 thousand dong or more, 25%, 31%, and 58% of 2024, 2025, and 2026 closes are tick multiples, against 100% below 10 thousand dong (an uninformative check, since the 0.01 tick equals the two-decimal resolution of the files), and near hits make up 62% of ceiling events for the higher-priced stocks against 23% for the others. Proportional adjustment leaves returns (except on ex-dates), the close-at-high rule, and locked days unchanged but makes the exact-hit classification of Equation (3) unreliable, so we treat that split as a data check, not a measure of distance to the limit. The listing snapshot excludes stocks delisted before the download. (v) Events in one market episode may depend on each other beyond our clustering, and we computed no calendar-time portfolio estimates or standard errors robust to both cross-sectional and serial dependence. (vi) Several characteristics (5-day return, MAX, MIN, move frequency, overnight return) share inputs with the event definition, and the Corwin–Schultz spread and range volatility use limit-censored highs and lows. (vii) The floor effect depends on the benchmark, and we built no beta- and size-matched control for the five-day outcome. (viii) The characteristic tests have limited power, and effect sizes may carry winner’s-curse bias from choosing this question among several screened on the same data.

# 8. Conclusion

Of 26 tests on 347 HOSE stocks, the four price-limit tests survive FDR control and the confirmation-half check, and the 22 lower-powered characteristic tests do not. After a ceiling close, the next-day abnormal return of 1.7% is an overnight gap of 2.2% less an intraday reversal of 0.5%. The gap is 2.7 percentage points larger than for stocks that rose 5% to 6.5% and 3.1 points larger than for those among them that also closed at their high. After a floor close, the overnight gap is −1.0%. An outside buyer at the next open loses 0.7% against the market by the fifth close. Delayed price discovery at the limit fits the pattern, but news and attention remain possible explanations; longer samples, announcement time stamps, and order-book queues would let future work separate them.

# Declarations

**Generative AI.** The authors used Claude (Anthropic) to write analysis code, draft text, and check numbers against output files. The authors are responsible for all content. We checked the references and the institutional facts in Section 3 by web search and did not consult primary documents.

**Data and code availability.** Daily price files and code are in the project repository (`trungcandygit/black_litterman_2`, commit 63bdc6d for the analysis plan; R code and output tables in `paper2/`). The data come from the vnstock library (version 4.0.4, source VCI), retrieved on 24 September 2026.

**Funding, competing interests, ethics, and author contributions.** \[To be completed by the authors.\]

# References

Aboody, D., Even-Tov, O., Lehavy, R., & Trueman, B. (2018). Overnight returns and firm-specific investor sentiment. *Journal of Financial and Quantitative Analysis, 53*(2), 485–505.

Akbas, F., Boehmer, E., Jiang, C., & Koch, P. D. (2022). Overnight returns, daytime reversals, and future stock returns. *Journal of Financial Economics, 145*(3), 850–875. <https://doi.org/10.1016/j.jfineco.2021.09.019>

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56. <https://doi.org/10.1016/S1386-4181(01)00024-6>

Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. *Journal of Financial Economics, 99*(2), 427–446. <https://doi.org/10.1016/j.jfineco.2010.08.014>

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300. <https://doi.org/10.1111/j.2517-6161.1995.tb02031.x>

Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). Paying attention: Overnight returns and the hidden cost of buying at the open. *Journal of Financial and Quantitative Analysis, 47*(4), 715–741. <https://doi.org/10.1017/S0022109012000270>

Berkman, H., & Lee, J. B. T. (2002). The effectiveness of price limits in an emerging market: Evidence from the Korean Stock Exchange. *Pacific-Basin Finance Journal, 10*(5), 517–530. <https://doi.org/10.1016/S0927-538X(02)00040-9>

Bildik, R., & Gülay, G. (2006). Are price limits effective? Evidence from the Istanbul Stock Exchange. *Journal of Financial Research, 29*(3), 383–403. <https://doi.org/10.1111/j.1475-6803.2006.00185.x>

Bogousslavsky, V. (2021). The cross-section of intraday and overnight returns. *Journal of Financial Economics, 141*(1), 172–194.

Brennan, M. J. (1986). A theory of price limits in futures markets. *Journal of Financial Economics, 16*(2), 213–233. <https://doi.org/10.1016/0304-405X(86)90061-9>

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2011). Robust inference with multiway clustering. *Journal of Business & Economic Statistics, 29*(2), 238–249. <https://doi.org/10.1198/jbes.2010.07136>

Chen, H., Petukhov, A., Wang, J., & Xing, H. (2024). The dark side of circuit breakers. *The Journal of Finance, 79*(2), 1405–1455. <https://doi.org/10.1111/jofi.13310>

Chen, T., Gao, Z., He, J., Jiang, W., & Xiong, W. (2019). Daily price limits and destructive market behavior. *Journal of Econometrics, 208*(1), 249–264. <https://doi.org/10.1016/j.jeconom.2018.09.014>

Chen, Y.-M. (1993). Price limits and stock market volatility in Taiwan. *Pacific-Basin Finance Journal, 1*(2), 139–153. <https://doi.org/10.1016/0927-538X(93)90005-3>

Cho, D. D., Russell, J., Tiao, G. C., & Tsay, R. S. (2003). The magnet effect of price limits: Evidence from high-frequency data on Taiwan Stock Exchange. *Journal of Empirical Finance, 10*(1–2), 133–168. <https://doi.org/10.1016/S0927-5398(02)00024-5>

Chordia, T., Goyal, A., & Saretto, A. (2020). Anomalies and false rejections. *The Review of Financial Studies, 33*(5), 2134–2179.

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. <https://doi.org/10.1111/j.1540-6261.2012.01729.x>

Deb, S. S., Kalev, P. S., & Marisetty, V. B. (2013). Flexible price limits: The case of Tokyo Stock Exchange. *Journal of International Financial Markets, Institutions and Money, 24*, 66–84.

Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium: Empirical tests. *Journal of Political Economy, 81*(3), 607–636. <https://doi.org/10.1086/260061>

Greenwald, B. C., & Stein, J. C. (1991). Transactional risk, market crashes, and the role of circuit breakers. *Journal of Business, 64*(4), 443–462.

Gu, M., Hu, Y., & Xiong, Z. (2025). Dissecting the lottery-like anomaly: Evidence from China. *Accounting & Finance, 65*(1), 883–911. <https://doi.org/10.1111/acfi.13354>

Gutierrez, R. C., Jr., & Kelley, E. K. (2008). The long-lasting momentum in weekly returns. *The Journal of Finance, 63*(1), 415–447. <https://doi.org/10.1111/j.1540-6261.2008.01320.x>

Harvey, C. R., & Liu, Y. (2020). False (and missed) discoveries in financial economics. *The Journal of Finance, 75*(5), 2503–2553. <https://doi.org/10.1111/jofi.12951>

Harvey, C. R., Liu, Y., & Zhu, H. (2016). …and the cross-section of expected returns. *The Review of Financial Studies, 29*(1), 5–68. <https://doi.org/10.1093/rfs/hhv059>

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.

Hou, K., Xue, C., & Zhang, L. (2020). Replicating anomalies. *The Review of Financial Studies, 33*(5), 2019–2133.

HSC. (2025). *Important changes of new trading system* \[Web page\]. Ho Chi Minh City Securities Corporation. <https://www.hsc.com.vn/en/important-changes-of-new-trading-system>

Huang, X., Liu, C., & Shu, T. (2023). Factors and anomalies in the Vietnamese stock market. *Pacific-Basin Finance Journal, 82*, 102176.

Huang, Y.-S., Fu, T.-W., & Ke, M.-C. (2001). Daily price limits and stock price behavior: Evidence from the Taiwan Stock Exchange. *International Review of Economics & Finance, 10*(3), 263–288.

Jia, S., An, Y., Yang, L., & Zhou, F. (2024). Price limit relaxation and stock price crash risk: Evidence from China. *Finance Research Letters, 59*, 104715. <https://doi.org/10.1016/j.frl.2023.104715>

Jones, C. M., Shi, D., Zhang, X., & Zhang, X. (2025). Retail trading and return predictability in China. *Journal of Financial and Quantitative Analysis, 60*(1), 68–104.

Kelly, M. A., & Clark, S. P. (2011). Returns in trading versus non-trading hours: The difference is day and night. *Journal of Asset Management, 12*, 132–145. <https://doi.org/10.1057/jam.2011.2>

Kim, K. A., & Limpaphayom, P. (2000). Characteristics of stocks that frequently hit price limits: Empirical evidence from Taiwan and Thailand. *Journal of Financial Markets, 3*(3), 315–332.

Kim, K. A., & Rhee, S. G. (1997). Price limit performance: Evidence from the Tokyo Stock Exchange. *The Journal of Finance, 52*(2), 885–901. <https://doi.org/10.1111/j.1540-6261.1997.tb04827.x>

Kim, W., & Jun, S. (2019). Effects of a price limit change on market stability at the intraday horizon in the Korean stock market. *Applied Economics Letters, 26*(7), 582–586.

Kodres, L. E., & O’Brien, D. P. (1994). The existence of Pareto-superior price limits. *American Economic Review, 84*(4), 919–932.

Liang, H., & Hu, Y. (2025). Stock price limit and its predictability in the Chinese stock market. *Journal of Forecasting, 44*, 297–319. <https://doi.org/10.1002/for.3197>

Lien, D., Hung, P.-H., Zhu, J.-D., & Chen, Y.-H. (2019). Price limit changes and market quality in the Taiwan Stock Exchange. *Pacific-Basin Finance Journal, 55*, 239–258.

Lin, F., Qiu, Z., & Zheng, W. (2023). Cranes among chickens: The general-attention-grabbing effect of daily price limits in China’s stock market. *Journal of Banking & Finance, 150*, 106818. <https://doi.org/10.1016/j.jbankfin.2023.106818>

Lou, D., Polk, C., & Skouras, S. (2019). A tug of war: Overnight versus intraday expected returns. *Journal of Financial Economics, 134*(1), 192–213. <https://doi.org/10.1016/j.jfineco.2019.03.011>

Lu, Z., Malliaris, S. G., & Qin, Z. (2023). Heterogeneous liquidity providers and night-minus-day return predictability. *Journal of Financial Economics, 148*(3), 175–200.

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica, 55*(3), 703–708. <https://doi.org/10.2307/1913610>

Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. *The Journal of Business, 53*(1), 61–65. <https://doi.org/10.1086/296071>

Petersen, M. A. (2009). Estimating standard errors in finance panel data sets: Comparing approaches. *The Review of Financial Studies, 22*(1), 435–480.

Qi, B. (2023). Effectiveness of price limits: Evidence from China’s ChiNext market. *PLOS ONE, 18*(6), e0287548. <https://doi.org/10.1371/journal.pone.0287548>

Qiao, K., & Dam, L. (2020). The overnight return puzzle and the “T+1” trading rule in Chinese stock markets. *Journal of Financial Markets, 50*, 100534.

Qiu, J., Huang, W., & Jiang, Y. (2025). Day-night anomaly returns in China: The role of institutions. *Research in International Business and Finance, 75*, 102776.

Subrahmanyam, A. (1994). Circuit breakers and market volatility: A theoretical perspective. *The Journal of Finance, 49*(1), 237–254. <https://doi.org/10.1111/j.1540-6261.1994.tb04427.x>

Viet Nam News. (2025). *KRX system officially goes live* \[News article\]. <https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html>

Zeng, Z., Wang, G., & Tang, G. (2024). Price limits hitting effect and cross-sectional stock returns: Evidence from China. *Finance Research Letters, 60*, 104803. <https://doi.org/10.1016/j.frl.2023.104803>

Zhang, X., Wang, Z., Hao, J., & He, F. (2022). Price limit and stock market quality: Evidence from a quasi-natural experiment in the Chinese stock market. *Pacific-Basin Finance Journal, 74*, 101778.

# Appendix A. Characteristic definitions

All characteristics use data up to each week’s formation day. REV1W and REV1M are the compounded returns over the last 5 and 20 trading days, and MOM3M and MOM6M over 60 and 110 trading days ending five days before formation. IMOM compounds the return in excess of the dollar-volume-weighted market over the MOM3M window. Over the last 60 days, VOL is the standard deviation of daily returns; BETA and IVOL are the slope and residual standard deviation of a regression of those returns on the dollar-volume-weighted return of that week’s cross-section; DOWNVOL is the square root of the mean of $\min(r,0)^{2}$; RANGEVOL is the Parkinson (1980) high-low estimator; SKEW and KURT are the third and fourth standardized moments; AMIHUD is the mean ratio of absolute return to dollar volume (Amihud, 2002); LNDVOL is the log of mean dollar volume; and CSSPREAD is the Corwin and Schultz (2012) spread estimator. Over the last 20 days, MAX and MIN are the largest and smallest daily returns (Bali et al., 2011), OVERNIGHT and INTRADAY the mean open-over-previous-close and close-over-open returns, and LIMITFREQ the share of days with an absolute return of 6.5% or more. DVOLCHG and TURNCHG are the ratios of 20-day to 60-day mean dollar volume and share volume. The quintile spread is the equal-weighted abnormal return of the top minus the bottom quintile over the next five days; the net spread subtracts $2 \times 0.0025 \times \left( {TO}_{L} + {TO}_{S} \right)$, where ${TO}_{L}$ and ${TO}_{S}$ are the shares of the long and short legs replaced since the previous week.
