# Phase 1 (Scoping) — Brainstorm, RQ Brief, Devil's Advocate Checkpoint 1

Skill files applied: `deep-research/SKILL.md` (full-mode Phase 1), `agents/research_question_agent.md` (FINER, scope, sub-questions, bindings), `agents/devils_advocate_agent.md` (Checkpoint 1, severity, concession protocol), `references/mode_selection_guide.md`.

`[SOCRATIC-NON-GENERATION-EXIT: explicit_user_request]` — the user explicitly asked the system to brainstorm alternative ideas ("cứ brain storming theo skill"); the candidates below are AI-generated starting points, not user-derived insights. Zero-question mode is active (user standing order), so selection is made by the FINER scores and recorded here.

## Evidence on hand that constrains the brainstorm (all from this project's own R outputs)
- Single-view BL-K_IO re-implementation on the current panel: Sharpe 0.71 vs 1/N 0.73 (the earlier headline is not reproduced).
- BL-KMV (pre-specified clustering-view rule): Sharpe 0.61, no significant difference from any benchmark; SPA vs 1/N p = 0.76.
- Minimum detectable Sharpe-ratio difference at 80% power, 106 months: about 0.32.
- Signal ICs: low volatility t = 2.66, momentum t = 1.48, composite t = 1.50.
- Ordering of simple rules: 1/N ≈ ERC > HRP > cap-weighted ≈ BL0 > tangency. The cap-weighted anchor is the weak link of inverse BL in a concentrated sector.
- Broad universe (347 stocks, daily, 79 weekly OOS steps): min-variance LW Sharpe 0.94, tangency-LW 0.98, 1/N 0.15, cluster-view rules ≈ 0.6.
- Data now available: 25 banks monthly 2014-06..2026-05 (price, cap); 347 HOSE stocks daily 2024-08..2026-09 (OHLCV); ICB codes; 21 banks' daily high/low for spreads.

## Candidate research questions (Step 2)

| # | Candidate (type) | Data fit | F | I | N | E | R | Avg |
|---|---|---|---|---|---|---|---|---|
| 1 | What share of out-of-sample BL performance is attributable to the equilibrium anchor, the views, and covariance shrinkage, and does the attribution replicate on an independent universe? (comparative / attributional) | banks monthly (12y) + broad daily | 5 | 4 | 4 | 5 | 5 | **4.6** |
| 2 | Do daily price limits distort volatility-based signals, and does a limit-adjusted volatility improve low-volatility selection? (causal-ish) | broad daily; limit hits detectable from OHLC | 4 | 4 | 5 | 5 | 4 | 4.4 |
| 3 | Net of stock-specific spreads estimated from OHLC, which anomaly strategies survive in Vietnam? (evaluative) | broad daily, 2 years only | 4 | 3 | 3 | 5 | 4 | 3.8 |
| 4 | Which price/volume characteristics predict next-week returns across 347 stocks, and do ML combinations add to simple ones? (predictive) | broad daily; 79 weeks | 4 | 4 | 3 | 5 | 4 | 4.0 |
| 5 | Does correlation-network centrality of banks predict portfolio risk contribution in stress? (correlational) | banks monthly; small N | 3 | 3 | 3 | 5 | 3 | 3.4 |
| 6 | Can a regime state (dispersion, correlation) tell when optimized rules beat 1/N? (predictive) | banks monthly; few regimes | 3 | 4 | 3 | 5 | 4 | 3.8 |
| 7 | Short-horizon reversal vs liquidity in Vietnam (descriptive/causal) | broad daily | 4 | 3 | 2 | 5 | 3 | 3.4 |

Selection: candidate 1. Reasons: (a) highest FINER average; (b) it turns the null result of the clustering-view study into the paper's identifying variation (a factorial design) instead of discarding it; (c) both samples are used for what each is good at (long time series in banks, wide cross-section in 347 stocks); (d) the ex-ante hypotheses below can be falsified. Candidate 2 is kept as an extension inside the study (a limit-adjusted volatility is one of the view characteristics only if time allows; it is not part of the pre-registered core).

## Research Question Brief (Step 3-5)

**Topic area:** Black–Litterman portfolio construction in a concentrated emerging equity market.

**Primary research question:** How much of the out-of-sample Sharpe-ratio variation across Black–Litterman portfolios in Vietnamese equities is attributable to the equilibrium anchor, the view signal, the covariance estimator and the position cap, and does that attribution replicate on an independent universe?

**FINER:** Feasible 5/5 (code exists; both datasets on hand), Interesting 4/5 (anchor-vs-signal puzzle; null results of signal-based BL), Novel 4/5 (factorial attribution with block-bootstrap CIs and a confirmation sample is rare in BL work), Ethical 5/5 (public market data), Relevant 5/5 (practitioners choose these four ingredients). **Average 4.6/5**, no criterion below 4.

**Scope boundaries.**
- In scope: long-only, fully invested, monthly (banks) and weekly (broad) rebalanced rules; four anchors (cap, equal, ERC, 50/50 cap–equal blend); five view types (none, momentum, low volatility, composite, K-means cluster views); two covariance estimators (sample, Ledoit–Wolf); two caps.
- Out of scope: short selling, derivatives, intraday trading, factor-model returns, CVaR objectives, tax; any claim about future performance.
- Domain: portfolio construction / empirical asset pricing. Timeframe: banks Aug 2017–May 2026 OOS; broad Feb 2025–Sep 2026 OOS. Geography: Vietnam (HOSE, bank sector and 347 liquid HOSE stocks). Population: listed equities; banks as the discovery sample, the broad universe as the confirmation sample.
- Key assumptions: adjusted prices are correct; the dollar-volume proxy is an acceptable stand-in for market capitalization in the broad sample; the 10-year VGB yield read from the authors' earlier figure is accurate to about 5 bp.

**Sub-questions** (each inherits the full scope; no deviation approved):
1. Which factor (anchor, view, covariance, cap) explains the largest share of Sharpe-ratio variance across the factorial portfolios, with block-bootstrap uncertainty?
2. Do view signals add Sharpe ratio relative to no view once the anchor and covariance are held fixed (an equivalence test with a pre-set margin)?
3. Does the factor ranking replicate on the 347-stock weekly universe, and how does trading cost change it?

**Sub-question bindings (Schema 1):**
1. inherits population=Vietnamese listed equities; timeframe=as above; geography=Vietnam; domain=portfolio construction; deviations: none.
2. inherits the same; deviations: none.
3. inherits the same; deviations: none.

**Pre-registered hypotheses (fixed before the factorial results were computed):**
- H1: the anchor explains a larger share of Sharpe variance than the view type.
- H2: Ledoit–Wolf covariance has a higher marginal Sharpe than sample covariance.
- H3: view types do not raise the Sharpe ratio over "no view" by more than 0.10 (annualized) on average (equivalence, TOST-style, block bootstrap).
- H4: the ranking of factor importance (anchor, covariance, cap, view) is the same in the bank panel and the broad universe (Spearman rank correlation of η² shares equals 1 only if identical; reported descriptively).
- H5: the equal-weight and ERC anchors have a higher marginal Sharpe than the capitalization anchor in the bank panel because bank capitalization is concentrated.

## Devil's Advocate Report — Checkpoint 1

**Verdict: REVISE (no Critical issues; Major issues addressed in the design below)**

*Critical:* none.

*Major:*
1. **Descriptive ANOVA on Sharpe ratios of 80 same-sample portfolios is not inference.** The 80 Sharpe estimates share one time series; their variance decomposition has no sampling distribution unless the time dimension is resampled. *Fix:* recompute the whole factorial on circular-block-bootstrap resamples of months (the portfolio weights are fixed; only the return months are resampled) and report percentile intervals of the shares, plus pairwise contrasts with Holm correction.
2. **Hypothesis H1 was suggested by results already seen** (EW/ERC > cap, signal weak). *Fix:* declare H1/H5 as hypotheses motivated by the earlier study and flag them as not independent; the broad universe is the confirmatory sample and its results are reported without any design change after seeing the bank results (log any change in decisions.md).
3. **Broad universe has 79 weekly steps and one market regime; anchor is a dollar-volume proxy.** *Fix:* state it as low-power replication; also report the bank-only and broad-only attribution separately; do not pool.
4. **Large factorial inflates apparent "findings".** *Fix:* the design is fully crossed and fully reported; there are no omitted cells; the trial ledger equals the number of cells (80 per universe).

*Minor:* the cap factor with "no cap" and sample covariance will give extreme weights (that is the intent; report maximum weight); defining δ for non-cap anchors uses the anchor portfolio's own window return and variance — state the convention.

*Observations:* the earlier BL-K_IO headline not being reproduced is itself a finding to disclose to the authors; the attribution framing makes the null results informative.

**Strongest counter-argument:** "A variance decomposition of backtest Sharpe ratios on 106 months and 25 correlated banks just measures noise." Response in design: the bootstrap shares will show whether any factor's share is distinguishable from the share expected under the null of no true factor effects (permutation benchmark: shuffle the factor labels of the Sharpe estimates within the bootstrap to obtain a noise-only share distribution).

*What's missing:* a pre-specified benchmark for "noise-only" share — added above (label-permutation null).

**Stress tests**
| Test | Result |
|---|---|
| Remove strongest source — does argument hold? | Yes (design does not rely on a single reference) |
| Flip the research question — is opposing view credible? | Yes ("views matter more than the anchor" is testable and could be supported) |
| Apply to different context — does finding generalize? | Unknown — that is sub-question 3 |
| "So what?" — is significance justified? | Yes: tells practitioners which ingredient to spend effort on |

`[DA-DECISION: Score n/a | ACTION: no rebuttal received | REASON: findings incorporated into design]`

## Checkpoint disposition (zero-question mode)
Checkpoint 1 is a design checkpoint, not an integrity gate. Per the user's standing no-ask order the revised design proceeds; the Major issues are binding design requirements recorded in `decisions.md` (A2).
