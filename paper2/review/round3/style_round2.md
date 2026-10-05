# Style and proofreading review, round 2 (final): stop-slop + proofreading

**Paper:** "Closing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange"  
**Source:** `paper2/manuscript/manuscript_final.Rmd` (rendered text checked with `pandoc manuscript_final.docx -t plain --wrap=none`)  
**Date:** 2026-10-05  
**Mode:** report only. No source file was changed.

## How to use this report

- Each edit gives an exact **old** string from the current `.Rmd` and its **new** string. A script confirmed that every old string occurs exactly once in the file and still occurs exactly once when the edits are applied in the listed order (see the verification log at the end). Apply them in order within each section.
- No edit changes code logic or a computed number. Three edits only reuse inline `r ...` expressions already in the file: S3 (the Section 8 gap expressions), S4 (the abstract's `abs(...)` expression at one decimal), and X1 (`c26(4)`, the trading-day count used in Section 3).
- Edits marked **[verify]** depend on a fact the authors must confirm: I3, L4, and L8 depend on the content of Huang et al. (2001), and M16 depends on how the authors classify H2 to H4.
- A scratch copy with all edits applied knits without error. Its rendered text was read in full.
- Stop-slop scores use a 1 to 10 scale on each dimension. Below 35/50 means "revise".

---

## Scorecard

### Stop-slop (per section, after round-1 edits, before round-2 edits)

| Section | Directness | Rhythm | Trust | Authenticity | Density | Total /50 | Round 1 | Edits |
|---|---|---|---|---|---|---|---|---|
| Abstract | 8 | 7 | 8 | 7 | 8 | 38 | 35 | 2 |
| 1. Introduction | 8 | 7 | 8 | 7 | 8 | 38 | 36 | 4 |
| 2. Related literature and hypotheses | 8 | 7 | 8 | 7 | 7 | 37 | 34 | 8 |
| 3. Data and institutional setting | 8 | 7 | 8 | 8 | 8 | 39 | 37 | 2 |
| 4. Design | 8 | 6 | 8 | 7 | 6 | 35 | 35 | 16 |
| 5. Results (incl. Tables 1 to 4, Figures 1 and 2) | 8 | 6 | 8 | 7 | 7 | 36 | 30 | 18 |
| 6. Discussion (incl. Table 5) | 8 | 7 | 8 | 7 | 7 | 37 | 30 | 4 |
| 7. Limitations | 8 | 6 | 8 | 7 | 8 | 37 | 37 | 2 |
| 8. Conclusion | 8 | 7 | 8 | 7 | 8 | 38 | 37 | 1 |
| Declarations | 8 | 7 | 8 | 7 | 8 | 38 | 37 | 1 |
| Appendix A | 8 | 7 | 8 | 7 | 8 | 38 | (new) | 0 |
| **Mean / total** | **8.0** | **6.7** | **8.0** | **7.1** | **7.5** | **37.4** | **34.8** | **58** |

Every section now scores 35 or more. The round-1 sections below 35 (2, 5, and 6) have recovered, mainly because the repeated caveats and literature comparisons are gone. Section 4 is the lowest in Rhythm and Density, since the method-fidelity additions produced long sentences and some repetition. Its edits (M3, M13, M15) would raise it to about 38.

### Proofreading (six checks, adapted to R Markdown)

| # | Check | Errors | Warnings | Info | Total |
|---|---|---|---|---|---|
| 1 | Paper structure (abstract, intro, related work, conclusion) | 3 | 4 | 2 | 9 |
| 2 | Math symbols and notation | 6 | 6 | 4 | 16 |
| 3 | Statistical relevance and number provenance | 2 | 4 | 1 | 7 |
| 4 | Figures and tables | 1 | 4 | 2 | 7 |
| 5 | Grammar and style | 2 | 15 | 10 | 27 |
| 6 | Abbreviations | 0 | 0 | 3 | 3 |
| + | Integrity (references), not self-approved | 0 | 3 | 0 | 3 |
| | **Total** | **14** | **36** | **22** | **72** |

Round 1 had 67 findings (18 errors). Each count above is one finding per edit, so the four edits that fix the one $R^{m}$ clash count as four errors. Counted by distinct problem, the paper has 9 errors left.

### Overall assessment

The paper is in good shape. The round-1 notation clashes, undefined symbols, missing Cameron et al. (2011) entry, Figure 1 code labels, and cross-section repetition are all resolved, and every number in the text comes from an inline R expression except the three that S3 and X1 fix. The method-fidelity additions made Section 4 complete enough to reproduce. They also brought in one notation clash ($R^{m}$ against $m$), one wrong index, a few symbols used before definition, and three overlong sentences. All are fixed below without changing content. The most important remaining issue is substantive: the novelty claim about the gap/session split conflicts with the paper's own account of Huang et al. (2001).

### Top issues to address

1. **[ERROR] Check 1.2/1.6, internal consistency.** The introduction (I3) and Section 2 (L4, L8) say no reviewed study splits the next-day return into gap and session, but Section 2 and Table 5 credit Huang et al. (2001) with that split. Confirm against the source, then apply I3, L4, and L8.
2. **[ERROR] Check 2.3.** The market label $m$ in $R^{m}$ clashes with the family size $m = 26$ and $m_{\text{max}}$ (M1, M2, M5, M6). The control tercile uses $\overline{V}_{j,d}$ for the event stock $i$ (M8). $k$ is used before Equation (4) defines it (M3, M6).
3. **[ERROR] Number provenance.** "About two percentage points ... about one" (Section 6) and "about 25 months" (Section 7) are hand-typed. S3 and X1 replace them with existing inline expressions.
4. **[ERROR] Check 4.3.** The Table 1 caption is ungrammatical and sets $G$ in roman type (R10). The Table 2 caption defines a tercile rule that no row uses and that conflicts with Section 4 (R7, R11, R12).
5. **[WARN] Check 5.9, readability.** In Section 4, the timing remarks come before the outcomes they qualify, the characteristics normalization is one 107-word sentence, and the text repeats Appendix A (M3, M13, M15).
6. **[WARN] Integrity (not self-approved).** 22 of 50 references have no DOI. For Huang, Liu, and Shu (2023) and Lin et al. (2023), the article number is missing. The HC1 estimator is credited to the R package *sandwich* with no reference. Run the integrity gate's DOI check before adding any of these (see "Findings without an edit").

### Round-1 issues: status

| Round-1 top issue | Status now |
|---|---|
| $\tau$, $G$, $i$, $j$, $k$ each carried two meanings | Resolved: $\delta$ is the tick size, $e$ indexes events, $G$ counts only clusters, $\tau$ only weeks, $j$ and $l$ index stocks in the market sum, and $k$ counts only days. A new clash ($R^{m}$ against $m$) is fixed by M1, M2, M5, and M6. |
| Cameron et al. (2011) missing from references | Resolved: the entry is listed with a DOI. Record the DOI check in the integrity log; this report does not self-approve it. |
| Figure 1 code labels undefined | Resolved: the caption now carries a full key that matches Appendix A. |
| $G$, $\Phi^{-1}$, $x_{i,\tau}$, $n_\tau$, $k$, $\widehat{\text{SE}}$, AR, CAR, MDE undefined | Resolved, except that $k$ is used before its definition (M3, M6), and $u_e$ and $\varepsilon_{i,\tau}$ are new undefined symbols (M11, M14). |
| Repetition across Sections 5, 6, and Table 5 | Resolved. One residual quotable closer remains (R15). |
| −0.7% / 0.75% / −0.75% inconsistency | Abstract and conclusion now agree ("loses 0.7%"). Section 6 still says "returned −0.75%" (S4). |
| Constraint checks | No em dash in the rendered text. Every minus in prose is U+2212 (ASCII hyphens appear only inside R lookup keys and TeX). The Oxford comma is used throughout except DC1. Spelling is American throughout (behavior, organize, realized). The paper has 8 numbered sections plus Appendix A, no subsections, and run-in bold heads only. Process language: none, apart from the analysis-plan disclosure and the Table 5 caption's access note, both of which are integrity disclosures and stay. |

---

## Section-by-section review

Fenced blocks: `~~~old` is the exact current text and `~~~new` is the replacement. A new string that begins with an empty line inserts a paragraph break. An empty new block deletes the old text.

### Abstract

**Verdict.** 169 words, with the four required parts in order. Round-1 problems are gone: the false agency, the stacked "although ... while", the sign that read as a gain, and the missing H3 number. Two small points remain. "22 price- and volume-based characteristics" are counted as tests without being called tests, and "the two" in the last sentence could refer to news and attention.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 8 = **38/50**

**A1.** [WARN, check 5] The abstract counts 22 characteristics as tests. Name them as tests so the 26 adds up, and say what the tests survive.
~~~old
four price-limit event tests and 22 price- and volume-based characteristics. All four limit tests survive; none of the 22 characteristics does, although those tests have limited power.
~~~
~~~new
four price-limit event tests and 22 tests of price- and volume-based characteristics. All four limit tests survive the control; none of the 22 characteristic tests does, although those tests have limited power.
~~~

**A2.** [WARN, check 5] "The two" is ambiguous because news and attention are already two things. Name the data that are missing.
~~~old
but news and attention fit it as well, and we cannot separate the two with these data.
~~~
~~~new
but news and attention fit it as well, and without news or order-book data we cannot separate these explanations.
~~~

---

### 1. Introduction

**Verdict.** The structure is complete: motivation, an explicit "However" gap, the approach, three contributions with numbers, and a roadmap that matches Sections 2 to 8 in the present tense. Round-1 problems are gone. One substantive problem remains. The gap claim ("none of the studies we reviewed splits the next-day return ... into the overnight gap and the trading session") contradicts Section 2 and Table 5, which credit Huang et al. (2001) with the same timing split. The opening sentence of paragraph 2 is a sweeping claim that the "However" sentence repeats.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 8 = **38/50**

**I1.** [WARN, check 1] Vague, sweeping opener ("No study has settled") that the "However, none ..." sentence repeats. Replace it with a topic sentence the next sentence supports.
~~~old
No study has settled how prices move after a limit close in such a market.
~~~
~~~new
Recent work on price limits measures market quality and investor behavior.
~~~

**I2.** [INFO, check 5] APA author-date order inside one parenthesis is alphabetical.
~~~old
(Qi, 2023; Lien et al., 2019; Jia et al., 2024)
~~~
~~~new
(Jia et al., 2024; Lien et al., 2019; Qi, 2023)
~~~

**I3.** [ERROR, check 1] **[verify]** Consistency of the gap claim. Section 2 says Huang et al. (2001) find that the overnight overreaction after limit hits reverses during the next session, and Table 5 calls their result "Same timing: positive gap, partial intraday reversal". The claim that none of the reviewed studies splits the next-day return into gap and session therefore contradicts the paper itself. The authors must confirm from Huang et al. (2001) that the wording below describes that study correctly.
~~~old
However, none of the studies we reviewed splits the next-day return after a limit close into the overnight gap and the trading session that follows, none places
~~~
~~~new
However, of the studies we reviewed, only Huang et al. (2001) split the next-day return after a limit hit into the overnight gap and the trading session that follows, none places
~~~

**I4.** [INFO, check 5] Filler adjective.
~~~old
with 22 familiar price- and volume-based characteristics
~~~
~~~new
with 22 price- and volume-based characteristics
~~~

---

### 2. Related literature and hypotheses

**Verdict.** The section is now organized by theme, and each theme ends with its own gap statement. Round-1 repetition is gone. Remaining: two run-in heads repeat in the first sentence of their paragraph ("Theory. Theory", "Overnight and intraday returns. Overnight and intraday returns differ"), and a third paragraph opens with a sentence that restates its head. The Huang et al. (2001) contradiction appears twice (end of the classic-evidence paragraph and the gap paragraph). "These designs compare markets or periods" misdescribes the account-level and cross-sectional studies. "Lets us test which prediction fits" promises more than Sections 5 and 6 deliver.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 7 = **37/50**

**L1.** [WARN, check 5] The run-in head and the first word repeat ("Theory. Theory").
~~~old
**Theory.** Theory predicts protection or distortion
~~~
~~~new
**Theory.** Models predict protection or distortion
~~~

**L2.** [WARN, check 1] Overclaim: Sections 5 and 6 conclude that the data cannot separate the readings, so the paragraph should not promise a test of "which prediction fits". State what the next-day return measures.
~~~old
The next-day return after a limit close lets us test which prediction fits.
~~~
~~~new
A limit that only delays adjustment leaves a predictable next-day continuation, so the return after a limit close bears on this debate.
~~~

**L3.** [WARN, check 5] Vague result ("implies a delay"); name what is delayed.
~~~old
which implies a delay, and Berkman and Lee (2002)
~~~
~~~new
which implies that the narrower limit delayed price adjustment, and Berkman and Lee (2002)
~~~

**L4.** [ERROR, check 1] **[verify]** Same contradiction as I3: three sentences earlier this paragraph reports that Huang et al. (2001) separate the overnight move from the next session.
~~~old
None of these studies splits the next-day return into the overnight gap and the session that follows.
~~~
~~~new
Apart from Huang et al. (2001), these studies do not split the next-day return into the overnight gap and the session that follows.
~~~

**L5.** [WARN, check 5] The first sentence repeats the run-in head word for word. Delete it.
~~~old
**Recent evidence from band changes and investor-level data.** Recent studies use band changes and investor-level data to measure how limits affect market quality and trader behavior. The widening
~~~
~~~new
**Recent evidence from band changes and investor-level data.** The widening
~~~

**L6.** [WARN, check 1] Inaccurate summary: Chen et al. (2019), Lin et al. (2023), and Zeng et al. (2024) do not compare markets or periods. Name the two designs.
~~~old
These designs compare markets or periods; ours conditions on individual limit closes within one band regime.
~~~
~~~new
The band-change studies compare periods with different bands, and the cross-sectional studies sort stocks by limit exposure; ours conditions on individual limit closes within one band regime.
~~~

**L7.** [WARN, check 5] The run-in head and the first sentence repeat each other ("Overnight and intraday returns. Overnight and intraday returns differ").
~~~old
**Overnight and intraday returns.** Overnight and intraday returns differ, and explanations
~~~
~~~new
**Overnight and intraday returns.** Returns earned overnight differ from returns earned during the session, and explanations
~~~

**L8.** [ERROR, check 1] **[verify]** The gap statement must agree with L4 and I3. Taiwan's market in the Huang et al. (2001) period also set prices by call auction, so "in a market with call auctions" cannot carry the novelty claim.
~~~old
None combines the two in a market with call auctions, controls for multiple testing, or uses the 2025 platform change.
~~~
~~~new
Apart from Huang et al. (2001), none combines the two, and none controls for multiple testing or uses the 2025 platform change.
~~~

---

### 3. Data and institutional setting

**Verdict.** Clear and specific. Every number is an inline R expression. Only small issues remain: one unparallel sentence, a missing comma after an introductory date, and "dollar volume ... in dong". Section 4 repeats that definition, and edit M3 removes the repeat.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 8, Density 8 = **39/50**

**D1.** [INFO, check 5] Comma after the introductory date phrase, matching "On 24 September 2026, we downloaded".
~~~old
On 5 May 2025 HOSE moved
~~~
~~~new
On 5 May 2025, HOSE moved
~~~

**D2.** [WARN, check 5] The two halves of the sentence are not parallel ("has a median ... and the mean is"). The phrase "in dong" also sits oddly beside "dollar volume". Keep the conventional term and say so once. Section 4 can then drop its repeat definition (edit M3).
~~~old
dollar volume (price times shares traded, in dong) has a median per stock-day of `r f(c26(9)/1000,1)` billion dong and the mean is `r f(c26(10)/1000,1)` billion dong.
~~~
~~~new
dollar volume (price times shares traded; we keep the conventional term although values are in dong) has a median of `r f(c26(9)/1000,1)` billion dong per stock-day and a mean of `r f(c26(10)/1000,1)` billion dong.
~~~

---

### 4. Design

**Verdict.** **Length and order.** The method-fidelity additions take the section from about 945 to about 1,535 source words. It is still readable, and its order is sound: events, outcomes, inference, characteristics, multiplicity, plan. Three passages are hard going. (a) The weight-timing sentences sit in the Returns paragraph before $k$, Table 1's outcomes, and the weekly regressions exist (M3, M6, M7). (b) The characteristics normalization is one 107-word sentence (M13). (c) The HC1 sentence runs to 62 words, with an undefined error term (M11). The section also repeats Appendix A's lookback windows (M15) and Section 3's dollar-volume definition (M3).

**Symbols.** Every symbol is now defined at or before first use, with three exceptions: $k$ (used in the Returns paragraph, defined after Equation (4)), $u_e$, and $\varepsilon_{i,\tau}$. One notation clash is new to this round's reading. The market label $m$ in $R^{m}$ shares its letter with the family size $m = 26$ and $m_{\text{max}}$, and M1, M2, M5, and M6 change the label to $\text{mkt}$. The round-1 clashes ($\tau$, $G$, $i$, $j$, $k$) are resolved. One index slip is new: the control-tercile variable is $\overline{V}_{j,d}$ where it should be $\overline{V}_{i,d}$ (M8). "The floor" and "the ceiling" in the rounding sentence read as the limit prices, not the rounding functions (M4). "Week" now has two meanings, calendar week for clustering and formation week (M12). $y$ serves as both the event outcome $y_e$ and the weekly outcome $y_{i,\tau}$. The subscripts tell them apart, so this report proposes no edit.

**Equations.** Equations (1) to (8) are numbered in order, and every displayed equation flows from a lead-in clause and ends with punctuation. No reference points forward. The text cites Equations (2), (3), (4), (5), (7), and (8). M10 adds a citation of Equation (6). Equation (1) is never cited (INFO; it defines $R_{i,d}$ and can stay numbered for the sequence). Multi-letter symbols are set consistently in `\mathit` (AR, CAR, GAP, INTRA, TO). Labels such as $\text{ceiling}$, $\text{floor}$, and $\text{max}$ are upright. M11 replaces the inline `\frac` with slashes. Units are consistent: prices and tick sizes in thousand dong, thresholds as decimals in formulas and as percentages in prose, costs in basis points.

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 6 = **35/50**

**M1.** [ERROR, check 2] Notation clash: the italic superscript $m$ in $R^{m}$ is a label, but Section 4 later uses $m$ for the family size ($m = 26$, $m_{\text{max}}$). Set the label upright as $\text{mkt}$. Edits M1, M2, M5, and M6 make the change everywhere it appears. Also, "all stocks" contradicts the eligibility rule in the where-clause.
~~~old
The market return $R^{m}_{d}$ is the dollar-volume-weighted return of all stocks,
~~~
~~~new
The market return $R^{\text{mkt}}_{d}$ is the dollar-volume-weighted return across stocks,
~~~

**M2.** [ERROR, check 2] Notation (see M1).
~~~old
$$R^{m}_{d} = \sum_{j}
~~~
~~~new
$$R^{\text{mkt}}_{d} = \sum_{j}
~~~

**M3.** [ERROR, check 2] Reading order. The paragraph uses $d+k$ and Table 1 before Equation (4) defines $k$ and the outcomes, and it gives the weight timing of the weekly regressions before they are introduced. The Characteristics paragraph already states that timing ("weighted by $\overline{V}$ at the end of the week"), and edits M6 and M7 move the rest next to Equations (4) and (5). Dollar volume is already defined in Section 3. A run-in head separates the market return from the exact-hit rule.
~~~old
where $j$ and $l$ run over the stocks with a return on the day and a full 60-day volume history, dollar volume is price times shares traded (in dong), and $\overline{V}_{j,d}$ is the average dollar volume of stock $j$ over the 60 trading days through day $d$. Abnormal returns subtract a market return over the same interval. In Table 1 the market return of each day $d+k$ uses Equation (2) with weights through that same day. Tables 2 to 4 and Figure 2 weight every interval after the day-$d$ close with $w_{j,d}$, known at the event close, and the weekly regressions below use weights through the formation day. An exact limit hit
~~~
~~~new
where $j$ and $l$ run over the stocks with a return on day $d$ and a full 60-day volume history, and $\overline{V}_{j,d}$ is the average dollar volume (Section 3) of stock $j$ over the 60 trading days through day $d$.

**Exact hits.** An exact limit hit
~~~

**M4.** [WARN, check 2] Ambiguity: "the floor" and "the ceiling" read as the floor and ceiling limits, but the text means the rounding functions (the floor function sets the ceiling price). Use the symbols.
~~~old
In computation we add $10^{-9}$ inside the floor and subtract it inside the ceiling to guard against floating-point error.
~~~
~~~new
In computation we add $10^{-9}$ inside $\lfloor \cdot \rfloor$ and subtract it inside $\lceil \cdot \rceil$ to guard against floating-point error.
~~~

**M5.** [ERROR, check 2] Notation (see M1).
~~~old
- R^{m}_{d+1}, \qquad \mathit{CAR}_{i,d} = \prod_{k=1}^{5} \left(1 + R_{i,d+k}\right) - \prod_{k=1}^{5} \left(1 + R^{m}_{d+k}\right)
~~~
~~~new
- R^{\text{mkt}}_{d+1}, \qquad \mathit{CAR}_{i,d} = \prod_{k=1}^{5} \left(1 + R_{i,d+k}\right) - \prod_{k=1}^{5} \left(1 + R^{\text{mkt}}_{d+k}\right)
~~~

**M6.** [ERROR, check 2] Give the range of $k$, and put the Table 1 weight timing (moved out by M3) where $k$ is defined.
~~~old
where $k$ counts trading days after the event. We split
~~~
~~~new
where $k = 1, \dots, 5$ counts trading days after the event and each $R^{\text{mkt}}_{d+k}$ uses weights through day $d+k$ (Table 1). We split
~~~

**M7.** [WARN, check 2] Put the lagged-weight convention for Tables 2 to 4 and Figure 2 (moved out by M3) next to the definition it governs. "All stocks" again contradicts the eligibility rule of Equation (2).
~~~old
and subtract the market counterpart of each component, the same-interval return of all stocks weighted with $w_{j,d}$, to obtain abnormal values.
~~~
~~~new
and subtract the market counterpart of each component, the same-interval return across stocks weighted with $w_{j,d}$, to obtain abnormal values. Tables 2 to 4 and Figure 2 use these weights, known at the event close, for every interval after the day-$d$ close.
~~~

**M8.** [ERROR, check 2] Wrong index: the event stock is $i$; $j$ indexes the stocks in the market return.
~~~old
in the event stock's tercile of $\overline{V}_{j,d}$;
~~~
~~~new
in the event stock's tercile of $\overline{V}_{i,d}$;
~~~

**M9.** [WARN, check 2] Link the new event index $e$ to the stock-day notation $(i, d)$ used up to this point.
~~~old
For a sample of $N$ events $e = 1, \dots, N$ with outcome $y_e$
~~~
~~~new
For a sample of $N$ events $e = 1, \dots, N$, each a stock-day pair $(i, d)$, with outcome $y_e$
~~~

**M10.** [WARN, check 5] Unclear coordination ("without the factor ... and a standard normal reference" can be read as "without ... a standard normal reference"). Make the three parts parallel, refer to Equation (6) (now never cited), and avoid "family-wide control", which the text has not yet defined.
~~~old
The *p*-values of the four event tests that enter the family-wide control use event-date clusters without the factor $G/(G-1)$ and a standard normal reference.
~~~
~~~new
The *p*-values with which the four event tests enter the multiple-testing family use Equation (6) with event-date clusters, omit the factor $G/(G-1)$, and take a standard normal reference.
~~~

**M11.** [WARN, check 2] This 62-word sentence defines no error term, reuses $N$ and $G$ for a different sample, and puts display fractions in inline math (Check 2.7). Split it, define $u_e$, and italicize the package name.
~~~old
for the comparison group, and cluster the standard error of $\hat{\beta}$ by event date with the small-sample factor $\frac{G}{G-1}\cdot\frac{N-1}{N-2}$ (the HC1 option of the R package sandwich).
~~~
~~~new
for the comparison group, and $u_e$ is the error term. We cluster the standard error of $\hat{\beta}$ by event date with the small-sample factor $G/(G-1) \cdot (N-1)/(N-2)$, where $N$ and $G$ now count the stock-days and dates in the regression sample (the HC1 option of the R package *sandwich*).
~~~

**M12.** [WARN, check 2] "Week" now has two meanings in Section 4: calendar weeks (clusters) and five-trading-day formation periods. Say so where the second is introduced.
~~~old
which we call weeks $\tau = 1, \dots, T$;
~~~
~~~new
which we call weeks $\tau = 1, \dots, T$ (they differ from the calendar weeks used for clustering);
~~~

**M13.** [WARN, check 5] A 107-word sentence that defines $z$, $\Phi^{-1}$, $y$, and the regression all at once, and reverses the usual order ("regressions on $z$ of $y$"). Split it into three sentences. The 115-day lookback moves here from the sentence that M15 deletes.
~~~old
At the end of each week we rank-normalize each characteristic $x_{i,\tau}$ across the $n_\tau$ stocks with complete data (returns, opens, and closes on all 115 lookback days, trades on at least 50 of the last 60 days, and returns on the next five days), with ties at average ranks, $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, where $\Phi^{-1}$ is the inverse standard normal distribution function, and run Fama and MacBeth (1973) regressions on $z_{i,\tau}$ of $y_{i,\tau}$, the stock's compounded return over the next five trading days minus the average of the same five-day returns across these stocks weighted by $\overline{V}$ at the end of the week,
~~~
~~~new
At the end of each week we rank-normalize each characteristic $x_{i,\tau}$ across the $n_\tau$ stocks with complete data: returns, opens, and closes on all 115 days of the longest lookback, which includes the formation day; trades on at least 50 of the last 60 days; and returns on the next five days. With ties at average ranks, the score is $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, where $\Phi^{-1}$ is the inverse standard normal distribution function. The outcome $y_{i,\tau}$ is the compounded return of stock $i$ over the next five trading days minus the average of the same five-day returns across these stocks, weighted by $\overline{V}$ at the end of the week. We run Fama and MacBeth (1973) regressions of $y_{i,\tau}$ on $z_{i,\tau}$,
~~~

**M14.** [WARN, check 2] Define the residual, and end the where-clause before the inference details so the sentence does not run on.
~~~old
where $a_\tau$ is the weekly intercept, and we compute the *t*-statistic
~~~
~~~new
where $a_\tau$ is the weekly intercept and $\varepsilon_{i,\tau}$ the residual. We compute the *t*-statistic
~~~

**M15.** [WARN, check 5] This sentence repeats Appendix A (momentum windows, idiosyncratic momentum) and the 115-day lookback, which M13 now states. Keep only the pointer.
~~~old
Lookbacks reach up to 115 trading days including the formation day; the 3-month and 6-month momentum windows cover 60 and 110 days ending five days before formation, and idiosyncratic momentum compounds the market-adjusted return over the 3-month window. Appendix A defines all 22 characteristics.
~~~
~~~new
Appendix A defines all 22 characteristics and their lookback windows.
~~~

**M16.** [WARN, check 1] **[verify]** Section 2 states H2 to H4 as hypotheses, but the analysis-plan paragraph lists the decomposition (H2), the comparison with sub-limit moves (H3), and the next-open returns (H4) as exploratory. Say so plainly so readers do not read H2 to H4 as pre-specified.
~~~old
the platform-change split, and the outlier exclusion.
~~~
~~~new
the platform-change split, and the outlier exclusion. The tests of H2 to H4 therefore rest on exploratory analyses.
~~~

---

### 5. Results (incl. Tables 1 to 4, Figures 1 and 2)

**Verdict.** The section is much tighter than in round 1, and the literature comparisons now sit in Table 5 and Section 6. The remaining problems are local. Two paragraphs exceed 250 words (Figure 1, Table 2), and edits R3 and R8 split them. In the Table 1 caption, a fragment follows a semicolon, and $G$ is set in roman type. The Table 2 caption defines all-stock liquidity terciles that no row of the table uses, and the definition conflicts with the control-tercile rule. "They survive" has no antecedent. Cho et al. (2003) are said to "predict" what they found. A quotable closing sentence overstates Table 3. Two citation lists are out of APA order (one here, one in Section 1).

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 7 = **36/50**

**R1.** [INFO, check 5] The list omits the 10-day blocks that Section 4 and Table 1 use.
~~~old
allow for dependence across dates, weeks, and stocks.
~~~
~~~new
allow for dependence across dates, weeks, 10-day blocks, and stocks.
~~~

**R2.** [WARN, check 5] Two unrelated claims are joined by "and". Split them.
~~~old
The null excludes only large effects, and dropping the least liquid 20% of stocks leaves
~~~
~~~new
The null excludes only large effects. Dropping the least liquid 20% of stocks leaves
~~~

**R3.** [INFO, check 5] The Figure 1 paragraph runs to about 260 words. Start a new paragraph where it turns from the estimates to their interpretation. Note the leading space in the old string.
~~~old
 The hurdles of Harvey et al. (2016) and Chordia et al. (2020)
~~~
~~~new


The hurdles of Harvey et al. (2016) and Chordia et al. (2020)
~~~

**R4.** [WARN, check 5] A short sample is a feature of the data, not of the market.
~~~old
Two features of this market can produce the null.
~~~
~~~new
Two features of the setting can produce the null.
~~~

**R5.** [WARN, check 3] The paragraph ends with a restatement rather than the inference. Name what the tests show relative to the characteristics without claiming a common horizon (the characteristics predict five-day returns, the events next-day returns).
~~~old
These tests support H1: limit closes carry information about the next day that none of the 22 characteristics carries.
~~~
~~~new
These tests support H1, and the limit closes pass the screen that none of the 22 characteristics passes.
~~~

**R6.** [INFO, check 5] Rhythm: four sentences in Section 5 end with "which supports H*n*". Vary one of them.
~~~old
The decomposition places the effect in the opening auction, which supports H2.
~~~
~~~new
The decomposition places the effect in the opening auction, as H2 predicts.
~~~

**R7.** [WARN, check 4] Define the subsample terciles where they are used. The Table 2 caption defines them now, but Table 2 has no tercile rows, and the rule differs from the control-benchmark terciles of Section 4 (edit R10 removes the caption sentence).
~~~old
and, for ceilings, in each liquidity tercile (
~~~
~~~new
and, for ceilings, in each tercile of 60-day average dollar volume across all stocks (
~~~

**R8.** [INFO, check 5] The Table 2 paragraph runs to about 380 words. Start the floor results as a new paragraph. Note the leading space in the old string.
~~~old
 After a floor close the gap is `r f(c16("Floor all","gap_mkt"),2)`%
~~~
~~~new


After a floor close the gap is `r f(c16("Floor all","gap_mkt"),2)`%
~~~

**R9.** [WARN, check 5] Tense shift ("were locked ... open again"), and "those" has an unclear referent.
~~~old
and some of those open again at the limit, where a buyer may be rationed.
~~~
~~~new
and some of these stocks opened at the limit the next day, where a buyer may be rationed.
~~~

**R10.** [ERROR, check 4] Table 1 caption: a fragment follows a semicolon ("; each with a ..."); $G$ appears in roman type while the text sets it in italics; and the caption assigns the *t* reference only to the week and 10-day statistics, whereas Section 4 assigns it to all Table 1 statistics.
~~~old
use clusters by event date, calendar week, and 10-day block; each with a G/(G − 1) correction, where G is the number of clusters; we judge the week and 10-day statistics against a *t* distribution with G − 1 degrees of freedom.
~~~
~~~new
use clusters by event date, calendar week, and 10-day block, each with the factor *G*/(*G* − 1), where *G* is the number of clusters; we judge all three against a *t* distribution with *G* − 1 degrees of freedom.
~~~

**R11.** [WARN, check 4] Table 2 caption: "non-event stocks" is imprecise (controls exclude every move of 6.5% or more, not only events). The tercile rule here is the control rule, not the all-stock rule that the caption gives later.
~~~old
or same-date non-event stocks in the same liquidity tercile.
~~~
~~~new
or same-date control stocks (absolute day-*d* return below 6.5%) in the same tercile of 60-day average dollar volume (Section 4).
~~~

**R12.** [WARN, check 4] Table 2 caption: remove the all-stock tercile definition, which describes no row of the table and conflicts with the control rule; R7 moves it to the text.
~~~old
Liquidity terciles rank all stocks by 60-day average dollar volume through day *d*; crash days are event days
~~~
~~~new
Crash days are event days
~~~

**R13.** [INFO, check 5] Two colon reveals in consecutive sentences. Use a plain clause for the second.
~~~old
At the limit the relation breaks: the overnight gap jumps up
~~~
~~~new
At the limit the relation breaks, and the overnight gap jumps up
~~~

**R14.** [WARN, check 5] Accuracy: Cho et al. (2003) is empirical (Section 2: "find that prices accelerate"), and only Chen et al. (2024) predict this. "A test" has no clear referent.
~~~old
Cho et al. (2003) and Chen et al. (2024) predict that prices accelerate toward a limit on the limit day (the magnet effect); a test needs intraday prices, which we lack.
~~~
~~~new
Cho et al. (2003) find, and Chen et al. (2024) predict, that prices accelerate toward a limit on the limit day (the magnet effect); testing this needs intraday prices, which we lack.
~~~

**R15.** [WARN, check 3] Quotable closer that overstates the Table 3 result ("shows ... carries information"; the comparison group closed 0.5 to 2 points below the limit, not "just below"). Table 3 and the H3 sentence already state the result. Delete. Note the leading space.
~~~old
 The larger gap at the limit shows that a close at the limit carries information that a close just below it lacks.
~~~
~~~new

~~~

**R16.** [INFO, check 5] APA order within one parenthesis.
~~~old
(Lien et al., 2019; Kim & Jun, 2019; Qi, 2023; Zhang et al., 2022)
~~~
~~~new
(Kim & Jun, 2019; Lien et al., 2019; Qi, 2023; Zhang et al., 2022)
~~~

**R17.** [WARN, check 5] False agency ("the split cannot isolate"). Name the actor and say what cannot be attributed.
~~~old
Both periods show the main pattern, and the split cannot isolate an effect of the auction rules.
~~~
~~~new
Both periods show the main pattern, and we cannot attribute the differences between them to the auction rules.
~~~

**R18.** [ERROR, check 5] "They" has no antecedent (the previous sentence's subject is "we").
~~~old
from Section 4. They survive a Bonferroni correction
~~~
~~~new
from Section 4. All four event tests survive a Bonferroni correction
~~~

---

### 6. Discussion (incl. Table 5)

**Verdict.** Round-1 duplication with Section 5 is gone. Remaining: a one-sentence paragraph; two hand-typed numbers ("about two percentage points ... about one") that break the R-output rule and hide the sign of the floor gap; the investor sentence still says "returned −0.75%" while the abstract and conclusion say "loses 0.7%"; and a comma splice in the Qi (2023) cell of Table 5. The Table 5 caption's "records we could access" is a citation-integrity disclosure, and this report keeps it.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 7 = **37/50**

**S1.** [INFO, check 5] A one-sentence paragraph that continues the point of the paragraph before it. Merge them. The old string spans the paragraph break.
~~~old
does not fit a gap-only reading.

Our decomposition adds timing
~~~
~~~new
does not fit a gap-only reading. Our decomposition adds timing
~~~

**S2.** [WARN, check 4] Table 5, Qi (2023) row: a comma splice ("Qi studies ..., we study ...") inside a cell that already holds a semicolon.
~~~old
Different outcome: Qi studies market quality after a band change, we study returns after limit closes; both ceiling and floor closes carry a significant next-day return here, with a weaker floor effect that depends on the benchmark
~~~
~~~new
Different outcome: market quality after a band change. Here both ceiling and floor closes carry a significant next-day return, and the weaker floor effect depends on the benchmark
~~~

**S3.** [ERROR, check 3] Hand-typed numbers ("about two", "about one") break the rule that every number comes from R output, and "about one" hides the negative sign of the floor gap. Reuse the inline expressions of Section 8.
~~~old
the next opening carries about two percentage points after ceiling closes and about one after floor closes.
~~~
~~~new
the overnight gap averages `r f(c16("Ceiling all","gap_mkt"),1)`% after ceiling closes and `r f(c16("Floor all","gap_mkt"),1)`% after floor closes.
~~~

**S4.** [WARN, check 3] "Returned −0.75%" reads as a gain and uses a different precision from the abstract and conclusion ("loses 0.7%"). This is a display-only change: the edit adds `abs()` and uses one decimal, reusing the abstract's expression.
~~~old
buying ceiling stocks at the quoted next open returned `r f(c11("Ceiling: rule-based","f5o_mkt"),2)`% against the market
~~~
~~~new
buying ceiling stocks at the quoted next open lost `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market
~~~

---

### 7. Limitations

**Verdict.** The numbered list is specific and honest. One hand-typed figure ("about 25 months") and one hedge (item viii) that is firmer than Section 4's "may overstate". The single long paragraph is acceptable for an enumerated list.

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 8 = **37/50**

**X1.** [ERROR, check 3] Hand-typed number ("about 25 months"). Use the saved trading-day count from Section 3.
~~~old
(i) The sample covers about 25 months on one exchange,
~~~
~~~new
(i) The sample covers `r c26(4)` trading days on one exchange,
~~~

**X2.** [WARN, check 3] Inconsistent hedge: Section 4 says the estimates "may overstate" the true effect, but this item states the bias as fact.
~~~old
and the effect sizes carry winner's-curse bias because
~~~
~~~new
and the effect sizes may carry winner's-curse bias because
~~~

---

### 8. Conclusion

**Verdict.** The conclusion restates the key numbers (all inline), the mechanism, and the open question, and it adds no new content. "Survive ... a confirmation half" is the one infelicity. The conclusion does not say why the results improve on earlier work (Check 1.8, INFO). Table 5 and Section 6 do that, so no edit is proposed.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 8 = **38/50**

**C1.** [INFO, check 1] "Survive ... a confirmation half" is not a test. Name the criterion.
~~~old
survive FDR control and a confirmation half, and the 22
~~~
~~~new
survive FDR control and the confirmation-half check, and the 22
~~~

---

### Declarations

**Verdict.** The disclosure of AI use and of the data source is adequate. One Oxford comma is missing.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 8 = **38/50**

**DC1.** [ERROR, check 5] Oxford comma.
~~~old
**Funding, competing interests, ethics and author contributions.**
~~~
~~~new
**Funding, competing interests, ethics, and author contributions.**
~~~

---

### Appendix A

**Verdict.** Definitions match the Section 4 list and the Figure 1 key, and the notation (`\mathit{TO}`) matches the main text. No edits.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 8 = **38/50**

No edits.

## Findings without an edit

- [INFO] Check 2.10: Equation (1) is numbered but never cited. Keep it; it anchors the numbering and is the base definition.
- [INFO] Check 2.3: $y$ means both the event outcome $y_e$ (Equation (6)) and the weekly outcome $y_{i,\tau}$ (Equation (7)). The subscripts tell them apart. If the authors want one symbol per concept, rename the weekly outcome $r_{i,\tau}$ in Equation (7) and in the sentence that defines it.
- [INFO] Check 2.9: Operator styling is mixed. $\widehat{\operatorname{Var}}$ uses `\operatorname`, while $\widehat{\text{SE}}$ and $\text{MDE}$ use `\text`. Both render upright in Word, so no edit.
- [INFO] Check 2.9: Section 4 writes days in math ($d+1$), while Section 5, the captions, and the analysis-plan paragraph write *d*+1 in Markdown italics. Both render as italic *d* in Word. The plain-text spacing difference ("d + 1" against "d+1") is a pandoc artifact.
- [INFO] Check 4.5: Figures 1 and 2 are PNG files. That is acceptable for Word, but a journal may ask for vector (PDF or EPS) versions at submission.
- [INFO] Check 4.3: Table 3, Table 4, and the Table 5 cells write ranges with en dashes ("3–5%"), while the prose writes "3% to 5%". That is a common table convention, so no edit.
- [INFO] Check 6.1: HC1 and ISO ("ISO week") are never expanded. Both are standard technical names. Spell out "ISO 8601 week" if the journal requires it.
- [INFO] Check 6.4: AR and CAR are introduced in Section 4 but appear only inside Equation (4); the prose says "market-adjusted return". That is acceptable because the abbreviations name the symbols.
- [INFO] Check 6.2: The abstract introduces no abbreviation and uses none, which is correct.
- [INFO] Check 1.8: The conclusion does not say why the results improve on earlier work. Table 5 and Section 6 cover this.
- [INFO] Check 3.1: Figure 2 shows 95% confidence bars and Figure 1 shows *t*-statistics with reference lines, so the uncertainty display is adequate.
- [WARN] Integrity: 22 reference entries have no DOI: Aboody et al. (2018), Bogousslavsky (2021), Chordia et al. (2020), Deb et al. (2013), Greenwald and Stein (1991), Holm (1979), Hou et al. (2020), Huang et al. (2023), Huang et al. (2001), Jones et al. (2025), Kim and Limpaphayom (2000), Kim and Jun (2019), Kodres and O'Brien (1994), Lien et al. (2019), Lin et al. (2023), Lu et al. (2023), Petersen (2009), Qiao and Dam (2020), Qiu et al. (2025), Zhang et al. (2022), and the two web sources (HSC, Viet Nam News). Run the DOI check for the 20 journal articles and add a DOI only after the check resolves. This report supplies none from memory.
- [WARN] Integrity: Huang, Liu, and Shu (2023, *Pacific-Basin Finance Journal, 82*) and Lin et al. (2023, *Journal of Banking & Finance, 150*) have no article number or page range.
- [WARN] Integrity: The HC1 option of the R package *sandwich* (Section 4) has no reference. The usual citation is the package's *Journal of Statistical Software* article by Zeileis (2004). Add it only after the DOI check confirms the entry. This report does not insert it.

## Verification log

Script: `scratchpad/edits.py` holds the edit list, and `scratchpad/gen.py` checks it and builds this report.

Source SHA-256 (first 12): `c48f027a3f96`. Edits: 58. Every old string occurs exactly once in the source: **yes**. Every old string still occurs exactly once when the earlier edits have been applied in order: **yes**. The knitted scratch copy rendered without error.

| Edit | Count in source | Count at application |
|---|---|---|
| A1 | 1 | 1 |
| A2 | 1 | 1 |
| I1 | 1 | 1 |
| I2 | 1 | 1 |
| I3 | 1 | 1 |
| I4 | 1 | 1 |
| L1 | 1 | 1 |
| L2 | 1 | 1 |
| L3 | 1 | 1 |
| L4 | 1 | 1 |
| L5 | 1 | 1 |
| L6 | 1 | 1 |
| L7 | 1 | 1 |
| L8 | 1 | 1 |
| D1 | 1 | 1 |
| D2 | 1 | 1 |
| M1 | 1 | 1 |
| M2 | 1 | 1 |
| M3 | 1 | 1 |
| M4 | 1 | 1 |
| M5 | 1 | 1 |
| M6 | 1 | 1 |
| M7 | 1 | 1 |
| M8 | 1 | 1 |
| M9 | 1 | 1 |
| M10 | 1 | 1 |
| M11 | 1 | 1 |
| M12 | 1 | 1 |
| M13 | 1 | 1 |
| M14 | 1 | 1 |
| M15 | 1 | 1 |
| M16 | 1 | 1 |
| R1 | 1 | 1 |
| R2 | 1 | 1 |
| R3 | 1 | 1 |
| R4 | 1 | 1 |
| R5 | 1 | 1 |
| R6 | 1 | 1 |
| R7 | 1 | 1 |
| R8 | 1 | 1 |
| R9 | 1 | 1 |
| R10 | 1 | 1 |
| R11 | 1 | 1 |
| R12 | 1 | 1 |
| R13 | 1 | 1 |
| R14 | 1 | 1 |
| R15 | 1 | 1 |
| R16 | 1 | 1 |
| R17 | 1 | 1 |
| R18 | 1 | 1 |
| S1 | 1 | 1 |
| S2 | 1 | 1 |
| S3 | 1 | 1 |
| S4 | 1 | 1 |
| X1 | 1 | 1 |
| X2 | 1 | 1 |
| C1 | 1 | 1 |
| DC1 | 1 | 1 |
