# Phase 1, round 2 — wide brainstorm for a result with more statistical power (skill: deep-research / research_question_agent, FINER; devils_advocate_agent Checkpoint 1)

Trigger: the user asked to brainstorm more ideas to find a stronger result. Zero-question mode.

## Integrity guard stated up front (Devil's Advocate, Major)
"Searching for a significant result" is p-hacking unless the search is itself the object of inference. Binding rules for this round:
1. Every idea tried is counted. The candidate set and hypotheses below are fixed BEFORE any of them is computed; all of them are reported, significant or not.
2. Tests are two-sided unless a sign is pre-registered from literature; family-wise / false-discovery control is applied across the whole family (Harvey-Liu-Zhu t >= 3.0 threshold; Benjamini-Hochberg FDR 5%; Holm).
3. Discovery/confirmation: first half of weeks = discovery, second half = confirmation. A characteristic "survives" only if the sign agrees and the confirmation t exceeds 1.96 AND it passes FDR on the full sample.
4. Statistical significance is not economic significance: decile spreads are also reported net of costs.

## Candidate ideas (14) with data fit and power
| # | Idea | Data | Power | FINER avg |
|---|---|---|---|---|
| 1 | Characteristic zoo (about 20 characteristics) with discovery-confirmation and FDR control, 347 HOSE stocks weekly | daily OHLCV | high (about 100 stocks x 80 weeks) | 4.4 |
| 2 | Price-limit event study: next-day/next-week returns after limit-up / limit-down closes (delayed price discovery) | daily OHLCV, thousands of events | high | 4.4 |
| 3 | MAX/lottery effect in a retail-dominated market | daily | medium-high | (inside #1) |
| 4 | Overnight vs intraday return decomposition | daily open/close | medium | (inside #1) |
| 5 | Abnormal volume / volume-conditioned reversal | daily | medium-high | (inside #1) |
| 6 | Range-based volatility estimators vs close-to-close for the low-volatility effect (price limits censor ranges) | daily | medium | 3.8 |
| 7 | ML (LASSO/RF) combination of characteristics vs OLS | daily | low-medium (79 weeks) | 3.6 |
| 8 | Volatility-managed portfolios (Moreira-Muir type) on the bank-sector return | 144 months | low | 3.4 |
| 9 | Trend following / time-series momentum, bank sector | 144 months | low | 3.2 |
| 10 | Day-of-week / turn-of-month / Tet seasonality | daily | medium | 3.0 (weak prior, high forking-path risk) |
| 11 | Network centrality of banks and portfolio risk | 25 banks | low | 3.4 |
| 12 | Regime-aware meta-allocator (1/N vs optimized) | banks monthly | low | 3.6 |
| 13 | Cost-aware anomaly capacity using Corwin-Schultz spreads | daily | medium | 3.8 |
| 14 | Extending Paper B to put surviving characteristics into BL views | both | medium | 4.0 (depends on #1) |

## Selected: Paper C = ideas 1 + 2 (+3,4,5 as members of the zoo; 13 as the economic-significance layer; 14 as a final link)
Primary RQ: Which price- and volume-based characteristics predict next-week stock returns on HOSE after controlling for the number of characteristics examined, and do the price limits create predictable continuation or reversal?

FINER: Feasible 5, Interesting 4, Novel 4 (Vietnamese evidence with explicit multiple-testing and a hold-out half is thin), Ethical 5, Relevant 5 -> 4.6.

## Pre-registered family (fixed before computation)
Characteristics at the end of week t (weekly sorting; all use only data up to t), 22 in total:
- Momentum/reversal: REV1W (5-day return), REV1M (20-day return), MOM3M (60d skip 5), MOM6M (110d skip 5), IMOM (idiosyncratic 60d skip 5).
- Risk: VOL (60d std), IVOL (60d std of market-model residual), BETA (60d), DOWNVOL (60d downside deviation), RANGEVOL (60d Parkinson), MAX (max daily return, 20d), MIN (min daily return, 20d), SKEW (60d skewness), KURT (60d).
- Liquidity/volume: AMIHUD (60d mean |r|/dollar volume), LNDVOL (log 60d mean dollar volume, size proxy), DVOLCHG (20d / 60d dollar-volume ratio), TURNCHG (volume 20d/60d ratio), CSSPREAD (60d mean Corwin-Schultz).
- Intraday: OVERNIGHT (20d mean close-to-open return), INTRADAY (20d mean open-to-close return), LIMITFREQ (20d share of days at a +/-6.5% close).
Outcome: next-week (5 trading days) stock return, market-adjusted by the dollar-volume-weighted market. Estimator: weekly Fama-MacBeth cross-sectional regressions on cross-sectionally standardized (rank-normal) characteristic, one characteristic at a time (22 univariate tests) and a multivariate model with all survivors; Newey-West (4 lags) t-statistics. Sample: all stocks with complete history in the lookback window; liquidity screen = exclude bottom 20% by dollar volume as a robustness check (pre-registered, not a replacement).
Price-limit events: ceiling event = daily return >= 6.5% and close equal to the day's high; floor event = return <= -6.5% and close equal to the low. Outcomes: market-adjusted return over days t+1, t+2..t+5. Inference: event-day cross-sectional means with standard errors clustered by date; control = non-event stock-days with the same stock and market-adjusted return, same sign filter. Hypotheses: H_A ceiling -> positive t+1 abnormal return; H_B floor -> negative or reversal (two-sided, no sign pre-registered).
Family size for FDR: 22 characteristic tests + 4 event tests (ceiling/floor x t+1, t+1..t+5) = 26 primary tests.

## Devil's Advocate Checkpoint 1 — verdict: PASS with binding constraints (above)
Strongest counter-argument: "Twenty-one months of daily data cannot support 22 anomaly tests; any survivors will be noise." Response: that is the reason for FDR, a hold-out half, and reporting all 26 results; a null family is a publishable finding about power, a survivor is a finding only if it passes the hold-out.
