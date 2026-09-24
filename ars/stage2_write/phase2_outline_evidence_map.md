# Phase 2: Paper Outline + Evidence Map (structure_architect)

Structure: IMRaD empirical article. Target about 7,000 words (excluding tables, references). Framing A (eligibility-attention), accepted at Phase 0.

**Working title**: Eligibility, not inclusion: stock liquidity around Vietnam's FTSE Russell reclassification

**Controlling idea (one sentence)**: When FTSE Russell reclassified Vietnam, stocks it named as eligible became more liquid from the announcement onward whether or not they entered the index, while final inclusion added only a one-day trading spike at rebalancing.

**Primary outcome**: log Amihud illiquidity on traded value (cleanest pre-period). Secondary: log trading value (pre-existing upward trend; trend-adjusted estimates reported). Tertiary: Corwin-Schultz spread (moves the opposite way; reported, interpreted cautiously).

| § | Section | Words | Key claim (evidence-bound) | Evidence (file) |
|---|---|---|---|---|
| 1 | Introduction | 1,000 | Eligible stocks' Amihud illiquidity falls 32% relative to other HOSE stocks after the Oct 2025 announcement and about 67% by the constituent list; near-miss eligible stocks move as much; only constituents spike at rebalancing. | table2_did.csv; table4_two_groups.csv; table5_rebalance_by_group.csv |
| 2 | Institutional setting and literature | 1,300 | Timeline (4 dates, phased inclusion); index-inclusion liquidity evidence strong in developed markets, weak in frontier markets; two channels (recognition vs price pressure) give testable timing predictions; hypotheses H1 to H3. | Stage 1 brief; bibliography_verified.md |
| 3 | Data and empirical design | 1,300 | 405 HOSE stocks downloaded, 366 pass filters (24 constituents, 5 near-miss, 337 others), 99 weeks, 35,752 stock-weeks; Amihud on VND value; DiD with stock and week FE; matched 3:1 sample; event study. | run_summary.txt; table1b_descriptives_by_group.csv |
| 4.1 | Results: eligibility lowers illiquidity from the announcement | 900 | Constituents: -0.39, -0.88, -1.12 by stage; matched sample -0.39, -0.71, -0.98. | table2_did.csv; Figure 1 |
| 4.2 | Results: near-miss stocks improve as much | 700 | Near-miss: -0.75, -1.25, -1.80; included minus near-miss not different from zero (p 0.18 to 0.46). | table4_two_groups.csv; table4b; Figure 2 |
| 4.3 | Results: inclusion adds a rebalancing-day spike | 500 | 18 Sep 2026: constituents +0.76 log points abnormal value; near-miss +0.22 (SE 0.33); matched controls -0.20. | table5_rebalance_by_group.csv; table_rebalance_reg.csv |
| 5 | Robustness and threats | 900 | Pre-trend test (Amihud p=0.037, value p=0.0006), event-study break at month 0; size x week FE; treated-specific trend (Amihud survives; value shrinks to +0.26 to +0.43); two-way clustering; dropping Vingroup family; placebo Apr 2025 = 0.03; spreads rise (+0.09 to +0.13 pp). | table3_robustness.csv; table_pretrend_wald.csv; table_event_study_two_groups.csv |
| 6 | Discussion and conclusion | 500 | Recognition channel fits the evidence; index-fund demand concentrates in one session; implications for regulators and issuers; limitations (5 near-miss stocks, 3 post-effective days, no foreign-flow data, eligibility list defined ex post). | all above |
| - | Declarations | 150 | Data availability, AI use, CRediT (authors to supply), funding, conflicts | Phase 0 |

## Tables and figures plan

- Table 1: Sample and pre-period descriptives by group.
- Table 2: Baseline DiD, all HOSE and matched (3 outcomes).
- Table 3: Two treated groups (included, near-miss) and their difference.
- Table 4: Rebalancing window, abnormal trading value by group.
- Table 5: Robustness matrix.
- Figure 1: Event study, constituents vs near-miss (log Amihud, log trading value) with stage lines.
- Figure 2 (optional): Timeline of FTSE decisions (non-data schematic).

## Devil's Advocate MAJOR conditions (carried from Stage 1): closure plan

| Condition | Where closed | How |
|---|---|---|
| Size-related pre-trends | §3, §5 | Amihud as primary outcome (flat pre-period, break at month 0); report joint pre-trend test honestly; size x week FE; treated-specific trend; value outcome labelled secondary with trend-adjusted estimate in text |
| Selection on eligibility | §3, §4.2 | Framing A turns the selection into the object of study: eligibility is the treatment; near-miss group separates eligibility from inclusion; stock FE absorb level differences |

## Language rules for this draft
- Causal verbs only for the Amihud result under matched and trend-robust designs; "is associated with" for trading value.
- No em dashes; claim-first headings; every number traced to an output file.
