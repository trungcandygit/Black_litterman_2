# Paper Configuration Record (academic-paper full, Phase 0)

Run: ftse2-20260924-01 | Stage 2 WRITE | Status: AWAITING USER CONFIRMATION (IRON RULE)

| Item | Setting | Source |
|---|---|---|
| Paper type | Empirical research article, IMRaD | design (Stage 1) |
| Discipline | Finance: market microstructure / international finance | Stage 1 |
| Target journal | Finance Research Open (Elsevier, ISSN 3050-7006), gold OA, APC waived for submissions to 31 Dec 2026 | user shortlist, intake decision |
| Citation format | APA 7 author-date (Elsevier "Your Paper Your Way" accepts any consistent style at first submission) | default; confirm |
| Output format | Markdown master, DOCX via Pandoc, LaTeX (elsarticle) + PDF at Stage 5 | default |
| Language | English body | venue |
| Abstract | English only (venue does not need a second language); ARS default pair zh-TW+EN overridden | proposed; confirm |
| Keywords | 5 to 6, not repeating the title | venue norm |
| Word count target | about 6,500 to 7,500 words excluding tables and references (FRO guide page not retrievable, HTTP 403; target set to typical Elsevier finance article length) | proposed; confirm |
| Existing materials | Stage 1 brief, blueprint, 18 verified references; R code and output (366 stocks, 99 weeks); draft-0 sections | handoff |
| Co-authors / CRediT | To be supplied by authors (prior-paper team: Nguyen Van Trung and co-authors) | OPEN |
| Funding | "This research did not receive any specific grant" unless authors state otherwise | OPEN |
| Data availability | Public exchange data via vnstock; code and data on request or repository | proposed |
| AI-use statement | Required (generic ARS statement) | IRON RULE |
| Citation-verification level | strict (every reference Crossref-verified; already applied in Stage 1) | recommended |
| Style calibration | Not used | default |
| ReviewTargetContext (#683) | criteria_binding_unavailable (no official venue criteria retrieved) | explicit degraded path |

## Framing decision required before Phase 1-2 (evidence from full-sample run)

Full-sample estimates (output/run_summary.txt):
- Constituents vs all HOSE: log Amihud -0.39 (announcement), -0.88 (confirmation), -1.12 (list), all p < 0.001; log trading value +0.67, +1.03, +1.19.
- Matched 3:1 sample: -0.39, -0.71, -0.98 (all p < 0.01).
- Size-tercile x week FE and treated-specific linear trend: Amihud effects survive; trend coefficient -0.0006 (n.s.). Trading-value effects shrink to +0.26 to +0.43 once a treated-specific trend is allowed (trend +0.011 per week, p < 0.001).
- Pre-trend joint test: Amihud p = 0.037; trading value p = 0.0006; spread p = 0.15.
- Corwin-Schultz spread rises slightly (+0.09 to +0.13 percentage points), so spreads do not narrow.
- Rebalancing session 18 Sep 2026: constituents +0.76 log points abnormal trading value vs -0.20 for matched controls.
- Placebo date (Apr 2025): 0.03 (n.s.).
- **Near-miss stocks (on FTSE eligibility lists, not included; n = 5): liquidity improves even more (-0.75, -1.25, -1.80).**

Implication: the liquidity gain appears to follow FTSE *eligibility* news (both included and near-miss stocks), not final inclusion alone. Two framings:
- (A) "Eligibility-attention effect": the upgrade raised liquidity for all stocks FTSE named as eligible; final inclusion adds a rebalancing-day volume spike. Honest and consistent with all evidence; changes treatment definition to include near-miss stocks as a second treated group.
- (B) "Inclusion effect": keep constituents as the only treated group and report near-miss results as a limitation. Weaker, reviewers will flag it.

Recommendation: (A).
