# Decision memo: framing A fails the naming-timing test (Stage 2, revision round 2)

Status: PIPELINE PAUSED, pending author decision (ARS frame-lock guard; decision-bearing regression).
Date: 2026-09-24. Run: ftse2-20260924-01. Evidence: output/run_summary_extensions.txt, output/table10_naming_timing.csv, output/table10b_nearmiss_by_stock.csv, output/table8_car_events.csv, output/table9_volatility_spreads.csv (script code/analysis_extensions.R).

## What changed

Framing A ("eligibility, not inclusion") rested on the five near-miss stocks improving as much as constituents. The naming-timing test splits them by when press reports first named them as FTSE-eligible:

| Stock | First named | Change in log Amihud vs controls (relative to pre-Oct 2025) |
|---|---|---|
| SAB | Nov 2025 list | -0.22 (Oct to Nov 2025), -0.03 (Nov 2025 to Apr 2026), -0.10 (after Apr 2026) |
| DXG | Nov 2025 list | -0.13, -0.06, -0.31 |
| PLX | Nov 2025 list; dropped Apr 2026 | -0.63, -0.79, -1.03 |
| GEE | Apr 2026 list | -1.66, -1.72, -2.97 |
| BSR | Apr 2026 list | -0.39, -1.23, -1.81 |

Regression (lamihud, stock and week FE): late-named (GEE, BSR) -1.05 (p=0.02) before November and -1.51 (p<0.001) from November to April, i.e. before they were named; early-named (SAB, DXG, PLX) -0.34, -0.31 (n.s.), -0.58.

Reading: the near-miss average is driven by GEE and BSR, whose liquidity rose before FTSE named them. This fits reverse selection (FTSE screens favour stocks whose size and liquidity were rising) better than an eligibility-announcement effect. Two of the three stocks named in November barely moved. The title claim "Eligibility, not inclusion" is not supported.

## What still holds (constituents)

- Amihud: -0.39, -0.88, -1.12; matched, size-by-week, trend, randomization inference all hold for the confirmation and list stages.
- Controlling for volatility strengthens the Amihud result: -0.57, -1.00, -1.20 (constituent volatility rose, so the unadjusted Amihud effect is conservative).
- Prices: constituents earn CAR +3.3% [-1,+1] at the announcement (t=6.4), +4.5% at confirmation (t=7.5), +2.6% at the constituent list (t=5.1); the announcement gain reverses over [0,+20] (-2.4%, n.s.), the confirmation gain persists (+10.0% over [0,+20], t=3.7); no effect around the effective date. Near-miss CARs are not significant.
- Rebalancing spike +0.80 (t=4.87), scaling with FTSE segment (large 1.23, mid 0.98, small 0.65).

## Options for the author

- (A') Keep near-miss evidence but downgrade it: title and thesis centre on constituents; near-miss results reported as inconclusive, with the naming-timing test shown openly. Working title: "Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification". Recommended.
- (B) Inclusion-effect framing: constituents are the treated group; near-miss and naming tests move to a robustness section as evidence that FTSE selection partly follows rising liquidity, which the paper then controls for (matched sample, trend).
- (C) Keep framing A and argue that eligibility screens themselves reward rising liquidity. Not recommended: the evidence contradicts the causal reading of A.

Whichever option: the new analyses (prices, volatility, naming timing) add roughly 1,500 to 2,000 words of substantive content toward the 7,000-word target the author kept (option b).

## Next steps once the author decides
1. Rewrite title, abstract, introduction and Section 4.2 under the chosen framing (Phase 4b round 2).
2. Insert drafted sections from `draft_round2_new_sections.md`.
3. Re-run mechanical gate, citation cross-check, writer/evaluator scoring.
4. Stage 2 checkpoint, then Stage 2.5 INTEGRITY (MANDATORY).
