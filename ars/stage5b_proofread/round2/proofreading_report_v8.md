# Proofreading Report — Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification (v8, final pass)

**Date:** 2026-09-24  
**Source:** /home/user/B-i-FTSE2/submission/manuscript_anonymized.tex (line numbers). Block IDs refer to /home/user/B-i-FTSE2/ars/stage4_5_integrity/correction_round4/manuscript_v8.md. Figures: /home/user/B-i-FTSE2/submission/figures/Figure_1.png, Figure_2.png (both viewed). LaTeX log: /home/user/B-i-FTSE2/ars/stage5_finalize/work/manuscript_anonymized.log (the .tex in that folder is identical to the submission .tex).

**Mode:** Report mode. No manuscript file was edited.

### Skill load record

| File (read in full with the Read tool) | First heading |
|---|---|
| /root/.claude/skills/proofreading/SKILL.md (Checks 1 to 6) | `# Paper Proofreading` |
| /root/.claude/skills/proofreading/templates/output_template.md | `# Proofreading Report — {{paper_title}}` |
| /root/.claude/skills/academic-paper/references/writing_quality_check.md | `# Writing Quality Check` |
| /root/.claude/skills/academic-paper/references/academic_writing_style.md | `# Academic Writing Style Guide` |

### Adaptations applied (same as round 1, stated, not silently dropped)

1. **Section mapping.** Template section 1 (Abbreviations) = SKILL Check 6; 2 (Math) = Check 2; 3 (Introduction Structure) = Check 1 (abstract, introduction, literature, hypotheses, conclusion); 4 (Grammar & Style) = Check 5; 5 (Figures & Tables) = Check 4; 6 (Statistical Relevance) = Check 3. Rule numbers below are SKILL.md numbers.
2. **Venue.** Finance Research Open (Elsevier), APA 7 author-year. Abstract limit 250 words (rule 1.1 default 150). The abstract has about 213 words: no finding.
3. **DOCX-first build.** Tables are pandoc longtables and equation, table and figure numbers are hard-coded. Missing `\label`/`\ref`/`\eqref` (rules 2.7, 4.1, 4.2) is INFO, not ERROR. Fixes are given for both the .tex and the Markdown source.
4. **Uncertainty.** Clustered standard errors, portfolio t-statistics, bootstrap and randomization p-values and 95% CIs count as uncertainty reporting (Check 3). Seed/run rules for stochastic ML experiments do not apply.
5. **ARS precedence where the checklist conflicts:**
   - Voice: active "we" (social sciences) is kept; rule 5.1 produced no findings.
   - Tense: past tense for results (ARS) overrides rule 5.2 (present tense throughout). Hypotheses are now correctly in the present tense.
   - Contribution: prose contribution with First to Fourth markers overrides the bulleted list of rule 1.3 (no finding; it now opens with "We make one contribution").
   - Literature positioning: rule 1.6 self-reference ERROR downgraded to WARN.
   - Oxford comma: omitted as house style; rule 5.4 ERROR downgraded to one WARN, and only inconsistencies are reported.
   - Numbers repeated from tables: finance/ARS practice; rule 5.9 not reported.
   - Titles without final period: Elsevier style; rule 4.3 period rule not reported.
   - Rule 1.3 "theorems, proofs, algorithms" and rule 5.11 (`siunitx`, parameter values) do not apply to an empirical finance paper.
6. **Not applicable or clean (checked):** rule 1.5 (no problem statement section); rule 2.6 (all symbols scalars; convention "unknown / not applicable"); rule 2.8 (no custom macros; no complex expression repeated 3+ times outside the equations that define it); rule 4.12 (not IEEE); rule 4.13 (no algorithms); rule 5.7 (no unhyphenated compound adjectives); rule 5.12 (First to Fourth in 3.4 sit in one paragraph); ARS Section A flagged terms (none); em dashes (none); first-person singular (none); "Note that" (none).
7. **Scope.** No finding proposes changing a number, a citation or the strength of a claim. Where a number or claim looks inconsistent with a table, a figure or the code, it is flagged for verification. Minus signs are written as ASCII hyphens in this report; the manuscript correctly uses U+2212.

### What round 1 fixed (verified in v8, not re-reported)

Undefined baseline-equation symbols; statistical symbols now italic; VND, VCI, UPCoM, ITT, CARs, CS spread and SMD introduced once in the body; significance stars referenced in every starred table; FE/SE removed; Figure 2 dashed lines explained; same y-range, distinct colour and shape, and units on both figures; hypotheses in present tense; comma splice; "organize"; the Table 8 "similar size" sentence; the "largest positive deviations" sentence; the "under every benchmark" takeaway; the Table 7 title and CS-spread units. The -0.855/-0.85 rounding flagged in round 1 is correct: output/revision/t5_segments.csv gives -0.8547.

---

## Scorecard

| # | Check                   | Errors | Warnings | Info | Total |
|---|-------------------------|--------|----------|------|-------|
| 1 | Abbreviations           | 0      | 2        | 1    | 3     |
| 2 | Math Symbols & Notation | 4      | 6        | 7    | 17    |
| 3 | Introduction Structure  | 0      | 2        | 2    | 4     |
| 4 | Grammar & Style         | 1      | 10       | 7    | 18    |
| 5 | Figures & Tables        | 0      | 5        | 7    | 12    |
| 6 | Statistical Relevance   | 0      | 3        | 3    | 6     |
|   | **Total**               | **5**  | **28**   | **27**| **60** |

---

## Overall Assessment

v8 is close to submission-ready. Every headline number spot-checked against the tables and the output CSVs reconciles: percentages from log coefficients, the 62% to 72% and 62% to 77% ratios, the 12% and 13% shrinkage, t = 6.84, the segment-weighted mean of 0.76, and the pretrend months in both figures. The round-1 fixes are in place. The weak spot is the new notation in Sections 3.2 and 3.3. Four symbols or indices are never defined: the event-window bounds and event-time index in Eq. (6), the error term in Eq. (9), the Corwin-Schultz intermediates and spread in Eqs. (2) and (3), and the range and reference of m in Eq. (8). The letters alpha and beta mean two things each. Three displayed equations overflow the margin by 21 to 135 pt. The compaction introduced one sentence whose meaning is inverted ("liquidity decline"), several ambiguous phrases, and table notes that point to the text for definitions (screening windows, benchmarks, test threshold).

### Top Issues to Address

1. **[ERROR] Check 5 (grammar)** — Line 824 (B0094): "The liquidity decline at the disclosures" states the opposite of the finding (illiquidity declined; liquidity rose) (G1).
2. **[ERROR] Check 2.2** — Eq. (6), line 350 (B0204/B0205): tau_1, tau_2 and the event-time meaning of t are never defined; Eq. (9), line 425 (B0208/B0209): u_id is never defined; Eqs. (2) and (3): beta^cs, gamma^cs, alpha^cs and S_it are never defined (M1 to M3).
3. **[ERROR] Check 2.2** — Eq. (8), lines 394 to 400 (B0049/B0206/B0207): the range of m is not stated, "relative to September 2025" and "relative to October 2025 (m = 0)" sit in consecutive sentences, and months are actually assigned by the Monday on which each week starts (M4, with T3).
4. **[WARN] Check 2 / log** — Eqs. (4), (6) and (9) overflow the text block by 134.7, 40.7 and 21.4 pt; split proposals are given (M7 to M9).
5. **[WARN] Check 3.3** — Line 342 (B0203) says the large-stock benchmark is the "110 never-named stocks in the top tercile" and lines 416 and 616 say "85 never-named stocks in the top tercile". The code confirms two different tercile bases, but the text does not say so (T1). Line 1195 (B0141): "Only three trading days follow the effective date" conflicts with a Monday 21 to Wednesday 23 September window (T2).
6. **[WARN] Check 4.3** — The Table 4, 7, 9 and A.3 notes are not self-contained: the benchmarks point to "Eq. (5)", which does not list them; there is no window unit or 5% threshold; the Table 7 headers (2) and (4) are identical; W1 to W3 are defined only in the text (F2 to F4). The Table 3 headers overflow their columns (F1).

---

## 1. Abbreviations

**Summary:** The abstract is self-contained: no abbreviations besides brand names; CAR and HOSE are spelled out. In the body, HOSE, ITT, VND, CS spread, CARs, SMD, UPCoM and VCI are each introduced once and not re-expanded. Articles and plurals are correct. Two issues remain: "VND" is also a ticker in Table 8 and Table A.2, and the table notes use CS and SMD without expanding them.

### Findings

- [WARN] manuscript_anonymized.tex:1002 (B0115; also line 1267, B0147) — "VND" is introduced as the currency (line 97) but is used here as a securities-firm ticker. A reader of the table notes cannot tell which is meant. ("VCI" is both the data vendor and its own ticker, which is the same firm, so it is harmless.)
  > are SSI, VCI, VIX, VND and HCM. Bootstrap: restricted residuals,
  Suggestion: "are SSI, VCI, VIX, VND (the VNDirect Securities ticker, not the currency) and HCM. Bootstrap: restricted residuals," Author to confirm the firm name. In Table A.2 (line 1267) no change is needed if the Table 8 note carries the clarification.
- [WARN] manuscript_anonymized.tex:288 (B0038/B0039; also lines 917–921, B0107/B0108; line 1228, B0144/B0145) — The table headers use "CS spread" and "SMD", but the notes never expand them. Tables should be self-contained (rule 4.3), and the abbreviations are defined only in body text (lines 98, 411).
  > CS spread (\%)
  Suggestion: Table 1 notes (line 301): "Weekly means; Amihud as in Eq. (1) with traded value in VND billion; CS spread is the Corwin and Schultz (2012) high-low spread, Eqs. (2)–(3). Source: ...". Table 7 notes (line 939): "Eq. (7). Volatility is \(\mathrm{Vol}_{iw}\) from Eq. (4); CS spreads (Eqs. (2)–(3)) are in decimal units ...". Table A.1 notes (line 1245): "Nearest-neighbour propensity-score matching ... SMD is the standardized mean difference. Log trading value ...".
- [INFO] manuscript_anonymized.tex:148 (B0018; also line 1121, B0128) — Carried over from round 1: GEE and BSR carry the Section 5.2 argument but are never linked to company names. BSR is described once, indirectly, through the VietnamPlus reference title.
  > adding BID, FPT, NVL, GEE and BSR (The Investor, 2026b). On 21 August
  Suggestion: "adding BID, FPT, NVL, Gelex Electricity (GEE) and Binh Son Refining and Petrochemical (BSR) (The Investor, 2026b). On 21 August" (author to confirm the names).

---

## 2. Math Symbols & Notation

**Summary:** Detected notation convention: unknown / not applicable (all symbols are scalars). All nine displayed equations are grammatically integrated and punctuated, operator names use `\mathrm{}`, and every numbered equation except (2) and (3) is referenced. Four definition gaps are new in v8: Eq. (6) bounds and event time, the Eq. (9) error term, the Corwin-Schultz intermediates, and the range of m in Eq. (8). Alpha and beta each carry two meanings, and the daily index switches from t to d without a bridge. Eqs. (4), (6) and (9) overflow the margin (log lines 583, 590, 597).

### Findings

- [ERROR] manuscript_anonymized.tex:350 (B0204; where clause B0205, lines 352–355) — In Eq. (6), \(\tau_1\) and \(\tau_2\) are never defined. The sum index t now counts event days relative to the disclosure, while t in Eqs. (1)–(5) is a calendar trading day (rules 2.2 and 2.9). \(D = \tau_2 - \tau_1 + 1\) implies the bounds but does not define them.
  > \mathrm{CAR}_p(\tau_1, \tau_2) = \sum_{t=\tau_1}^{\tau_2}\mathrm{AR}_{pt}
  Suggestion: Begin the where clause at line 352 with: "where \(t\) in Eq. (6) counts trading days relative to the disclosure date (day 0), \(\tau_1\) and \(\tau_2\) are the first and last days of the event window, \(p\) denotes the equal-weighted portfolio of group \(g\), \(\hat\sigma_p\) is the standard deviation of \(\mathrm{AR}_{pt}\) in the estimation window and \(D = \tau_2 - \tau_1 + 1\) is the number of event-window days; ..." (this also resolves the undefined subscript p, see the INFO below).
- [ERROR] manuscript_anonymized.tex:425 (B0208; where clause B0209, lines 427–431) — \(u_{id}\) in Eq. (9) is never defined.
  > + \theta_2\left(\mathrm{Constituent}_i \times \mathrm{Eff}_d\right) + u_{id}, \qquad (9)\]
  Suggestion: Line 427: "where \(d\) indexes sessions, \(\lambda_d\) are date fixed effects, \(\mathrm{Reb}_d\) and \(\mathrm{Eff}_d\) indicate 18 September (the rebalancing session) and 21 September (the effective date), and \(u_{id}\) is the error term."
- [ERROR] manuscript_anonymized.tex:322 (B0197, B0198; first later use B0199, line 326) — \(\beta^{\mathrm{cs}}_{it}\), \(\gamma^{\mathrm{cs}}_{it}\), \(\alpha^{\mathrm{cs}}_{it}\) and \(S_{it}\) are never defined in prose. Line 326 then winsorizes "\(S_{it}\)" as if the reader knows it is the spread estimate.
  > We winsorize \(\mathrm{ILLIQ}_{it}\) and \(S_{it}\) at the 1st and 99th
  Suggestion: Line 326: "Here \(\beta^{\mathrm{cs}}_{it}\) sums the squared log high-low ranges of days \(t-1\) and \(t\), \(\gamma^{\mathrm{cs}}_{it}\) is the squared log range over the two days combined, and \(S_{it}\) is the resulting spread estimate, set to zero when negative. We winsorize \(\mathrm{ILLIQ}_{it}\) and \(S_{it}\) at the 1st and 99th".
- [ERROR] manuscript_anonymized.tex:394 (B0049, B0206, B0207; lines 394–400) — The index m has no stated range (rule 2.2). Two consecutive sentences give different anchors: "a monthly event study relative to September 2025" and "month m relative to October 2025 (m = 0)". The code assigns months by the Monday on which the week starts (code/analysis.R lines 58 and 71: `week := cut(date, "week")`, `relm := ... month(week) - 10`), not by where the week "falls". Output/revision/t_event_study.csv runs from m = -13 to 11.
  > where \(M_{mw}\) equals one if week \(w\) falls in month \(m\) relative
  Suggestion: Line 394: "For timing, we estimate a monthly event study (Roth et al., 2023):". Lines 399–400: "where \(M_{mw}\) equals one if week \(w\) starts in month \(m\), counted from October 2025 (\(m = 0\)), with \(m\) running from \(-13\) to \(11\) and September 2025 (\(m = -1\)) as the omitted reference month." (Range from the output CSV; author to confirm. See T3 on month -13.)
- [WARN] manuscript_anonymized.tex:324 (B0198; conflicts with B0047/B0048 line 368, B0206, B0208) — One symbol, two concepts (rule 2.3): \(\alpha^{\mathrm{cs}}_{it}\) (Corwin-Schultz intermediate) and \(\alpha_i\) (stock fixed effect, Eqs. (7)–(9)); \(\beta^{\mathrm{cs}}_{it}\) and \(\beta_k\) (window coefficients). The market model already avoids the clash by using \(\hat a_i\), \(\hat b_i\).
  > \[\alpha^{\mathrm{cs}}_{it} = \frac{\sqrt{2\beta^{\mathrm{cs}}_{it}} - ...
  Suggestion: Either keep the Corwin and Schultz (2012) letters and add to the sentence proposed above: "the superscript cs distinguishes these from the regression coefficients in Eqs. (7)–(9)", or rename them throughout Eqs. (2)–(3) to \(\phi_{it}\) (for \(\beta^{\mathrm{cs}}\)), \(\psi_{it}\) (for \(\gamma^{\mathrm{cs}}\)) and \(\eta_{it}\) (for \(\alpha^{\mathrm{cs}}\)).
- [WARN] manuscript_anonymized.tex:425 (B0208; vs B0041/B0042 lines 309–314) — One concept, two symbols (rule 2.3): daily traded value is \(\mathrm{VAL}_{it}\) in Eqs. (1) and (4) and \(\mathrm{VAL}_{id}\) in Eq. (9), and the day index switches from t to d without a bridge.
  > \[\ln\mathrm{VAL}_{id} = \alpha_i + \lambda_d + \theta_1\left(...
  Suggestion: Line 422: "For the rebalancing session we estimate, over the 32 sessions from 6 August to 23 September 2026, and writing \(d\) for these sessions to distinguish them from the day index \(t\) of Section 3.2," Alternatively, replace d with t in Eq. (9) and lines 427–429.
- [WARN] manuscript_anonymized.tex:331 (B0200; log line 583, "Overfull \hbox (134.7039pt too wide) detected at line 331") — Eq. (4) overflows the text block by 134.7 pt.
  > \[\mathrm{Amihud}_{iw} = \ln\left(...\right), \qquad \mathrm{TV}_{iw} = ...
  Suggestion (split into three aligned lines; in the Markdown source, put the same `aligned` block inside `$$...$$`; pandoc converts it for both LaTeX and DOCX):
  `\[\begin{aligned} \mathrm{Amihud}_{iw} &= \ln\Bigl(\frac{1}{N_{iw}}\sum_{t \in w}\mathrm{ILLIQ}_{it}\Bigr),\\ \mathrm{TV}_{iw} &= \ln\sum_{t \in w}\mathrm{VAL}_{it},\\ \mathrm{Vol}_{iw} &= \ln\Bigl(\frac{1}{N_{iw}}\sum_{t \in w}|R_{it}|\Bigr), \end{aligned} \qquad (4)\]`
- [WARN] manuscript_anonymized.tex:350 (B0204; log line 590, 40.7 pt too wide) — Eq. (6) overflows the text block.
  > \[\mathrm{AR}_{pt} = ..., \qquad \mathrm{CAR}_p(\tau_1, \tau_2) = ..., \qquad t_{\mathrm{CAR}} = ...
  Suggestion: `\[\begin{aligned} \mathrm{AR}_{pt} &= \frac{1}{N_g}\sum_{i \in g}\mathrm{AR}_{it}, \qquad \mathrm{CAR}_p(\tau_1, \tau_2) = \sum_{t=\tau_1}^{\tau_2}\mathrm{AR}_{pt},\\ t_{\mathrm{CAR}} &= \frac{\mathrm{CAR}_p(\tau_1, \tau_2)}{\hat\sigma_p\sqrt{D}}, \end{aligned} \qquad (6)\]`
- [WARN] manuscript_anonymized.tex:425 (B0208; log line 597, 21.4 pt too wide) — Eq. (9) overflows the text block.
  > \[\ln\mathrm{VAL}_{id} = \alpha_i + \lambda_d + \theta_1\left(...\right) + \theta_2...
  Suggestion: `\[\begin{aligned} \ln\mathrm{VAL}_{id} = \alpha_i + \lambda_d &+ \theta_1\left(\mathrm{Constituent}_i \times \mathrm{Reb}_d\right)\\ &+ \theta_2\left(\mathrm{Constituent}_i \times \mathrm{Eff}_d\right) + u_{id}, \end{aligned} \qquad (9)\]`
- [WARN] manuscript_anonymized.tex:1062 (B0123; B0128, B0131, B0212, B0213) — The screening windows W1–W3 share their letter with the week index w, and they are a second set of three windows alongside the disclosure windows \(P_{1w}\)–\(P_{3w}\) of Eq. (7). The text never says the two sets differ (W3 spans both the confirmation and the list windows).
  > end of window W1 (from 7 October 2025; W2 runs to 6 April 2026 and W3
  Suggestion: Keep the labels and add one sentence (see G4 for the full rewrite): "These screening windows differ from the disclosure windows \(P_{kw}\) of Eq. (7)." Optionally rename them S1–S3 throughout Section 5.2, Table 9 and Table A.3.
- [INFO] manuscript_anonymized.tex:336 (B0044/B0202; B0203 line 344) — The subscript b in \(R_{bt}\) is not stated to index the four benchmarks, and b is also the slope letter \(\hat b_i\) in the same equation. \(\hat a_i\) and \(\hat b_i\) are defined after Eq. (5); this is acceptable (rule 2.2 INFO).
  > benchmark return \(R_{bt}\) is
  Suggestion: "benchmark return \(R_{bt}\), where \(b\) indexes the four benchmarks described below, is".
- [INFO] manuscript_anonymized.tex:322 (B0197, B0198) — Eqs. (2) and (3) are numbered but never referenced (rule 2.10).
  > \left[\ln\frac{H_{i,t-1}}{L_{i,t-1}}\right]^2, ... \qquad (2)\]
  Suggestion: Reference them in the Table 1 and Table 7 notes as proposed under Abbreviations ("CS spread ..., Eqs. (2)–(3)"). No renumbering is needed.
- [INFO] manuscript_anonymized.tex:314 (all displayed equations; references at lines 301, 370, 388, 467, 511, 569 and others) — Equation numbers are typed as `\qquad (n)` inside `\[...\]`, so they are not flush right, and references are hard-coded "Eq. (n)" (rules 2.7, 2.10). This is accepted for the DOCX-first build.
  > \[\mathrm{ILLIQ}_{it} = \frac{|R_{it}|}{\mathrm{VAL}_{it}}. \qquad (1)\]
  Suggestion: For a LaTeX-native build, use `\begin{equation}...\label{eq:illiq}\end{equation}` and `Eq.~\eqref{eq:illiq}`. Otherwise no change.
- [INFO] manuscript_anonymized.tex:333 (B0201; also lines 1100, 1247) — The equations write `\ln` while the prose and tables write "log" (log Amihud, "log(1 + traded value", Table A.1). This is conventional, but the base is never stated.
  > and the weekly spread is the mean of \(S_{it}\) within the week.
  Suggestion: "and the weekly spread is the mean of \(S_{it}\) within the week; ln and log denote the natural logarithm."
- [INFO] manuscript_anonymized.tex:370 (B0048; B0199 lines 328–329) — "the weekly spread" is an outcome of Eq. (7) but has no symbol, and "\(t \in w\)" in Eq. (4) is not glossed.
  > where \(y_{iw}\) is an outcome from Eq. (4) or the weekly spread for
  Suggestion: Line 328: "For stock \(i\) in week \(w\), with \(N_{iw}\) trading days \(t \in w\)," Line 370 can stay as is.
- [INFO] manuscript_v8.md B0053 (tex line 440) — The Markdown source writes the symbol as the raw Unicode string "β_k" rather than `$\beta_k$`. The current .tex and DOCX render it correctly as math (verified in word/document.xml), but a fresh pandoc build from v8.md would print a literal underscore.
  > The coefficients β_k identify the effect of the upgrade on constituents
  Suggestion: In B0053, write "The coefficients $\beta_k$ identify the effect of the upgrade on constituents under four assumptions."
- [INFO] manuscript_anonymized.tex:324 (B0198; log line 577, 0.84 pt too wide) — Eq. (3) overflows by less than 1 pt. This is invisible in print, but it disappears if the equation is split.
  > \alpha^{\mathrm{cs}}_{it} = ..., \qquad S_{it} = \max\left\{0,\ ...\right\}. \qquad (3)\]
  Suggestion: Optional: `\[\begin{aligned} \alpha^{\mathrm{cs}}_{it} &= \frac{\sqrt{2\beta^{\mathrm{cs}}_{it}} - \sqrt{\beta^{\mathrm{cs}}_{it}}}{3 - 2\sqrt{2}} - \sqrt{\frac{\gamma^{\mathrm{cs}}_{it}}{3 - 2\sqrt{2}}},\\ S_{it} &= \max\Bigl\{0,\ \frac{2\left(e^{\alpha^{\mathrm{cs}}_{it}} - 1\right)}{1 + e^{\alpha^{\mathrm{cs}}_{it}}}\Bigr\}. \end{aligned} \qquad (3)\]`

---

## 3. Introduction Structure

**Summary:** The abstract now has all four parts in order: motivation, gap ("studies of aggregate indices ... do not show which stocks gain or when"), approach, and quantitative results. It has 213 words (limit 250). The introduction has motivation, an explicit gap, the approach, novelty ("In a search bounded to Crossref records ..."), a contribution beginning with "We", and a correct roadmap. H1, H2 and H4 are evaluated by name. Two issues remain: one contribution clause attributes a result to the wrong group, and one literature-review claim has no citation.

### Findings

- [WARN] manuscript_anonymized.tex:110 (B0013) — The clause "with a discrete step at the confirmation but not at the list" is attached to the ITT estimates, but the step test in Section 4.1 (lines 472–476, drift variant) concerns the constituents, and Tables 2 and 3 do not show it. Author to verify whether an ITT step test exists; if not, the clause needs the right subject.
  > 0.81 log points across the three windows, about two thirds of the
  Suggestion: "First, ITT illiquidity fell by 0.27, 0.55 and 0.81 log points across the three windows, about two thirds of the constituent declines (Tables 2 and 3), and constituent illiquidity stepped down discretely at the confirmation but not at the list (Section 4.1)."
- [WARN] manuscript_anonymized.tex:211 (B0025) — A comparative claim in the literature review has no citation (rules 1.6 and 5.10): "benchmark-tracking foreign money changes the investor base more than an S&P 500 addition does". The paragraph also contains the authors' own design ("we do not measure that shift"), which is downgraded to WARN (adaptation 5).
  > investors dominate turnover, benchmark-tracking foreign money changes
  Suggestion: The author should add the supporting citation, for example "(Raddatz et al., 2017)" if it covers the claim, or another source. The claim strength is left unchanged. Move "we do not measure that shift" to Section 6 (for example, after "For issuers," at line 1190) or keep it as the sentence split proposed in G8.
- [INFO] manuscript_anonymized.tex:824 (B0094; H3 at line 231, B0030) — The second half of H3 ("the first index tranche adds no further price effect") is never evaluated by name. Line 763 covers only the disclosures.
  > additions, whereas the first-tranche purchase in Vietnam left no
  Suggestion: At line 825, end the sentence with: "... left no reliable price effect, consistent with the second part of H3."
- [INFO] manuscript_anonymized.tex:124 (B0014) — The roadmap does not mention the Appendix (rule 1.4).
  > robustness checks and the selection evidence. Section 6 concludes.
  Suggestion: "robustness checks and the selection evidence. Section 6 concludes, and the Appendix reports covariate balance, the stocks on each FTSE list and stock-level screening results."

---

## 4. Grammar & Style

**Summary:** Detected English variant: British with Oxford -ize spelling ("favour", "centres", "neighbour" beside "organized", "standardized", "winsorize"). There are no deviations. The prose is clear and has no em dashes, first-person singular, or ARS-flagged terms. The compaction created one inverted statement, several ambiguous phrases ("listed stocks", "whose", "the persistent effect", the W1–W3 sentence), and three serial-comma inconsistencies. Four "gives" remain.

### Findings

- [ERROR] manuscript_anonymized.tex:824 (B0094) — The sentence says "liquidity decline", but the paper's result is a decline in illiquidity (a liquidity gain). As written, it states the opposite of the finding.
  > reliable price effect. The liquidity decline at the disclosures and the
  Suggestion: "reliable price effect. The illiquidity decline at the disclosures and the volume surge at the close are consistent with ..."
- [WARN] manuscript_anonymized.tex:742 (B0083) — "whose" attaches grammatically to Harris and Gurel (the authors), not to the S&P 500 additions. This is a new comparison sentence.
  > Gurel (1986), whose announcement gains of more than 3\% were almost
  Suggestion: "The fading after the conditional announcement is consistent with temporary price pressure: in Harris and Gurel (1986), S\&P 500 additions gained more than 3\% on the announcement, and the gain was almost fully reversed after two weeks."
- [WARN] manuscript_anonymized.tex:456 (B0054; also lines 521–523, B0064) — "listed stocks" can mean exchange-listed stocks or stocks on FTSE's list. The whole paper uses "listed" in the exchange sense (lines 245, 1195).
  > average effect on likely constituents, including the 12 listed stocks
  Suggestion: Line 456: "average effect on likely constituents, including the 12 stocks on the preliminary list that FTSE did not include." Lines 521–524: "as expected when 12 of the 27 stocks on the preliminary list were never included: those that later entered the index became less illiquid by 0.43, 0.87 and 1.12 log points, the others by 0.11, 0.25 and 0.53."
- [WARN] manuscript_anonymized.tex:1061 (B0123) — The compacted window definition is hard to parse. W1's start is given in a parenthesis after its end, W2's start is missing, and W3's end is missing. The code (code/analysis_revision.R lines 101–104) assigns weeks by start date: W1 from the announcement to 31 December 2025, W2 after that to before 7 April 2026, and W3 from 7 April 2026.
  > FTSE screened the April 2026 list on data up to 31 December 2025, the
  Suggestion: "We split the period after the announcement into three screening windows, assigning weeks by their start date: W1 from 7 October to 31 December 2025, the last date of the data FTSE screened for the April 2026 list; W2 from 1 January to 6 April 2026; and W3 from 7 April 2026 to the end of the sample. These differ from the disclosure windows of Eq. (7)."
- [WARN] manuscript_anonymized.tex:838 (B0097) — "the persistent effect" has no clear referent, since only the rebalancing surge has been mentioned in the sentence.
  > foreign allocations (Raddatz et al., 2017) point the same way for the
  Suggestion: "H4 predicts a larger rebalancing surge for large constituents, whose index weights are larger, and benchmark-driven foreign allocations (Raddatz et al., 2017) suggest the same ordering for the persistent liquidity effect."
- [WARN] manuscript_anonymized.tex:99 (B0012) — "tested at the portfolio level for the common event dates" is ambiguous: it can mean testing on those dates or correcting for them.
  > abnormal returns (CARs). CARs are tested at the portfolio level for the
  Suggestion: "abnormal returns (CARs). We test CARs at the portfolio level to account for the common event dates (Brown \& Warner, 1985) and call them reliable only if significant at 5\% under all four benchmarks."
- [WARN] manuscript_anonymized.tex:391 (B0049) — There is a number disagreement: "A third treatment ... is the 27 stocks".
  > A third treatment, ``predicted constituents'', is the 27 stocks with the highest
  Suggestion: "A third treatment group, the ``predicted constituents'', consists of the 27 stocks with the highest pre-announcement trading value, 16 of which became constituents."
- [WARN] manuscript_anonymized.tex:206 (B0025) — A run-on sentence joins three claims with "and ... so ...;" (ARS style: one idea per sentence).
  > liquidity predicts returns in emerging markets, where segmentation from
  Suggestion: "Local market liquidity predicts returns in emerging markets, where segmentation from global capital is only partial (Bekaert et al., 2007). Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity. A liquidity gain for some stocks could therefore shift their cost of capital, although we do not measure that shift."
- [WARN] manuscript_anonymized.tex:900 (B0105) — The new comparison sentence repeats Section 2.2 (lines 172–174, "mainly through lower direct trading costs") and sits between the volatility-control result and its explanation. "By contrast" leaves the contrast implicit.
  > to 0.06, 0.08 and 0.12 percentage points (column 4). S\&P 500 additions,
  Suggestion: "to 0.06, 0.08 and 0.12 percentage points (column 4). The rise contrasts with S\&P 500 additions, whose liquidity gain came mainly through lower direct trading costs (Hegde \& McDermott, 2003)."
- [WARN] manuscript_anonymized.tex:123 (B0014; also line 360, B0205) — The serial comma appears here and at line 360, although the paper omits it everywhere else, for example "high, low and close prices" and "24%, 43% and 56%" (rule 5.4, downgraded to house-style consistency). Line 1326 is Elsevier's prescribed wording; keep it.
  > presents the data and design, Section 4 the results, and Section 5 the
  Suggestion: Line 123: "presents the data and design, Section 4 the results and Section 5 the". Line 360: "every disclosure, report all of them and call a CAR reliable when it is".
- [WARN] manuscript_anonymized.tex:753 (B0084; also lines 879 B0101, 1068 B0123, 1213 B0210) — "gives" is used for "yields/reports/provides" (rule 5.5). Line 194 ("give back") is idiomatic; keep it.
  > significant under three of four benchmarks (the matched benchmark gives
  Suggestion: Line 753: "(the matched benchmark yields \emph{t} = 1.91)". Line 879: "the last row reports the mean (standard error)". Line 1068: "which provides a reason other than liquidity". Line 1213: "and Table A.3 reports the liquidity change".
- [INFO] manuscript_anonymized.tex:355 (B0205) — "day -130 to -11 before each event" states the direction twice (a negative sign and "before").
  > returns. The estimation window runs from trading day −130 to −11 before
  Suggestion: "returns. The estimation window runs from trading day −130 to −11 relative to each event and excludes days ..."
- [INFO] manuscript_anonymized.tex:1068 (B0123) — Number style: "twelve" here, "12" at lines 456, 521, 1269 and in Table 9.
  > gives a reason other than liquidity for its later addition. The twelve
  Suggestion: "provides a reason other than liquidity for its later addition. The 12 November names changed little".
- [INFO] manuscript_anonymized.tex:60 (B0008) — Possessive on a non-person noun (rule 5.5).
  > Market classification decides which benchmarks a country's stocks can
  Suggestion: "Market classification decides which benchmarks the stocks of a country can enter,".
- [INFO] manuscript_anonymized.tex:1188 (B0140) — A sentence-level "which" has an unclear antecedent (carried over from round 1; the other new "which" clauses at lines 382, 1135 are correctly non-restrictive).
  > rather than with index trading, which is consistent with early
  Suggestion: "rather than with index trading. This timing is consistent with early communication bringing it forward; one event cannot show that earlier communication causes larger gains."
- [INFO] manuscript_anonymized.tex:67 (B0009) — "this" has no clear antecedent (ARS precision).
  > Existing evidence says little about this for frontier markets. Additions
  Suggestion: "Existing evidence says little about which stocks gain, and when, in frontier markets. Additions".
- [INFO] manuscript_anonymized.tex:108 (B0013) — The parenthetical "unlike Biktimirov and Afego (2026)" needs commas.
  > a pre-determined treatment list, and unlike Biktimirov and Afego (2026)
  Suggestion: "a pre-determined treatment list, and, unlike Biktimirov and Afego (2026), we follow liquidity stage by stage within one market."
- [INFO] manuscript_anonymized.tex:390 (B0049; also lines 520, 564, 602) — "never-named, never-included" is redundant with the definition at line 258, where the 328 never-named stocks already exclude all constituents. Table 3 observation counts confirm the ITT variant uses exactly those 328 stocks.
  > preliminary list, and keeps all other stocks (in a variant, only
  Suggestion: Line 390: "and keeps all other stocks (in a variant, only the 328 never-named stocks) as controls." At lines 520, 564 and 602, write "never-named controls" / "never-named HOSE stocks". Keep the double label if you want to stress that HCM, HDB, MCH, MSB, SSB and VPB are excluded; in that case say so once at line 391.

---

## 5. Figures & Tables

**Summary:** Every table and figure is called out in the body before it appears. Booktabs is used with no vertical rules. Both figures now use a common y-range for log Amihud, distinct colour and shape per group (blue circle, orange triangle, green square), unit-bearing axis titles, 95% CIs, light grids, no in-plot title, and notes that explain the dashed lines. Stars are defined in Table 2 and referenced in every other starred table. The remaining gaps are self-containment of four compacted notes, identical Table 7 headers, Table 3 header overflow, and stale figure paths in the Markdown source.

### Findings

- [WARN] manuscript_anonymized.tex:536 (B0066; log lines 605–617) — The Table 3 headers "Announcement", "Confirmation" and "Observations" overflow their 0.148 columns by 12.3, 4.7 and 3.9 pt and run into the neighbouring headers. TeX does not hyphenate the first word of a paragraph.
  > Announcement
  Suggestion: In the .tex, write `\hspace{0pt}Announcement`, `\hspace{0pt}Confirmation` and `\hspace{0pt}Observations` at lines 536, 538 and 544 (this enables hyphenation). Optionally, also change the column spec at line 531 to first column `0.2000` and the other five `0.1600`. In the Markdown pipe table B0066, shorten the dash run of the first column relative to the others to get the same widths.
- [WARN] manuscript_anonymized.tex:731 (B0082) — The Table 4 notes are not self-contained. "the four benchmarks of Eq. (5)": Eq. (5) defines the abnormal return, and the benchmarks are listed in the prose after it. The window unit is not stated. The table has no significance marks and no stated 5% threshold, so a reader cannot tell which cells the text calls "significant".
  > \emph{Notes}: CAR from Eq. (6) with the portfolio \emph{t}-statistic in
  Suggestion: "\emph{Notes}: CARs from Eq. (6), in percent, with the portfolio \emph{t}-statistic in parentheses. Windows are in trading days relative to the disclosure date (day 0). Benchmarks (Section 3.2): equal-weighted never-named stocks; matched controls weighted by their matching weights; never-named stocks in the top tercile of pre-period trading value; a market model estimated against the first benchmark. A CAR is significant at 5\% when [state the critical value and reference distribution used in the code]. Effective-date windows beyond +1 are not reported because the data end on 23 September 2026. Source: ..." The critical value must come from the code (author to fill in; not proposed here).
- [WARN] manuscript_anonymized.tex:917 (B0107) — Columns (2) and (4) have the identical header "CS spread", and column (5) "Amihud" does not show that it includes the volatility control. The distinction appears only in the notes.
  > (4) CS spread
  Suggestion: Headers: "(4) CS spread, volatility control" and "(5) Amihud, volatility control". Then the notes sentence "columns 4 and 5 control for volatility" can be deleted.
- [WARN] manuscript_anonymized.tex:1125 (B0131; also line 1308, B0213) — The Table 9 and Table A.3 notes define W1–W3 only by reference ("as defined in Section 5.2"), which is not self-contained. The in-text definition is itself ambiguous (G4).
  > week fixed effects; W1 to W3 as defined in Section 5.2. The two-stock
  Suggestion: "week fixed effects; W1: 7 October to 31 December 2025; W2: 1 January to 6 April 2026; W3: from 7 April 2026 (weeks assigned by start date). The two-stock". Use the same wording in the Table A.3 notes. Author to confirm the W2 start and the W3 end against code/analysis_revision.R lines 102–104.
- [WARN] manuscript_v8.md B0070, B0188 (tex lines 588, 600) — The Markdown source embeds `figures/figure1_event_study.png` and `figures/figure2_itt_event_study.png`. The copies of those names in the repository (output/figure1_event_study.png, ars/stage2_write/figures/*.png) have different MD5 hashes from the submitted submission/figures/Figure_1.png and Figure_2.png, so they are older versions. A DOCX rebuilt from v8.md could embed stale figures (old colours and y-ranges).
  > `![](figures/figure1_event_study.png)`
  Suggestion: B0070: `![](figures/Figure_1.png)`; B0188: `![](figures/Figure_2.png)`, with the build copying submission/figures/ (identical to output/figures/, verified by MD5).
- [INFO] manuscript_anonymized.tex:589 (B0071) — The Figure 1 note says "Coefficients δ_m of Eq. (8)" but does not say that panel A is log Amihud and panel B is log trading value. The panel strips say so, but the note should too.
  > {\small \emph{Note}: Coefficients \(\delta_m\) of Eq. (8), with the same
  Suggestion: "{\small \emph{Note}: Coefficients \(\delta_m\) of Eq. (8) for log Amihud illiquidity (panel A) and log trading value (panel B), with the same interactions for named-but-excluded stocks; ..."
- [INFO] manuscript_anonymized.tex:878 (B0101) — The last row of Table 6 has no significance marks even for the 18-stock segment (0.645, SE 0.150), but the notes say marks are omitted only for the three-stock segments.
  > outcomes); the last row gives the mean (standard error) of abnormal log
  Suggestion: "outcomes); the last row reports the mean (standard error) of abnormal log trading value, without significance marks. Clustering and significance marks as in Table 2; marks are omitted for the three-stock segments."
- [INFO] manuscript_anonymized.tex:808 (B0093) — The Table 5 notes do not say how the named-but-excluded row is estimated (Eq. (9) is written for Constituent_i).
  > \emph{Notes}: Eq. (9) over the sessions from 6 August to 23 September
  Suggestion: Add: "The last row replaces \(\mathrm{Constituent}_i\) with an indicator for the 14 named-but-excluded stocks."
- [INFO] manuscript_anonymized.tex:562 (B0067) — The Table 3 notes do not state the control group of the predicted-constituent row. Its observation count (35,752, the same as "ITT (27), all controls") implies all other stocks.
  > \emph{Notes}: Log Amihud unless stated. The ITT group is FTSE's
  Suggestion: Add: "The predicted row uses all other stocks as controls." (author to confirm).
- [INFO] manuscript_anonymized.tex:286 (B0038; also line 1100, B0127) — The header "log trading value" and the panel title "log Amihud by ..." start lowercase, unlike all other headers. The Table 1 unit is also implicit: weekly log of VND billion, which is a different definition from Table A.1's daily log(1 + VND billion).
  > log trading value
  Suggestion: Table 1 header: "Log trading value". Notes: "Weekly means; Amihud as in Eq. (1) with traded value in VND billion; log trading value is \(\mathrm{TV}_{iw}\) of Eq. (4); ...". Panel B title: "Panel B. Log Amihud by FTSE screening window". Author to confirm that Table 1 uses \(\mathrm{TV}_{iw}\).
- [INFO] submission/figures/Figure_1.png, Figure_2.png — The tick labels use an ASCII hyphen-minus ("-10", "-0.5") while the text and tables use U+2212.
  > y-axis ticks -1.5 ... 0.5; x-axis ticks -10, -5
  Suggestion: In code/figure1.R and code/figure2.R, add `scale_y_continuous(labels = scales::label_number(style_negative = "minus"))` and the same for `scale_x_continuous`, then re-export.
- [INFO] manuscript_anonymized.tex:585 (B0069–B0071, B0187–B0189) — Carried over: the figures are raster PNG (600 dpi, accepted by the venue) although vector PDFs exist, both use `[p]` (float page; rule 4.6), and numbers are hard-coded (no `\label`/`\ref`). This is accepted for the DOCX-first build.
  > \begin{figure}[p]
  Suggestion: For a LaTeX-native build only: `\begin{figure}[t]` and `\includegraphics[width=0.95\textwidth]{Figure_1.pdf}`.

---

## 6. Statistical Relevance

**Summary:** Uncertainty is reported throughout: clustered SEs, portfolio t-statistics with the independence assumption stated, a wild bootstrap, randomization inference, joint pre-trend F-tests, and 95% CIs in both figures. The reasons for omitting marks (Tables 6 and 9) are stated. The spot-checks reconcile with output/revision/*.csv, for example Table 9 panel A against t8_named_excluded.csv and the trend estimates against t7_robustness.csv. Three statements need verification: two definitions of "top tercile", the count of post-effective-date days, and the month -13 bin.

### Findings

- [WARN] manuscript_anonymized.tex:342 (B0203; vs lines 416 B0050, 616 B0073, 1004 B0115, 1040 B0192) — Line 342 has "the 110 never-named stocks in the top tercile of pre-period trading value" (benchmark 3); lines 416 and 616 have "the 85 never-named stocks in the top tercile ... among all 366 stocks" (randomization pool). The code confirms two different tercile bases: code/analysis_revision.R line 207 takes the tercile within never-named stocks, and line 142 plus output/revision2_log.txt ("RI pool size: 85") take the tercile among all stocks. The text states only one base.
  > top tercile of pre-period trading value, and a market model whose
  Suggestion: Line 342–343: "the equal-weighted mean of the 110 never-named stocks in the top tercile of pre-period trading value among never-named stocks, and a market model whose". No number changes.
- [WARN] manuscript_anonymized.tex:1195 (B0141) — "Only three trading days follow the effective date". 21 September 2026 is a Monday and the data end on Wednesday 23 September, so two sessions follow the effective date, and three include it. The Table 4 note ("windows beyond +1 are not reported") is consistent with either count. Author to verify.
  > The sample omits stocks delisted before 24 September 2026. Only three
  Suggestion: "Only three trading sessions, 21 to 23 September 2026, are observed from the effective date on, and the first tranche carried 10\% of the eventual weight, so ..."
- [WARN] manuscript_anonymized.tex:569 (B0068; Figure 1 and Figure 2, leftmost point) — The event study starts at m = -13 (September 2024) although the sample starts on 1 October 2024. Because weeks are dated by their Monday (code/analysis.R lines 58, 71), month -13 is a single week (30 September to 4 October 2024) holding only 1 to 4 October trading days. The first plotted coefficient therefore rests on one week. Author to verify.
  > Figure 1 plots the coefficients \(\delta_m\) of Eq. (8). Before the
  Suggestion: If confirmed, add to both figure notes: "Month −13 contains only the week beginning 30 September 2024." (combined with the M4 definition "week \(w\) starts in month \(m\)").
- [INFO] manuscript_anonymized.tex:1011 (B0116) — The trend coefficient and its SE are reported at different precision and without a unit. Output/revision/t7_robustness.csv gives -0.00023 (SE 0.00276).
  > constituent-specific linear trend (−0.0002 per week, standard error
  Suggestion: "constituent-specific linear trend (−0.0002 log points per week, standard error 0.003)". The author may choose to report both values at the same precision from the CSV; this report proposes no number.
- [INFO] manuscript_anonymized.tex:477 (B0060; also lines 638–640 B0076, 741–744 B0083, 821–824 B0094, 900–902 B0105) — The new comparison sentences characterize prior studies: Hegde and McDermott "sustained liquidity increase"; Dong et al. "short-term excess returns around the announcement"; Harris and Gurel "announcement gains of more than 3% ... almost fully reversed after two weeks" and "temporary price rises when index funds buy". These are claims about source content that cannot be checked from the repository.
  > increase that Hegde and McDermott (2003) document after S\&P 500
  Suggestion: No wording change. Route to the Stage 4.5/6 citation-content check (claim_verification_protocol) before submission.
- [INFO] manuscript_anonymized.tex:296 (B0038) — Carried over: Table 1 reports means without dispersion. It is descriptive, not a stochastic experiment.
  > Constituents & 24 & 1,248 & 0.00017 & 6.82 & 0.57 & 1.40 \\
  Suggestion: Optional: report standard deviations in parentheses and change the notes to "Weekly means (standard deviations)".

---

## PDF generation

`python3 /root/.claude/skills/proofreading/scripts/generate_report_pdf.py proofreading_report_v8.md` failed with `! LaTeX Error: File 'fontawesome5.sty' not found.` A copy of the template without the fontawesome5 dependency is at `ars/stage5b_proofread/round2/report_latex_nofa.tex` (only line 19, `\usepackage{fontawesome5}`, removed; the installed template is untouched). The script hard-codes its template path (`TEMPLATE = .../templates/report_latex.tex`) and accepts only `input`, `-o`, `--engine` and `--check-deps`. It has no template argument, so the copy was not used and no PDF was produced. This Markdown report is complete and is the deliverable.
