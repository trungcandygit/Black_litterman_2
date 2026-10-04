## Devil's Advocate Report — Checkpoint 1

Reviewed: Research Question Brief and pre-registered methodology in `paper2/process/03_brainstorm_round2.md`, plus Amendments A3/A4 in `paper2/process/decisions.md`. Context only: `data/` listing (405 per-symbol CSVs, a listing file dated 2026-09-24, typical history of 519 trading days). No outcome analyses were run.

Independence note: `decisions.md` already contains Amendment A4, which reports the "pre-registered" outcome (4/4 event tests survive, 0/22 characteristics survive, about +1.7% next day). This Checkpoint 1 is therefore retrospective. Pre-registration protects only against what was fixed before the data were seen, and the A4 text shows the results were seen before this review. I judge the design below as written, but the verdict cannot claim the independence a true Checkpoint 1 would have.

### Verdict: REVISE

The design is a serious improvement on the usual zoo paper (counted family, hold-out, FDR, costs reported). It is not fatally flawed. But several protocol-level weaknesses undermine the headline claim, namely that price-limit events predict returns. They must be fixed or explicitly disclosed before the event result can be presented as a finding. No Critical issue, so progression is not blocked.

Steel-man: the authors state the multiplicity problem up front, fix the family before computation, report all 26 tests, allow nulls to be a publishable "power" finding, require sign agreement plus a confirmation-half t > 1.96 plus full-sample FDR, and report net-of-cost spreads. Delayed price discovery at limit-hit is a well-motivated mechanism with a large event count. This is better practice than most of the literature it responds to.

### Critical Issues (Blocks Progression)

No critical issues identified.

### Major Issues

1. **The event definition does not identify limit hits, and mixes true ceiling hits with near-hits**
   - **Type**: Method (construct validity)
   - **Location**: "ceiling event = daily return >= 6.5% and close equal to the day's high"
   - **Problem**: HOSE's daily band is about +/-7% around a reference price rounded to the tick. Return >= 6.5% and close == high captures (i) true locked or ceiling closes, (ii) strong closes of 6.5-6.99% that never touched the ceiling, (iii) rounding and tick artefacts for low-priced stocks (a 10-VND tick on a 10,000-VND stock is 0.1%, so the attainable ceiling return itself varies by price), (iv) ex-dividend or rights days where the exchange's reference price differs from the previous close, so computed returns differ from the band return, (v) different bands (first-day listings, other rules) that appear in the sample. It also misses ceiling hits where the close falls back. Close == high is not evidence of a limit-hit, because many ordinary strong days close at the high through the ATC auction. The hypothesis "limits create delayed price discovery" is about unfilled queue demand, and the rule cannot distinguish that from an ordinary 6.5% momentum day.
   - **Impact**: The estimand is "strong up day that closed at its high," not "price-limit hit." Any mechanism claim about price limits is unsupported. Floor events have the same problem, plus an asymmetry (selling queues, margin calls).
   - **Recommendation**: Reconstruct the exchange reference price (previous close adjusted for the corporate action, if the data are adjusted) and the tick-rounded ceiling and floor per stock-day. Define a hit as close == computed limit price. Report separate results for exact hits, near-hits (6.5%-limit, close == high), and locked days (open=high=low=close). State in the paper whether the VCI series are adjusted, and check that adjustment does not alter event membership.

2. **Consecutive limit days and overlapping windows make the t+1 and t+1..t+5 results mechanically dependent**
   - **Type**: Method
   - **Location**: "Outcomes: ... t+1, t+2..t+5. Inference: event-day cross-sectional means, clustered by date"
   - **Problem**: Ceiling closes cluster in streaks. If t is a ceiling and t+1 opens at or near the ceiling again (unfilled queue), the t+1 return is largely determined by the persistence of the queue, which is the mechanism but is also non-tradable. Overlapping 5-day windows for repeated events on the same stock are not independent, and clustering by date does not address within-stock serial dependence. Market-wide rally days produce many simultaneous events (cross-sectional dependence, only partly handled by date clustering). The 4 tests (ceiling/floor x two horizons) are also near-duplicates, so "4/4 survive" is not four independent confirmations.
   - **Impact**: Reported significance is probably overstated, and the "4/4" count creates a false impression of robustness.
   - **Recommendation**: Treat the first event in a streak (non-overlapping events, with a gap rule) as the primary event and report streak continuation separately. Two-way cluster by date and stock (or use date-block bootstrap). Present the 4 tests as one family with 2 effective degrees of freedom. Count effective, not nominal, tests.

3. **The discovery/confirmation split is not valid as specified for weekly data with long lookbacks**
   - **Type**: Method (design)
   - **Location**: Rule 3, "first half of weeks = discovery, second half = confirmation"; 60-110-day lookbacks
   - **Problem**: (a) Characteristics use 60d to 110d windows, so the first confirmation weeks reuse discovery-period returns in their predictors, and the 5-day outcome straddles the boundary. No embargo is specified. (b) "Survives" requires the full-sample FDR to pass, but the full sample contains the confirmation half. The discovery half then plays almost no inferential role (only a sign check), so this is not a hold-out in the usual sense. (c) With about 79 weekly cross-sections (about 21-24 months minus the first 60-110 days of warm-up), each half holds about 35-40 weeks, so a confirmation t > 1.96 on 40 weekly slopes has low power for realistic anomaly sizes. Failure to confirm will be read as "no anomaly" when it is mostly low power. A single time split also confounds "false discovery" with regime change in a short window. (d) The 22 characteristics are highly collinear (VOL/IVOL/RANGEVOL/DOWNVOL, REV1W/MAX/LIMITFREQ), so the effective number of tests is far below 22 and BH is not tuned to it.
   - **Impact**: "0/22 characteristics survive" is uninformative about the existence of anomalies (power), and the confirmation step does less than the paper's framing suggests.
   - **Recommendation**: Add an embargo of at least the longest lookback plus horizon. Select on the discovery half only, test once on confirmation (a true out-of-sample test with a pre-set one-sided sign, which also raises power). Report minimum detectable effects (MDE) per characteristic given the sample so the null is interpretable. Report effective number of tests (e.g. from eigenvalues of the characteristic correlation matrix).

4. **Selection across papers sits outside the 26-test family (forking paths at the programme level)**
   - **Type**: Bias (selection / researcher degrees of freedom)
   - **Location**: Standing order in A4 item 22 ("advance only the paper with the best-estimated result"); round-2 brainstorm of 14 ideas
   - **Problem**: Paper C was chosen after a round-2 search "for a result with more statistical power," after Papers A and B were produced, and the advancement rule favours the best-estimated result. The FDR across 26 tests controls false discoveries inside Paper C only. It does not control for choosing C over A/B, nor the 14 candidate ideas, nor the earlier universe of tests in Papers A/B. Decision 18/A3 admits that H1/H5 are motivated by Paper A's results. The brief itself concedes the search is p-hacking "unless the search is itself the object of inference" but does not make it the object of inference.
   - **Impact**: The reported adjusted p-values and "survives" statements understate the true selection. A hostile referee will count this as a garden of forking paths. Note this concern grows once an A4-style "advance the best" rule is applied: the paper that advances is by construction the one with the most favourable draw (winner's curse).
   - **Recommendation**: Disclose the full programme-level count (all papers, all ideas tried) in the manuscript, give the programme-level adjusted threshold, and report the advance rule's effect on estimates (winner's-curse caveat). Prefer reporting Paper C regardless of its rank.

5. **Post hoc rescue/robustness block (A4) is added after seeing a large result, and the decision rule is asymmetric**
   - **Type**: Bias (moving goalposts, partially)
   - **Location**: Amendment A4 items 21-22
   - **Problem**: Ten robustness checks are added after the result, and labelled post hoc, which is honest. But advancement is conditional on checks (a)-(c) passing, so the post hoc checks now decide the paper's fate. Checks (a) and (c) will be the decisive tests, yet they were designed after the outcome was known, and a result that passes ten checks chosen after the fact is not pre-registered evidence. Also the pre-registered primary outcome (close-to-close t+1 from a ceiling close) is not tradable by construction, so the pre-registered test measured something the user cannot act on. The larger the t+1 effect, the more suspicious it should be: +1.7% next day after a ceiling close is exactly what an unfilled-queue gap-up would produce mechanically, and the mean may be dominated by the overnight gap (check b).
   - **Impact**: The pre-registration provides little protection for the main claim. The primary result is likely a microstructure mechanical continuation, not a predictability finding in the economic sense.
   - **Recommendation**: Make the tradable next-open-to-close and next-open-to-t+5 return the primary outcome in any manuscript, and describe close-to-close results as descriptive. Freeze the A4 checks now, declare which pass/fail criteria decide advancement (thresholds, not "survives"), and write them to `decisions.md` before running anything else.

6. **"Market-adjusted return with dollar-volume weights" is a weak benchmark for a mostly small-cap event set**
   - **Type**: Method
   - **Location**: "Outcome: next-week stock return, market-adjusted by the dollar-volume-weighted market"
   - **Problem**: Dollar-volume weighting concentrates the benchmark in a handful of very liquid names (large banks and real-estate conglomerates, in this sample period dominated by few tickers). Limit events are concentrated in smaller, high-beta, retail-traded stocks. Subtracting the return of a large-cap-dominated index leaves size, beta and volatility premia in the "abnormal" return. A limit-up stock has different beta from the benchmark by construction (a stock that just rose 7% is more likely a high-beta day stock). Also 20% bottom-liquidity exclusion is only a robustness check, while the illiquid names are where bid-ask bounce and price discreteness matter. The control in the brief ("non-event stock-days of the same stock") is stock-specific but not matched on date or liquidity (this is only added as post hoc check (c)).
   - **Impact**: The abnormal-return level is not interpretable as alpha, and the sign of any benchmark mismatch is unknown.
   - **Recommendation**: Pre-specify (before more computation) the primary benchmark as a same-date, same-liquidity-tercile (or size-matched) non-event control; report the equal-weighted market and a beta-adjusted version as sensitivity. Report the benchmark's top-10 weight share.

7. **Survivorship and sample construction are unaddressed**
   - **Type**: Bias (selection)
   - **Location**: "Sample: all stocks with complete history in the lookback window"; data listing dated 2026-09-24
   - **Problem**: The universe is built from a listing snapshot taken on 2026-09-24, so stocks delisted, suspended or removed during 2024-08..2026-09 are absent. "Complete history in the lookback window" also drops new listings (e.g. a symbol with only 86 rows) and stocks with trading halts, and limit-hit events are disproportionately followed by halts and by late-listing price rules. Dropping stocks after an event (missing t+1..t+5) is a classic conditional-on-future selection that biases event study means. The text also gives inconsistent sample sizes (347 stocks vs "about 100 stocks x 80 weeks").
   - **Impact**: Both the zoo and the event estimates may carry survivorship and attrition bias of unknown sign; the sample size claim in the brief is not reliable.
   - **Recommendation**: Report the universe construction (counts at each filter, number of delistings or halts), treat missing post-event returns explicitly (halt = 0 return or carry-forward, show sensitivity), and fix the stated sample size.

### Minor Issues

- The brief says "two-sided unless a sign is pre-registered," then pre-registers no sign for any of the 22 characteristics, although the literature gives clear priors for several (MAX, IVOL, AMIHUD, REV1W). Pre-register signs for those that have literature priors and use one-sided tests on confirmation; this raises power at no cost in validity.
- Three multiplicity procedures are named (HLZ t >= 3.0, BH-FDR at 5%, Holm) but the survival rule uses only a conjunction of confirmation t > 1.96 and BH. State which procedure is primary. HLZ t >= 3.0 with about 79 weekly slopes is close to unreachable; say so.
- Newey-West with 4 lags on about 40 weekly slopes (confirmation half) is unreliable for 60-110d overlapping characteristics. Report a bootstrap or a longer lag sensitivity.
- Several characteristics are mechanically linked to the event definition (REV1W, MAX, LIMITFREQ, MIN, OVERNIGHT). The "event" family and the "zoo" family are not separate; the 26-test family has overlapping content.
- Rank-normal standardization before Fama-MacBeth makes coefficients unit-free but hides economic size; the net-of-cost decile spread is promised but its cost model (HOSE round-trip fees, sell tax, tick size, price-limit queue fill probability) is not specified.
- "A multivariate model with all survivors" is outside the 26-test family and is conditional on selection; label it descriptive.
- The brief says "Fama-MacBeth ... Newey-West" but the Corwin-Schultz spread estimator is known to be biased in price-limit markets (the daily high/low range is censored at the band); CSSPREAD and RANGEVOL are exposed to censoring. The brief notes censoring only for idea #6.
- The brief's FINER "Novel 4" claim ("Vietnamese evidence ... is thin") is asserted without a literature check recorded in the file.

### Observations

- A null family result is worth presenting as a power analysis (MDE table), which is a good use of this data window. Pre-commit to that framing.
- The strongest design asset is the commitment to report all 26 results; keep it, and report the actual 22 + 4 table including non-survivors.
- There is a possible frame lock: the question is posed as "which characteristics predict returns" (a testing frame), when with 21-24 months the more defensible frame is "what can this window rule out?" (estimation with intervals). A different tradition (Bayesian shrinkage, hierarchical modelling of anomaly effects, Harvey-Liu 2020 style) would shrink 22 estimates jointly and report posterior intervals instead of a binary survive/fail.
- Another unquestioned premise is that the ceiling-close effect is an anomaly. A microstructure tradition would ask whether it is simply the unfilled order book (a queue). Under that reading it is expected, large, and not an inefficiency a trader can capture, so "predictable continuation" and "tradable alpha" are different claims and the paper should never merge them.
- Retail-dominated markets with price limits (China, Korea, Taiwan) have a large literature on limit-hit "magnet effects" and volatility spillover. The brief cites none of it, which weakens the novelty claim and makes the 4 hypotheses less ex ante than stated.
- Today is 2026-10-04 and the data end about 2026-09; the sample covers a single market regime (a strong rally period for Vietnam in 2025-2026, plus the possible FTSE upgrade run-up). External validity across regimes is nil.

### Strongest Counter-Argument

"The headline result is a mechanical artefact of the exchange's price limit queue. A stock that closes at its high after a 6.5%+ rise very often has excess buy orders pending, so it opens higher the next day. The close-to-close return of +1.7% is largely the overnight gap, which no investor can earn, because the stock cannot be bought at the ceiling close. The event rule does not even identify true limit hits, 'pre-registration' was applied to a non-tradable outcome with the tradable tests added after the result was seen, the benchmark is a large-cap-dominated index that mismeasures abnormal returns for small-caps, the 'confirmation' sample is the second half of a 21-month window that overlaps in lookback with the first, and Paper C was picked as the best of several papers and 14 ideas, so adjusted p-values over 26 tests understate the selection. 0/22 characteristics surviving says nothing except that 40 weeks is too short."

### What's Missing

- A power analysis or MDE table for the 22 characteristics and the event tests under the actual number of weeks and effective stocks.
- Exact limit-price reconstruction (reference price, tick, band rules) and a definition of a hit that matches exchange rules; adjustment status of the price series.
- A pre-specified tradable primary outcome, cost model (fees, tax, queue fill probability, short-sale constraints), and capacity; the real-world ability to buy at the next open when queues are present.
- Programme-level multiplicity accounting (Papers A, B, C, 14 ideas) and a winner's-curse caveat for the advance-the-best rule.
- Handling of halts, delistings, new listings, and survivorship in the universe.
- Literature on price-limit magnet and delayed price discovery effects in other retail-dominated markets, and on anomaly replication with short samples.
- Regime and subperiod evidence (up/down markets, pre/post any regulatory change such as margin rules or the FTSE reclassification process), or an explicit statement that none is possible.
- An out-of-window validation plan (e.g. extend the data back, or reserve the next 6 months as a true hold-out declared now).

### Stress Test Results

| Test | Result |
|------|--------|
| Remove strongest source (drop the ceiling t+1 result) — does the argument hold? | Partly: the null zoo stands but is uninformative without a power analysis; the paper loses its only positive finding |
| Flip the research question (limit hits cause no predictability beyond the unfilled queue) — is the opposing view credible? | Yes: it is the default microstructure reading and is not ruled out until the next-open tradable result and the exact-hit definition are in place |
| Apply to different context (other regimes, HNX/UPCoM, other limit-band markets) — does the finding generalize? | No (untested): single 21-24 month regime, HOSE only, no out-of-window sample |
| "So what?" — is the significance justified? | Not yet: significance is statistical and non-tradable as designed; economic significance rests on post hoc checks (a)-(c) and cost assumptions not yet specified |

### Concession log
No rebuttals received at this checkpoint; concession protocol not triggered.

Disclosure: this report was produced by an AI agent (devils_advocate_agent role) from the files named above; it did not run any outcome analysis, and it did not read the `06_integrity*` or `05_verification*` files.
