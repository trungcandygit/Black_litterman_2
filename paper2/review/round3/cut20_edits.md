# Cut-20% edit list for manuscript_final.Rmd

Apply each edit as an exact, single-occurrence string replacement. Old strings are unique in the current `paper2/manuscript/manuscript_final.Rmd` and no two edits overlap.

**E1.** Abstract: trim to budget, merge power caveat
~~~old
**Abstract.** Regulators impose daily price limits to cool markets, but limits can delay price discovery. Few studies trace prices after limit closes in emerging markets, and those we know of ignore the many other price-based signals a researcher could have tested. We study `r nstocks` stocks on the Ho Chi Minh Stock Exchange from August 2024 to September 2026 and run 26 tests under false-discovery-rate control: four price-limit event tests and 22 tests of price- and volume-based characteristics. All four limit tests survive the control; none of the 22 characteristic tests does, although those tests have limited power. After a ceiling close, the stock earns a next-day abnormal return of `r f(ev("ceiling","t+1","mean_ar_pct"),1)`%: an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%. The gap exceeds that of stocks that rose 5% to 6.5% by `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points. A buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. The pattern fits delayed price discovery, but news and attention fit it as well, and without news or order-book data we cannot separate these explanations.
~~~
~~~new
**Abstract.** Daily price limits aim to cool markets but can delay price discovery. Few studies trace prices after limit closes in emerging markets, and none we know of tests the limit against other candidate signals. For `r nstocks` stocks on the Ho Chi Minh Stock Exchange from August 2024 to September 2026, we run 26 tests under false-discovery-rate control: four price-limit event tests and 22 price- and volume-based characteristics. All four limit tests survive; none of the 22 lower-powered characteristic tests does. After a ceiling close, the next-day abnormal return of `r f(ev("ceiling","t+1","mean_ar_pct"),1)`% is an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%, and the gap exceeds that after rises of 5% to 6.5% by `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points. A buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. Delayed price discovery fits the pattern, but so do news and attention; without news or order-book data we cannot separate them.
~~~

**E2.** Intro P1: drop band-change sentence repeated in P2 and Section 2
~~~old
A daily price limit stops a stock from moving beyond a fixed band within one trading day. Regulators adopt limits to cool markets after large shocks, and exchanges in Tokyo, Taipei, Seoul, Shenzhen, and Ho Chi Minh City have used them. Economists ask whether a limit protects prices or postpones their adjustment, and recent band changes in China, Taiwan, and Korea give them new test cases. The question is sharpest in markets where a limit close is common and where opening and closing prices come from call auctions. The Ho Chi Minh Stock Exchange (HOSE) has both features: it applies one 7% band to all stocks, and about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in our event window close at the upper limit (a ceiling close; Section 4) and about `r f(100 * C13$value[6] / C13$value[1], 1)`% at the lower limit (a floor close).
~~~
~~~new
A daily price limit stops a stock from moving beyond a fixed band within one trading day. Exchanges in Tokyo, Taipei, Seoul, Shenzhen, and Ho Chi Minh City have used limits to cool markets after large shocks, and economists ask whether a limit protects prices or postpones their adjustment. The question is sharpest where limit closes are common and call auctions set the opening and closing prices. The Ho Chi Minh Stock Exchange (HOSE) has both features: one 7% band applies to all stocks, and about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in our event window close at the upper limit (a ceiling close; Section 4) and about `r f(100 * C13$value[6] / C13$value[1], 1)`% at the lower limit (a floor close).
~~~

**E3.** Intro P2: keep bounded novelty statement, cut list redundancy
~~~old
Recent work on price limits measures market quality and investor behavior. Studies of band changes document effects on volatility, liquidity, and crash risk (Jia et al., 2024; Lien et al., 2019; Qi, 2023), and account-level work shows that large investors buy on the limit day and sell on the next day (Chen et al., 2019). However, of the studies we reviewed, only Huang et al. (2001) describe the overnight-then-intraday pattern after limit hits, and the records we could access give no magnitudes; none measures the overnight gap and the intraday return after a limit close against a benchmark, none places the limit result in a family of tests that controls for the many other price-based signals a researcher could have examined, and none examines the 2025 move of HOSE to a new trading platform.
~~~
~~~new
Studies of band changes document effects on volatility, liquidity, and crash risk (Jia et al., 2024; Lien et al., 2019; Qi, 2023), and account-level data show that large investors buy on the limit day and sell on the next (Chen et al., 2019). Of the studies we reviewed, only Huang et al. (2001) describe the overnight-then-intraday pattern after limit hits, and the records we could access give no magnitudes. None measures the overnight gap and the intraday return after a limit close against a benchmark, places the limit result in a family of tests that controls for the other price-based signals a researcher could have examined, or examines the 2025 move of HOSE to a new trading platform.
~~~

**E4.** Intro P3: tighten
~~~old
We estimate the abnormal return after ceiling and floor closes on HOSE, measure how much of it arises in the overnight gap, and test whether an outside buyer can capture it. We place the four limit tests in one family of 26 tests with 22 price- and volume-based characteristics and control the false discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).
~~~
~~~new
We estimate the abnormal return after ceiling and floor closes on HOSE, split it into the overnight gap and the intraday return, and test whether an outside buyer can capture it. We place the four limit tests in a family of 26 tests with 22 price- and volume-based characteristics and control the false discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).
~~~

**E5.** Intro contributions: tighten second contribution, drop meta sentence
~~~old
We make three contributions. First, we measure the overnight gap and the intraday return after limit closes, a pattern that Huang et al. (2001) describe qualitatively for Taiwan, and show that the ceiling effect is a gap of `r f(c16("Ceiling all","gap_mkt"),1)`% of which the following session reverses `r f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0)`%. Second, we compare limit closes with stocks that moved almost as far without reaching the limit, including stocks that also closed at their daily high, and find that the ceiling gap is `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points larger at the limit than after rises of 5% to 6.5%. Third, we show that all four limit tests survive a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. We also compare each result with the studies reviewed in Section 2 and split the events at the 2025 change of trading platform.
~~~
~~~new
We make three contributions. First, we measure the overnight gap and the intraday return after limit closes, a pattern that Huang et al. (2001) describe qualitatively for Taiwan, and show that the ceiling effect is a gap of `r f(c16("Ceiling all","gap_mkt"),1)`% of which the following session reverses `r f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0)`%. Second, we show that the ceiling gap is `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points larger than after rises of 5% to 6.5% that stop short of the limit, and that the contrast survives when the comparison stocks also close at their daily high. Third, we show that all four limit tests survive a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. We also split the events at the 2025 platform change.
~~~

**E6.** Roadmap: compress
~~~old
Section 2 reviews the literature and states the hypotheses, Section 3 describes the data and the institutional setting, and Section 4 sets out the design. Section 5 reports the results, Section 6 compares them with earlier studies and discusses mechanisms and implications, Section 7 lists limitations, and Section 8 concludes.
~~~
~~~new
Section 2 reviews the literature, Sections 3 and 4 describe the data and design, Section 5 reports results, Section 6 discusses them, and Sections 7 and 8 give limitations and conclusions.
~~~

**E7.** Section 2 theory: merge sentences
~~~old
**Theory.** Models predict protection or distortion, depending on the source of the shock. Brennan (1986) provides a rationale for price limits in futures markets, and Kodres and O'Brien (1994) show that well-chosen limits can be Pareto superior when fluctuations come from fundamental news, because limits insure traders against part of the implementation risk. Greenwald and Stein (1991) link crashes to imperfections in transactional mechanisms. Against this case, Subrahmanyam (1994) shows that trading halts can advance trades in time and raise price variability, and Chen et al. (2024) show in an equilibrium model that volatility rises as the price approaches a circuit breaker, which produces a magnet effect. A limit that only delays adjustment leaves a predictable next-day continuation, so the return after a limit close bears on this debate.
~~~
~~~new
**Theory.** Models predict protection or distortion, depending on the source of the shock. Brennan (1986) rationalizes limits in futures markets, Kodres and O'Brien (1994) show that limits can be Pareto superior when fundamental news drives prices because they insure traders against implementation risk, and Greenwald and Stein (1991) link crashes to imperfect transactional mechanisms. Subrahmanyam (1994) shows that halts can advance trades in time and raise price variability, and in the model of Chen et al. (2024) volatility rises as the price nears a circuit breaker, a magnet effect. A limit that only delays adjustment leaves a predictable next-day continuation, which the return after a limit close can reveal.
~~~

**E8.** Section 2 classic evidence: tighten; gap sentence moved to the gap paragraph
~~~old
**Classic evidence on price-limit performance.** Early empirical work infers the costs of limits from volatility and serial correlation across days. Kim and Rhee (1997) organize the empirical debate around three criticisms of limits: they spill volatility into later days, delay price discovery, and interfere with trading. They find support for all three in Tokyo. Bildik and Gülay (2006) find the same in Istanbul and show that price locks at the limit give stronger evidence than limit moves alone. Chen (1993) finds that serial correlation falls as the Taiwanese limit widens, which implies that the narrower limit delayed price adjustment, and Berkman and Lee (2002) examine volatility and trading activity around a revision of the limit system in Korea. Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits reverses during the following trading day, the timing pattern we test on HOSE. Cho et al. (2003) add a fourth hypothesis, the magnet effect, and find that prices accelerate toward the upper limit in five-minute Taiwanese data. Kim and Limpaphayom (2000) show that small, volatile, high-volume stocks are more likely to hit limits, and Deb et al. (2013) argue that rigid limits in Tokyo can disrupt price discovery and liquidity provision. Apart from Huang et al. (2001), these studies do not split the next-day return into the overnight gap and the session that follows.
~~~
~~~new
**Classic evidence.** Kim and Rhee (1997) find support in Tokyo for three criticisms of limits: they spill volatility into later days, delay price discovery, and interfere with trading. Bildik and Gülay (2006) find the same in Istanbul, with stronger evidence from price locks than from limit moves alone. Chen (1993) finds that serial correlation falls as the Taiwanese limit widens, which implies delayed adjustment under the narrower limit, and Berkman and Lee (2002) examine volatility and trading activity around a revision of the Korean limit system. Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits reverses during the following day, the timing pattern we test. Cho et al. (2003) find a magnet effect: prices accelerate toward the upper limit in five-minute Taiwanese data. Kim and Limpaphayom (2000) show that small, volatile, high-volume stocks hit limits more often, and Deb et al. (2013) argue that rigid limits in Tokyo can disrupt price discovery and liquidity provision.
~~~

**E9.** Section 2 band changes: compress; positioning sentence folded into gap paragraph
~~~old
**Recent evidence from band changes and investor-level data.** The widening of the ChiNext band from 10% to 20% in August 2020 gave several studies a quasi-natural experiment. Qi (2023) confirms delayed price discovery, volatility spillover, and trading interference, with stronger effects at the lower limit and no magnet effect. Zhang et al. (2022) find higher liquidity, higher volatility, and a higher probability of informed trading after the widening, and Jia et al. (2024) find lower crash risk. Lien et al. (2019) find higher spreads and intraday volatility but better execution quality after Taiwan widened its band in 2015, and Kim and Jun (2019) find higher intraday realized variance after Korea widened its band from 15% to 30%. Chen et al. (2019) use account-level Shenzhen data and show that large investors buy on the day a stock hits the 10% upper limit and sell on the next day, and that their net buying on the limit day predicts stronger long-run reversal. Two recent studies look at the cross-section: Lin et al. (2023) find that stocks with large exposure to daily price limits attract attention and earn lower future returns, with the largest effect where retail investors hold many shares, and Zeng et al. (2024) relate the frequency of upper-limit hits to lower future returns. Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit. The band-change studies compare periods with different bands, and the cross-sectional studies sort stocks by limit exposure; ours conditions on individual limit closes within one band regime.
~~~
~~~new
**Band changes and investor-level data.** After ChiNext widened its band from 10% to 20% in August 2020, Qi (2023) confirms delayed price discovery, volatility spillover, and trading interference, stronger at the lower limit and with no magnet effect; Zhang et al. (2022) find higher liquidity, volatility, and probability of informed trading; and Jia et al. (2024) find lower crash risk. Wider bands raised spreads and intraday volatility but improved execution quality in Taiwan (Lien et al., 2019) and raised intraday realized variance in Korea (Kim & Jun, 2019). In Shenzhen account data, large investors buy on the day a stock hits the 10% upper limit and sell the next day, and their limit-day net buying predicts stronger long-run reversal (Chen et al., 2019). Stocks with large limit exposure attract attention and earn lower future returns, most where retail investors hold many shares (Lin et al., 2023), as do stocks with frequent upper-limit hits (Zeng et al., 2024). Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit.
~~~

**E10.** Section 2 overnight: compress; drop 'none conditions' (stated once in gap paragraph)
~~~old
**Overnight and intraday returns.** Returns earned overnight differ from returns earned during the session, and explanations range from investor attention and sentiment to funding costs and market-maker inventory. Kelly and Clark (2011) document the split for index funds. Berkman et al. (2012) find positive overnight returns followed by intraday reversals in U.S. stocks, concentrated among stocks with recent retail attention. Aboody et al. (2018) tie overnight persistence to investor sentiment, Lou et al. (2019) show strong overnight and intraday continuation with an offsetting cross-period reversal, and Akbas et al. (2022) show that a persistent pattern of positive overnight and negative daytime returns predicts higher future returns. Bogousslavsky (2021) links the split to differences in margin and lending costs, and Lu et al. (2023) trace night-minus-day returns to the market makers who absorb retail order imbalances near the open. Chinese evidence adds institutional detail: Qiao and Dam (2020) show that overnight returns are on average negative and link them to the T+1 rule, under which shares bought on one day cannot be sold until the next. Gu et al. (2025) show that the lottery-like anomaly in Chinese stocks comes mainly from overnight returns, with stronger effects where retail gambling preference and limits to arbitrage are high. Qiu et al. (2025) find that day-night anomalies concentrate at the open and close, and Jones et al. (2025) find weak stock selection among small retail investors. Studies of overnight returns measure them on all stocks; none conditions on a limit close.
~~~
~~~new
**Overnight and intraday returns.** Kelly and Clark (2011) show for index funds that overnight and intraday returns differ. In U.S. stocks, positive overnight returns are followed by intraday reversals, concentrated among stocks with recent retail attention (Berkman et al., 2012). Aboody et al. (2018) tie overnight persistence to sentiment, Lou et al. (2019) find overnight and intraday continuation with an offsetting cross-period reversal, Akbas et al. (2022) find that persistent positive-overnight, negative-daytime patterns predict higher returns, Bogousslavsky (2021) links the split to margin and lending costs, and Lu et al. (2023) link it to market makers who absorb retail imbalances near the open. In China, overnight returns are negative on average, which Qiao and Dam (2020) link to the T+1 rule that bars selling shares on the day of purchase; the lottery-like anomaly arises mainly overnight (Gu et al., 2025); day-night anomalies concentrate at the open and close (Qiu et al., 2025); and small retail investors show weak stock selection (Jones et al., 2025).
~~~

**E11.** Section 2 multiple testing: merge
~~~old
**Multiple testing and weekly regressions.** Testing many signals raises the bar for each one. Harvey et al. (2016) argue that a new factor needs a *t*-statistic above 3.0. Harvey and Liu (2020) tie the hurdle to a chosen FDR, Chordia et al. (2020) find that multiple-testing thresholds for cross-sectional regressions are near 3.4, and Hou et al. (2020) find that, with microcaps mitigated, 65% of 452 anomalies fail the single-test hurdle of 1.96. Petersen (2009) compares standard-error estimators for panel data, which motivates our alternative clusters, and Gutierrez and Kelley (2008) study weekly returns, the frequency of our regressions. For Vietnam, Huang et al. (2023) find a significant size effect and an earnings-to-price effect. We found no peer-reviewed study of post-limit returns on HOSE.
~~~
~~~new
**Multiple testing and weekly regressions.** Harvey et al. (2016) argue that a new factor needs a *t*-statistic above 3.0, Harvey and Liu (2020) tie the hurdle to a chosen FDR, Chordia et al. (2020) put multiple-testing thresholds for cross-sectional regressions near 3.4, and Hou et al. (2020) find that, with microcaps mitigated, 65% of 452 anomalies fail the single-test hurdle of 1.96. Petersen (2009) compares standard-error estimators for panel data, which motivates our alternative clusters, and Gutierrez and Kelley (2008) study weekly returns, the frequency of our regressions. For Vietnam, Huang et al. (2023) find a size effect and an earnings-to-price effect; we found no peer-reviewed study of post-limit returns on HOSE.
~~~

**E12.** Section 2 gap and hypotheses: single statement of the gap
~~~old
**Gap and hypotheses.** The reviewed studies document the volatility, liquidity, and long-run effects of limits, and the overnight-intraday split for all stocks. Apart from Huang et al. (2001), none combines the two, and none controls for multiple testing or uses the 2025 platform change. Four hypotheses follow. If a limit delays price discovery, a ceiling close predicts a positive next-day abnormal return and a floor close a negative one (H~1~). If the opening auction absorbs the blocked demand, the effect concentrates in the overnight gap (H~2~). If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of similar size that stop short of the limit (H~3~). An investor who buys at the next open earns no positive abnormal return through the fifth trading day (H~4~). The 22 characteristics provide a benchmark for H~1~: a limit effect that survives the procedure that screens every characteristic is more credible than a single large estimate.
~~~
~~~new
**Gap and hypotheses.** These studies compare band regimes, sort stocks by limit exposure, or split overnight and intraday returns for all stocks. Only Huang et al. (2001) link limit hits to the overnight-intraday split, and none controls for multiple testing or uses the 2025 platform change. If a limit delays price discovery, a ceiling close predicts a positive next-day abnormal return and a floor close a negative one (H~1~). If the opening auction absorbs the blocked demand, the effect concentrates in the overnight gap (H~2~). If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of similar size that stop short of the limit (H~3~). An investor who buys at the next open earns no positive abnormal return through the fifth trading day (H~4~). A limit effect that survives the screen applied to all 22 characteristics is more credible than a single large estimate.
~~~

**E13.** Section 3 data source: tighten (delisting caveat kept in Section 7)
~~~old
**Data source.** On 24 September 2026, we downloaded daily open, high, low, close, and volume series for all stocks on the HOSE listing with the vnstock Python library (version 4.0.4), which draws them from Vietcap Securities Joint Stock Company (VCI). A listing file from the same source and date (`r fi(c26(2))` rows, all instrument types) defines the universe and omits stocks delisted before that date. The retrieval returned `r fi(c26(1))` HOSE stock files with daily records through 23 September 2026, and we use the `r c26(4)` trading days from 21 August 2024. Prices are in thousand dong. The vendor does not document corporate-action adjustment, and the files contain no market capitalization, order book, investor type, or news.
~~~
~~~new
**Data source.** On 24 September 2026, we downloaded daily open, high, low, close, and volume series for all HOSE-listed stocks with the vnstock Python library (version 4.0.4; source Vietcap Securities, VCI). A listing file from the same source and date (`r fi(c26(2))` rows, all instrument types) defines the universe. The retrieval returned `r fi(c26(1))` HOSE stock files with records through 23 September 2026, and we use the `r c26(4)` trading days from 21 August 2024. Prices are in thousand dong. The vendor does not document corporate-action adjustment, and the files contain no market capitalization, order book, investor type, or news.
~~~

**E14.** Section 3 sample: tighten
~~~old
**Sample.** We keep the `r nstocks` stocks with at least 95% non-missing closes, which yields `r fi(nsd)` stock-days. The mean daily close-to-close return is `r f(c26(6),3)`%, the median is `r f(c26(8),2)`%, and the standard deviation is `r f(c26(7),2)`%. Liquidity is skewed: dollar volume (price times shares traded; we keep the conventional term although values are in dong) has a median of `r f(c26(9)/1000,1)` billion dong per stock-day and a mean of `r f(c26(10)/1000,1)` billion dong. The stocks span `r c26(11)` two-digit sector codes of the Industry Classification Benchmark, and the largest sector holds `r f(c26(12),0)`% of them.
~~~
~~~new
**Sample.** We keep the `r nstocks` stocks with at least 95% non-missing closes, `r fi(nsd)` stock-days in all. The daily close-to-close return has a mean of `r f(c26(6),3)`%, a median of `r f(c26(8),2)`%, and a standard deviation of `r f(c26(7),2)`%. Dollar volume (price times shares traded, in dong) is skewed, with a median of `r f(c26(9)/1000,1)` billion dong per stock-day and a mean of `r f(c26(10)/1000,1)` billion. The stocks span `r c26(11)` two-digit Industry Classification Benchmark sectors; the largest holds `r f(c26(12),0)`% of them.
~~~

**E15.** Section 3 institutional setting: tighten
~~~old
**Institutional setting.** HOSE sets a daily price limit of 7% around the reference price, which is the previous close on normal trading days (Ho Chi Minh City Securities Corporation [HSC], 2025). On 5 May 2025, HOSE moved to the trading platform of the Korea Exchange (KRX). The band stayed unchanged, but at-the-open and at-the-close orders lost their priority over limit orders in the call auctions that set the opening and closing prices (HSC, 2025; Viet Nam News, 2025). The close defines the event and the open defines the gap, so both auction prices matter here. We treat the 7% band, the tick sizes, and the reference-price rule as assumptions and check the band against the data: `r f(pu(c("6.5% to 6.9%","6.9% to 7.1%")),2)`% of all stock-days fall between +6.5% and +7.1% and `r f(pu(c("-6.9% to -6.5%","-7.1% to -6.9%")),2)`% between −7.1% and −6.5%, against `r f(pu("6.0% to 6.5%"),2)`% between +6.0% and +6.5%, a pile-up consistent with a 7% band.
~~~
~~~new
**Institutional setting.** HOSE sets a daily price limit of 7% around the reference price, the previous close on normal trading days (Ho Chi Minh City Securities Corporation [HSC], 2025). On 5 May 2025, HOSE moved to the trading platform of the Korea Exchange (KRX). The band stayed unchanged, but at-the-open and at-the-close orders lost their priority over limit orders in the opening and closing call auctions (HSC, 2025; Viet Nam News, 2025), whose prices define our events and gaps. Treating the band, tick sizes, and reference-price rule as assumptions, we check the band against the data: `r f(pu(c("6.5% to 6.9%","6.9% to 7.1%")),2)`% of stock-days fall between +6.5% and +7.1% and `r f(pu(c("-6.9% to -6.5%","-7.1% to -6.9%")),2)`% between −7.1% and −6.5%, against `r f(pu("6.0% to 6.5%"),2)`% between +6.0% and +6.5%, a pile-up consistent with a 7% band.
~~~

**E16.** Section 4: tighten notation sentence
~~~old
**Returns and events.** For stock $i$ on trading day $d$, let $C_{i,d}$, $O_{i,d}$, $H_{i,d}$, and $L_{i,d}$ denote the close, open, high, and low prices, and let $R_{i,d}$ denote the close-to-close return,
~~~
~~~new
**Returns and events.** For stock $i$ on trading day $d$, $C_{i,d}$, $O_{i,d}$, $H_{i,d}$, and $L_{i,d}$ are the close, open, high, and low prices, and the close-to-close return is
~~~

**E17.** Section 4: tighten event definition
~~~old
Stock $i$ has a ceiling event on day $d$ if $R_{i,d} \geq 0.065$ and $C_{i,d} = H_{i,d}$, and a floor event if $R_{i,d} \leq -0.065$ and $C_{i,d} = L_{i,d}$. The event window runs from day 61 of the sample, once a 60-day volume history exists, to five days before its end. The market return $R^{\text{mkt}}_{d}$ is the dollar-volume-weighted return across stocks,
~~~
~~~new
A ceiling event has $R_{i,d} \geq 0.065$ and $C_{i,d} = H_{i,d}$, and a floor event has $R_{i,d} \leq -0.065$ and $C_{i,d} = L_{i,d}$. The event window runs from day 61, once a 60-day volume history exists, to five days before the sample end. The market return weights stocks by dollar volume,
~~~

**E18.** Section 4: shorten 'where' clause
~~~old
where $j$ and $l$ run over the stocks with a return on day $d$ and a full 60-day volume history, and $\overline{V}_{j,d}$ is the average dollar volume (Section 3) of stock $j$ over the 60 trading days through day $d$.
~~~
~~~new
where $j$ and $l$ run over stocks with a day-$d$ return and a full 60-day history, and $\overline{V}_{j,d}$ is the mean dollar volume of stock $j$ over the 60 trading days through day $d$.
~~~

**E19.** Section 4 exact hits: tighten
~~~old
**Exact hits.** An exact limit hit is an event whose close $C_{i,d}$ equals the limit price (to within $10^{-6}$ thousand dong),
~~~
~~~new
**Exact hits.** An exact hit is an event whose close equals the limit price (within $10^{-6}$ thousand dong),
~~~

**E20.** Section 4: merge 'where' clause and floating-point note
~~~old
where $\lfloor \cdot \rfloor$ and $\lceil \cdot \rceil$ round down and up, and the tick size $\delta$ is 0.01, 0.05, or 0.10 thousand dong for reference prices $C_{i,d-1}$ (the previous close) below 10, from 10 to below 50, and from 50 thousand dong upward. In computation we add $10^{-9}$ inside $\lfloor \cdot \rfloor$ and subtract it inside $\lceil \cdot \rceil$ to guard against floating-point error. Events whose close differs from the limit price of Equation (3) are near hits; Section 7 explains why this split depends on how the vendor adjusts prices.
~~~
~~~new
where $\lfloor \cdot \rfloor$ and $\lceil \cdot \rceil$ round down and up (after adding and subtracting $10^{-9}$, respectively, against floating-point error), and the tick $\delta$ is 0.01, 0.05, or 0.10 thousand dong for reference prices $C_{i,d-1}$ below 10, from 10 to below 50, and from 50 upward. Other events are near hits (see Section 7 on vendor price adjustment).
~~~

**E21.** Section 4 outcomes: tighten
~~~old
**Outcomes.** For an event of stock $i$ on day $d$, the abnormal return (AR) on day $d+1$ and the cumulative abnormal return (CAR) over days $d+1$ to $d+5$ are
~~~
~~~new
**Outcomes.** The abnormal return (AR) on day $d+1$ and the cumulative abnormal return (CAR) over days $d+1$ to $d+5$ are
~~~

**E22.** Section 4: shorten 'where' clause
~~~old
where $k = 1, \dots, 5$ counts trading days after the event and each $R^{\text{mkt}}_{d+k}$ uses weights through day $d+k$ (Table 1). We split the day-$d+1$ return into the overnight gap $\mathrm{GAP}_{i,d}$ and the intraday return $\mathrm{INTRA}_{i,d}$,
~~~
~~~new
where each $R^{\text{mkt}}_{d+k}$ uses weights through day $d+k$ (Table 1). The day-$d+1$ return splits into the overnight gap and the intraday return,
~~~

**E23.** Section 4: compress benchmark prose
~~~old
and subtract the market counterpart of each component, the same-interval return across stocks weighted with $w_{j,d}$, to obtain abnormal values. Tables 2 to 4 and Figure 2 use these weights, known at the event close, for every interval after the day-$d$ close. A buyer at the next open earns $C_{i,d+5}/O_{i,d+1} - 1$ through day $d+5$, less the buy-and-hold market return $\sum_j w_{j,d}\,(C_{j,d+5}/O_{j,d+1} - 1)$ over the same interval. The control benchmark replaces the market counterpart with the equal-weighted mean same-interval return of control stocks, those with an absolute day-$d$ return below 6.5%, in the event stock's tercile of $\overline{V}_{i,d}$; the tercile cut-offs come from the control stocks on that date, and dates with fewer than 30 control stocks have no benchmark.
~~~
~~~new
and abnormal values subtract the market counterpart of each component, the same-interval return across stocks weighted with $w_{j,d}$, known at the event close. A buyer at the next open earns $C_{i,d+5}/O_{i,d+1} - 1$ less the buy-and-hold market return $\sum_j w_{j,d}\,(C_{j,d+5}/O_{j,d+1} - 1)$. The control benchmark is the equal-weighted mean same-interval return of control stocks (absolute day-$d$ return below 6.5%) in the event stock's tercile of $\overline{V}_{i,d}$ on that date; dates with fewer than 30 control stocks have no benchmark.
~~~

**E24.** Section 4 inference: tighten
~~~old
**Inference.** For a sample of $N$ events $e = 1, \dots, N$, each a stock-day pair $(i, d)$, with outcome $y_e$ (any return defined above), the mean is $\overline{y} = N^{-1}\sum_{e} y_e$, and the cluster-robust variance is
~~~
~~~new
**Inference.** For $N$ events $e$, each a stock-day pair, with outcome $y_e$ and mean $\overline{y} = N^{-1}\sum_{e} y_e$, the cluster-robust variance is
~~~

**E25.** Section 4 inference: merge 'where' clause, compress
~~~old
where $g = 1, \dots, G$ indexes clusters. We cluster by event date, by calendar week (the ISO week of the event date), and by 10-day block (consecutive blocks of ten trading days). The *p*-values with which the four event tests enter the multiple-testing family use Equation (6) with event-date clusters, omit the factor $G/(G-1)$, and take a standard normal reference. The *t*-statistics in Table 1 and the Bonferroni bound below include the factor and use a *t* reference distribution with $G-1$ degrees of freedom. Two-way clustering by date and stock sets the variance to the date-clustered variance plus the stock-clustered variance minus the heteroskedasticity-robust variance $N^{-2}\sum_e (y_e - \overline{y})^2$, each without the factor $G/(G-1)$ and with the sum bounded below at $10^{-12}$ (Cameron et al., 2011). To compare limit closes with near-limit moves, we regress $y_e = \alpha + \beta D_e + u_e$, where $D_e = 1$ for limit closes and $D_e = 0$ for the comparison group, and $u_e$ is the error term. We cluster the standard error of $\hat{\beta}$ by event date with the small-sample factor $G/(G-1) \cdot (N-1)/(N-2)$, where $N$ and $G$ now count the stock-days and dates in the regression sample (the HC1 option of the R package *sandwich*).
~~~
~~~new
where $g = 1, \dots, G$ indexes clusters: event dates, ISO calendar weeks, or blocks of ten consecutive trading days. The family *p*-values of the four event tests use Equation (6) with event-date clusters, omit $G/(G-1)$, and take a normal reference; Table 1 *t*-statistics include the factor and use a *t* reference with $G-1$ degrees of freedom. Two-way clustering by date and stock follows Cameron et al. (2011), without the factor and with the variance bounded below at $10^{-12}$. Table 3 reports $\hat{\beta}$ from $y_e = \alpha + \beta D_e + u_e$, where $D_e = 1$ for limit closes, with date-clustered HC1 standard errors (R package *sandwich*).
~~~

**E26.** Section 4 characteristics: compress
~~~old
**Characteristics.** We form cross-sections every five trading days, on trading days 120, 125, and so on to day 510, which gives $T = 79$ formation dates that we call weeks $\tau = 1, \dots, T$ (they differ from the calendar weeks used for clustering), each followed by a non-overlapping five-day holding period. The first formation date is the 120th trading day, so that every lookback is complete. At the end of each week we rank-normalize each characteristic $x_{i,\tau}$ across the $n_\tau$ stocks with complete data: returns, opens, and closes on all 115 days of the longest lookback, which includes the formation day; trades on at least 50 of the last 60 days; and returns on the next five days. With ties at average ranks, the score is $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, where $\Phi^{-1}$ is the inverse standard normal distribution function. The outcome $y_{i,\tau}$ is the compounded return of stock $i$ over the next five trading days minus the average of the same five-day returns across these stocks, weighted by $\overline{V}$ at the end of the week. We run Fama and MacBeth (1973) regressions of $y_{i,\tau}$ on $z_{i,\tau}$,
~~~
~~~new
**Characteristics.** We form cross-sections on trading days 120 (so that every lookback is complete), 125, and so on to 510: $T = 79$ formation weeks $\tau$, each followed by a non-overlapping five-day holding period. Each week we rank-normalize each characteristic $x_{i,\tau}$ across the $n_\tau$ stocks with complete data (all 115 days of the longest lookback, trades on 50 of the last 60 days, and next-five-day returns) as $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, with ties at average ranks and $\Phi^{-1}$ the inverse standard normal distribution function. The outcome $y_{i,\tau}$ is the stock's compounded return over the next five trading days minus the $\overline{V}$-weighted average five-day return of these stocks. The Fama and MacBeth (1973) regressions are
~~~

**E27.** Section 4: merge 'where' clause; Appendix A defines the characteristics
~~~old
where $a_\tau$ is the weekly intercept and $\varepsilon_{i,\tau}$ the residual. We compute the *t*-statistic of $\hat{\gamma}$ with Newey and West (1987) standard errors with four lags, Bartlett weights, and no prewhitening, and its *p*-value from a *t* distribution with $T - 1 = 78$ degrees of freedom. The characteristics cover momentum and reversal (5-day, 20-day, 3-month, 6-month, and idiosyncratic momentum), risk (volatility, idiosyncratic volatility, beta, downside deviation, Parkinson (1980) range volatility, the maximum daily return (MAX; Bali et al., 2011), the minimum daily return (MIN), skewness, and kurtosis), liquidity and volume (Amihud (2002) illiquidity, log dollar volume, dollar-volume and volume ratios, and the Corwin and Schultz (2012) spread), and intraday behavior (mean overnight return, mean intraday return, and the frequency of moves of 6.5% or more). Appendix A defines all 22 characteristics and their lookback windows. We also report the long–short return spread between the extreme quintiles of each characteristic, before and after a cost of 25 basis points per unit of traded value. The minimum detectable effect (MDE) on $\hat{\gamma}$ at 80% power and a 5% two-sided level is $\text{MDE} = (1.96 + 0.84)\, \widehat{\text{SE}}(\hat{\gamma}) \approx 2.8\, \widehat{\text{SE}}(\hat{\gamma})$, where $\widehat{\text{SE}}$ is the Newey–West standard error.
~~~
~~~new
with weekly intercept $a_\tau$. The *t*-statistic of $\hat{\gamma}$ uses Newey and West (1987) standard errors (four lags, Bartlett weights, no prewhitening) and 78 degrees of freedom. Appendix A defines the 22 momentum, reversal, risk, liquidity, volume, and intraday characteristics. We also report long–short spreads between the extreme quintiles, before and after a cost of 25 basis points per unit of traded value. The minimum detectable effect at 80% power and a 5% two-sided level is $\text{MDE} = (1.96 + 0.84)\, \widehat{\text{SE}}(\hat{\gamma}) \approx 2.8\, \widehat{\text{SE}}(\hat{\gamma})$, with $\widehat{\text{SE}}$ the Newey–West standard error.
~~~

**E28.** Section 4 multiplicity: tighten
~~~old
**Multiplicity and survival.** The family has $m = 26$ tests: 22 characteristics and the ceiling and floor tests at the two horizons of Equation (4). Order the *p*-values as $p_{(1)} \leq \dots \leq p_{(m)}$. For rank $r = 1, \dots, m$, the Benjamini–Hochberg (BH) adjusted *p*-value is
~~~
~~~new
**Multiplicity and survival.** The family has $m = 26$ tests: 22 characteristics and the ceiling and floor tests at the two horizons of Equation (4). With *p*-values ordered as $p_{(1)} \leq \dots \leq p_{(m)}$, the Benjamini–Hochberg (BH) adjusted *p*-value at rank $r$ is
~~~

**E29.** Section 4 survival rule: compress; Bonferroni definition moved to Section 5
~~~old
and we also report Holm (1979) adjustments and the hurdle of |*t*| = 3 of Harvey et al. (2016). A test survives if three conditions hold: $\tilde{p} < 0.05$, which controls the FDR at 5%; the signs in the discovery half (the first 39 weeks for characteristics, events up to the median event date for events) and in the confirmation half agree; and the confirmation-half |*t*| exceeds 1.96. Lookbacks overlap the discovery half, so the confirmation half is not a strict hold-out. Under a Bonferroni correction at 5%, all four event tests survive in families of up to $m_{\text{max}} = \lfloor 0.05 / p_{\text{max}} \rfloor$ tests, where $p_{\text{max}}$ is the largest of the four event-test *p*-values computed with the factor $G/(G-1)$ and a *t* reference, separately for event-date and calendar-week clusters. The weekly regressions start on the 120th trading day and the event window on the 61st, so the two parts of the family cover different spans.
~~~
~~~new
and we also report Holm (1979) adjustments and the |*t*| = 3 hurdle of Harvey et al. (2016). A test survives if $\tilde{p} < 0.05$, which controls the FDR at 5%; if its signs agree in the discovery half (the first 39 weeks, or events up to the median event date) and the confirmation half; and if its confirmation-half |*t*| exceeds 1.96. Lookbacks overlap the discovery half, so the confirmation half is not a strict hold-out, and the weekly regressions (from day 120) and event window (from day 61) cover different spans.
~~~

**E30.** Section 4 analysis plan: compress departures and exploratory list
~~~old
**Analysis plan.** We fixed the family, estimators, multiplicity control, and survival rule in a written analysis plan before computing results. A version-control time stamp shows that the plan predates the first analysis code, but no external registry holds it, and we had examined related data in earlier work, so the plan gives no independent confirmation. We departed from the plan in four ways. The plan was ambiguous about the second horizon (days *d*+2 to *d*+5 or *d*+1 to *d*+5), and we implemented the second reading. We split the event half-samples at the median event date instead of at weeks 39 and 40. We report quintile spreads instead of deciles. We did not run the plan's same-stock control and multivariate model. Analyses added after the first results are exploratory: the decomposition, the next-open returns, the control group, the comparison with sub-limit moves, exact hits, two-way clustering, subsamples, the volume and prior-return terciles, the platform-change split, and the outlier exclusion. The tests of H~2~ to H~4~ therefore rest on exploratory analyses. We also screened several candidate ideas on the same data before choosing this one, so effect-size estimates may overstate the true effect.
~~~
~~~new
**Analysis plan.** We fixed the family, estimators, multiplicity control, and survival rule in a written analysis plan before computing results. A version-control time stamp dates the plan before the first analysis code, but no external registry holds it and we had examined related data in earlier work, so it gives no independent confirmation. We departed from it by reading its ambiguous second horizon as days *d*+1 to *d*+5 (not *d*+2 to *d*+5), splitting event halves at the median event date (not weeks 39 and 40), reporting quintile rather than decile spreads, and omitting its same-stock control and multivariate model. Analyses added after the first results are exploratory, and the tests of H~2~ to H~4~ rest on them: the decomposition, next-open returns, control group, sub-limit comparison, exact hits, two-way clustering, subsamples, terciles, platform split, and outlier exclusion. We also screened several candidate ideas on the same data before choosing this one, so effect sizes may be overstated.
~~~

**E31.** Section 5 opening: tighten
~~~old
The event sample holds `r fi(ev("ceiling","t+1","n_events"))` ceiling events on `r fi(ev("ceiling","t+1","n_dates"))` dates and `r fi(ev("floor","t+1","n_events"))` floor events on `r fi(ev("floor","t+1","n_dates"))` dates, so limit closes cluster in market episodes, and we report standard errors that allow for dependence across dates, weeks, 10-day blocks, and stocks.
~~~
~~~new
The event sample holds `r fi(ev("ceiling","t+1","n_events"))` ceiling events on `r fi(ev("ceiling","t+1","n_dates"))` dates and `r fi(ev("floor","t+1","n_events"))` floor events on `r fi(ev("floor","t+1","n_dates"))` dates. Limit closes cluster in market episodes, so our standard errors allow dependence across dates, weeks, 10-day blocks, and stocks.
~~~

**E32.** Section 5 characteristics: one power caveat
~~~old
Figure 1 plots the *t*-statistics of the 22 slopes $\hat{\gamma}$ in Equation (7): none reaches |*t*| = 3, and none survives the BH control. The largest full-sample |*t*| is `r f(max(abs(Z$t_nw)),2)`, for 3-month and idiosyncratic momentum (confirmation-half *t* of `r f(Z$t_conf[Z$characteristic=="MOM3M"],2)` and `r f(Z$t_conf[Z$characteristic=="IMOM"],2)`). Volatility has *t* = `r f(Z$t_nw[Z$characteristic=="VOL"],2)`, idiosyncratic volatility `r f(Z$t_nw[Z$characteristic=="IVOL"],2)`, and MAX `r f(Z$t_nw[Z$characteristic=="MAX"],2)`. After a cost of 25 basis points per unit of traded value, `r sum(Z$quintile_net25_pct < 0)` of the 22 long–short quintile spreads are negative. Power is limited: with 79 weekly cross-sections, the MDE at 80% power is `r f(min(C14$mde80_pct_per_week),2)` to `r f(max(C14$mde80_pct_per_week),2)` percentage points per week per standard deviation, and no characteristic reaches |*t*| = 3 with eight Newey–West lags (largest |*t*| `r f(max(abs(C14$t_lag8)),2)`). The null excludes only large effects. Dropping the least liquid 20% of stocks leaves the largest |*t*| at `r f(max(abs(Z$t_excl_illiq), na.rm = TRUE),2)`.
~~~
~~~new
Figure 1 plots the *t*-statistics of the 22 slopes $\hat{\gamma}$ in Equation (7): none reaches |*t*| = 3 in any sample or 1.96 in the full sample, and none survives the BH control. The largest full-sample |*t*| is `r f(max(abs(Z$t_nw)),2)`, for 3-month and idiosyncratic momentum (confirmation-half *t* of `r f(Z$t_conf[Z$characteristic=="MOM3M"],2)` and `r f(Z$t_conf[Z$characteristic=="IMOM"],2)`). After the 25-basis-point cost, `r sum(Z$quintile_net25_pct < 0)` of the 22 long–short quintile spreads are negative. With 79 weekly cross-sections, the MDE at 80% power is `r f(min(C14$mde80_pct_per_week),2)` to `r f(max(C14$mde80_pct_per_week),2)` percentage points per week per standard deviation, so the null excludes only large effects. With eight Newey–West lags the largest |*t*| is `r f(max(abs(C14$t_lag8)),2)`, and dropping the least liquid 20% of stocks leaves it at `r f(max(abs(Z$t_excl_illiq), na.rm = TRUE),2)`.
~~~

**E33.** Section 5: drop literature comparison repeated in Section 2 and Table 5
~~~old
The hurdles of Harvey et al. (2016) and Chordia et al. (2020) and the replication failures in Hou et al. (2020) predict few survivors; here no characteristic reaches 1.96 in the full sample. Huang et al. (2023) find a size effect and an earnings-to-price effect in Vietnam, but our files contain no market capitalization or accounting data, so we cannot test those two signals and our null does not contradict theirs. Two features of the setting can produce the null. The sample is short, so a premium of a tenth of a percentage point per week stays below the MDE, and daily limits censor the highs and lows that range-based characteristics use. We cannot tell these explanations apart and draw no conclusion about market efficiency from the null.
~~~
~~~new
Without market capitalization or accounting data, we cannot test the size and earnings-to-price effects that Huang et al. (2023) find in Vietnam, so our null does not contradict theirs. A short sample, which leaves a premium of a tenth of a percentage point per week below the MDE, and limits that censor the highs and lows of range-based characteristics can each produce the null, and we draw no conclusion about market efficiency from it.
~~~

**E34.** Figure 1 caption: labels defined in Appendix A
~~~old
fig.cap="Figure 1. *t*-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half (first 39 weeks), and the confirmation half. Labels: REV1W and REV1M, 5-day and 20-day returns; MOM3M and MOM6M, 3- and 6-month momentum; IMOM, idiosyncratic momentum; VOL and IVOL, total and idiosyncratic volatility; BETA, market beta; DOWNVOL, downside deviation; RANGEVOL, Parkinson range volatility; MAX and MIN, maximum and minimum daily return; SKEW and KURT, skewness and kurtosis; AMIHUD, Amihud illiquidity; LNDVOL, log dollar volume; DVOLCHG and TURNCHG, dollar-volume and volume ratios; CSSPREAD, Corwin and Schultz spread; OVERNIGHT and INTRADAY, mean overnight and intraday returns; LIMITFREQ, frequency of moves of 6.5% or more. Dashed lines mark |*t*| = 1.96 and dotted lines mark |*t*| = 3. Characteristics are ordered by absolute full-sample *t*."
~~~
~~~new
fig.cap="Figure 1. *t*-statistics of the Fama and MacBeth regressions for the 22 characteristics in the full sample, the discovery half (first 39 weeks), and the confirmation half, ordered by absolute full-sample *t*. Appendix A defines the labels. Dashed lines mark |*t*| = 1.96 and dotted lines |*t*| = 3."
~~~

**E35.** Section 5 Table 1 text: tighten
~~~old
Table 1 reports the event tests. Stocks that close at the ceiling earn a market-adjusted return of `r f(ev("ceiling","t+1","mean_ar_pct"),2)`% on day *d*+1 and `r f(ev("ceiling","t+1..t+5","mean_ar_pct"),2)`% over days *d*+1 to *d*+5. Stocks that close at the floor earn `r f(ev("floor","t+1","mean_ar_pct"),2)`% and `r f(ev("floor","t+1..t+5","mean_ar_pct"),2)`%. All four tests survive the BH control (Equation (8); adjusted *p*-values of at most `r formatC(max(FAM$p_bh[23:26]), format = "f", digits = 4)`). They keep their signs in both halves, and the confirmation-half |*t*| exceeds 1.96. Clustering by calendar week or 10-day block, with a *t* reference distribution, leaves all four significant. The floor five-day test clears the confirmation criterion by the smallest margin (*t* = `r f(c18("floor","t+1..t+5","calendar week","t_second_half"),2)` with week clusters), and all four tests survive the rule re-applied with week-clustered statistics.
~~~
~~~new
Table 1 reports the event tests. Ceiling closes earn a market-adjusted return of `r f(ev("ceiling","t+1","mean_ar_pct"),2)`% on day *d*+1 and `r f(ev("ceiling","t+1..t+5","mean_ar_pct"),2)`% over days *d*+1 to *d*+5, and floor closes earn `r f(ev("floor","t+1","mean_ar_pct"),2)`% and `r f(ev("floor","t+1..t+5","mean_ar_pct"),2)`%. All four tests survive the BH control (Equation (8); adjusted *p*-values of at most `r formatC(max(FAM$p_bh[23:26]), format = "f", digits = 4)`), keep their signs in both halves, and exceed |*t*| = 1.96 in the confirmation half. Clustering by calendar week or 10-day block, with a *t* reference, leaves all four significant. The floor five-day test clears the confirmation criterion by the smallest margin (*t* = `r f(c18("floor","t+1..t+5","calendar week","t_second_half"),2)` with week clusters), and all four tests survive the rule re-applied with week-clustered statistics.
~~~

**E36.** Section 5 horizons: tighten, drop meta-joiner and repeated Kim-Rhee comparison
~~~old
For ceilings, the five-day result comes from the first day. Over days *d*+2 to *d*+5 the ceiling return is `r f(c18("ceiling","t+2..t+5","event date","mean_pct"),2)`% (*t* = `r f(c18("ceiling","t+2..t+5","event date","t"),2)`). After floor closes, days *d*+2 to *d*+5 add `r f(c18("floor","t+2..t+5","event date","mean_pct"),2)`% (*t* = `r f(c18("floor","t+2..t+5","event date","t"),2)`), but the confirmation-half week-clustered *t* is `r f(c18("floor","t+2..t+5","calendar week","t_second_half"),2)`. If the second horizon were days *d*+2 to *d*+5, the ceiling test would fail and the floor test would fail the confirmation criterion. Ceiling closes carry a one-day effect; floor closes carry a one-day effect plus some later drift. The ceiling result fits the delayed price discovery that Kim and Rhee (1997) find support for in Tokyo, because the abnormal return arrives after the limit day. These tests support H~1~: limit closes predict the next day's abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon. Table 2 tests when in the day that information arrives (H~2~).
~~~
~~~new
For ceilings, the five-day result comes from the first day: over days *d*+2 to *d*+5 the ceiling return is `r f(c18("ceiling","t+2..t+5","event date","mean_pct"),2)`% (*t* = `r f(c18("ceiling","t+2..t+5","event date","t"),2)`). After floor closes, days *d*+2 to *d*+5 add `r f(c18("floor","t+2..t+5","event date","mean_pct"),2)`% (*t* = `r f(c18("floor","t+2..t+5","event date","t"),2)`), but the confirmation-half week-clustered *t* is `r f(c18("floor","t+2..t+5","calendar week","t_second_half"),2)`. With days *d*+2 to *d*+5 as the second horizon, the ceiling test would fail and the floor test would fail the confirmation criterion. Ceiling closes carry a one-day effect, and floor closes a one-day effect plus some later drift. These tests support H~1~: limit closes predict the next day's abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon.
~~~

**E37.** Table 1 caption: shorten
~~~old
caption = "Table 1. Market-adjusted returns after ceiling and floor closes. Mean returns are in percent. *t* (date), *t* (week), and *t* (10-day) use clusters by event date, calendar week, and 10-day block, each with the factor *G*/(*G* − 1), where *G* is the number of clusters; we judge all three against a *t* distribution with *G* − 1 degrees of freedom. *t* (halves) gives week-clustered statistics for the first and second half of event dates. Events require complete returns for days *d*+1 to *d*+5."
~~~
~~~new
caption = "Table 1. Market-adjusted returns (percent) after ceiling and floor closes. *t* (date), *t* (week), and *t* (10-day) cluster by event date, calendar week, and 10-day block, with the factor *G*/(*G* − 1) for *G* clusters and a *t* reference with *G* − 1 degrees of freedom. *t* (halves) gives week-clustered statistics for the first and second half of event dates. Events require complete returns for days *d*+1 to *d*+5."
~~~

**E38.** Section 5 decomposition: drop mechanism and literature repeated in readings paragraph and Table 5
~~~old
Table 2 decomposes the next-day return as in Equation (5). After a ceiling close the overnight gap is `r f(c16("Ceiling all","gap_mkt"),2)`% (two-way-clustered *t* = `r f(c16("Ceiling all","gap_mkt","t_twoway"),1)`), and the intraday return is `r f(c16("Ceiling all","intraday_mkt"),2)`% (*t* = `r f(c16("Ceiling all","intraday_mkt","t_twoway"),1)`). The close-to-close effect is positive because the gap exceeds the giveback, and the session reverses about `r f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0)`% of the gap. The decomposition places the effect in the opening auction, as H~2~ predicts. A stock that closes at its ceiling may carry a queue of unfilled buy orders into the night, the mechanism that delayed price discovery assumes (Kim & Rhee, 1997). Those orders and any overnight news set the opening price, and traders reverse part of the move during the session, which suggests that part of the opening price reflects transient demand. The signs match the overnight gain and intraday reversal in Berkman et al. (2012) and Huang et al. (2001); Table 5 sets out the other comparisons.
~~~
~~~new
Table 2 decomposes the next-day return as in Equation (5). After a ceiling close the overnight gap is `r f(c16("Ceiling all","gap_mkt"),2)`% (two-way-clustered *t* = `r f(c16("Ceiling all","gap_mkt","t_twoway"),1)`) and the intraday return is `r f(c16("Ceiling all","intraday_mkt"),2)`% (*t* = `r f(c16("Ceiling all","intraday_mkt","t_twoway"),1)`): the session reverses about `r f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0)`% of the gap, and the close-to-close effect is positive because the gap exceeds the giveback. The effect sits in the opening auction, as H~2~ predicts. Unfilled buy orders carried into the night and any overnight news set the opening price, and the intraday reversal suggests that part of that price reflects transient demand.
~~~

**E39.** Section 5 floor and near hits: tighten; keep vendor-adjustment reading
~~~old
After a floor close the gap is `r f(c16("Floor all","gap_mkt"),2)`% (*t* = `r f(c16("Floor all","gap_mkt","t_twoway"),1)`) and the intraday return is a weak reversal of `r f(c16("Floor all","intraday_mkt"),2)`%. The pattern holds for exact limit hits, where the ceiling gap is `r f(c11("Ceiling: exact tick-rule hit","gap_mkt"),2)`%, and for the first day of a streak of exact hits, where it is `r f(c11("Ceiling: first day of streak (exact)","gap_mkt"),2)`%. Near hits show a smaller gap (`r f(c11("Ceiling: near-hit (rule-based, not exact)","gap_mkt"),2)`%) and no significant intraday return. Their median day-*d* return is `r f(c27(8),2)`% against `r f(c27(7),2)`% for exact hits, and `r f(c27(9),0)`% of their closes are not multiples of the tick size, which points to later price adjustment by the vendor rather than to closes below the limit. The split is therefore weighted toward higher-priced stocks, where the tick is coarser, and we do not read the difference as a gradient toward the limit. The gap appears in both halves of the sample, on days when the stock stayed locked at one price from open to close, and, for ceilings, in each tercile of 60-day average dollar volume across all stocks (`r f(c16("Ceiling liquidity tercile 3","gap_mkt"),2)`% in the most liquid). Against same-date control stocks of similar liquidity the ceiling gap is `r f(c11("Ceiling: rule-based","gap_ctrl"),2)`% and the floor close-to-close return is `r f(c16("Floor all","cc1_ctrl"),2)`%, so the floor effect depends on the benchmark. Floor events cluster on market-wide down days (only `r fi(c16("Floor excluding market-crash days (market < -2%)","gap_mkt","n"))` of `r fi(c16("Floor all","gap_mkt","n"))` remain when we drop days on which the market fell more than 2%), and the floor gap is not significant in the least liquid tercile (*t* = `r f(c16("Floor liquidity tercile 1","gap_mkt","t_twoway"),1)`).
~~~
~~~new
After a floor close the gap is `r f(c16("Floor all","gap_mkt"),2)`% (*t* = `r f(c16("Floor all","gap_mkt","t_twoway"),1)`) and the intraday return is a weak reversal of `r f(c16("Floor all","intraday_mkt"),2)`%. The ceiling gap holds for exact limit hits (`r f(c11("Ceiling: exact tick-rule hit","gap_mkt"),2)`%) and for the first day of a streak of exact hits (`r f(c11("Ceiling: first day of streak (exact)","gap_mkt"),2)`%). Near hits show a smaller gap (`r f(c11("Ceiling: near-hit (rule-based, not exact)","gap_mkt"),2)`%) and no significant intraday return, but their median day-*d* return is `r f(c27(8),2)`% against `r f(c27(7),2)`% for exact hits, and `r f(c27(9),0)`% of their closes are not multiples of the tick size. This points to later price adjustment by the vendor, concentrated in higher-priced stocks with coarser ticks, rather than to closes below the limit, so we do not read the difference as a gradient toward the limit. The gap appears in both halves of the sample, on days locked at one price from open to close, and, for ceilings, in each tercile of 60-day average dollar volume (`r f(c16("Ceiling liquidity tercile 3","gap_mkt"),2)`% in the most liquid). Against same-date controls the ceiling gap is `r f(c11("Ceiling: rule-based","gap_ctrl"),2)`% and the floor close-to-close return `r f(c16("Floor all","cc1_ctrl"),2)`%, so the floor effect depends on the benchmark. Floor events cluster on market-wide down days (`r fi(c16("Floor excluding market-crash days (market < -2%)","gap_mkt","n"))` of `r fi(c16("Floor all","gap_mkt","n"))` remain without days on which the market fell more than 2%), and the floor gap is not significant in the least liquid tercile (*t* = `r f(c16("Floor liquidity tercile 1","gap_mkt","t_twoway"),1)`).
~~~

**E40.** Section 5 next-open buyer: tighten; drop giveback figure that repeats the intraday mean
~~~old
An outside buyer cannot capture the close-to-close continuation. A buyer who wants a stock at its ceiling joins a queue at the close, so the first price such a buyer can obtain is the next open, which already contains the gap. From that open the ceiling return is `r f(c11("Ceiling: rule-based","f5o_mkt"),2)`% through the fifth close against the market (*t* = `r f(c11("Ceiling: rule-based","f5o_mkt","t_twoway"),1)`) and `r f(c11("Ceiling: rule-based","f5o_ctrl"),2)`% against same-date controls (*t* = `r f(c11("Ceiling: rule-based","f5o_ctrl","t_twoway"),1)`). A holder who sells at the next open instead of the close avoids an average giveback of `r f(abs(c16("Ceiling all","intraday_mkt")),2)` percentage points. These figures, which support H~4~, use quoted prices and ignore achievable fills: `r fi(c16("Ceiling locked all day","gap_mkt","n"))` ceiling events were locked at one price all day, and some of these stocks opened at the limit the next day, where a buyer may be rationed. After floor closes, prices fall a further `r f(abs(c11("Floor: rule-based","f5o_mkt")),2)`% from the next open to the fifth close against the market (*t* = `r f(c11("Floor: rule-based","f5o_mkt","t_twoway"),1)`; Table 2), which is not significant at the 5% level.
~~~
~~~new
An outside buyer cannot capture the close-to-close continuation: a buyer who wants a stock at its ceiling joins a queue at the close, so the first obtainable price is the next open, which already contains the gap. From that open the ceiling return through the fifth close is `r f(c11("Ceiling: rule-based","f5o_mkt"),2)`% against the market (*t* = `r f(c11("Ceiling: rule-based","f5o_mkt","t_twoway"),1)`) and `r f(c11("Ceiling: rule-based","f5o_ctrl"),2)`% against same-date controls (*t* = `r f(c11("Ceiling: rule-based","f5o_ctrl","t_twoway"),1)`), which supports H~4~; a holder who sells at the next open avoids the intraday giveback. These figures use quoted prices and ignore achievable fills: `r fi(c16("Ceiling locked all day","gap_mkt","n"))` ceiling events were locked at one price all day, and some of these stocks opened at the limit the next day, where a buyer may be rationed. After floor closes, prices fall a further `r f(abs(c11("Floor: rule-based","f5o_mkt")),2)`% from the next open to the fifth close against the market (*t* = `r f(c11("Floor: rule-based","f5o_mkt","t_twoway"),1)`), which is not significant at the 5% level.
~~~

**E41.** Table 2 caption: shorten
~~~old
caption = "Table 2. Next-day abnormal returns by component and sample. Entries are mean abnormal returns in percent with two-way-clustered *t*-statistics in parentheses. Benchmarks are the dollar-volume-weighted market (weights lagged to day *d*) or same-date control stocks (absolute day-*d* return below 6.5%) in the same tercile of 60-day average dollar volume (Section 4). Open to day *d*+5 is the return from the day-*d*+1 open to the day-*d*+5 close. Exact hits and near hits are defined in Section 4. Crash days are event days on which the market return of Equation (2) is below −2%. Close-to-close need not equal the sum of the two components because returns compound. Events are the stock-days that meet the event definition in Section 4 and have the stated return."
~~~
~~~new
caption = "Table 2. Next-day abnormal returns (percent) by component and sample, with two-way-clustered *t*-statistics in parentheses. Benchmarks are the dollar-volume-weighted market (weights lagged to day *d*) or same-date control stocks in the same liquidity tercile (Section 4). Open to day *d*+5 runs from the day-*d*+1 open to the day-*d*+5 close. Crash days have a market return (Equation (2)) below −2%. Close-to-close need not equal the sum of the components because returns compound."
~~~

**E42.** Section 5 Figure 2 text: tighten
~~~old
Figure 2 plots the three next-day measures against the size of the day-*d* move. Inside the band the close-to-close relation is negative: larger rises are followed by lower returns, a short-term reversal. At the limit the relation breaks, and the overnight gap jumps up at the ceiling and down at the floor.
~~~
~~~new
Figure 2 plots the three next-day measures against the size of the day-*d* move. Inside the band the close-to-close relation is negative, a short-term reversal. At the limit the relation breaks, and the overnight gap jumps up at the ceiling and down at the floor.
~~~

**E43.** Figure 2 caption: shorten
~~~old
fig.cap="Figure 2. Next-day abnormal return by the size of the day-*d* move, split into overnight gap, intraday return, and close-to-close return. Circles are 1-percentage-point bins of day-*d* returns inside the band, triangles are ceiling and floor events (Section 4), and squares are other moves of 6.5% to 10% in absolute value (moves beyond 10% are omitted). Bars show 95% confidence intervals clustered by date with a normal reference and no small-sample factor. Market weights are lagged to day *d*, and the figure uses all event days up to the second-to-last trading day."
~~~
~~~new
fig.cap="Figure 2. Next-day abnormal return (overnight gap, intraday, and close-to-close) by the size of the day-*d* move. Circles are 1-percentage-point bins inside the band, triangles are ceiling and floor events, and squares are other moves of 6.5% to 10% in absolute value. Bars show 95% confidence intervals clustered by date (normal reference, no small-sample factor). Market weights are lagged to day *d*; the figure uses event days up to the second-to-last trading day."
~~~

**E44.** Section 5 Table 3 text: tighten
~~~old
Table 3 quantifies the break. Ceiling closers have a gap `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),2)` percentage points larger than stocks that rose 5% to 6.5% (*t* = `r f(c17("ceiling vs 5-6.5% up","gap_mkt","t_cluster"),1)`) and an intraday return `r f(abs(c17("ceiling vs 5-6.5% up","intraday_mkt","diff_pct")),2)` points lower. Floor closers have a gap `r f(abs(c17("floor vs 5-6.5% down","gap_mkt","diff_pct")),2)` points lower than stocks that fell 5% to 6.5% (*t* = `r f(c17("floor vs 5-6.5% down","gap_mkt","t_cluster"),1)`). The event rule requires a close at the day's high, so we repeat the comparison with stocks that also closed at their high (low). The ceiling gap is then `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","diff_pct"),2)` points larger (*t* = `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","t_cluster"),1)`) and the floor gap `r f(abs(c23("floor vs 5-6.5% down, close = low","gap_mkt","diff_pct")),2)` points lower, so a strong close does not explain the contrast, which supports H~3~. Comparisons with 3% to 5% moves give the same result: the ceiling gap exceeds that of 3% to 5% risers by `r f(c17("ceiling vs 3-5% up","gap_mkt","diff_pct"),2)` percentage points, and the floor gap falls short of that of 3% to 5% fallers by `r f(abs(c17("floor vs 3-5% down","gap_mkt","diff_pct")),2)` points. The comparison is an association around a rule-based threshold. We make no regression-discontinuity claim: the design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.
~~~
~~~new
Table 3 quantifies the break. Ceiling closers have a gap `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),2)` percentage points larger than stocks that rose 5% to 6.5% (*t* = `r f(c17("ceiling vs 5-6.5% up","gap_mkt","t_cluster"),1)`) and an intraday return `r f(abs(c17("ceiling vs 5-6.5% up","intraday_mkt","diff_pct")),2)` points lower. Floor closers have a gap `r f(abs(c17("floor vs 5-6.5% down","gap_mkt","diff_pct")),2)` points lower than stocks that fell 5% to 6.5% (*t* = `r f(c17("floor vs 5-6.5% down","gap_mkt","t_cluster"),1)`). Because the event rule requires a close at the day's high (low), we repeat the comparison with stocks that also closed there. The ceiling gap is then `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","diff_pct"),2)` points larger (*t* = `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","t_cluster"),1)`) and the floor gap `r f(abs(c23("floor vs 5-6.5% down, close = low","gap_mkt","diff_pct")),2)` points lower, so a strong close does not explain the contrast, which supports H~3~. Against 3% to 5% moves, the ceiling gap is `r f(c17("ceiling vs 3-5% up","gap_mkt","diff_pct"),2)` percentage points larger and the floor gap `r f(abs(c17("floor vs 3-5% down","gap_mkt","diff_pct")),2)` points lower. The comparison is an association around a rule-based threshold, and we make no regression-discontinuity claim: the design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.
~~~

**E45.** Table 3 caption: shorten
~~~old
caption = "Table 3. Differences in next-day abnormal returns between limit closes and stocks that moved 3–5% or 5–6.5% in the same direction without closing at the limit. Entries are differences in percentage points with date-clustered *t*-statistics in parentheses. Returns are market-adjusted with lagged weights."
~~~
~~~new
caption = "Table 3. Differences in next-day abnormal returns (percentage points) between limit closes and same-direction moves of 3–5% or 5–6.5% that did not close at the limit, with date-clustered *t*-statistics in parentheses. Returns are market-adjusted with lagged weights."
~~~

**E46.** Section 5 readings: compress
~~~old
Three readings fit the pattern, and our data do not separate them. (1) Demand or supply that the limit blocked on day *d* clears at the next opening, the delayed price discovery of Kim and Rhee (1997). (2) Stocks that reach a limit carry news and retail attention, which persist overnight and produce the overnight gain and intraday reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit. (3) The opening call auction overshoots and corrects part of the move within the day. The sample has no announcement data, no order book, and no stock-days without a limit, so we run two partial checks. First, the ceiling gap rises with day-*d* volume relative to the prior 60-day mean (`r f(c24("Ceiling","volume",1,"gap_mkt"),2)`%, `r f(c24("Ceiling","volume",2,"gap_mkt"),2)`% and `r f(c24("Ceiling","volume",3,"gap_mkt"),2)`% across terciles) and with the prior 20-day return of the stock (`r f(c24("Ceiling","prior 20",1,"gap_mkt"),2)`%, `r f(c24("Ceiling","prior 20",2,"gap_mkt"),2)`% and `r f(c24("Ceiling","prior 20",3,"gap_mkt"),2)`%). The gap is larger where the attention and news proxies are higher, which fits reading (2) as well as reading (1), and it stays positive and significant in the lowest tercile of each proxy (*t* = `r f(c24("Ceiling","volume",1,"gap_mkt","t_twoway"),1)` and `r f(c24("Ceiling","prior 20",1,"gap_mkt","t_twoway"),1)`). For floors the gap moves from `r f(c24("Floor","volume",1,"gap_mkt"),2)`% to `r f(c24("Floor","volume",3,"gap_mkt"),2)`% across volume terciles and is not monotone in the prior return, so the attention reading does not carry over. Second, the comparison with stocks that closed at their high removes selection on the shape of the close but not selection on news. The intraday giveback fits readings (2) and (3) at least as well as a permanent price-discovery story. We use "break at the limit" as a description and treat delayed price discovery as one hypothesis. Cho et al. (2003) find, and Chen et al. (2024) predict, that prices accelerate toward a limit on the limit day (the magnet effect); testing this needs intraday prices, which we lack.
~~~
~~~new
Three readings fit the pattern, and our data do not separate them: (1) demand or supply that the limit blocked on day *d* clears at the next opening, the delayed price discovery of Kim and Rhee (1997); (2) news and retail attention persist overnight and produce the overnight gain and intraday reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit; and (3) the opening auction overshoots and corrects within the day. Lacking announcements, order books, and limit-free stock-days, we run two partial checks. First, the ceiling gap rises across terciles of day-*d* volume relative to its prior 60-day mean (`r f(c24("Ceiling","volume",1,"gap_mkt"),2)`%, `r f(c24("Ceiling","volume",2,"gap_mkt"),2)`%, and `r f(c24("Ceiling","volume",3,"gap_mkt"),2)`%) and of the prior 20-day return (`r f(c24("Ceiling","prior 20",1,"gap_mkt"),2)`%, `r f(c24("Ceiling","prior 20",2,"gap_mkt"),2)`%, and `r f(c24("Ceiling","prior 20",3,"gap_mkt"),2)`%), which fits readings (1) and (2) alike, and stays positive and significant in the lowest tercile of each proxy (*t* = `r f(c24("Ceiling","volume",1,"gap_mkt","t_twoway"),1)` and `r f(c24("Ceiling","prior 20",1,"gap_mkt","t_twoway"),1)`). For floors the gap moves from `r f(c24("Floor","volume",1,"gap_mkt"),2)`% to `r f(c24("Floor","volume",3,"gap_mkt"),2)`% across volume terciles and is not monotone in the prior return, so the attention reading does not carry over. Second, the comparison with stocks that closed at their high removes selection on the shape of the close but not on news. The intraday giveback fits readings (2) and (3) at least as well as permanent price discovery, so "break at the limit" is a description and delayed price discovery one hypothesis. Testing the magnet effect (Chen et al., 2024; Cho et al., 2003) needs intraday prices, which we lack.
~~~

**E47.** Section 5: auction-priority detail already in Section 3
~~~old
Table 4 splits the events at 5 May 2025, when HOSE moved to the KRX platform and at-the-open and at-the-close orders lost their auction priority.
~~~
~~~new
Table 4 splits the events at 5 May 2025, when HOSE moved to the KRX platform.
~~~

**E48.** Table 4 caption: shorten
~~~old
caption = "Table 4. Next-day abnormal returns before and after the move to the KRX platform on 5 May 2025. Entries are mean abnormal returns in percent with two-way-clustered *t*-statistics in parentheses. The split uses the date of the opening that defines the gap, and the difference *t*-statistic treats the two periods as independent."
~~~
~~~new
caption = "Table 4. Next-day abnormal returns (percent) before and after the move to the KRX platform on 5 May 2025, with two-way-clustered *t*-statistics in parentheses. The split uses the date of the opening that defines the gap; the difference *t*-statistic treats the periods as independent."
~~~

**E49.** Section 5 platform split: tighten; keep pre-change insignificance caveat
~~~old
Band changes in other markets changed volatility, liquidity, and execution quality (Kim & Jun, 2019; Lien et al., 2019; Qi, 2023; Zhang et al., 2022). Our split follows a change in auction priority with the band held at 7%. The ceiling gap appears in both periods (`r f(c22("Ceiling","gap_mkt","pre_mean"),2)`% before, `r f(c22("Ceiling","gap_mkt","post_mean"),2)`% after the move to KRX; difference *t* = `r f(c22("Ceiling","gap_mkt","diff_t"),1)`; Table 4). The floor gap is more negative after the move (`r f(c22("Floor","gap_mkt","pre_mean"),2)`% before, `r f(c22("Floor","gap_mkt","post_mean"),2)`% after; difference *t* = `r f(c22("Floor","gap_mkt","diff_t"),1)`), and the intraday return after floor closes turns positive (`r f(c22("Floor","intraday_mkt","post_mean"),2)`%). The drift from the next open to day *d*+5 after floor closes exists only before the move (`r f(c22("Floor","f5o_mkt","pre_mean"),2)`% before, `r f(c22("Floor","f5o_mkt","post_mean"),2)`% after). The change coincides with a different market period, and the post-change sample holds `r f(100*c22("Ceiling","gap_mkt","post_n")/(c22("Ceiling","gap_mkt","pre_n")+c22("Ceiling","gap_mkt","post_n")),0)`% of the ceiling events and `r f(100*c22("Floor","gap_mkt","post_n")/(c22("Floor","gap_mkt","pre_n")+c22("Floor","gap_mkt","post_n")),0)`% of the floor events. Both periods show a positive ceiling gap followed by an intraday reversal, but before the change neither the ceiling close-to-close return (*t* = `r f(c22("Ceiling","cc1_mkt","pre_t"),1)`) nor the floor gap (*t* = `r f(c22("Floor","gap_mkt","pre_t"),1)`) is significant at the 5% level, so the full-sample significance rests mainly on the post-change events. We cannot attribute the differences between the periods to the auction rules.
~~~
~~~new
The ceiling gap, followed by an intraday reversal, appears in both periods (`r f(c22("Ceiling","gap_mkt","pre_mean"),2)`% before and `r f(c22("Ceiling","gap_mkt","post_mean"),2)`% after; difference *t* = `r f(c22("Ceiling","gap_mkt","diff_t"),1)`). The floor gap is more negative after the move (`r f(c22("Floor","gap_mkt","pre_mean"),2)`% before, `r f(c22("Floor","gap_mkt","post_mean"),2)`% after; difference *t* = `r f(c22("Floor","gap_mkt","diff_t"),1)`), the intraday return after floor closes turns positive (`r f(c22("Floor","intraday_mkt","post_mean"),2)`%), and the floor drift from the next open to day *d*+5 exists only before the move (`r f(c22("Floor","f5o_mkt","pre_mean"),2)`% before, `r f(c22("Floor","f5o_mkt","post_mean"),2)`% after). The change coincides with a different market period, and the post-change sample holds `r f(100*c22("Ceiling","gap_mkt","post_n")/(c22("Ceiling","gap_mkt","pre_n")+c22("Ceiling","gap_mkt","post_n")),0)`% of the ceiling events and `r f(100*c22("Floor","gap_mkt","post_n")/(c22("Floor","gap_mkt","pre_n")+c22("Floor","gap_mkt","post_n")),0)`% of the floor events. Before the change neither the ceiling close-to-close return (*t* = `r f(c22("Ceiling","cc1_mkt","pre_t"),1)`) nor the floor gap (*t* = `r f(c22("Floor","gap_mkt","pre_t"),1)`) is significant at the 5% level, so the full-sample significance rests mainly on post-change events. We cannot attribute the differences between the periods to the auction rules.
~~~

**E50.** Section 5 outliers: tighten
~~~old
Returns beyond ±8%, which a 7% band does not allow, occur on `r fi(sum(PILE$n[PILE$range %in% c("< -8.0%", "> 8.0%")]))` stock-days and may reflect unadjusted corporate actions or listing-day bands. Dropping every event within five trading days of such a return changes the ceiling gap from `r f(c25("Ceiling","gap_mkt","all_mean"),2)`% to `r f(c25("Ceiling","gap_mkt","excl_mean"),2)`% and the floor gap from `r f(c25("Floor","gap_mkt","all_mean"),2)`% to `r f(c25("Floor","gap_mkt","excl_mean"),2)`%. The exclusion removes events but leaves the outlier days in the market benchmark.
~~~
~~~new
Returns beyond ±8%, which a 7% band does not allow, occur on `r fi(sum(PILE$n[PILE$range %in% c("< -8.0%", "> 8.0%")]))` stock-days and may reflect unadjusted corporate actions or listing-day bands. Dropping every event within five trading days of such a return moves the ceiling gap from `r f(c25("Ceiling","gap_mkt","all_mean"),2)`% to `r f(c25("Ceiling","gap_mkt","excl_mean"),2)`% and the floor gap from `r f(c25("Floor","gap_mkt","all_mean"),2)`% to `r f(c25("Floor","gap_mkt","excl_mean"),2)`%; the outlier days stay in the market benchmark.
~~~

**E51.** Section 5 Bonferroni bound: define m_max here once
~~~old
To bound the effect of a wider search, we compute $m_{\text{max}}$ from Section 4. All four event tests survive a Bonferroni correction at 5% for families of up to `r fi(c21(5))` tests with date clusters and up to `r fi(c21(6))` tests with calendar-week clusters (largest *p*-values `r formatC(c21(2), format = "f", digits = 5)` and `r formatC(c21(3), format = "f", digits = 5)`, *t* reference). The bound limits false discoveries and leaves the upward bias in effect sizes untouched.
~~~
~~~new
To bound the effect of a wider search, let $p_{\text{max}}$ be the largest event-test *p*-value computed with the factor $G/(G-1)$ and a *t* reference. All four event tests survive a Bonferroni correction at 5% in families of up to $m_{\text{max}} = \lfloor 0.05 / p_{\text{max}} \rfloor$ tests: `r fi(c21(5))` with date clusters and `r fi(c21(6))` with calendar-week clusters ($p_{\text{max}}$ of `r formatC(c21(2), format = "f", digits = 5)` and `r formatC(c21(3), format = "f", digits = 5)`). The bound limits false discoveries but leaves the upward bias in effect sizes untouched.
~~~

**E52.** Section 5 summary: drop meta-joiner
~~~old
The results support H~1~ to H~4~. The ceiling effect survives alternative benchmarks, clusters, and event definitions and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture. The floor effect combines a gap with drift that appears only before the 2025 platform change, and its size depends on the benchmark. Section 6 weighs the explanations.
~~~
~~~new
The results support H~1~ to H~4~. The ceiling effect survives alternative benchmarks, clusters, and event definitions and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture. The floor effect combines a gap with drift that appears only before the 2025 platform change, and its size depends on the benchmark.
~~~

**E53.** Section 6 P1: merge timing statements
~~~old
The evidence fits delayed price discovery and the rival readings of Section 5. After a ceiling close, the continuation sits in the opening: days *d*+2 to *d*+5 add no significant return, and traders reverse part of the gap during day *d*+1, a one-day analogue of the cross-period reversal in Lou et al. (2019). The contrast with stocks that moved almost as far, including those that also closed at their high, is the part of the evidence that a pure attention reading must explain. The post-open drift after floor closes, which exists only before the platform change, does not fit a gap-only reading. Our decomposition adds timing to the evidence of Kim and Rhee (1997): on HOSE the continuation after ceiling closes arrives at the next opening and ends after the first day.
~~~
~~~new
Our decomposition adds timing to the evidence of Kim and Rhee (1997): on HOSE the continuation after ceiling closes arrives at the next opening and ends after the first day, and the intraday giveback is a one-day analogue of the cross-period reversal in Lou et al. (2019). A pure attention reading must explain the contrast with stocks that moved almost as far, including those that also closed at their high, and a gap-only reading cannot explain the pre-change post-open drift after floor closes.
~~~

**E54.** Section 6: single 'no comparable study' statement
~~~old
Table 5 sets each result against the studies reviewed in Section 2. No source reports the next-day abnormal return, the overnight gap, or the intraday return after a limit close in a form that matches ours, so the table compares signs, timing, and mechanism.
~~~
~~~new
No earlier study reports post-limit returns in a form that matches ours, so Table 5 compares signs, timing, and mechanism.
~~~

**E55.** Table 5 setting column: shorten
~~~old
Setting = c("Tokyo; limit-hit events", "Korea; revision of the limit system", "Taiwan; limit hits", "Taiwan; five-minute data", "Shenzhen; account-level data", "ChiNext; band widened from 10% to 20%", "China; cross-section of stocks", "United States; intraday data", "United States; stock-level returns", "China A-shares; all stocks", "United States; published anomalies"),
~~~
~~~new
Setting = c("Tokyo; limit hits", "Korea; limit revision", "Taiwan; limit hits", "Taiwan; five-minute data", "Shenzhen; accounts", "ChiNext; band 10% to 20%", "China; cross-section", "U.S.; intraday data", "U.S.; stock returns", "China A-shares", "U.S.; anomalies"),
~~~

**E56.** Table 5 findings column: trim wording that repeats Section 2
~~~old
`Reported finding` = c("Support for volatility spillover, delayed price discovery, and trading interference", "Volatility and trading activity examined around the revision", "Overnight overreaction after limit hits corrected on the following day", "Prices accelerate toward the upper limit", "Large investors buy on the limit day and sell on the next day; their net buying predicts long-run reversal", "Delayed price discovery, volatility spillover, and trading interference, stronger at the lower limit; no magnet effect", "Stocks with large limit exposure, or frequent upper-limit hits, earn lower future returns", "Positive overnight returns followed by intraday reversals, concentrated in high-attention stocks", "Overnight and intraday continuation with an offsetting cross-period reversal", "Average overnight return is negative; T+1 rule lowers opening prices", "With microcaps mitigated, 65% of 452 anomalies fail the 1.96 hurdle; a new factor needs *t* above 3.0"),
~~~
~~~new
`Reported finding` = c("Volatility spillover, delayed price discovery, and trading interference", "Volatility and trading activity around the revision", "Overnight overreaction after limit hits corrected the next day", "Prices accelerate toward the upper limit", "Large investors buy on the limit day and sell the next; their net buying predicts long-run reversal", "Delayed price discovery, spillover, and interference, stronger at the lower limit; no magnet effect", "Large limit exposure or frequent upper-limit hits predict lower returns", "Overnight gains, intraday reversals, concentrated in high-attention stocks", "Overnight and intraday continuation, offsetting cross-period reversal", "Negative average overnight return; T+1 rule lowers opening prices", "65% of 452 anomalies fail the 1.96 hurdle; a new factor needs *t* above 3.0"),
~~~

**E57.** Table 5 relation column: trim
~~~old
`Relation to our result` = c("Our significant next-day return after ceiling closes is consistent with delayed price discovery; we do not test spillover or interference", "Different question; no comparison with our returns", "Same timing: positive gap, partial intraday reversal", "Not tested; our data lack intraday prices", "Consistent with our intraday reversal; our data lack account identities", "Different outcome: market quality after a band change. Here both ceiling and floor closes carry a significant next-day return, and the weaker floor effect depends on the benchmark", "Different horizon; a positive one-day return can coexist with later reversal, which we do not measure", "Same signs after limit closes; the gap here also rises with volume and prior return", "The gap-then-reversal has the sign of that cross-period reversal at a one-day horizon", "Opposite sign: the overnight return after a ceiling close is positive", "None of our 22 characteristics reaches 1.96 in the full sample"), check.names = FALSE)
~~~
~~~new
`Relation to our result` = c("Ceiling next-day return consistent with delayed price discovery; spillover and interference not tested", "Different question", "Same timing: positive gap, partial intraday reversal", "Not tested; no intraday prices", "Consistent with our intraday reversal; no account identities", "Different outcome (market quality); here both limit closes carry a next-day return, the floor effect depending on the benchmark", "Different horizon; a one-day gain can coexist with later reversal, which we do not measure", "Same signs; the gap also rises with volume and prior return", "Gap-then-reversal has the sign of that cross-period reversal at one day", "Opposite sign: positive overnight return after ceiling closes", "None of our 22 characteristics reaches 1.96 in the full sample"), check.names = FALSE)
~~~

**E58.** Table 5 caption: shorten
~~~old
caption = "Table 5. Comparison with earlier studies. The second and third columns summarize each source as reported in its abstract or in the records we could access; the last column relates it to our results."
~~~
~~~new
caption = "Table 5. Comparison with earlier studies. Findings are as reported in each source's abstract or in the records we could access."
~~~

**E59.** Section 6 design: drop repeated platform caveat detail
~~~old
The findings bear on two design choices, the width of the band and the priority of auction orders. A 7% band leaves room for a large overnight gap, so the opening auction may do much of the adjustment that a wider band would allow on day *d*. The floor gap grows and the intraday return after floor closes turns positive after at-the-open orders lose priority (Table 4). This is consistent with auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time, so the split cannot isolate the auction rules (Section 5). A band change on HOSE, like the ChiNext widening that Qi (2023) studies, would give a natural experiment to test the readings.
~~~
~~~new
A 7% band leaves room for a large overnight gap, so the opening auction may do much of the adjustment that a wider band would allow on day *d*. The floor results after at-the-open orders lost priority (Table 4) fit auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time; a band change on HOSE, like the ChiNext widening that Qi (2023) studies, would give a natural experiment.
~~~

**E60.** Section 6 attention: drop Berkman repetition
~~~old
The volume and prior-return results fit an attention channel. If attention drives the gap, the limit acts as an amplifier: a stock at its ceiling may appear on screens and rankings the next morning, and a queue at the limit may signal excess demand to other investors. Berkman et al. (2012) trace the overnight returns of U.S. stocks to such attention, and Akbas et al. (2022) and Lu et al. (2023) trace the split between overnight and intraday returns to different clienteles, with noise traders overnight, arbitrageurs by day, and market makers absorbing retail imbalances near the open. Under this reading, a limit adds a visible, rule-based trigger to an attention mechanism that operates without limits.
~~~
~~~new
The volume and prior-return results also fit an attention channel in which the limit amplifies demand: a stock at its ceiling may appear on screens and rankings the next morning, and a queue at the limit may signal excess demand. With noise traders overnight, arbitrageurs by day, and market makers absorbing retail imbalances near the open (Akbas et al., 2022; Lu et al., 2023), a limit would add a visible, rule-based trigger to an attention mechanism that operates without limits.
~~~

**E61.** Section 6: merge power caveat
~~~old
We use the 22 characteristics to set the multiplicity burden and as a null benchmark; with low power (Section 5), their null says little about the cross-section. Ceiling closes cover about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in the event window, so we make no claim that limit closes explain the cross-section of returns.
~~~
~~~new
Ceiling closes cover about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in the event window, and the low-powered characteristic null says little about the cross-section, so we make no claim that limit closes explain the cross-section of returns.
~~~

**E62.** Section 6 closing: drop numbers and data wish-list repeated in Section 5 and Conclusion
~~~old
The estimates describe what follows limit closes on HOSE in 2024 to 2026: the overnight gap averages `r f(c16("Ceiling all","gap_mkt"),1)`% after ceiling closes and `r f(c16("Floor all","gap_mkt"),1)`% after floor closes. They cannot show what the limit does to price discovery: the band does not vary, no period lacks a limit, and we measure none of the benefits a limit is meant to deliver. Announcement time stamps, order-book queue sizes at the close, and a market or period without a limit would test the readings. For investors, buying ceiling stocks at the quoted next open lost `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close, before costs and rationing at the open.
~~~
~~~new
The estimates describe what follows limit closes on HOSE in 2024 to 2026. They cannot show what the limit does to price discovery: the band does not vary, no period lacks a limit, and we measure none of the benefits a limit is meant to deliver. For investors, buying ceiling stocks at the quoted next open lost money against the market by the fifth close, excluding costs and rationing at the open.
~~~

**E63.** Section 7: compress each limitation, keep substance
~~~old
(i) The sample covers `r c26(4)` trading days on one exchange, with one trading-platform change and a period of market stress. (ii) We have no order-book, investor-type, announcement, or news data, so we infer the unfilled-demand mechanism and cannot separate it from selection on news. (iii) The 7% band, the reference price, and the platform change come from brokerage and press descriptions, which we check against the return distribution but not against exchange circulars. Tick sizes, reference-price treatment on corporate-action days, and wider bands for first-day listings and resumed trading are assumptions. (iv) The vendor appears to adjust earlier prices for later corporate actions: for stocks priced at 10 thousand dong or more, only `r f(c27(2),0)`% of 2024 closes, `r f(c27(4),0)`% of 2025 closes, and `r f(c27(6),0)`% of 2026 closes are multiples of the tick size, against `r f(c27(1),0)`% for stocks below 10 thousand dong, where the 0.01 tick equals the two-decimal resolution of the files and the check is uninformative, and near hits make up `r f(c27(11),0)`% of ceiling events for the higher-priced stocks against `r f(c27(10),0)`% for the others. Proportional adjustment leaves returns (except on ex-dates), the close-at-high event rule, and locked days unchanged, but it makes the exact-hit classification of Equation (3) unreliable, so we treat exact and near hits as a data check rather than as a measure of distance to the limit. The listing snapshot also excludes earlier delistings. (v) Clustered standard errors allow dependence across dates, weeks, blocks, and stocks, but events in the same market episode may depend on each other more, and we did not compute calendar-time portfolio estimates or standard errors robust to both cross-sectional and serial dependence. (vi) Several characteristics (5-day return, MAX, MIN, move frequency, overnight return) share inputs with the event definition, and the Corwin–Schultz spread and range volatility use high and low prices that limits censor. (vii) The floor effect depends on the benchmark, and we built no beta- and size-matched control for the five-day outcome. (viii) The characteristic tests have limited power, and the effect sizes may carry winner's-curse bias because we chose this question from several screened on the same data.
~~~
~~~new
(i) The sample covers `r c26(4)` trading days on one exchange, with one platform change and a period of market stress. (ii) Without order-book, investor-type, announcement, or news data, we infer the unfilled-demand mechanism and cannot separate it from selection on news. (iii) The 7% band, reference price, and platform change come from brokerage and press descriptions, checked against returns but not against exchange circulars; tick sizes, reference prices on corporate-action days, and wider bands for first-day listings and resumed trading are assumptions. (iv) The vendor appears to adjust earlier prices for later corporate actions. For stocks priced at 10 thousand dong or more, `r f(c27(2),0)`%, `r f(c27(4),0)`%, and `r f(c27(6),0)`% of 2024, 2025, and 2026 closes are tick multiples, against `r f(c27(1),0)`% below 10 thousand dong (an uninformative check, since the 0.01 tick equals the two-decimal resolution of the files), and near hits make up `r f(c27(11),0)`% of ceiling events for the higher-priced stocks against `r f(c27(10),0)`% for the others. Proportional adjustment leaves returns (except on ex-dates), the close-at-high rule, and locked days unchanged but makes the exact-hit classification of Equation (3) unreliable, so we treat that split as a data check, not a measure of distance to the limit. The listing snapshot excludes stocks delisted before the download. (v) Events in one market episode may depend on each other beyond our clustering, and we computed no calendar-time portfolio estimates or standard errors robust to both cross-sectional and serial dependence. (vi) Several characteristics (5-day return, MAX, MIN, move frequency, overnight return) share inputs with the event definition, and the Corwin–Schultz spread and range volatility use limit-censored highs and lows. (vii) The floor effect depends on the benchmark, and we built no beta- and size-matched control for the five-day outcome. (viii) The characteristic tests have limited power, and effect sizes may carry winner's-curse bias from choosing this question among several screened on the same data.
~~~

**E64.** Conclusion: tighten
~~~old
Of 26 tests on `r nstocks` HOSE stocks, the four price-limit tests survive FDR control and the confirmation-half check, and the 22 characteristic tests do not, although the latter have limited power. After a ceiling close, the stock earns a next-day abnormal return of about `r f(ev("ceiling","t+1","mean_ar_pct"),1)`%, which is an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%. The gap is `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points larger than for stocks that rose 5% to 6.5% and `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","diff_pct"),1)` points larger than for those among them that also closed at their high. After a floor close, the overnight gap is `r f(c16("Floor all","gap_mkt"),1)`%. The pattern fits delayed price discovery at the limit, but news and attention remain possible explanations. An outside buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. Longer samples, announcement data, and order-book data would let future work separate these explanations.
~~~
~~~new
Of 26 tests on `r nstocks` HOSE stocks, the four price-limit tests survive FDR control and the confirmation-half check, and the 22 lower-powered characteristic tests do not. After a ceiling close, the next-day abnormal return of `r f(ev("ceiling","t+1","mean_ar_pct"),1)`% is an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%. The gap is `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points larger than for stocks that rose 5% to 6.5% and `r f(c23("ceiling vs 5-6.5% up, close = high","gap_mkt","diff_pct"),1)` points larger than for those among them that also closed at their high. After a floor close, the overnight gap is `r f(c16("Floor all","gap_mkt"),1)`%. An outside buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close. Delayed price discovery at the limit fits the pattern, but news and attention remain possible explanations; longer samples, announcement time stamps, and order-book queues would let future work separate them.
~~~

**E65.** Appendix A: group measures by window; Bali et al. citation moved here from Section 4
~~~old
All characteristics use data up to the formation day of each week. REV1W and REV1M are the compounded returns over the last 5 and 20 trading days. MOM3M and MOM6M are the compounded returns over 60 and 110 trading days ending five days before formation. IMOM compounds the return in excess of the dollar-volume-weighted market over the MOM3M window. VOL is the standard deviation of daily returns over the last 60 days, BETA is the slope and IVOL the residual standard deviation of a regression of those returns on the dollar-volume-weighted return of the stocks in that week's cross-section, with weights at the formation day, and DOWNVOL is the square root of the mean of $\min(r, 0)^2$ over the same 60 days, so days with positive returns enter as zeros. RANGEVOL is the Parkinson (1980) estimator from daily highs and lows over 60 days. MAX and MIN are the largest and smallest daily returns over 20 days, and SKEW and KURT are the third and fourth standardized moments of daily returns over 60 days. AMIHUD is the mean ratio of absolute return to dollar volume over 60 days (Amihud, 2002), LNDVOL the log of mean dollar volume over 60 days, and DVOLCHG and TURNCHG the ratios of 20-day to 60-day mean dollar volume and share volume. CSSPREAD is the Corwin and Schultz (2012) spread estimator over 60 days. OVERNIGHT and INTRADAY are the mean open-over-previous-close and close-over-open returns over 20 days, and LIMITFREQ is the share of the last 20 days with an absolute return of 6.5% or more. The quintile spread is the equal-weighted abnormal return of the top minus the bottom quintile over the next five days; the net spread subtracts $2 \times 0.0025 \times (\mathrm{TO}_{L} + \mathrm{TO}_{S})$, where $\mathrm{TO}_{L}$ and $\mathrm{TO}_{S}$ are the shares of the long and short legs replaced since the previous week.
~~~
~~~new
All characteristics use data up to each week's formation day. REV1W and REV1M are the compounded returns over the last 5 and 20 trading days, and MOM3M and MOM6M over 60 and 110 trading days ending five days before formation. IMOM compounds the return in excess of the dollar-volume-weighted market over the MOM3M window. Over the last 60 days, VOL is the standard deviation of daily returns; BETA and IVOL are the slope and residual standard deviation of a regression of those returns on the dollar-volume-weighted return of that week's cross-section; DOWNVOL is the square root of the mean of $\min(r, 0)^2$; RANGEVOL is the Parkinson (1980) high-low estimator; SKEW and KURT are the third and fourth standardized moments; AMIHUD is the mean ratio of absolute return to dollar volume (Amihud, 2002); LNDVOL is the log of mean dollar volume; and CSSPREAD is the Corwin and Schultz (2012) spread estimator. Over the last 20 days, MAX and MIN are the largest and smallest daily returns (Bali et al., 2011), OVERNIGHT and INTRADAY the mean open-over-previous-close and close-over-open returns, and LIMITFREQ the share of days with an absolute return of 6.5% or more. DVOLCHG and TURNCHG are the ratios of 20-day to 60-day mean dollar volume and share volume. The quintile spread is the equal-weighted abnormal return of the top minus the bottom quintile over the next five days; the net spread subtracts $2 \times 0.0025 \times (\mathrm{TO}_{L} + \mathrm{TO}_{S})$, where $\mathrm{TO}_{L}$ and $\mathrm{TO}_{S}$ are the shares of the long and short legs replaced since the previous week.
~~~
