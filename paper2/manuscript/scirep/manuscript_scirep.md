::: title
Do price limits delay price discovery? Overnight gaps after limit closes in Vietnam
:::

Ha Hong Hanh^1^, Nguyen Van Trung^2,^\* & Nguyen Thanh Binh^2^

^1^School of Accounting and Auditing, National Economics University, Hanoi, Vietnam.

^2^Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam.

\*Corresponding author: Nguyen Van Trung, e-mail: kontrungcany@gmail.com

::: pagebreak
:::

## Abstract

Daily price limits are meant to cool markets, but they may also delay the adjustment of prices to news. We study what happens after a stock closes at its daily limit on the Ho Chi Minh Stock Exchange, a market dominated by individual investors that applies a single 7% band and sets opening prices by call auction. Using daily prices of 347 stocks from August 2024 to September 2026, we split the next-day abnormal return into an overnight gap and an intraday return. After a ceiling close, the stock opens on average 2.2% above the market, and the following session gives back about 24% of this gap. The gap is 2.7 percentage points larger than after rises that stop short of the limit. An investor who buys at the next opening cannot capture the effect and trails the market by 0.7% by the fifth close. After a floor close the gap is negative, but its size depends on the benchmark. The limit effects pass a multiple-testing control that none of 22 price- and volume-based characteristics passes. The pattern is consistent with delayed price discovery, although news, attention and auction overshooting may also contribute.

**Keywords:** market microstructure; multiple testing; false discovery rate; call auction; emerging markets; Ho Chi Minh Stock Exchange

## Introduction

A daily price limit prevents a stock from moving beyond a fixed band within a single trading day. Exchanges in Tokyo, Taipei, Seoul, Shenzhen and Ho Chi Minh City have used limits to cool markets after large shocks, and economists ask whether a limit protects prices or postpones their adjustment. The question is sharpest where limit closes are common and call auctions set opening and closing prices. The Ho Chi Minh Stock Exchange (HOSE) has both features: a single 7% band applies to all stocks, and about 2.0% of stock-days in our event window close at the upper limit (a ceiling close) and about 1.4% at the lower limit (a floor close).

Theory predicts protection or distortion depending on the source of the shock. Well-chosen limits can be Pareto superior when fundamental news drives prices⟦brennan,kodres⟧, and imperfect transactional mechanisms can produce crashes⟦greenwald⟧, but halts can also advance trades in time and raise price variability⟦subrah⟧, and volatility can rise as the price nears a limit, a magnet effect⟦chen24,cho⟧. Empirical studies found support for three criticisms of limits (volatility spillover, delayed price discovery and trading interference) in Tokyo and Istanbul⟦kimrhee,bildik⟧, and delayed adjustment under narrow limits in Taiwan⟦chen93,huangy⟧. Studies of band changes document effects on volatility, liquidity and crash risk⟦berkmanlee,qi,zhang,jia,lien,kimjun⟧. Account data show that large investors buy on the limit day and sell on the next⟦chen19⟧, and stocks with large limit exposures or frequent upper-limit hits earn lower future returns⟦lin,zeng⟧; limit hits can be forecast⟦liang⟧ and are more frequent in small, volatile and high-volume stocks⟦kimlimp,deb⟧. For Vietnam, earlier work evaluated how narrower bands after 2008 affected price risk⟦le⟧ and documented clusters of limit hits in the early years of the market⟦farber⟧. In Taiwan, which also had a 7% band, one-day up-limit closes gained 1.18% overnight in abnormal terms and gave back 0.77% in the next session⟦huangy⟧.

A second literature separates overnight from intraday returns. Positive overnight returns are followed by intraday reversals in U.S. stocks, concentrated among stocks with recent retail attention⟦kelly,berkman12⟧; overnight returns are tied to sentiment, margin and lending costs, and market makers who absorb retail imbalances near the open⟦aboody,lou,akbas,bogous,lu⟧. In China, overnight returns are negative on average, which has been linked to the T+1 rule, and day-night anomalies concentrate at the open and close⟦qiao,gu,qiu,jones⟧. A third literature concerns multiple testing: a new return predictor needs a *t*-statistic above 3.0, or a threshold tied to a chosen false discovery rate (FDR), because many signals could have been tested⟦hlz,harveyliu,chordia,hou⟧. For Vietnam, a size effect and an earnings-to-price effect have been reported⟦huangx⟧.

Less is known about three questions. How large are the overnight gap and the intraday reversal after a limit close relative to a benchmark? Does the limit effect remain once the many other price-based signals that a researcher could test are taken into account? How does the pattern behave around the 2025 move of the HOSE to a new trading platform? We estimate the abnormal return after the ceiling and floor close, split it into an overnight gap and an intraday return, and test whether an outside buyer can capture it. We place the four limit tests in a family of 26 tests with 22 price- and volume-based characteristics and control the FDR⟦bh,hlz⟧. We test four hypotheses. If a limit delays price discovery, a ceiling close predicts a positive next-day abnormal return and a floor close a negative one (H~1~). If the opening auction absorbs blocked demand, the effect concentrates in the overnight gap (H~2~). If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of a similar size that stop short of the limit (H~3~). If the gap already contains the blocked demand, an investor who buys at the next open cannot earn the continuation, so the abnormal return from the next open to the fifth close is zero or negative (H~4~).

We report three main results. After a ceiling close, the overnight gap is 2.2%, of which the following session reverses 24%. The gap is 2.7 percentage points larger than after rises of 5% to 6.5% that stop short of the limit, and the contrast survives when the comparison stocks also close at their daily high. All four limit tests survive a multiplicity-controlled family in which no characteristic survives, and a buyer at the next open trails the market by 0.7% by the fifth close. We also split the events at the 2025 platform change.

## Results

**Sample and statistical conventions.** The event sample contains 3,187 ceiling events on 446 dates and 2,105 floor events on 319 dates among 347 stocks. A ceiling (floor) event is a close-to-close return of at least +6.5% (at most −6.5%) with the close at the daily high (low). The overnight gap is the open-to-previous-close return on day *d*+1, the intraday return is the open-to-close return on that day, and abnormal values subtract the dollar-volume-weighted market counterpart (Methods, equations (1)–(5)). All tests are two-sided at α = 0.05. For each *t*-statistic we report the *P* value from the standard normal distribution, which is below 0.001 for |*t*| ≥ 3.29; Table 1 uses the *t* distribution with *G* − 1 degrees of freedom (Methods).

### Limit closes predict next-day returns, and the characteristics do not

Figure 1 plots the *t*-statistics of the 22 Fama–MacBeth slopes in equation (7): none reaches |*t*| = 3 in any sample or 1.96 in the full sample, and none survives the Benjamini–Hochberg (BH) control. The largest full-sample |*t*| is 1.45, for 3-month and idiosyncratic momentum (confirmation-half *t* of 1.17 and 1.14). After a cost of 25 basis points, 18 of the 22 long–short quintile spreads are negative. With 79 weekly cross-sections, the minimum detectable effect at 80% power is 0.12 to 0.31 percentage points per week per standard deviation, so the null excludes only large effects. With eight Newey–West lags the largest |*t*| is 1.79 (*P* = 0.07), and dropping the least liquid 20% of stocks leaves it at 1.62 (*P* = 0.11). Without market capitalization or accounting data we cannot test the size and earnings-to-price effects reported for Vietnam⟦huangx⟧, so our null result does not contradict them. A short sample, which leaves a premium of a tenth of a percentage point per week below the minimum detectable effect, and limits that censor the highs and lows of range-based characteristics can each produce the null, and we draw no conclusion about market efficiency.

Table 1 presents the event tests. Ceiling closes earn a market-adjusted return of 1.66% on day *d*+1 and 1.45% over days *d*+1 to *d*+5, and floor closes earn −0.71% and −1.76%. All four tests survive the BH control (equation (8); adjusted *P* ≤ 0.0004), keep their signs in both halves of the sample, and exceed |*t*| = 1.96 in the confirmation half. Clustering by calendar week or 10-day block, with a *t* reference, leaves all four significant at *P* < 0.001. The floor five-day test clears the confirmation criterion by the smallest margin (*t* = −2.22 with week clusters, *P* = 0.03), and all four tests survive the rule re-applied with week-clustered statistics.

For ceilings, the five-day result comes from the first day: over days *d*+2 to *d*+5 the ceiling return is −0.24% (<<t -1.53>>). After floor closes, days *d*+2 to *d*+5 add −1.10% (<<t -2.91>>), but the confirmation-half week-clustered *t* is −1.14 (*P* = 0.25). With days *d*+2 to *d*+5 as the second horizon, the ceiling test would fail and the floor test would fail the confirmation criterion. Ceiling closes therefore carry a one-day effect, whereas floor closes carry a one-day effect plus some later drift. These tests support H~1~: limit closes predict the next day's abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon.

### The ceiling effect is an overnight gap

Table 2 decomposes the next-day return (equation (5)). After a ceiling close, the overnight gap is 2.24% (two-way-clustered <<t 9.7>>) and the intraday return is −0.54% (<<t -3.5>>): the session reverses about 24% of the gap, and the close-to-close effect is positive because the gap exceeds the giveback. The effect occurs in the opening auction, as H~2~ predicts. A stock that closes at its ceiling may carry unfilled buy orders into the night; those orders and any overnight news set the opening price, and the intraday reversal suggests that part of that price reflects transient demand. After a floor close, the gap is −0.97% (<<t -4.6>>), and the intraday return is a weak reversal of 0.30% (<<t 1.4>>).

The ceiling gap holds for exact limit hits (2.79%) and for the first day of a streak of exact hits (2.39%). Near hits show a smaller gap (1.67%) and no reliable intraday return. However, their median day-*d* return is 6.89%, almost the same as the 6.90% of exact hits, and 83% of their closes are not multiples of the tick size. This points to later price adjustment by the data vendor rather than to closes below the limit; the split is therefore weighted toward higher-priced stocks, where the tick is coarser, and we do not read the difference as a gradient toward the limit. The ceiling gap appears in both halves of the sample and on days locked at one price from open to close. It also appears in each tercile of the 60-day average dollar volume (1.52% in the most liquid tercile). Against same-date controls, the ceiling gap is 2.70%.

The floor effect is less robust. Against same-date controls the floor close-to-close return is −1.65%, so its size depends on the benchmark. Floor events also cluster on market-wide down days: excluding days on which the market fell by more than 2% removes 1,371 of the 2,111 floor events. The floor gap is not significant in the least liquid tercile (<<t -1.0>>).

An outside buyer cannot capture the close-to-close continuation. A buyer who wants a stock at its ceiling joins a queue at the close, so the first obtainable price is the next open, which already contains the gap. From that open, the ceiling return through the fifth close is −0.75% against the market (<<t -2.7>>) and −0.53% against same-date controls (<<t -1.8>>), which supports H~4~; a holder who sells at the next open avoids the intraday giveback. These figures use quoted prices and ignore achievable fills: 522 ceiling events were locked at one price all day, and some of these stocks opened at the limit the next day, where a buyer may be rationed. After floor closes, prices fall a further 0.82% from the next open to the fifth close against the market (<<t -1.7>>), which is not significant at the 5% level.

### The gap breaks at the limit

Figure 2 plots the three next-day measures against the size of the day-*d* move. Inside the band, the close-to-close relation is negative, a short-term reversal. At the limit the relation breaks: the overnight gap jumps up at the ceiling and down at the floor. Table 3 quantifies the break. Ceiling closers have a gap 2.66 percentage points larger than stocks that rose 5% to 6.5% (<<t 14.0>>), and their intraday return is 0.31 points lower. Floor closers have a gap 1.59 points lower than stocks that fell 5% to 6.5% (<<t -9.7>>). Because the event rule requires a close at the day's high (low), we repeat the comparison with stocks that also closed at their high (low). The ceiling gap is then 3.14 points larger (<<t 14.5>>), and the floor gap is 1.81 points lower (<<t -8.7>>). A strong close therefore does not explain the contrast, which supports H~3~. The comparison is an association around a rule-based threshold, not a regression-discontinuity design, and stocks that reach the limit may differ in news content.

Three readings fit the pattern, and our data do not separate them: (1) demand or supply that the limit blocked on day *d* clears at the next opening, the delayed price discovery described by Kim and Rhee⟦kimrhee⟧; (2) news and retail attention persist overnight and produce the overnight gain and intraday reversal of attention-grabbing stocks⟦berkman12⟧, with or without a limit; and (3) the opening auction overshoots and corrects within the day. Lacking announcements, order books and limit-free stock-days, we run two partial checks. First, the ceiling gap rises across terciles of day-*d* volume relative to its prior 60-day mean (1.97%, 2.16% and 2.63%) and of the prior 20-day return (1.41%, 2.18% and 3.16%), which fits readings (1) and (2) alike, and stays positive in the lowest tercile of each proxy (<<t 4.8>> and <<t 4.2>>). For floors, the gap moves from −1.20% to −0.68% across volume terciles and is not monotone in the prior return, so the attention reading does not carry over. Second, the comparison with stocks that closed at their high removes selection on the shape of the close, but not on news. The intraday giveback fits readings (2) and (3) at least as well as permanent price discovery, so "break at the limit" is a description and delayed price discovery is one hypothesis. Testing the magnet effect⟦chen24,cho⟧ requires intraday prices, which we lack.

### Timing around the 2025 change of trading platform

Table 4 splits the events on 5 May 2025, when the HOSE moved to the trading platform of the Korea Exchange (KRX). The ceiling gap, followed by an intraday reversal, appears in both periods: 1.65% before and 2.49% after (difference <<t 1.6>>). The floor gap is more negative after the move, at −0.42% before and −1.37% after (difference <<t -3.2>>). After the move the intraday return after floor closes turns positive (0.64%), and the floor drift from the next open to day *d*+5 exists only before it (−1.73% before and −0.15% after). The change coincides with a different market period: the post-change sample accounts for 71% of the ceiling events and 58% of the floor events. Before the change, neither the ceiling close-to-close return (<<t 1.0>>) nor the floor gap (<<t -1.9>>) is significant at the 5% level, so the full-sample significance of these two measures rests mainly on post-change events. We cannot attribute the differences between the periods to the auction rules.

Because the events are unbalanced in time, Table 5 reports them by calendar quarter. The ceiling gap is positive in each of the eight quarters (*t* from 2.5 to 16.8; *P* ≤ 0.013), and the floor gap is negative in every quarter and significant at the 5% level in seven of them. We also move the break date to the first trading day of each month from January 2025 to April 2026. These placebo dates give ceiling-gap differences between −0.45 and 0.72 percentage points, all with |*t*| ≤ 1.4 (*P* ≥ 0.16). The split at 5 May 2025 gives the largest difference, 0.85 points, which is not significant either (<<t 1.6>>). For floors, the difference is positive at the four placebo dates before the platform change and negative at 11 of the 11 later ones; the split at 5 May 2025 gives −0.95 points (<<t -3.2>>), close to the placebo dates that follow it. Table 5 shows no trend in the floor gap, but the floor gap is weak in 2025-Q2 (−0.34%, <<t -1.5>>), the quarter with the most floor events (802). The placebo dates therefore cannot separate a break at the platform change from a shift specific to that quarter.

A difference-in-differences regression compares limit closes with 5–6.5% movers that also closed at the extreme (Supplementary Table S4). For ceilings, the excess gap was 2.91 percentage points before the change (<<t 6.2>>) and changed by 0.38 points after it (<<t 0.8>>). For floors, the excess gap was −1.62 points before (<<t -6.6>>) and changed by −0.49 points (<<t -1.5>>). The break at the limit is therefore present before the change and does not depend on the post-change period, although the significance of the raw ceiling close-to-close return and of the raw floor gap does (Table 4). These comparisons describe timing, not an effect of the auction rules.

### Robustness

Returns beyond ±8%, which a 7% band does not allow, occur on 96 stock-days and may reflect unadjusted corporate actions or listing-day bands. Dropping every event within five trading days of such a return moves the ceiling gap from 2.24% to 2.26% and the floor gap from −0.97% to −0.98%; the outlier days stay in the market benchmark. Event definitions that do not depend on the tick grid give the same picture (Supplementary Table S2): the ceiling gap is 2.07% for returns of at least 6.0% that close at the high, 2.33% at 6.8%, 2.35% for returns between 6.7% and 7.3%, 2.10% without the close-at-high condition and 2.91% on days locked at one price (all *t* > 2.9, *P* < 0.01); the floor gap ranges from −0.79% to −2.50%. The four event tests also survive every alternative family definition we consider (Supplementary Table S3): the four event tests as their own family, separate ceiling and floor families, the 26 tests under Holm⟦holm⟧ or Bonferroni adjustment, a 28-test family that adds the days *d*+2 to *d*+5 outcomes, and week-clustered event *P* values; the largest adjusted *P* value across these definitions is 0.0026.

To bound the effect of a wider search, let *p*~max~ be the largest event-test *P* value computed with the factor *G*/(*G* − 1) and a *t* reference. All four event tests survive a Bonferroni correction at 5% in families of up to ⌊0.05/*p*~max~⌋ tests: 683 with date clusters and 125 with calendar-week clusters (*p*~max~ of 0.00007 and 0.00040). The bound limits false discoveries but leaves the upward bias in effect sizes untouched. The results support H~1~ to H~4~ for ceilings; the floor effect depends on the benchmark, and its drift appears only before the 2025 platform change.

## Discussion

Our ceiling gap is larger than the 1.18% reported for Taiwan⟦huangy⟧, and the following session reverses a smaller share of it (about 24% against about two thirds). Our decomposition also adds timing to the evidence from Tokyo⟦kimrhee⟧: on the HOSE, the continuation after ceiling closes arrives at the next opening and ends after the first day, and the intraday giveback is a one-day analogue of the cross-period reversal found in U.S. stocks⟦lou⟧. A pure attention reading must explain the contrast with stocks that moved almost as far, including those that also closed at their high, and a gap-only reading cannot explain the pre-change post-open drift after floor closes. The earlier studies measure different outcomes and horizons, so Supplementary Table S1 compares signs, timing and mechanisms rather than magnitudes; for example, the day-1 abnormal return after ceiling and floor closes on ChiNext⟦qi⟧ shows the opposite asymmetry, and overnight returns in China are negative on average⟦qiao⟧, whereas on the HOSE the overnight return after ceiling closes is positive.

A 7% band leaves room for a large overnight gap, so the opening auction may do much of the adjustment that a wider band would allow on day *d*. The floor results after at-the-open orders lost priority (Table 4) fit auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time; a band change on the HOSE, like the ChiNext widening⟦qi⟧, would give a natural experiment. The volume and prior-return results also fit an attention channel in which the limit amplifies demand: a stock at its ceiling may appear on screens and rankings the next morning, and a queue at the limit may signal excess demand.

The estimates describe what follows limit closes on the HOSE from 2024 to 2026. They cannot show what the limit does to price discovery: the band does not vary, no period lacks a limit, and we measure none of the benefits a limit is meant to deliver. For investors, buying ceiling stocks at the quoted next open lost money against the market by the fifth close, excluding costs and rationing at the open.

Several limitations qualify these results. The sample covers 519 trading days on one exchange, with one platform change and a period of market stress. Without order-book, investor-type, announcement or news data, we infer the unfilled-demand mechanism and cannot separate it from selection on news. The 7% band, reference price and platform change come from brokerage and press descriptions, checked against returns but not against exchange circulars; tick sizes, reference prices on corporate-action days, and wider bands for first-day listings and resumed trading are assumptions. The data vendor appears to adjust earlier prices for later corporate actions: for stocks priced at 10 thousand dong or more, only 25% to 58% of closes are tick multiples, and near hits make up 62% of ceiling events for the higher-priced stocks against 23% for the others. Proportional adjustment leaves returns (except on ex-dates), the close-at-high rule and locked days unchanged but makes the exact-hit classification unreliable, so we treat that split as a data check, not a measure of distance to the limit. The listing snapshot excludes stocks delisted before the download. Events in one market episode may depend on each other beyond our clustering, and we computed no calendar-time portfolio estimates or standard errors robust to both cross-sectional and serial dependence. Several characteristics (5-day return, largest and smallest daily returns, move frequency and overnight return) share inputs with the event definition, and the Corwin–Schultz spread and range volatility use limit-censored highs and lows. The floor effect depends on the benchmark, and we built no beta- and size-matched control for the five-day outcome. The characteristic tests have limited power, and effect sizes may carry winner's-curse bias from choosing this question among several screened on the same data.

In sum, of 26 tests on 347 HOSE stocks, the four price-limit tests survive FDR control and the confirmation-half check, and the 22 lower-powered characteristic tests do not. After a ceiling close, the next-day abnormal return of 1.7% is an overnight gap of 2.2% less an intraday reversal of 0.5%. The gap is 2.7 percentage points larger than for stocks that rose 5% to 6.5% and 3.1 points larger than for those among them that also closed at their high. After a floor close, the overnight gap is −1.0%. An outside buyer at the next open loses 0.7% against the market by the fifth close. The pattern is consistent with delayed price discovery at the limit, but news, attention and opening-auction overshooting remain possible explanations; longer samples, announcement time stamps and order-book queues would let future work separate them.

## Methods

### Data and institutional setting

On 24 September 2026 we downloaded daily open, high, low, close and volume series for all HOSE-listed stocks with the vnstock Python library (version 4.0.4; source Vietcap Securities, VCI). A listing file from the same source and date (743 rows for all instrument types) defines the universe. The retrieval returned 405 HOSE stock files with records through 23 September 2026, and we used the 519 trading days from 21 August 2024. Prices are in thousand dong. The vendor does not document corporate-action adjustment, and the files contain no market capitalization, order book, investor type or news. We kept the 347 stocks with at least 95% non-missing closes, 178,773 stock-days in all. The daily close-to-close return has a mean of 0.018%, a median of 0.00% and a standard deviation of 2.10%. Dollar volume (price times shares traded, in dong) is skewed, with a median of 2.6 billion dong per stock-day and a mean of 51.2 billion. The stocks span 18 two-digit Industry Classification Benchmark sectors; the largest holds 15% of them.

The HOSE sets a daily price limit of 7% around the reference price, the previous close on normal trading days⟦hsc⟧. On 5 May 2025 the HOSE moved to the trading platform of the Korea Exchange (KRX). The band remained unchanged, but at-the-open and at-the-close orders lost their priority over limit orders in the opening and closing call auctions⟦hsc,vnnews⟧, whose prices define our events and gaps. Treating the band, tick sizes and reference-price rule as assumptions, we check the band against the data: 1.98% of stock-days fall between +6.5% and +7.1% and 1.30% between −7.1% and −6.5%, against 0.29% between +6.0% and +6.5%, a pile-up consistent with a 7% band.

### Returns, events and outcomes

For stock *i* on trading day *d*, *C*~*i,d*~, *O*~*i,d*~, *H*~*i,d*~ and *L*~*i,d*~ are the close, open, high and low prices, and the close-to-close return is

| | |
|:------------------------------------------------:|:--:|
| $$R_{i,d} = \frac{C_{i,d}}{C_{i,d-1}} - 1.$$ | (1) |

A ceiling event has a return (equation (1)) of *R*~*i,d*~ ≥ 0.065 and *C*~*i,d*~ = *H*~*i,d*~, whereas a floor event has *R*~*i,d*~ ≤ −0.065 and *C*~*i,d*~ = *L*~*i,d*~. The event window runs from day 61, when a 60-day volume history exists, to five days before the sample end. The market return weights stocks by dollar volume,

| | |
|:-------------------------------------------------:|:--:|
| $$R^{\text{mkt}}_{d} = \sum_{j} w_{j,d} R_{j,d}, \qquad w_{j,d} = \frac{\overline{V}_{j,d}}{\sum_{l} \overline{V}_{l,d}}$$ | (2) |

where *j* and *l* run over stocks with a day-*d* return and a full 60-day history, and *V̄*~*j,d*~ is the mean dollar volume of stock *j* over the 60 trading days through day *d*. An exact hit is an event whose close equals the limit price (within 10^−6^ thousand dong),

| | |
|:------------------------------------------------:|:--:|
| $$P^{\text{ceiling}}_{i,d} = \left\lfloor \frac{1.07\, C_{i,d-1}}{\delta} \right\rfloor \delta, \qquad P^{\text{floor}}_{i,d} = \left\lceil \frac{0.93\, C_{i,d-1}}{\delta} \right\rceil \delta$$ | (3) |

where ⌊·⌋ and ⌈·⌉ round down and up (after adding and subtracting 10^−9^, respectively, against floating-point error), and the tick δ is 0.01, 0.05 or 0.10 thousand dong for reference prices *C*~*i,d*−1~ below 10, from 10 to below 50, and from 50 upward. Other events are near hits (see Discussion on vendor price adjustment).

The abnormal return (AR) on day *d*+1 and the cumulative abnormal return (CAR) over days *d*+1 to *d*+5 are

| | |
|:------------------------------------------------:|:--:|
| $$\text{AR}_{i,d} = R_{i,d+1} - R^{\text{mkt}}_{d+1}, \qquad \text{CAR}_{i,d} = \prod_{k=1}^{5}\left(1 + R_{i,d+k}\right) - \prod_{k=1}^{5}\left(1 + R^{\text{mkt}}_{d+k}\right)$$ | (4) |

where each *R*^mkt^~*d*+*k*~ uses weights through day *d*+*k* (Table 1). The day-*d*+1 return splits into the overnight gap and the intraday return,

| | |
|:------------------------------------------------:|:--:|
| $$\text{GAP}_{i,d} = \frac{O_{i,d+1}}{C_{i,d}} - 1, \quad \text{INTRA}_{i,d} = \frac{C_{i,d+1}}{O_{i,d+1}} - 1, \quad 1 + R_{i,d+1} = \left(1 + \text{GAP}_{i,d}\right)\left(1 + \text{INTRA}_{i,d}\right)$$ | (5) |

and abnormal values subtract the market counterpart of each component, the same-interval return across stocks weighted by *w*~*j,d*~, known at the event close. A buyer at the next open earns *C*~*i,d*+5~/*O*~*i,d*+1~ − 1 less the buy-and-hold market return Σ~*j*~ *w*~*j,d*~ (*C*~*j,d*+5~/*O*~*j,d*+1~ − 1). The control benchmark is the equal-weighted mean same-interval return of control stocks (absolute day-*d* return below 6.5%) in the event stock's tercile of *V̄*~*i,d*~ on that date; dates with fewer than 30 control stocks have no benchmark.

The event definition uses only returns and the close-at-high (close-at-low) condition, which proportional price adjustment by the vendor leaves unchanged except on ex-dates; the exact-hit split is a diagnostic only. Event counts differ across exhibits because each outcome requires different data. Table 1 requires returns on all five days after the event (3,187 ceiling and 2,105 floor events). Tables 2 to 4 require the opening and closing prices of day *d*+1 (3,199 and 2,111 events), the open-to-day-*d*+5 return also requires the day-*d*+5 closing price, and the control benchmark requires at least 30 control stocks on the date (3,100 and 2,047 events). Figure 2 uses event days up to the second-to-last trading day (3,220 ceiling events). No event was dropped for any other reason.

### Statistical inference

For *N* events *e*, each a stock-day pair, with outcome *y*~*e*~ and mean *ȳ* = *N*^−1^Σ~*e*~ *y*~*e*~, the cluster-robust variance is

| | |
|:------------------------------------------------:|:--:|
| $$\widehat{\mathrm{Var}}(\bar{y}) = \frac{1}{N^{2}} \cdot \frac{G}{G-1} \sum_{g=1}^{G}\left(\sum_{e \in g}\left(y_{e} - \bar{y}\right)\right)^{2}$$ | (6) |

where *g* = 1, …, *G* indexes clusters: event dates, calendar weeks (ISO 8601) or blocks of ten consecutive trading days. The family *P* values of the four event tests use equation (6) with event-date clusters, omit *G*/(*G* − 1) and take a normal reference. Table 1 *t*-statistics include the factor and use a *t* reference with *G* − 1 degrees of freedom. The family *P* values keep the convention of the first computation of the planned tests; the analysis plan specified date-clustered standard errors but not the reference distribution, and we did not change the convention after seeing the results, so that the multiplicity control is not tuned to them. Table 1 adds the small-sample factor and the *t* reference as a more conservative check. Under these settings the four event tests still survive a Bonferroni correction in families of up to 683 tests with date clusters and 125 with calendar-week clusters, so the choice does not change any conclusion. Two-way clustering by date and stock follows Cameron et al.⟦cameron⟧, without the factor and with the variance bounded below at 10^−12^. Table 3 reports β̂ from *y*~*e*~ = α + β *D*~*e*~ + *u*~*e*~, where *D*~*e*~ = 1 for limit closes and 0 for the comparison moves, α is the intercept and *u*~*e*~ is the error, with date-clustered HC1 standard errors (R package *sandwich*). For the *t*-statistics of Tables 2 to 5 and of the text we report two-sided *P* values from the standard normal distribution (|*t*| = 1.96 gives *P* = 0.05; |*t*| = 3.29 gives *P* = 0.001); Table 1 uses the *t* reference instead. The word "significant" always means *P* < 0.05 for the stated test. Descriptive statistics report means and, where stated, medians and standard deviations; the *n* of each analysis is given in the tables and text.

### Characteristics and Fama–MacBeth regressions

We form cross-sections on trading days 120 (so that every lookback is complete), 125 and so on to 510: *T* = 79 formation weeks τ (five-trading-day periods, not the calendar weeks used for clustering), each followed by a non-overlapping five-day holding period. Each week we rank-normalize each characteristic *x*~*i*,τ~ across the *n*~τ~ stocks with complete data (all 115 days of the longest lookback, trades on at least 50 of the last 60 days, and next-five-day returns) as *z*~*i*,τ~ = Φ^−1^((rank(*x*~*i*,τ~) − 0.5)/*n*~τ~), with ties at average ranks and Φ^−1^ the inverse standard normal distribution function. The outcome *y*~*i*,τ~ is the stock's compounded return over the next five trading days minus the *V̄*-weighted average five-day return of these stocks. The Fama–MacBeth regressions⟦fm⟧ are

| | |
|:------------------------------------------------:|:--:|
| $$y_{i,\tau} = a_{\tau} + \gamma_{\tau} z_{i,\tau} + \varepsilon_{i,\tau}, \qquad \hat{\gamma} = \frac{1}{T}\sum_{\tau=1}^{T}\hat{\gamma}_{\tau}$$ | (7) |

with a weekly intercept *a*~τ~, slope γ~τ~ and residual ε~*i*,τ~. The *t*-statistic of γ̂ uses Newey–West standard errors⟦nw⟧ (four lags, Bartlett weights, no prewhitening) and 78 degrees of freedom. Supplementary Note 1 defines the 22 momentum, reversal, risk, liquidity, volume and intraday characteristics. We also report long–short spreads between the extreme quintiles before and after a cost of 25 basis points per unit of traded value. The minimum detectable effect (MDE) at 80% power and a 5% two-sided level is MDE = (1.96 + 0.84) SE(γ̂) ≈ 2.8 SE(γ̂), with SE the Newey–West standard error.

### Multiplicity and survival rule

The family has *m* = 26 tests: the 22 characteristics and the ceiling and floor tests at the two horizons of equation (4). With *P* values ordered as *p*~(1)~ ≤ … ≤ *p*~(*m*)~, the BH adjusted *P* value at rank *r* is

| | |
|:------------------------------------------------:|:--:|
| $$\tilde{p}_{(r)} = \min_{s \ge r}\left\{\min\left(1, \frac{m}{s}\, p_{(s)}\right)\right\}$$ | (8) |

We also report Holm adjustments⟦holm⟧ and the |*t*| = 3 hurdle⟦hlz⟧. A test survives if the adjusted *P* value is below 0.05, which controls the FDR⟦bh⟧ at 5%; if its signs agree in the discovery half (the first 39 weeks or the events up to the median event date) and the confirmation half; and if its confirmation-half |*t*| exceeds 1.96. Lookbacks overlap with the discovery half, so the confirmation half is not a strict hold-out, and the weekly regressions (from day 120) and event window (from day 61) cover different spans. We place the four event tests and the 22 characteristics in one family because the analysis plan treated all 26 as candidate predictors of short-horizon returns examined on the same data, so the limit result pays for every candidate signal in the plan.

### Analysis plan and exploratory analyses

We fixed the family, estimators, multiplicity control and survival rule in a written analysis plan before computing the results. A version-control time stamp dates the plan before the first analysis code, but no external registry holds it, and we had examined related data in earlier work, so it gives no independent confirmation. We departed from it by reading its ambiguous second horizon as days *d*+1 to *d*+5 (not *d*+2 to *d*+5), splitting event halves at the median event date (not weeks 39 and 40), reporting quintile rather than decile spreads, and omitting its same-stock control and multivariate model. Analyses added after the first results are exploratory, and the tests of H~2~ to H~4~ rest on them: decomposition, next-open returns, control group, sub-limit comparison, exact hits, two-way clustering, subsamples, terciles, platform split and outlier exclusion. We also screened several candidate ideas on the same data before choosing this one, so the effect sizes may be overstated.

### Use of generative AI

The authors used the generative AI tool Gemini (Google) only to edit the language of the manuscript. It was not used for the analysis, the code, the literature search or the interpretation of results, and it is not an author. The authors reviewed all edited text and take full responsibility for the content. References and the institutional facts above were checked by web search, not against exchange circulars.

### Software and ethics

One R 4.3.3 script (packages sandwich, lmtest and ggplot2) reproduces every number, table and figure; the figures in this version were redrawn from the saved R output tables with Python (matplotlib) without re-estimating any number. The study uses public market prices and involves no human or animal participants, so ethical approval and consent were not required.

## Data availability

The price files (vnstock 4.0.4, source VCI, retrieved on 24 September 2026), the R code and the output tables are available at https://github.com/trungcandygit/black_litterman_2 (folders data/raw and paper2).

## References

::: references
:::

## Acknowledgements

The authors received no assistance beyond that described in Methods.

## Author contributions

H.H.H. contributed to the methodology and validation and reviewed and edited the manuscript. N.V.T. conceived the study, curated the data, performed the formal analysis, developed the methodology and software, produced the visualizations, administered the project and wrote the original draft. N.T.B. conceived the study, supervised the work, validated the results, and reviewed and edited the manuscript.

## Funding

This research did not receive any financial support.

## Competing interests

The authors declare no competing interests.

## Additional information

**Supplementary information** is provided in a separate file. **Correspondence** and requests for materials should be addressed to N.V.T.

## Figure legends

::: figures
:::

## Tables

::: tables
:::
