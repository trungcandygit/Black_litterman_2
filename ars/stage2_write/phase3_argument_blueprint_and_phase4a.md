# Phase 3: Argument Blueprint (argument_builder)

Thesis: FTSE Russell eligibility, not final index inclusion, is associated with a persistent fall in stock illiquidity on HOSE; inclusion adds a one-session trading spike at rebalancing.

| # | Claim | Evidence (output file) | Reasoning / citation |
|---|---|---|---|
| C1 | Eligible constituents became less illiquid from the Oct 2025 announcement, and the gap widened at each disclosure stage. | table2_did.csv: -0.39, -0.88, -1.12 (all p<0.001); matched -0.39, -0.71, -0.98 | Recognition channel predicts gradual gains after information arrives (Hegde & McDermott, 2003; Chen et al., 2004) |
| C2 | The Amihud result is not a continuation of a pre-existing trend. | table_event_study_two_groups.csv (flat pre-period, break at month 0); robustness treated_trend: -0.37, -0.85, -1.08, trend -0.0006 n.s.; size x week FE -0.40, -0.75, -0.91 | Roth et al. (2023) on pre-trend diagnostics; Ho et al. (2007) on matching |
| C3 | Near-miss eligible stocks improved at least as much; the included vs near-miss gap is statistically zero. | table4_two_groups.csv: near -0.75, -1.25, -1.80; table4b p = 0.22, 0.46, 0.18 | Eligibility lists are public information; benchmark-driven attention (Raddatz et al., 2017) reaches all named stocks |
| C4 | Only included stocks show a rebalancing-session spike. | table_rebalance_reg.csv rel0 +0.80 (t=4.87), all 27 prior sessions n.s.; table5: near-miss +0.22 (SE 0.33) | Price-pressure channel (Harris & Gurel, 1986; Shleifer, 1986) operates through index-fund trades on the effective date |
| C5 | Trading value rose but partly continues a pre-existing trend; spreads did not narrow. | lval pre-trend p=0.0006; trend-adjusted +0.26, +0.38, +0.43; cs +0.09 to +0.13 pp | Corwin & Schultz (2012) spread also loads on volatility; interpret cautiously |
| Counter | Large caps may have gained liquidity for reasons unrelated to FTSE (2025 rally, retail inflows). | size x week FE; matched sample balance (SMD 0.07 on value); placebo Apr 2025 = 0.03 | Addressed, not eliminated: common shocks to the largest stocks remain possible; stated as limitation |

# Phase 4a: Writer paper-blind pre-commitment (contract writer_full)

## Acceptance Criteria Paraphrase

D1 section completeness: every outline section (1 to 6 plus declarations) exists in the draft, with no unresolved [MATERIAL GAP] markers at handoff.

D2 citation density: every factual statement about prior work cites a Stage 1 verified source; every empirical number cites a table, figure, or output file; no claim rests on hedging alone.

D3 argument blueprint fidelity: sections follow C1 to C5 and the counter-argument row; topic sentences state these claims; evidence comes from the assigned outputs.

D4 total word count: body within 7,000 plus or minus 10 percent (6,300 to 7,700), excluding tables, references and declarations.

D5 per-section word count: each section within plus or minus 15 percent of its Phase 2 allocation.

D6 paragraph structure: each body paragraph makes one point, supports it with a number or citation, explains it, and links to the thesis.

D7 register consistency: formal finance register, active voice, no em dashes, causal language only where the design supports it (Amihud under matched and trend-robust designs).

[PRE-COMMITMENT-ACKNOWLEDGED]
