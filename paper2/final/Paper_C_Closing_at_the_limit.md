**Abstract.** Daily price limits are meant to cool markets, but they can
also postpone price discovery. Using daily open–high–low–close–volume
data on 347 stocks of the Ho Chi Minh Stock Exchange (HOSE; 21 August
2024 to 23 September 2026, 178,773 stock-days), we examine a family of
26 tests whose specification was fixed in a version-controlled project
log before the results were computed (it is not an external registry
entry): 22 price- and volume-based characteristics as predictors of
next-week returns and four price-limit event tests. After
false-discovery-rate control and a confirmation half-sample (not a
strict hold-out), 0 of the 22 characteristics survive (largest absolute
Fama–MacBeth t-statistic 1.45; the tests can rule out only slopes above
roughly 0.1–0.3 percentage points per week), while the four limit tests
survive, also with calendar-week-clustered errors. For ceilings,
survival at the five-day horizon is carried by day t+1: abnormal returns
over days t+2 to t+5 are not significant (-0.24%, t = -1.5); for floors,
days t+2 to t+5 add a further -1.10% that does not pass the confirmation
half. A stock that closes at its daily ceiling earns an abnormal return
of 1.66% on the next day (date-clustered t = 4.9, 3,187 events), and a
stock that closes at its floor earns -0.71% (t = -5.3; the floor figure
depends on the benchmark and is -1.65% against same-date controls).
Analyses added after seeing these results show that the ceiling effect
is an overnight gap (2.23%, two-way-clustered t = 9.8) followed by a
partial intraday reversal (-0.53%, t = -3.5), and that the gap is 2.66
percentage points larger than for stocks that rose 5–6.5% without
reaching the limit (t = 14.0), and 3.14 points larger when those
comparison stocks also closed at their day’s high. We read this as a
break at the limit that is consistent with demand blocked by the limit
being realized at the next opening, but the design cannot separate that
from news and attention: the gap is larger after strong prior run-ups
and heavy volume. The effect is not available to an outside buyer:
buying at the quoted next open and holding to the fifth close returns
-0.75% relative to the market (t = -2.7) and -0.53% relative to
same-date liquidity-matched controls (t = -1.8). A public,
non-peer-reviewed analysis whose longer sample contains our window
reports a close-to-close ceiling effect of similar size; our incremental
content is the overnight–intraday decomposition, the comparison with
moves just below the limit, and the multiplicity-controlled frame, and
the sample is a single exchange with a trading-platform change in May
2025.

**Keywords:** price limits; overnight returns; multiple testing;
Vietnam; retail investors

**JEL classification:** G14; G15; G18

**Tóm tắt.** Bài viết kiểm định một họ 26 giả thuyết trên 347 cổ phiếu
HOSE (8/2024–9/2026): 22 đặc trưng giá–khối lượng và 4 kiểm định sự kiện
chạm giá trần/giá sàn. Đặc tả được cố định trong nhật ký dự án có kiểm
soát phiên bản trước khi tính kết quả; đây không phải đăng ký với cơ
quan bên ngoài, và nhóm tác giả đã hoàn thành các bản thảo trước trên dữ
liệu liên quan. Sau khi kiểm soát tỷ lệ phát hiện sai và dùng nửa mẫu
xác nhận (không phải mẫu giữ lại nghiêm ngặt), 0 đặc trưng sống sót và 4
kiểm định sự kiện sống sót; kiểm định 5 ngày chủ yếu do ngày t+1 quyết
định. Cổ phiếu đóng cửa ở giá trần có lợi suất bất thường ngày kế tiếp
1.66% (t = 4.9), toàn bộ đến từ khoảng trống giá qua đêm (2.23%), sau đó
đảo chiều một phần trong phiên (-0.53%). Nhà đầu tư mua ở giá mở cửa kế
tiếp không có lợi nhuận bất thường dương. Cơ chế (nhu cầu bị giới hạn
chặn lại hay tin tức và sự chú ý) chưa thể phân biệt bằng dữ liệu hiện
có. Một phân tích công khai chưa qua bình duyệt đã báo cáo hiệu ứng đóng
cửa–đóng cửa tương tự.

# 1. Introduction

A daily price limit stops a stock from moving beyond a fixed band on a
single day. Price limits have a theoretical rationale in futures markets
(Brennan, 1986). In equity markets, advocates argue that limits reduce
volatility and counter overreaction, while critics argue that they delay
price discovery, spill volatility into later days and interfere with
trading (Kim & Rhee, 1997). Theory also warns that trading halts can
advance trades in time and raise price variability (Subrahmanyam, 1994).
Kim and Rhee (1997) find support for all three critical hypotheses on
the Tokyo Stock Exchange, Bildik and Gülay (2006) report support for
volatility spillover, delayed price discovery and trading interference
on the Istanbul Stock Exchange, Chen (1993) finds that return serial
correlation falls as the limit widens in Taiwan, Berkman and Lee (2002)
report more frequent price continuations after limit hits on the Korean
Stock Exchange, and Cho et al. (2003) document a magnet effect toward
the upper limit in intraday Taiwanese data. For the closest
institutional analogue, the Chinese A-share market with retail-dominated
trading and daily bands, Qi (2023) studies the widening of the ChiNext
band from 10% to 20% and reports delayed price discovery, volatility
spillover and trading interference, stronger at the lower limit, and no
magnet effect; the Chinese evidence is mixed across studies and designs.
Evidence for Vietnam is thinner. Le (2012) studies the effect of
narrowing the fluctuation limit on stock price risk in Vietnam with
GARCH models, Veeraraghavan et al. (2007; an SSRN working paper) study
momentum and price limits on the Vietnamese exchange for 2000–2006, and
an open analysis posted on GitHub (tungtran0911, 2026; not peer
reviewed) reports that stocks closing at the HOSE ceiling earn a further
1.69% the next session while stocks that rise 3–6.5% give back 0.39%.

We ask a narrower question than whether limits “work”. On a stock-day
basis, does closing at the limit predict the next day’s return, how much
of that prediction is the overnight gap versus the trading session that
follows, and is the prediction available to an investor who was not
already holding the stock? The limit result is the contribution; the 22
characteristics play a supporting role. Because an investigator who
searches many ideas will find a large effect by luck, we place the four
limit tests in one family of 26 tests with the 22 familiar price- and
volume-based characteristics, apply false-discovery-rate control
(Benjamini & Hochberg, 1995; Harvey et al., 2016) and ask whether the
limit effect survives while the characteristics do not. The
characteristic half has limited power (Section 4.7) and is reported as a
multiplicity device and a null benchmark, not as a separate finding
about the cross-section.

**Contributions and novelty.** To our knowledge, among the sources our
search reached (Appendix C), no peer-reviewed study documents the
following for HOSE: (i) a decomposition of the next-day effect into the
overnight gap and the intraday return, showing that the continuation is
a gap and that the following session reverses part of it; (ii) a
comparison with stocks that moved nearly as far without reaching the
limit, including stocks that also closed at their day’s high; and (iii)
a multiplicity-controlled frame in which the same data yield no
surviving characteristic. We separate what is confirmatory from what is
exploratory. Confirmatory in the weak sense of fixed before computation
in a project log: the four close-to-close and five-day event tests and
the null for the 22 characteristics. Exploratory (post hoc): the
decomposition, the comparison groups, the exact tick-rule definition,
the sub-samples, the platform-change split and the attention proxies.
The close-to-close ceiling effect is the confirmatory part and is also
the part that is already public; the decomposition and the comparison
with sub-limit moves are the new part and are exploratory.

We do not claim to be first to document the close-to-close ceiling
effect, nor its interpretation. tungtran0911 (2026) reports a
close-to-close next-session effect of 1.69% after closes at or near the
ceiling, a reversal after 3–6.5% rises, a mechanism in which the close
is not a market-clearing price and the next session completes the move,
and the inference that outsiders cannot capture the gap. Their sample
(404 stocks, 2016–2026) contains our window, they define events by a
return of at least 6.5% without requiring the close to equal the day’s
high, and they use an equal-weighted benchmark; our estimate under their
definition (a return of at least 6.5%) and an equal-weighted benchmark
is 1.75% (1.87% under our stricter rule that also requires the close to
equal the day’s high). Our result is therefore consistent with theirs
but is not an independent replication: it uses the same exchange, an
overlapping period and, at least partly, the same data vendor family.
The overnight-gain-then-intraday-reversal signature is known from U.S.
data for attention-grabbing stocks without any price limit (Berkman et
al., 2012), so the gap-then-giveback pattern alone does not point to the
limit. What a price limit adds is a testable contrast: if the limit is
irrelevant, stocks that rose almost as much (5–6.5%) and also closed at
their high should show the same gap. We test that contrast (Section
4.4); the answer is that they do not, although a difference in news
content cannot be excluded.

The remainder of the paper describes the data and design (Sections 2 and
3), reports results (Section 4), and discusses implications and
limitations (Sections 5 and 6).

# 2. Data

The raw data are daily open, high, low, close and volume for 405
HOSE-listed stocks from 21 August 2024 to 23 September 2026, retrieved
with the vnstock library; the stock list is a listing file from the VCI
source dated 24 September 2026, so the universe is a snapshot of stocks
listed at that date. We keep the 347 stocks with at least 95%
non-missing prices (178,773 stock-days with a return). Returns are
close-to-close. The market return is the dollar-volume-weighted return
of all stocks, with weights from the trailing 60-day average dollar
volume; stock abnormal returns are stock returns minus the market return
over the same interval. The vendor does not document whether prices are
adjusted for corporate actions.

HOSE’s daily price limit is 7% around the reference price (the previous
close on normal trading days), with a wider band on the first trading
day of a newly listed stock, and the band was not changed by the move to
the KRX trading platform on 5 May 2025 (HSC, 2025; Viet Nam News, 2025;
these are brokerage and press descriptions of the exchange rules, not
the exchange circulars, which we did not consult, so the rule is still
treated as an assumption that we check against the data). The platform
change matters for our design: the closing price that defines an event
and the opening price that defines the gap are both call-auction prices,
and under the new system the at-the-open (ATO) and at-the-close (ATC)
orders no longer have priority over limit orders in the auctions (HSC,
2025; Viet Nam News, 2025). The window therefore contains a
trading-system regime change at about month 9 of 25 (Section 4.8). Table
1 shows that 1.98% of stock-days have a return between +6.5% and +7.1%
and 1.30% between −7.1% and −6.5%, against 0.29% between +6.0% and
+6.5%, 0.010% between +7.1% and +8.0%, and 0.064% beyond ±7.1%, which is
the pile-up expected from a 7% limit. Returns beyond ±7.1% can arise
from first-day listing bands, resumed trading, or unadjusted corporate
actions; Section 4.7 reports that excluding events within five days of
such returns leaves the estimates unchanged, but we do not investigate
their individual causes.

Table 1. Distribution of daily returns around the 7% limit, 347 analysed
stocks.

| Close-to-close return | Stock-days | Share (%) |
|-----------------------|------------|-----------|
| \< -8.0%              | 38         | 0.021     |
| -8.0% to -7.1%        | 2          | 0.001     |
| -7.1% to -6.9%        | 1,136      | 0.635     |
| -6.9% to -6.5%        | 1,193      | 0.667     |
| -6.5% to -6.0%        | 459        | 0.257     |
| -6.0% to 6.0%         | 171,809    | 96.105    |
| 6.0% to 6.5%          | 514        | 0.288     |
| 6.5% to 6.9%          | 1,925      | 1.077     |
| 6.9% to 7.1%          | 1,622      | 0.907     |
| 7.1% to 8.0%          | 17         | 0.010     |
| \> 8.0%               | 58         | 0.032     |

We do not observe order books, trade sizes by investor type, or intraday
prices beyond the high and the low. Market capitalization is also
unavailable for this sample, which is why the market return uses
dollar-volume weights.

# 3. Design

## 3.1 A log-specified family of 26 tests

Before computing any result we fixed the family, the estimators, the
multiplicity controls and the survival rule in a time-stamped internal
decision log (`process/03_brainstorm_round2.md`, `process/decisions.md`
A3). “Specified in advance” here means fixed in that log before the
results were computed; it is not an external registry entry, and the
earlier manuscripts of the same project (on portfolio construction) had
already been completed on related data, so the specification is not
independent of the project’s prior results (Section 6). What can be
checked from outside is the order of events in the version-controlled
repository: the file `process/03_brainstorm_round2.md`, which contains
the family, the estimators, the multiplicity controls and the survival
rule, was committed at 07:23:38 UTC on 4 October 2026 (commit 63bdc6d;
SHA-256 of the file as committed 3d6dc7e1ff57…026effaf; full value in
Appendix A), and the first commit that contains the analysis code and
any result tables (commit 9b8644b) is dated 07:36:19 UTC the same day.
Commit dates are set by the committer and are not an independent time
stamp; only the push times recorded by the repository host are external,
and the authors should deposit the files with an independent time stamp
before submission. We use the words “log-specified” in the sense just
defined and not as “pre-registered”. The family is 22 characteristics
measured at the end of each week and four price-limit event tests.

*Characteristics.* Momentum and reversal: 5-day return (REV1W), 20-day
return (REV1M), 60-day return skipping 5 days (MOM3M), 110-day return
skipping 5 days (MOM6M), 60-day idiosyncratic momentum (IMOM). Risk:
60-day volatility (VOL), idiosyncratic volatility (IVOL), market beta
(BETA), downside deviation (DOWNVOL), Parkinson (1980) range volatility
(RANGEVOL), maximum daily return in 20 days (MAX; Bali et al., 2011),
minimum daily return (MIN), skewness (SKEW), kurtosis (KURT). Liquidity
and volume: Amihud (2002) illiquidity (AMIHUD), log dollar volume
(LNDVOL), 20/60-day dollar-volume ratio (DVOLCHG) and volume ratio
(TURNCHG), the Corwin and Schultz (2012) spread (CSSPREAD). Intraday:
mean overnight return (OVERNIGHT), mean intraday return (INTRADAY),
share of days with a move of 6.5% or more (LIMITFREQ). Each is
rank-normalized in the cross-section.

*Estimator.* Weekly Fama and MacBeth (1973) cross-sectional regressions
of the next five trading days’ abnormal return on one standardized
characteristic at a time, with Newey and West (1987) t-statistics (4
lags) on the time series of slopes; 79 weekly cross-sections (the first
decision is on trading day 120 to allow the longest lookback, then every
fifth day, giving 79 decisions in the 519-day sample). The first 39
weeks are the discovery half and the remaining 40 the confirmation half.
For each characteristic we also report the long–short quintile spread
(equal weighted) net of a cost of 25 basis points per unit of traded
value, and the t-statistic after excluding the least liquid 20% of
stocks.

*Limit events.* A ceiling event is a day with a return of at least +6.5%
and a close equal to the day’s high; a floor event is a return of at
most −6.5% with a close equal to the day’s low. Outcomes are the
market-adjusted return on day $t + 1$ and cumulatively over days $t + 1$
to $t + 5$ (the specification names the horizons both as “$t + 1$ and
$t + 2$ to $t + 5$” and, when it counts the family, as “$t + 1$, $t + 1$
to $t + 5$”; we implemented the second reading and report the days
$t + 2$ to $t + 5$ outcome in Section 4.2). Inference uses the
cross-sectional mean with standard errors clustered by date. These are
the four event tests (ceiling and floor, two horizons).

*Multiplicity.* The 26 p-values are adjusted by Benjamini–Hochberg (5%
false-discovery rate) and by Holm (1979); we also report the Harvey et
al. (2016) threshold of \|t\| = 3. A test *survives* if its adjusted
p-value is below 5% and, in addition, its sign in the discovery half
agrees with the full sample and the confirmation-half \|t\| exceeds
1.96.

*Deviations between the specification and the implementation.* (a) The
specification described the event horizons as day $t + 1$ and days
$t + 2$ to $t + 5$ in one place and as $t + 1$ and $t + 1$ to $t + 5$ in
the family count; we implemented the cumulative return over days $t + 1$
to $t + 5$ and report the other horizon in Section 4.2. (b) The
specification asked for decile spreads and we report quintile spreads;
it listed a same-stock non-event control and a multivariate model of the
surviving characteristics; neither was implemented (no characteristic
survived; the control was replaced by a same-date control in Section
4.7). (c) For the event tests the first-half and second-half samples are
split at the median event date, not at weeks 39 and 40 (the split at
weeks 39 and 40 is reported in Table 3b). (d) The specification of the
3-month momentum and idiosyncratic momentum windows was 60 days; an
early version of the code used 59 days; the window was corrected to 60
days after the first independent integrity review and all dependent
tables were regenerated (the t-statistics changed from 1.55 to 1.45 and
from 1.53 to 1.45). (e) Table 3 uses dollar-volume weights through day
$t + 1$ for the market return; on the same events, lagged weights give
1.667% instead of 1.660%, and lagged weights are used in Tables 4 to 8.

The event window runs from trading day 61 (so that 60 days of trailing
dollar volume exist) to five trading days before the last day;
stock-days outside it are not events.

## 3.2 Post hoc analyses

The following analyses were added **after** seeing that the limit tests
survive; they are labelled post hoc throughout (`process/decisions.md`
A4): (a) decomposition of day $t + 1$ into the overnight gap (open at
$t + 1$ over close at $t$) and the intraday return (close over open at
$t + 1$); (b) returns measured from the next open, which is what an
investor entering after the close can obtain, since a stock that closes
at its ceiling usually cannot be bought at that close; (c) a control
group of stocks in the same liquidity tercile on the same date; (d) a
comparison with days on which stocks rose or fell 3–5% or 5–6.5% without
hitting the limit; (e) an exact tick-rule definition of the limit hit
(the close equals the previous close times 1.07, rounded to the price
tick, assuming ticks of 0.01, 0.05 and 0.10 thousand VND below 10, below
50 and from 50); (f) two-way (date and stock) clustering (Cameron et
al., 2011); (g) sub-samples (halves, market-crash days, liquidity
terciles, days with the stock locked at one price from open to close);
(h) a plot of next-day returns by the size of the day-$t$ move (Imbens &
Lemieux, 2008); and, added after the first round of independent review,
(i) inference for the event tests with calendar-week and 10-day-block
clusters and a t reference, and the outcome for days $t + 2$ to $t + 5$;
(j) a split at the trading-platform change of 5 May 2025; (k) comparison
groups that also close at their day’s high or low; (l) volume and
prior-return terciles as proxies for news and attention; and (m) an
exclusion of events near returns beyond ±8%.

# 4. Results

## 4.1 The 22 characteristics

Table 2. Fama–MacBeth results for the 22 characteristics specified in
the log (ordered by absolute full-sample t-statistic).

| Characteristic | Slope (% per week, per s.d.) | t (full) | t (discovery) | t (confirmation) | t (excl. least liquid 20%) | Quintile spread, net of 25 bps (% per week) |
|----------------|------------------------------|----------|---------------|------------------|----------------------------|---------------------------------------------|
| MOM3M          | 0.123                        | 1.45     | 0.87          | 1.17             | 1.49                       | 0.092                                       |
| IMOM           | 0.123                        | 1.45     | 0.89          | 1.14             | 1.48                       | 0.090                                       |
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

<img src="media/rId25.png" style="width:5.83333in;height:4.66667in"
alt="Figure 1. Fama-MacBeth t-statistics of the 22 characteristics: full sample, discovery half and confirmation half." />

Figure 1. Fama-MacBeth t-statistics of the 22 characteristics: full
sample, discovery half and confirmation half.

None of the 22 characteristics has a full-sample \|t\| above 1.45 (Table
2, Figure 1), none passes the Harvey et al. (2016) threshold of 3, and
none survives the family-wide control. The leading candidates, 3-month
and idiosyncratic momentum, have t-statistics of 1.45 and 1.45, with
confirmation-half t-statistics of 1.17 and 1.14. Standard risk measures
are weak in this cross-section: volatility has t = -0.09, idiosyncratic
volatility -0.54, and MAX -0.02. The long–short quintile spreads are
small and, net of 25 basis points per unit traded, mostly negative; no
characteristic combines a significant slope with a spread that survives
costs. The tests have limited power with 79 cross-sections, so the null
is informative mainly about effects as large as a few tenths of a
percent per week.

## 4.2 The four limit tests specified in advance

Table 3. Price-limit event tests specified in the log: market-adjusted
returns after a ceiling or floor close. Events require complete returns
for days t+1 to t+5, so Table 3 has slightly fewer events than Table 4,
which requires only the open and close of day t+1; later tables use the
lagged-weight market and the samples stated in their notes.

| Event   | Horizon  | Mean abnormal return (%) | t (date-clustered) | Events | Dates | t (first half) | t (second half) |
|---------|----------|--------------------------|--------------------|--------|-------|----------------|-----------------|
| ceiling | t+1      | 1.66                     | 4.91               | 3,187  | 446   | 2.28           | 14.36           |
| ceiling | t+1..t+5 | 1.45                     | 4.01               | 3,187  | 446   | 1.78           | 6.82            |
| floor   | t+1      | -0.71                    | -5.33              | 2,105  | 319   | -2.97          | -5.12           |
| floor   | t+1..t+5 | -1.76                    | -4.75              | 2,105  | 319   | -11.57         | -2.16           |

All four tests are significant, survive the Benjamini–Hochberg control
over the 26 tests (adjusted p-values between 2.6e-06 and 4.0e-04) and
keep the same sign in both halves of the sample with confirmation-half
\|t\| above 1.96 (Table 3). A ceiling close is followed by an abnormal
return of 1.66% the next day and 1.45% over five days; a floor close by
-0.71% and -1.76%. Of the 26 tests, 4 of 4 event tests and 0 of 22
characteristic tests survive.

Two features of this result need qualification, and Table 3b reports the
corresponding checks (post hoc). First, the date-clustered standard
errors of Table 3 ignore dependence between events on adjacent dates,
which is likely at the five-day horizon because windows overlap. With
calendar-week clusters (95 weeks) and 10-day-block clusters (46 blocks)
and a t reference with G−1 degrees of freedom, all four tests keep their
sign and remain significant: the ceiling five-day t-statistic falls from
4.01 (Table 3) to 3.67 and 3.81, and the confirmation-half t-statistic
of the floor five-day test, which clears 1.96 by the smallest margin, is
-2.16 with date clusters, -2.22 with week clusters and -2.46 with block
clusters. Re-applying the survival rule with week-clustered statistics
and t-based p-values (all 26 tests, Benjamini–Hochberg) leaves all four
event tests surviving (adjusted p-values up to 2.6e-03). The split at
weeks 39 and 40 that the specification called for gives the same
picture, with confirmation-half week-clustered t-statistics of 13.3,
3.8, -4.5 and -2.6. Second, the survival of the five-day tests is
carried by the first day. Over days $t + 2$ to $t + 5$ alone the ceiling
abnormal return is -0.24% (date-clustered t = -1.53; week-clustered
-1.11), which is not significant, and the floor return over the same
days is -1.10% (t = -2.91) in the full sample but not significant in the
second half (week-clustered t = -1.14, against a week-clustered
full-sample t of -3.01). If the horizon of the specification is read as
days $t + 2$ to $t + 5$ (Section 3.1), the ceiling test would therefore
not survive and the floor test would fail the confirmation-half
criterion. We read the evidence as a one-day effect after ceiling closes
and a one-day effect with some further drift after floor closes, not as
a multi-day continuation.

Table 3b. Inference for the event tests under alternative clustering
(post hoc). Same events and market-adjusted returns as Table 3; the
date-clustered t-statistics here use a G/(G−1) small-cluster correction
and differ slightly from Table 3. Halves: split at the median event
date. Weeks 1-39 / 40-79: the split of the specification, applied to
events from trading day 120.

| Event   | Horizon  | Mean (%) | t (date) | t (week) | t (10-day block) | t (halves, week) | t (weeks 1-39 / 40-79) |
|---------|----------|----------|----------|----------|------------------|------------------|------------------------|
| ceiling | t+1      | 1.66     | 4.90     | 4.67     | 4.61             | 2.2 / 13.7       | 2.4 / 13.3             |
| ceiling | t+1..t+5 | 1.45     | 4.00     | 3.67     | 3.81             | 1.7 / 5.0        | 2.0 / 3.8              |
| ceiling | t+2..t+5 | -0.24    | -1.53    | -1.11    | -1.25            | -1.1 / -0.4      | -0.8 / -1.1            |
| floor   | t+1      | -0.71    | -5.32    | -4.66    | -6.25            | -2.7 / -4.6      | -2.8 / -4.5            |
| floor   | t+1..t+5 | -1.76    | -4.74    | -4.80    | -4.92            | -12.3 / -2.2     | -3.9 / -2.6            |
| floor   | t+2..t+5 | -1.10    | -2.91    | -3.01    | -2.81            | -8.7 / -1.1      | -2.8 / -1.6            |

## 4.3 The effect is an overnight gap (post hoc)

Table 4. Decomposition of the next-day abnormal return into the
overnight gap and the intraday return, with three clustering schemes.
Upper block: events defined by the log-specified rule; lower block:
events defined by the exact tick rule.

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

<img src="media/rId30.png" style="width:5.83333in;height:2.83333in"
alt="Figure 2. Next-day abnormal return after a limit close, decomposed into the overnight gap and the intraday return (post hoc; two-way-clustered 95% intervals)." />

Figure 2. Next-day abnormal return after a limit close, decomposed into
the overnight gap and the intraday return (post hoc; two-way-clustered
95% intervals).

Table 4 and Figure 2 show where the next-day effect arises. After a
ceiling close the abnormal return from the previous close to the next
open is 2.23% (two-way-clustered t = 9.8); from the next open to the
next close it is -0.53% (t = -3.5). The total is positive only because
the gap exceeds the intraday giveback. After a floor close the gap is
-0.99% (t = -4.7) and the intraday return is a partial and statistically
weak reversal (0.31%, t = 1.4). The exact tick rule, which picks about
half as many events (1,666 ceilings), strengthens the estimates: the
ceiling gap is 2.76% (t = 13.5) and the intraday return -0.73% (t =
-5.3). The rule-based definition therefore includes some closes that
were near but not at the limit, and the log-specified estimate
understates the exact-limit effect.

## 4.4 A break at the limit (post hoc)

<img src="media/rId34.png" style="width:5.83333in;height:6in"
alt="Figure 3. Next-day abnormal return (overnight gap, intraday, close-to-close) by the size of the day-t move. Triangles: closed at the 7% limit; squares: moved more than 6.5% without closing at the limit (post hoc)." />

Figure 3. Next-day abnormal return (overnight gap, intraday,
close-to-close) by the size of the day-t move. Triangles: closed at the
7% limit; squares: moved more than 6.5% without closing at the limit
(post hoc).

Figure 3 plots the three next-day measures against the size of the
day-$t$ move. Inside the band the close-to-close relation is broadly
negative (the overnight-gap bins are noisier): the larger the rise
(fall), the lower (higher) the next-day abnormal return, which is the
pattern of a short-term reversal. At the limit the relation breaks. The
overnight gap jumps up at the ceiling and down at the floor, and the
close-to-close return changes sign relative to the adjacent bins. This
is one shape expected if the limit prevents the full adjustment on day
$t$ and the unfilled part is realized at the next open; the alternatives
are discussed at the end of this section.

Table 5. Difference in next-day abnormal returns (market-adjusted,
lagged weights) between stocks closing at the limit (rule-based
definition) and stocks that moved 3–5% or 5–6.5% in the same direction
without closing at the limit.

| Contrast             | Outcome                  | Difference (pp) | t (date-clustered) | n (limit) | n (comparison) |
|----------------------|--------------------------|-----------------|--------------------|-----------|----------------|
| ceiling vs 5-6.5% up | Overnight gap            | 2.66            | 14.0               | 3,199     | 1,751          |
| ceiling vs 5-6.5% up | Intraday                 | -0.31           | -2.1               | 3,199     | 1,751          |
| ceiling vs 5-6.5% up | Close-to-close           | 2.32            | 7.6                | 3,199     | 1,751          |
| ceiling vs 5-6.5% up | Next open to day-5 close | -0.02           | -0.1               | 3,193     | 1,742          |
| ceiling vs 3-5% up   | Overnight gap            | 2.40            | 11.6               | 3,199     | 5,932          |
| ceiling vs 3-5% up   | Intraday                 | -0.32           | -2.2               | 3,199     | 5,932          |
| ceiling vs 3-5% up   | Close-to-close           | 2.05            | 6.1                | 3,199     | 5,932          |
| ceiling vs 3-5% up   | Next open to day-5 close | -0.45           | -2.2               | 3,193     | 5,923          |
| floor vs 5-6.5% down | Overnight gap            | -1.59           | -9.7               | 2,111     | 1,522          |
| floor vs 5-6.5% down | Intraday                 | -0.07           | -0.3               | 2,111     | 1,522          |
| floor vs 5-6.5% down | Close-to-close           | -1.66           | -11.6              | 2,111     | 1,522          |
| floor vs 5-6.5% down | Next open to day-5 close | -1.01           | -2.6               | 2,108     | 1,512          |
| floor vs 3-5% down   | Overnight gap            | -1.14           | -6.4               | 2,111     | 5,237          |
| floor vs 3-5% down   | Intraday                 | 0.14            | 0.6                | 2,111     | 5,237          |
| floor vs 3-5% down   | Close-to-close           | -1.01           | -7.5               | 2,111     | 5,237          |
| floor vs 3-5% down   | Next open to day-5 close | -0.90           | -2.2               | 2,108     | 5,218          |

Table 5 quantifies the break. Relative to stocks that rose 5–6.5% on day
$t$, stocks that closed at the ceiling have an overnight gap that is
2.66 percentage points larger (t = 14.0) and an intraday return that is
0.31 points lower (t = -2.1). For floors the gap is 1.59 percentage
points lower than for stocks that fell 5–6.5% (t = -9.7). Because the
comparison groups moved almost as far on day $t$, the difference is not
a generic reversal or continuation after large moves. It could still
reflect that limit closers differ from the comparison stocks in more
than the limit. One such difference is the shape of the close: the event
rule requires the close to equal the day’s high (low), whereas the
comparison groups of Table 5 do not. Table 5b restricts the comparison
groups to stocks that also closed at their day’s high (low). The ceiling
gap is then 3.14 percentage points larger than for 5–6.5% risers that
closed at their high (t = 14.5; 679 comparison stock-days), and the
floor gap is 1.81 points lower (t = -8.7), so a strong close does not
account for the contrast. We describe the result as an association
around a rule-based threshold, not as a randomized or exact
regression-discontinuity design: there is no bandwidth choice, local
polynomial, manipulation test or covariate balance, and stocks that
reach the limit may differ in news content. We do not claim a causal
effect of the limit on prices.

Table 5b. As Table 5, with comparison stocks that also closed at their
day’s high (up moves) or low (down moves) (post hoc).

| Contrast                           | Outcome                  | Difference (pp) | t (date-clustered) | n (limit) | n (comparison) |
|------------------------------------|--------------------------|-----------------|--------------------|-----------|----------------|
| ceiling vs 5-6.5% up, close = high | Overnight gap            | 3.14            | 14.5               | 3,199     | 679            |
| ceiling vs 5-6.5% up, close = high | Intraday                 | -0.66           | -3.4               | 3,199     | 679            |
| ceiling vs 5-6.5% up, close = high | Close-to-close           | 2.47            | 7.2                | 3,199     | 679            |
| ceiling vs 5-6.5% up, close = high | Next open to day-5 close | -0.49           | -1.5               | 3,193     | 673            |
| ceiling vs 3-5% up, close = high   | Overnight gap            | 2.81            | 13.1               | 3,199     | 1,795          |
| ceiling vs 3-5% up, close = high   | Intraday                 | -0.61           | -3.8               | 3,199     | 1,795          |
| ceiling vs 3-5% up, close = high   | Close-to-close           | 2.17            | 6.4                | 3,199     | 1,795          |
| ceiling vs 3-5% up, close = high   | Next open to day-5 close | -0.64           | -2.7               | 3,193     | 1,790          |
| floor vs 5-6.5% down, close = low  | Overnight gap            | -1.81           | -8.7               | 2,111     | 722            |
| floor vs 5-6.5% down, close = low  | Intraday                 | -0.13           | -0.6               | 2,111     | 722            |
| floor vs 5-6.5% down, close = low  | Close-to-close           | -1.95           | -10.7              | 2,111     | 722            |
| floor vs 5-6.5% down, close = low  | Next open to day-5 close | -1.23           | -2.8               | 2,108     | 715            |
| floor vs 3-5% down, close = low    | Overnight gap            | -1.35           | -7.4               | 2,111     | 2,228          |
| floor vs 3-5% down, close = low    | Intraday                 | 0.18            | 0.8                | 2,111     | 2,228          |
| floor vs 3-5% down, close = low    | Close-to-close           | -1.19           | -8.0               | 2,111     | 2,228          |
| floor vs 3-5% down, close = low    | Next open to day-5 close | -1.06           | -2.5               | 2,108     | 2,218          |

*Rival readings.* Three readings fit the pattern, and the data do not
separate them. (1) Demand or supply that the limit prevented from
clearing on day $t$ is realized at the next opening, the reading of
delayed price discovery. (2) Stocks that reach a limit are selected on
news and retail attention, which persist overnight and are followed by
the familiar overnight-gain-then-intraday-reversal of attention-grabbing
stocks (Berkman et al., 2012), with or without a limit. (3) The opening
call auction overshoots and partly corrects within the day. The sample
contains no announcement data, no order book and no stock-days without a
limit regime, so we offer only two partial checks. Within ceiling events
the overnight gap rises with the day-$t$ volume relative to the prior
60-day mean (1.97%, 2.16% and 2.63% across terciles) and with the
stock’s prior 20-day return (1.41%, 2.18% and 3.16%; repository table
C24), so the gap is larger where attention and news are plausibly
stronger, which fits reading (2) as well as reading (1); it remains
positive and significant in the lowest tercile of each proxy (t = 4.8
for volume and 4.2 for prior return). For floors the pattern is not the
same: the gap moves from -1.20% to -0.68% across volume terciles (less
negative with more volume) and is not monotone in the prior return, so
the attention reading does not carry over cleanly to floors. The
contrast with 5–6.5% risers that also closed at their high (Table 5b)
removes selection on a strong close but not selection on news. The
intraday giveback after ceiling closes (-0.53%) fits readings (2) and
(3) at least as well as a permanent price-discovery story. We therefore
use “break at the limit” as a description, and “delayed price discovery”
as a hypothesis.

## 4.5 Robustness (post hoc)

Table 6. Next-day abnormal returns (%) by sub-sample, with
two-way-clustered t-statistics in parentheses. Market: dollar-volume
weights lagged to day t; controls: same-date non-event stocks in the
same liquidity tercile; liquidity terciles are cross-sectional terciles
of trailing dollar volume on day t. Liquidity-tercile samples do not
exhaust the events because the tercile requires a trailing dollar
volume.

| Sample                                              | Events | Gap vs market | Intraday vs market | Close-to-close vs market | Close-to-close vs controls |
|-----------------------------------------------------|--------|---------------|--------------------|--------------------------|----------------------------|
| Ceiling all                                         | 3,199  | 2.24 (9.7)    | -0.54 (-3.5)       | 1.66 (4.8)               | 2.16 (18.0)                |
| Ceiling first half (by event date)                  | 1,615  | 2.24 (5.4)    | -0.77 (-3.3)       | 1.42 (2.3)               | 2.37 (17.4)                |
| Ceiling second half (by event date)                 | 1,584  | 2.25 (13.0)   | -0.29 (-2.5)       | 1.91 (11.3)              | 1.94 (11.8)                |
| Ceiling excluding market-crash days (market \< -2%) | 3,125  | 2.24 (9.6)    | -0.53 (-3.4)       | 1.67 (4.7)               | 2.18 (18.2)                |
| Ceiling locked all day                              | 522    | 2.91 (3.0)    | -1.30 (-5.9)       | 1.54 (1.4)               | 3.52 (18.3)                |
| Ceiling not locked all day                          | 2,677  | 2.11 (14.2)   | -0.39 (-3.6)       | 1.69 (8.5)               | 1.90 (16.5)                |
| Ceiling liquidity tercile 1                         | 832    | 2.59 (6.9)    | -0.55 (-2.1)       | 1.99 (3.7)               | 2.49 (11.6)                |
| Ceiling liquidity tercile 2                         | 1,102  | 2.77 (11.1)   | -0.88 (-3.9)       | 1.83 (4.2)               | 2.28 (16.2)                |
| Ceiling liquidity tercile 3                         | 1,166  | 1.52 (7.8)    | -0.18 (-1.5)       | 1.32 (5.8)               | 1.82 (7.2)                 |
| Floor all                                           | 2,111  | -0.97 (-4.6)  | 0.30 (1.4)         | -0.69 (-4.8)             | -1.65 (-3.4)               |
| Floor first half (by event date)                    | 1,059  | -0.55 (-2.4)  | -0.09 (-0.3)       | -0.63 (-2.9)             | -2.32 (-3.0)               |
| Floor second half (by event date)                   | 1,052  | -1.40 (-6.5)  | 0.70 (4.9)         | -0.75 (-4.3)             | -0.95 (-4.5)               |
| Floor excluding market-crash days (market \< -2%)   | 740    | -1.83 (-8.7)  | 0.90 (5.3)         | -0.99 (-4.5)             | -0.98 (-4.3)               |
| Floor locked all day                                | 260    | -2.50 (-4.8)  | 1.11 (2.4)         | -1.44 (-3.4)             | -2.18 (-2.7)               |
| Floor not locked all day                            | 1,851  | -0.76 (-4.1)  | 0.19 (0.9)         | -0.59 (-3.9)             | -1.58 (-3.4)               |
| Floor liquidity tercile 1                           | 469    | -0.32 (-1.0)  | 0.42 (1.7)         | 0.06 (0.2)               | -0.56 (-1.8)               |
| Floor liquidity tercile 2                           | 685    | -1.44 (-4.4)  | 0.29 (0.9)         | -1.17 (-5.0)             | -2.24 (-4.1)               |
| Floor liquidity tercile 3                           | 893    | -0.91 (-5.2)  | 0.18 (0.9)         | -0.74 (-5.1)             | -1.77 (-3.1)               |

The pattern is not driven by one part of the sample (Table 6). It
appears in both halves of the event dates, in each liquidity tercile for
ceilings, and on days when the stock was locked at one price from open
to close, which is the case in which unfilled interest is most
plausible. The overnight gap on locked ceiling days (2.91%) is larger
than on other ceiling days (2.11%), and the intraday giveback is also
larger on locked days (-1.30% against -0.39%). Using same-date,
same-liquidity non-event stocks as the control instead of the market
raises the close-to-close ceiling effect from 1.66% to 2.16% and the
floor effect from -0.69% to -1.65%, so the benchmark matters for the
size of the floor effect in particular. The estimates are heterogeneous:
the ceiling gap is smaller in the most liquid tercile (1.52%) than in
the other two; floor events are concentrated on market-wide down days
(excluding days on which the market fell more than 2% leaves only 740 of
2,111 floor events, with a larger gap of -1.83%), and the floor gap is
not significant in the least liquid tercile (t = -1.0).

## 4.6 What can an investor do with it?

The close-to-close continuation is not available to an outside buyer. A
stock that closes at its ceiling typically cannot be bought at that
close, so the first price at which it can be bought is the next open,
which already contains the gap. Measured from that open, the abnormal
return of ceiling stocks is -0.54% within the day (two-way-clustered t =
-3.5) and -0.75% through the fifth close (t = -2.7); against same-date
liquidity-matched controls the corresponding figures are -0.50% (t =
-6.0) and -0.53% (t = -1.8). Table 6b collects these figures. A
long-only investor therefore gains nothing from chasing ceiling stocks
at the quoted open, and a holder of a ceiling stock who sells at the
next open instead of at the close avoids an average intraday giveback of
about 0.54 percentage points. These figures are measured at the quoted
open: in an opening call auction a buyer may be rationed or unable to
trade when the stock opens again at the limit (522 of the ceiling events
were locked at one price all day on day $t$, and some of these open
again at the limit), so they describe prices, not achievable fills.
Short selling the intraday reversal is not feasible in this market
without borrowing. Trading costs would further reduce any intraday
strategy; the only cost proxy we have comes from 21 large banks in the
same data (a Corwin–Schultz spread of about 59 basis points on average,
an upward-biased estimator) and is not necessarily representative of the
stocks that experience limit events.

Table 6b. Returns available from the next open (post hoc). Market:
dollar-volume weights lagged to day t; controls: same-date non-event
stocks in the same liquidity tercile. Prices are quoted opens and
closes, not achievable fills.

| Event   | Outcome                          | Mean (%) | t (two-way) | Events |
|---------|----------------------------------|----------|-------------|--------|
| Ceiling | Open to close, vs market         | -0.54    | -3.5        | 3,199  |
| Ceiling | Open to close, vs controls       | -0.50    | -6.0        | 3,100  |
| Ceiling | Open to day-5 close, vs market   | -0.75    | -2.7        | 3,193  |
| Ceiling | Open to day-5 close, vs controls | -0.53    | -1.8        | 3,099  |
| Floor   | Open to close, vs market         | 0.30     | 1.4         | 2,111  |
| Floor   | Open to close, vs controls       | 0.14     | 0.6         | 2,047  |
| Floor   | Open to day-5 close, vs market   | -0.82    | -1.7        | 2,108  |
| Floor   | Open to day-5 close, vs controls | -0.36    | -0.6        | 2,047  |

After floor closes, prices keep falling from the next open to the fifth
close against the market (Table 6b) and against 5–6.5% fallers that also
closed at their low (-1.23 percentage points, t = -2.8), a post-open
drift that a gap-only mechanism does not explain; it is concentrated in
the period before the platform change (Section 4.8).

## 4.7 Responses to design concerns (post hoc)

An independent devil’s-advocate review of the log-specified design
(`review/DA_checkpoint1_report.md`; retrospective, because it was run
after the log-specified results were known, as the reviewer noted)
raised concerns about the event definition, overlapping events, the
hold-out split, selection across projects, the benchmark and attrition.
We addressed each with additional analyses that were not log-specified
and are labelled post hoc (`process/decisions.md` A5).

Table 7. Next-day abnormal returns (%) by event definition and benchmark
(two-way-clustered t-statistics in parentheses). Controls: same-date
non-event stocks in the same liquidity tercile. Streak start: no event
of the same type on the previous day. Event counts differ across tables
by construction: 3,220 ceilings in Table 4 (all days up to the last
trading day minus one), 3,207 rule-based ceilings in Tables 5 to 7 (days
up to the last trading day minus five so that day-5 outcomes exist),
3,199 of these with a next-day price, and 3,187 in Table 3, which also
requires complete returns for days t+1 to t+5.

| Event definition                          | Events (market) | Events (controls) | Gap vs market | Gap vs controls | Intraday vs market | Intraday vs controls | Open to day-5 close vs controls |
|-------------------------------------------|-----------------|-------------------|---------------|-----------------|--------------------|----------------------|---------------------------------|
| Ceiling: rule-based                       | 3,199           | 3,100             | 2.24 (9.7)    | 2.70 (20.2)     | -0.54 (-3.5)       | -0.50 (-6.0)         | -0.53 (-1.8)                    |
| Ceiling: exact tick-rule hit              | 1,648           | 1,583             | 2.77 (13.5)   | 3.19 (21.5)     | -0.73 (-5.3)       | -0.74 (-7.5)         | -0.88 (-2.3)                    |
| Ceiling: near-hit (rule-based, not exact) | 1,557           | 1,523             | 1.67 (6.4)    | 2.17 (13.2)     | -0.32 (-1.6)       | -0.24 (-2.4)         | -0.15 (-0.5)                    |
| Ceiling: first day of streak (rule-based) | 2,480           | 2,403             | 1.83 (8.2)    | 2.37 (15.6)     | -0.38 (-1.9)       | -0.31 (-3.8)         | -0.43 (-1.6)                    |
| Ceiling: first day of streak (exact)      | 1,287           | 1,232             | 2.37 (12.2)   | 2.85 (19.3)     | -0.55 (-3.1)       | -0.53 (-4.9)         | -0.73 (-2.1)                    |
| Ceiling: locked all day                   | 522             | 505               | 2.91 (3.0)    | 4.39 (12.2)     | -1.30 (-5.9)       | -0.81 (-3.1)         | 0.57 (0.8)                      |
| Floor: rule-based                         | 2,111           | 2,047             | -0.97 (-4.6)  | -1.75 (-4.0)    | 0.30 (1.4)         | 0.14 (0.6)           | -0.36 (-0.6)                    |
| Floor: exact tick-rule hit                | 1,028           | 984               | -1.29 (-5.0)  | -1.93 (-4.8)    | 0.41 (1.7)         | 0.23 (0.9)           | -0.49 (-0.8)                    |
| Floor: near-hit (rule-based, not exact)   | 1,086           | 1,066             | -0.66 (-3.7)  | -1.58 (-3.2)    | 0.20 (0.9)         | 0.04 (0.2)           | -0.22 (-0.3)                    |
| Floor: first day of streak (exact)        | 831             | 801               | -1.04 (-4.7)  | -1.72 (-4.2)    | 0.22 (0.9)         | 0.07 (0.3)           | -0.62 (-0.9)                    |

Exact tick-rule ceiling counts differ across tables for the same reason
as the rule-based counts: 1,666 in Table 4 (days up to the last trading
day minus one), 1,654 in the event window (days up to the last trading
day minus five), 1,648 of these with a next-day price and 1,583 with a
control value (Table 7).

*Event definition.* The log-specified rule includes strong closes that
did not reach the limit price. Table 7 separates exact tick-rule hits
from near-hits: for exact ceiling hits the overnight gap is 2.77%
against the market (t = 13.5) and the intraday return -0.73%; near-hits
show a smaller gap (1.67%) and an intraday return that is not
significant. The size of the effect rises with proximity to the limit,
which supports an association with the limit itself, and the series’
adjustment status for corporate actions is not documented by the vendor.

*Overlapping events.* Restricting to the first day of a streak removes
mechanical dependence between consecutive limit days: for exact hits the
gap is 2.37% (t = 12.2) and the intraday return -0.55% (t = -3.1). The
four log-specified event tests are two effective tests (ceiling and
floor), each at two nested horizons.

*Benchmark.* Dollar-volume weights are concentrated (the ten largest
stocks carry on average 34% of the benchmark). Against same-date,
same-liquidity-tercile control stocks the overnight gap after a ceiling
is 2.70% (t = 20.2) and the intraday return -0.50% (t = -6.0); an
equal-weighted market gives a gap of 2.38%. The tradable five-day return
from the next open is -0.75% against the market (t = -2.7) but only
-0.53% against the controls (t = -1.8); we therefore describe the
intraday reversal as robust to the benchmark and the five-day tradable
shortfall as benchmark-sensitive.

*Return outliers.* There are 96 stock-days with a return beyond ±8%,
which a 7% band does not allow (first-day listing bands, resumed trading
or unadjusted corporate actions are candidates). Dropping every event
whose stock has such a return within five trading days leaves the
ceiling gap at 2.26% (t = 9.7, from 2.24%) and the floor gap at -0.98%
(from -0.97%) (repository table C25). The exclusion drops events only;
the outlier stock-days stay in the market benchmark, and it catches only
returns beyond ±8%, so it bounds but does not remove the
corporate-action concern.

*Attrition.* Of 3,207 rule-based ceiling closes and 2,115 floor closes,
8 and 4 lack a next-day price; treating a missing next day as a zero
return changes the means by less than 0.01 percentage points (repository
table C12). The universe is a snapshot of stocks listed at the time of
data collection, so stocks delisted earlier in the sample window are
absent.

Table 8. Sensitivity of the Fama–MacBeth t-statistics to the Newey–West
lag, and the minimum detectable slope at 80% power (2.8 standard
errors).

| Characteristic | t, NW lag 2 | t, NW lag 4 | t, NW lag 8 | Minimum detectable slope, 80% power (% per week per s.d.) |
|----------------|-------------|-------------|-------------|-----------------------------------------------------------|
| MOM3M          | 1.39        | 1.45        | 1.74        | 0.24                                                      |
| IMOM           | 1.39        | 1.45        | 1.72        | 0.24                                                      |
| DVOLCHG        | 1.32        | 1.42        | 1.79        | 0.14                                                      |
| TURNCHG        | 1.19        | 1.27        | 1.60        | 0.13                                                      |
| MOM6M          | 1.09        | 1.12        | 1.31        | 0.24                                                      |
| REV1M          | 0.84        | 0.92        | 1.08        | 0.23                                                      |
| MIN            | 0.75        | 0.86        | 1.04        | 0.16                                                      |
| DOWNVOL        | -0.82       | -0.84       | -0.85       | 0.21                                                      |
| CSSPREAD       | -0.80       | -0.77       | -0.73       | 0.19                                                      |
| INTRADAY       | 0.57        | 0.62        | 0.76        | 0.16                                                      |
| IVOL           | -0.52       | -0.54       | -0.62       | 0.14                                                      |
| RANGEVOL       | -0.51       | -0.51       | -0.50       | 0.20                                                      |
| REV1W          | 0.41        | 0.41        | 0.46        | 0.23                                                      |
| LIMITFREQ      | -0.26       | -0.28       | -0.30       | 0.25                                                      |
| LNDVOL         | 0.26        | 0.27        | 0.26        | 0.25                                                      |
| AMIHUD         | -0.25       | -0.26       | -0.25       | 0.24                                                      |
| KURT           | 0.20        | 0.20        | 0.21        | 0.16                                                      |
| BETA           | -0.18       | -0.18       | -0.18       | 0.31                                                      |
| VOL            | -0.09       | -0.09       | -0.09       | 0.20                                                      |
| OVERNIGHT      | 0.06        | 0.06        | 0.05        | 0.18                                                      |
| SKEW           | -0.03       | -0.03       | -0.03       | 0.12                                                      |
| MAX            | -0.02       | -0.02       | -0.02       | 0.15                                                      |

*Power and effective tests.* With 79 weekly cross-sections the minimum
detectable slope is between 0.12 and 0.31 percentage points per week per
standard deviation of the characteristic (Table 8); a null for
characteristics below that size is not informative. The 22
characteristics are correlated: the effective number of tests is about
6.8 by the participation ratio of the average correlation matrix and 14
by the Li–Ji method, so the Benjamini–Hochberg control over 22 nominal
tests is conservative. The conclusions about the characteristics do not
depend on the Newey–West lag: the largest absolute t-statistic is 1.79
at 8 lags (DVOLCHG; MOM3M 1.74; both below 1.96).

*Selection across projects.* The family-wide control addresses the 26
tests in this manuscript. Paper C is one of three manuscripts produced
from the same data and was chosen after the earlier two returned null
results, from a list of 14 candidate ideas
(`process/03_brainstorm_round2.md`); estimates of an effect chosen
because it is large are biased upward in expectation (winner’s curse).
To bound the issue we report that all four event tests would still
survive a Bonferroni correction at 5% for a project-wide family of up to
683 tests when p-values use a t reference with date clusters (the
largest event p-value is 7.3e-05; the normal reference used in the first
draft gave 816 tests), and for up to 125 tests with calendar-week
clusters (largest p-value 4.0e-04). The size of the project-wide family
is arbitrary, and the bound addresses false discoveries, not the
winner’s-curse bias in the size of the effect.

## 4.8 The May 2025 trading-platform change (post hoc)

HOSE moved to the KRX trading platform on 5 May 2025, inside the sample
(Section 2). We split events by the date of the opening that defines the
gap: 936 ceiling events open before the change and 2,263 after it.

Table 9. Next-day abnormal returns (%, market-adjusted, lagged weights)
before and after the KRX platform change of 5 May 2025,
two-way-clustered t-statistics in parentheses; the difference
t-statistic treats the two periods as independent.

| Event   | Outcome                  | Before: mean (t) | Before: n | After: mean (t) | After: n | Difference (t) |
|---------|--------------------------|------------------|-----------|-----------------|----------|----------------|
| Ceiling | Overnight gap            | 1.65 (3.2)       | 936       | 2.49 (17.9)     | 2,263    | 0.85 (1.6)     |
| Ceiling | Intraday                 | -0.77 (-2.0)     | 936       | -0.44 (-4.3)    | 2,263    | 0.34 (0.8)     |
| Ceiling | Close-to-close           | 0.83 (1.0)       | 936       | 2.01 (14.6)     | 2,263    | 1.18 (1.3)     |
| Ceiling | Next open to day-5 close | -0.71 (-1.3)     | 936       | -0.77 (-2.5)    | 2,257    | -0.06 (-0.1)   |
| Floor   | Overnight gap            | -0.42 (-1.9)     | 891       | -1.37 (-7.0)    | 1,220    | -0.95 (-3.2)   |
| Floor   | Intraday                 | -0.15 (-0.4)     | 891       | 0.64 (4.6)      | 1,220    | 0.79 (2.0)     |
| Floor   | Close-to-close           | -0.57 (-2.3)     | 891       | -0.78 (-5.0)    | 1,220    | -0.21 (-0.7)   |
| Floor   | Next open to day-5 close | -1.73 (-4.7)     | 891       | -0.15 (-0.3)    | 1,217    | 1.58 (2.5)     |

The ceiling gap is present in both periods (1.65% before, 2.49% after)
and is larger after the change, although the difference is not
significant (t = 1.6). The floor gap is larger in absolute value after
the change (-0.42% before, -1.37% after; difference t = -3.2), and the
intraday return after floor closes turns positive (0.64%, t = 4.6) while
the post-open drift to day 5 that Table 6b shows for floors is confined
to the earlier period (-1.73% before, -0.15% after). The platform change
coincides with a different market period and with a growing sample of
events (roughly 60–70% of the events are after the change), so the split
documents that the main pattern holds on both sides and that the details
differ; it does not isolate an effect of the auction rules.

# 5. Discussion

**Interpretation.** The evidence is consistent with delayed price
discovery in the sense of Kim and Rhee (1997) and with the continuation
reported by Berkman and Lee (2002), with a refinement on timing: the
continuation is concentrated in the opening, not spread over the next
days, and the intraday return that follows reverses part of it. Berkman
et al. (2012) document, for U.S. stocks and without any limit, positive
overnight returns followed by intraday reversals, concentrated among
stocks that recently attracted retail attention. The signature after
ceiling closes is the same, and Lou et al. (2019) show that overnight
and intraday returns have different persistence and that heterogeneous
traders can explain it. Our data cannot identify who trades, what news
arrived, or how the opening auction formed its price (Section 4.4 lists
the rival readings). What is specific to this setting is that the gap is
larger than for comparable moves just below the limit, including those
that also closed at their high, which is the part of the evidence that a
pure attention reading must explain. The post-open drift after floor
closes, which is confined to the period before the platform change
(Section 4.8), is not explained by a gap-only reading.

**Relation to the characteristic zoo.** The 22 characteristics serve as
a multiplicity device and a null benchmark: the same procedure that lets
the limit tests survive rejects every characteristic, which is the
contrast the family-wide frame was built to deliver. It is not a
separate finding about the cross-section, because the zoo has limited
power (minimum detectable slopes of 0.12 to 0.31 percentage points per
week). The limit hits are rare (about 2.0% of stock-days in the event
window close at the ceiling by the log-specified rule and about 1.1% by
the exact tick rule), whereas the characteristics are measured on all
stocks every week. We therefore do not claim that limit hits explain the
cross-section of returns.

**Implications, conditional on this market and window.** The
close-to-close and gap estimates describe what happens after limit
closes on HOSE in 2024–2026: the next opening carries about two
percentage points after ceiling closes and about one after floor closes.
They do not show what the limit does to price settlement, because there
is no variation in the band, no period without a limit and no measure of
the benefits a limit is meant to deliver; a regulator should read them
as a description of the post-limit opening. For investors the figures
are consistent with not chasing limit-up stocks at the quoted open and
with treating the next open as the point at which most of the day-$t$
effect is realized; the data that would test them are announcement time
stamps, order-book queue sizes at the close and a market or period
without a limit; they are not trading advice, and costs, rationing at
the open and the platform change within the sample are not modelled.

# 6. Limitations

The limitations are as follows. (i) The sample is about 25 months (519
trading days), which is short; the specified family and the confirmation
half address this only partly, but a longer sample is desirable. The
public analysis of tungtran0911 (2026) covers a longer period that
contains ours and reports a similar close-to-close effect, but it is not
independent of our sample and is not peer reviewed. (ii) There are no
order-book or investor-type data, so the unfilled-demand mechanism is
inferred. (iii) The 7% limit, the reference price and the platform
change are taken from brokerage and press descriptions (HSC, 2025; Viet
Nam News, 2025) and checked indirectly (Table 1), not against exchange
circulars; the tick-size table and the treatment of ex-rights and
ex-dividend reference prices, first-day listing bands and resumed
trading are assumptions of the exact-tick definition. (iv) Prices may be
adjusted for corporate actions in ways that affect limit-hit
classification; the log-specified rule and the exact tick rule give the
same sign and similar sizes, which limits but does not eliminate this
concern. (v) The decomposition, control group, comparison-group and
robustness analyses are post hoc, although they were motivated by the
log-specified result and are reported in full; they should be read as
explanations of a log-specified finding. (vi) The characteristic tests
use one-at-a-time Fama–MacBeth regressions; multivariate and non-linear
specifications were not part of the log-specified family. (vii)
Clustered standard errors treat dates, weeks, blocks and stocks as the
dependence dimensions (Table 3b); events in the same market episode may
be more strongly dependent than that allows, and no calendar-time
portfolio or Driscoll–Kraay estimate was computed. (viii) The
confirmation half is not a strict hold-out: lookbacks of up to 115
trading days overlap the discovery half, and a full embargo is
infeasible with 79 weekly cross-sections. (ix) The Corwin–Schultz spread
and range volatility are computed from high and low prices that price
limits censor, and some characteristics (REV1W, MAX, MIN, LIMITFREQ,
OVERNIGHT) are mechanically related to the event definition. (x) The
sample is one exchange over about 25 months that includes a change of
trading platform (5 May 2025; Section 4.8) and a period of market-wide
stress, so it is not a single stable regime and the pre-change sample is
small. (xi) The project selected this manuscript among several (Section
4.7), so its estimates are subject to a winner’s-curse bias. (xii) The
sample contains no announcement, news or order-book data, so selection
on news and the unfilled-demand mechanism are not separated (Section
4.4); the quoted next open is not an achievable fill (Section 4.6).
(xiii) The floor effect depends on the benchmark (Table 6) and no beta-
and size-matched control was used for the five-day outcome.

# 7. Conclusion

In a family of 26 tests specified in a project log before computation,
none of 22 familiar price- and volume-based characteristics survives
false-discovery-rate control and a confirmation half (with limited
power), whereas all four price-limit tests do, also with week- and
block-clustered inference; for ceilings the five-day test is carried by
the first day, and for floors the days after the first add a further
drift that does not pass the confirmation half. A ceiling close is
followed by a next-day abnormal return of about +1.7%, which is an
overnight gap of 2.2% followed by a partial intraday reversal. The gap
is 2.7 percentage points larger than for stocks that rose 5–6.5% without
hitting the limit, and 3.1 points larger than for those that also closed
at their high. The close-to-close effect is already reported publicly
for a longer sample; the decomposition and the comparison with sub-limit
moves are exploratory. The pattern is consistent with delayed price
discovery at the limit, but news and attention are not excluded, and the
effect is a feature of the opening after a limit close, not a profit
opportunity for investors who buy after the close.

# Declarations

**Use of artificial intelligence.** The analysis code, tables,
manuscript draft and revisions were produced by Claude (Anthropic, model
family Claude Sonnet 5.x, Claude Code agent, 4 October 2026) under the
Academic Research Skills workflow, without line-by-line human editing.
Within that workflow, separate Claude agent instances in fresh contexts
acted as the devil’s advocate, as the five reviewers of the review panel
and the editorial synthesizer, and as integrity auditors; they share the
model family with the author-agent, so their agreement is not
independent verification, and no cross-model verifier was used. The
agents searched the web to check references; the checks are logged in
`process/04_literature_search_log.md`. The human authors are responsible
for verifying every choice, result and reference before submission; the
references and the institutional facts taken from press and brokerage
pages (Section 2) have not been checked by a human.

**Data and code availability.** The raw daily files are in `data/raw/`
and the 25-bank files in `Data_fetch/` of the project repository
(`trungcandygit/black_litterman_2`); code is in `paper2/R/` (scripts
40–48), derived tables are in `paper2/output/tables/` (C1–C25, T10), and
this manuscript’s source regenerates the numbers in the text and tables
from the saved tables (the saved tables in turn come from the scripts
listed in Appendix B). The data come from the vnstock library with a
listing file dated 24 September 2026; the library version and the
retrieval dates were not recorded, so a third party can reuse the files
but cannot rebuild them from the vendor with certainty. The process logs
cited in the text (`process/`, `review/`) are in the same repository.

**Ethics, funding, competing interests, author contributions.** \[To be
completed by the authors; not completed by the drafting agents.\]

# References

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and
time-series effects. *Journal of Financial Markets, 5*(1), 31–56.

Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). Maxing out: Stocks as
lotteries and the cross-section of expected returns. *Journal of
Financial Economics, 99*(2), 427–446.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery
rate: A practical and powerful approach to multiple testing. *Journal of
the Royal Statistical Society: Series B (Methodological), 57*(1),
289–300. <https://doi.org/10.1111/j.2517-6161.1995.tb02031.x>

Berkman, H., & Lee, J. B. T. (2002). The effectiveness of price limits
in an emerging market: Evidence from the Korean Stock Exchange.
*Pacific-Basin Finance Journal, 10*(5), 517–530.

Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). Paying
attention: Overnight returns and the hidden cost of buying at the open.
*Journal of Financial and Quantitative Analysis, 47*(4), 715–741.

Bildik, R., & Gülay, G. (2006). Are price limits effective? Evidence
from the Istanbul Stock Exchange. *Journal of Financial Research,
29*(3), 383–403. <https://doi.org/10.1111/j.1475-6803.2006.00185.x>

Brennan, M. J. (1986). A theory of price limits in futures markets.
*Journal of Financial Economics, 16*(2), 213–233.
<https://doi.org/10.1016/0304-405X(86)90061-9>

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2011). Robust inference
with multiway clustering. *Journal of Business & Economic Statistics,
29*(2), 238–249. <https://doi.org/10.1198/jbes.2010.07136>

Chen, Y.-M. (1993). Price limits and stock market volatility in Taiwan.
*Pacific-Basin Finance Journal, 1*(2), 139–153.

Cho, D. D., Russell, J., Tiao, G. C., & Tsay, R. S. (2003). The magnet
effect of price limits: Evidence from high-frequency data on Taiwan
Stock Exchange. *Journal of Empirical Finance, 10*(1–2), 133–168.

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask
spreads from daily high and low prices. *The Journal of Finance, 67*(2),
719–760. <https://doi.org/10.1111/j.1540-6261.2012.01729.x>

Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium:
Empirical tests. *Journal of Political Economy, 81*(3), 607–636.
<https://doi.org/10.1086/260061>

Harvey, C. R., Liu, Y., & Zhu, H. (2016). …and the cross-section of
expected returns. *The Review of Financial Studies, 29*(1), 5–68.
<https://doi.org/10.1093/rfs/hhv059>

HSC. (2025). *Important changes of new trading system* \[Web page\]. Ho
Chi Minh City Securities Corporation. Retrieved October 4, 2026, from
<https://www.hsc.com.vn/en/important-changes-of-new-trading-system>

Holm, S. (1979). A simple sequentially rejective multiple test
procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.

Imbens, G. W., & Lemieux, T. (2008). Regression discontinuity designs: A
guide to practice. *Journal of Econometrics, 142*(2), 615–635.

Kim, K. A., & Rhee, S. G. (1997). Price limit performance: Evidence from
the Tokyo Stock Exchange. *The Journal of Finance, 52*(2), 885–901.
<https://doi.org/10.1111/j.1540-6261.1997.tb04827.x>

Le, D. N. (2012). Evaluating impacts of reduction in fluctuation limit
on stock price risks in Vietnam. *Journal of Economic Development, 214*,
116–128.

Lou, D., Polk, C., & Skouras, S. (2019). A tug of war: Overnight versus
intraday expected returns. *Journal of Financial Economics, 134*(1),
192–213. <https://doi.org/10.1016/j.jfineco.2019.03.011>

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite,
heteroskedasticity and autocorrelation consistent covariance matrix.
*Econometrica, 55*(3), 703–708. <https://doi.org/10.2307/1913610>

Parkinson, M. (1980). The extreme value method for estimating the
variance of the rate of return. *The Journal of Business, 53*(1), 61–65.

Qi, B. (2023). Effectiveness of price limits: Evidence from China’s
ChiNext market. *PLOS ONE, 18*(6), e0287548.
<https://doi.org/10.1371/journal.pone.0287548>

Subrahmanyam, A. (1994). Circuit breakers and market volatility: A
theoretical perspective. *The Journal of Finance, 49*(1), 237–254.
<https://doi.org/10.1111/j.1540-6261.1994.tb04427.x>

tungtran0911. (2026). *vn-equity-factors* \[Source code\]. GitHub.
Retrieved October 4, 2026, from
<https://github.com/tungtran0911/vn-equity-factors>

Viet Nam News. (2025). *KRX system officially goes live* \[News
article\]. Retrieved October 4, 2026, from
<https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html>

Veeraraghavan, M., Nguyen, M. T. T., & Truong, C. (2007). *Delayed price
discovery and momentum strategies: Evidence from Vietnam* (SSRN
Scholarly Paper No. 1009042). Social Science Research Network.
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1009042>

# Appendix A. Log-specified versus post hoc analyses

| Analysis                                                                                                                                                                                                                                  | Status                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| 22 characteristics, Fama–MacBeth, quintile spreads, discovery/confirmation split, illiquidity exclusion                                                                                                                                   | Specified in the log before computation     |
| Ceiling and floor event tests at t+1 and t+1..t+5; BH/Holm/HLZ control over 26 tests; survival rule                                                                                                                                       | Specified in the log before computation     |
| Overnight–intraday decomposition; next-open returns; same-date liquidity-matched control                                                                                                                                                  | Post hoc (A4)                               |
| Comparison with 3–5% and 5–6.5% moves; discontinuity plot and table                                                                                                                                                                       | Post hoc (A4)                               |
| Exact tick-rule definition; two-way clustering; sub-sample robustness                                                                                                                                                                     | Post hoc (A4)                               |
| Week- and block-clustered inference, t reference, days t+2 to t+5, split at weeks 39/40, platform-change split, comparison groups closing at the extreme, volume and prior-return terciles, outlier exclusion (Tables 3b, 5b, 9; C18–C25) | Post hoc (A9, after the first review round) |

Time-stamp anchor of the specification:
`process/03_brainstorm_round2.md`, commit 63bdc6d (4 October 2026,
07:23:38 UTC), SHA-256
3d6dc7e1ff57f43092ff47da1b3cf49a848521568ea55dbaa09f61ff026effaf; first
commit with analysis code and results: 9b8644b (07:36:19 UTC). Commit
dates are set by the committer; the repository host’s push records are
the only external anchor.

# Appendix B. Code and reproducibility

`R/40_zoo.R` (family of 26 tests), `R/42_rd.R` (bins, tick rule, two-way
clustering), `R/45_figuresC.R` (figures), `R/46_verify_C.R`
(verification tests), `R/47_da_response.R` (responses to the independent
reviews and the NA-safe Tables 1, 5, 6 and 7), `R/48_revision.R`
(responses to the first review round: Tables 3b, 5b, 6b, 9; tables
C18–C25). Scripts `R/41_limits_robust.R`, `R/43_disc.R` and
`R/44_desc.R` and the tables they wrote (C4, C8, C9, C10, renamed with
the prefix SUPERSEDED\_) are superseded by `R/47_da_response.R` for
every number in this manuscript and are kept for audit only. Seeds are
fixed. The decisions log records the specification fixed before
computation (A3, an internal time-stamped log, not an external registry)
and the post hoc amendments (A4, A5).

# Appendix C. Literature search and verification

The search strategy, the prior-art finding that bounds the novelty
claim, and the verification status of every reference are in
`process/04_literature_search_log.md`. References were checked against
records returned by web search (publisher, IDEAS/RePEc, SSRN, PMC or
abstract pages); for Le (2012), Chen (1993) and Berkman and Lee (2002)
only abstract-level or bibliographic records were seen, and no DOI was
resolved because the DOI resolver and Crossref were not reachable from
the analysis environment; DOIs in the list come from the search records
and need a final check by the authors. After the first review round the
search was extended to price-limit theory (Subrahmanyam, 1994), Turkish
and Chinese evidence (Bildik & Gülay, 2006; Qi, 2023) and the HOSE rules
and platform change (HSC, 2025; Viet Nam News, 2025);
Vietnamese-language journals, further Chinese A-share studies and Le
(2012) were not retrieved or checked in full text, and the novelty
statement remains bounded by this search.
