# Eligibility, not inclusion: Stock liquidity around Vietnam's FTSE Russell reclassification

## Abstract

FTSE Russell reclassified Vietnam from frontier to secondary emerging status in four public steps between October 2025 and September 2026. Using weekly data on 366 stocks listed on the Ho Chi Minh City Stock Exchange, we compare the 24 index constituents and 5 stocks that FTSE named as eligible but did not include with all other listed stocks. Amihud illiquidity of constituents fell by 59% relative to other stocks after FTSE confirmed the upgrade and by 67% once it published the constituent list; the smaller 32% decline after the first announcement is less robust. The eligible stocks left out of the index improved by as much, and the difference between the two groups is statistically indistinguishable from zero. The later-stage results survive matched controls, size-by-week fixed effects, a group-specific trend and randomization inference. Final inclusion added one effect: constituents traded 124% more than matched controls on the rebalancing session. Public eligibility, rather than index membership, carries the liquidity gain of a market upgrade.

**Keywords**: market reclassification; index effect; stock liquidity; frontier markets; difference-in-differences; Vietnam

**JEL classification**: G12; G14; G15

## 1. Introduction

Stocks that FTSE Russell named as eligible for its emerging-market indices became markedly more liquid after the provider announced Vietnam's upgrade, whether or not they later entered an index. Relative to other stocks on the Ho Chi Minh City Stock Exchange (HOSE), the Amihud (2002) illiquidity of the eventual constituents fell by 32% within the first six months and by 67% by the time FTSE published the constituent list; the later-stage declines survive every robustness check, while the first-stage decline halves in the most demanding one. Five stocks that appeared on FTSE's eligibility lists but did not make the final cut improved by as much. Index membership itself added a single event: a trading surge on the session before the upgrade took effect.

The question matters because market classification decides which benchmarks a country's stocks can enter, and benchmark weights steer international portfolio allocations (Raddatz et al., 2017). An upgrade from frontier to emerging status therefore promises new foreign demand, and policymakers in Vietnam pursued it for seven years of watch-list reviews. Whether the promised liquidity reaches individual stocks, which stocks it reaches, and when, has direct consequences for issuers' cost of capital, because liquidity is priced in emerging markets (Bekaert et al., 2007).

Existing evidence answers these questions poorly for frontier markets. In developed markets, additions to the S&P 500 raise trading activity and narrow spreads for years (Hegde & McDermott, 2003), and added firms with larger liquidity gains invest more (Becker-Blease & Paul, 2006). In frontier markets, index reconstitutions move prices, but liquidity measures other than volume show no reliable link to the price response (Biktimirov & Afego, 2026). Most studies of market reclassification also work with aggregate indices or price reactions, which cannot separate the stocks an upgrade targets from market-wide trends that accompany it. An earlier study of the same market by the present authors (anonymized for review) found that FTSE watch-list reviews did not coincide with structural breaks in index-level liquidity; that design could not ask which stocks gained.

Vietnam's reclassification offers a cleaner test for three reasons. FTSE Russell disclosed the decision in four dated steps: the announcement on 7 October 2025, the confirmation on 7 April 2026, the constituent list on 21 August 2026, and the effective date of 21 September 2026. FTSE also published eligibility lists before choosing the final constituents, which creates a second group of stocks that received the same public signal without index membership. Finally, hundreds of HOSE stocks received neither signal and trade under the same rules, hours and price limits.

We exploit this structure with a difference-in-differences design on 35,752 stock-weeks from October 2024 to September 2026. Treated stocks are the 24 constituents with a full pre-period and the 5 near-miss stocks (SAB, DXG, GEE, BSR and PLX) that press reports of FTSE's eligibility lists named but the final list excluded. Controls are the remaining 337 HOSE stocks, and a matched subsample pairs each constituent with three control stocks of similar pre-period trading value, price and volatility (Ho et al., 2007). The main outcome is the Amihud ratio computed on traded value in Vietnamese dong; we also report trading value and the Corwin and Schultz (2012) high-low spread.

The paper makes one contribution. It separates the liquidity effect of being named eligible under a market upgrade from the effect of entering the index. Three findings support this separation. First, constituents' illiquidity fell by 0.39, 0.88 and 1.12 log points across the announcement, confirmation and list stages (Table 2), with a flat pre-period and a break in the announcement month (Figure 1). Second, near-miss stocks fell by 0.75, 1.25 and 1.80 log points, and the gap between the two groups is not significant at any stage (Table 3). Third, only constituents traded abnormally on the rebalancing session of 18 September 2026, when their trading value rose 0.80 log points above matched controls (t = 4.87; Table 4). Randomization inference that draws pseudo-treated groups from the largest control stocks places every observed coefficient beyond all 500 placebo draws (Table 3).

Section 2 describes the institutional setting, reviews the literature and states the hypotheses. Section 3 presents the data and design. Section 4 reports the results, Section 5 the robustness checks, and Section 6 concludes.

## 2. Setting, literature and hypotheses

### 2.1 FTSE Russell's four-step reclassification of Vietnam

FTSE Russell kept Vietnam on its watch list for possible reclassification from September 2018. On 7 October 2025 it announced that Vietnam would move from frontier to secondary emerging status (LSEG, 2025). On 7 April 2026 it confirmed that Vietnam met the requirements and fixed the effective date of 21 September 2026, with inclusion phased in four tranches of 10%, 20%, 35% and 35% between September 2026 and September 2027 (LSEG, 2026). Between these dates the financial press reported FTSE's lists of eligible stocks: a preliminary list of 28 names in November 2025 (Viet Nam News, 2025) and a list of 32 eligible stocks in April 2026 (The Investor, 2026). On 21 August 2026 FTSE published the 27 constituents, effective after the close of 18 September 2026 (VIR, 2026).

This sequence separates two kinds of information. The announcement and confirmation told investors that Vietnamese stocks would enter emerging-market benchmarks and which stocks were candidates. The constituent list and the rebalancing session identified the stocks that index-tracking funds would buy. A liquidity response that appears at the announcement and reaches all eligible stocks points to the information itself; a response concentrated in constituents on the rebalancing date points to mechanical index demand.

### 2.2 Index inclusion and liquidity

Two channels link index membership to liquidity. The price-pressure channel works through the trades of index funds: additions force passive funds to buy on the effective date, which produces temporary volume and price effects around the event (Harris & Gurel, 1986). The demand and recognition channel works through a lasting change in the investor base. Shleifer (1986) interprets permanent price effects as evidence that demand curves for stocks slope down, and Chen et al. (2004) find asymmetric effects of additions and deletions that fit a gain in investor awareness. Hegde and McDermott (2003) show that S&P 500 additions narrow spreads and raise trading activity persistently, which they attribute to more information and more trading interest.

Liquidity gains from inclusion also have real consequences. Becker-Blease and Paul (2006) find that firms added to the S&P 500 with larger liquidity improvements increase capital investment, and Gregoriou and Nguyen (2010) find the mirror pattern for FTSE 100 deletions. Liquidity co-moves across stocks (Chordia et al., 2000), so any study of these effects must separate stock-specific changes from market-wide liquidity shocks.

### 2.3 Market reclassification and frontier markets

Reclassification moves a whole market between benchmark families. Mutual funds allocate across countries with reference to benchmark weights, so a change in classification changes capital flows (Raddatz et al., 2017), and an MSCI index change even moved currency values through this channel (Hau et al., 2010). The inclusion of China A-shares in the MSCI Emerging Markets Index improved market quality through liquidity and price synchronization (Dong et al., 2023). The frontier-market evidence is weaker. Biktimirov and Afego (2026) study FTSE Frontier 50 reconstitutions and find a persistent price effect but no reliable relation between liquidity and abnormal returns. No study we know of, in a search bounded to Crossref records and the literature cited here, estimates the stock-level liquidity effect of a frontier-to-emerging reclassification with a comparison group.

Liquidity carries particular weight in these markets. Bekaert et al. (2007) show that local market liquidity predicts returns in emerging markets, where segmentation from global capital is only partial, and Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity. A reclassification that improves liquidity for a subset of stocks could therefore shift their cost of capital relative to the rest of the market. Frontier markets also differ from developed ones in who trades: when domestic retail investors dominate turnover, the arrival of benchmark-tracking foreign money is a larger change in the investor base than an S&P 500 addition, and the recognition channel has more room to operate. The Vietnamese evidence available before the upgrade concerns market-wide liquidity shocks rather than classification events; for example, Nguyen et al. (2021) study the returns and liquidity of financial-services stocks during the COVID-19 outbreak. The present paper asks how a classification event redistributed liquidity across stocks.

### 2.4 Hypotheses

The recognition channel predicts that liquidity improves for every stock that the upgrade makes visible to international investors, from the moment the information becomes public. The price-pressure channel predicts a concentrated trading spike for constituents when index funds rebalance.

H1. After the reclassification announcement, stocks named as eligible became less illiquid than other HOSE stocks.

H2. The gap widened as FTSE moved from announcement to confirmation and to the constituent list.

H3. Index inclusion added a trading-value spike on the rebalancing session that eligible stocks outside the index did not share.

## 3. Data and empirical design

### 3.1 Sample

We collect daily open, high, low and close prices and share volume for all 405 common stocks listed on HOSE as of 24 September 2026, from 1 October 2024 to 23 September 2026. The data come from the VCI feed through the open-source vnstock library. We keep stocks with at least 200 trading days before 7 October 2025, zero volume on fewer than 20% of those days, and a median price of at least VND 1,000. Three constituents listed after October 2025 (TCX, VPL and VCK) fail the pre-period requirement, which leaves 24 constituents, 5 near-miss stocks and 337 control stocks: 366 stocks in total.

Table 1 shows that the treated stocks are much larger and more liquid than the average HOSE stock. Before the announcement, constituents traded a mean of 6.82 log VND billion per week against 2.30 for control stocks, and their mean weekly Amihud ratio was about three orders of magnitude lower. Near-miss stocks sit between the two groups. Spreads and absolute returns are similar across groups. The size gap motivates the matched sample and the size-specific checks below.

**Table 1. Sample composition and pre-announcement characteristics (October 2024 to 6 October 2025)**

| Group | Stocks | Stock-weeks | Mean weekly Amihud | Mean log trading value (VND bn) | Mean CS spread (%) | Mean absolute return (%) |
|---|---|---|---|---|---|---|
| FTSE constituents | 24 | 1,248 | 0.00017 | 6.82 | 0.57 | 1.40 |
| Near-miss eligible | 5 | 258 | 0.0089 | 5.45 | 0.60 | 1.59 |
| Other HOSE stocks | 337 | 17,383 | 0.19 | 2.30 | 0.61 | 1.37 |

*Notes*: Amihud is the mean daily ratio of absolute log return to traded value (VND billion) within a week. CS is the Corwin and Schultz (2012) spread. Source: authors' calculations (output/table1b_descriptives_by_group.csv).

### 3.2 Liquidity measures

Daily traded value equals the closing price times share volume, in VND billion. The Amihud (2002) ratio for stock i on day t is

ILLIQ_it = |R_it| / VAL_it,

where R_it is the log return and VAL_it the traded value. Traded value, rather than share volume, makes the ratio comparable across stocks with different price levels. We compute the Corwin and Schultz (2012) spread from two-day high and low prices and set negative estimates to zero. We winsorize each daily measure cross-sectionally at the 1st and 99th percentiles and aggregate to a stock-week panel, keeping weeks with at least three trading days. Weekly Amihud is the mean of daily ratios, used in logs; weekly trading value is the log of total traded value; the weekly spread is the mean daily spread. Kang and Zhang (2014) compare liquidity proxies for emerging markets and support the Amihud ratio for markets where most stocks trade daily, as on HOSE.

### 3.3 Estimation

The baseline specification is

y_iw = α_i + λ_w + Σ_k β_k (Included_i × P_kw) + Σ_k γ_k (NearMiss_i × P_kw) + ε_iw,

where y_iw is a liquidity measure for stock i in week w, α_i and λ_w are stock and week fixed effects, and P_1, P_2 and P_3 indicate the announcement window (7 October 2025 to 6 April 2026), the confirmation window (7 April to 20 August 2026) and the list-and-rebalancing window (21 August to 23 September 2026). Week fixed effects absorb market-wide shocks, including monetary conditions and the rally that accompanied the upgrade. We cluster standard errors by stock.

Constituents are the largest HOSE stocks, so shocks that affect large stocks differently could bias the comparison. We address this threat in four ways. We re-estimate on a matched sample that pairs each constituent with three control stocks by nearest-neighbour propensity score, with replacement, on pre-period traded value, price and return volatility (Ho et al., 2007); matching reduces the standardized mean difference in pre-period traded value to 0.07. We replace week fixed effects with size-tercile-by-week fixed effects. We estimate a monthly event study relative to September 2025 and test whether the pre-period coefficients are jointly zero (Roth et al., 2023). We add a group-specific linear trend. Because FTSE treated all stocks at the same dates, the specification has no staggered adoption, and the two-way fixed effects estimator does not suffer the negative-weighting problem that motivates Callaway and Sant'Anna (2021).

With only five near-miss stocks, cluster-robust standard errors for that group rely on few treated clusters. We therefore add randomization inference: we draw 500 pseudo-treated groups of 5 and of 24 stocks from the 94 control stocks in the top tercile of pre-period trading value, re-estimate the specification on control stocks only, and compare the observed coefficients with the placebo distribution.

For the rebalancing session we estimate a daily regression of log traded value on stock and date fixed effects and constituent-by-session interactions around 18 September 2026, with the last session before the constituent list as the reference day, on constituents and their matched controls.

### 3.4 Identification assumptions

The coefficients β_k and γ_k measure the change in eligible stocks' liquidity relative to control stocks. They identify the effect of eligibility under four assumptions, each of which we examine.

First, parallel trends: without the upgrade, eligible and control stocks would have followed the same liquidity path. The event study tests the observable implication for the twelve pre-announcement months, and the size-by-week, matched and trend specifications relax it in different directions.

Second, no anticipation before 7 October 2025. Vietnam sat on the FTSE watch list for seven years, so investors could have bought eligible stocks in advance of the decision. Anticipation of this kind would raise liquidity before the announcement and bias the estimates toward zero. The event study shows no such pre-announcement improvement in the Amihud ratio.

Third, no spillovers onto control stocks. If investors sold control stocks to buy eligible ones, the control group's liquidity would fall because of the treatment, and the difference-in-differences estimate would combine a gain for eligible stocks with a loss for the rest. Section 5 examines the control group's own path. Under either reading, the estimate measures how the upgrade redistributed liquidity toward eligible stocks, which is the quantity of interest for issuers and regulators.

Fourth, the treatment groups must not be defined by post-treatment outcomes. FTSE selected the final constituents in August 2026 on data that include part of the treatment period, so constituents might be stocks whose liquidity had already improved. The near-miss comparison guards against this concern: the near-miss stocks passed earlier eligibility screens and the final list excluded them, yet they improved by as much as the constituents. Stock fixed effects absorb all time-invariant differences in liquidity levels between groups.


## 4. Results

### 4.1 Eligible constituents became less illiquid from the announcement onward

Constituents' Amihud illiquidity fell relative to other HOSE stocks in each disclosure window, and the fall deepened at each stage. Table 2, column 1, reports coefficients of -0.39, -0.88 and -1.12 log points, which correspond to declines of 32%, 59% and 67% relative to control stocks. All three are significant at the 0.1% level. The matched sample in column 4 gives -0.39, -0.71 and -0.98 (declines of 32%, 51% and 62%), so the result does not depend on comparing the largest stocks with the smallest.

**Table 2. Liquidity of FTSE constituents relative to control stocks, by disclosure stage**

| | (1) log Amihud | (2) log trading value | (3) CS spread | (4) log Amihud | (5) log trading value | (6) CS spread |
|---|---|---|---|---|---|---|
| Sample | All HOSE | All HOSE | All HOSE | Matched 3:1 | Matched 3:1 | Matched 3:1 |
| Constituent × Announcement | -0.391*** (0.098) | 0.671*** (0.108) | 0.0009** (0.0003) | -0.388** (0.134) | 0.544** (0.162) | 0.0005 (0.0004) |
| Constituent × Confirmation | -0.884*** (0.123) | 1.025*** (0.125) | 0.0010** (0.0003) | -0.712*** (0.179) | 0.893*** (0.193) | 0.0010* (0.0004) |
| Constituent × List and rebalancing | -1.120*** (0.178) | 1.189*** (0.168) | 0.0013* (0.0005) | -0.979*** (0.233) | 1.157*** (0.235) | 0.0011 (0.0006) |
| Stock and week FE | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 35,259 | 35,259 | 35,259 | 5,146 | 5,146 | 5,146 |

*Notes*: Stock-week panel, October 2024 to September 2026; near-miss stocks excluded. Standard errors clustered by stock in parentheses. *, **, *** denote significance at 5%, 1% and 0.1%. Source: output/table2_did.csv.

Figure 1 shows the timing. In the twelve months before the announcement, the constituents' monthly coefficients fluctuate around zero; the joint test rejects equality to zero at the 5% level (F = 1.84, p = 0.037), driven by positive values two and three months before the announcement, which run against the later decline. The coefficient turns negative in October 2025 (-0.23) and falls steadily to -1.11 by August 2026. This pattern supports H1 and H2: illiquidity dropped when FTSE made the upgrade public and continued to fall as each later step resolved uncertainty about the outcome.

**Figure 1. Monthly event-study coefficients for FTSE constituents and near-miss eligible stocks**

![](figures/figure1_event_study.png)
 *Note*: Coefficients relative to September 2025 from regressions with stock and week fixed effects; 95% confidence intervals from stock-clustered standard errors. Dashed lines mark the announcement, confirmation and constituent-list months.

Trading value tells a similar story with one caveat. Constituents' trading value rose by 0.67, 1.03 and 1.19 log points relative to control stocks (Table 2, column 2). Unlike the Amihud ratio, trading value was already rising for constituents before October 2025 (Figure 1, lower panel; joint pre-trend test p < 0.001), so part of this increase continues an earlier trend. Section 5 reports trend-adjusted estimates.

**Takeaway.** Constituents' illiquidity fell by about one third within months of the announcement and by two thirds by the constituent list, with no comparable movement beforehand.

### 4.2 Eligible stocks left out of the index improved as much as constituents

The five near-miss stocks became less illiquid by as much as the constituents. Table 3 reports coefficients of -0.75, -1.25 and -1.80 log points for this group, equivalent to declines of 53%, 71% and 84%. The difference between constituents and near-miss stocks is positive in every window but never significant (p = 0.22, 0.46 and 0.18). Near-miss stocks show the same timing in Figure 1: no downward drift before October 2025 (their pre-period coefficients are imprecise and, if anything, positive) and a steady decline afterwards.

**Table 3. Two eligible groups: constituents and near-miss stocks**

| | (1) log Amihud | (2) log trading value | (3) CS spread |
|---|---|---|---|
| Constituent × Announcement | -0.391*** (0.098) | 0.671*** (0.108) | 0.0009** (0.0003) |
| Constituent × Confirmation | -0.884*** (0.123) | 1.025*** (0.125) | 0.0010** (0.0003) |
| Constituent × List and rebalancing | -1.120*** (0.178) | 1.189*** (0.168) | 0.0013* (0.0005) |
| Near-miss × Announcement | -0.753** (0.284) | 1.138*** (0.311) | 0.0021*** (0.0004) |
| Near-miss × Confirmation | -1.245** (0.480) | 1.562** (0.476) | 0.0027*** (0.0006) |
| Near-miss × List and rebalancing | -1.805*** (0.493) | 1.805** (0.547) | 0.0013 (0.0010) |
| Constituent minus near-miss, p-values (three windows) | 0.22, 0.46, 0.18 | 0.15, 0.27, 0.28 | 0.02, 0.01, 0.97 |
| Randomization-inference p-value, all windows (500 draws) | < 0.002 (both groups) | | |
| Observations | 35,752 | 35,752 | 35,752 |

*Notes*: Stock and week fixed effects; standard errors clustered by stock. Randomization inference draws pseudo-treated groups of 5 and 24 stocks from the 94 control stocks in the top pre-period trading-value tercile. Sources: output/table4_two_groups.csv, output/table4b_included_minus_nearmiss.csv, output/table6_randomization_inference.csv.

With five stocks, the near-miss estimates are imprecise, which is why we add randomization inference. None of the 500 pseudo-groups of five large control stocks produced a coefficient as negative as the observed one in any window (Table 3; output/table6_randomization_inference.csv). The placebo distribution centres at -0.22 in the list window, so large non-eligible stocks also became somewhat more liquid, but by one eighth of the near-miss effect.

The near-miss result reframes what the upgrade did. FTSE's eligibility screens rest on investability criteria such as size, free float and foreign-ownership headroom (LSEG, 2026), and the eligibility lists made these stocks visible to international investors months before the final selection. The evidence fits a recognition effect that reached every stock FTSE named, in line with the investor-awareness interpretation of index effects (Chen et al., 2004) and the benchmark channel of international flows (Raddatz et al., 2017), and it does not require index membership.

**Takeaway.** Being named eligible, not being included, carries the persistent liquidity gain.

### 4.3 Index inclusion added a one-session trading spike at rebalancing

Inclusion did matter on one day. On 18 September 2026, the last session before the upgrade took effect, constituents' trading value rose 0.80 log points above matched controls (standard error 0.17, t = 4.87; Table 4, panel A). In the 27 sessions before it, including the day FTSE published the constituent list, no coefficient differs from zero at the 5% level, and the effect vanishes after the effective date (0.23 on 21 September, not significant). Panel B shows raw abnormal trading value by group: constituents +0.76 log points, matched controls -0.20, and near-miss stocks +0.22 with a standard error of 0.33.

**Table 4. Trading value around the rebalancing session of 18 September 2026**

Panel A. Daily regression, constituents vs matched controls

| Session | Coefficient | Std. error | t |
|---|---|---|---|
| 16 Sep 2026 (t-2) | 0.032 | 0.161 | 0.20 |
| 17 Sep 2026 (t-1) | 0.123 | 0.164 | 0.75 |
| 18 Sep 2026 (rebalancing) | 0.805 | 0.165 | 4.87 |
| 21 Sep 2026 (effective date) | 0.226 | 0.164 | 1.38 |
| 22 Sep 2026 | -0.132 | 0.181 | -0.73 |
| 23 Sep 2026 | -0.134 | 0.207 | -0.65 |

Panel B. Mean abnormal log trading value on 18 September 2026 (relative to each stock's mean before the list announcement)

| Group | Mean | Std. error | Stocks |
|---|---|---|---|
| FTSE constituents | 0.760 | 0.124 | 24 |
| Near-miss eligible | 0.220 | 0.327 | 5 |
| Matched controls | -0.199 | 0.121 | 28 |

*Notes*: Panel A: stock and date fixed effects; reference day is the last session before 21 August 2026; standard errors clustered by stock; all 25 earlier session coefficients (not shown) have |t| < 1.2. Sources: output/table_rebalance_reg.csv, output/table5_rebalance_by_group.csv.

This spike is the signature of the price-pressure channel (Harris & Gurel, 1986): index funds tracking FTSE benchmarks had to buy constituents at the closing price of 18 September, and nothing obliged them to trade near-miss stocks. The spike supports H3, and its one-day duration separates it from the persistent improvement documented in Sections 4.1 and 4.2.

**Takeaway.** Index membership concentrated passive demand in one session; it did not add a lasting liquidity gain beyond eligibility.

### 4.4 The gains rise with FTSE size segment, and so does the rebalancing spike

FTSE assigned the constituents to size segments on 21 August 2026: three large-capitalization stocks (VCB, VIC, VHM), three mid-capitalization stocks (BID, VPB, HPG) and 18 small-capitalization stocks among those in our sample (VIR, 2026). Segment matters for both channels. Index weights, and therefore passive purchases, rise with capitalization, so the price-pressure channel predicts a larger rebalancing spike for large-capitalization constituents. Benchmark-driven foreign allocations also concentrate in the heaviest index weights (Raddatz et al., 2017), which points the same way for the persistent effect.

Table 5 splits the constituent coefficients by segment. The fall in illiquidity is largest for the three large-capitalization stocks: -0.61, -1.35 and -2.19 log points across the three windows, compared with -0.20, -0.62 and -0.81 for mid-capitalization stocks and -0.39, -0.85 and -0.99 for small-capitalization stocks. The ordering between mid and small stocks does not follow size, and with three stocks in each of the two upper segments the segment estimates are imprecise. The rebalancing spike, in contrast, rises monotonically with segment: abnormal log trading value on 18 September 2026 averaged 1.23 for large-capitalization constituents, 0.98 for mid-capitalization and 0.65 for small-capitalization constituents.

**Table 5. Constituent effects by FTSE size segment**

| | Large (3 stocks) | Mid (3 stocks) | Small (18 stocks) | Near-miss (5 stocks) |
|---|---|---|---|---|
| log Amihud: Announcement | -0.606* (0.273) | -0.203 (0.119) | -0.386*** (0.113) | -0.753** (0.284) |
| log Amihud: Confirmation | -1.345** (0.413) | -0.625*** (0.075) | -0.850*** (0.133) | -1.245** (0.480) |
| log Amihud: List and rebalancing | -2.189*** (0.395) | -0.810*** (0.229) | -0.993*** (0.186) | -1.805*** (0.493) |
| log trading value: List and rebalancing | 2.333*** (0.484) | 0.896*** (0.193) | 1.048*** (0.159) | 1.805** (0.547) |
| Abnormal log trading value, 18 Sep 2026 (mean, SE) | 1.231 (0.110) | 0.976 (0.294) | 0.645 (0.150) | 0.220 (0.327) |

*Notes*: One regression per outcome with stock and week fixed effects and all group-by-window interactions; standard errors clustered by stock. The last row reports raw abnormal trading value relative to each stock's mean before the constituent list. Sources: output/table7_segment_heterogeneity.csv, output/table7b_rebalance_by_segment.csv, output/table5_rebalance_by_group.csv.

The two patterns separate the channels again. The rebalancing spike scales with index weight, as mechanical index demand implies. The persistent gain is present in every segment and among near-miss stocks with no index weight at all, so it does not require index demand, although it is largest for the three stocks that dominate the index.

**Takeaway.** Index weight sets the size of the one-day rebalancing trade; eligibility sets whether a stock gains liquidity in the months before.

## 5. Robustness and threats to identification

Table 6 collects the robustness checks for the Amihud result. The coefficients remain negative, significant and of similar size across specifications.

**Table 6. Robustness of the constituent Amihud estimates**

| Specification | Announcement | Confirmation | List and rebalancing | Observations |
|---|---|---|---|---|
| Baseline (Table 2, column 1) | -0.391*** (0.098) | -0.884*** (0.123) | -1.120*** (0.178) | 35,259 |
| Size-tercile × week FE | -0.405*** (0.099) | -0.751*** (0.126) | -0.913*** (0.186) | 35,259 |
| Two-way clustering (stock and week) | -0.391*** (0.105) | -0.884*** (0.130) | -1.120*** (0.206) | 35,259 |
| Excluding Vingroup-family stocks | -0.388*** (0.100) | -0.858*** (0.113) | -0.998*** (0.167) | 34,962 |
| Constituent-specific linear trend | -0.369*** (0.098) | -0.850*** (0.155) | -1.080*** (0.223) | 35,259 |
| Matched sample with constituent-specific trend | -0.207 (0.122) | -0.431* (0.187) | -0.646* (0.260) | 5,146 |
| Placebo: fake event on 7 April 2025 (pre-period only) | 0.026 (0.104) | | | 18,631 |

*Notes*: Dependent variable log weekly Amihud illiquidity. Standard errors clustered by stock unless stated. Vingroup-family stocks are VIC, VHM, VRE and VPL. Source: output/table3_robustness.csv.

**Size-related shocks.** Replacing week fixed effects with size-tercile-by-week fixed effects compares constituents only with stocks in the same size tercile each week. The announcement coefficient rises slightly (-0.40), the later two shrink by 15% and 18%, and all remain significant at 0.1%. The randomization inference in Section 4.2 makes the same point from a different angle: large control stocks improved by about one fifth of the constituent effect.

**Pre-existing trends.** The Amihud event study shows no downward drift before October 2025, and adding a constituent-specific linear trend leaves the estimates almost unchanged (-0.37, -0.85, -1.08), with a trend coefficient of -0.0006 per week (not significant). The trend specification on the matched sample is the most demanding check: it halves the announcement coefficient, which loses significance (p < 0.1), while the confirmation and list coefficients remain significant at 5%. Trading value behaves differently. Its pre-period trend is strong (0.011 log points per week, p < 0.001), and trend-adjusted effects fall to 0.26, 0.38 and 0.43 log points (output/table3_robustness.csv). We therefore treat the Amihud ratio as the main outcome and describe the trading-value result as an association.

**Inference and influential stocks.** Two-way clustering by stock and week widens standard errors by less than 20%. Excluding the four Vingroup-family stocks, so that no single business group drives the result, changes the estimates by at most 11%.

**Matching quality.** Matching removes most of the pre-period gap between constituents and controls. The standardized mean difference in pre-period log trading value falls from 3.97 in the full sample to 0.07 in the matched sample, and in the propensity score from 1.69 to 0.06 (Appendix Table A1). The difference in return volatility (0.27) and log price (0.16) remains above the conventional 0.10 threshold, which is why we pair the matched estimates with the size-by-week and trend specifications.

**Spillovers to control stocks.** A reallocation of trading from control stocks to eligible stocks would inflate the difference-in-differences estimates. The randomization inference speaks to this concern for the most comparable controls: pseudo-treated groups drawn from the 94 largest control stocks show an average change of -0.22 log points in the list window, a small improvement. Large non-eligible stocks became slightly more liquid while eligible stocks gained far more, so the estimates do not rest on a decline in the comparison group.

**Placebo.** A fake event on 7 April 2025, estimated on pre-announcement data only, gives a coefficient of 0.03 (standard error 0.10).

**Spreads.** The Corwin and Schultz (2012) spread did not narrow. It rose by 0.09 to 0.13 percentage points for constituents (Table 2, column 3), from a pre-period mean of 0.57%, and by more for near-miss stocks. Because the high-low estimator also rises with intraday volatility, and eligible stocks traded more actively after the announcement, we do not read this as higher transaction costs. The result limits the paper's claim to price impact and trading activity, the dimensions the Amihud ratio and trading value capture.

**Remaining threats.** The design cannot rule out a shock that coincided with the announcement and affected exactly the stocks FTSE named, beyond what size, price and volatility matching absorbs. Foreign-ownership limits and free float drive both FTSE eligibility and foreign investor interest, so the eligibility effect may operate through foreign trading; the price data used here do not record investor type.

## 6. Discussion and conclusion

Vietnam's reclassification made stocks that FTSE Russell named as eligible more liquid from the day the upgrade became public, whether or not they entered an index. Constituents' Amihud illiquidity fell by 32% relative to other HOSE stocks after the announcement and by 67% by the constituent list; eligible stocks left out of the index improved by as much, and the two groups are statistically indistinguishable. Index inclusion added one thing: a trading surge on the rebalancing session that disappeared the next day.

These findings favour the recognition channel over the price-pressure channel as the source of lasting liquidity gains. The upgrade functioned as a public certificate for a set of stocks, and investors acted on the certificate months before any index fund had to trade. This reading reconciles two strands of evidence: developed-market studies that find lasting liquidity gains after inclusion (Hegde & McDermott, 2003), and frontier-market studies that find weak liquidity effects of index reconstitutions (Biktimirov & Afego, 2026). A frontier-to-emerging upgrade differs from a routine reconstitution because it changes which benchmark family can hold the stocks, and the information arrives in advance.

The segment evidence adds a second margin. The persistent gain was largest for the three large-capitalization stocks that dominate the index, which suggests that the investors who responded to eligibility weighted their attention by expected index weight, as benchmark-driven allocations would (Raddatz et al., 2017). Yet near-miss stocks with no index weight gained as much as small-capitalization constituents. Recognition set whether a stock gained; expected weight set how much.

The results also revise the conclusion that an index-level study of the same market reached. Aggregate liquidity of HOSE indices showed no structural break at FTSE watch-list reviews, which could suggest that classification decisions do not matter for liquidity. The stock-level design shows that the October 2025 decision mattered a great deal for the stocks it named, while the broad market, which contains hundreds of stocks outside FTSE's eligibility screens, moved much less. Classification events redistribute liquidity; index averages dilute that redistribution.

The results carry two implications. For regulators, the liquidity dividend of an upgrade arrives with the announcement and extends to stocks that meet eligibility screens, which strengthens the case for measures that raise free float and foreign-ownership headroom. For issuers near the eligibility thresholds, being named eligible matters more for liquidity than the final index decision.

The study has limits. The near-miss group contains five stocks, so its point estimates are imprecise even though randomization inference rejects chance. The sample uses stocks listed on 24 September 2026, which omits stocks delisted during the period. Only three trading days follow the effective date, so the analysis cannot evaluate the phased inclusion tranches of 2027. The price data do not identify foreign investors, so the channel through which eligibility raised liquidity remains an inference that the present data cannot test. Extending the panel through September 2027 and adding foreign-flow data would test whether the eligibility effect persists through the remaining tranches and whether foreign trading drives it.

## Appendix

**Table A1. Covariate balance before and after matching (constituents vs control stocks)**

| Variable | Constituent mean | Control mean, all | SMD, all | Control mean, matched | SMD, matched |
|---|---|---|---|---|---|
| Propensity score | 0.475 | 0.037 | 1.69 | 0.459 | 0.06 |
| Pre-period log trading value | 5.170 | 1.665 | 3.97 | 5.107 | 0.07 |
| Log median price | 3.228 | 2.746 | 0.63 | 3.110 | 0.16 |
| Pre-period return volatility | 0.0206 | 0.0207 | -0.03 | 0.0196 | 0.27 |

*Notes*: Nearest-neighbour matching on a logistic propensity score, three controls per constituent, with replacement; 28 distinct control stocks. Pre-period log trading value is the mean daily log(1 + traded value, VND billion). SMD is the standardized mean difference. Source: output/table_matching_balance.csv.

## Declarations

**Data availability.** Daily price and volume data are public and were retrieved through the vnstock library (VCI source). The R code that reproduces all tables and figures is available from the corresponding author and will be deposited in a public repository on acceptance.

**Ethics.** The study uses public market data and involves no human participants.

**Author contributions (CRediT).** [To be supplied by the authors before submission.]

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. [Authors to confirm.]

**Declaration of competing interest.** The authors declare no competing interests. [Authors to confirm.]

**Declaration of generative AI use.** During the preparation of this work the authors used an AI assistant (Claude, Anthropic) to organise the analysis code, draft text and verify references against Crossref. The authors reviewed and edited the content and take full responsibility for the publication.

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

LSEG. (2025, October 7). *FTSE Russell country classification: September 2025 review* [Press release]. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025

LSEG. (2026, April 7). *FTSE Russell announces results of the March 2026 semi-annual country classification review* [Press release]. https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-russell-announces-results-march-2026-semi-annual-country-classification-review-equities-fixed-income

Nguyen, C. T., Hai, P. T., & Nguyen, H. K. (2021). Stock market returns and liquidity during the COVID-19 outbreak: Evidence from the financial services sector in Vietnam. *Asian Journal of Economics and Banking, 5*(3), 324–342. https://doi.org/10.1108/AJEB-06-2021-0070

Raddatz, C., Schmukler, S. L., & Williams, T. (2017). International asset allocations and capital flows: The benchmark effect. *Journal of International Economics, 108*, 413–430. https://doi.org/10.1016/j.jinteco.2017.06.007

Roth, J., Sant'Anna, P. H. C., Bilinski, A., & Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. *Journal of Econometrics, 235*(2), 2218–2244. https://doi.org/10.1016/j.jeconom.2023.03.008

Shleifer, A. (1986). Do demand curves for stocks slope down? *The Journal of Finance, 41*(3), 579–590. https://doi.org/10.1111/j.1540-6261.1986.tb04518.x

Stereńczak, S., Zaremba, A., & Umar, Z. (2020). Is there an illiquidity premium in frontier markets? *Emerging Markets Review, 42*, 100673. https://doi.org/10.1016/j.ememar.2019.100673

The Investor. (2026, April 8). *FTSE Russell names 32 Vietnamese stocks eligible for emerging-market index inclusion*. https://theinvestor.vn/ftse-russell-names-32-vietnamese-stocks-eligible-for-emerging-market-index-inclusion-d18800.html

Viet Nam News. (2025, November 13). *FTSE Russell plans inclusion of 28 Vietnamese stocks in 2026 market upgrade*. https://vietnamnews.vn/economy/1729462/ftse-russell-plans-inclusion-of-28-vietnamese-stocks-in-2026-market-upgrade.html

VIR. (2026, August 22). *FTSE Russell names 27 Vietnamese stocks in review*. https://vir.com.vn/ftse-russell-names-27-vietnamese-stocks-in-review-159265.html
