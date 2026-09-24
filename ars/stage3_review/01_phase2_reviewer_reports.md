# Stage 3 REVIEW, Phase 2 reports (paper-visible), five seats

Manuscript: manuscript_v2.md, SHA-256 1adeb804...63c. Read-only. Provenance: review_panel_provenance.json (role-separated; same context, same model family, peer outputs visible; correlated-error disclosure required).
Anchor types: [S x.y] = manuscript section; [T n] = table; [F1] = Figure 1; [EXT] = external public source checked during review.

---

## EIC: Journal-Fit Reviewer (D5, D6)

**Recommendation signal:** Major Revision. **Confidence:** 4/5.

**Summary.** The paper asks which stocks gained, and when, from Vietnam's FTSE Russell upgrade, and answers with a stage-by-stage decomposition: liquidity and prices move at disclosures, and the effective date produces only a rebalancing volume spike. The question is timely, the setting is clean in its dating, and the writing is unusually direct. Fit with a broad open-access empirical finance venue is good. Its value to readers rests on whether the constituent effects are effects of the upgrade and not of FTSE's choice of stocks, which the methodology and devil's-advocate seats probe.

**Strengths**
- S1 Clear, dated four-step setting with verified sources [S 2.1]; readers can reuse the timeline.
- S2 Results presented claim-first with magnitudes and takeaways; tables are self-contained [T2-T8].
- S3 Candid reporting of unfavourable checks (matched trend, trading-value pre-trend, rising spreads, near-miss selection) [S 5].

**Weaknesses**
- W1 (D6, warn) Contribution hinges on identification that is still open. The stage decomposition is the paper's one idea [S 1, para 6]; if selection explains the stage pattern, the contribution reduces to a descriptive account. Remedy: the identification repairs in R1/DA.
- W2 (D5, minor) Section 5.2 near-miss analysis and Section 4 tables use two different group definitions of "eligible" without a table that lists every stock named on each public list. Remedy: an appendix table of names by list (Nov 2025, Apr 2026, Aug 2026) and sample status.
- W3 (D5, minor) Abstract is 183 words; check the venue limit and drop the fourth-to-last sentence if needed.

Scores: D5 pass; D6 warn.

---

## R1: Methodology Reviewer (D1, D3)

**Recommendation signal:** Major Revision. **Confidence:** 5/5.

**Summary.** The difference-in-differences and event-study machinery is standard and competently run, with stock and week fixed effects, clustering, randomization inference and a matched sample. Two inferential problems affect headline claims directly, and the treatment definition uses information from the treatment period.

**Strengths**
- S1 Randomization inference against the top tercile of control stocks addresses few-treated-cluster inference credibly [T7].
- S2 Transparent window assignment rules and code-matched method description [S 3.3].

**Weaknesses**
- W1 (D1, block) Treatment defined with post-treatment information. The 24 treated stocks are the August 2026 constituents [S 3.1]. FTSE selected them in 2026 on screens applied to data from the treatment period (the April 2026 list uses data as of 31 December 2025 [EXT: The Investor, 8 Apr 2026]). A stock whose liquidity improved after October 2025 was more likely to enter the treated group, which biases the P1 and P2 coefficients away from zero and can by itself generate the monotone stage pattern (H2). Stock fixed effects and a linear treated trend do not remove selection on post-treatment shocks. Remedy (feasible with the current data): an intention-to-treat design whose treatment is the preliminary list of 28 stocks FTSE screened on data as of 31 December 2024, before the announcement [EXT: The Investor, 4 Mar 2026; Viet Nam News, 13 Nov 2025]; report ITT alongside the constituent estimates, and a "predicted constituent" group built from pre-period size and liquidity ranks.
- W2 (D1, block) CAR inference ignores event-date clustering. All 24 constituents share each event date, so the cross-sectional t-statistics in Table 3 treat correlated abnormal returns as independent and overstate precision (the classic clustered-event problem). Remedy: a portfolio (calendar-time) test using the time-series standard deviation of the constituent-minus-benchmark portfolio in a pre-event estimation window, or the Kolari-Pynnönen adjusted statistic; report both.
- W3 (D1, block) CAR benchmark mismatched to large caps. The benchmark is the equal-weighted mean of 337 control stocks [S 3.2], dominated by small caps. A disclosure-day rally concentrated in large caps would appear as constituent abnormal return. Remedy: benchmark on matched controls, a size-tercile benchmark, or a market model with pre-estimated betas; show Table 3 under each.
- W4 (D1, warn) Pre-period window sensitivity. The monthly Amihud coefficients at months -3 and -2 are positive (0.33 and 0.22, both p < 0.01) [T event study; F1], so the pooled pre-period mean is lifted by a temporary deterioration just before the announcement. The P1 estimate partly reflects reversion. Remedy: re-estimate excluding July to August 2025, or report P1 relative to a pre-period that ends in June 2025.
- W5 (D1, warn) Few treated clusters. Complement stock-clustered standard errors with a wild cluster bootstrap for the DiD coefficients, including the segment regressions with three treated stocks per segment [T5], which cannot support conventional clustered inference.
- W6 (D3, warn) H2 ("strengthens with resolution") is observationally equivalent to gradual growth or selection; the event study shows a steady drift more than steps at disclosure months [F1]. Remedy: test for level shifts at the confirmation and list months against a trend, or soften H2.

Scores: D1 block (not fatal: repairable with available data); D3 warn.

---

## R2: Domain Reviewer (D2)

**Recommendation signal:** Major Revision. **Confidence:** 4/5.

**Summary.** The paper describes FTSE's process accurately after integrity corrections and positions itself against index-effect and reclassification studies. One assignment problem affects estimates.

**Strengths**
- S1 Accurate reclassification timeline with primary FTSE documents [S 2.1].
- S2 Correct characterisation of the recognition and price-pressure channels [S 2.2].

**Weaknesses**
- W1 (D2, block) Control group contains named-eligible stocks. The public preliminary list of 28 names includes KBC, KDH, FRT, DGC, EIB, DPM, PDR, DIG and KDC, all HOSE-listed and absent from the constituents [EXT: The Investor, 4 Mar 2026]. The manuscript's near-miss group contains only SAB, DXG, PLX, GEE and BSR [S 3.1], so at least nine named-eligible stocks sit in the control group. If eligibility itself attracted trading, this biases the constituent estimates toward zero; if these stocks lost liquidity after exclusion, it biases them away from zero. It also makes the near-miss test in Section 5.2 incomplete. Remedy: rebuild groups from the full public lists (Nov 2025 list of 28, Apr 2026 list of 32, Aug 2026 constituents), re-run Tables 2, 7 and 8 with named-but-excluded stocks removed from controls, and extend the naming-timing test to all of them.
- W2 (D2, warn) FTSE's screening cut-off dates are not used. The Nov 2025 list used data as of 31 Dec 2024 and the Apr 2026 list data as of 31 Dec 2025 [EXT]. These dates turn the "selection follows liquidity" discussion [S 5.2] into a testable statement: GEE and BSR improved in October to December 2025, inside the window FTSE screened for the April list. Remedy: state the cut-off dates and frame Section 5.2 around them.
- W3 (D2, warn) Institutional detail on foreign ownership limits and free float is absent. FTSE's investability weights depend on free float and foreign headroom; readers need this to interpret segment results. Remedy: one paragraph in Section 2.1 from FTSE's documents.
- W4 (D2, minor) The literature on MSCI's inclusion of China A-shares has stock-level liquidity studies beyond Dong et al. (2023); a short, verified addition would strengthen Section 2.3. Any added reference must pass integrity verification.

Scores: D2 block (repairable).

---

## R3: Perspective Reviewer (D4)

**Recommendation signal:** Minor Revision. **Confidence:** 3/5.

**Summary.** The paper speaks to regulators and issuers, and the policy message (credible, early communication brings the gains forward) is appealing. Some implications outrun the evidence.

**Strengths**
- S1 Accessible framing for non-specialists; hypotheses stated in plain terms [S 2.4].

**Weaknesses**
- W1 (D4, warn) The effective date carried only the first tranche, 10% of the applicable weight; 90% arrives in March, June and September 2027 [S 2.1]. "The effective date added nothing" and "index funds ... found prices already adjusted" [Abstract; S 4.3; S 6] should be scoped to the first tranche. Remedy: rephrase and add the tranche caveat where the claim is made.
- W2 (D4, warn) Cost-of-capital implications for issuers [S 1; S 6] are inferred, not measured. Remedy: present as a motivation citing Bekaert et al. (2007), not as a finding.
- W3 (D4, minor) The recognition-channel reading lacks investor-type evidence; foreign net buying data (published by the exchange) would test it directly. Remedy: acknowledge in the limitations or add if obtainable.

Scores: D4 warn.

---

## DA: Devil's Advocate (D3)

### Strongest counter-argument
The paper's treated group is a list FTSE drew up in August 2026 of stocks that were, by then, large and liquid enough to pass its screens. Any stock whose trading grew between October 2025 and mid-2026 for any reason (a sector rally, a retail inflow into banks and brokers, a corporate event) had a higher chance of making the list. Compare such a group with the rest of the market and illiquidity "falls" from the announcement onwards and "deepens" towards the list date, without any causal role for the upgrade. The two stocks that the paper itself shows were chosen after their liquidity rose (GEE and BSR) are a direct example of this mechanism. The price evidence does not rescue the thesis yet: the abnormal returns are measured against a small-cap benchmark with t-statistics that ignore common event dates, so large-cap market days would pass as FTSE effects. The flat pre-trend is not reassuring either, because selection acts after October 2025, not before. And the effective-date null concerns a 10% tranche. What remains robust is the rebalancing-day volume spike, which follows mechanically from index demand.

### Issue list
- DA-C1 CRITICAL (D3): selection of the treated group on post-announcement outcomes can reproduce the central stage pattern [S 3.1, S 3.4 fourth assumption, S 5.2]. Not fatal: an ITT group screened on pre-announcement data exists publicly.
- DA-M1 MAJOR (D3): price-at-disclosure claim (H3) rests on inference that ignores event clustering and on a size-mismatched benchmark [T3].
- DA-M2 MAJOR (D3): "effective date added nothing" overgeneralises from the 10% first tranche [Abstract, S 6].
- DA-m1 MINOR (D3): "Classification events redistribute liquidity" [S 6] generalises from one event.

### Ignored alternatives
Sector composition (banks and brokers dominate constituents; brokers' liquidity co-moves with market turnover); the mid-2025 market rally; the removal of pre-funding for foreign investors, which LSEG credits for the upgrade [EXT: LSEG 2026] and which could raise foreign trading in large caps irrespective of index membership.

### Observations (non-defects)
Unfavourable results are reported rather than hidden; the reframing away from the earlier "eligibility, not inclusion" thesis after contrary evidence counts against frame-lock.

Scores: D3 block (via DA-C1; not fatal).
