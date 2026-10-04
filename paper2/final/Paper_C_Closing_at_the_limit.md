**Abstract.** Daily price limits aim to cool markets but can delay price discovery. Evidence on prices after limit closes in emerging markets is thin, and published limit studies do not account for the many price-based signals a researcher could have examined. We study 347 stocks on the Ho Chi Minh Stock Exchange (HOSE) from August 2024 to September 2026 and test 26 hypotheses under false-discovery-rate control: four price-limit event tests and 22 price- and volume-based characteristics. None of the 22 characteristics survives, although the tests have limited power, while all four limit tests do. A ceiling close is followed by a next-day abnormal return of 1.7%, an overnight gap of 2.2% less an intraday reversal of 0.5%, and the gap exceeds that of stocks that rose almost as far without reaching the limit. A buyer at the next open earns nothing from it. The pattern fits delayed price discovery, but news and attention explain it as well, and our data cannot separate the two.

**Keywords:** price limits; overnight returns; multiple testing; market microstructure; Vietnam

**JEL classification:** G14; G15; G18

# 1. Introduction

A daily price limit stops a stock from moving beyond a fixed band within one trading day. Brennan (1986) gives a rationale for limits in futures markets, and Subrahmanyam (1994) shows that trading halts can advance trades in time and raise price variability. In equity markets, advocates argue that limits reduce volatility and counter overreaction, while critics argue that they delay price discovery, spill volatility into later days, and interfere with trading (Kim & Rhee, 1997). Kim and Rhee find support for all three criticisms in Tokyo, and Bildik and Gülay (2006) find the same in Istanbul. Chen (1993) shows that serial correlation falls as the Taiwanese limit widens, Berkman and Lee (2002) report more continuations after limit hits in Korea, and Cho et al. (2003) document a magnet effect toward the upper limit in Taiwanese intraday data. Qi (2023) studies the widening of the ChiNext band in China from 10% to 20% and finds delayed price discovery, volatility spillover and trading interference, with no magnet effect. Evidence on Vietnam is sparse. Le (2012) studies a narrowing of the fluctuation limit with GARCH models, and Veeraraghavan et al. (2007, a working paper) study momentum and price limits for 2000 to 2006.

To our knowledge, none of these studies separates the next-day return after a limit close into the overnight gap and the trading session that follows, and none places the limit result in a family of tests that controls for the many other price-based signals a researcher could have examined. The gap shows what the opening auction does with demand that the limit blocked. The session shows whether an investor who did not already hold the stock can earn anything from it. The family of tests asks whether a long search could have produced a large effect by luck.

HOSE offers a useful setting for this question. It applies one daily band to every stock, sets opening and closing prices in call auctions, and produces many limit closes: about 2.0% of stock-days in our event window close at the ceiling and about 1.4% at the floor. The frequency gives enough events to estimate the next-day return with tight confidence intervals and to split the sample in several ways.

We estimate the abnormal return after closes at the upper limit (ceiling) and the lower limit (floor) on the Ho Chi Minh Stock Exchange (HOSE), measure how much of it arises in the overnight gap, and test whether an outside buyer can capture it. To discipline the search, we place four limit tests in one family of 26 tests with 22 familiar price- and volume-based characteristics and control the false-discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).

We make three contributions. First, we decompose the next-day abnormal return after limit closes into an overnight gap and an intraday return, and show that the ceiling effect is a gap followed by a partial reversal. Second, we compare limit closes with stocks that moved almost as far without reaching the limit, including stocks that also closed at their daily high, and find that the gap is larger at the limit. Third, we show that the limit effect survives a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open cannot capture it. Berkman et al. (2012) find the same overnight-gain-then-intraday-reversal signature in U.S. stocks, which have no price limit, so the pattern alone does not identify a limit effect.

Section 2 describes the setting and data, Section 3 the design, and Section 4 the results and rival readings. Section 5 discusses the findings, Section 6 lists limitations, and Section 7 concludes.

# 2. Institutional setting and data

HOSE sets a daily price limit of 7% around the reference price, which is the previous close on normal trading days, and allows a wider band on the first trading day of a new listing (HSC, 2025). On 5 May 2025 HOSE moved to the trading platform of the Korea Exchange (KRX). The band stayed unchanged, but at-the-open and at-the-close orders lost their priority over limit orders in the call auctions that set the opening and closing prices (HSC, 2025; Viet Nam News, 2025). The close defines the event and the open defines the gap, so both prices matter here. We treat the 7% band, the tick sizes and the reference-price rule as assumptions and check the band against the data: 1.98% of stock-days fall between +6.5% and +7.1% and 1.30% between −7.1% and −6.5%, against 0.29% between +6.0% and +6.5%, A 7% band implies this pile-up.

The raw data are daily open, high, low, close, and volume for 405 HOSE-listed stocks from 21 August 2024 to 23 September 2026, retrieved with the vnstock library. We take the stock list from a listing file dated 24 September 2026, so stocks delisted earlier are absent. We keep the 347 stocks with at least 95% non-missing closes, which yields 178,773 stock-days. Returns are close-to-close. The market return is the dollar-volume-weighted return of all stocks, with weights from the trailing 60-day average dollar volume, and abnormal returns are stock returns minus the market return over the same interval. The vendor does not document corporate-action adjustment. The data contain no order books, investor types, news or market capitalization.

# 3. Design

A ceiling event is an event day *d* with a return of at least +6.5% and a close equal to the day’s high. A floor event is a day with a return of at most −6.5% and a close equal to the day’s low. We measure the market-adjusted return on day *d*+1 and over days *d*+1 to *d*+5. We split the day-*d*+1 return into the overnight gap (open on *d*+1 over close on *d*) and the intraday return (close over open on *d*+1). Standard errors cluster by event date. We also report clustering by calendar week and by 10-day block, which allows for overlapping five-day windows, and two-way clustering by date and stock.

An exact limit hit is a close equal to the reference price times 1.07 (0.93 for floors), rounded to the tick, with ticks of 0.01, 0.05 and 0.10 thousand dong for prices below 10, below 50 and from 50 thousand dong. We call closes that meet the event rule but not the exact rule near hits.

The family has 26 tests. Twenty-two are weekly Fama and MacBeth (1973) regressions of the next five days’ abnormal return on one rank-normalized characteristic, with Newey and West (1987) *t*-statistics using four lags. The characteristics cover momentum and reversal (5-day, 20-day, 3-month, 6-month, and idiosyncratic momentum), risk (volatility, idiosyncratic volatility, beta, downside deviation, Parkinson (1980) range volatility, the maximum daily return (MAX; Bali et al., 2011), the minimum daily return (MIN), skewness and kurtosis), liquidity and volume (Amihud, 2002, illiquidity, log dollar volume, dollar-volume and volume ratios, and the Corwin and Schultz, 2012, spread) and intraday behavior (mean overnight return, mean intraday return, frequency of moves of 6.5% or more). The sample has 79 weekly cross-sections. The remaining four tests are the ceiling and floor tests at the two horizons.

We adjust the 26 *p*-values by the Benjamini–Hochberg (BH) procedure at a 5% FDR and by Holm (1979), and report the hurdle of \|*t*\| = 3 of Harvey et al. (2016). A test survives if its BH-adjusted *p*-value is below 5%, its discovery-half sign agrees with the full sample, and its confirmation-half \|*t*\| exceeds 1.96. The first 39 weeks form the discovery half. Lookbacks of up to 115 days overlap the discovery half, so the confirmation half is not a strict hold-out.

The tests address four hypotheses. First, if a limit delays price discovery, a ceiling close should predict a positive next-day abnormal return and a floor close a negative one. Second, if the opening auction absorbs the blocked demand, the effect should concentrate in the overnight gap. Third, the gap after a limit close should exceed the gap after moves that come close to the limit, because only the limit blocks trading. Fourth, an investor who buys at the next open should not earn the gap. The 22 characteristics give a benchmark for the first hypothesis: a limit effect that survives the same procedure that rejects every characteristic is more credible than a single large estimate.

We fixed the family, estimators, multiplicity control and survival rule in a written analysis plan before computing results. A version-control time stamp predates the first analysis code, but no external registry holds the plan, and we had examined related data in earlier work, so the plan gives no independent confirmation. We departed from the plan in four ways. The plan names the event horizons as days *d*+1 and *d*+2 to *d*+5 in one place and as *d*+1 and *d*+1 to *d*+5 in its count of tests, and we implemented the second reading. We split the event half-samples at the median event date instead of at weeks 39 and 40. We report quintile spreads instead of deciles. We did not run the plan’s same-stock control and multivariate model. Analyses added after the first results are exploratory: the decomposition, the next-open returns, the control group, the comparison with sub-limit moves, exact hits, two-way clustering, subsamples, the volume and prior-return terciles, the platform-change split, and the outlier exclusion. The authors also screened several candidate ideas on the same data before choosing this one, so effect-size estimates may overstate the true effect.

# 4. Results

The event sample holds 3,187 ceiling events on 446 dates and 2,105 floor events on 319 dates, so events cluster in market episodes with several limit closes on the same day. This clustering is why we report standard errors that allow for dependence across dates, weeks and stocks. We first report the null for the 22 characteristics and then the four limit tests. Three exploratory analyses follow: where in the trading day the limit effect arises, whether it breaks at the limit, and whether it survives the 2025 platform change.

None of the 22 characteristics reaches \|*t*\| = 3, and none survives the family-wide control (Figure 1). The largest full-sample \|*t*\| is 1.45, for 3-month and idiosyncratic momentum (confirmation-half *t* of 1.17 and 1.14). Volatility has *t* = −0.09, idiosyncratic volatility −0.54 and MAX −0.02. After a cost of 25 basis points per unit of traded value, 18 of the 22 long–short quintile spreads are negative. Power is limited: with 79 cross-sections the minimum detectable slope at 80% power is 0.12 to 0.31 percentage points per week per standard deviation, and no characteristic reaches \|*t*\| = 3 with eight Newey–West lags (largest \|*t*\| 1.79). The null excludes only large effects. Three features of this market can produce it. The sample is short, so a premium of a tenth of a percentage point per week stays invisible. Daily limits censor the highs and lows that several characteristics use, which weakens range-based measures. Slow-moving signals such as momentum and volatility may also carry little information in a market where short selling is costly and arbitrage capital is thin. Our data cannot tell these explanations apart, and we draw no conclusion about market efficiency from the null.

<img src="media/rId23.png" style="width:6.29167in;height:4.45256in" alt="Figure 1. t-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half and the confirmation half. Dashed lines mark |t| = 1.96 and dotted lines mark |t| = 3. Characteristics are ordered by absolute full-sample t." />

Figure 1. *t*-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half and the confirmation half. Dashed lines mark \|*t*\| = 1.96 and dotted lines mark \|*t*\| = 3. Characteristics are ordered by absolute full-sample *t*.

Table 1 reports the event tests. A ceiling close is followed by a market-adjusted return of 1.66% on day *d*+1 and 1.45% over days *d*+1 to *d*+5. A floor close is followed by −0.71% and −1.76%. All four tests survive the BH control (adjusted *p*-values from 2.6e-06 to 4.0e-04). They keep their signs in both halves, and the confirmation-half \|*t*\| exceeds 1.96. Clustering by calendar week or 10-day block, with a *t* reference distribution, leaves all four significant. The floor five-day test clears the confirmation criterion by the smallest margin (*t* = −2.22 with week clusters), and all four tests survive the rule re-applied with week-clustered statistics.

For ceilings, the five-day result comes from the first day. Over days *d*+2 to *d*+5 the ceiling return is −0.24% (*t* = −1.53). After floor closes, days *d*+2 to *d*+5 add −1.10% (*t* = −2.91), but the confirmation-half week-clustered *t* is −1.14. If we read the planned horizon as days *d*+2 to *d*+5, the ceiling test would fail and the floor test would fail the confirmation criterion. The evidence shows a one-day effect after ceiling closes and a one-day effect with some later drift after floor closes. These tests establish that limit closes carry information about the next day that none of the 22 characteristics carries. They leave open when in the day that information arrives, which the next analysis addresses.

Table 1. Market-adjusted returns after ceiling and floor closes. Mean returns are in percent. *t* (date), *t* (week) and *t* (10-day) use clusters by event date, calendar week and 10-day block; the week and 10-day statistics use a *t* reference distribution and a G/(G − 1) correction, where G is the number of clusters. *t* (halves) gives week-clustered statistics for the first and second half of event dates. Events require complete returns for days *d*+1 to *d*+5.

| **Event** | **Horizon**    | **Mean (%)** | ***t* (date)** | ***t* (week)** | ***t* (10-day)** | ***t* (halves)** | **Events** |
|-----------|----------------|--------------|----------------|----------------|------------------|------------------|------------|
| Ceiling   | *d*+1          | 1.66         | 4.90           | 4.67           | 4.61             | 2.2 / 13.7       | 3,187      |
| Ceiling   | *d*+1 to *d*+5 | 1.45         | 4.00           | 3.67           | 3.81             | 1.7 / 5.0        | 3,187      |
| Ceiling   | *d*+2 to *d*+5 | −0.24        | −1.53          | −1.11          | −1.25            | −1.1 / −0.4      | 3,187      |
| Floor     | *d*+1          | −0.71        | −5.32          | −4.66          | −6.25            | −2.7 / −4.6      | 2,105      |
| Floor     | *d*+1 to *d*+5 | −1.76        | −4.74          | −4.80          | −4.92            | −12.3 / −2.2     | 2,105      |
| Floor     | *d*+2 to *d*+5 | −1.10        | −2.91          | −3.01          | −2.81            | −8.7 / −1.1      | 2,105      |

Table 2 decomposes the next-day return. After a ceiling close the overnight gap is 2.24% (two-way-clustered *t* = 9.7), and the intraday return is −0.54% (*t* = −3.5). The close-to-close effect is positive because the gap exceeds the giveback, and the session reverses about 24% of the gap. The decomposition places the effect in the opening auction. A stock that closes at its ceiling carries a queue of unfilled buy orders into the night. Those orders and any overnight news set the opening price, and the session that follows undoes part of the move, which suggests that part of the opening price reflects demand that does not persist. After a floor close the gap is −0.97% (*t* = −4.6) and the intraday return is a weak reversal of 0.30%. The pattern holds for exact limit hits, where the ceiling gap is 2.77%, and for the first day of a streak of exact hits, where it is 2.37%. Near hits show a smaller gap (1.67%) and no significant intraday return, so the effect grows as the close approaches the limit. It appears in both halves of the sample, in each liquidity tercile for ceilings (the gap is 1.52% in the most liquid tercile), and on days when the stock stayed locked at one price from open to close. Against same-date control stocks of similar liquidity the ceiling gap is 2.70% and the floor close-to-close return is −1.65%, so the floor effect depends on the benchmark. Floor events cluster on market-wide down days (only 740 of 2,111 remain when we drop days on which the market fell more than 2%), and the floor gap is not significant in the least liquid tercile (*t* = −1.0).

The close-to-close continuation is not available to an outside buyer. A buyer who wants a stock at its ceiling joins a queue at the close, so the first price available to an outside buyer is the next open, which already contains the gap. From that open the ceiling return is −0.75% through the fifth close against the market (*t* = −2.7) and −0.53% against same-date controls (*t* = −1.8). A holder who sells at the next open instead of the close avoids an average giveback of 0.54 percentage points. These figures use quoted prices and ignore achievable fills: 522 ceiling events were locked at one price all day, and some of those open again at the limit, where a buyer may be rationed. After floor closes, prices keep falling from the next open to the fifth close (Table 2).

Table 2. Next-day abnormal returns by component and sample. Entries are mean abnormal returns in percent with two-way-clustered *t*-statistics in parentheses. Benchmarks are the dollar-volume-weighted market (weights lagged to day *d*) or same-date non-event stocks in the same liquidity tercile. Open to day 5 is the return from the day-*d*+1 open to the day-*d*+5 close. Exact hits and near hits are defined in Section 3. Close-to-close need not equal the sum of the two components because returns compound. Events are the stock-days with the relevant return.

| **Sample**                        | **Events** | **Overnight gap** | **Intraday** | **Close-to-close** | **Open to day 5** |
|-----------------------------------|------------|-------------------|--------------|--------------------|-------------------|
| Ceiling closes                    |            |                   |              |                    |                   |
| All, vs market                    | 3,199      | 2.24 (9.7)        | −0.54 (−3.5) | 1.66 (4.8)         | −0.75 (−2.7)      |
| All, vs same-date controls        | 3,100      | 2.70 (20.2)       | −0.50 (−6.0) | 2.16 (18.0)        | −0.53 (−1.8)      |
| Exact limit hit                   | 1,648      | 2.77 (13.5)       | −0.73 (−5.3) | 1.98 (7.0)         | −1.01 (−3.0)      |
| Near hit                          | 1,557      | 1.67 (6.4)        | −0.32 (−1.6) | 1.31 (3.1)         | −0.46 (−1.3)      |
| Locked all day                    | 522        | 2.91 (3.0)        | −1.30 (−5.9) | 1.54 (1.4)         | −0.76 (−1.5)      |
| First half of sample              | 1,615      | 2.24 (5.4)        | −0.77 (−3.3) | 1.42 (2.3)         | −1.13 (−2.9)      |
| Second half of sample             | 1,584      | 2.25 (13.0)       | −0.29 (−2.5) | 1.91 (11.3)        | −0.36 (−1.2)      |
| Excluding days with market \< −2% | 3,125      | 2.24 (9.6)        | −0.53 (−3.4) | 1.67 (4.7)         | −0.70 (−2.6)      |
| Floor closes                      |            |                   |              |                    |                   |
| All, vs market                    | 2,111      | −0.97 (−4.6)      | 0.30 (1.4)   | −0.69 (−4.8)       | −0.82 (−1.7)      |
| All, vs same-date controls        | 2,047      | −1.75 (−4.0)      | 0.14 (0.6)   | −1.65 (−3.4)       | −0.36 (−0.6)      |
| Exact limit hit                   | 1,028      | −1.29 (−5.0)      | 0.41 (1.7)   | −0.92 (−5.7)       | −0.96 (−1.8)      |
| Near hit                          | 1,086      | −0.66 (−3.7)      | 0.20 (0.9)   | −0.47 (−2.9)       | −0.66 (−1.4)      |
| Locked all day                    | 260        | −2.50 (−4.8)      | 1.11 (2.4)   | −1.44 (−3.4)       | −3.91 (−3.0)      |
| First half of sample              | 1,059      | −0.55 (−2.4)      | −0.09 (−0.3) | −0.63 (−2.9)       | −1.69 (−5.1)      |
| Second half of sample             | 1,052      | −1.40 (−6.5)      | 0.70 (4.9)   | −0.75 (−4.3)       | 0.07 (0.1)        |
| Excluding days with market \< −2% | 740        | −1.83 (−8.7)      | 0.90 (5.3)   | −0.99 (−4.5)       | −0.81 (−1.7)      |

Figure 2 plots the three next-day measures against the size of the day-*d* move. Inside the band the close-to-close relation is negative: larger rises are followed by lower returns, a short-term reversal. At the limit the relation breaks: the overnight gap jumps up at the ceiling and down at the floor.

<img src="media/rId26.png" style="width:6.29167in;height:2.71026in" alt="Figure 2. Next-day abnormal return by the size of the day-d move, split into overnight gap, intraday return and close-to-close return. Circles are interior bins, triangles are closes at the 7% limit and squares are moves beyond 6.5% that did not close at the limit. Bars show 95% confidence intervals clustered by date." />

Figure 2. Next-day abnormal return by the size of the day-*d* move, split into overnight gap, intraday return and close-to-close return. Circles are interior bins, triangles are closes at the 7% limit and squares are moves beyond 6.5% that did not close at the limit. Bars show 95% confidence intervals clustered by date.

Table 3 quantifies the break. Ceiling closers have a gap 2.66 percentage points larger than stocks that rose 5% to 6.5% (*t* = 14.0) and an intraday return 0.31 points lower. Floor closers have a gap 1.59 points lower than stocks that fell 5% to 6.5% (*t* = −9.7). The event rule requires a close at the day’s high, so we repeat the comparison with stocks that also closed at their high (low). The ceiling gap is then 3.14 points larger (*t* = 14.5) and the floor gap 1.81 points lower, so a strong close does not explain the contrast. The comparison is an association around a rule-based threshold. It makes no regression-discontinuity claim, because it has no bandwidth choice, manipulation test or covariate balance, and stocks that reach the limit may differ in news content.

Table 3. Differences in next-day abnormal returns between limit closes and stocks that moved 3–5% or 5–6.5% in the same direction without closing at the limit. Entries are differences in percentage points with date-clustered *t*-statistics in parentheses. Returns are market-adjusted with lagged weights.

| **Contrast**                        | **Overnight gap** | **Intraday** | **Close-to-close** | **Open to day 5** | **Comparison stock-days** |
|-------------------------------------|-------------------|--------------|--------------------|-------------------|---------------------------|
| Ceiling vs 5–6.5% rises             | 2.66 (14.0)       | −0.31 (−2.1) | 2.32 (7.6)         | −0.02 (−0.1)      | 1,751                     |
| same, comparison closes at its high | 3.14 (14.5)       | −0.66 (−3.4) | 2.47 (7.2)         | −0.49 (−1.5)      | 679                       |
| Ceiling vs 3–5% rises               | 2.40 (11.6)       | −0.32 (−2.2) | 2.05 (6.1)         | −0.45 (−2.2)      | 5,932                     |
| same, comparison closes at its high | 2.81 (13.1)       | −0.61 (−3.8) | 2.17 (6.4)         | −0.64 (−2.7)      | 1,795                     |
| Floor vs 5–6.5% falls               | −1.59 (−9.7)      | −0.07 (−0.3) | −1.66 (−11.6)      | −1.01 (−2.6)      | 1,522                     |
| same, comparison closes at its low  | −1.81 (−8.7)      | −0.13 (−0.6) | −1.95 (−10.7)      | −1.23 (−2.8)      | 722                       |
| Floor vs 3–5% falls                 | −1.14 (−6.4)      | 0.14 (0.6)   | −1.01 (−7.5)       | −0.90 (−2.2)      | 5,237                     |
| same, comparison closes at its low  | −1.35 (−7.4)      | 0.18 (0.8)   | −1.19 (−8.0)       | −1.06 (−2.5)      | 2,228                     |

Three readings fit the pattern, and our data do not separate them. (1) Demand or supply that the limit blocked on day *d* clears at the next opening, the delayed price discovery of Kim and Rhee (1997). (2) Stocks that reach a limit are selected on news and retail attention, which persist overnight and are followed by the overnight-gain-then-reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit. (3) The opening call auction overshoots and corrects part of the move within the day. The sample has no announcement data, order book or stock-days without a limit, so we run two partial checks. First, the ceiling gap rises with day-*d* volume relative to the prior 60-day mean (1.97%, 2.16% and 2.63% across terciles) and with the prior 20-day return of the stock (1.41%, 2.18% and 3.16%). The gap is larger where attention and news are likely stronger, which fits reading (2) as well as reading (1), and it stays positive and significant in the lowest tercile of each proxy (*t* = 4.8 and 4.2). For floors the gap moves from −1.20% to −0.68% across volume terciles and is not monotone in the prior return, so the attention reading does not carry over. Second, the comparison with stocks that closed at their high removes selection on the shape of the close but not selection on news. The intraday giveback fits readings (2) and (3) at least as well as a permanent price-discovery story. Comparisons with 3% to 5% moves give the same result: the ceiling gap exceeds that of 3% to 5% risers by 2.40 percentage points and the floor gap falls short of that of 3% to 5% fallers by 1.14 points (Table 3). We use “break at the limit” as a description and treat delayed price discovery as one hypothesis.

Table 4 splits the events at the move to the KRX platform.

Table 4. Next-day abnormal returns before and after the move to the KRX platform on 5 May 2025. Entries are mean abnormal returns in percent with two-way-clustered *t*-statistics in parentheses. The split uses the date of the opening that defines the gap, and the difference *t*-statistic treats the two periods as independent.

| **Event** | **Outcome**    | **Before the change** | **After the change** | **Difference** | **Events (before / after)** |
|-----------|----------------|-----------------------|----------------------|----------------|-----------------------------|
| Ceiling   | Overnight gap  | 1.65 (3.2)            | 2.49 (17.9)          | 0.85 (1.6)     | 936 / 2,263                 |
| Ceiling   | Intraday       | −0.77 (−2.0)          | −0.44 (−4.3)         | 0.34 (0.8)     | 936 / 2,263                 |
| Ceiling   | Close-to-close | 0.83 (1.0)            | 2.01 (14.6)          | 1.18 (1.3)     | 936 / 2,263                 |
| Ceiling   | Open to day 5  | −0.71 (−1.3)          | −0.77 (−2.5)         | −0.06 (−0.1)   | 936 / 2,257                 |
| Floor     | Overnight gap  | −0.42 (−1.9)          | −1.37 (−7.0)         | −0.95 (−3.2)   | 891 / 1,220                 |
| Floor     | Intraday       | −0.15 (−0.4)          | 0.64 (4.6)           | 0.79 (2.0)     | 891 / 1,220                 |
| Floor     | Close-to-close | −0.57 (−2.3)          | −0.78 (−5.0)         | −0.21 (−0.7)   | 891 / 1,220                 |
| Floor     | Open to day 5  | −1.73 (−4.7)          | −0.15 (−0.3)         | 1.58 (2.5)     | 891 / 1,217                 |

The ceiling gap appears in both periods (1.65% before, 2.49% after the move to KRX; difference *t* = 1.6; Table 4). The floor gap is larger after the move (−0.42% before, −1.37% after; difference *t* = −3.2), and the intraday return after floor closes turns positive (0.64%). The drift from the next open to day 5 after floor closes exists only before the move (−1.73% before, −0.15% after). The change coincides with a different market period, and the post-change sample holds 71% of the ceiling events and 58% of the floor events. The split shows the main pattern on both sides, with differences in detail, and cannot isolate an effect of the auction rules.

Returns beyond ±8%, which a 7% band does not allow, occur on 96 stock-days and may reflect unadjusted corporate actions or listing-day bands. Dropping every event within five trading days of such a return changes the ceiling gap from 2.24% to 2.26% and the floor gap from −0.97% to −0.98%. The exclusion removes events but leaves the outlier days in the market benchmark.

To bound the effect of a larger project-wide search, we compute how many tests the four event tests could absorb. They survive a Bonferroni correction at 5% for families of up to 683 tests with date clusters and up to 125 tests with calendar-week clusters (largest *p*-values 7.3e-05 and 4.0e-04, *t* reference). The bound limits false discoveries and leaves the upward bias in effect sizes untouched.

Taken together, the results give a consistent but bounded picture. The limit effect is large in each of the measures we use, it survives alternative benchmarks, clusters and definitions, and it grows as the close approaches the limit. It differs between ceilings and floors in the details: the ceiling effect is a one-day gap with a partial reversal, and the floor effect combines a gap with drift that appears only before the 2025 platform change. The effect is not available to an outside buyer at the quoted next open. What the evidence does not settle is why the gap arises, and Section 5 returns to that question.

# 5. Discussion

The evidence is consistent with delayed price discovery. The continuation after a ceiling close sits in the opening. Days *d*+2 to *d*+5 add no significant return, and the *d*+1 session reverses part of it. Lou et al. (2019) show that overnight and intraday returns have different persistence and that heterogeneous traders can explain the difference. The contrast with stocks that moved almost as far, including those that also closed at their high, is the part of the evidence that a pure attention reading must explain. The post-open drift after floor closes, which exists only before the platform change, does not fit a gap-only reading.

Earlier evidence from Asian markets gives context. Kim and Rhee (1997) read return continuation after limit hits as delayed price discovery, and Berkman and Lee (2002) report more continuation after limit hits in Korea. Our decomposition adds timing: on HOSE the continuation arrives at the next opening and mostly stops there, which differs from a multi-day adjustment. We do not test the magnet effect that Cho et al. (2003) document, because our data lack intraday prices. The close-to-close pattern after ceilings in our sample resembles the continuation in those studies, and the gap-then-reversal shape links it to the overnight-return literature.

The findings bear on two design choices, the width of the band and the priority of auction orders. A 7% band leaves room for a large overnight gap, so the opening auction does much of the adjustment that a wider band would allow on day *d*. The floor gap grows and the intraday return after floor closes turns positive after ATO orders lose priority (Table 4), which suggests that auction design shapes how overnight pressure resolves. The split cannot identify the rule change, because the market period changed with it. The widening of the ChiNext band studied by Qi (2023) shows how a band change can serve as a natural experiment, and a similar change on HOSE would test the readings directly.

The volume and prior-return results point to an attention channel. If attention drives the gap, the limit acts as an amplifier: a stock at its ceiling appears on screens and rankings the next morning, and a queue at the limit signals excess demand to every investor. Berkman et al. (2012) trace the overnight returns of U.S. stocks to such attention, and Lou et al. (2019) trace the split between overnight and intraday returns to heterogeneous traders. A limit then adds a visible, rule-based trigger to a mechanism that already exists without limits. Under this reading the limit does not delay information so much as create the attention event.

We use the 22 characteristics to set the multiplicity burden and as a null benchmark: the procedure that lets the limit tests survive leaves no characteristic significant. The null says little about the cross-section because power is low (Section 4). Limit hits are rare: about 2.0% of stock-days in the event window close at the ceiling, and we do not claim that limit hits explain the cross-section of returns.

The estimates describe what follows limit closes on HOSE in 2024 to 2026: the next opening carries about two percentage points after ceiling closes and about one after floor closes. They cannot show what the limit does to price discovery: the band does not vary, no period lacks a limit, and we measure none of the benefits a limit is meant to deliver. Announcement time stamps, order-book queue sizes at the close, and a market or period without a limit would test the readings. For investors, the figures suggest that buying limit-up stocks at the quoted open returned −0.75% by the fifth close. The figures omit costs and rationing at the open, so they offer no trading advice.

# 6. Limitations

1)  The sample covers about 25 months on one exchange, with one trading-platform change and a period of market stress. (ii) We have no order-book, investor-type, announcement or news data, so the unfilled-demand mechanism is inferred and selection on news is not separated from it. (iii) The 7% band, the reference price and the platform change come from brokerage and press descriptions and we check only against the return distribution, with no exchange circulars. Tick sizes, reference-price treatment on corporate-action days, and wider bands for first-day listings and resumed trading are assumptions. (iv) Prices may be adjusted for corporate actions in ways that affect event classification, and the listing snapshot excludes earlier delistings. (v) Clustered standard errors allow dependence across dates, weeks, blocks, and stocks, but events in the same market episode may depend on each other more, and we did not compute calendar-time portfolio or Driscoll–Kraay estimates. (vi) Several characteristics (5-day return, MAX, MIN, move frequency, overnight return) share inputs with the event definition, and the Corwin–Schultz spread and range volatility use high and low prices that limits censor. (vii) The floor effect depends on the benchmark, and we built no beta- and size-matched control for the five-day outcome. (viii) The characteristic tests have limited power, and the effect sizes carry winner’s-curse bias because the authors chose the idea among several.

# 7. Conclusion

Of 26 tests on 347 HOSE stocks, the four price-limit tests survive FDR control and a confirmation half, and the 22 characteristic tests do not, although the latter have limited power. A ceiling close is followed by a next-day abnormal return of about 1.7%, which is an overnight gap of 2.2% less an intraday reversal of 0.5%. The gap is 2.7 percentage points larger than for stocks that rose 5% to 6.5% and 3.1 points larger than for those that also closed at their high. The pattern is consistent with delayed price discovery at the limit, but news and attention remain possible. An outside buyer at the next open earns −0.75% by the fifth close. Longer samples, announcement data and order-book data would let future work separate the readings.

# Declarations

**Generative AI.** The authors used Claude (Anthropic) to write analysis code, draft text and check numbers against output files. The authors are responsible for all content. We checked the references and the institutional facts in Section 2 by web search and did not consult primary documents.

**Data and code availability.** Daily price files and code are in the project repository (`trungcandygit/black_litterman_2`, commit 63bdc6d for the analysis plan; R scripts `paper2/R/40` to `49`, tables in `paper2/output/tables`). The data come from the vnstock library; we did not record the library version or retrieval dates.

**Funding, competing interests, ethics and author contributions.** \[To be completed by the authors.\]

# References

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56. <https://doi.org/10.1016/S1386-4181(01)00024-6>

Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. *Journal of Financial Economics, 99*(2), 427–446. <https://doi.org/10.1016/j.jfineco.2010.08.014>

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300. <https://doi.org/10.1111/j.2517-6161.1995.tb02031.x>

Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). Paying attention: Overnight returns and the hidden cost of buying at the open. *Journal of Financial and Quantitative Analysis, 47*(4), 715–741. <https://doi.org/10.1017/S0022109012000270>

Berkman, H., & Lee, J. B. T. (2002). The effectiveness of price limits in an emerging market: Evidence from the Korean Stock Exchange. *Pacific-Basin Finance Journal, 10*(5), 517–530. <https://doi.org/10.1016/S0927-538X(02)00040-9>

Bildik, R., & Gülay, G. (2006). Are price limits effective? Evidence from the Istanbul Stock Exchange. *Journal of Financial Research, 29*(3), 383–403. <https://doi.org/10.1111/j.1475-6803.2006.00185.x>

Brennan, M. J. (1986). A theory of price limits in futures markets. *Journal of Financial Economics, 16*(2), 213–233. <https://doi.org/10.1016/0304-405X(86)90061-9>

Chen, Y.-M. (1993). Price limits and stock market volatility in Taiwan. *Pacific-Basin Finance Journal, 1*(2), 139–153. <https://doi.org/10.1016/0927-538X(93)90005-3>

Cho, D. D., Russell, J., Tiao, G. C., & Tsay, R. S. (2003). The magnet effect of price limits: Evidence from high-frequency data on Taiwan Stock Exchange. *Journal of Empirical Finance, 10*(1–2), 133–168. <https://doi.org/10.1016/S0927-5398(02)00024-5>

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. <https://doi.org/10.1111/j.1540-6261.2012.01729.x>

Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium: Empirical tests. *Journal of Political Economy, 81*(3), 607–636. <https://doi.org/10.1086/260061>

Harvey, C. R., Liu, Y., & Zhu, H. (2016). …and the cross-section of expected returns. *The Review of Financial Studies, 29*(1), 5–68. <https://doi.org/10.1093/rfs/hhv059>

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.

HSC. (2025). *Important changes of new trading system* \[Web page\]. Ho Chi Minh City Securities Corporation. <https://www.hsc.com.vn/en/important-changes-of-new-trading-system>

Kim, K. A., & Rhee, S. G. (1997). Price limit performance: Evidence from the Tokyo Stock Exchange. *The Journal of Finance, 52*(2), 885–901. <https://doi.org/10.1111/j.1540-6261.1997.tb04827.x>

Le, D. N. (2012). Evaluating impacts of reduction in fluctuation limit on stock price risks in Vietnam. *Journal of Economic Development, 214*, 116–128.

Lou, D., Polk, C., & Skouras, S. (2019). A tug of war: Overnight versus intraday expected returns. *Journal of Financial Economics, 134*(1), 192–213. <https://doi.org/10.1016/j.jfineco.2019.03.011>

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica, 55*(3), 703–708. <https://doi.org/10.2307/1913610>

Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. *The Journal of Business, 53*(1), 61–65. <https://doi.org/10.1086/296071>

Qi, B. (2023). Effectiveness of price limits: Evidence from China’s ChiNext market. *PLOS ONE, 18*(6), e0287548. <https://doi.org/10.1371/journal.pone.0287548>

Subrahmanyam, A. (1994). Circuit breakers and market volatility: A theoretical perspective. *The Journal of Finance, 49*(1), 237–254. <https://doi.org/10.1111/j.1540-6261.1994.tb04427.x>

Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price discovery and momentum strategies: Evidence from Vietnam* (SSRN Working Paper No. 1009042). <https://doi.org/10.2139/ssrn.1009042>

Viet Nam News. (2025). *KRX system officially goes live* \[News article\]. <https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html>
