# Round-2 sections drafted independently of the framing decision

<!-- Every number maps to output/table8_car_events.csv, output/table9_volatility_spreads.csv, output/table10_naming_timing.csv, output/table10b_nearmiss_by_stock.csv. -->

### Prices moved at each disclosure, and only for constituents

Constituents earned positive abnormal returns around each of the three disclosures that preceded the effective date. We measure abnormal returns as the stock's daily log return minus the equal-weighted mean return of control stocks and sum them over event windows. Around the announcement, constituents earned 3.3% over days -1 to +1 (t = 6.4) and 7.6% over days -1 to +5 (t = 5.1). Around the confirmation, they earned 4.5% over days -1 to +1 (t = 7.5), and around the constituent list 2.6% (t = 5.1). Nothing happened around the effective date: the cumulative abnormal return over days -1 to +5 was -0.6% (t = -0.8).

The announcement and confirmation gains behaved differently afterwards. The announcement gain reversed within a month: the cumulative abnormal return over days 0 to +20 was -2.4% and not significant. The confirmation gain grew: over days 0 to +20 constituents earned 10.0% (t = 3.7). The reversal after the first announcement fits temporary price pressure (Harris & Gurel, 1986), while the persistent gain after the confirmation, once the outcome was certain, fits a lasting shift in demand for the stocks (Shleifer, 1986; Chen et al., 2004). The near-miss stocks show no significant abnormal return in any window, with point estimates between -0.8% and 8.6%.

**Table X. Cumulative abnormal returns around FTSE disclosures**

| Event | Window | Constituents: CAR (t) | Near-miss: CAR (t) |
|---|---|---|---|
| Announcement, 7 Oct 2025 | [-1,+1] | 3.3% (6.40) | 1.4% (1.80) |
| | [-1,+5] | 7.6% (5.07) | 6.9% (1.39) |
| | [0,+20] | -2.4% (-0.82) | 8.6% (1.05) |
| Confirmation, 7 Apr 2026 | [-1,+1] | 4.5% (7.47) | 0.2% (0.14) |
| | [-1,+5] | 4.7% (4.80) | 0.1% (0.09) |
| | [0,+20] | 10.0% (3.68) | 4.3% (1.51) |
| Constituent list, 21 Aug 2026 | [-1,+1] | 2.6% (5.09) | 0.9% (0.66) |
| | [-1,+5] | 4.4% (5.09) | -0.8% (-0.34) |
| | [0,+20] | 4.6% (2.87) | 3.3% (0.80) |
| Effective date, 21 Sep 2026 | [-1,+1] | -0.2% (-0.23) | -0.3% (-0.22) |
| | [-1,+5] | -0.6% (-0.77) | 0.7% (0.31) |

*Notes*: Abnormal return = daily log return minus the equal-weighted mean log return of the 337 control stocks. t-statistics from the cross-section of 24 constituents and 5 near-miss stocks. The effective-date [0,+20] window is not available (data end on 23 September 2026). Source: output/table8_car_events.csv.

### Volatility rose, so the Amihud decline is conservative

Eligible stocks became more volatile after the announcement. Their weekly log absolute return rose by 0.33, 0.21 and 0.15 log points across the three windows relative to control stocks (the last only at the 10% level). Because the Amihud ratio divides absolute returns by traded value, rising volatility pushes the ratio up; the measured decline in illiquidity therefore understates the gain in trading capacity. Controlling for the weekly log absolute return enlarges the constituent Amihud coefficients to -0.57, -1.00 and -1.20.

Volatility also explains part of the spread result. With the same control, the Corwin and Schultz (2012) spread rises by 0.06, 0.08 and 0.12 percentage points for constituents, smaller than the unconditional 0.09, 0.10 and 0.13. The high-low estimator loads on intraday price ranges, so the residual rise may still reflect volatility the weekly control misses rather than a higher cost of trading.

**Table Y. Volatility and liquidity**

| | (1) log absolute return | (2) CS spread, controlling for volatility | (3) log Amihud, controlling for volatility |
|---|---|---|---|
| Constituent × Announcement | 0.333*** (0.058) | 0.0006* (0.0003) | -0.568*** (0.102) |
| Constituent × Confirmation | 0.212*** (0.056) | 0.0008* (0.0003) | -0.997*** (0.122) |
| Constituent × List and rebalancing | 0.145 (0.086) | 0.0012* (0.0005) | -1.197*** (0.164) |
| Near-miss × Announcement | 0.445*** (0.057) | 0.0017*** (0.0004) | -0.989** (0.303) |
| Near-miss × Confirmation | 0.439*** (0.103) | 0.0023*** (0.0005) | -1.478** (0.492) |
| Near-miss × List and rebalancing | 0.196 (0.148) | 0.0012 (0.0010) | -1.909*** (0.529) |
| log absolute return | | 0.0010*** (0.0001) | 0.531*** (0.021) |
| Observations | 35,752 | 35,752 | 35,752 |

*Notes*: Stock and week fixed effects; standard errors clustered by stock. Source: output/table9_volatility_spreads.csv.

### Near-miss stocks: the timing of their gains precedes their naming

(Text to be written after the framing decision. Evidence: late-named GEE and BSR improved by -1.05 (p = 0.02) before November 2025 and -1.51 (p < 0.001) between November 2025 and April 2026, before press reports first listed them as eligible; early-named SAB and DXG changed by -0.03 to -0.31; PLX by -0.63 to -1.03. Source: output/table10_naming_timing.csv, output/table10b_nearmiss_by_stock.csv.)
