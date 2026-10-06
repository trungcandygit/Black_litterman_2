# Revision round 5 (reviewer comments of 2026-10-06), MSJ version.
# Each entry replaces a whole paragraph that starts with the given prefix. Numbers stay as inline R calls.
# Skill references: academic-paper/references/intro_title_rhetoric_guide.md (no universal negatives),
# abstract_writing_guide.md (few key numbers), academic_writing_style.md and writing_quality_check.md
# (one result per sentence where possible, no dense multi-result sentences).

PARAS = {}

PARAS["[[ABSTRACT]]"] = (
"[[ABSTRACT]] Daily price limits are meant to cool markets, but they may also delay price discovery. "
"We examine what happens after a stock closes at its daily limit on the Ho Chi Minh Stock Exchange, a market dominated by individual investors "
"that applies one 7% band and sets opening and closing prices by call auction. Using daily prices for `r nstocks` stocks from August 2024 to September 2026, "
"we split the next-day abnormal return after limit closes into an overnight gap and an intraday return. We compare limit closes with stocks that rose or fell almost as far, "
"and we test the limit effect together with a broad set of price- and volume-based characteristics under false discovery rate control. "
"The limit tests survive this control, whereas none of the lower-powered characteristic tests does. "
"After a ceiling close, the stock opens on average `r f(c16(\"Ceiling all\",\"gap_mkt\"),1)`% above the market, and the following session gives back about "
"`r f(100 * abs(c16(\"Ceiling all\",\"intraday_mkt\")) / c16(\"Ceiling all\",\"gap_mkt\"), 0)`% of this gap. "
"The gap is `r f(c17(\"ceiling vs 5-6.5% up\",\"gap_mkt\",\"diff_pct\"),1)` percentage points larger than after rises that stop short of the limit, "
"and the difference remains when those stocks also closed at their daily high. "
"An investor who buys at the next opening cannot capture the effect and loses `r f(abs(c11(\"Ceiling: rule-based\",\"f5o_mkt\")),1)`% against the market by the fifth close. "
"Floor closes are followed by a negative gap whose size depends on the benchmark. The ceiling gap appears in every calendar quarter and before the exchange changed its trading platform in 2025. "
"The pattern is consistent with delayed price discovery, but news, investor attention, and auction overshooting may also contribute, and data on news and order books are needed to separate them. "
"For market design, the results suggest that the opening auction absorbs much of the price adjustment that the 7% band postpones.")

PARAS["Studies on band changes have documented"] = (
"Studies on band changes have documented effects on volatility, liquidity, and crash risk (Jia et al., 2024; Lien et al., 2019; Qi, 2023), "
"and account-level data have shown that large investors buy on the limit day and sell on the next (Chen et al., 2019). "
"For Vietnam, Le (2012) evaluated how narrower bands after 2008 affected stock price risk, and Farber et al. (2006) documented clusters and sequences of limit hits in the early years of the market. "
"Huang et al. (2001) reported for Taiwan that the overnight overreaction after limit hits reverses on the following day. "
"Less is known about three questions. How large are the overnight gap and the intraday reversal after a limit close relative to a benchmark? "
"Does the limit effect remain once the many other price-based signals that a researcher could test are taken into account? "
"How does the pattern behave around the 2025 move of the HOSE to a new trading platform?")

PARAS["*Multiple testing and weekly regressions.*"] = (
"*Multiple testing and weekly regressions.* Harvey et al. (2016) argued that a new factor needs a *t*-statistic above 3.0, and Harvey and Liu (2020) tied the hurdle to a chosen FDR. "
"Chordia et al. (2020) put multiple-testing thresholds for cross-sectional regressions near 3.4, and Hou et al. (2020) found that with microcaps mitigated, 65% of 452 anomalies fail the single-test hurdle of 1.96. "
"Petersen (2009) compared standard-error estimators for panel data, which motivates our alternative clusters, and Gutierrez and Kelley (2008) studied weekly returns, the frequency of our regressions. "
"For Vietnam, Huang et al. (2023) found a size effect and an earnings-to-price effect.")

PARAS["*Gap and hypotheses.*"] = (
"*Gap and hypotheses.* These studies compared band regimes, sorted stocks by limit exposure, or split overnight and intraday returns for all stocks. "
"Huang et al. (2001) linked limit hits to the overnight-intraday timing in Taiwan. "
"The present study measures this split against benchmarks on the HOSE, places the limit tests in a family that controls for multiple testing, and uses the 2025 platform change. "
"If a limit delays price discovery, a ceiling close predicts a positive next-day abnormal return, and a floor close predicts a negative one (H~1~). "
"If the opening auction absorbs blocked demand, the effect concentrates in the overnight gap (H~2~). "
"If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of a similar size that stop short of the limit (H~3~). "
"If the gap already contains the blocked demand, an investor who buys at the next open cannot earn the continuation; the abnormal return from the next open to the fifth close is then zero or negative (H~4~). "
"A limit effect that survives the screen applied to all 22 characteristics is more credible than a single large estimate.")

PARAS["After a floor close, the gap is"] = (
"After a floor close, the gap is `r f(c16(\"Floor all\",\"gap_mkt\"),2)`% (*t* = `r f(c16(\"Floor all\",\"gap_mkt\",\"t_twoway\"),1)`). "
"The intraday return is a weak reversal of `r f(c16(\"Floor all\",\"intraday_mkt\"),2)`%.\n\n"
"The ceiling gap holds for exact limit hits (`r f(c11(\"Ceiling: exact tick-rule hit\",\"gap_mkt\"),2)`%) and for the first day of a streak of exact hits (`r f(c11(\"Ceiling: first day of streak (exact)\",\"gap_mkt\"),2)`%). "
"Near hits show a smaller gap (`r f(c11(\"Ceiling: near-hit (rule-based, not exact)\",\"gap_mkt\"),2)`%) and no significant intraday return. "
"However, their median day-*d* return is `r f(c27(8),2)`%, almost the same as the `r f(c27(7),2)`% of exact hits, and `r f(c27(9),0)`% of their closes are not multiples of the tick size. "
"This points to later price adjustment by the vendor rather than to closes below the limit. "
"The split is therefore weighted toward higher-priced stocks, where the tick is coarser, and we do not read the difference as a gradient toward the limit.\n\n"
"The ceiling gap appears in both halves of the sample and on days locked at one price from open to close. "
"It also appears in each tercile of the 60-day average dollar volume; in the most liquid tercile it is `r f(c16(\"Ceiling liquidity tercile 3\",\"gap_mkt\"),2)`%. "
"Against same-date controls, the ceiling gap is `r f(c11(\"Ceiling: rule-based\",\"gap_ctrl\"),2)`%.\n\n"
"The floor effect is less robust. Against same-date controls, the floor close-to-close return is `r f(c16(\"Floor all\",\"cc1_ctrl\"),2)`%, so its size depends on the benchmark. "
"Floor events also cluster on market-wide down days: excluding days on which the market fell by more than 2% removes "
"`r fi(c16(\"Floor all\",\"gap_mkt\",\"n\") - c16(\"Floor excluding market-crash days (market < -2%)\",\"gap_mkt\",\"n\"))` of the `r fi(c16(\"Floor all\",\"gap_mkt\",\"n\"))` floor events. "
"The floor gap is also not significant in the least liquid tercile (*t* = `r f(c16(\"Floor liquidity tercile 1\",\"gap_mkt\",\"t_twoway\"),1)`).")

PARAS["Table 3 quantifies the break."] = (
"Table 3 quantifies the break. Ceiling closers have a gap `r f(c17(\"ceiling vs 5-6.5% up\",\"gap_mkt\",\"diff_pct\"),2)` percentage points larger than stocks that rose 5% to 6.5% "
"(*t* = `r f(c17(\"ceiling vs 5-6.5% up\",\"gap_mkt\",\"t_cluster\"),1)`). Their intraday return is `r f(abs(c17(\"ceiling vs 5-6.5% up\",\"intraday_mkt\",\"diff_pct\")),2)` points lower. "
"Floor closers have a gap `r f(abs(c17(\"floor vs 5-6.5% down\",\"gap_mkt\",\"diff_pct\")),2)` points lower than stocks that fell 5% to 6.5% (*t* = `r f(c17(\"floor vs 5-6.5% down\",\"gap_mkt\",\"t_cluster\"),1)`).\n\n"
"Because the event rule requires a close at the day's high (low), we repeat the comparison with stocks that also closed at their high (low). "
"The ceiling gap is then `r f(c23(\"ceiling vs 5-6.5% up, close = high\",\"gap_mkt\",\"diff_pct\"),2)` points larger (*t* = `r f(c23(\"ceiling vs 5-6.5% up, close = high\",\"gap_mkt\",\"t_cluster\"),1)`), "
"and the floor gap is `r f(abs(c23(\"floor vs 5-6.5% down, close = low\",\"gap_mkt\",\"diff_pct\")),2)` points lower. A strong close therefore does not explain the contrast, which supports H~3~. "
"The comparison is an association around a rule-based threshold, and we make no regression-discontinuity claim. "
"The design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.")

PARAS["The ceiling gap, followed by an intraday reversal, appears in both periods"] = (
"The ceiling gap, followed by an intraday reversal, appears in both periods: `r f(c22(\"Ceiling\",\"gap_mkt\",\"pre_mean\"),2)`% before and `r f(c22(\"Ceiling\",\"gap_mkt\",\"post_mean\"),2)`% after "
"(difference *t* = `r f(c22(\"Ceiling\",\"gap_mkt\",\"diff_t\"),1)`). "
"The floor gap is more negative after the move, at `r f(c22(\"Floor\",\"gap_mkt\",\"pre_mean\"),2)`% before and `r f(c22(\"Floor\",\"gap_mkt\",\"post_mean\"),2)`% after (difference *t* = `r f(c22(\"Floor\",\"gap_mkt\",\"diff_t\"),1)`). "
"After the move, the intraday return after floor closes turns positive (`r f(c22(\"Floor\",\"intraday_mkt\",\"post_mean\"),2)`%). "
"The floor drift from the next open to day *d*+5 exists only before the move (`r f(c22(\"Floor\",\"f5o_mkt\",\"pre_mean\"),2)`% before and `r f(c22(\"Floor\",\"f5o_mkt\",\"post_mean\"),2)`% after).\n\n"
"The change coincides with a different market period. The post-change sample accounts for "
"`r f(100*c22(\"Ceiling\",\"gap_mkt\",\"post_n\")/(c22(\"Ceiling\",\"gap_mkt\",\"pre_n\")+c22(\"Ceiling\",\"gap_mkt\",\"post_n\")),0)`% of the ceiling events and "
"`r f(100*c22(\"Floor\",\"gap_mkt\",\"post_n\")/(c22(\"Floor\",\"gap_mkt\",\"pre_n\")+c22(\"Floor\",\"gap_mkt\",\"post_n\")),0)`% of the floor events. "
"Before the change, neither the ceiling close-to-close return (*t* = `r f(c22(\"Ceiling\",\"cc1_mkt\",\"pre_t\"),1)`) nor the floor gap (*t* = `r f(c22(\"Floor\",\"gap_mkt\",\"pre_t\"),1)`) is significant at the 5% level. "
"The full-sample significance of these two measures therefore rests mainly on post-change events. We cannot attribute the differences between the periods to the auction rules.")

PARAS["Because the events are unbalanced in time"] = (
"Because the events are unbalanced in time, Table 5 reports them by calendar quarter. "
"The ceiling gap is positive and significant in each of the `r nw(nrow(C29))` quarters (*t* from `r f(min(C29$ceiling_gap_t),1)` to `r f(max(C29$ceiling_gap_t),1)`). "
"The floor gap is negative in every quarter and significant at the 5% level in `r nw(sum(abs(C29$floor_gap_t) > 1.96))` of them.\n\n"
"We also move the break date to the first trading day of each month from January 2025 to April 2026. "
"These placebo dates give ceiling-gap differences between `r f(min(pl$ceiling_gap_diff),2)` and `r f(max(pl$ceiling_gap_diff),2)` percentage points, all with |*t*| of at most `r f(max(abs(pl$ceiling_gap_diff_t)),1)`. "
"The split at May 5, 2025, gives the largest difference, `r f(C30$ceiling_gap_diff[C30$krx],2)` points, but it is not significant either (*t* = `r f(C30$ceiling_gap_diff_t[C30$krx],1)`). "
"For floors, the difference is positive at the `r nw(sum(pl$floor_gap_diff > 0 & pl$break_date < \"2025-05-05\"))` placebo dates before the platform change "
"and negative at `r sum(pl$floor_gap_diff < 0 & pl$break_date > \"2025-05-05\")` of the `r sum(pl$break_date > \"2025-05-05\")` later ones. "
"The split at May 5, 2025, gives `r f(C30$floor_gap_diff[C30$krx],2)` points (*t* = `r f(C30$floor_gap_diff_t[C30$krx],1)`), close to the placebo dates that follow it. "
"Table 5 shows no trend in the floor gap, but the floor gap is weak in 2025-Q2 (`r f(C29$floor_gap_pct[C29$quarter == \"2025-Q2\"],2)`%), the quarter with the most floor events (`r fi(C29$floor_n[C29$quarter == \"2025-Q2\"])`). "
"The placebo dates therefore cannot separate a break at the platform change from a shift specific to that quarter.\n\n"
"A difference-in-differences regression compares limit closes with 5–6.5% movers that also closed at the extreme (repository table C31). "
"For ceilings, the excess gap was `r f(c31(\"ceiling vs 5-6.5% up at high\",\"gap_mkt\",\"limit_minus_control_pre_pct\"),2)` percentage points before the change (*t* = `r f(c31(\"ceiling vs 5-6.5% up at high\",\"gap_mkt\",\"t_pre\"),1)`) "
"and changed by `r f(c31(\"ceiling vs 5-6.5% up at high\",\"gap_mkt\",\"change_after_krx_pct\"),2)` points after it (*t* = `r f(c31(\"ceiling vs 5-6.5% up at high\",\"gap_mkt\",\"t_change\"),1)`). "
"For floors, the excess gap was `r f(c31(\"floor vs 5-6.5% down at low\",\"gap_mkt\",\"limit_minus_control_pre_pct\"),2)` points before (*t* = `r f(c31(\"floor vs 5-6.5% down at low\",\"gap_mkt\",\"t_pre\"),1)`) "
"and changed by `r f(c31(\"floor vs 5-6.5% down at low\",\"gap_mkt\",\"change_after_krx_pct\"),2)` points (*t* = `r f(c31(\"floor vs 5-6.5% down at low\",\"gap_mkt\",\"t_change\"),1)`). "
"The break at the limit is therefore present before the change and does not depend on the post-change period, although the significance of the raw ceiling close-to-close return and of the raw floor gap does (Table 4). "
"As with the split in Table 4, these comparisons describe timing and do not identify an effect of the auction rules.")

PARAS["None of the studies identified by our search"] = (
"The earlier studies measure different outcomes and horizons, so Table 6 compares signs, timing, and mechanisms rather than magnitudes.")

PARAS["(i) The sample covers"] = None   # handled below: escape the list marker so (i) is kept

# extra sentence: why the family p-values and Table 1 use different conventions
INFERENCE_OLD = "and use a *t* reference with $G-1$ degrees of freedom."
INFERENCE_NEW = ("and use a *t* reference with $G-1$ degrees of freedom. "
 "The family *p*-values keep the convention of the first computation of the planned tests; the analysis plan specified date-clustered standard errors but not the reference distribution, "
 "and we did not change the convention after seeing the results, so that the multiplicity control is not tuned to them. Table 1 adds the small-sample factor and the *t* reference as a more conservative check. "
 "Under these settings, the four event tests still survive a Bonferroni correction in families of up to `r fi(c21(5))` tests with date clusters and `r fi(c21(6))` with calendar-week clusters (Section 3), so the choice does not change any conclusion.")


# ---- round 5b: full texts of Kim and Rhee (1997), Huang et al. (2001), and Qi (2023) read (PDFs supplied by the authors) ----
# Kim & Rhee (1997) Table IV/text: overnight continuation 65% (upper) vs 50% for stocks reaching 90% of the limit; 49% vs 32% (lower); TSE First Section 1989-1992.
# Huang et al. (2001) Table 4/5, Section 6.2-6.3: 1-day up-limit closes AR1,co 1.18%, AR1,oc -0.77% (ratio -0.65); down-limit -2.17% and +1.24%; up near-limit (>5%) +0.23% and -0.72%; TSE 1990-1996, 7% band, call auctions at open and close.
# Qi (2023) Table 2: day-1 AR after upper-limit closes +0.24% (N = 1537), after lower-limit closes -3.37% (N = 1042), before the 2020 widening; market-model close-to-close returns.
LIT_EDITS = [
 ("Huang et al. (2001) reported for Taiwan that the overnight overreaction after limit hits reverses on the following day.",
  "In Taiwan, which also had a 7% band, Huang et al. (2001) found that one-day up-limit closes gained 1.18% overnight and gave back 0.77% in the next session."),
 ("Our decomposition adds timing to the evidence of Kim and Rhee (1997):",
  "Our ceiling gap is larger than the 1.18% that Huang et al. (2001) reported for Taiwan, and the following session reverses a smaller share of it (about `r f(100 * abs(c16(\"Ceiling all\",\"intraday_mkt\")) / c16(\"Ceiling all\",\"gap_mkt\"), 0)`% against about two thirds). Our decomposition also adds timing to the evidence of Kim and Rhee (1997):"),
 ('"Kim and Rhee (1997)", "Berkman and Lee (2002)", "Huang et al. (2001)"', '"Kim and Rhee (1997)", "Berkman and Lee (2002)", "Huang et al. (2001)"'),
 ('"Volatility spillover, delayed price discovery, and trading interference", ',
  '"Overnight continuation after limit hits in 65% (upper) and 49% (lower) of cases, against 50% and 32% for stocks reaching 90% of the limit; volatility spillover and trading interference", '),
 ('"Overnight overreaction after limit hits corrected the next day", ',
  '"One-day up-limit closes: +1.18% overnight, \\u22120.77% in the next session; near-limit rises: +0.23% and \\u22120.72%; down-limit closes: \\u22122.17% and +1.24%", '),
 ('"Delayed price discovery, spillover, and interference, stronger at the lower limit; no magnet effect", ',
  '"Day-1 abnormal return +0.24% after upper-limit closes and \\u22123.37% after lower-limit closes under the 10% band; spillover and interference, stronger at the lower limit; no magnet effect", '),
 ('"Ceiling next-day return consistent with delayed price discovery; spillover and interference not tested", ',
  '"Same direction: the overnight move is larger at the limit than near it; we measure its size, not its frequency; spillover and interference not tested", '),
 ('"Same timing: positive gap, partial intraday reversal", ',
  'paste0("Same timing; our ceiling gap (", f(c16("Ceiling all","gap_mkt"),2), "%) is larger, and the session reverses a smaller share (", f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0), "% against about two thirds)"), '),
 ('"Different outcome (market quality); here both limit closes carry a next-day return, the floor effect depending on the benchmark", ',
  'paste0("Opposite asymmetry: our day-", "*d*+1 return is ", f(ev("ceiling","t+1","mean_ar_pct"),2), "% after ceiling and ", f(ev("floor","t+1","mean_ar_pct"),2), "% after floor closes"), '),
 ("Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit.", "Liang and Hu (2025) forecast limit hits."),
 # length: shorter wording elsewhere to stay within 7,500 words
 ("The comparison is an association around a rule-based threshold, and we make no regression-discontinuity claim. The design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.",
  "The comparison is an association around a rule-based threshold, not a regression-discontinuity design, and stocks that reach the limit may differ in news content."),
]
TABLE6_NOTE_NEW = "*Note.* Entries for Kim and Rhee (1997), Huang et al. (2001), and Qi (2023) report results from the full texts; the other entries summarize each study's abstract."


LIT_EDITS += [
 ("a pattern that Huang et al. (2001) describe qualitatively for Taiwan,", "a split that Huang et al. (2001) applied to Taiwan,"),
 ("gained 1.18% overnight and gave back 0.77% in the next session.", "gained 1.18% overnight in abnormal terms and gave back 0.77% in the next session."),
 (" Limit closes cluster in market episodes, so our standard errors allow dependence across dates, weeks, 10-day blocks, and stocks.", ""),
 ('"Tokyo; limit hits", "Korea; limit revision", "Taiwan; limit hits"', '"Tokyo, 1989\\u20131992; limit hits", "Korea; limit revision", "Taiwan, 1990\\u20131996; 7% band"'),
 ('"ChiNext; band 10% to 20%"', '"ChiNext, 2020\\u20132021; band 10% to 20%"'),
 ("As with the split in Table 4, these comparisons describe timing and do not identify an effect of the auction rules.", "These comparisons describe timing, not an effect of the auction rules."),
]

TABLE6_NOTE_OLD = "*Note.* Findings as reported in each source's abstract or in the records we could access."

NEW_REFS = [
 "Farber, A., Nguyen, V. N., & Vuong, Q. H. (2006). *Policy impacts on Vietnam stock market: A case of anomalies and disequilibria 2000–2006* (CEB Working Paper No. 06/005). Université Libre de Bruxelles. https://ideas.repec.org/p/sol/wpaper/06-005.html",
 "Le, D. N. (2012). Evaluating impacts of reduction in fluctuation limit on stock price risks in Vietnam. *Journal of Economic Development* (University of Economics Ho Chi Minh City), (214), 116–128. https://vjol.info.vn/ed/article/view/34298",
]

def apply(b):
    for prefix, new in PARAS.items():
        if new is None or prefix == "[[ABSTRACT]]": continue
        i = b.find(prefix); assert i >= 0 and b.count(prefix) == 1, prefix
        j = b.index("\n", i)
        b = b[:i] + new + b[j:]
    for o_, n_ in LIT_EDITS:
        assert b.count(o_) == 1, o_[:70]; b = b.replace(o_, n_)
    assert b.count(INFERENCE_OLD) == 1; b = b.replace(INFERENCE_OLD, INFERENCE_NEW)
    # length (journal limit 7,500 words): shorten two passages that repeat evidence given elsewhere
    old = ("For stocks priced at 10 thousand dong or more, `r f(c27(2),0)`%, `r f(c27(4),0)`%, and `r f(c27(6),0)`% of 2024, 2025, and 2026 closes are tick multiples, "
           "against `r f(c27(1),0)`% below 10 thousand dong (an uninformative check, since the 0.01 tick equals the two-decimal resolution of the files), and near hits make up")
    new = "For stocks priced at 10 thousand dong or more, only `r f(c27(2),0)`% to `r f(c27(6),0)`% of closes are tick multiples, and near hits make up"
    assert b.count(old) == 1; b = b.replace(old, new)
    i = b.index("With noise traders overnight"); j = b.index(".", b.index("operates without limits", i)) + 1
    b = b[:i].rstrip() + b[j:]
    assert b.count("(i) The sample covers") == 1
    b = b.replace("(i) The sample covers", "\\(i) The sample covers")
    return b
