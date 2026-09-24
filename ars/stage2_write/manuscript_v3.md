# Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification

## Abstract

FTSE Russell reclassified Vietnam from frontier to secondary emerging status in four public steps between October 2025 and September 2026. Using daily data on 366 stocks listed on the Ho Chi Minh City Stock Exchange, we trace liquidity and prices at each step. The 24 eventual index constituents became more liquid than never-named stocks at every disclosure: their Amihud illiquidity fell by 59% after FTSE confirmed the upgrade and by 68% once it published the constituent list. Because FTSE chose the constituents on mid-2026 data, we also estimate intention-to-treat effects for the 27 stocks FTSE had screened as eligible on data from before the announcement. Their illiquidity fell by 43% and 56% over the same stages, so the gains do not merely reflect FTSE picking stocks that were already improving. Constituents earned abnormal returns of 7.8% in the week around the announcement and 4.5% around the confirmation; both gains hold under four benchmarks and a test that allows for event-date clustering; the constituent list and the first 10% index tranche added no reliable price effect. Index funds traded the constituents heavily at the rebalancing close, but not the stocks FTSE named and then excluded. The upgrade's liquidity and price gains arrived with FTSE's disclosures, months before index funds traded.

**Keywords**: market reclassification; index effect; stock liquidity; frontier markets; intention to treat; Vietnam

**JEL classification**: G12; G14; G15

## 1. Introduction

Vietnam's market upgrade delivered its liquidity gains months before any index fund traded. When FTSE Russell reclassified Vietnam from frontier to secondary emerging status, the Amihud (2002) illiquidity of the stocks it would include fell relative to never-named stocks on the Ho Chi Minh City Stock Exchange (HOSE) at each public step: by 59% after FTSE confirmed the upgrade in April 2026 and by 68% after it named the constituents in August 2026. Stocks that FTSE had screened as eligible on data from before the announcement gained too, by 43% and 56%. On the effective date, prices did not move; the trace of index membership was a one-session trading surge at the rebalancing close.

Market classification decides which benchmarks a country's stocks can enter, and benchmark weights steer international portfolio allocations (Raddatz et al., 2017). An upgrade from frontier to emerging status therefore promises new foreign demand, and Vietnamese policymakers pursued it through seven years of watch-list reviews. Whether the promised liquidity reaches individual stocks, which stocks it reaches, and when, bears on issuers' cost of capital, because liquidity is priced in emerging markets (Bekaert et al., 2007).

Existing evidence answers these questions poorly for frontier markets. In developed markets, additions to the S&P 500 raise trading activity and narrow spreads for years (Hegde & McDermott, 2003), and added firms with larger liquidity gains invest more (Becker-Blease & Paul, 2006). In frontier markets, index additions raise prices persistently, and the evidence points to institutional demand rather than trading pressure or liquidity changes as the cause (Biktimirov & Afego, 2026). Most studies of market reclassification also work with aggregate indices or country-level flows, which cannot separate the stocks an upgrade targets from market-wide trends. An earlier study of the same market by the present authors (anonymized for review) found that FTSE watch-list reviews did not coincide with structural breaks in index-level liquidity; that design could not ask which stocks gained.

Vietnam's reclassification offers a cleaner test for three reasons. FTSE Russell disclosed the decision in four dated steps: the announcement on 7 October 2025, the confirmation on 7 April 2026, the constituent list on 21 August 2026, and the effective date of 21 September 2026. Each step resolved a different piece of uncertainty, so their separate effects reveal when investors acted. Hundreds of HOSE stocks outside the index trade under the same rules, hours and price limits and provide a comparison group. And FTSE published lists of eligible stocks before it chose the constituents, including a preliminary list screened on data as of 31 December 2024, before the upgrade was announced. That list lets us estimate intention-to-treat effects that do not depend on FTSE's later choice.

The last point matters because FTSE selected the final constituents on data as of 30 June 2026 (FTSE Russell, 2026), in the middle of the period we study. A stock whose trading grew after October 2025 for any reason was more likely to be selected, so a comparison of final constituents with other stocks could mistake selection for an upgrade effect. We address this in two ways. We remove from the comparison group every stock FTSE named as eligible but did not include, and we estimate intention-to-treat effects for the preliminary list.

We estimate difference-in-differences and event-study regressions on 35,752 stock-weeks and on daily returns from October 2024 to September 2026. The main liquidity measure is the Amihud ratio computed on traded value in Vietnamese dong; we also report trading value, the Corwin and Schultz (2012) high-low spread, volatility and abnormal returns. For prices, we test cumulative abnormal returns at the portfolio level, which accounts for the common event dates (Brown & Warner, 1985), under four benchmarks.

The paper makes one contribution: it decomposes the stock-level liquidity and price effects of a frontier-to-emerging reclassification by disclosure stage, with treatment defined on information available before the upgrade. Four findings support the decomposition. First, constituents' illiquidity fell by 0.39, 0.89 and 1.13 log points across the announcement, confirmation and constituent-list windows (Table 2), with significant steps at the confirmation and the list, and the intention-to-treat estimates are about two thirds as large (Table 3). Second, prices rose in the week around the announcement and at the confirmation, and the confirmation gain persisted; the constituent list and the effective date produced no reliable price effect (Table 4). Third, the rebalancing session raised constituents' trading value by 0.79 log points relative to never-named stocks, rising with FTSE size segment, while named-but-excluded stocks showed no surge (Table 5). Fourth, FTSE's selection partly followed rising liquidity: two stocks added to the eligible list in April 2026 had become more liquid during the data window FTSE screened (Table 9). This last result limits causal readings of the constituent estimates and is the reason we report intention-to-treat effects beside them.

Section 2 describes the setting, reviews the literature and states the hypotheses. Section 3 presents the data and design. Section 4 reports the results, Section 5 the robustness checks and the selection evidence, and Section 6 concludes.

## 2. Setting, literature and hypotheses

### 2.1 FTSE Russell's four-step reclassification of Vietnam

FTSE Russell added Vietnam to its watch list for possible reclassification in September 2018 (FTSE Russell, 2018). On 7 October 2025 it announced that Vietnam would move from frontier to secondary emerging status with effect from 21 September 2026, subject to an interim review in March 2026 (LSEG, 2025). On 7 April 2026 it confirmed that Vietnam met all criteria for secondary emerging status and kept the effective date (LSEG, 2026). Inclusion is phased in four tranches that add 10%, 20%, 35% and 35% of the applicable index weight on 21 September 2026, 22 March 2027, 21 June 2027 and 20 September 2027 (FTSE Russell, 2026). The effective date we study therefore carried only the first tenth of the eventual index weight.

Between these dates the financial press reported FTSE's lists of eligible stocks. A preliminary list of 28 names, screened on data as of 31 December 2024, appeared in November 2025 (Viet Nam News, 2025; The Investor, 2026a). A list of 32 names, screened on data as of 31 December 2025, followed in April 2026; it dropped Petrolimex (PLX) and added BID, FPT, NVL, GEE and BSR (The Investor, 2026b). On Friday 21 August 2026 FTSE published the September semi-annual review with 27 constituents, selected on data as of 30 June 2026 and effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026). FTSE screened Vietnamese securities as non-constituents on its liquidity, minimum-size and foreign-headroom screens, using each security's investability weight (free float) in the liquidity test (FTSE Russell, 2026). Appendix Table A2 lists every stock by list.

The four steps carried different information. The announcement told investors that Vietnamese stocks would become eligible for emerging-market benchmarks but made the upgrade conditional on an interim review. The confirmation removed that condition. The constituent list named the stocks index-tracking funds would buy, and the rebalancing session was the day they bought the first tranche. Effects that appear at the early disclosures indicate that investors traded on information; effects concentrated at the rebalancing session indicate mechanical index demand.

### 2.2 Index inclusion and liquidity

Two channels link index membership to liquidity and prices. The price-pressure channel works through the trades of index funds: additions force passive funds to buy on the effective date, which produces temporary volume and price effects that reverse afterwards (Harris & Gurel, 1986). The demand and recognition channel works through a lasting change in the investor base. Shleifer (1986) interprets permanent price effects as evidence that demand curves for stocks slope down, and Chen et al. (2004) find asymmetric effects of additions and deletions that fit a gain in investor awareness. Hegde and McDermott (2003) show that S&P 500 additions narrow spreads and raise trading activity persistently, which they attribute to more information and more trading interest.

Liquidity gains from inclusion also have real consequences. Becker-Blease and Paul (2006) find that firms added to the S&P 500 with larger liquidity improvements increase capital investment, and Gregoriou and Nguyen (2010) find the mirror pattern for FTSE 100 deletions. Liquidity co-moves across stocks (Chordia et al., 2000), so any study of these effects must separate stock-specific changes from market-wide liquidity shocks.

### 2.3 Market reclassification and frontier markets

Reclassification moves a whole market between benchmark families. Mutual funds allocate across countries with reference to benchmark weights, so a change in classification changes capital flows (Raddatz et al., 2017), and an MSCI index change even moved currency values through this channel (Hau et al., 2010). When MSCI included China A-shares in its Emerging Markets Index, the included stocks earned abnormal returns around the announcement, and market quality changed over the longer run through liquidity, turnover and price synchronization (Dong et al., 2023). The frontier-market evidence is thinner. Biktimirov and Afego (2026) study changes to the FTSE Frontier 50 Index from 2008 to 2025. Additions earn persistent price gains, country reclassification events show distinct return and volume effects, and the authors attribute the gains to institutional demand rather than to trading pressure or liquidity. Our design complements theirs: it follows liquidity stage by stage and compares index stocks with non-index stocks of the same market. No study we know of, in a search bounded to Crossref records and the literature cited here, estimates the stock-level liquidity effect of a frontier-to-emerging reclassification with a comparison group and a pre-determined treatment list.

Liquidity carries particular weight in these markets. Bekaert et al. (2007) show that local market liquidity predicts returns in emerging markets, where segmentation from global capital is only partial, and Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity. A reclassification that improves liquidity for a subset of stocks could therefore shift their cost of capital relative to the rest of the market; we do not measure that shift here. Frontier markets also differ from developed ones in who trades: when domestic retail investors dominate turnover, the arrival of benchmark-tracking foreign money is a larger change in the investor base than an S&P 500 addition. The Vietnamese evidence available before the upgrade concerns market-wide liquidity shocks rather than classification events; for example, Nguyen et al. (2021) study the returns and liquidity of financial-services stocks during the COVID-19 outbreak.

### 2.4 Hypotheses

The recognition channel predicts that liquidity and prices respond when information reaches investors; the price-pressure channel predicts a trading and price spike when index funds rebalance, followed by reversal.

H1. After the reclassification announcement, stocks likely to enter the index became less illiquid than other HOSE stocks.

H2. The liquidity gap widened at each later disclosure that resolved uncertainty about the upgrade and its constituents.

H3. Likely constituents earned abnormal returns at the disclosures, and the first index tranche added no further price effect.

H4. The rebalancing session produced a trading-value surge for constituents, and not for excluded stocks, that scaled with index weight.

## 3. Data and empirical design

### 3.1 Sample and groups

We collect daily open, high, low and close prices and share volume for all 405 common stocks listed on HOSE as of 24 September 2026, from 1 October 2024 to 23 September 2026. The data come from the VCI feed through the open-source vnstock library. We keep stocks with at least 200 trading days before 7 October 2025, zero volume on fewer than 20% of those days, and a median price of at least VND 1,000, which leaves 366 stocks.

We sort them into three groups using FTSE's public lists (Appendix Table A2). Constituents are the 24 stocks of the final 27 with a full pre-period; TCX, VPL and VCK listed after October 2025. Named-but-excluded stocks are the 14 HOSE stocks that appeared on the November 2025 or April 2026 eligible list but not among the constituents (BSR, DGC, DIG, DPM, DXG, EIB, FRT, GEE, KBC, KDC, KDH, PDR, PLX and SAB); the fifteenth such name, Tasco (HUT), trades on the Hanoi exchange. The comparison group consists of the remaining 328 never-named stocks. The intention-to-treat (ITT) group consists of the 27 HOSE stocks on the preliminary list screened on 2024 data, of which 15 later became constituents and 12 did not.

Table 1 shows that constituents are much larger and more liquid than the average HOSE stock. Before the announcement, constituents traded a mean of 6.82 log VND billion per week against 2.19 for never-named stocks, and their mean weekly Amihud ratio was about three orders of magnitude lower. Named-but-excluded stocks sit between the two. Spreads and absolute returns are similar across groups. The size gap motivates the matched sample and the size-specific checks below.

**Table 1. Sample composition and pre-announcement characteristics (October 2024 to 6 October 2025)**

| Group | Stocks | Stock-weeks | Mean weekly Amihud | Mean log trading value (VND bn) | Mean CS spread (%) | Mean absolute return (%) |
|---|---|---|---|---|---|---|
| FTSE constituents | 24 | 1,248 | 0.00017 | 6.82 | 0.57 | 1.40 |
| Named on eligible lists, not included | 14 | 726 | 0.0033 | 5.96 | 0.61 | 1.49 |
| Never-named HOSE stocks | 328 | 16,915 | 0.195 | 2.19 | 0.61 | 1.37 |

*Notes*: Amihud is the mean daily ratio of absolute log return to traded value (VND billion) within a week. CS is the Corwin and Schultz (2012) spread. Source: output/revision/t1_descriptives.csv.

### 3.2 Liquidity and return measures

Daily traded value equals the closing price times share volume, in VND billion. The Amihud (2002) ratio for stock i on day t is

ILLIQ_it = |R_it| / VAL_it,

where R_it is the log return and VAL_it the traded value. Traded value, rather than share volume, makes the ratio comparable across stocks with different price levels. We compute the Corwin and Schultz (2012) spread from two-day high and low prices and set negative estimates to zero. We winsorize the daily Amihud ratio and spread cross-sectionally at the 1st and 99th percentiles of each day and aggregate to a stock-week panel, keeping weeks with at least three trading days and a positive Amihud ratio. Weekly Amihud is the mean of daily ratios, used in logs; weekly trading value is the log of total traded value; the weekly spread is the mean daily spread; weekly volatility is the log of the mean absolute daily return. Kang and Zhang (2014) show that the Amihud ratio loses accuracy in emerging markets where many days have zero volume, and propose an adjustment; our filter removes stocks with zero volume on 20% or more of pre-period days, which limits this problem.

For prices, the daily abnormal return of stock i is its log return minus a benchmark return. We use four benchmarks: the equal-weighted mean of the 328 never-named stocks; the mean of the matched control stocks described below; the equal-weighted mean of never-named stocks in the top tercile of pre-period trading value; and a market model with intercept and slope estimated for each stock over trading days -130 to -11 before each event against the first benchmark. Because every constituent shares the same event dates, abnormal returns are correlated across stocks, and cross-sectional t-statistics overstate precision. We therefore test cumulative abnormal returns (CARs) on the equal-weighted portfolio of the group, dividing the portfolio CAR by the standard deviation of daily portfolio abnormal returns over days -130 to -11, scaled by the square root of the window length (Brown & Warner, 1985).

### 3.3 Estimation

The baseline liquidity specification is

y_iw = α_i + λ_w + Σ_k β_k (Constituent_i × P_kw) + ε_iw,

where y_iw is a liquidity measure for stock i in week w, α_i and λ_w are stock and week fixed effects, and P_1, P_2 and P_3 indicate the announcement window (7 October 2025 to 6 April 2026), the confirmation window (7 April to 20 August 2026) and the list-and-rebalancing window (21 August to 23 September 2026). Weeks start on Monday, and a week enters a window only if it starts on or after the disclosure date, so each window begins with the first full week after the disclosure. FTSE does not state the hour at which it released the constituent list; the weekly assignment and the [-1,+1] event window, which spans 20, 21 and 24 August, both contain the first Vietnamese session after the release. The baseline sample excludes named-but-excluded stocks, so the comparison group contains only never-named stocks. Week fixed effects absorb market-wide shocks. We cluster standard errors by stock.

The ITT specification replaces Constituent_i with an indicator for the 27 stocks on the preliminary list, keeps every other stock in the sample, and in a variant restricts the comparison group to never-named, never-included stocks. A third treatment, "predicted constituents", takes the 27 stocks with the highest pre-announcement trading value; 16 of them became constituents.

Constituents are the largest HOSE stocks, so shocks that affect large stocks differently could bias the comparison. We re-estimate on a matched sample that pairs each constituent with three never-named stocks by nearest-neighbour propensity score, with replacement, on pre-period traded value, price and return volatility (Ho et al., 2007); matching reduces the standardized mean difference in pre-period traded value from 4.06 to 0.04 (Appendix Table A1). We also replace week fixed effects with size-tercile-by-week fixed effects, add a constituent-specific linear trend, and estimate a monthly event study relative to September 2025 (Roth et al., 2023). For inference with 24 treated stocks, we report a wild cluster bootstrap (Cameron et al., 2008) and randomization inference that draws 500 pseudo-treated groups of 24 stocks from the 85 never-named stocks in the top tercile of pre-period trading value. Because FTSE treated all constituents at the same dates, the specification has no staggered adoption, and the two-way fixed effects estimator does not suffer the negative-weighting problem that motivates Callaway and Sant'Anna (2021).

For the rebalancing session we estimate a daily regression of log traded value on stock and date fixed effects and constituent indicators for 18 September (the rebalancing session) and 21 September (the effective date), over the 32 sessions from 6 August to 23 September 2026. The coefficients measure the surge on those sessions relative to the other sessions in the window.

### 3.4 Identification assumptions

The coefficients β_k identify the effect of the upgrade on constituents under four assumptions.

First, parallel trends: without the upgrade, constituents and never-named stocks would have followed the same liquidity path. The event study tests its observable implication for the pre-announcement months, and the matched, size-by-week and trend specifications relax it in different directions.

Second, no anticipation before 7 October 2025. Vietnam sat on the FTSE watch list for seven years (FTSE Russell, 2018), so investors could have bought likely constituents in advance of the decision. Anticipation of this kind would raise liquidity before the announcement and bias the estimates toward zero.

Third, no spillovers onto comparison stocks. If investors sold never-named stocks to buy constituents, the comparison group's liquidity would fall because of the treatment. Removing named-but-excluded stocks from the comparison group, as we do, prevents the most likely spillover channel, trading in near-substitutes, from contaminating it.

Fourth, the treatment group must not be selected on post-treatment outcomes. This assumption fails for the final constituents by construction, because FTSE selected them on data as of 30 June 2026. The ITT group avoids the problem: FTSE screened it on data from 2024. ITT estimates measure the effect on stocks that were likely constituents before the announcement, and they understate the effect of inclusion to the extent that 12 of the 27 listed stocks were not included.

## 4. Results

### 4.1 Likely constituents became less illiquid from the announcement onward

Constituents' Amihud illiquidity fell relative to never-named stocks in each disclosure window, and the fall deepened at each stage. Table 2, column 1, reports coefficients of -0.39, -0.89 and -1.13 log points, declines of 32%, 59% and 68%. All three are significant at the 0.1% level, and the wild cluster bootstrap p-values are below 0.001. The matched sample in column 4 gives -0.39, -0.75 and -0.94 (declines of 32%, 53% and 61%). The steps are significant: the confirmation-window coefficient exceeds the announcement-window coefficient by 0.50 log points (standard error 0.08, p < 0.001), and the list-window coefficient exceeds the confirmation-window coefficient by 0.24 (standard error 0.11, p = 0.025). Both steps survive a constituent-specific linear trend (0.49, p < 0.001; 0.24, p = 0.036), which supports H2.

**Table 2. Liquidity of FTSE constituents relative to never-named HOSE stocks, by disclosure stage**

| | (1) log Amihud | (2) log trading value | (3) CS spread | (4) log Amihud | (5) log trading value | (6) CS spread |
|---|---|---|---|---|---|---|
| Sample | All never-named controls | All never-named controls | All never-named controls | Matched 3:1 | Matched 3:1 | Matched 3:1 |
| Constituent × Announcement | -0.392*** (0.098) | 0.678*** (0.108) | 0.0009** (0.0003) | -0.386** (0.117) | 0.638*** (0.136) | 0.0014** (0.0004) |
| Constituent × Confirmation | -0.888*** (0.124) | 1.030*** (0.125) | 0.0010** (0.0003) | -0.751*** (0.152) | 1.036*** (0.182) | 0.0014** (0.0004) |
| Constituent × List and rebalancing | -1.129*** (0.178) | 1.189*** (0.168) | 0.0013** (0.0005) | -0.938*** (0.204) | 1.308*** (0.221) | 0.0020** (0.0006) |
| Stock and week FE | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 34,369 | 34,369 | 34,369 | 4,751 | 4,751 | 4,751 |

*Notes*: Stock-week panel, October 2024 to September 2026; named-but-excluded stocks removed. Standard errors clustered by stock in parentheses. *, **, *** denote significance at 5%, 1% and 0.1%. Source: output/revision/t2_baseline_clean.csv.

The ITT estimates in Table 3 confirm that the decline is not an artefact of FTSE's later choice. The 27 stocks screened on 2024 data became less illiquid by 0.27, 0.55 and 0.81 log points (declines of 24%, 43% and 56%), all significant at the 1% level or better, and slightly more when the comparison group excludes every named or included stock. The ITT effects are 62% to 72% of the constituent effects, as expected when 12 of the 27 listed stocks were never included. Splitting the ITT group shows where the gains concentrated: listed stocks that later entered the index gained 0.43, 0.87 and 1.12 log points, while listed stocks that did not enter gained 0.11, 0.25 and 0.53, the last significant at 5%. The 27 predicted constituents, chosen by pre-period trading value alone, gained 0.25, 0.59 and 0.74 log points.

**Table 3. Intention-to-treat and predicted-constituent estimates (log Amihud unless stated)**

| Treatment group | Announcement | Confirmation | List and rebalancing | log trading value, list window | Observations |
|---|---|---|---|---|---|
| ITT: preliminary list (27), all other stocks as controls | -0.268** (0.083) | -0.554*** (0.129) | -0.811*** (0.167) | 0.724*** (0.194) | 35,752 |
| ITT: preliminary list (27), never-named, never-included controls | -0.286*** (0.083) | -0.593*** (0.129) | -0.860*** (0.167) | 0.776*** (0.194) | 34,666 |
|   of which later included (15) | -0.428*** (0.101) | -0.872*** (0.146) | -1.123*** (0.192) | | 34,666 |
|   of which not included (12) | -0.108 (0.102) | -0.245 (0.159) | -0.527* (0.236) | | 34,666 |
| Predicted constituents: top 27 by pre-period trading value | -0.250*** (0.073) | -0.595*** (0.089) | -0.741*** (0.120) | 0.607*** (0.144) | 35,752 |

*Notes*: The preliminary list is FTSE's November 2025 eligible list screened on data as of 31 December 2024 (27 HOSE stocks). Stock and week fixed effects; standard errors clustered by stock. The split rows come from one regression with separate interactions. Source: output/revision/t_itt.csv.

Figure 1 shows the timing. The constituents' monthly Amihud coefficients move around zero in the pre-announcement year without a downward drift. They are positive in several months, most clearly three and two months before the announcement (0.33 and 0.23), so constituents were, if anything, becoming less liquid just before October 2025. Because these deviations are precisely estimated, the joint test that all pre-period coefficients are zero rejects in the full sample (F = 6.66, p < 0.001); in the matched sample it does not reject at 5% (F = 1.72, p = 0.056). The coefficient turns negative in October 2025 (-0.23), steps down after the confirmation (-0.62 in April 2026) and reaches -1.12 in August 2026. Section 5 shows that the estimates do not depend on the months before the announcement.

**Figure 1. Monthly event-study coefficients for FTSE constituents and named-but-excluded stocks**

![](figures/figure1_event_study.png)

*Note*: Coefficients relative to September 2025 from one regression per outcome with stock and week fixed effects; the comparison group is never-named HOSE stocks. 95% confidence intervals from stock-clustered standard errors. Dashed lines mark the announcement, confirmation and constituent-list months. Source: output/revision/t_event_study.csv.

Trading value tells a similar story with one caveat. Constituents' trading value rose by 0.68, 1.03 and 1.19 log points relative to never-named stocks (Table 2, column 2), but it was already rising before October 2025 (Figure 1, panel B). Trend-adjusted effects fall to 0.28, 0.39 and 0.43 log points (Section 5), and we describe the trading-value result as an association.

Randomization inference confirms that the declines are not what large HOSE stocks experienced in general. None of 500 pseudo-groups of 24 stocks drawn from the 85 largest never-named stocks produced a coefficient as negative as the observed one in any window (one-sided p < 0.002). The placebo distribution centres at -0.21 in the list window: large stocks became somewhat more liquid, by less than one fifth of the constituent effect.

**Takeaway.** Stocks that were likely constituents before the announcement became about one quarter less illiquid within months of it and more than half less illiquid by the constituent list; the stocks FTSE finally included gained most.

### 4.2 Prices moved at the announcement and the confirmation

Constituents earned abnormal returns in the week around the announcement and around the confirmation, and these survive every benchmark and the portfolio test. Table 4, panel A, reports CARs with portfolio t-statistics. Over days -1 to +5 around the announcement, constituents earned 7.8% against never-named stocks (t = 3.46) and between 4.4% and 6.6% against the matched, large-stock and market-model benchmarks (t between 2.16 and 3.04). Over days -1 to +1 around the confirmation, they earned 4.5% (t = 2.54), and 2.9% to 3.6% under the other benchmarks (t between 2.30 and 2.51). The constituent list and the effective date produced no reliable price effect: around the list the three-day CAR ranges from 1.1% to 2.7% with portfolio t-statistics between 0.97 and 1.82, and around the effective date it is between -0.9% and 0.6%. The last column shows why the portfolio test matters: cross-sectional t-statistics, which ignore the common event date, are up to three times larger.

**Table 4. Cumulative abnormal returns around FTSE disclosures: portfolio tests**

Panel A. FTSE constituents (24): CAR (portfolio t) by benchmark

| Event | Window | Never-named, equal-weighted | Matched controls | Large never-named stocks | Market model | Cross-sectional t (first benchmark) |
|---|---|---|---|---|---|---|
| Announcement, 7 Oct 2025 | [-1,+1] | 3.3% (2.27) | 1.3% (0.93) | 2.3% (1.54) | 2.6% (1.85) | 6.48 |
| | [-1,+5] | 7.8% (3.46) | 4.4% (2.16) | 6.3% (2.75) | 6.6% (3.04) | 5.18 |
| | [0,+20] | -2.4% (-0.61) | -0.1% (-0.03) | -1.4% (-0.35) | -5.5% (-1.47) | -0.80 |
| Confirmation, 7 Apr 2026 | [-1,+1] | 4.5% (2.54) | 2.9% (2.35) | 3.6% (2.51) | 3.6% (2.30) | 7.50 |
| | [-1,+5] | 4.7% (1.74) | 1.9% (1.02) | 3.5% (1.61) | 3.4% (1.42) | 4.81 |
| | [0,+20] | 10.0% (2.11) | 7.1% (2.20) | 10.6% (2.79) | 8.1% (1.95) | 3.68 |
| Constituent list, 21 Aug 2026 | [-1,+1] | 2.7% (1.82) | 1.1% (0.97) | 1.8% (1.41) | 1.3% (1.00) | 5.23 |
| | [-1,+5] | 4.4% (1.99) | 2.6% (1.47) | 3.9% (2.02) | 2.5% (1.30) | 5.15 |
| | [0,+20] | 4.6% (1.18) | 4.2% (1.37) | 5.2% (1.54) | 1.7% (0.51) | 2.87 |
| Effective date, 21 Sep 2026 | [-1,+1] | -0.1% (-0.11) | 0.6% (0.53) | 0.0% (0.03) | -0.9% (-0.78) | -0.20 |

Panel B. ITT group and named-but-excluded stocks: CAR (portfolio t)

| Event | Window | ITT (27), never-named benchmark | ITT (27), large-stock benchmark | Named-excluded (14), never-named benchmark | Named-excluded (14), large-stock benchmark |
|---|---|---|---|---|---|
| Announcement | [-1,+1] | 3.0% (2.43) | 2.0% (1.87) | 1.5% (1.11) | 0.5% (0.50) |
| | [-1,+5] | 7.5% (3.97) | 5.9% (3.72) | 6.2% (2.97) | 4.7% (3.10) |
| | [0,+20] | -1.0% (-0.32) | -0.1% (-0.03) | 4.8% (1.32) | 5.8% (2.18) |
| Confirmation | [-1,+1] | 3.1% (1.86) | 2.2% (1.83) | 0.4% (0.25) | -0.5% (-0.40) |
| | [-1,+5] | 3.2% (1.24) | 2.0% (1.08) | 0.3% (0.11) | -0.9% (-0.48) |
| | [0,+20] | 7.0% (1.57) | 7.6% (2.38) | 1.0% (0.20) | 1.6% (0.49) |
| Constituent list | [-1,+1] | 2.7% (2.05) | 1.8% (1.98) | 2.0% (1.32) | 1.1% (1.07) |
| | [-1,+5] | 3.2% (1.59) | 2.7% (1.91) | 0.9% (0.38) | 0.4% (0.22) |
| | [0,+20] | 1.2% (0.35) | 1.8% (0.75) | 1.2% (0.30) | 1.8% (0.65) |
| Effective date | [-1,+1] | 0.4% (0.34) | 0.6% (0.68) | 0.3% (0.21) | 0.5% (0.46) |

*Notes*: CAR = sum of daily portfolio abnormal returns. Portfolio t = CAR divided by the standard deviation of daily portfolio abnormal returns over trading days -130 to -11, times the square root of the window length (Brown & Warner, 1985). Market-model parameters estimated per stock over the same window against the never-named benchmark. The effective-date windows beyond +1 are not reported because the data end on 23 September 2026. Source: output/revision/t3_car_portfolio.csv.

The announcement and confirmation gains behaved differently afterwards. The announcement gain faded within a month: over days 0 to +20 the CAR is between -5.5% and -0.1% and never significant. The confirmation gain grew: over days 0 to +20 constituents earned 7.1% to 10.6%, with portfolio t-statistics between 1.95 and 2.79. The fading after the first, conditional announcement fits temporary price pressure (Harris & Gurel, 1986). The persistent gain after the confirmation, once the upgrade was certain and dated, fits a lasting shift in demand for the stocks (Shleifer, 1986; Chen et al., 2004).

Panel B separates the stocks that were likely to be included from those that were eventually passed over. The ITT group earned 7.5% in the week around the announcement (t = 3.97), close to the constituents' figure, which shows that the announcement gain does not depend on FTSE's later choice. Named-but-excluded stocks also gained in the announcement week (6.2%, t = 2.97) but not at the confirmation (0.4%, t = 0.25), when the market had more information about which stocks would qualify. Prices thus responded first to eligibility and then to the likelihood of inclusion.

**Takeaway.** Prices rose when FTSE announced the upgrade and again when it confirmed it; the confirmation gain lasted, and later disclosures added little.

### 4.3 The rebalancing session produced a trading surge only for included stocks

On 18 September 2026, the last session before the upgrade took effect, constituents' log trading value rose 0.79 above its level on other sessions in the window, relative to never-named stocks (standard error 0.12, t = 6.84; Table 5, panel A), and 0.84 relative to matched controls. On the effective date the excess fell to 0.20 (p = 0.057) and 0.34 (p = 0.007). Named-but-excluded stocks show no surge on either day (-0.01 and -0.16). Panel B shows mean abnormal trading value on 18 September against each stock's mean from 60 to 6 calendar days before the constituent list: constituents +0.76, matched controls -0.28, named-but-excluded stocks 0.00.

**Table 5. Trading value at the rebalancing session**

Panel A. Excess log trading value on the rebalancing and effective sessions, relative to other sessions from 6 August to 23 September 2026

| Group compared with controls | 18 Sep 2026 (rebalancing) | 21 Sep 2026 (effective date) | Observations |
|---|---|---|---|
| Constituents vs never-named stocks | 0.794*** (0.116) | 0.202 (0.106) | 10,820 |
| Constituents vs matched controls | 0.837*** (0.122) | 0.341** (0.122) | 1,536 |
| Named-but-excluded vs never-named stocks | -0.013 (0.116) | -0.159 (0.136) | 10,500 |

Panel B. Mean abnormal log trading value on 18 September 2026

| Group | Mean | Std. error | Stocks |
|---|---|---|---|
| FTSE constituents | 0.760 | 0.124 | 24 |
| Matched controls | -0.277 | 0.102 | 24 |
| Named-but-excluded | 0.000 | 0.153 | 14 |

*Notes*: Panel A: stock and date fixed effects; standard errors clustered by stock. Panel B: abnormal = daily log trading value minus the stock's mean from 60 to 6 calendar days before 21 August 2026. Sources: output/revision/t4c_spike_test.csv, output/revision/t4b_rebalance_groups.csv.

This surge is the signature of the price-pressure channel (Harris & Gurel, 1986): funds tracking FTSE benchmarks had to buy the first tranche of constituents at the closing price of 18 September, and nothing obliged them to trade the stocks FTSE had named and passed over. The null for named-but-excluded stocks is a direct falsification test: a general rise in trading among large or eligible stocks would have shown up there. The surge moved volume but not prices: the three-day CAR around the effective date is between -0.9% and 0.6% under every benchmark (Table 4), consistent with active investors having bought earlier and supplying the stocks to index funds at the close. Because the first tranche carried only 10% of the eventual index weight, this evidence concerns the first tranche; the three later tranches in 2027 may carry larger demand.

**Takeaway.** Index funds concentrated their first-tranche demand in one session, on the included stocks only, and prices had already adjusted by then.

### 4.4 The gains and the rebalancing surge rise with FTSE size segment

FTSE assigned the constituents to size segments on 21 August 2026: three large-capitalization stocks (VCB, VIC, VHM), three mid-capitalization stocks (BID, VPB, HPG) and 18 small-capitalization stocks among those in our sample (VIR, 2026). Index weights, and therefore passive purchases, rise with capitalization, so the price-pressure channel predicts a larger rebalancing surge for large-capitalization constituents. Foreign allocations follow benchmark weights (Raddatz et al., 2017), which points the same way for the persistent effect.

Table 6 splits the constituent coefficients by segment. The fall in illiquidity is largest for the three large-capitalization stocks: -0.61, -1.35 and -2.20 log points across the three windows, compared with -0.20, -0.63 and -0.82 for mid-capitalization stocks and -0.39, -0.85 and -1.00 for small-capitalization stocks. The ordering between mid and small stocks does not follow size, and with three stocks in each of the two upper segments the segment estimates rest on few clusters and should be read as descriptive. The rebalancing surge, in contrast, rises monotonically with segment: abnormal log trading value on 18 September 2026 averaged 1.23 for large-capitalization constituents, 0.98 for mid-capitalization and 0.65 for small-capitalization constituents. This supports H4.

**Table 6. Constituent effects by FTSE size segment**

| | Large (3 stocks) | Mid (3 stocks) | Small (18 stocks) |
|---|---|---|---|
| log Amihud: Announcement | -0.607* (0.273) | -0.204 (0.119) | -0.387*** (0.113) |
| log Amihud: Confirmation | -1.350** (0.413) | -0.629*** (0.076) | -0.855*** (0.133) |
| log Amihud: List and rebalancing | -2.198*** (0.396) | -0.819*** (0.229) | -1.002*** (0.187) |
| log trading value: List and rebalancing | 2.332*** (0.484) | 0.896*** (0.194) | 1.048*** (0.160) |
| Abnormal log trading value, 18 Sep 2026 (mean, SE) | 1.231 (0.110) | 0.976 (0.294) | 0.645 (0.150) |

*Notes*: One regression per outcome with stock and week fixed effects and all segment-by-window interactions; comparison group is never-named stocks; standard errors clustered by stock. The last row reports abnormal log trading value relative to each stock's mean from 60 to 6 calendar days before the constituent list. Sources: output/revision/t5_segments.csv, output/table7b_rebalance_by_segment.csv.

**Takeaway.** Index weight sets the size of the rebalancing trade and of the liquidity gain; every segment gained before index funds traded.

### 4.5 Volatility rose, so the illiquidity decline is conservative

Constituents became more volatile after the announcement. Their weekly log absolute return rose by 0.34 and 0.21 log points in the announcement and confirmation windows relative to never-named stocks, both significant at 0.1%; the list-window coefficient of 0.14 is not significant (Table 7, column 1). Because the Amihud ratio divides absolute returns by traded value, rising volatility pushes the ratio up; the measured decline in illiquidity therefore understates the gain in trading capacity. Controlling for the weekly log absolute return enlarges the constituent Amihud coefficients to -0.57, -1.00 and -1.20 (column 3).

Volatility also explains part of the spread result. The Corwin and Schultz (2012) spread did not narrow: it rose by 0.09 to 0.13 percentage points for constituents (Table 2, column 3), and by 0.14 to 0.20 points in the matched sample, from a pre-period mean of 0.57%. With the volatility control, the increase shrinks to 0.06, 0.08 and 0.12 points (Table 7, column 2). The high-low estimator loads on intraday price ranges, so the residual rise may reflect volatility that the weekly control misses rather than a higher cost of trading. We therefore limit our liquidity claims to price impact and trading activity, the dimensions that the Amihud ratio and trading value capture.

**Table 7. Volatility and liquidity**

| | (1) log absolute return | (2) CS spread, controlling for volatility | (3) log Amihud, controlling for volatility |
|---|---|---|---|
| Constituent × Announcement | 0.341*** (0.058) | 0.0006* (0.0003) | -0.574*** (0.102) |
| Constituent × Confirmation | 0.215*** (0.056) | 0.0008* (0.0003) | -1.003*** (0.122) |
| Constituent × List and rebalancing | 0.139 (0.086) | 0.0012* (0.0005) | -1.203*** (0.164) |
| log absolute return | | 0.0010*** (0.0001) | 0.535*** (0.021) |
| Observations | 34,369 | 34,369 | 34,369 |

*Notes*: Stock and week fixed effects; comparison group is never-named stocks; standard errors clustered by stock. Sources: output/revision/t6_volatility.csv, output/revision/t7_robustness.csv.

**Takeaway.** Rising trading value, which more than offset rising volatility, drove the fall in illiquidity.

## 5. Robustness and selection

### 5.1 Robustness of the liquidity result

Table 8 collects the robustness checks for the constituent Amihud result. The coefficients remain negative and of similar size in every specification.

**Table 8. Robustness of the constituent Amihud estimates**

| Specification | Announcement | Confirmation | List and rebalancing | Observations |
|---|---|---|---|---|
| Baseline (Table 2, column 1) | -0.392*** (0.098) | -0.888*** (0.124) | -1.129*** (0.178) | 34,369 |
| Size-tercile × week FE | -0.424*** (0.108) | -0.786*** (0.139) | -0.978*** (0.207) | 34,369 |
| Two-way clustering (stock and week) | -0.392*** (0.105) | -0.888*** (0.130) | -1.129*** (0.207) | 34,369 |
| Excluding Vingroup-family stocks | -0.389*** (0.100) | -0.863*** (0.114) | -1.007*** (0.168) | 34,072 |
| Constituent-specific linear trend | -0.382*** (0.098) | -0.874*** (0.156) | -1.111*** (0.225) | 34,369 |
| Matched sample with constituent-specific trend | -0.303* (0.124) | -0.619** (0.226) | -0.781* (0.292) | 4,751 |
| Excluding July to August 2025 from the pre-period | -0.354*** (0.105) | -0.850*** (0.130) | -1.091*** (0.183) | 31,212 |
| Controlling for volatility | -0.574*** (0.102) | -1.003*** (0.122) | -1.203*** (0.164) | 34,369 |
| Wild cluster bootstrap p-value, all controls (352 clusters, 999 draws) | < 0.001 | < 0.001 | < 0.001 | |
| Wild cluster bootstrap p-value, matched sample (48 clusters) | 0.003 | < 0.001 | < 0.001 | |
| Randomization inference, one-sided p (500 draws, 85-stock pool) | < 0.002 | < 0.002 | < 0.002 | |
| Placebo: fake event on 7 April 2025 (pre-period only) | 0.037 (0.104) | | | 18,163 |

*Notes*: Dependent variable log weekly Amihud illiquidity; comparison group is never-named stocks. Standard errors clustered by stock unless stated. Vingroup-family stocks in the sample are VIC, VHM and VRE (VPL listed too late to enter the sample). Wild cluster bootstrap: restricted residuals, Rademacher weights (Cameron et al., 2008). Sources: output/revision/t7_robustness.csv, output/revision/t_wild_bootstrap.csv, output/revision/t6_randomization_inference.csv.

**Pre-announcement months.** The pre-period deviations in Figure 1 are positive, so they work against the estimated declines rather than for them. Dropping July and August 2025, the two months with the largest positive deviations, changes the estimates to -0.35, -0.85 and -1.09. A constituent-specific linear trend leaves the estimates almost unchanged, with a trend coefficient of -0.0002 per week (standard error 0.003). The most demanding specification, the matched sample with a trend, gives -0.30, -0.62 and -0.78, all significant at 5%.

**Size-related shocks.** Replacing week fixed effects with size-tercile-by-week fixed effects compares constituents only with stocks in the same size tercile each week. The announcement coefficient rises slightly (-0.42), the later two shrink by 12% and 13%, and all remain significant at 0.1%. The predicted-constituent estimates in Table 3, which use only pre-period size, point the same way.

**Trading value.** Trading value behaves differently from the Amihud ratio: its pre-period trend is strong (0.010 log points per week, p < 0.001), and trend-adjusted effects fall to 0.28, 0.39 and 0.43 log points, the last significant only at 10%. We describe the trading-value result as an association.

**Inference and influential stocks.** Two-way clustering by stock and week widens standard errors by less than 17%. Excluding the three Vingroup-family stocks changes the estimates by at most 11%. With only 48 clusters in the matched sample, the wild cluster bootstrap p-values remain at or below 0.003.

**Placebo.** A fake event on 7 April 2025, estimated on pre-announcement data only, gives a coefficient of 0.04 (standard error 0.10).

### 5.2 Selection: FTSE's lists partly followed rising liquidity

The 14 stocks FTSE named as eligible but did not include allow a direct test of selection. As a group they became less illiquid than never-named stocks by 0.29, 0.55 and 0.87 log points across the three windows, 62% to 77% of the constituent effects, with the first estimate significant only at 10% (Table 9, panel A). Their gains are concentrated in two stocks, and the timing of those gains points to selection.

FTSE screened the April 2026 list on data as of 31 December 2025, which covers the first twelve weeks after the announcement. GEE and BSR entered the list in April. Relative to never-named stocks, their illiquidity fell by 1.15 log points between the announcement and 31 December 2025 (p = 0.024), inside the data window FTSE screened, and by 1.67 between January and April 2026 (Table 9, panel B). The twelve stocks named in November 2025 changed little: -0.02, -0.19 and -0.30 log points across the three windows, none significant at 5%. At the stock level (panel C), GEE's illiquidity fell by 1.83 log points before FTSE's cut-off date, and PLX, which FTSE dropped in April, was the only November name besides DPM to fall by more than 0.5 log points by the April list.

**Table 9. Named-but-excluded stocks and the timing of FTSE's screening**

Panel A. Named-but-excluded (14) and constituents vs never-named stocks

| Window | Constituents: log Amihud | Named-excluded: log Amihud | Named-excluded: log trading value |
|---|---|---|---|
| Announcement | -0.392*** (0.098) | -0.293 (0.154) | 0.589** (0.186) |
| Confirmation | -0.888*** (0.124) | -0.554* (0.255) | 0.683* (0.269) |
| List and rebalancing | -1.129*** (0.178) | -0.865** (0.304) | 0.653 (0.345) |

Panel B. log Amihud by FTSE screening window (W1: 7 Oct to 31 Dec 2025, inside the data FTSE screened for the April list; W2: 1 Jan to 6 Apr 2026; W3: from 7 Apr 2026)

| Group | W1 | W2 | W3 |
|---|---|---|---|
| Constituents (24) | -0.339** (0.110) | -0.440*** (0.100) | -0.932*** (0.129) |
| Named Nov 2025, not included (12) | -0.024 (0.092) | -0.185 (0.127) | -0.295 (0.168) |
| Added Apr 2026, not included: GEE, BSR | -1.146* (0.504) | -1.666*** (0.058) | -2.508*** (0.409) |

Panel C. Change in mean log Amihud relative to never-named stocks and to the stock's own pre-announcement level

| Stock | First named | W1 | W2 | W3 |
|---|---|---|---|---|
| BSR | Apr 2026 | -0.39 | -1.68 | -1.81 |
| GEE | Apr 2026 | -1.83 | -1.59 | -2.98 |
| DGC | Nov 2025 | 0.11 | 0.18 | 1.20 |
| DIG | Nov 2025 | -0.01 | 0.04 | 0.19 |
| DPM | Nov 2025 | -0.21 | -0.86 | -0.74 |
| DXG | Nov 2025 | -0.02 | -0.12 | -0.32 |
| EIB | Nov 2025 | 0.22 | -0.24 | -0.61 |
| FRT | Nov 2025 | -0.02 | -0.10 | -0.10 |
| KBC | Nov 2025 | 0.31 | 0.04 | 0.03 |
| KDC | Nov 2025 | 0.66 | 0.46 | 0.10 |
| KDH | Nov 2025 | -0.33 | -0.16 | -0.47 |
| PDR | Nov 2025 | -0.25 | -0.19 | -0.50 |
| PLX | Nov 2025 | -0.37 | -1.12 | -1.04 |
| SAB | Nov 2025 | -0.17 | 0.02 | -0.11 |

*Notes*: Panels A and B: one regression each with stock and week fixed effects on all 366 stocks; standard errors clustered by stock. Panel C: descriptive. List membership follows Viet Nam News (2025) and The Investor (2026a, 2026b). Sources: output/revision/t8_named_excluded.csv, output/revision/t8c_named_by_stock.csv.

This evidence bounds the constituent results. FTSE's screens rest on investability, and at least two stocks became eligible after their liquidity rose during the screening window. The same mechanism can operate among the final constituents, which FTSE chose on June 2026 data. Three results limit the concern. The ITT group, fixed on 2024 data, shows declines of 24% to 56%. The steps at the confirmation and the list survive a treated-specific trend. And the price reactions occur on disclosure dates, which a gradual selection process cannot produce. We therefore read the constituent estimates as upper bounds on the effect of the upgrade for included stocks and the ITT estimates as lower bounds.

**Takeaway.** FTSE's lists partly followed liquidity, but stocks fixed as likely constituents before the announcement also gained, so selection does not explain the liquidity response.

## 6. Discussion and conclusion

Vietnam's reclassification delivered its liquidity and price gains at the disclosures, months before index funds traded. Stocks that FTSE had screened as eligible on data from before the announcement became 24% less illiquid within months and 56% less illiquid by the constituent list; the stocks FTSE finally included became 32% and 68% less illiquid. Controlling for rising volatility makes the decline larger. Constituents' prices rose by 7.8% in the week around the announcement and by 4.5% around the confirmation, and only the confirmation gain lasted. The first index tranche added a trading surge at the rebalancing close, scaled by index weight and absent for excluded stocks, and no price change.

These findings favour the recognition channel over the price-pressure channel as the source of lasting effects. Investors acted on FTSE's public statements, and the index funds that the first tranche obliged to buy found prices already adjusted. This reading fits developed-market studies that find lasting liquidity gains after inclusion (Hegde & McDermott, 2003) and frontier-market evidence that index effects reflect investor demand rather than liquidity alone (Biktimirov & Afego, 2026). In Vietnam, demand and liquidity moved together, and both moved at disclosure. A frontier-to-emerging upgrade differs from a routine reconstitution because it changes which benchmark family can hold the stocks, and the information arrives in advance.

The price evidence also shows how investors learned. In the announcement week, the portfolio of stocks on FTSE's eligible lists gained whether or not FTSE later included them. At the confirmation, only the portfolio of stocks that went on to be included gained. Investors first priced eligibility and then the likelihood of inclusion, consistent with the recognition channel operating on the best available information at each step.

The segment evidence adds a second margin. The liquidity gain was largest for the three large-capitalization stocks that dominate the index, which suggests that investors weighted their attention by expected index weight, as benchmark-driven allocations would (Raddatz et al., 2017). The results also revise the conclusion that an index-level study of the same market reached. Aggregate liquidity of HOSE indices showed no structural break at FTSE watch-list reviews, which could suggest that classification decisions do not matter for liquidity. The stock-level design shows that the 2025 and 2026 decisions mattered for the stocks they concerned, while the broad market, which contains hundreds of stocks outside FTSE's screens, moved much less. In Vietnam's case, the classification event redistributed liquidity toward likely index stocks, and index averages diluted that redistribution.

The selection evidence sets a boundary on these conclusions. FTSE's eligibility lists partly followed rising liquidity, and the final constituents were chosen on data from mid-2026. We report the constituent estimates as upper bounds and the intention-to-treat estimates as lower bounds; both show a large response at disclosure.

The results carry two implications. For regulators, the liquidity and price dividend of an upgrade arrives with credible announcements, which rewards clear and early communication of reclassification steps. For issuers, the benefits concentrate in stocks that index providers can hold, which strengthens the case for measures that raise free float and foreign-ownership headroom, which enter FTSE's investability and foreign-headroom screens.

The study has limits. The sample uses stocks listed on 24 September 2026, which omits stocks delisted during the period. Only three trading days follow the effective date, and the first tranche carried 10% of the eventual weight, so the analysis cannot evaluate the three tranches of 2027. The price data do not identify investor type, so we cannot observe whether foreign investors drove the gains. The preliminary and April lists come from press reports of FTSE's screening results rather than FTSE documents. Extending the panel through September 2027 and adding foreign-flow data would test whether the constituent effects persist through the remaining tranches and whether foreign trading drives them.

## Appendix

**Table A1. Covariate balance before and after matching (constituents vs never-named stocks)**

| Variable | Constituent mean | Control mean, all | SMD, all | Control mean, matched | SMD, matched |
|---|---|---|---|---|---|
| Propensity score | 0.522 | 0.035 | 1.80 | 0.500 | 0.08 |
| Pre-period log trading value | 5.170 | 1.585 | 4.06 | 5.132 | 0.04 |
| Log median price | 3.228 | 2.725 | 0.66 | 3.061 | 0.22 |
| Pre-period return volatility | 0.0206 | 0.0207 | -0.03 | 0.0194 | 0.33 |

*Notes*: Nearest-neighbour matching on a logistic propensity score, three never-named controls per constituent, with replacement; 24 distinct control stocks. Pre-period log trading value is the mean daily log(1 + traded value, VND billion). SMD is the standardized mean difference. Log price and volatility remain imbalanced above 0.10, which is why we pair the matched estimates with the size-by-week and trend specifications. Source: output/revision/tA1_balance.csv.

**Table A2. Stocks by FTSE list**

| List | Stocks |
|---|---|
| Preliminary list, Nov 2025 (data as of 31 Dec 2024), later constituents (15) | GEX, HPG, MSN, SHB, SSI, STB, VCB, VCI, VHM, VIC, VIX, VJC, VND, VNM, VRE |
| Preliminary list, Nov 2025, not included (12 on HOSE) | DGC, DIG, DPM, DXG, EIB, FRT, KBC, KDC, KDH, PDR, PLX, SAB (HUT trades on the Hanoi exchange) |
| Added to the April 2026 list (data as of 31 Dec 2025) | BID, FPT, NVL (later constituents); GEE, BSR (not included); PLX removed |
| Constituents not on either eligible list | HCM, HDB, MCH, MSB, SSB, VPB (in sample); TCX, VCK, VPL (listed after Oct 2025, not in sample) |

*Sources*: Viet Nam News (2025); The Investor (2026a, 2026b); FTSE Russell (2026); VIR (2026).

## Declarations

**Data availability.** Daily price and volume data are public and were retrieved through the vnstock library (VCI source). The R code that reproduces all tables and figures (code/analysis.R, code/analysis_extensions.R, code/analysis_revision.R, code/figure1.R) is available from the corresponding author and will be deposited in a public repository on acceptance.

**Ethics.** The study uses public market data and involves no human participants.

**Author contributions (CRediT).** [To be supplied by the authors before submission.]

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. [Authors to confirm.]

**Declaration of competing interest.** The authors declare no competing interests. [Authors to confirm.]

**Declaration of generative AI use.** During the preparation of this work the authors used an AI assistant (Claude, Anthropic) to organise the analysis code, draft text, simulate peer review and verify references against Crossref. The authors reviewed and edited the content and take full responsibility for the publication.

## References

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets, 5*(1), 31–56. https://doi.org/10.1016/S1386-4181(01)00024-6

Becker-Blease, J. R., & Paul, D. L. (2006). Stock liquidity and investment opportunities: Evidence from index additions. *Financial Management, 35*(3), 35–51. https://doi.org/10.1111/j.1755-053X.2006.tb00146.x

Bekaert, G., Harvey, C. R., & Lundblad, C. (2007). Liquidity and expected returns: Lessons from emerging markets. *Review of Financial Studies, 20*(6), 1783–1831. https://doi.org/10.1093/rfs/hhm030

Biktimirov, E. N., & Afego, P. N. (2026). Is there an index effect in frontier markets? *International Review of Economics & Finance, 110*, 105562. https://doi.org/10.1016/j.iref.2026.105562

Brown, S. J., & Warner, J. B. (1985). Using daily stock returns: The case of event studies. *Journal of Financial Economics, 14*(1), 3–31. https://doi.org/10.1016/0304-405X(85)90042-X

Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. https://doi.org/10.1016/j.jeconom.2020.12.001

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics, 90*(3), 414–427. https://doi.org/10.1162/rest.90.3.414

Chen, H., Noronha, G., & Singal, V. (2004). The price response to S&P 500 index additions and deletions: Evidence of asymmetry and a new explanation. *The Journal of Finance, 59*(4), 1901–1930. https://doi.org/10.1111/j.1540-6261.2004.00683.x

Chordia, T., Roll, R., & Subrahmanyam, A. (2000). Commonality in liquidity. *Journal of Financial Economics, 56*(1), 3–28. https://doi.org/10.1016/S0304-405X(99)00057-4

Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance, 67*(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x

Dong, S., Zheng, J., Jia, H., & Zhang, Z. (2023). Impact of capital market internationalization on stock markets: Evidence from the inclusion of China A-shares in the MSCI Emerging Markets Index. *Research in International Business and Finance, 66*, 101989. https://doi.org/10.1016/j.ribaf.2023.101989

FTSE Russell. (2018, September 26). *FTSE classification of markets: September 2018*. https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/ftse-country-classification-update-2018.pdf

FTSE Russell. (2026, August). *Reclassification of Vietnam from frontier to secondary emerging market status: Frequently asked questions* (Version 1.3). https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf

Gregoriou, A., & Nguyen, N. D. (2010). Stock liquidity and investment opportunities: New evidence from FTSE 100 index deletions. *Journal of International Financial Markets, Institutions and Money, 20*(3), 267–274. https://doi.org/10.1016/j.intfin.2010.03.005

Harris, L., & Gurel, E. (1986). Price and volume effects associated with changes in the S&P 500 list: New evidence for the existence of price pressures. *The Journal of Finance, 41*(4), 815–829. https://doi.org/10.1111/j.1540-6261.1986.tb04550.x

Hau, H., Massa, M., & Peress, J. (2010). Do demand curves for currencies slope down? Evidence from the MSCI global index change. *Review of Financial Studies, 23*(4), 1681–1717. https://doi.org/10.1093/rfs/hhp095

Hegde, S. P., & McDermott, J. B. (2003). The liquidity effects of revisions to the S&P 500 index: An empirical analysis. *Journal of Financial Markets, 6*(3), 413–459. https://doi.org/10.1016/S1386-4181(02)00046-0

Ho, D. E., Imai, K., King, G., & Stuart, E. A. (2007). Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference. *Political Analysis, 15*(3), 199–236. https://doi.org/10.1093/pan/mpl013

Kang, W., & Zhang, H. (2014). Measuring liquidity in emerging markets. *Pacific-Basin Finance Journal, 27*, 49–71. https://doi.org/10.1016/j.pacfin.2014.02.001

LSEG. (2025, October 7). *FTSE Russell country classification: September 2025 review* [Press release]. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025

LSEG. (2026, April 7). *FTSE Russell announces results of the March 2026 semi-annual country classification review* [Press release]. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-russell-announces-results-march-2026-semi-annual-country-classification-review-equities-fixed-income

Nguyen, C. T., Hai, P. T., & Nguyen, H. K. (2021). Stock market returns and liquidity during the COVID-19 outbreak: Evidence from the financial services sector in Vietnam. *Asian Journal of Economics and Banking, 5*(3), 324–342. https://doi.org/10.1108/AJEB-06-2021-0070

Raddatz, C., Schmukler, S. L., & Williams, T. (2017). International asset allocations and capital flows: The benchmark effect. *Journal of International Economics, 108*, 413–430. https://doi.org/10.1016/j.jinteco.2017.06.007

Roth, J., Sant'Anna, P. H. C., Bilinski, A., & Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. *Journal of Econometrics, 235*(2), 2218–2244. https://doi.org/10.1016/j.jeconom.2023.03.008

Shleifer, A. (1986). Do demand curves for stocks slope down? *The Journal of Finance, 41*(3), 579–590. https://doi.org/10.1111/j.1540-6261.1986.tb04518.x

Stereńczak, S., Zaremba, A., & Umar, Z. (2020). Is there an illiquidity premium in frontier markets? *Emerging Markets Review, 42*, 100673. https://doi.org/10.1016/j.ememar.2019.100673

The Investor. (2026a, March 4). *FTSE Russell eyes 28 Vietnam stocks ahead of market status upgrade review*. https://theinvestor.vn/ftse-russell-eyes-28-vietnam-stocks-ahead-of-market-status-upgrade-review-d18516.html

The Investor. (2026b, April 8). *FTSE Russell names 32 Vietnamese stocks eligible for emerging-market index inclusion*. https://theinvestor.vn/ftse-russell-names-32-vietnamese-stocks-eligible-for-emerging-market-index-inclusion-d18800.html

Viet Nam News. (2025, November 13). *FTSE Russell plans inclusion of 28 Vietnamese stocks in 2026 market upgrade*. https://vietnamnews.vn/economy/1729462/ftse-russell-plans-inclusion-of-28-vietnamese-stocks-in-2026-market-upgrade.html

VIR. (2026, August 22). *FTSE Russell names 27 Vietnamese stocks in review*. https://vir.com.vn/ftse-russell-names-27-vietnamese-stocks-in-review-159265.html
