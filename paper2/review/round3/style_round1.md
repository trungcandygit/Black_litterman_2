# Style and proofreading review, round 1 (stop-slop + proofreading)

**Paper:** "Closing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange"
**Source:** `paper2/manuscript/manuscript_final.Rmd` (rendered text checked against `manuscript_final.docx` via pandoc)
**Date:** 2026-10-05
**Mode:** report only. The source files are unchanged.

## How to use this report

- Every edit gives an exact **old** string from the `.Rmd` (each one appears once in the file; a script checked this, see the end of the report) and a **new** string. Apply the edits in order within each section.
- No edit changes code logic or a computed number. Some edits reuse inline `r ...` expressions already in the file. Three edits are display-only: they change rounding (`d = 2` to `d = 1`) or add `abs()` to show a sign as a verb ("loses"). Edit **D2** and edit **C1** swap two hard-coded data numbers (519 and 347) for inline R expressions that already exist in the file.
- Edits marked **[verify]** state a method detail that the reviewer inferred from the R scripts or output tables. The authors must confirm these against the code before applying them.
- Stop-slop scores use 1 to 10 per dimension. A section below 35/50 needs revision.

---

## Scorecard

### Stop-slop (per section)

| Section | Directness | Rhythm | Trust | Authenticity | Density | Total /50 | Edits |
|---|---|---|---|---|---|---|---|
| Abstract | 7 | 6 | 8 | 7 | 7 | 35 | 7 |
| 1 Introduction | 8 | 6 | 8 | 7 | 7 | 36 | 9 |
| 2 Related literature and hypotheses | 7 | 6 | 8 | 6 | 7 | 34 | 12 |
| 3 Data and institutional setting | 8 | 7 | 8 | 7 | 7 | 37 | 9 |
| 4 Design | 8 | 6 | 8 | 7 | 6 | 35 | 25 |
| 5 Results (incl. Tables 1–4, Figures 1–2) | 7 | 5 | 7 | 6 | 5 | 30 | 30 |
| 6 Discussion (incl. Table 5) | 6 | 6 | 7 | 6 | 5 | 30 | 9 |
| 7 Limitations | 8 | 6 | 8 | 7 | 8 | 37 | 5 |
| 8 Conclusion | 8 | 6 | 8 | 7 | 8 | 37 | 6 |
| Declarations | 8 | 7 | 8 | 7 | 7 | 37 | 2 |
| **Mean / total** | **7.5** | **6.1** | **7.8** | **6.7** | **6.7** | **34.8** | **114** |

Sections 2, 5 and 6 fall below 35. Two problems account for most of the gap. The paper restates the same claims ("no study reports a comparable next-day return", "our data lack intraday prices", "the split cannot isolate the rule change") two or three times. Section 5 also repeats the literature comparisons that Table 5 and Section 6 already make.

### Proofreading (six checks)

| # | Check | Errors | Warnings | Info | Total |
|---|---|---|---|---|---|
| 1 | Paper structure (abstract, intro, related work, conclusion) | 1 | 6 | 2 | 9 |
| 2 | Math symbols and notation | 9 | 6 | 4 | 19 |
| 3 | Statistical relevance | 0 | 3 | 1 | 4 |
| 4 | Figures and tables | 2 | 4 | 3 | 9 |
| 5 | Grammar and style | 2 | 12 | 3 | 17 |
| 6 | Abbreviations | 4 | 3 | 2 | 9 |
| | **Total** | **18** | **34** | **15** | **67** |

### Overall assessment

The paper is factual and hedges its claims carefully. Its numbers in the abstract, text and tables agree, and they all come from R output. The weakest parts are (a) Section 4 notation: one letter carries two meanings in three places, two symbols are used without definition, and multi-letter symbols are not set in `\mathit` (no wrapper on AR and CAR), and (b) repetition across Sections 5, 6 and Table 5. A missing reference (Cameron et al., 2011) is an integrity-gate item, and the authors must fix it before submission.

### Top issues to address

1. **[ERROR] Check 2.3:** $\tau$ means both tick size (Eq. 3) and week (Eq. 7). $G$ means both the overnight gap (Eq. 5) and the number of clusters (Eq. 6, Table 1 caption). $i$ means both stock and event (Eqs. 4–6). $j$ and $k$ each mean both a stock and a rank or day (Eqs. 2, 4, 8). Fix with edits M3–M5, M8–M10 and M14.
2. **[ERROR] Integrity / Check 4.2 analogue:** Section 4 cites "Cameron et al., 2011", but the reference list does not include it. Add Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2011). Robust inference with multiway clustering. *Journal of Business & Economic Statistics, 29*(2), 238–249. https://doi.org/10.1198/jbes.2010.07136. **Run the DOI check from the integrity gate before inserting it.** Do not self-approve this item.
3. **[ERROR] Check 6 / 4.3:** Figure 1 labels its axis with code names (REV1W, CSSPREAD, LIMITFREQ, DVOLCHG, TURNCHG, …) that the paper never defines. Edit R-F1 adds a key to the caption.
4. **[ERROR] Check 2.2:** Section 4 never defines $G$, $\Phi^{-1}$, $x_{i,\tau}$, $n_\tau$, $k$ (Eq. 4) or $\widehat{\text{SE}}$. It writes AR, CAR and MDE as bare letters with no abbreviation defined. Fix with edits M4–M13.
5. **[WARN] Check 5.9:** Claims repeat across Sections 5, 6 and Table 5 (literature comparisons, the magnet effect, "no comparable study", the platform-split caveat). Edits R15, R11, R26, S3–S5 remove the duplicates.
6. **[WARN] Check 1.1/5.6:** The numbers are inconsistent in one place. The abstract says the buyer "earns −0.7%", the conclusion says "loses 0.75%" and Section 6 says "returned −0.75%". Edits A6 and C5 align them at one decimal.

---

## Section-by-section review

Fenced blocks: `~~~old` is the exact current text and `~~~new` is the replacement.

### Abstract

**Verdict.** It has 166 words and contains all four required parts (motivation, gap, approach, results) in order. Problems: false agency ("limits aim"); an awkward sentence that buries the main result ("None … survives, although …, while all four … do"); a sign that reads as a gain ("earns −0.7%"); an H3 claim with no number; and HOSE is defined but never reused in the abstract. After the edits it has about 180 words.

**Scores:** Directness 7, Rhythm 6, Trust 8, Authenticity 7, Density 7 = **35/50**

**A1.** False agency: limits do not "aim".
~~~old
Daily price limits aim to cool markets but can delay price discovery.
~~~
~~~new
Regulators impose daily price limits to cool markets, but limits can delay price discovery.
~~~

**A2.** Vague gap ("is thin"); name what is missing.
~~~old
Evidence on prices after limit closes in emerging markets is thin, and published limit studies do not account for the many price-based signals a researcher could have examined.
~~~
~~~new
Few studies trace prices after limit closes in emerging markets, and those we know of ignore the many other price-based signals a researcher could have tested.
~~~

**A3.** The abstract never uses "HOSE" again. Under Check 6.2, an abbreviation used once should not be introduced.
~~~old
We study `r nstocks` stocks on the Ho Chi Minh Stock Exchange (HOSE) from August 2024
~~~
~~~new
We study `r nstocks` stocks on the Ho Chi Minh Stock Exchange from August 2024
~~~

**A4.** Lead with the surviving tests and remove the stacked "although … while".
~~~old
None of the 22 characteristics survives, although the tests have limited power, while all four limit tests do.
~~~
~~~new
All four limit tests survive; none of the 22 characteristics does, although those tests have limited power.
~~~

**A5.** Active subject. Split the sentence and add the H3 number.
~~~old
A ceiling close is followed by a next-day abnormal return of `r f(ev("ceiling","t+1","mean_ar_pct"),1)`%: an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%, and the gap exceeds that of stocks that rose almost as far without reaching the limit.
~~~
~~~new
After a ceiling close, the stock earns a next-day abnormal return of `r f(ev("ceiling","t+1","mean_ar_pct"),1)`%: an overnight gap of `r f(c16("Ceiling all","gap_mkt"),1)`% less an intraday reversal of `r f(abs(c16("Ceiling all","intraday_mkt")),1)`%. The gap exceeds that of stocks that rose 5% to 6.5% by `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points.
~~~

**A6.** "Earns −0.7%" reads as a gain. This is a display-only change (adds `abs()`; the number is the same).
~~~old
A buyer at the next open earns `r f(c11("Ceiling: rule-based","f5o_mkt"),1)`% by the fifth close.
~~~
~~~new
A buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close.
~~~

**A7.** False agency ("data cannot separate").
~~~old
The pattern fits delayed price discovery, but news and attention can explain it as well, and our data cannot separate the two.
~~~
~~~new
The pattern fits delayed price discovery, but news and attention fit it as well, and we cannot separate the two with these data.
~~~

---

### 1. Introduction

**Verdict.** The structure is right: motivation, gap with an explicit "However", approach, a contribution list containing the word "contribution", and a roadmap that matches Sections 2–8. Problems: the adverb "long"; false agency ("band changes have reopened the question"); "to our knowledge, none of the studies we reviewed", which says the same thing twice; and three contributions with no numbers (Check 1.3 ERROR, too vague to falsify). The roadmap is correct but drops its verb ("and Section 4 the design").

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 7 = **36/50**

**I1.** Adverb "long", and false agency.
~~~old
Economists have long asked whether a limit protects prices or only postpones their adjustment, and recent band changes in China, Taiwan, and Korea have reopened the question.
~~~
~~~new
Economists ask whether a limit protects prices or postpones their adjustment, and recent band changes in China, Taiwan, and Korea give them new test cases.
~~~

**I2.** Wordy double "meet our definition". Section 4 now defines "event window" (edit M2).
~~~old
it applies one 7% band to every stock, and about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in our event window meet our definition of an upper-limit close (the ceiling, Section 4) and about `r f(100 * C13$value[6] / C13$value[1], 1)`% meet our definition of a lower-limit close (the floor).
~~~
~~~new
it applies one 7% band to all stocks, and about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in our event window close at the upper limit (a ceiling close; Section 4) and about `r f(100 * C13$value[6] / C13$value[1], 1)`% at the lower limit (a floor close).
~~~

**I3.** Vague declarative.
~~~old
The literature has not settled what happens after a limit close in such a market.
~~~
~~~new
No study has settled how prices move after a limit close in such a market.
~~~

**I4.** The hedge is stated twice.
~~~old
However, to our knowledge, none of the studies we reviewed splits
~~~
~~~new
However, none of the studies we reviewed splits
~~~

**I5.** Jargon ("discipline the search"). Use the unhyphenated noun form "false discovery rate" (hyphenate only before a noun).
~~~old
To discipline the search, we place four limit tests in one family of 26 tests with 22 familiar price- and volume-based characteristics and control the false-discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).
~~~
~~~new
We place the four limit tests in one family of 26 tests with 22 familiar price- and volume-based characteristics and control the false discovery rate (FDR; Benjamini & Hochberg, 1995; Harvey et al., 2016).
~~~

**I6.** Contribution 1 needs a number (Check 1.3).
~~~old
and show that the ceiling effect is a gap followed by a partial reversal.
~~~
~~~new
and show that the ceiling effect is a gap of `r f(c16("Ceiling all","gap_mkt"),1)`% of which the following session reverses `r f(100 * abs(c16("Ceiling all","intraday_mkt")) / c16("Ceiling all","gap_mkt"), 0)`%.
~~~

**I7.** Contribution 2 needs a number.
~~~old
and find that the gap is larger at the limit.
~~~
~~~new
and find that the ceiling gap is `r f(c17("ceiling vs 5-6.5% up","gap_mkt","diff_pct"),1)` percentage points larger at the limit than after rises of 5% to 6.5%.
~~~

**I8.** Contribution 3 needs a number and a precise subject.
~~~old
Third, we show that the limit effect survives a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open cannot capture it.
~~~
~~~new
Third, we show that all four limit tests survive a multiplicity-controlled family in which no characteristic survives, and that a buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close.
~~~

**I9.** The roadmap is missing a verb.
~~~old
Section 2 reviews the related literature and states the hypotheses, Section 3 describes the data and the institutional setting, and Section 4 the design.
~~~
~~~new
Section 2 reviews the literature and states the hypotheses, Section 3 describes the data and the institutional setting, and Section 4 sets out the design.
~~~


---

### 2. Related literature and hypotheses

**Verdict.** The section is organized by theme (theory; classic evidence; band changes and investor data; overnight returns; multiple testing; gap and hypotheses), which passes Check 1.6. Four of the five paragraphs open with a topic sentence. The "Classic evidence" paragraph opens on a citation instead. Two paragraphs read as citation lists ("X find …, Y find …, Z find …"). Each paragraph ends with the same "none splits the next-day return …" gap line, which reads as a formula. Links to the design are present and useful: Huang et al. timing, Petersen clusters, Gutierrez–Kelley weekly frequency, and the H1 benchmark. Other problems: false agency in "Band changes … now show" and in "which says nothing about returns"; "tend to" hedges; and FDR is spelled out after its definition in Section 1. H3 and H4 are loosely worded: "If only the limit blocks trading" is ambiguous, and H4 says "does not earn the gap" while the paper tests the return from the open to day *d*+5.

**Scores:** Directness 7, Rhythm 6, Trust 8, Authenticity 6, Density 7 = **34/50 (revise)**

**L1.** Add a topic sentence to the "Classic evidence" paragraph.
~~~old
**Classic evidence on price-limit performance.** Kim and Rhee (1997) organize
~~~
~~~new
**Classic evidence on price-limit performance.** Early empirical work infers the costs of limits from volatility and serial correlation across days. Kim and Rhee (1997) organize
~~~

**L2.** After L1, the closing sentence repeats the new topic sentence. Keep only the gap.
~~~old
These studies infer delay from volatility and serial correlation across days; none splits the next-day return into the overnight gap and the session that follows.
~~~
~~~new
None of these studies splits the next-day return into the overnight gap and the session that follows.
~~~

**L3.** Passive voice ("is corrected") and a wordy link.
~~~old
Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits is corrected during the following trading day, which is the timing pattern we examine on HOSE.
~~~
~~~new
Huang et al. (2001) report for Taiwan that the overnight overreaction after limit hits reverses during the following trading day, the timing pattern we test on HOSE.
~~~

**L4.** False agency and the adverb "now" in the topic sentence.
~~~old
Band changes and investor-level data now show what limits do to markets and traders.
~~~
~~~new
Recent studies use band changes and investor-level data to measure how limits affect market quality and trader behavior.
~~~

**L5.** Hedge ("tend to").
~~~old
show that large investors tend to buy on the day a stock hits the 10% upper limit
~~~
~~~new
show that large investors buy on the day a stock hits the 10% upper limit
~~~

**L6.** False agency and a dismissive tone.
~~~old
Liang and Hu (2025) show that a forecasting model predicts a share of limit hits, which says nothing about returns after the hit.
~~~
~~~new
Liang and Hu (2025) forecast limit hits but leave returns after the hit unexamined.
~~~

**L7.** The gap line repeats L2 almost word for word. Vary it and link it to the design.
~~~old
None of these studies reports the next-day return after a limit close split into its overnight and intraday parts.
~~~
~~~new
These designs compare markets or periods; ours conditions on individual limit closes within one band regime.
~~~

**L8.** The paragraph's topic sentence already says the returns differ.
~~~old
Kelly and Clark (2011) document that overnight and intraday returns differ for index funds.
~~~
~~~new
Kelly and Clark (2011) document the split for index funds.
~~~

**L9.** "Them" has no clear referent.
~~~old
Bogousslavsky (2021) links them to differences in margin and lending costs
~~~
~~~new
Bogousslavsky (2021) links the split to differences in margin and lending costs
~~~

**L10.** Section 1 already defines FDR, so use the abbreviation (Check 6.4).
~~~old
Harvey and Liu (2020) tie the hurdle to a chosen false-discovery rate
~~~
~~~new
Harvey and Liu (2020) tie the hurdle to a chosen FDR
~~~

**L11.** Tighten the gap sentence and the H3 and H4 wording. H4 must match the test (open to day 5).
~~~old
The reviewed studies document volatility, liquidity, and long-run effects of limits and the overnight-intraday split for all stocks, but none combines the two in a market with call auctions or controls for multiple testing. None uses the 2025 platform change.
~~~
~~~new
The reviewed studies document the volatility, liquidity, and long-run effects of limits, and the overnight-intraday split for all stocks. None combines the two in a market with call auctions, controls for multiple testing, or uses the 2025 platform change.
~~~

**L12.**
~~~old
If only the limit blocks trading, the gap after a limit close exceeds the gap after moves that come close to the limit (H3). An investor who buys at the next open does not earn the gap (H4).
~~~
~~~new
If the limit itself drives the gap, the gap after a limit close exceeds the gap after moves of similar size that stop short of the limit (H3). An investor who buys at the next open earns no positive abnormal return through the fifth trading day (H4).
~~~


---

### 3. Data and institutional setting

**Verdict.** The section is concrete and complete. Problems: one first sentence is overloaded, with the date at the end and the abbreviation "VCI" placed before its full term (Check 6.3 INFO). A hard-coded data count (519) should be an inline R value. There is a stray comma before the HSC citation. "Dollar volume" is measured in dong, so it needs a definition. The definition of the market return and abnormal return repeats Equation (2) in Section 4. The weight-timing remark about Tables 1–4 belongs in Section 4, and it appears before Table 1 does. The paragraph ends on a punchy fragment.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 7 = **37/50**

**D1.** Reorder the sentence and give the full term before the abbreviation.
~~~old
We obtained daily open, high, low, close, and volume series for every stock on the HOSE listing with the vnstock Python library (version 4.0.4), which retrieves them from its VCI source (Vietcap Securities Joint Stock Company), on 24 September 2026.
~~~
~~~new
On 24 September 2026, we downloaded daily open, high, low, close, and volume series for all stocks on the HOSE listing with the vnstock Python library (version 4.0.4), which draws them from Vietcap Securities Joint Stock Company (VCI).
~~~

**D2.** Hard-coded data number. `c26(4)` holds 519 in `C26_sample_description.csv`.
~~~old
and we use the 519 trading days from 21 August 2024.
~~~
~~~new
and we use the `r c26(4)` trading days from 21 August 2024.
~~~

**D3.** Put the survivorship fact next to the listing it describes (part 1 of 2).
~~~old
A listing file from the same source and date (`r fi(c26(2))` rows, all instrument types) defines the universe.
~~~
~~~new
A listing file from the same source and date (`r fi(c26(2))` rows, all instrument types) defines the universe and omits stocks delisted before that date.
~~~

**D4.** Part 2 of 2: delete the old sentence. Note the leading space.
~~~old
 The listing file excludes stocks delisted before 24 September 2026.
~~~
~~~new

~~~

**D5.** "Returns are close-to-close" stands alone as a fragment. Fold it in, and define dollar volume in dong.
~~~old
which yields `r fi(nsd)` stock-days. Returns are close-to-close. The mean daily return is
~~~
~~~new
which yields `r fi(nsd)` stock-days. The mean daily close-to-close return is
~~~

**D6.**
~~~old
Liquidity is skewed: the median stock-day with a price has a dollar volume of
~~~
~~~new
Liquidity is skewed: dollar volume (price times shares traded, in dong) has a median per stock-day of
~~~

**D7.** Remove the duplicate market-return definition. Edit M3 moves the weight-timing remark into Section 4. Note the leading space.
~~~old
 The market return is the dollar-volume-weighted return of all stocks, with weights from the trailing 60-day average dollar volume, and abnormal returns are stock returns minus the market return over the same interval. Table 1 uses weights through day *d*+1, and Tables 2 to 4 lag the weights to day *d*.
~~~
~~~new

~~~

**D8.** Stray comma before the citation.
~~~old
which is the previous close on normal trading days, (Ho Chi Minh City Securities Corporation [HSC], 2025).
~~~
~~~new
which is the previous close on normal trading days (Ho Chi Minh City Securities Corporation [HSC], 2025).
~~~

**D9.** End the paragraph on content, not a one-liner.
~~~old
against `r f(pu("6.0% to 6.5%"),2)`% between +6.0% and +6.5%. The pile-up fits a 7% band.
~~~
~~~new
against `r f(pu("6.0% to 6.5%"),2)`% between +6.0% and +6.5%, a pile-up consistent with a 7% band.
~~~


---

### 4. Design

**Verdict.** The structure is good: labeled run-in paragraphs; every display is introduced by a sentence that flows into it; most equations are followed by a "where" clause; and the paper discloses its plan deviations. The section fails Check 2 (notation) in several places:

- **Clashes (ERROR, Check 2.3):** $\tau$ means tick size (Eq. 3) and week (Eq. 7). $G$ means the overnight gap $G_i$ (Eq. 5) and the number of clusters (Eq. 6 and the Table 1 caption). $i$ means a stock (Eqs. 1–3) and an event (Eqs. 4–6, regression). $j$ means a stock (Eq. 2) and a rank (Eq. 8). $k$ means a stock (Eq. 2), a day (Eq. 4) and a rank (Eq. 8). The fix: tick size becomes $\delta$; the gap and intraday returns become $\mathit{GAP}_{i,d}$ and $\mathit{INTRA}_{i,d}$; events take the index $e$; ranks become $r$ and $s$; the stock index in the Eq. 2 denominator becomes $l$. $\tau$ stays the week index and $G$ stays the cluster count, the standard use.
- **Undefined (ERROR, Check 2.2):** $G$ (the text only says "*g* indexes clusters"), $k$ in Eq. 4, $x_{i,\tau}$, $n_\tau$, $\Phi^{-1}$, $a_\tau$, $\widehat{\text{SE}}$; the abbreviations AR, CAR and MDE; and the quintile spreads reported in Section 5. The constant 2.8 needs an explanation.
- **Multi-letter symbols (ERROR, Check 2.7):** `AR_{i}` and `CAR_{i}` render as products of letters. Use `\mathit{}`.
- **Italics (WARN, Check 2.4):** symbols appear as Markdown italics (`*i*`, `*j*`, `*g*`, `*N*`, `*d*`) in some places and as math (`$i$`) in others. In Word these render in two different fonts (body italic and Cambria Math). Rule: in Section 4, write every defined symbol as `$...$`. In Sections 5–8 and in table text, keep `*d*+1` for day labels, since it is stable across tables. Keep `*t*`, `*p*` and `|*t*|` as italic statistic labels.
- **Equation punctuation (ERROR, Check 2.5):** Eq. (4) ends with a period, but a "where" clause should follow it (M5).
- **Unreferenced equations (INFO, Check 2.10):** the text never cites (1), (2), (5), (6), (7) or (8). Edits R2, R8 and R13 cite (5), (7) and (8) in Section 5. (1), (2) and (6) can keep their numbers for the reader.
- **Number format (INFO):** the event thresholds appear as decimals in equations (0.065, 1.07, 0.93) and as percentages in prose (6.5%, 7%). This is acceptable; keep it consistent.
- **BH wording (WARN):** "adjusted *p*-value at a 5% false-discovery rate" mixes the adjusted value with the threshold. FDR is also introduced a second time here (Check 6.4 ERROR).
- **Symbol subscripts (INFO):** write `m_{\max}` as `m_{\text{max}}`.

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 6 = **35/50**

**M1.** Symbols in math mode. "Prices" makes the list concrete.
~~~old
For stock *i* on day *d*, let $C_{i,d}$, $O_{i,d}$, $H_{i,d}$, and $L_{i,d}$ denote the close, open, high, and low, and let $R_{i,d}$ denote the close-to-close return,
~~~
~~~new
For stock $i$ on trading day $d$, let $C_{i,d}$, $O_{i,d}$, $H_{i,d}$, and $L_{i,d}$ denote the close, open, high, and low prices, and let $R_{i,d}$ denote the close-to-close return,
~~~

**M2.** "A ceiling event is an event day" is circular. This edit also defines the "event window" that Sections 1 and 6 use. **[verify]**: `C13_universe_counts.csv` gives "days 61 to nd-5".
~~~old
A ceiling event is an event day *d* with $R_{i,d} \geq 0.065$ and $C_{i,d} = H_{i,d}$. A floor event has $R_{i,d} \leq -0.065$ and $C_{i,d} = L_{i,d}$.
~~~
~~~new
Stock $i$ has a ceiling event on day $d$ if $R_{i,d} \geq 0.065$ and $C_{i,d} = H_{i,d}$, and a floor event if $R_{i,d} \leq -0.065$ and $C_{i,d} = L_{i,d}$. The event window runs from day 61 of the sample, once a 60-day volume history exists, to five days before its end.
~~~

**M3.** Index clash: $k$ is a stock here but a day in Eq. 4.
~~~old
w_{j,d} = \frac{\overline{V}_{j,d}}{\sum_{k} \overline{V}_{k,d}}, \qquad (2)$$
~~~
~~~new
w_{j,d} = \frac{\overline{V}_{j,d}}{\sum_{l} \overline{V}_{l,d}}, \qquad (2)$$
~~~

**M4.** Define the indices and dollar volume. Move the weight-timing and abnormal-return definitions here from Section 3 (D7). Make the exact-hit sentence precise. **[verify]**: whether the 60-day window ends on day $d$ or on $d-1$ (`47_da_response.R` uses `adv[t - 60, ]`).
~~~old
where $\overline{V}_{j,d}$ is the trailing 60-day average dollar volume of stock *j*. An exact limit hit has a close equal to the limit price,
~~~
~~~new
where $j$ and $l$ run over all stocks, dollar volume is price times shares traded (in dong), and $\overline{V}_{j,d}$ is the average dollar volume of stock $j$ over the 60 trading days through day $d$. Abnormal returns subtract the market return over the same interval. Table 1 uses Equation (2) at day $d+1$; Tables 2 to 4 hold the weights at $w_{j,d}$, known at the event close. An exact limit hit is a close $C_{i,d}$ equal to the limit price,
~~~

**M5.** Tick clash: $\tau$ becomes $\delta$.
~~~old
$$P^{\text{ceiling}}_{i,d} = \left\lfloor \frac{1.07\, C_{i,d-1}}{\tau} \right\rfloor \tau, \qquad P^{\text{floor}}_{i,d} = \left\lceil \frac{0.93\, C_{i,d-1}}{\tau} \right\rceil \tau, \qquad (3)$$
~~~
~~~new
$$P^{\text{ceiling}}_{i,d} = \left\lfloor \frac{1.07\, C_{i,d-1}}{\delta} \right\rfloor \delta, \qquad P^{\text{floor}}_{i,d} = \left\lceil \frac{0.93\, C_{i,d-1}}{\delta} \right\rceil \delta, \qquad (3)$$
~~~

**M6.**
~~~old
where the tick $\tau$ is 0.01, 0.05, or 0.10 thousand dong for reference prices below 10, from 10 to below 50, and from 50 thousand dong upward.
~~~
~~~new
where $\lfloor \cdot \rfloor$ and $\lceil \cdot \rceil$ round down and up, and the tick size $\delta$ is 0.01, 0.05, or 0.10 thousand dong for reference prices $C_{i,d-1}$ below 10, from 10 to below 50, and from 50 thousand dong upward.
~~~

**M7.** Define AR and CAR at first use. "Market-adjusted" and "abnormal" were both in use; settle on "abnormal" as defined.
~~~old
**Outcomes.** The market-adjusted return on day *d*+1 and the cumulative return over days *d*+1 to *d*+5 are
~~~
~~~new
**Outcomes.** For an event of stock $i$ on day $d$, the abnormal return (AR) on day $d+1$ and the cumulative abnormal return (CAR) over days $d+1$ to $d+5$ are
~~~

**M8.** Use `\mathit` for the multi-letter symbols, give the event-level subscript $(i,d)$, and end with a comma so the "where" clause follows. (Optional: the product difference is a buy-and-hold abnormal return. Consider "BHAR" if the journal's readers expect that term.)
~~~old
$$AR_{i} = R_{i,d+1} - R^{m}_{d+1}, \qquad CAR_{i} = \prod_{k=1}^{5} \left(1 + R_{i,d+k}\right) - \prod_{k=1}^{5} \left(1 + R^{m}_{d+k}\right). \qquad (4)$$
~~~
~~~new
$$\mathit{AR}_{i,d} = R_{i,d+1} - R^{m}_{d+1}, \qquad \mathit{CAR}_{i,d} = \prod_{k=1}^{5} \left(1 + R_{i,d+k}\right) - \prod_{k=1}^{5} \left(1 + R^{m}_{d+k}\right), \qquad (4)$$
~~~

**M9.** Define $k$, and name the gap and intraday symbols. This removes the $G$ clash.
~~~old
We split the day-*d*+1 return into the overnight gap and the intraday return,
~~~
~~~new
where $k$ counts trading days after the event. We split the day-$d+1$ return into the overnight gap $\mathit{GAP}_{i,d}$ and the intraday return $\mathit{INTRA}_{i,d}$,
~~~

**M10.**
~~~old
$$G_{i} = \frac{O_{i,d+1}}{C_{i,d}} - 1, \qquad I_{i} = \frac{C_{i,d+1}}{O_{i,d+1}} - 1, \qquad 1 + R_{i,d+1} = (1 + G_{i})(1 + I_{i}), \qquad (5)$$
~~~
~~~new
$$\mathit{GAP}_{i,d} = \frac{O_{i,d+1}}{C_{i,d}} - 1, \qquad \mathit{INTRA}_{i,d} = \frac{C_{i,d+1}}{O_{i,d+1}} - 1, \qquad 1 + R_{i,d+1} = (1 + \mathit{GAP}_{i,d})(1 + \mathit{INTRA}_{i,d}), \qquad (5)$$
~~~

**M11.** Active voice; remove "can"; math-mode day.
~~~old
The return a buyer at the next open can earn through day *d*+5 is $C_{i,d+5}/O_{i,d+1} - 1$, again less its market counterpart.
~~~
~~~new
A buyer at the next open earns $C_{i,d+5}/O_{i,d+1} - 1$ through day $d+5$, again less its market counterpart.
~~~

**M12.** Give $R^{m}$ its subscript and name the sorting variable.
~~~old
The control benchmark replaces $R^{m}$ with the mean return of non-event stocks (absolute return below 6.5%) on the same date and in the same tercile of trailing dollar volume.
~~~
~~~new
The control benchmark replaces $R^{m}_{d}$ with the mean return of non-event stocks (absolute return below 6.5%) on the same date and in the same tercile of $\overline{V}_{j,d}$.
~~~

**M13.** The event index becomes $e$ (removes the $i$ clash).
~~~old
For a sample of *N* events with outcome $y_i$, the mean is $\overline{y} = N^{-1}\sum_i y_i$, and the cluster-robust variance is
~~~
~~~new
For a sample of $N$ events $e = 1, \dots, N$ with outcome $y_e$ (any return defined above), the mean is $\overline{y} = N^{-1}\sum_{e} y_e$, and the cluster-robust variance is
~~~

**M14.**
~~~old
\sum_{i \in g} (y_i - \overline{y})
~~~
~~~new
\sum_{e \in g} (y_e - \overline{y})
~~~

**M15.** Define $G$, and repeat "by" so the list reads in parallel.
~~~old
where *g* indexes clusters. We cluster by event date (without the $G/(G-1)$ factor), calendar week, and 10-day block,
~~~
~~~new
where $g = 1, \dots, G$ indexes clusters. We cluster by event date (without the factor $G/(G-1)$), by calendar week, and by 10-day block,
~~~

**M16.** Event index in the comparison regression.
~~~old
we regress $y_i = \alpha + \beta D_i + u_i$, where $D_i = 1$ for limit closes and $D_i = 0$ for the comparison group, and we cluster the standard error of $\hat{\beta}$ by date.
~~~
~~~new
we regress $y_e = \alpha + \beta D_e + u_e$, where $D_e = 1$ for limit closes and $D_e = 0$ for the comparison group, and cluster the standard error of $\hat{\beta}$ by date.
~~~

**M17.** Define $x$, $n_\tau$ and $\Phi^{-1}$. Replace the hard-coded 79 with $T$. Put the Fama–MacBeth citation where the method appears.
~~~old
**Characteristics.** At the end of each of 79 weeks $\tau$, we rank-normalize each characteristic across stocks, $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, and regress the next five days' abnormal return on it,
~~~
~~~new
**Characteristics.** At the end of each week $\tau = 1, \dots, T$, with $T = 79$, we rank-normalize each characteristic $x_{i,\tau}$ across the $n_\tau$ stocks with data, $z_{i,\tau} = \Phi^{-1}\!\left((\operatorname{rank}(x_{i,\tau}) - 0.5)/n_\tau\right)$, where $\Phi^{-1}$ is the inverse standard normal distribution function, and run Fama and MacBeth (1973) regressions of the abnormal return $y_{i,\tau}$ over the next five trading days on $z_{i,\tau}$,
~~~

**M18.**
~~~old
\hat{\gamma} = \frac{1}{79} \sum_{\tau} \hat{\gamma}_{\tau}
~~~
~~~new
\hat{\gamma} = \frac{1}{T} \sum_{\tau=1}^{T} \hat{\gamma}_{\tau}
~~~

**M19.**
~~~old
with the Newey and West (1987) *t*-statistic of $\hat{\gamma}$ computed with four lags (Fama & MacBeth, 1973).
~~~
~~~new
where $a_\tau$ is the weekly intercept, and we compute the *t*-statistic of $\hat{\gamma}$ with Newey and West (1987) standard errors and four lags.
~~~

**M20.** Define the quintile spreads used in Section 5, the MDE abbreviation, the 2.8 constant and SE. **[verify]**: the quintile construction against `40_zoo.R`.
~~~old
Lookbacks reach up to 115 days. The minimum detectable slope at 80% power and a 5% two-sided level is $\text{MDE} = 2.8 \times \widehat{\text{SE}}(\hat{\gamma})$.
~~~
~~~new
Lookbacks reach up to 115 trading days. We also report the long–short return spread between the extreme quintiles of each characteristic, before and after a cost of 25 basis points per unit of traded value. The minimum detectable effect (MDE) on $\hat{\gamma}$ at 80% power and a 5% two-sided level is $\text{MDE} = (1.96 + 0.84)\, \widehat{\text{SE}}(\hat{\gamma}) \approx 2.8\, \widehat{\text{SE}}(\hat{\gamma})$, where $\widehat{\text{SE}}$ is the Newey–West standard error.
~~~

**M21.** Section 1 already defines FDR. Separate the adjusted value from the threshold, and rename the rank indices.
~~~old
The Benjamini–Hochberg (BH) adjusted *p*-value at a 5% false-discovery rate (FDR) is
~~~
~~~new
For rank $r = 1, \dots, m$, the Benjamini–Hochberg (BH) adjusted *p*-value is
~~~

**M22.**
~~~old
\tilde{p}_{(k)} = \min_{j \geq k} \left\{ \min\!\left( 1, \frac{m}{j}\, p_{(j)} \right) \right\}
~~~
~~~new
\tilde{p}_{(r)} = \min_{s \geq r} \left\{ \min\!\left( 1, \frac{m}{s}\, p_{(s)} \right) \right\}
~~~

**M23.** The survival rule packs three conditions into one sentence. Make them parallel, and state that the threshold is the FDR level.
~~~old
A test survives if $\tilde{p} < 0.05$, the sign in the discovery half (the first 39 weeks, or the first half of event dates) agrees with the full sample, and the confirmation-half |*t*| exceeds 1.96.
~~~
~~~new
A test survives if three conditions hold: $\tilde{p} < 0.05$, which controls the FDR at 5%; the sign in the discovery half (the first 39 weeks for characteristics, the first half of event dates for events) agrees with the full sample; and the confirmation-half |*t*| exceeds 1.96.
~~~

**M24.** The sentence reads backward ("the largest number of tests that all four survive").
~~~old
The largest number of tests that all four event tests survive under a Bonferroni correction is $m_{\max} = \lfloor 0.05 / p_{\max} \rfloor$, where $p_{\max}$ is the largest event-test *p*-value.
~~~
~~~new
Under a Bonferroni correction at 5%, all four event tests survive in families of up to $m_{\text{max}} = \lfloor 0.05 / p_{\text{max}} \rfloor$ tests, where $p_{\text{max}}$ is the largest event-test *p*-value.
~~~

**M25.** Clearer subject. The "Analysis plan" paragraph is a necessary integrity disclosure, so keep it.
~~~old
A version-control time stamp predates the first analysis code, but no external registry holds the plan,
~~~
~~~new
A version-control time stamp shows that the plan predates the first analysis code, but no external registry holds it,
~~~


---

### 5. Results (with Tables 1–4 and Figures 1–2)

**Verdict.** All six floats are called out in the text before they appear: Figure 1 → Table 1 → Table 2 → Figure 2 → Table 3 → Table 4. The numbers in the text match the tables. Problems: this section has the most repetition and the lowest density. It repeats the literature comparisons that Table 5 and Section 6 make (Berkman, Lou, Akbas, Huang, Chen 2019, Qiao–Dam), including the tautology "so the ceiling gap is not the negative overnight pattern they report". It states "no comparable construction" here and again in Section 6. It states the magnet-effect caveat here, in Section 6 and in Table 5. It puts the 3–5% comparison in the "three readings" paragraph when it belongs with Table 3. Other problems: false agency ("the evidence shows", "the comparison makes no claim", "the split shows"); throat-clearing ("Taken together"); "This clustering is why" (narrator voice); a three-item list of explanations, one of them speculative ("short selling is costly"); and "e" notation for *p*-values (2.6e-06). The summary paragraph overclaims: "survives alternative benchmarks" and "appears in each measure" contradict the paper's own statement that the floor effect depends on the benchmark and that the floor intraday return is not significant. The Table 4 call-out is a one-sentence paragraph with no content. The captions of Table 1 and Figures 1–2 lack Oxford commas. Figure 1's axis uses undefined code labels. Table 5's "None of our 22 characteristics reaches 1.96" is false for the confirmation half: in Figure 1, CSSPREAD and RANGEVOL fall below −1.96. Because Table 5 is the Section 6 table, its edit is listed under Section 6.

**Scores:** Directness 7, Rhythm 5, Trust 7, Authenticity 6, Density 5 = **30/50 (revise)**

**R1.** Narrator voice ("This clustering is why").
~~~old
so events cluster in market episodes with several limit closes on the same day. This clustering is why we report standard errors that allow for dependence across dates, weeks, and stocks.
~~~
~~~new
so limit closes cluster in market episodes, and we report standard errors that allow for dependence across dates, weeks, and stocks.
~~~

**R2.** Cite the equation and name the control precisely.
~~~old
Figure 1 plots the *t*-statistics of the 22 characteristics: none reaches |*t*| = 3, and none survives the family-wide control.
~~~
~~~new
Figure 1 plots the *t*-statistics of the 22 slopes $\hat{\gamma}$ in Equation (7): none reaches |*t*| = 3, and none survives the BH control.
~~~

**R3.** Oxford comma (the paper uses it elsewhere).
~~~old
idiosyncratic volatility `r f(Z$t_nw[Z$characteristic=="IVOL"],2)` and MAX
~~~
~~~new
idiosyncratic volatility `r f(Z$t_nw[Z$characteristic=="IVOL"],2)`, and MAX
~~~

**R4.** Use the abbreviation defined in M20.
~~~old
Power is limited: with 79 cross-sections the minimum detectable slope at 80% power is
~~~
~~~new
Power is limited: with 79 weekly cross-sections, the MDE at 80% power is
~~~

**R5.** "Excludes … excluding" repeats.
~~~old
and excluding the least liquid 20% of stocks leaves the largest |*t*| at
~~~
~~~new
and dropping the least liquid 20% of stocks leaves the largest |*t*| at
~~~

**R6.** Throat-clearing ("The result is in line with") and the adverb "even".
~~~old
The result is in line with the multiple-testing literature: the hurdles of Harvey et al. (2016) and Chordia et al. (2020) and the replication failures that Hou et al. (2020) report lead us to expect few survivors, and no characteristic here reaches even 1.96 in the full sample.
~~~
~~~new
The hurdles of Harvey et al. (2016) and Chordia et al. (2020) and the replication failures in Hou et al. (2020) predict few survivors; here no characteristic reaches 1.96 in the full sample.
~~~

**R7.** Cut the three-item list to the two explanations the paper can support. Fix the false agency ("Our data cannot tell").
~~~old
Three features of this market can produce it. The sample is short, so a premium of a tenth of a percentage point per week stays invisible. Daily limits censor the highs and lows that several characteristics use, which weakens range-based measures. Slow-moving signals such as momentum and volatility may also carry little information in a market where short selling is costly and arbitrage capital is thin. Our data cannot tell these explanations apart, and we draw no conclusion about market efficiency from the null.
~~~
~~~new
Two features of this market can produce the null. The sample is short, so a premium of a tenth of a percentage point per week stays below the MDE, and daily limits censor the highs and lows that range-based characteristics use. We cannot tell these explanations apart and draw no conclusion about market efficiency from the null.
~~~

**R8.** Cite Equation (8).
~~~old
All four tests survive the BH control (adjusted *p*-values from
~~~
~~~new
All four tests survive the BH control (Equation (8); adjusted *p*-values from
~~~

**R9.** False agency ("The evidence shows").
~~~old
The evidence shows a one-day effect after ceiling closes and a one-day effect with some later drift after floor closes.
~~~
~~~new
Ceiling closes carry a one-day effect; floor closes carry a one-day effect plus some later drift.
~~~

**R10.** "None of these studies" has no clear referent (only one study is named). Section 6 makes the same point. Delete the sentence; note the trailing space in the old string.
~~~old
None of these studies reports a next-day abnormal return of comparable construction, so we cannot compare magnitudes, and Section 6 compares them in qualitative terms. 
~~~
~~~new

~~~

**R11.** The closing transition loses the agent. Point to the table that answers the question.
~~~old
They leave open when in the day that information arrives (H2).
~~~
~~~new
Table 2 tests when in the day that information arrives (H2).
~~~

**R12.** Cite Equation (5).
~~~old
Table 2 decomposes the next-day return.
~~~
~~~new
Table 2 decomposes the next-day return as in Equation (5).
~~~

**R13.** False agency ("the session … undoes").
~~~old
and the session that follows undoes part of the move, which suggests that part of the opening price reflects demand that does not persist.
~~~
~~~new
and traders reverse part of the move during the session, which suggests that part of the opening price reflects transient demand.
~~~

**R14.** Delete the comparisons repeated from Table 5 and Section 6, including the tautology. Keep one pointer.
~~~old
The pattern has the same signs as the overnight-gain-then-intraday-reversal that Berkman et al. (2012) find in U.S. stocks and the cross-period reversal that Lou et al. (2019) and Akbas et al. (2022) document, and it matches the correction of overnight overreaction on the following trading day that Huang et al. (2001) report for Taiwan. It also matches the account-level finding of Chen et al. (2019) that large Shenzhen investors who buy on the limit day sell on the next day, which would produce an intraday reversal after a high opening. The overnight return after a ceiling close is positive, in contrast to the negative average overnight return that Qiao and Dam (2020) find for all Chinese stocks under the T+1 rule, so the ceiling gap is not the negative overnight pattern they report for Chinese stocks.
~~~
~~~new
The signs match the overnight gain and intraday reversal in Berkman et al. (2012) and Huang et al. (2001); Table 5 sets out the other comparisons.
~~~

**R15.** "It" is ambiguous, and the qualifier "for ceilings" is misplaced (the floor gap is also significant in both halves and on locked days; see Table 2).
~~~old
It appears in both halves of the sample, in each liquidity tercile for ceilings (the gap is `r f(c16("Ceiling liquidity tercile 3","gap_mkt"),2)`% in the most liquid tercile), and on days when the stock stayed locked at one price from open to close.
~~~
~~~new
The gap appears in both halves of the sample, on days when the stock stayed locked at one price from open to close, and, for ceilings, in each liquidity tercile (`r f(c16("Ceiling liquidity tercile 3","gap_mkt"),2)`% in the most liquid).
~~~

**R16.** Put the actor first.
~~~old
The close-to-close continuation is not available to an outside buyer. A buyer who wants a stock at its ceiling joins a queue at the close, so the first price available to an outside buyer is the next open, which already contains the gap.
~~~
~~~new
An outside buyer cannot capture the close-to-close continuation. A buyer who wants a stock at its ceiling joins a queue at the close, so the first price such a buyer can obtain is the next open, which already contains the gap.
~~~

**R17.** Move the 3–5% robustness result into the Table 3 paragraph (part 1 of 2).
~~~old
so a strong close does not explain the contrast, which supports H3.
~~~
~~~new
so a strong close does not explain the contrast, which supports H3. Comparisons with 3% to 5% moves give the same result: the ceiling gap exceeds that of 3% to 5% risers by `r f(c17("ceiling vs 3-5% up","gap_mkt","diff_pct"),2)` percentage points, and the floor gap falls short of that of 3% to 5% fallers by `r f(abs(c17("floor vs 3-5% down","gap_mkt","diff_pct")),2)` points.
~~~

**R18.** Part 2 of 2: delete the old sentence from the "three readings" paragraph. Note the leading space.
~~~old
 Comparisons with 3% to 5% moves give the same result: the ceiling gap exceeds that of 3% to 5% risers by `r f(c17("ceiling vs 3-5% up","gap_mkt","diff_pct"),2)` percentage points and the floor gap falls short of that of 3% to 5% fallers by `r f(abs(c17("floor vs 3-5% down","gap_mkt","diff_pct")),2)` points (Table 3).
~~~
~~~new

~~~

**R19.** False agency ("It makes no … claim"). Oxford comma.
~~~old
It makes no regression-discontinuity claim, because it has no bandwidth choice, manipulation test or covariate balance, and stocks that reach the limit may differ in news content.
~~~
~~~new
We make no regression-discontinuity claim: the design has no bandwidth choice, manipulation test, or covariate-balance check, and stocks that reach the limit may differ in news content.
~~~

**R20.** Passive voice ("are selected", "are followed by"); hyphen chain.
~~~old
(2) Stocks that reach a limit are selected on news and retail attention, which persist overnight and are followed by the overnight-gain-then-reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit.
~~~
~~~new
(2) Stocks that reach a limit carry news and retail attention, which persist overnight and produce the overnight gain and intraday reversal of attention-grabbing stocks (Berkman et al., 2012), with or without a limit.
~~~

**R21.** Adverb "likely"; name the proxies.
~~~old
The gap is larger where attention and news are likely stronger,
~~~
~~~new
The gap is larger where the attention and news proxies are higher,
~~~

**R22.** Section 6 and Table 5 repeat the magnet caveat. Shorten it here (Section 6 cuts its copy in S3). Remove "only".
~~~old
The comparison also bears on the magnet effect. Cho et al. (2003) and Chen et al. (2024) predict that prices accelerate toward a limit on the limit day, and our data lack the intraday prices needed to test that. The rise of the gap at the limit relative to near-limit moves shows only that the close at the limit carries information that a close just below the limit does not.
~~~
~~~new
Cho et al. (2003) and Chen et al. (2024) predict that prices accelerate toward a limit on the limit day (the magnet effect); a test needs intraday prices, which we lack. The larger gap at the limit shows that a close at the limit carries information that a close just below it lacks.
~~~

**R23.** The one-sentence Table 4 call-out has no content. Give it the facts the split rests on.
~~~old
Table 4 splits the events at the move to the KRX platform.
~~~
~~~new
Table 4 splits the events at 5 May 2025, when HOSE moved to the KRX platform and at-the-open and at-the-close orders lost their auction priority.
~~~

**R24.** A "not X" contrast plus a vague "different margin".
~~~old
Our split follows a change in auction priority, not a change in the band, so it speaks to a different margin.
~~~
~~~new
Our split follows a change in auction priority with the band held at 7%.
~~~

**R25.** False agency ("The split shows").
~~~old
The split shows the main pattern on both sides, with differences in detail, and cannot isolate an effect of the auction rules.
~~~
~~~new
Both periods show the main pattern, and the split cannot isolate an effect of the auction rules.
~~~

**R26.** "Project-wide" mentions the internal process. Point to the formula in Section 4.
~~~old
To bound the effect of a larger project-wide search, we compute how many tests the four event tests could absorb.
~~~
~~~new
To bound the effect of a wider search, we compute $m_{\text{max}}$ from Section 4.
~~~

**R27.** The summary paragraph opens with throat-clearing, overclaims ("each measure", "survives alternative benchmarks" for floors) and repeats Section 6.
~~~old
Taken together, the results support H1 to H4. The limit effect appears in each measure, survives alternative benchmarks, clusters, and definitions, and grows as the close approaches the limit. It differs between ceilings and floors in the details: the ceiling effect is a one-day gap with a partial reversal, and the floor effect combines a gap with drift that appears only before the 2025 platform change. The effect is not available to an outside buyer at the quoted next open. The evidence does not settle why the gap arises, and Section 6 returns to that question.
~~~
~~~new
The results support H1 to H4. The ceiling effect survives alternative benchmarks, clusters, and definitions, grows as the close approaches the limit, and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture. The floor effect combines a gap with drift that appears only before the 2025 platform change, and its size depends on the benchmark. Section 6 weighs the explanations.
~~~

**R-T1.** Oxford commas in the Table 1 caption (a string inside the code chunk, so the code logic does not change).
~~~old
*t* (date), *t* (week) and *t* (10-day) use clusters by event date, calendar week and 10-day block;
~~~
~~~new
*t* (date), *t* (week), and *t* (10-day) use clusters by event date, calendar week, and 10-day block;
~~~

**R-F1.** The Figure 1 caption needs an Oxford comma and a key to the axis labels (Check 4.3/6). **[verify]**: the mapping against `40_zoo.R`.
~~~old
in the full sample, the discovery half and the confirmation half. Dashed lines mark
~~~
~~~new
in the full sample, the discovery half (first 39 weeks), and the confirmation half. Labels: REV1W and REV1M, 5-day and 20-day returns; MOM3M and MOM6M, 3- and 6-month momentum; IMOM, idiosyncratic momentum; VOL and IVOL, total and idiosyncratic volatility; BETA, market beta; DOWNVOL, downside deviation; RANGEVOL, Parkinson range volatility; MAX and MIN, maximum and minimum daily return; SKEW and KURT, skewness and kurtosis; AMIHUD, Amihud illiquidity; LNDVOL, log dollar volume; DVOLCHG and TURNCHG, dollar-volume and volume ratios; CSSPREAD, Corwin–Schultz spread; OVERNIGHT and INTRADAY, mean overnight and intraday returns; LIMITFREQ, frequency of moves of 6.5% or more. Dashed lines mark
~~~

**R-F2.** The Figure 2 caption does not define the bins, and "closes at the 7% limit" misstates the event rule (events are rule-based closes of 6.5% or more at the high or low; see `C5_rd_bins.csv`). Add the Oxford commas.
~~~old
split into overnight gap, intraday return and close-to-close return. Circles are interior bins, triangles are closes at the 7% limit and squares are moves beyond 6.5% that did not close at the limit.
~~~
~~~new
split into overnight gap, intraday return, and close-to-close return. Circles are 1-percentage-point bins of day-*d* returns inside the band, triangles are ceiling and floor events (Section 4), and squares are other moves of 6.5% to 10% in absolute value.
~~~


**Non-edit notes for Section 5**
- [INFO] The *p*-values print in "e" notation (`2.6e-06`, `7.3e-05`). For a journal, prefer 2.6 × 10⁻⁶. This needs a display-only helper, for example `sci <- function(x) sub("e-0?(\\d+)", " × 10^−\\1^", formatC(x, format = "e", digits = 1))` in the setup chunk, with `formatC(..., format = "e", digits = 1)` replaced by `sci(...)` at the three call sites. The values stay the same.
- [WARN, Check 3.3] "the effect grows as the close approaches the limit" (exact 2.77% vs near 1.67%) and "the ceiling gap rises with day-*d* volume" (terciles) have no test of the difference or trend. Report the difference *t* or soften the verb to "is larger for".
- [INFO] The event counts differ across tables (3,187 in Table 1; 3,199 in Table 2; 3,207 rule-based closes behind the 2.0% in Section 1). The captions explain the difference, but one clause in the first Results paragraph would prevent reviewer queries, e.g., "(counts in Tables 2–4 differ slightly because each outcome needs its own prices)".
- [INFO] The largest Table 1 BH-adjusted *p* (4.0e-04) equals the largest week-clustered raw *p* in the Bonferroni paragraph (4.0e-04). Confirm in `C3_family_control.csv` and `C21_programme_t_reference.csv` that this is a coincidence and not a copy.

---

### 6. Discussion (with Table 5)

**Verdict.** The section has substance: the attention-amplifier reading, the design implications for band width and auction priority, and a clear scope statement. But it repeats Section 5. Its first paragraph restates the timing result, and the Lou et al. sentence hangs without a link. "We do not test the magnet effect" is the third copy of that caveat. "Our estimates … are our estimates for this market" is a tautology, and the next sentence repeats the one before it. "The split cannot identify the rule change" is the second copy. "Limit hits are rare" contradicts Section 1 ("markets where a limit close is common"). "Under this reading the limit creates the attention event" contradicts the sentence before it and reads as a pull-quote. In the `.Rmd`, the paragraph "Our decomposition…" runs straight into "Table 5 sets…" with no blank line, so Word merges them into one paragraph. Table 5's last row overstates the result (see the Section 5 verdict).

**Scores:** Directness 6, Rhythm 6, Trust 7, Authenticity 6, Density 5 = **30/50 (revise)**

**S1.** Merge the restatement, and link Lou et al. to the result.
~~~old
The evidence is consistent with delayed price discovery and with the rival readings of Section 5. The continuation after a ceiling close sits in the opening. Days *d*+2 to *d*+5 add no significant return, and the *d*+1 session reverses part of it. Lou et al. (2019) show continuation in both periods with an offsetting cross-period reversal.
~~~
~~~new
The evidence fits delayed price discovery and the rival readings of Section 5. After a ceiling close, the continuation sits in the opening: days *d*+2 to *d*+5 add no significant return, and traders reverse part of the gap during day *d*+1, a one-day analogue of the cross-period reversal in Lou et al. (2019).
~~~

**S2.** Lazy contrast ("which differs from a multi-day adjustment"). Delete the third magnet caveat and restore the missing paragraph break. The old string spans a line break.
~~~old
on HOSE the continuation arrives at the next opening and stops there after the first day, which differs from a multi-day adjustment. We do not test the magnet effect that Cho et al. (2003) document, because our data lack intraday prices.
Table 5 sets each result
~~~
~~~new
on HOSE the continuation arrives at the next opening and ends after the first day.

Table 5 sets each result
~~~

**S3.** Cut the tautology and the repeated claim. Avoid the "not X" ending.
~~~old
so the comparison concerns signs, timing, and mechanism, not magnitudes. Our estimates of +`r f(ev("ceiling","t+1","mean_ar_pct"),1)`% for the ceiling, +`r f(c16("Ceiling all","gap_mkt"),1)`% for the gap, and `r f(c16("Ceiling all","intraday_mkt"),1)`% for the intraday return are our estimates for this market. We know of no peer-reviewed study that measures them in the same way.
~~~
~~~new
so the table compares signs, timing, and mechanism.
~~~

**S4.** The Table 5 row overstates the result (the confirmation-half |*t*| exceeds 1.96 for two characteristics in Figure 1). The string sits inside the chunk, and the logic does not change.
~~~old
"None of our 22 characteristics reaches 1.96"
~~~
~~~new
"None of our 22 characteristics reaches 1.96 in the full sample"
~~~

**S5.** Remove the repeated caveat, the adverb "directly", and false agency ("shows how").
~~~old
which suggests that auction design shapes how overnight pressure resolves. The split cannot identify the rule change, because the market period changed with it. The widening of the ChiNext band studied by Qi (2023) shows how a band change can serve as a natural experiment, and a similar change on HOSE would test the readings directly.
~~~
~~~new
which suggests that auction design shapes how the opening absorbs overnight pressure, although the market period changed at the same time (Section 5). A band change on HOSE, like the ChiNext widening that Qi (2023) studies, would give a natural experiment to test the readings.
~~~

**S6.** Lazy extreme ("every investor").
~~~old
may signal excess demand to every investor.
~~~
~~~new
may signal excess demand to other investors.
~~~

**S7.** Contradiction plus a quotable ending. Merge into one sentence.
~~~old
A limit then adds a visible, rule-based trigger to a mechanism that already exists without limits. Under this reading the limit creates the attention event.
~~~
~~~new
Under this reading, a limit adds a visible, rule-based trigger to an attention mechanism that operates without limits.
~~~

**S8.** "Limit hits are rare" contradicts Section 1, and the power caveat is the fourth copy. Shorten.
~~~old
We use the 22 characteristics to set the multiplicity burden and as a null benchmark: the procedure that lets the limit tests survive leaves no characteristic significant. The null says little about the cross-section because power is low (Section 5). Limit hits are rare: about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in the event window meet the ceiling definition, and we do not claim that limit hits explain the cross-section of returns.
~~~
~~~new
We use the 22 characteristics to set the multiplicity burden and as a null benchmark; with low power (Section 5), their null says little about the cross-section. Ceiling closes cover about `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days in the event window, so we make no claim that limit closes explain the cross-section of returns.
~~~

**S9.** False agency ("the figures suggest"); the term "limit-up" appears nowhere else in the paper.
~~~old
For investors, the figures suggest that buying limit-up stocks at the quoted open returned `r f(c11("Ceiling: rule-based","f5o_mkt"),2)`% by the fifth close. The figures omit costs and rationing at the open, so they offer no trading advice.
~~~
~~~new
For investors, buying ceiling stocks at the quoted next open returned `r f(c11("Ceiling: rule-based","f5o_mkt"),2)`% against the market by the fifth close, before costs and rationing at the open.
~~~

**Table 5 caption (INFO, no edit required).** "as reported in its abstract or in the records we could access" is an honest integrity disclosure, so keep it. Optional tightening: "Columns 2 and 3 summarize each source from its abstract or accessible records; column 4 relates it to our results."

---

### 7. Limitations

**Verdict.** The section is compact, specific and honest. Problems: passive voice in (ii) and (iv); missing Oxford commas in (ii) and (iii); a run-on in (iii); and an eponymous estimator cited without a reference ("Driscoll–Kraay"). This is an integrity issue: either add Driscoll and Kraay (1998) after a DOI check or describe the method without the name, as the edit below does.

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 8 = **37/50**

**Q1.**
~~~old
(ii) We have no order-book, investor-type, announcement or news data, so the unfilled-demand mechanism is inferred and selection on news is not separated from it.
~~~
~~~new
(ii) We have no order-book, investor-type, announcement, or news data, so we infer the unfilled-demand mechanism and cannot separate it from selection on news.
~~~

**Q2.**
~~~old
(iii) The 7% band, the reference price and the platform change come from brokerage and press descriptions and we check only against the return distribution, with no exchange circulars.
~~~
~~~new
(iii) The 7% band, the reference price, and the platform change come from brokerage and press descriptions, which we check against the return distribution but not against exchange circulars.
~~~

**Q3.**
~~~old
(iv) Prices may be adjusted for corporate actions in ways that affect event classification,
~~~
~~~new
(iv) The vendor may adjust prices for corporate actions in ways that affect event classification,
~~~

**Q4.** Uncited eponym.
~~~old
and we did not compute calendar-time portfolio or Driscoll–Kraay estimates.
~~~
~~~new
and we did not compute calendar-time portfolio estimates or standard errors robust to both cross-sectional and serial dependence.
~~~

**Q5.** Name the question instead of "the idea".
~~~old
because we chose the idea among several.
~~~
~~~new
because we chose this question from several screened on the same data.
~~~

---

### 8. Conclusion

**Verdict.** It restates the approach, gives the key numbers and names future data, which passes Check 1.8. Problems: a hard-coded data number (347); passive voice ("is followed by"); a two-decimal figure (0.75%) beside one-decimal figures (and the abstract shows 0.7%); no floor result; the vague "remain possible"; and a missing Oxford comma.

**Scores:** Directness 8, Rhythm 6, Trust 8, Authenticity 7, Density 8 = **37/50**

**C1.** Hard-coded number; use the inline value.
~~~old
Of 26 tests on 347 HOSE stocks,
~~~
~~~new
Of 26 tests on `r nstocks` HOSE stocks,
~~~

**C2.** Active voice, plus one floor clause (the conclusion currently says nothing about floors).
~~~old
A ceiling close is followed by a next-day abnormal return of about
~~~
~~~new
After a ceiling close, the stock earns a next-day abnormal return of about
~~~

**C3.** Precise comparison group. Add the floor gap.
~~~old
points larger than for those that also closed at their high.
~~~
~~~new
points larger than for those among them that also closed at their high. After a floor close, the overnight gap is `r f(c16("Floor all","gap_mkt"),1)`%.
~~~

**C4.**
~~~old
The pattern is consistent with delayed price discovery at the limit, but news and attention remain possible.
~~~
~~~new
The pattern fits delayed price discovery at the limit, but news and attention remain possible explanations.
~~~

**C5.** Match the abstract's rounding (display only, `d = 2` to `d = 1`).
~~~old
An outside buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),2)`% by the fifth close against the market.
~~~
~~~new
An outside buyer at the next open loses `r f(abs(c11("Ceiling: rule-based","f5o_mkt")),1)`% against the market by the fifth close.
~~~

**C6.**
~~~old
Longer samples, announcement data and order-book data would let future work separate the readings.
~~~
~~~new
Longer samples, announcement data, and order-book data would let future work separate these explanations.
~~~

---

### Declarations

**Verdict.** The AI-use disclosure is present and specific, which meets the integrity requirement. Problems: a missing Oxford comma, and internal path details (`paper2/R/40` to `50`) that expose the project layout. If the target journal reviews double-blind, the GitHub account and the repository name (`black_litterman_2`, which has nothing to do with the paper's topic) both reveal the authors. Before submission, use an anonymized link or a dedicated repository. That decision belongs to the authors; the reviewer has not made it.

**Scores:** Directness 8, Rhythm 7, Trust 8, Authenticity 7, Density 7 = **37/50**

**X1.**
~~~old
to write analysis code, draft text and check numbers against output files.
~~~
~~~new
to write analysis code, draft text, and check numbers against output files.
~~~

**X2.** Remove the internal script numbering.
~~~old
R scripts `paper2/R/40` to `50`, tables C1 to C26 in `paper2/output/tables`).
~~~
~~~new
R code and output tables in `paper2/`).
~~~

---

## Proofreading checks: findings not already covered by an edit

### Check 1: Paper structure
- [ERROR, 1.3] Contributions are not falsifiable (no numbers). Fixed by I6–I8.
- [WARN, 1.1] The abstract gives no number for the H3 contrast. Fixed by A5.
- [WARN, 1.6] The "Classic evidence" paragraph has no topic sentence. Fixed by L1.
- [WARN, 1.6] Every literature paragraph ends with the same gap line. Fixed by L2 and L7.
- [WARN, 1.7] The paper states hypotheses H1–H4 before the results (pass). The H4 wording does not match the test. Fixed by L12.
- [WARN, 1.8] The conclusion omits the floor result. Fixed by C3.
- [WARN, 1.9] Section 5 restates motivation and the literature. Fixed by R14 and R10.
- [INFO, 1.4] The roadmap matches Sections 2–8 and uses present tense (pass). It lacks a verb for Section 4. Fixed by I9.
- [INFO, 1.2] The paper states its novelty as "none of the studies we reviewed" (acceptable).

### Check 2: Math symbols and notation
Detected convention: **B** (all scalars italic, no vectors or matrices). Consistent.
- [ERROR, 2.3] Clashes for $\tau$, $G$, $i$, $j$ and $k$. Fixed by M3, M5, M6, M9, M10, M13–M16, M21 and M22.
- [ERROR, 2.2] $G$, $k$ (Eq. 4), $x_{i,\tau}$, $n_\tau$ and $\Phi^{-1}$ are undefined. Fixed by M9, M15 and M17.
- [ERROR, 2.2] AR, CAR and MDE are undefined. Fixed by M7 and M20.
- [ERROR, 2.7] AR and CAR are multi-letter symbols without `\mathit`. Fixed by M8.
- [ERROR, 2.5] Eq. (4) ends with a period before a "where" clause. Fixed by M8.
- [ERROR, 2.2] The quintile spreads are undefined in Section 4. Fixed by M20.
- [ERROR, 2.2] The constant 2.8 is unexplained. Fixed by M20.
- [ERROR, 2.3] The Table 1 caption uses "G" for the number of clusters while Eq. (5) uses $G_i$. Fixed by M10 (the gap symbol changes).
- [ERROR, 2.2] "Event window" (Sections 1 and 6) is undefined. Fixed by M2.
- [WARN, 2.4] Symbols in Section 4 mix Markdown italics and math mode. Fixed by M1, M4, M11, M13 and M15; apply the stated rule to any remaining cases.
- [WARN, 2.3] "Market-adjusted return" and "abnormal return" are used as synonyms. M7 settles on "abnormal". "Market-adjusted" in Section 5 and the Table 1 and Table 3 captions can stay as a description of the benchmark.
- [WARN] The BH wording mixes the adjusted value with the threshold. Fixed by M21 and M23.
- [WARN, 2.9] Two names for one hyphenated notion: "two-way-clustered" in Tables 2 and 4 and the text, "date-clustered" in Table 3. Consistent within each; OK.
- [WARN] The weight timing (Table 1 vs Tables 2–4) is stated in prose but not in the notation. Fixed by M4.
- [WARN] $y$ is the event outcome and also the weekly regressand $y_{i,\tau}$. Acceptable, because the subscripts differ and both are "an outcome"; noted for the authors.
- [INFO, 2.10] Equations (1), (2) and (6) are never cited. Optional.
- [INFO, 2.7] `m_{\max}` should be `m_{\text{max}}`. Fixed by M24.
- [INFO] Thresholds appear as decimals in equations and as percentages in prose. Acceptable.
- [INFO] The product-difference "CAR" is a buy-and-hold abnormal return. Consider "BHAR".

### Check 3: Statistical relevance
- [WARN, 3.3] "Effect grows as the close approaches the limit" has no test of the difference (Section 5 note).
- [WARN, 3.3] "Gap rises with volume / prior return" has no trend test (Section 5 note).
- [WARN, 3.3] "The floor gap is not significant in the least liquid tercile" is a difference-in-significance argument; fine as worded.
- [INFO, 3.2] Tables 1–4 report *t*-statistics and Figure 2 shows 95% CIs (pass). Figure 1 shows *t*-statistics themselves (pass).

### Check 4: Figures and tables
- [ERROR, 4.3] The Figure 1 axis labels are undefined code names. Fixed by R-F1.
- [ERROR, 4.3] The Figure 2 caption misdescribes the triangles and does not define the bins. Fixed by R-F2.
- [WARN, 4.1/4.4] Every table and figure is called out before it appears (pass). The Table 4 call-out is a bare one-sentence paragraph. Fixed by R23.
- [WARN, 4.3] The Table 1 and Figure 1–2 captions lack Oxford commas. Fixed by R-T1, R-F1 and R-F2.
- [WARN, 4.8] Table 5 is called out with an explanation (pass). The paragraph break before it is missing. Fixed by S2.
- [WARN] A Table 5 cell overstates the result. Fixed by S4.
- [INFO, 4.5] The figures are PNG. Acceptable for Word; supply vector PDF or EPS at submission if the journal asks.
- [INFO, 4.9] Figure 2 uses colour by panel, and the shapes separate bins, events and other moves (pass). Figure 1 uses both colour and shape (pass). Neither has a plot title inside the axes (pass).
- [INFO] Section 3 mentions Table 1 before Section 5 introduces it. D7 and M4 move that mention into Section 4, which is still before the table.

### Check 5: Grammar and style
English variant: **American** (behavior, realized, rank-normalize). Consistent.
- [ERROR, 5.4] Missing Oxford commas in several lists, against the dominant style. Fixed by R3, R19, R-T1, R-F1, R-F2, Q1, Q2, C6 and X1.
- [ERROR] A stray comma before the citation in Section 3. Fixed by D8.
- [WARN, stop-slop] Adverbs: "long", "now", "directly", "even", "likely", "tend to" and filler uses of "only". Fixed by I1, L4, S5, R6, R21, L5 and R22. The remaining "only" uses carry meaning ("exists only before the move") and stay.
- [WARN, stop-slop] False agency: "limits aim", "data cannot separate", "evidence shows", "comparison makes no claim", "split shows", "figures suggest", "session undoes". Fixed by A1, A7, R9, R19, R25, S9 and R13.
- [WARN, stop-slop] Narrator voice: "This clustering is why". Fixed by R1.
- [WARN, stop-slop] Throat-clearing: "Taken together", "The result is in line with". Fixed by R27 and R6.
- [WARN, stop-slop] "Not X" contrasts: "not a change in the band", "not magnitudes", "which differs from a multi-day adjustment". Fixed by R24, S3 and S2.
- [WARN, stop-slop] Three-item list of speculative explanations. Cut to two by R7.
- [WARN, stop-slop] Quotable ending: "Under this reading the limit creates the attention event". Fixed by S7.
- [WARN, 5.9] Repeated claims across Sections 5, 6 and Table 5. Fixed by R10, R14, R22, S2, S3, S5 and S8.
- [WARN, 5.1] Passive voice where "we" works: Section 7 (ii) and (iv), and the abstract and conclusion "is followed by". Fixed by Q1, Q3, A5 and C2.
- [WARN] Contradiction: "limit close is common" (Section 1) vs "Limit hits are rare" (Section 6). Fixed by S8.
- [WARN] Overclaim in the summary paragraph of Section 5. Fixed by R27.
- [WARN] Mention of internal process ("project-wide search", script numbers). Fixed by R26 and X2.
- [INFO, 5.2] Section 2 uses present tense throughout. APA-like style allows it. Optional: put results of published work in the past tense.
- [INFO, 5.4] "which" clauses are mostly non-restrictive with commas (pass).
- [INFO] The title list "price limits, overnight gaps and next-day returns" lacks an Oxford comma. Optional: "price limits, overnight gaps, and next-day returns".
- No em dashes in the prose (pass). No Wh- sentence openers (pass). "If …" conditionals are used for the hypotheses and are acceptable.

### Check 6: Abbreviations
- [ERROR, 6.4] FDR is introduced twice in the body (Section 1 and Section 4). Fixed by M21. It is also spelled out after its definition (Section 2). Fixed by L10.
- [ERROR, 6.3] AR and CAR are never introduced. Fixed by M7.
- [ERROR, 6.3] MDE is used without introduction. Fixed by M20.
- [ERROR, 6.3] The Figure 1 code labels are undefined. Fixed by R-F1.
- [WARN, 6.2] HOSE is introduced in the abstract but used only once there. Fixed by A3.
- [WARN, 6.3] VCI appears before its full term. Fixed by D1.
- [WARN] "Dollar volume" is measured in dong. Defined by D6 and M4.
- [INFO] Checked and correct: HOSE (Section 1), HSC (Section 3, APA bracket form), KRX (Section 3), T+1 (defined in Section 2: "under which shares bought on one day cannot be sold until the next"), BH (Section 4), MAX and MIN (Section 4, used in Sections 5 and 7), H1–H4 (Section 2). GARCH does not appear in the paper. "U.S." is standard.
- [INFO, 6.5] Articles before abbreviations: none of the pairs is wrong.

## Integrity-gate items (not style; must not be self-approved)

1. **Missing reference:** Section 4 cites "Cameron et al., 2011", which is not in the reference list. The candidate entry is given in the Top Issues list; run the DOI check before adding it.
2. **Uncited eponym:** "Driscoll–Kraay" in Section 7. Edit Q4 removes the name. If the authors want the name, add Driscoll and Kraay (1998) after a DOI check.
3. **Reference completeness (INFO):** Huang et al. (2023) and Lin et al. (2023) have no article number or pages. Fourteen entries have no DOI (Aboody 2018, Bogousslavsky 2021, Chordia 2020, Deb 2013, Greenwald 1991, Hou 2020, Huang 2001, Jones 2025, Kim & Limpaphayom 2000, Kim & Jun 2019, Lien 2019, Lu 2023, Petersen 2009, Qiao & Dam 2020, Qiu 2025, Zhang 2022). Add the DOIs at the DOI-check stage. Do not add them from memory.

## Number consistency (abstract ↔ text ↔ tables)

| Quantity | Abstract | Text | Table | Status |
|---|---|---|---|---|
| Stocks | 347 (inline) | 347 (inline; Section 8 hard-coded) | — | OK; C1 makes Section 8 inline |
| Ceiling next-day AR | 1.7% | 1.66% (Section 5), 1.7% (Sections 6, 8) | 1.66 (T1), 1.66 (T2) | OK |
| Ceiling gap | 2.2% | 2.24% | 2.24 (T2) | OK |
| Ceiling intraday | 0.5% | −0.54% | −0.54 (T2) | OK |
| Gap vs 5–6.5% risers | (none; A5 adds 2.7) | 2.66 / 2.7 | 2.66 (T3) | OK |
| Gap vs those closing at high | — | 3.14 / 3.1 | 3.14 (T3) | OK |
| Next-open to day 5, ceiling | −0.7% ("earns") | −0.75% (Sections 5, 6), 0.75% (Section 8, "loses") | −0.75 (T2) | **Rounding/sign mismatch**; fixed by A6 and C5 |
| Ceiling share of stock-days | — | 2.0% (Sections 1, 6) | C13 3,207/156,653 | OK |
| Post-KRX share | — | 71% / 58% | 2,263/3,199; 1,220/2,111 | OK |
| Bonferroni bound | — | 683 / 125 | C21 | OK |
| Trading days | — | 519 (hard-coded) | C26 = 519 | OK; D2 makes it inline |

## Old-string check

A script extracted all 114 `~~~old` blocks and searched for each in `manuscript_final.Rmd`. Each block occurs exactly once, and no two blocks overlap, so the authors can apply the edits in any order.
