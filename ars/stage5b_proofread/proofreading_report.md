# Proofreading Report — Who gains from a market upgrade? Stock liquidity and prices around Vietnam's FTSE Russell reclassification

**Date:** 2026-09-24  
**Source:** /home/user/B-i-FTSE2/submission/manuscript_anonymized.tex (line numbers). Block IDs refer to /home/user/B-i-FTSE2/ars/stage4_5_integrity/correction_round3/manuscript_v7.md. Figures: /home/user/B-i-FTSE2/submission/figures/Figure_1.png, Figure_2.png.

**Mode:** Report mode. No manuscript file was edited.

### Skill load record

| File (read in full with the Read tool) | First heading |
|---|---|
| /root/.claude/skills/proofreading/SKILL.md (Checks 1 to 6) | `# Paper Proofreading` |
| /root/.claude/skills/proofreading/templates/output_template.md | `# Proofreading Report — {{paper_title}}` |
| /root/.claude/skills/academic-paper/references/writing_quality_check.md | `# Writing Quality Check` |
| /root/.claude/skills/academic-paper/references/academic_writing_style.md | `# Academic Writing Style Guide` |

### Adaptations applied (stated, not silently dropped)

1. **Section mapping.** The template orders the sections differently from SKILL.md. Template section 1 (Abbreviations) = SKILL Check 6; 2 (Math) = Check 2; 3 (Introduction Structure) = Check 1 (Paper Structure: abstract, introduction, related work, hypotheses, conclusion); 4 (Grammar & Style) = Check 5; 5 (Figures & Tables) = Check 4; 6 (Statistical Relevance) = Check 3. Rule numbers cited below (for example "rule 4.9") are SKILL.md numbers.
2. **Venue.** The venue is Finance Research Open (Elsevier), with APA 7 author-year citations. The abstract limit is 250 words (rule 1.1 default is 150). The abstract has 210 words, so there is no finding.
3. **Tables and references.** Tables are pandoc longtables generated from Markdown. Booktabs, alignment, `\label` and `\ref` items therefore concern the generated .tex, and each fix is stated for the Markdown source. Table and figure numbers are hard-coded ("Table 3", "Figure 1") because the submission is DOCX-first. Missing `\label`/`\ref` (rules 4.1, 4.2) is reported as INFO, not ERROR.
4. **Uncertainty.** Regression standard errors in parentheses and 95% CIs in the figures count as the uncertainty reporting for Check 3. Rules written for stochastic ML experiments (seeds, runs) do not apply.
5. **Structure rules.** Rule 1.3 asks that contributions be backed by "theorems, proofs, algorithms". It does not apply to an empirical finance paper. Hypotheses H1 to H4 are in Section 2.4 (rule 1.7).
6. **ARS precedence where the checklist conflicts:**
   - Voice: ARS (social sciences) prefers active voice with "we", and passive voice is acceptable in methods. Rule 5.1 therefore produced no findings.
   - Tense: ARS uses past tense for methods and results. This overrides rule 5.2, which asks for present tense throughout, so past-tense results are not flagged.
   - Contribution list: ARS prose with First to Fourth markers overrides the bulleted list of rule 1.3 (INFO only).
   - Positioning in the literature review: rule 1.6 treats self-reference in the literature review as an ERROR. Positioning against the closest paper is standard in finance, so this is downgraded to WARN.
   - Oxford comma: the paper omits it consistently, and the venue does not require it. Rule 5.4 is downgraded from ERROR to one consolidated WARN.
   - Numbers repeated from tables: repeating table numbers in the text is ARS/finance practice. Rule 5.9 is reported as INFO.
   - Caption periods: Elsevier sets table and figure titles without a final period. Rule 4.3 is downgraded to INFO.
7. **Not applicable (checked, no findings):**
   - rule 1.5 (no problem-statement section)
   - rule 2.6 (all symbols are scalars; notation convention "unknown / not applicable")
   - rules 2.8 and 2.10 (no custom macros; displayed equations are unnumbered)
   - rule 4.12 (not IEEE)
   - rule 4.13 (no algorithms)
   - rule 5.11 (no physical units, so `siunitx` is not needed; the numeric filters in Section 3 are sample definitions, not tunable method parameters)
   - rule 5.7 (no unhyphenated compound adjectives found)
   - rule 5.12 (the First to Fourth markers in Section 3.4 sit in consecutive one-item paragraphs)
   - ARS Section A flagged terms (none found; "robustness" is a statistical term)
   - em dashes (none)
8. **Scope.** No finding proposes changing a number, a citation, or the strength of a claim. Where a number or claim looks inconsistent with a table or figure, the finding flags it for the author to verify. Minus signs are written as ASCII hyphens in this report. Use U+2212 in the manuscript (see finding M4).

---

## Scorecard

| # | Check                   | Errors | Warnings | Info | Total |
|---|-------------------------|--------|----------|------|-------|
| 1 | Abbreviations           | 3      | 2        | 6    | 11    |
| 2 | Math Symbols & Notation | 2      | 2        | 1    | 5     |
| 3 | Introduction Structure  | 1      | 3        | 5    | 9     |
| 4 | Grammar & Style         | 2      | 9        | 5    | 16    |
| 5 | Figures & Tables        | 1      | 9        | 4    | 14    |
| 6 | Statistical Relevance   | 0      | 4        | 3    | 7     |
|   | **Total**               | **9**  | **29**   | **24**| **62** |

---

## Overall Assessment

The manuscript is in strong shape for submission.

- **Numbers:** a spot-check of the headline percentages against the log coefficients and of the t-statistics against the estimates and standard errors found no conflict, and all group counts reconcile.
- **Tables and figures:** every table and figure is called out in the text before it appears.
- **Uncertainty:** reporting is complete throughout.
- **Weakest area: notation and self-containment.** The error term and the coefficient in the baseline equation are never defined. Several tables use significance stars, "FE" or "SE" without defining them. Three abbreviations (VND, VCI, UPCoM) are never expanded.
- **Claims to verify:** two sentences look inconsistent with the evidence they summarize, "of similar size in every specification" (Table 8) and "the two months with the largest positive deviations" (Figure 1).
- **Structure:** the abstract has no explicit gap statement.

### Top Issues to Address

1. **[ERROR] Check 2.2** — Eq. at line 417 (B0047): the error term and the coefficient in the baseline specification are never defined, and the treatment indicator is never defined explicitly (M1).
2. **[WARN] Check 3.3** — Line 1121 (B0112): "negative and of similar size in every specification" conflicts with Table 8 rows whose coefficients are about half the baseline (T1).
3. **[ERROR] Check 1.1** — The abstract (B0003) has no explicit motivation or gap sentence (S1).
4. **[ERROR] Check 6.3** — VND, VCI and UPCoM are never expanded. "VCI" is both the data vendor and a constituent ticker (A1 to A3).
5. **[WARN] Check 4.3** — Significance stars are undefined in the notes to Tables 3, 5, 6, 7, 8 and 9. "FE" and "SE" appear in tables without definition (F2, A4, A5).
6. **[ERROR] Check 4.3** — The Figure 2 note does not explain the dashed vertical lines (F1). Figures 1 and 2 also use different y-axis ranges for the same metric and the same colour and marker for different groups (F5, F7).

---

## 1. Abbreviations

**Summary:** The abstract uses no abbreviations other than brand names, so it is self-contained. HOSE, ITT, CAR and SMD are introduced correctly, and the articles ("an MSCI", "a CAR") and plurals ("CARs") are correct. VND, VCI and UPCoM are never expanded, "FE" and "SE" appear only in tables, and the ITT and CAR full terms are used before the abbreviations are introduced. Stock tickers (BID, GEE, and others) are treated as identifiers, not abbreviations, and only an optional expansion is suggested for them.

### Findings

- [ERROR] manuscript_anonymized.tex:300 (B0034; fix at line 112, B0012) — "VND" is used bare (lines 300, 321, 341, 358, 369, 1493). The currency is spelled out at line 112 without the abbreviation.
  > and a median price of at least VND 1,000, which leaves
  Suggestion: At line 112, replace "computed on traded value in Vietnamese dong;" with "computed on traded value in Vietnamese dong (VND);".
- [ERROR] manuscript_anonymized.tex:298 (B0034) — "VCI" (the data vendor) is never expanded. The same string is also a constituent ticker (lines 1183, 1514), which is ambiguous.
  > The data come from the VCI feed through the open-source vnstock library.
  Suggestion: "The data come from the Vietcap Securities (VCI) price feed through the open-source vnstock library."
- [ERROR] manuscript_anonymized.tex:315 (B0035) — "UPCoM" is never expanded (it is used again at line 1258, B0123).
  > traded on the UPCoM market until 6 January 2025 and on HOSE from
  Suggestion: "traded on the Unlisted Public Company Market (UPCoM) until 6 January 2025 and on HOSE from"
- [WARN] manuscript_anonymized.tex:560 (B0062) — "FE" is never introduced. It is also used at line 1145 (B0114, Table 8).
  > Stock and week FE & Yes & Yes & Yes & Yes & Yes & Yes \\
  Suggestion: Change the row label to "Stock and week fixed effects". In Table 8, change "Size-tercile × week FE" to "Size-tercile-by-week fixed effects", which matches the wording at line 449.
- [WARN] manuscript_anonymized.tex:1035 (B0100) — "SE" is not introduced, and it is inconsistent with "Std. error" in Table 5, panel B (line 945).
  > Abnormal log trading value, 18 Sep 2026 (mean, SE)
  Suggestion: "Abnormal log trading value, 18 Sep 2026 (mean, standard error)"
- [INFO] manuscript_anonymized.tex:96 (B0010) — The full term "intention-to-treat" is used at lines 96, 107 and 139 (B0010, B0011, B0013) before "(ITT)" is introduced at line 312 (B0035).
  > estimate intention-to-treat effects that do not depend on FTSE's later
  Suggestion: At line 96, write "estimate intention-to-treat (ITT) effects that do not depend on FTSE's later". At line 107, write "we estimate ITT effects for the preliminary list". At line 139, write "is why we report ITT effects". At line 312, write "The ITT group consists of the 27 HOSE" so that the term is introduced only once in the body.
- [INFO] manuscript_anonymized.tex:585 (B0065; also B0187 line 660, B0080 line 760) — The table and figure titles spell out "Intention-to-treat" after ITT has been introduced. This is acceptable because titles should be self-contained. Adding the abbreviation links the titles to the text.
  > Table 3. Intention-to-treat and predicted-constituent estimates
  Suggestion: "Table 3. Intention-to-treat (ITT) and predicted-constituent estimates (log Amihud unless stated)". Apply the same change to the Figure 2 title and the Table 4 panel B title.
- [INFO] manuscript_anonymized.tex:115 (B0012) — The full term "cumulative abnormal returns" appears here before "(CARs)" is introduced at line 399 (B0044).
  > cumulative abnormal returns at the portfolio level, which accounts for
  Suggestion: At line 115, write "cumulative abnormal returns (CARs) at the portfolio level, which accounts for". At line 399, write "We therefore test CARs on the equal-weighted portfolio of the group".
- [INFO] manuscript_anonymized.tex:112 (B0012) — "CS" is used in table headers (lines 343, 536, 1088) but is defined only in the Table 1 notes, never in the body.
  > Schultz (2012) high-low spread, volatility and abnormal returns. For
  Suggestion: "Schultz (2012) high-low spread (CS spread), volatility and abnormal returns. For"
- [INFO] manuscript_anonymized.tex:448 (B0050) — "standardized mean difference" is used in the body, while Table A.1 uses "SMD", defined only in its notes.
  > Matching reduces the standardized mean difference in
  Suggestion: "Matching reduces the standardized mean difference (SMD) in"
- [INFO] manuscript_anonymized.tex:172 (B0018) — Tickers are used without company names except PLX and HUT. GEE and BSR carry the argument of Section 5.2.
  > and added BID, FPT, NVL, GEE and BSR (The Investor, 2026b). On Friday 21
  Suggestion: "and added BID, FPT, NVL, Gelex Electricity (GEE) and Binh Son Refining and Petrochemical (BSR) (The Investor, 2026b). On Friday 21"

---

## 2. Math Symbols & Notation

**Summary:** Detected notation convention: unknown / not applicable (all symbols are scalars; there are no vectors, matrices or sets). The two displayed equations are grammatically integrated and punctuated, and operator names use `\mathrm{}`. The baseline equation leaves the error term and the coefficient undefined. Statistical symbols (p, t, F) appear bare in prose, and the letter t has two meanings.

### Findings

- [ERROR] manuscript_anonymized.tex:417 (B0047; where-clause B0048, lines 419–424) — The where clause never defines `\varepsilon_{iw}` or `\beta_k`. `\beta_k` is first named at line 472 (B0053). `\mathrm{Constituent}_i` is also never defined explicitly.
  > ... \beta_k \left(\mathrm{Constituent}_i \times P_{kw}\right) + \varepsilon_{iw},
  Suggestion: Extend the where clause at lines 419–424 to: "where \(y_{iw}\) is a liquidity measure for stock \(i\) in week \(w\), \(\alpha_i\) and \(\lambda_w\) are stock and week fixed effects, \(\mathrm{Constituent}_i\) equals one for the 24 constituents and zero otherwise, \(P_{1w}\), \(P_{2w}\) and \(P_{3w}\) indicate the announcement window (...), the confirmation window (...) and the list-and-rebalancing window (...), \(\beta_k\) is the change in the outcome of constituents relative to never-named stocks in window \(k\), and \(\varepsilon_{iw}\) is the error term." Keep the window dates as they are.
- [ERROR] manuscript_anonymized.tex:518 (B0060; also B0068, B0073, B0076, B0083, B0084, B0087, B0093, B0115, B0118, B0078) — Statistical symbols are typeset as plain letters outside math mode (rule 2.4). Examples: "p = 0.002" (lines 518, 520, 521), "F = 6.66, p" (634–636, 643), "one-sided p" (680), "t between" (700–701, 869), "t = 1.91" (878), "t = 6.84", "p = 0.057" (905–906), "t = 3.54" (960), "p = 0.002" (1180), "p < 0.001" (1208), and "portfolio t" in the Table 4 panel titles (715, 761, 804) and header (732). APA 7 also italicizes these symbols.
  > announcement (-0.012 log points per week, p = 0.002), the
  Suggestion: In the Markdown source, write `*p* = 0.002`, `*t* = 6.84` and `*F* = 6.66`. Pandoc emits `\emph{p}` and DOCX italics. For example, "(-0.012 log points per week, *p* = 0.002)".
- [WARN] manuscript_anonymized.tex:848 (B0082) — The letter t denotes the day index in `R_{it}` (lines 368–373, B0041–B0043) and the portfolio t-statistic here.
  > \(t = \mathrm{CAR} / (\sigma \sqrt{L})\), where \(\sigma\) is the
  Suggestion: "The portfolio t-statistic equals \(\mathrm{CAR} / (\sigma \sqrt{L})\), where \(\sigma\) is the"
- [WARN] manuscript_anonymized.tex:512 (B0060; all result blocks and tables) — Negative numbers are typed with an ASCII hyphen ("-0.39", "-0.012", "-130 to -11"). In text mode this renders as a hyphen, not a minus sign.
  > column 1, reports coefficients of -0.39, -0.89 and -1.13 log points,
  Suggestion: Use the Unicode minus sign U+2212 in the Markdown source (for example "coefficients of U+2212 0.39", typed as the single character) so both the DOCX and the fontspec PDF render a true minus. In hand-edited .tex, write `$-0.39$`.
- [INFO] manuscript_anonymized.tex:371 (B0042; also line 848, B0082) — `R_{it}` and `\mathrm{VAL}_{it}` (and, in the Table 4 notes, `\sigma` and `L`) are defined only in a where clause after the formula. This is acceptable, but defining them before the formula is preferred.
  > we define illiquidity for stock \(i\) on day \(t\)
  Suggestion: Lines 368–369: "we define illiquidity for stock \(i\) on day \(t\), with log return \(R_{it}\) and traded value \(\mathrm{VAL}_{it}\) in VND, as". Then shorten line 373 to "Traded value, rather than share volume, makes the ratio".

---

## 3. Introduction Structure

**Summary:** The introduction has explicit motivation, gap ("Existing evidence answers these questions poorly..."), approach, contribution ("The paper makes one contribution"), and a present-tense roadmap whose section numbers match Sections 2 to 6. Hypotheses H1 to H4 are stated in Section 2.4 before the results, and the literature review is organized by theme. The abstract has no explicit gap sentence, novelty is stated only in Section 2.3, and H1 and H3 are never evaluated by name in the results.

### Findings

- [ERROR] manuscript_anonymized.tex:20 (B0003) — The abstract has no explicit motivation or gap statement (rule 1.1). It moves from the event straight to the design. Adding one sentence brings it to about 234 of the 250 words allowed.
  > FTSE Russell reclassified Vietnam from frontier to secondary emerging
  Suggestion: After "...between October 2025 and September 2026." (line 21), insert: "Such upgrades promise new foreign demand, but studies based on aggregate indices or country-level flows do not show which stocks gain or when."
- [WARN] manuscript_anonymized.tex:123 (B0013) — Novelty is not stated in the introduction (rule 1.2). The bounded claim appears only in Section 2.3 (lines 245–249, B0024).
  > information available before the upgrade. Four findings support the
  Suggestion: "information available before the upgrade. In a search bounded to Crossref records and the literature cited here, we found no earlier stock-level estimate of this effect with a comparison group and a pre-determined treatment list. Four findings support the"
- [WARN] manuscript_anonymized.tex:243 (B0024; also lines 256–257 and 265–267, B0025) — The literature review describes the authors' own design (rule 1.6). This is downgraded from ERROR because positioning against the closest paper is standard in finance.
  > demand rather than to trading pressure or liquidity. Our design
  Suggestion: Delete "Our design complements theirs: it follows liquidity stage by stage and compares index stocks with non-index stocks of the same market." from lines 243–245. In B0013 (line 123), after the novelty sentence above, add: "Relative to Biktimirov and Afego (2026), the design follows liquidity stage by stage and compares index stocks with non-index stocks of the same market."
- [WARN] manuscript_anonymized.tex:583 (B0064; also line 895, B0085) — H1 and H3 are never evaluated by name (rule 1.7). H2 is evaluated at line 522 and H4 at line 1008.
  > trading value alone, gained 0.25, 0.59 and 0.74 log points.
  Suggestion: End B0064 with "These estimates support H1." End the Table 4 discussion at line 890 (B0084) with "These results support H3 for the announcement and the confirmation but not for the constituent list, and the first index tranche added no reliable price effect."
- [INFO] manuscript_anonymized.tex:50 (B0007) — The introduction opens with the result paragraph before the motivation (B0008), which deviates from rule 1.2. Leading with the finding is a finance and ARS convention.
  > Vietnam's market upgrade raised the liquidity of likely index stocks
  Suggestion: No change recommended. If the editor prefers motivation first, move B0007 unchanged to follow B0008.
- [INFO] manuscript_anonymized.tex:120 (B0013) — The contributions are written as prose with First to Fourth markers, not as a bulleted list. The items do not begin with "We" (rule 1.3). ARS prose convention takes precedence.
  > The paper makes one contribution: it decomposes the stock-level
  Suggestion: No change. Optional: "We make one contribution: we decompose the stock-level".
- [INFO] manuscript_anonymized.tex:142 (B0014) — The roadmap has no standard linking phrase (rule 1.4). It is otherwise complete and in the present tense.
  > Section 2 describes the setting, reviews the literature and states the
  Suggestion: "The remainder of the paper is organized as follows. Section 2 describes the setting, reviews the literature and states the"
- [INFO] manuscript_anonymized.tex:1443 (B0141) — The conclusion raises survivorship (delisted stocks omitted), which Section 3.1 never mentions (rule 1.8).
  > The study has limits. The sample uses stocks listed on 24 September
  Suggestion: At line 302 (B0034), after "which leaves 366 stocks.", add "Because the sample consists of stocks listed on 24 September 2026, it omits stocks delisted during the period."
- [INFO] manuscript_anonymized.tex:991 (B0097) — The results section restates the channel logic from Section 2.4 (rule 1.9).
  > rise with capitalization, so the price-pressure channel predicts a
  Suggestion: Replace "Index weights, and therefore passive purchases, rise with capitalization, so the price-pressure channel predicts a larger rebalancing surge for large-capitalization constituents." with "H4 predicts a larger rebalancing surge for large-capitalization constituents, whose index weights are larger."

---

## 4. Grammar & Style

**Summary:** Detected English variant: British with Oxford -ize spelling ("favour", "centres", "artefact", "neighbour" alongside "standardized", "randomization", "capitalization", "winsorize"). There is one deviation ("organise"). The prose is clear and concise. It has no em dashes, no first-person singular, and no ARS-flagged vocabulary. The main issues are one comma splice, hypotheses written in the past tense, "gives" used for "yields", possessives on non-person nouns, and repeated trend-adjusted numbers.

### Findings

- [ERROR] manuscript_anonymized.tex:1552 (B0155) — The -ise spelling breaks the Oxford -ize convention used elsewhere ("standardized", "capitalization"). The phrase "in order to" is Elsevier's prescribed declaration wording, so keep it.
  > in order to organise the analysis code, draft text, simulate peer review
  Suggestion: "in order to organize the analysis code, draft text, simulate peer review"
- [ERROR] manuscript_anonymized.tex:128 (B0013) — Comma splice.
  > post-announcement drift, the constituent list did not. Second, prices
  Suggestion: "post-announcement drift; the constituent list did not. Second, prices"
- [WARN] manuscript_anonymized.tex:444 (B0050; the pattern recurs throughout, for example lines 21, 28–29, 296) — The Oxford comma is omitted consistently (rule 5.4, downgraded from ERROR as house style). Only one list is ambiguous: "price and return volatility" can be read as volatility of both price and return.
  > traded value, price and return volatility (Ho et al., 2007); because
  Suggestion: "return volatility, price and traded value (Ho et al., 2007); because". The reordering removes the ambiguity without adding one serial comma. If you adopt the Oxford comma throughout instead, the abstract line 28 becomes "24\%, 43\%, and 56\%".
- [WARN] manuscript_anonymized.tex:277 (B0028–B0031, lines 277–288) — The hypotheses are written in the past tense as if they were observed outcomes. They should be stated as predictions. The strength of each claim is unchanged.
  > H1. After the reclassification announcement, stocks likely to enter the
  Suggestion:
  - "H1. After the reclassification announcement, stocks likely to enter the index become less illiquid than other HOSE stocks."
  - "H2. The liquidity gap widens at each later disclosure that resolves uncertainty about the upgrade and its constituents."
  - "H3. Likely constituents earn abnormal returns at the disclosures, and the first index tranche adds no further price effect."
  - "H4. The rebalancing session produces a trading-value surge for constituents, and not for excluded stocks, that scales with index weight."
- [WARN] manuscript_anonymized.tex:514 (B0060; also 878 B0084, 960 B0093, 1193 B0116, 1235 B0120, 1260 B0123) — "gives" is used in the sense of "yields" (rule 5.5).
  > matched sample, with each control weighted by its matching weight, gives
  Suggestion: Replace "gives" with "yields" in each instance, for example "... weighted by its matching weight, yields smaller declines" and "gives a coefficient of 0.04" becoming "yields a coefficient of 0.04".
- [WARN] manuscript_anonymized.tex:509 (B0060 and others) — Possessive "'s" is used on non-person nouns (rule 5.5). Proper names ("FTSE's", "Vietnam's") are left as they are.
  > Constituents' Amihud illiquidity fell relative to never-named stocks in
  Suggestion:
  - 509 (B0060): "The Amihud illiquidity of constituents fell"
  - 628 (B0068): "The monthly Amihud coefficients of constituents"
  - 670 (B0072): "The trading value of constituents rose"
  - 903 (B0087): "the log trading value of constituents rose"
  - 1382 (B0135): "The prices of constituents rose"
  - 488 (B0056): "the liquidity of the comparison group"
  - 909, 957, 1042 (B0087, B0093, B0101): "the mean of each stock"
  - 1321 (B0129): "and to its own pre-announcement level"
  - 1364 (B0132): "the effect of the upgrade"
  - 179/181/184 (B0018): "the investability weight of each security", "the weight of a security", "The index weight of a constituent"
  - 1441 (B0140): "the outcome for an issuer"
- [WARN] manuscript_anonymized.tex:1409 (B0138; also line 1386, B0135) — A comparative claim has no number in the same sentence (rule 5.6).
  > The liquidity gain was largest for the three large-capitalization stocks
  Suggestion: "The liquidity gain was largest for the three large-capitalization stocks (-2.20 log points in the list window, against -0.82 and -1.00; Table 6)". At line 1386, write "largest for the largest constituents (abnormal log trading value of 1.23, against 0.98 and 0.65)".
- [WARN] manuscript_anonymized.tex:673 (B0072; repeated at lines 1209–1211, B0118) — The trend-adjusted numbers and the "association" sentence are stated twice (rule 5.9).
  > 0.39 and 0.43 log points (Section 5), and we describe the trading-value
  Suggestion: At lines 673–675, write "Section 5.1 reports trend-adjusted effects, and we describe the trading-value result as an association." Keep the numbers in B0118.
- [WARN] manuscript_anonymized.tex:80 (B0009) — "cannot" appears without a citation (rule 5.10). The claim is a property of aggregate data, so the justification belongs in the sentence. The own-limitation uses at lines 1437, 1446, 1447 and 1449 are appropriate.
  > 2017), which cannot separate the stocks an upgrade targets from
  Suggestion: "2017), which, being aggregated across stocks, cannot separate the stocks an upgrade targets from"
- [WARN] manuscript_anonymized.tex:580 (B0064) — "gained ... log points" is used for a fall in log Amihud. The direction is ambiguous next to Table 3's negative signs.
  > later entered the index gained 0.43, 0.87 and 1.12 log points, while
  Suggestion: "later entered the index became less illiquid by 0.43, 0.87 and 1.12 log points, while listed stocks that did not enter became less illiquid by 0.11, 0.25 and 0.53, the last significant at 5\%. The 27 predicted constituents, chosen by pre-period trading value alone, became less illiquid by 0.25, 0.59 and 0.74 log points."
- [WARN] manuscript_anonymized.tex:1071 (B0105; also line 1074) — The unit changes from "percentage points" (line 1070) to "points".
  > in the weighted matched sample, from a pre-period mean of 0.57\%. With
  Suggestion: Line 1071: "and by 0.11 to 0.14 percentage points". Line 1074: "the increase shrinks to 0.06, 0.08 and 0.12 percentage points".
- [INFO] manuscript_anonymized.tex:985 (B0096; also line 1005, B0098) — Tense: this heading uses the present tense while the other results headings use the past ("became", "moved", "produced", "rose"). ARS past tense for results is followed.
  > \subsection*{4.4 The rebalancing surge rises with FTSE size
  Suggestion: "4.4 The rebalancing surge rose with FTSE size segment". At line 1005, write "The rebalancing surge rose monotonically with segment".
- [INFO] manuscript_anonymized.tex:994 (B0097; also line 1435, B0140) — "which" clause review (rule 5.4). All 17 relative "which" clauses (lines 115, 179, 204, 212, 301, 313, 399, 406, 428, 642, 994, 1045, 1110, 1252, 1263, 1359, 1435, 1494) are non-restrictive and correctly take a comma. Two are sentence-level and have an ambiguous antecedent.
  > (Raddatz et al., 2017), which points the same way for the persistent effect.
  Suggestion: Line 994: "(Raddatz et al., 2017); this points the same way for the persistent effect." Line 1435: "rather than with index trading. This timing is consistent with clear and early communication of reclassification steps bringing the response forward; one event cannot show that earlier communication causes larger gains."
- [INFO] manuscript_anonymized.tex:93 (B0010) — A sentence opens with "And" (ARS formality).
  > comparison group. And FTSE published lists of eligible stocks before it
  Suggestion: "comparison group. Finally, FTSE published lists of eligible stocks before it"
- [INFO] manuscript_anonymized.tex:1188 (B0116; also 1193 B0116, 1223–1224 B0192) — Numbers from Table 8 are repeated in the text right after the table (rule 5.9). This is kept as finance practice.
  > positive deviations, changes the estimates to -0.35, -0.85 and -1.09. A
  Suggestion: Optional shortening: "positive deviations, changes each estimate by 0.04 log points or less (Table 8). A"
- [INFO] manuscript_anonymized.tex:685 (B0074, B0085, B0095, B0102, B0109, B0133) — The six "Takeaway." closing paragraphs are summary sentences (rule 5.8). ARS accepts signposting, and they aid skimming.
  > \textbf{Takeaway.} Stocks that were likely constituents before the
  Suggestion: No change. If the editor asks for tighter prose, drop the bold "Takeaway." label and keep each sentence as the last sentence of the preceding paragraph.

---

## 5. Figures & Tables

**Summary:** Every table and figure is cited in the body before it appears. In the compiled PDF, each float lands one or two pages after its body call-out. Tables use booktabs with no vertical rules, and the source figures follow good plotting practice: colour plus marker, a colourblind-safe blue and orange pair, grid lines, no in-plot title, and 95% CIs. The main gaps are self-containment of the notes (stars, units, dashed lines), a y-axis range and colour mismatch between Figures 1 and 2, and small figure text at the printed scale.

### Findings

- [ERROR] manuscript_anonymized.tex:662 (B0189) — The Figure 2 note does not explain the dashed vertical lines or their labels (rule 4.3). The Figure 1 note does.
  > September 2025 from a regression with stock and week fixed effects; 95\%
  Suggestion: Append to the note, before "Source:": "Dashed lines mark the announcement, confirmation and constituent-list months."
- [WARN] manuscript_anonymized.tex:622 (B0067; also 955 B0093, 1039 B0101, 1106 B0108, 1175 B0115, 1346 B0131) — Tables 3, 5, 6, 7, 8 and 9 use significance stars, but only the Table 2 notes define them.
  > \emph{Notes}: The preliminary list is FTSE's November 2025 eligible list
  Suggestion: Add to each of these notes: "*, **, *** denote significance at 5\%, 1\% and 0.1\%."
- [WARN] manuscript_anonymized.tex:536 (B0062; also line 1088, B0107) — The CS spread coefficients are in decimal units (0.0009), while Table 1 reports the spread in percent (0.57) and the text converts to percentage points. The tables do not state the unit.
  > (3) CS spread
  Suggestion: Table 2 header "(3) CS spread (decimal)" and "(6) CS spread (decimal)". Table 7 header "(2) CS spread (decimal), controlling for volatility". Alternatively, add to the notes: "CS spread coefficients are in decimal units; 0.0010 equals 0.10 percentage points."
- [WARN] manuscript_anonymized.tex:1080 (B0106) — The table title is a fragment that does not describe the contents (rule 4.3).
  > \textbf{Table 7. Volatility and liquidity}
  Suggestion: "Table 7. Constituent volatility, CS spread and Amihud estimates with a volatility control"
- [WARN] manuscript_anonymized.tex:330 (B0038 and all table blocks) — All data columns are left-aligned (`\raggedright` p-columns), which breaks rule 4.7 (the first column should be l and the rest c).
  > \begin{longtable}[]{@{}>{\raggedright\arraybackslash}p{...
  Suggestion: In each Markdown pipe table, set the alignment row to left for column 1 and centred for the others, for example `|:---|:---:|:---:|:---:|`. Pandoc then emits `\centering` columns.
- [WARN] manuscript_anonymized.tex:661 (B0188; figure file Figure_2.png) — The same metric (log Amihud event-study coefficients) has different y-axis ranges: about -1.5 to 0.7 in Figure 1 panel A and about -1.2 to 0.6 in Figure 2. Side-by-side comparison of the "same shape" claimed at line 641 is misleading.
  > \noindent\includegraphics[width=0.95\textwidth]{Figure_2.png}\par\medskip
  Suggestion: In code/figure2.R, add `+ coord_cartesian(ylim = c(-1.5, 0.7))` so the range matches Figure 1 panel A, then re-export Figure_2.pdf and Figure_2.png.
- [WARN] manuscript_anonymized.tex:649 (B0070, B0188) — The figure text is small at the printed scale (rule 4.9). The figures are saved 7.5 in wide with `theme_bw(base_size = 10)` and `annotate(size = 2.6)`, then placed at 0.95 of a 384 pt text width (scale about 0.68). Tick labels and event labels print at about 5 to 5.5 pt and axis titles at about 7 pt, against a 10.95 pt figure note. They are readable but well below the note size.
  > \noindent\includegraphics[width=0.95\textwidth]{Figure_1.png}\par\medskip
  Suggestion: In code/figure1.R and code/figure2.R, change `theme_bw(base_size = 10)` to `theme_bw(base_size = 14)` and `size = 2.6` to `size = 3.6`, keeping the 7.5 in export width.
- [WARN] manuscript_anonymized.tex:659 (B0187) — The colour and marker are inconsistent across figures (rule 4.9). Figure 2's ITT group is drawn with the same blue circle (#1b6ca8) that Figure 1 uses for "FTSE constituents", a different group.
  > \noindent \textbf{Figure 2. Monthly event-study coefficients for the
  Suggestion: In code/figure2.R, change `colour = "#1b6ca8"` to `colour = "#009E73", shape = 15` (Okabe-Ito green, square) in `geom_pointrange`.
- [WARN] manuscript_anonymized.tex:649 (B0070; also B0188) — The y-axis labels give no unit (rule 4.9).
  > y = "Coefficient relative to never-named HOSE stocks (95% CI)"
  Suggestion: Figure 1: "Coefficient (log points) relative to never-named HOSE stocks, 95% CI". Figure 2: "Coefficient, log Amihud (log points, 95% CI)".
- [WARN] manuscript_anonymized.tex:628 (B0068) — Figure 1 plots the named-but-excluded series (orange triangles), but the text never interprets it (rule 4.8). Section 5.2 relies on Table 9 only.
  > Figure 1 shows the timing. The constituents' monthly Amihud coefficients
  Suggestion: At the end of B0068 (line 644), add: "Figure 1 also plots the named-but-excluded stocks, which Section 5.2 examines."
- [INFO] manuscript_anonymized.tex:319 (all tables and figures) — Table and figure numbers are hard-coded, with no `\label` or `\ref` (rules 4.1 and 4.2, downgraded by design of the DOCX-first build). Every table and figure is referenced in the body. Figure 2 is referenced only once (line 641), early enough. The introduction cites Tables 2 to 6 and 9 (lines 128–138) many pages before the floats. This is acceptable for summary citations.
  > Table 1 shows that constituents are much larger and more liquid than the
  Suggestion: No change for the DOCX build. For a LaTeX-native build, add `\label{tab:1}` inside each table and write `Table~\ref{tab:1}`.
- [INFO] manuscript_anonymized.tex:327 (all Table, Figure and Panel titles) — The titles end without a period (rule 4.3, downgraded because Elsevier sets titles without a final period). All Notes paragraphs end with a period.
  > Table 1. Sample composition and pre-announcement characteristics
  Suggestion: No change for Elsevier. To satisfy the checklist, write "Table 1. Sample composition and pre-announcement characteristics (October 2024 to 6 October 2025)." with the same pattern for the others.
- [INFO] manuscript_anonymized.tex:649 (B0070, B0188) — The figures are included as raster PNG, although vector PDFs exist in submission/figures/ (rule 4.5). The venue accepts bitmaps of at least 300 dpi, and the PNGs are 600 dpi. The Markdown source also points to differently named files (figures/figure1_event_study.png, figures/figure2_itt_event_study.png). Confirm that they match the submitted Figure_1 and Figure_2.
  > \includegraphics[width=0.95\textwidth]{Figure_1.png}
  Suggestion: `\includegraphics[width=0.95\textwidth]{Figure_1.pdf}` and `{Figure_2.pdf}` in the .tex. Keep the PNGs for the DOCX.
- [INFO] manuscript_anonymized.tex:958 (B0093; also 1044 B0101, 1349 B0131, 1496 B0145) — The "Source:" sentence sits in the middle of the notes in Tables 5, 6, 9 and A.1, but at the end in the other tables.
  > data (VCI, via vnstock). An event regression that uses the last session
  Suggestion: Move "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock)." to the end of each of these four notes.

---

## 6. Statistical Relevance

**Summary:** Uncertainty is reported throughout: standard errors in parentheses, stars defined in Table 2, portfolio t-statistics, wild-bootstrap and randomization p-values, and 95% CIs in both figures. Where significance marks or standard errors are omitted (Tables 6 and 9), the reason is stated. Four prose sentences need attention: two look inconsistent with the table or figure they summarize, and two are imprecise or lack a number.

### Findings

- [WARN] manuscript_anonymized.tex:1121 (B0112) — The claim looks inconsistent with Table 8. In the weighted matched sample with trend (-0.204 n.s., -0.425, -0.637) and in the post-announcement drift row (-0.231, -0.446, -0.541), the coefficients are about half the baseline (-0.392, -0.888, -1.129). Author to verify.
  > result. The coefficients remain negative and of similar size in every
  Suggestion: "result. The coefficients remain negative in every specification; they are of similar size except in the weighted matched sample with a trend and the post-announcement drift specification, where they are about half as large."
- [WARN] manuscript_anonymized.tex:1188 (B0116) — Figure 1 panel A shows the month -6 (April 2025) coefficient at about 0.25, above August 2025 (0.23). "Largest" therefore holds only for July. Line 631 (B0068) says "most clearly", which fits the CIs excluding zero. Author to verify.
  > Dropping July and August 2025, the two months with the largest
  Suggestion: "Dropping July and August 2025, the two months with the most precisely estimated positive deviations,"
- [WARN] manuscript_anonymized.tex:892 (B0085) — "under every benchmark" is true only for the announcement [-1,+5] and confirmation [-1,+1] windows. The announcement [-1,+1] window is significant under one benchmark (line 702).
  > \textbf{Takeaway.} Prices rose in the announcement week and at the
  Suggestion: "\textbf{Takeaway.} Prices rose in the announcement week (days -1 to +5) and around the confirmation (days -1 to +1) under every benchmark;"
- [WARN] manuscript_anonymized.tex:1420 (B0138) — A comparative claim has no statistic in the sentence (rule 3.3).
  > market, which contains hundreds of stocks outside FTSE's screens, moved
  Suggestion: "market, which contains hundreds of stocks outside FTSE's screens, moved much less (pseudo-groups of large never-named stocks: -0.21 log points in the list window, against -1.13 for constituents; Section 4.1)."
- [INFO] manuscript_anonymized.tex:351 (B0038) — Table 1 reports means without dispersion. It is a descriptive table, so this is not a stochastic-experiment omission.
  > FTSE constituents & 24 & 1,248 & 0.00017 & 6.82 & 0.57 & 1.40 \\
  Suggestion: Optional: add standard deviations in parentheses under each mean and change the header to "Mean (SD) weekly Amihud", with the same pattern for the other mean columns.
- [INFO] manuscript_anonymized.tex:1045 (B0101; also 1350 B0131) — Significance marks are omitted for the three-stock segments, and the GEE/BSR row shows point estimates only. The reason is stated in the notes, which is acceptable (rule 3.2).
  > Significance marks are omitted for the large and mid segments, which
  Suggestion: No change.
- [INFO] manuscript_anonymized.tex:1193 (B0116; also 1000 B0098) — Two rounded values are borderline: the text says "-0.42" for Table 8's -0.425 and "-0.85" for Table 6's -0.855. Conventional rounding gives -0.43 and -0.86. The unrounded estimates may justify the text.
  > matched sample with a trend, gives -0.20, -0.42 and -0.64; the
  Suggestion: Check the unrounded estimates in the R output. If they are at least 0.425 and 0.855 in absolute value, write "-0.20, -0.43 and -0.64" (line 1193) and "-0.39, -0.86 and -1.00" (line 1000).
