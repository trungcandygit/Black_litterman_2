**Abstract.** Daily price limits are meant to cool markets, but they can also postpone price discovery. Using daily open–high–low–close–volume data on 347 stocks listed on the Ho Chi Minh Stock Exchange (HOSE; 21 August 2024 to 23 September 2026, 200,468 stock-days), we test a pre-registered family of 26 hypotheses: 22 price- and volume-based characteristics as predictors of next-week returns and four price-limit event tests. After false-discovery-rate control and a hold-out half-sample, 0 of the 22 characteristics survive (largest absolute Fama–MacBeth t-statistic 1.55), while 4 of the 4 limit tests survive. A stock that closes at its daily ceiling earns an abnormal return of 1.66% on the next day (date-clustered t = 4.9, 3,187 events), and a stock that closes at its floor earns -0.71% (t = -5.3). A decomposition that was added after seeing these results shows that the ceiling effect is entirely an overnight gap (2.23%, two-way-clustered t = 9.8), followed by an intraday reversal (-0.53%, t = -3.5). Relative to stocks that rose 5–6.5% without reaching the limit, ceiling closers show an overnight gap that is 2.67 percentage points larger (t = 13.7); for floors the gap is 1.58 points lower (t = -9.5). The pattern is consistent with demand and supply that the limit prevents from clearing on the limit day and that the next opening absorbs. It does not offer a profit to a buyer who enters after the close: buying at the next open and holding to the fifth close loses 0.79% relative to the market (t = -3.7). A public, non-peer-reviewed analysis of a longer sample reports a close-to-close ceiling effect of similar size; our contributions are the overnight–intraday decomposition, the discontinuity comparison, and the multiple-testing frame.

**Keywords:** price limits; delayed price discovery; overnight returns; multiple testing; Vietnam; retail investors

**JEL classification:** G14; G15; G18

**Tóm tắt.** Bài viết kiểm định một họ 26 giả thuyết đã đăng ký trước trên 347 cổ phiếu HOSE (8/2024–9/2026): 22 đặc trưng giá–khối lượng và 4 kiểm định sự kiện chạm giá trần/giá sàn. Sau khi kiểm soát tỷ lệ phát hiện sai và dùng nửa mẫu xác nhận, chỉ 4 kiểm định sự kiện sống sót, không đặc trưng nào. Cổ phiếu đóng cửa ở giá trần có lợi suất bất thường ngày kế tiếp 1.66% (t = 4.9), toàn bộ đến từ khoảng trống giá qua đêm (2.23%), sau đó đảo chiều trong phiên (-0.53%). Nhà đầu tư mua ở giá mở cửa kế tiếp không có lợi nhuận bất thường dương.

# 1. Introduction

A daily price limit stops a stock from moving beyond a fixed band on a single day. Price limits have a theoretical rationale in futures markets (Brennan, 1986). In equity markets, advocates argue that limits reduce volatility and counter overreaction, while critics argue that they delay price discovery, spill volatility into later days and interfere with trading (Kim & Rhee, 1997). Kim and Rhee (1997) find support for all three critical hypotheses on the Tokyo Stock Exchange, Chen (1993) finds that return serial correlation falls as the limit widens in Taiwan, Berkman and Lee (2002) report more frequent price continuations after limit hits on the Korean Stock Exchange, and Cho et al. (2003) document a magnet effect toward the upper limit in intraday Taiwanese data. Evidence for Vietnam is thinner. Veeraraghavan et al. (2007) study momentum and price limits on the Vietnamese exchange for 2000–2006, and an open analysis posted on GitHub (tungtran0911, 2026; not peer reviewed) reports that stocks closing at the HOSE ceiling earn a further 1.69% the next session while stocks that rise 3–6.5% give back 0.39%.

We ask a narrower question than whether limits “work”. On a stock-day basis, does closing at the limit predict the next day’s return, how much of that prediction is the overnight gap versus the trading session that follows, and is the prediction available to an investor who was not already holding the stock? We also ask how this evidence compares with the 22 familiar price- and volume-based characteristics when all are examined in one pre-registered family with false-discovery-rate control (Benjamini & Hochberg, 1995; Harvey et al., 2016). The family-wide frame matters because the limit result is large; the frame answers the objection that a large effect found after a long search is likely to be luck.

**Contributions and novelty.** To our knowledge, among the sources our search reached (Appendix C), no peer-reviewed study documents the following for HOSE: (i) a decomposition of the next-day effect into the overnight gap and the intraday return, showing that the continuation is entirely a gap and that the following session reverses part of it; (ii) a comparison with stocks that moved nearly as far without reaching the limit, estimated with date-clustered and two-way-clustered inference; and (iii) a pre-registered, multiplicity-controlled family in which the same data yield no surviving characteristic. The overnight-gain-then-intraday-reversal signature is known from U.S. data for attention-grabbing stocks (Berkman et al., 2012); our contribution is to document it as a discontinuity at a price limit. We do not claim to be first to document the close-to-close ceiling effect in Vietnam: tungtran0911 (2026) reports it on a longer sample (2016–2026) from a different data feed, and our estimate (1.66%) is close to theirs (1.69%), which serves as an independent replication.

The remainder of the paper describes the data and design (Sections 2 and 3), reports results (Section 4), and discusses implications and limitations (Sections 5 and 6).

# 2. Data

The raw data are daily open, high, low, close and volume for 405 HOSE-listed stocks from 21 August 2024 to 23 September 2026. We keep the 347 stocks with at least 95% non-missing prices. Returns are close-to-close. The market return is the dollar-volume-weighted return of all stocks, with weights from the trailing 60-day average dollar volume; stock abnormal returns are stock returns minus the market return over the same interval.

HOSE’s daily price limit is understood to be 7% around a reference price (public exchange guides; we treat this as an assumption and check it against the data): Table 1 shows that 2.21% of stock-days have a close-to-close return between 6.5% and 7.1%, against 0.37% between 6.0% and 6.5% and 0.011% between 7.1% and 8.0%, which is the pile-up expected from a 7% limit. Returns beyond 7.1% are rare (about 0.05% of stock-days) and we do not investigate their causes.

Table 1. Distribution of daily returns around the 7% limit (200,468 stock-days).

| Close-to-close return | Stock-days | Share (%) |
|-----------------------|------------|-----------|
| \< -8.0%              | 46         | 0.023     |
| -8.0% to -7.1%        | 5          | 0.002     |
| -7.1% to -6.9%        | 1,449      | 0.723     |
| -6.9% to -6.5%        | 1,659      | 0.828     |
| -6.5% to -6.0%        | 722        | 0.360     |
| -6.0% to 6.0%         | 191,315    | 95.434    |
| 6.0% to 6.5%          | 741        | 0.370     |
| 6.5% to 6.9%          | 2,475      | 1.235     |
| 6.9% to 7.1%          | 1,960      | 0.978     |
| 7.1% to 8.0%          | 23         | 0.011     |
| \> 8.0%               | 73         | 0.036     |

Table 1. Distribution of daily returns around the 7% limit (200,468 stock-days).

We do not observe order books, trade sizes by investor type, or intraday prices beyond the high and the low. Market capitalization is also unavailable for this sample, which is why the market return uses dollar-volume weights.

# 3. Design

## 3.1 A pre-registered family of 26 tests

Before computing any result we fixed the family, the estimators, the multiplicity controls and the survival rule (`process/03_brainstorm_round2.md`, `process/decisions.md` A3). The family is 22 characteristics measured at the end of each week and four price-limit event tests.

*Characteristics.* Momentum and reversal: 5-day return (REV1W), 20-day return (REV1M), 60-day return skipping 5 days (MOM3M), 110-day return skipping 5 days (MOM6M), 60-day idiosyncratic momentum (IMOM). Risk: 60-day volatility (VOL), idiosyncratic volatility (IVOL), market beta (BETA), downside deviation (DOWNVOL), Parkinson (1980) range volatility (RANGEVOL), maximum daily return in 20 days (MAX; Bali et al., 2011), minimum daily return (MIN), skewness (SKEW), kurtosis (KURT). Liquidity and volume: Amihud (2002) illiquidity (AMIHUD), log dollar volume (LNDVOL), 20/60-day dollar-volume ratio (DVOLCHG) and volume ratio (TURNCHG), the Corwin and Schultz (2012) spread (CSSPREAD). Intraday: mean overnight return (OVERNIGHT), mean intraday return (INTRADAY), share of days with a move of 6.5% or more (LIMITFREQ). Each is rank-normalized in the cross-section.

*Estimator.* Weekly Fama and MacBeth (1973) cross-sectional regressions of the next five trading days’ abnormal return on one standardized characteristic at a time, with Newey and West (1987) t-statistics (4 lags) on the time series of slopes; 79 weekly cross-sections. The first 39 weeks are the discovery half and the remaining 40 the confirmation half. For each characteristic we also report the long–short quintile spread (equal weighted) net of a cost of 25 basis points per unit of traded value, and the t-statistic after excluding the least liquid 20% of stocks.

*Limit events.* A ceiling event is a day with a return of at least +6.5% and a close equal to the day’s high; a floor event is a return of at most −6.5% with a close equal to the day’s low. Outcomes are the market-adjusted return on day $t + 1$ and cumulatively over days $t + 1$ to $t + 5$. Inference uses the cross-sectional mean with standard errors clustered by date. These are the four event tests (ceiling and floor, two horizons).

*Multiplicity.* The 26 p-values are adjusted by Benjamini–Hochberg (5% false-discovery rate) and by Holm (1979); we also report the Harvey et al. (2016) threshold of \|t\| = 3. A test *survives* if its adjusted p-value is below 5% and, in addition, its sign in the discovery half agrees with the full sample and the confirmation-half \|t\| exceeds 1.96.

## 3.2 Post hoc analyses

The following analyses were added **after** seeing that the limit tests survive; they are labelled post hoc throughout (`process/decisions.md` A4): (a) decomposition of day $t + 1$ into the overnight gap (open at $t + 1$ over close at $t$) and the intraday return (close over open at $t + 1$); (b) returns measured from the next open, which is what an investor entering after the close can obtain, since a stock that closes at its ceiling usually cannot be bought at that close; (c) a control group of stocks in the same liquidity tercile on the same date; (d) a comparison with days on which stocks rose or fell 3–5% or 5–6.5% without hitting the limit; (e) an exact tick-rule definition of the limit hit (the close equals the previous close times 1.07, rounded to the price tick, assuming ticks of 0.01, 0.05 and 0.10 thousand VND below 10, below 50 and from 50); (f) two-way (date and stock) clustering (Cameron et al., 2011); (g) sub-samples (halves, market-crash days, liquidity terciles, days with the stock locked at one price from open to close); and (h) a discontinuity plot by the size of the day-$t$ move (Imbens & Lemieux, 2008).

# 4. Results

## 4.1 The 22 characteristics

Table 2. Fama\<U+2013\>MacBeth results for the 22 pre-registered characteristics (ordered by absolute full-sample t-statistic).

| Characteristic | Slope (% per week, per s.d.) | t (full) | t (discovery) | t (confirmation) | t (excl. least liquid 20%) | Quintile spread, net of 25 bps (% per week) |
|----------------|------------------------------|----------|---------------|------------------|----------------------------|---------------------------------------------|
| MOM3M          | 0.131                        | 1.55     | 1.00          | 1.18             | 1.60                       | 0.091                                       |
| IMOM           | 0.129                        | 1.53     | 1.01          | 1.14             | 1.57                       | 0.088                                       |
| DVOLCHG        | 0.072                        | 1.42     | 1.29          | 0.78             | 1.22                       | -0.021                                      |
| TURNCHG        | 0.057                        | 1.27     | 1.17          | 0.68             | 0.97                       | -0.081                                      |
| MOM6M          | 0.094                        | 1.12     | 0.60          | 0.97             | 1.21                       | 0.066                                       |
| REV1M          | 0.074                        | 0.92     | 1.18          | 0.14             | 1.48                       | -0.172                                      |
| MIN            | 0.048                        | 0.86     | 0.16          | 1.14             | 1.62                       | -0.151                                      |
| DOWNVOL        | -0.062                       | -0.84    | 0.12          | -1.64            | -1.28                      | -0.293                                      |
| CSSPREAD       | -0.051                       | -0.77    | 0.72          | -2.77            | -0.42                      | -0.203                                      |
| INTRADAY       | 0.036                        | 0.62     | 0.75          | 0.08             | 0.96                       | -0.215                                      |
| IVOL           | -0.028                       | -0.54    | 0.58          | -1.44            | -0.62                      | -0.198                                      |
| RANGEVOL       | -0.037                       | -0.51    | 0.92          | -2.35            | -0.40                      | -0.163                                      |
| REV1W          | 0.034                        | 0.41     | 1.08          | -0.26            | 1.52                       | -0.711                                      |
| LIMITFREQ      | -0.024                       | -0.28    | 0.61          | -1.16            | -0.26                      | -0.049                                      |
| LNDVOL         | 0.024                        | 0.27     | 0.43          | -0.18            | 0.79                       | 0.110                                       |
| AMIHUD         | -0.022                       | -0.26    | -0.37         | 0.07             | -0.84                      | -0.210                                      |
| KURT           | 0.012                        | 0.20     | 0.10          | 0.19             | 0.44                       | -0.127                                      |
| BETA           | -0.020                       | -0.18    | 0.32          | -0.97            | -0.29                      | -0.171                                      |
| VOL            | -0.006                       | -0.09    | 0.94          | -1.52            | -0.36                      | -0.067                                      |
| OVERNIGHT      | 0.004                        | 0.06     | 0.80          | -1.12            | 0.16                       | -0.322                                      |
| SKEW           | -0.001                       | -0.03    | 0.31          | -0.59            | 0.34                       | -0.213                                      |
| MAX            | -0.001                       | -0.02    | 0.96          | -1.73            | -0.09                      | -0.224                                      |

Table 2. Fama\<U+2013\>MacBeth results for the 22 pre-registered characteristics (ordered by absolute full-sample t-statistic).

<img src="media/rId25.png" style="width:5.83333in;height:4.66667in" alt="Figure 1. Fama&lt;U+2013&gt;MacBeth t-statistics of the 22 characteristics: full sample, discovery half and confirmation half." />

Figure 1. Fama\<U+2013\>MacBeth t-statistics of the 22 characteristics: full sample, discovery half and confirmation half.

None of the 22 characteristics has a full-sample \|t\| above 1.55 (Table 2, Figure 1), none passes the Harvey et al. (2016) threshold of 3, and none survives the family-wide control. The leading candidates, 3-month and idiosyncratic momentum, have t-statistics of 1.55 and 1.53, with confirmation-half t-statistics of 1.18 and 1.14. Standard risk measures are weak in this cross-section: volatility has t = -0.09, idiosyncratic volatility -0.54, and MAX -0.02. The long–short quintile spreads are small and, net of 25 basis points per unit traded, mostly negative; no characteristic combines a significant slope with a spread that survives costs. The tests have limited power with 79 cross-sections, so the null is informative mainly about effects as large as a few tenths of a percent per week.

## 4.2 The pre-registered limit tests

Table 3. Pre-registered price-limit event tests: market-adjusted returns after a ceiling or floor close.

| Event   | Horizon  | Mean abnormal return (%) | t (date-clustered) | Events | Dates | t (first half) | t (second half) |
|---------|----------|--------------------------|--------------------|--------|-------|----------------|-----------------|
| ceiling | t+1      | 1.66                     | 4.91               | 3,187  | 446   | 2.28           | 14.36           |
| ceiling | t+1..t+5 | 1.45                     | 4.01               | 3,187  | 446   | 1.78           | 6.82            |
| floor   | t+1      | -0.71                    | -5.33              | 2,105  | 319   | -2.97          | -5.12           |
| floor   | t+1..t+5 | -1.76                    | -4.75              | 2,105  | 319   | -11.57         | -2.16           |

Table 3. Pre-registered price-limit event tests: market-adjusted returns after a ceiling or floor close.

All four tests are significant, survive the Benjamini–Hochberg control over the 26 tests (adjusted p-values between 2.6e-06 and 4.0e-04) and keep the same sign in both halves of the sample with confirmation-half \|t\| above 1.96 (Table 3). A ceiling close is followed by an abnormal return of 1.66% the next day and 1.45% over five days; a floor close by -0.71% and -1.76%. Of the 26 pre-registered tests, 4 of 4 event tests and 0 of 22 characteristic tests survive.

## 4.3 The effect is an overnight gap (post hoc)

Table 4. Decomposition of the next-day abnormal return into the overnight gap and the intraday return, with three clustering schemes. Upper block: events defined by the pre-registered rule; lower block: events defined by the exact tick rule.

| Event         | Measure        | Mean (%) | t (date) | t (stock) | t (two-way) | Events | Stocks |
|---------------|----------------|----------|----------|-----------|-------------|--------|--------|
| ceiling       | overnight gap  | 2.23     | 10.8     | 19.7      | 9.8         | 3,220  | 335    |
| ceiling       | intraday       | -0.53    | -3.6     | -7.1      | -3.5        | 3,220  | 335    |
| ceiling       | close-to-close | 1.66     | 5.0      | 16.1      | 4.8         | 3,220  | 335    |
| floor         | overnight gap  | -0.99    | -5.0     | -10.2     | -4.7        | 2,122  | 318    |
| floor         | intraday       | 0.31     | 1.4      | 4.0       | 1.4         | 2,122  | 318    |
| floor         | close-to-close | -0.71    | -5.4     | -7.3      | -4.9        | 2,122  | 318    |
| exact ceiling | overnight gap  | 2.76     | 16.4     | 20.1      | 13.5        | 1,666  | 264    |
| exact ceiling | intraday       | -0.73    | -5.4     | -8.3      | -5.3        | 1,666  | 264    |
| exact ceiling | close-to-close | 1.97     | 7.4      | 15.4      | 7.0         | 1,666  | 264    |
| exact floor   | overnight gap  | -1.33    | -5.6     | -9.4      | -5.1        | 1,037  | 257    |
| exact floor   | intraday       | 0.40     | 1.7      | 3.6       | 1.7         | 1,037  | 257    |
| exact floor   | close-to-close | -0.96    | -6.5     | -7.2      | -5.8        | 1,037  | 257    |

Table 4. Decomposition of the next-day abnormal return into the overnight gap and the intraday return, with three clustering schemes. Upper block: events defined by the pre-registered rule; lower block: events defined by the exact tick rule.

<img src="media/rId30.png" style="width:5.83333in;height:2.83333in" alt="Figure 2. Next-day abnormal return after a limit close, decomposed into the overnight gap and the intraday return (post hoc; two-way-clustered 95% intervals)." />

Figure 2. Next-day abnormal return after a limit close, decomposed into the overnight gap and the intraday return (post hoc; two-way-clustered 95% intervals).

Table 4 and Figure 2 show where the next-day effect arises. After a ceiling close the abnormal return from the previous close to the next open is 2.23% (two-way-clustered t = 9.8); from the next open to the next close it is -0.53% (t = -3.5). The total is positive only because the gap exceeds the intraday giveback. After a floor close the gap is -0.99% (t = -4.7) and the intraday return is a partial and statistically weak reversal (0.31%, t = 1.4). The exact tick rule, which picks about half as many events (1,666 ceilings), strengthens the estimates: the ceiling gap is 2.76% (t = 13.5) and the intraday return -0.73% (t = -5.3). The rule-based definition therefore includes some closes that were near but not at the limit, and the pre-registered estimate understates the exact-limit effect.

## 4.4 A discontinuity at the limit (post hoc)

<img src="media/rId34.png" style="width:5.83333in;height:6in" alt="Figure 3. Next-day abnormal return (overnight gap, intraday, close-to-close) by the size of the day-t move. Triangles mark closes at the limit; squares mark moves beyond 6.5% that did not close at the limit (post hoc)." />

Figure 3. Next-day abnormal return (overnight gap, intraday, close-to-close) by the size of the day-t move. Triangles mark closes at the limit; squares mark moves beyond 6.5% that did not close at the limit (post hoc).

Figure 3 plots the three next-day measures against the size of the day-$t$ move. Inside the band the relation is monotone and negative: the larger the rise (fall), the lower (higher) the next-day abnormal return, which is the pattern of a short-term reversal. At the limit the relation breaks. The overnight gap jumps up at the ceiling and down at the floor, and the close-to-close return changes sign relative to the adjacent bins. This is the shape expected if the limit prevents the full adjustment on day $t$ and the unfilled part is realized at the next open.

Table 5. Difference in next-day abnormal returns between stocks closing at the limit and stocks that moved 3\<U+2013\>5% or 5\<U+2013\>6.5% in the same direction without closing at the limit.

| Contrast             | Outcome                  | Difference (pp) | t (date-clustered) | n (limit) | n (comparison) |
|----------------------|--------------------------|-----------------|--------------------|-----------|----------------|
| ceiling vs 5-6.5% up | Overnight gap            | 2.67            | 13.7               | 3,136     | 1,696          |
| ceiling vs 5-6.5% up | Intraday                 | -0.34           | -2.2               | 3,136     | 1,696          |
| ceiling vs 5-6.5% up | Close-to-close           | 2.29            | 6.7                | 2,819     | 1,480          |
| ceiling vs 5-6.5% up | Next open to day-5 close | -0.06           | -0.2               | 3,136     | 1,696          |
| ceiling vs 3-5% up   | Overnight gap            | 2.40            | 11.4               | 3,136     | 5,768          |
| ceiling vs 3-5% up   | Intraday                 | -0.32           | -2.2               | 3,136     | 5,768          |
| ceiling vs 3-5% up   | Close-to-close           | 2.00            | 5.4                | 2,819     | 5,122          |
| ceiling vs 3-5% up   | Next open to day-5 close | -0.47           | -2.3               | 3,136     | 5,768          |
| floor vs 5-6.5% down | Overnight gap            | -1.58           | -9.5               | 2,088     | 1,462          |
| floor vs 5-6.5% down | Intraday                 | -0.07           | -0.3               | 2,088     | 1,462          |
| floor vs 5-6.5% down | Close-to-close           | -1.72           | -10.9              | 1,829     | 1,251          |
| floor vs 5-6.5% down | Next open to day-5 close | -0.97           | -2.4               | 2,088     | 1,462          |
| floor vs 3-5% down   | Overnight gap            | -1.14           | -6.3               | 2,088     | 5,024          |
| floor vs 3-5% down   | Intraday                 | 0.14            | 0.6                | 2,088     | 5,024          |
| floor vs 3-5% down   | Close-to-close           | -1.06           | -7.1               | 1,829     | 4,330          |
| floor vs 3-5% down   | Next open to day-5 close | -0.87           | -2.1               | 2,088     | 5,024          |

Table 5. Difference in next-day abnormal returns between stocks closing at the limit and stocks that moved 3\<U+2013\>5% or 5\<U+2013\>6.5% in the same direction without closing at the limit.

Table 5 quantifies the break. Relative to stocks that rose 5–6.5% on day $t$, stocks that closed at the ceiling have an overnight gap that is 2.67 percentage points larger (t = 13.7) and an intraday return that is 0.34 points lower (t = -2.2). For floors the gap is 1.58 percentage points lower than for stocks that fell 5–6.5% (t = -9.5). Because the comparison groups moved almost as far on day $t$, the difference is not a generic reversal or continuation after large moves; it is attached to the limit itself. This is an association around a rule-based threshold, not a randomized or exact regression-discontinuity design: stocks that reach the limit may differ in news content, and we do not claim a causal effect of the limit on prices.

## 4.5 Robustness (post hoc)

Table 6. Next-day abnormal returns (%) with date-clustered t-statistics in parentheses, by sub-sample.

| Sample                                       | Gap          | Intraday     | Close-to-close | Close-to-close vs same-date, same-liquidity controls |
|----------------------------------------------|--------------|--------------|----------------|------------------------------------------------------|
| ceiling all                                  | 2.26 (10.6)  | -0.55 (-3.7) | 1.63 (4.3)     | 2.20 (11.6)                                          |
| ceiling first half                           | 2.22 (5.5)   | -0.78 (-3.3) | 1.38 (2.2)     | 2.20 (11.6)                                          |
| ceiling second half                          | 2.31 (21.4)  | -0.32 (-3.0) | 1.95 (12.6)    | \<U+2014\>                                           |
| ceiling excl. market-crash days (mkt \< -2%) | 2.26 (9.4)   | -0.58 (-3.6) | 1.64 (4.2)     | 2.16 (11.4)                                          |
| ceiling locked all day (open=high=low=close) | 2.91 (3.0)   | -1.30 (-6.0) | 1.36 (1.2)     | 2.88 (4.5)                                           |
| ceiling not locked all day                   | 2.14 (16.3)  | -0.41 (-4.2) | 1.68 (7.9)     | 2.14 (10.5)                                          |
| ceiling liquidity tercile 1 (low)            | 3.38 (9.8)   | -0.57 (-1.5) | 2.67 (7.3)     | 2.88 (10.2)                                          |
| ceiling liquidity tercile 2 (mid)            | 3.30 (15.9)  | -0.86 (-4.7) | 2.38 (8.8)     | 2.42 (9.4)                                           |
| ceiling liquidity tercile 3 (high)           | 1.88 (10.0)  | -0.49 (-2.2) | 1.35 (5.0)     | 1.39 (4.8)                                           |
| floor all                                    | -0.98 (-4.9) | 0.31 (1.4)   | -0.78 (-5.3)   | -0.99 (-2.4)                                         |
| floor first half                             | -0.55 (-2.4) | -0.09 (-0.3) | -0.59 (-2.8)   | -0.99 (-2.4)                                         |
| floor second half                            | -1.44 (-8.2) | 0.71 (4.5)   | -1.03 (-5.8)   | \<U+2014\>                                           |

Table 6. Next-day abnormal returns (%) with date-clustered t-statistics in parentheses, by sub-sample.

The pattern is not driven by one part of the sample (Table 6). It appears in both halves, outside market-crash days (days on which the market fell more than 2%), in each liquidity tercile and on days when the stock was locked at one price from open to close, which is the case in which unfilled interest is most plausible. The overnight gap on locked ceiling days (2.91%) is larger than on other ceiling days (2.14%), and the intraday giveback is also larger on locked days (-1.30%). Using same-date, same-liquidity non-event stocks as the control instead of the market leaves the close-to-close effect essentially unchanged (2.20% for ceilings, -0.99% for floors). The estimates are heterogeneous in size: the ceiling effect is larger in the second half of the sample, and for floors the effect is not significant in the least liquid tercile (close-to-close t = 0.6).

## 4.6 What can an investor do with it?

The close-to-close continuation is not available to an outside buyer. A stock that closes at its ceiling typically cannot be bought at that close, so the first price at which it can be bought is the next open, which already contains the gap. Measured from that open, the abnormal return of ceiling stocks is -0.55% within the day (t = -3.7) and -0.79% through the fifth close (t = -3.7); 58% of ceiling events have a negative intraday abnormal return. A long-only investor therefore gains nothing from chasing ceiling stocks at the open, and a holder of a ceiling stock who sells at the next open instead of at the close captures 0.55 percentage points on average. Short selling the intraday reversal is not feasible in this market without borrowing. Trading costs would further reduce any intraday strategy: for the 21 banks in the same data, a Corwin–Schultz spread proxy averages about 59 basis points (an upward-biased estimator).

# 5. Discussion

**Interpretation.** The evidence fits delayed price discovery in the sense of Kim and Rhee (1997) and the continuation reported by Berkman and Lee (2002), with an important refinement on timing: the continuation is not spread over the next days but concentrated in the opening, and the intraday return that follows reverses part of it. Berkman et al. (2012) document, for U.S. stocks, positive overnight returns followed by intraday reversals, driven by an opening price that is high relative to intraday prices and concentrated among stocks that recently attracted retail attention, with high net retail buying at the start of the day. The signature we find after ceiling closes (a large overnight gain and a partial intraday giveback) is the same. Lou et al. (2019) show that overnight and intraday returns have different persistence and that heterogeneous traders can explain the difference. Our data cannot identify who trades, so we offer the unfilled-demand and retail-attention readings as consistent with the evidence, not as a test of it; what is specific to the present setting is that the gap is tied to a regulatory constraint on the previous day’s price. The weak intraday reversal at the floor is consistent with limited buying capacity for stocks that cannot be shorted, but we do not test that.

**Why the limit-day return does not behave like the 3–6.5% days.** Moves inside the band show the familiar reversal; moves at the band show a gap. If the limit were just a large move, the 5–6.5% bin should lie on the trend line of the interior bins and the limit bin on its extension. It does not (Figure 3, Table 5). This points to a mechanism attached to the constraint and is the main reason we describe the result as a discontinuity.

**Relation to the characteristic zoo.** The limit result stands out because every other characteristic in the same family is null. The two findings are compatible: limit hits are rare (about 1.6% of stock-days close at the ceiling by the pre-registered rule and about 0.8% by the exact tick rule), whereas the characteristics are measured on all stocks every week. We therefore do not claim that limit hits explain the cross-section of returns, only that they carry large and precisely estimated next-day information in the days that follow them.

**Implications.** For regulators, the evidence says that the limit does not settle the price on the limit day: the next opening does part of the work, with gaps of about two percentage points for ceiling closes and one percentage point for floor closes. For investors, it argues against chasing limit-up stocks at the open and for treating the next open as the point at which the day-$t$ pressure is realized.

# 6. Limitations

1)  The sample is about 21 months (519 trading days), which is short; the pre-registered family and the hold-out half address this, but a longer sample is desirable and is partly supplied by the independent public analysis (tungtran0911, 2026). (ii) There are no order-book or investor-type data, so the unfilled-demand mechanism is inferred. (iii) The 7% limit is checked indirectly (Table 1) but not against exchange documents; the reference price, tick sizes and any rule changes during the sample are assumptions of the exact-tick definition. (iv) Prices may be adjusted for corporate actions in ways that affect limit-hit classification; the pre-registered rule and the exact tick rule give the same sign and similar sizes, which limits but does not eliminate this concern. (v) The decomposition, control group, discontinuity and robustness analyses are post hoc, although they were motivated by the pre-registered result and are reported in full; they should be read as explanations of a pre-registered finding. (vi) The characteristic tests use one-at-a-time Fama–MacBeth regressions; multivariate and non-linear specifications were not part of the pre-registered family. (vii) Clustered standard errors treat dates and stocks as the dependence dimensions; events in the same market episode may be more strongly dependent than that allows.

# 7. Conclusion

In a pre-registered family of 26 tests on 347 HOSE stocks, none of 22 familiar price- and volume-based characteristics survives false-discovery-rate control and a hold-out half, whereas all four price-limit tests do. A ceiling close is followed by a next-day abnormal return of about +1.7%, entirely through an overnight gap that is 2.7 percentage points larger than for stocks that rose 5–6.5% without hitting the limit, and then by an intraday reversal. The result is a feature of the opening after a limit close, not a profit opportunity for investors who buy after the close.

# Declarations

**Use of artificial intelligence.** The analysis code, tables and manuscript draft were produced with the assistance of Claude (Anthropic) under the Academic Research Skills workflow; the authors are responsible for verifying all choices, results and references before submission. Reference verification status is in `process/04_literature_search_log.md`.

**Data and code availability.** Code in `paper2/R/` (scripts 40–45), derived tables in `paper2/output/tables/` (C1–C10), and this manuscript’s source regenerate every number from saved output.

**Ethics, funding, competing interests, author contributions.** \[To be completed by the authors.\]

# References

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56.

Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. *Journal of Financial Economics, 99*(2), 427–446.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological), 57*(1), 289–300. <https://doi.org/10.1111/j.2517-6161.1995.tb02031.x>

Berkman, H., & Lee, J. B. T. (2002). The effectiveness of price limits in an emerging market: Evidence from the Korean Stock Exchange. *Pacific-Basin Finance Journal, 10*(5), 517–530.

Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). Paying attention: Overnight returns and the hidden cost of buying at the open. *Journal of Financial and Quantitative Analysis, 47*(4), 715–741.

Brennan, M. J. (1986). A theory of price limits in futures markets. *Journal of Financial Economics, 16*(2), 213–233. <https://doi.org/10.1016/0304-405X(86)90061-9>

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2011). Robust inference with multiway clustering. *Journal of Business & Economic Statistics, 29*(2), 238–249. <https://doi.org/10.1198/jbes.2010.07136>

Chen, Y.-M. (1993). Price limits and stock market volatility in Taiwan. *Pacific-Basin Finance Journal, 1*(2), 139–153.

Cho, D. D., Russell, J., Tiao, G. C., & Tsay, R. S. (2003). The magnet effect of price limits: Evidence from high-frequency data on Taiwan Stock Exchange. *Journal of Empirical Finance, 10*(1–2), 133–168.

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. <https://doi.org/10.1111/j.1540-6261.2012.01729.x>

Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium: Empirical tests. *Journal of Political Economy, 81*(3), 607–636. <https://doi.org/10.1086/260061>

Harvey, C. R., Liu, Y., & Zhu, H. (2016). …and the cross-section of expected returns. *The Review of Financial Studies, 29*(1), 5–68. <https://doi.org/10.1093/rfs/hhv059>

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.

Imbens, G. W., & Lemieux, T. (2008). Regression discontinuity designs: A guide to practice. *Journal of Econometrics, 142*(2), 615–635.

Kim, K. A., & Rhee, S. G. (1997). Price limit performance: Evidence from the Tokyo Stock Exchange. *The Journal of Finance, 52*(2), 885–901. <https://doi.org/10.1111/j.1540-6261.1997.tb04827.x>

Lou, D., Polk, C., & Skouras, S. (2019). A tug of war: Overnight versus intraday expected returns. *Journal of Financial Economics, 134*(1), 192–213. <https://doi.org/10.1016/j.jfineco.2019.03.011>

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica, 55*(3), 703–708. <https://doi.org/10.2307/1913610>

Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. *The Journal of Business, 53*(1), 61–65.

tungtran0911. (2026). *vn-equity-factors* \[Source code\]. GitHub. Retrieved October 4, 2026, from <https://github.com/tungtran0911/vn-equity-factors>

Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price discovery and momentum strategies: Evidence from Vietnam* (SSRN Scholarly Paper No. 1009042). Social Science Research Network. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1009042>

# Appendix A. Pre-registered versus post hoc analyses

| Analysis                                                                                                | Status         |
|---------------------------------------------------------------------------------------------------------|----------------|
| 22 characteristics, Fama–MacBeth, quintile spreads, discovery/confirmation split, illiquidity exclusion | Pre-registered |
| Ceiling and floor event tests at t+1 and t+1..t+5; BH/Holm/HLZ control over 26 tests; survival rule     | Pre-registered |
| Overnight–intraday decomposition; next-open returns; same-date liquidity-matched control                | Post hoc (A4)  |
| Comparison with 3–5% and 5–6.5% moves; discontinuity plot and table                                     | Post hoc (A4)  |
| Exact tick-rule definition; two-way clustering; sub-sample robustness                                   | Post hoc (A4)  |

# Appendix B. Code and reproducibility

`R/40_zoo.R` (family of 26 tests), `R/41_limits_robust.R` (event-level post hoc analyses), `R/42_rd.R` (bins, tick rule, two-way clustering), `R/43_disc.R` (discontinuity comparisons), `R/44_desc.R` (pile-up and counts), `R/45_figuresC.R` (figures). Seeds are fixed. The decisions log records the pre-registration (A3) and the post hoc amendment (A4).

# Appendix C. Literature search and verification

The search strategy, the prior-art finding that bounds the novelty claim, and the verification status of every reference are in `process/04_literature_search_log.md`. References marked “author-supplied or recalled” in that log (Harvey et al., Newey & West) are to be verified before submission.
