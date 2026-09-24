# Stop-slop audit (final): manuscript_v8.md

Input: `/home/user/B-i-FTSE2/ars/stage4_5_integrity/correction_round4/manuscript_v8.md` (read-only; no manuscript file was edited).
Previous audit: `/home/user/B-i-FTSE2/ars/stage5b_proofread/stop_slop_audit.md` (SS-1 to SS-37 on v7, applied in v8).
Scope: every prose block, table note and figure note in the abstract, Sections 1 to 6 and the Appendix. Tables, display equations, references and the fixed Elsevier wording in Declarations (B0150 to B0155) were skipped. The focus is text that is new or rewritten in v8: table lead-ins, short notes, new comparison sentences with prior studies, paragraphs compressed during compaction, repeated templates and pull-quote endings. Date: 2026-09-24.

## 1. Skill load record

| File (read in full with the Read tool) | First heading |
|---|---|
| /root/.claude/skills/stop-slop/SKILL.md | `# Stop Slop` |
| /root/.claude/skills/stop-slop/references/phrases.md | `# Phrases to Remove` |
| /root/.claude/skills/stop-slop/references/structures.md | `# Structures to Avoid` |
| /root/.claude/skills/stop-slop/references/examples.md | `# Before/After Examples` |
| /root/.claude/skills/academic-paper/references/writing_quality_check.md | `# Writing Quality Check` |
| /root/.claude/skills/academic-paper/references/academic_writing_style.md | `# Academic Writing Style Guide` |

## 2. Precedence rule and mechanical scan

This is an empirical finance journal article. Where stop-slop conflicts with the ARS conventions, ARS wins. writing_quality_check.md calls its items "non-blocking prompts for judgment" and forbids weakening a claim's evidential support. For that reason, this audit does not flag:
- passive voice in methods;
- statistical hedges;
- technical adverbs (daily, weekly, persistently, monotonically, precisely estimated, reliably [defined in B0012/B0205], gradually);
- the absence of "you";
- the Section 1 roadmap (B0014);
- lists of three that name three real windows or groups;
- contrasts that report a tested distinction.

No suggestion changes a number, citation, significance statement, evidential hedge or claim rung. The last column says "possible" where a fix could touch meaning. Rung issues are listed separately in Section 5.

Mechanical scan (prose only):
- **Em dashes:** 0. **En dashes in prose:** 0.
- **Sentence-initial Wh- words:** 1 (B0025, "Where").
- **Banned filler adverbs** (really, just, actually, simply, genuinely, importantly, crucially, even, somewhat): 0.
- **Other adverb:** one non-technical intensifier, "most clearly" (B0068).
- **Flagged ARS terms** (robust, crucial, pivotal, underscore, landscape, etc.): 0.
- **Prose sentences of 45 words or more:** 24. Twelve are equation "where" clauses or benchmark lists in methods, which are exempt. The rest are compaction joins (Section 3, F-5 to F-16).

Status of earlier decisions:
- **SS-6** ("We make one contribution:"): the colon setup was kept. This audit treats it as a deliberate author choice and does not flag it again.
- **SS-17** (Takeaways): removed.
- **SS-36:** only partly resolved (see F-3).

## 3. Findings

| ID | Block | Pattern | Offending text (≤120 chars) | Suggested replacement (minimal) | Touches meaning |
|---|---|---|---|---|---|
| F-1 | B0009, B0021, B0060, B0105, B0136 | Repeated citation template across sections (the new comparison sentences restate Hegde & McDermott in near-identical words) | B0009 "raise trading activity and narrow spreads persistently"; B0021 "narrow spreads and raise trading activity persistently, mainly through lower direct trading costs"; B0105 "gained liquidity mainly through lower direct trading costs" | Keep B0009, B0060 and B0105 as they are. In B0021, cut the repeat: "…and Hegde and McDermott (2003) attribute the persistent liquidity gains of S&P 500 additions mainly to lower direct trading costs." | no |
| F-2 | B0009, B0024, B0136 | Same finding restated three times with the same "rather than" template; B0009 also uses false agency ("the evidence points") | B0009 "the evidence points to institutional demand rather than trading pressure or liquidity changes as the cause" | B0009: "…index additions raise prices persistently, and Biktimirov and Afego (2026) attribute the gains to institutional demand." Keep the full contrast in B0024. See O-6 for the B0136 wording mismatch. | no |
| F-3 | B0003, B0007, B0060, B0135 | Repeated closing template left over from the SS-36 fix ("before index funds …") | B0003 "before index funds bought"; B0007 "before index funds had to buy"; B0060 "months before index funds traded" | Keep B0003 and B0007. In B0060, write "…months before the 18 September rebalancing." | no |
| F-4 | B0094 / B0136 | Same fact twice within B0094, then verbatim again in B0136 ("left no reliable price effect") | B0094 "Harris and Gurel (1986) find temporary price rises…, whereas the first-tranche purchase in Vietnam left no reliable price effect." | B0094: "Harris and Gurel (1986), by contrast, find temporary price rises when index funds buy S&P 500 additions." ("Prices did not respond" already opens that point.) In B0136, write "…prices and liquidity moved with FTSE's public statements rather than with the first-tranche rebalancing." | no |
| F-5 | B0010 | Dangling "Finally" (no First or Second before it) | "Finally, FTSE published a preliminary list of eligible stocks screened on data as of 31 December 2024…" | "FTSE also published a preliminary list of eligible stocks screened on data as of 31 December 2024…" | no |
| F-6 | B0010 | Compressed run-on (49 words, "so … ; we also …") | "…could mistake selection for an upgrade effect; we also drop from the comparison group every stock FTSE named…" | Split at the semicolon: "…could mistake selection for an upgrade effect. We therefore drop from the comparison group every stock FTSE named as eligible but did not include." | no |
| F-7 | B0009 | Stacked, redundant clause introduced by compaction | "(e.g., Burnham et al., 2018; Raddatz et al., 2017), which, being aggregated across stocks, cannot separate the stocks…" | "(e.g., Burnham et al., 2018; Raddatz et al., 2017), which cannot separate the stocks an upgrade targets from market-wide trends." | no |
| F-8 | B0018 | Overloaded sentence (63 words, with a colon and a worked example) | "…each tranche applies a fraction of that weight (FTSE Russell, 2026): a security with a 49% investability weight enters…" | End the sentence at "(FTSE Russell, 2026)." and begin the next with "A security with a 49% investability weight thus enters at 4.9%…". | no |
| F-9 | B0021 | Overloaded sentence (74 words; a colon followed by three studies joined with commas) | "…changes lastingly: Shleifer (1986) interprets excess returns… slope down, Chen et al. (2004) find asymmetric effects…" | Split after "slope down.": "Chen et al. (2004) find asymmetric effects of additions and deletions that fit a gain in investor awareness." Then add the F-1 sentence. | no |
| F-10 | B0025 | Compressed chain with a weak causal link ("ask whether …, so …; we do not…") | "…and Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity, so a liquidity gain…" | "…(Bekaert et al., 2007). Stereńczak et al. (2020) ask whether frontier-market investors demand compensation for illiquidity. If they do, a liquidity gain for some stocks could shift their cost of capital, which we do not measure." | no |
| F-11 | B0025 | Wh- sentence opener | "Where domestic retail investors dominate turnover, benchmark-tracking foreign money changes the investor base more…" | "In markets where domestic retail investors dominate turnover, benchmark-tracking foreign money changes…" (see also O-5) | no |
| F-12 | B0024 | Ambiguous word ("separate" can be read as a verb) in a new comparison sentence | "they find persistent price gains for additions and separate return and trading-volume responses when a country changes class" | "…and distinct return and trading-volume responses when a country changes class" | no |
| F-13 | B0054 | Compressed assumptions (Third and Fourth each join a condition, a consequence and a remedy) | "…would fall because of the treatment, and excluding named-but-excluded stocks removes the most likely channel, trading in…" | Split: "…would fall because of the treatment. Excluding named-but-excluded stocks removes the most likely channel, trading in near-substitutes." Fourth: split at "whereas": "…as of 30 June 2026. The ITT group, screened on 2024 data, avoids it and measures…" | no |
| F-14 | B0050 | Methods run-on (63 words plus a semicolon) | "…weighting each control by its matching weight (Ho et al., 2007); matching reduces the standardized mean difference…" | Split at the semicolon: "…(Ho et al., 2007). Matching reduces the standardized mean difference (SMD)…" | no |
| F-15 | B0084 | Table lead-in does not match the table (Panel B reports only the ITT group; the passed-over stocks are "not tabulated") | "Panel B separates likely constituents from the stocks FTSE passed over." | "Panel B reports the ITT group; we add the named-but-excluded stocks in the text." | no |
| F-16 | B0084 | Semicolon chain at the paragraph's end | "…such as size and liquidity; by the confirmation the preliminary list was public, and only stocks that went on…" | Replace the semicolon with a period: "…such as size and liquidity. By the confirmation the preliminary list was public…" | no |
| F-17 | B0097 / B0117 | Repeated idiom plus false agency ("point the same way") | B0097 "benchmark-driven foreign allocations (Raddatz et al., 2017) point the same way for the persistent effect" | B0097: "…and benchmark-driven foreign allocations (Raddatz et al., 2017) imply a larger persistent effect for them as well." Keep B0117 as it is. | possible |
| F-18 | B0098 | Compressed sentence (50 words: numbers, then a semicolon, then a hedge) | "…-1.00 for small stocks; the mid-small ordering does not follow size, and with three stocks in each upper segment…" | Replace the semicolon with a period: "…for small stocks. The mid-small ordering does not follow size, and with three stocks in each upper segment we read these estimates as descriptive." | no |
| F-19 | B0104 | Stacked "Because …, so …; …" | "…so the measured decline in illiquidity understates the gain in trading capacity; controlling for volatility enlarges…" | Replace the semicolon with a period: "…understates the gain in trading capacity. Controlling for volatility enlarges the Amihud coefficients to…" | no |
| F-20 | B0122 | Parallel pull-quote ending plus false agency ("timing points to") that pre-empts the next paragraph | "The gains concentrate in GEE, whose timing points to selection, and BSR, whose timing does not." | "The gains concentrate in GEE and BSR." (B0123 gives the timing evidence for each.) | no |
| F-21 | B0122 | Semicolon chain of two estimate sets | "…the first significant only at 10% (panel A); without BSR, whose pre-period spans two venues, the estimates are…" | Replace the semicolon with a period: "…(panel A). Without BSR, whose pre-period spans two venues, the estimates are -0.23, -0.46 and -0.73…" | no |
| F-22 | B0123 | Window definitions packed into a parenthesis with a semicolon | "…the end of window W1 (from 7 October 2025; W2 runs to 6 April 2026 and W3 from 7 April 2026)." | "FTSE screened the April 2026 list on data up to 31 December 2025. W1 runs from 7 October to 31 December 2025, W2 to 6 April 2026 and W3 from 7 April 2026." | no |
| F-23 | B0123 | Stacked clauses about BSR | "…(-0.39 in W1, -1.68 in W2) and joined HOSE only in January 2025, after the data date of the November list…" | "…(-0.39 in W1, -1.68 in W2). It joined HOSE only in January 2025, after the data date of the November list (VietnamPlus, 2024), which gives…" | no |
| F-24 | B0073 / B0192 / B0138 | The same comparison (-0.21 against -1.13) three times, with inconsistent wording ("less than one fifth" and "about one fifth") | B0192 "The 85 large never-named stocks became more liquid by about one fifth as much as constituents in the list window (-0.21 against -1.13)" | B0192: "The 85 large never-named stocks also became more liquid (Section 4.1), but this comparison does not separate the reform from the upgrade for the largest stocks." Keep the figures in B0073 and B0138. | no |
| F-25 | B0135 | Word repetition and a zeugma ("added … a surge … and no reliable price effect") | "The first tranche added a trading surge at the rebalancing close, largest for the largest constituents and absent…" | "The first tranche brought a trading surge at the rebalancing close, largest for the large-capitalization constituents and absent for excluded stocks, but no reliable price effect." | no |
| F-26 | B0136 | Generic, quotable paragraph closer (an uncited general claim) | "Unlike a routine reconstitution, a frontier-to-emerging upgrade changes which benchmark family can hold the stocks, and…" | "Unlike a routine reconstitution, the Vietnamese upgrade changed which benchmark family could hold the stocks, and FTSE announced it months in advance." | possible (narrows the scope to the case) |
| F-27 | B0138 | Compressed sentence (64 words: a colon, then "while", then "and") | "…at FTSE watch-list reviews: the 2025 and 2026 decisions were followed by liquidity gains…, and index averages…" | Split into three sentences at the colon and before "and index averages": "…watch-list reviews. The 2025 and 2026 decisions were followed by… (-0.21 against -1.13 log points). Index averages over hundreds of stocks…" (see O-7) | no |
| F-28 | B0025, B0138, B0140 (x2) | Repeated template: a disclaimer hooked on with a semicolon ("…; we do not test/measure…", "…; one event cannot show…") | B0140 "…bringing it forward; one event cannot show…" and "…index weights; we do not test whether raising them…" | Keep every hedge. In B0140, change the form: "…consistent with early communication bringing it forward, although one event cannot show that…" and "…index weights, although we do not test whether raising them would change the outcome." | no |
| F-29 | B0141 | Three unrelated limitations stacked in one sentence by compaction | "For the largest stocks, the upgrade cannot be fully separated from…, BSR changed trading venue…, and the preliminary…" | Make three sentences: "For the largest stocks, the upgrade cannot be fully separated from the concurrent removal of pre-funding requirements. BSR changed trading venue during the pre-period, and the preliminary and April lists come from press reports rather than FTSE documents." | no |
| F-30 | B0007 | Elliptical tail on a 57-word lead sentence | "…by 56% after the August 2026 constituent list, and that of the final constituents by 59% and 68%." | End the sentence at "constituent list." and add: "For the final constituents, the declines were 59% and 68%." | no |
| F-31 | B0003 | Vague referent in the abstract's closing line | "The response came with FTSE's disclosures, before index funds bought." | "The liquidity and price responses came with FTSE's disclosures, before index funds bought." | no |
| F-32 | B0068 | Non-technical intensifier | "…are positive in several months, most clearly three and two months before it (0.33 and 0.23)." | "…are positive in several months, largest three and two months before it (0.33 and 0.23)." | no |
| F-33 | B0060, B0087 | Stub lead-in sentences that only announce ("Table N reports Eq. (x).") | "Table 2 reports Eq. (7)." / "Table 5 reports Eq. (9)." | Optional. Merge each into the next sentence, e.g. "In Table 2 (Eq. 7), the Amihud illiquidity of constituents fell…". The other lead-ins (Tables 3, 4, 6, 8, 9) vary and are fine. | no |

Not flagged after checking:
- The colon setup in B0013 (author retained SS-6).
- "The two gains behaved differently afterwards" (B0083): a topic sentence followed at once by numbers.
- "Liquidity gains from inclusion also have real consequences:" (B0022).
- "Frontier-market evidence is thinner." (B0024): the specifics follow.
- "These estimates support H1." (B0064): the hypothesis closers in B0060, B0064, B0084 and B0098 vary in form.
- "rather than" in B0024, B0105, B0140 and B0141 (rival hypotheses or sources).
- "but not for stocks FTSE named and then excluded" (B0003) and "only for included stocks" (heading B0086), which are tested contrasts.
- The new Dong et al. (2023) comparison in B0076 and the new Hegde and McDermott (2003) comparison in B0060, which are clean on their own (their repetition is covered by F-1).
- Passive voice in B0034 to B0051.
- All table notes (B0039, B0063, B0067, B0082, B0093, B0101, B0108, B0115, B0131, B0145, B0148, B0213) and figure notes (B0071, B0189), apart from O-8.

## 4. Stop-slop 5-dimension score

Scored under the precedence rule, so exempt passive voice, hedges and technical adverbs do not lower any score.

| Dimension | Current (v8) | Projected after fixes | Basis |
|---|---|---|---|
| Directness | 8 | 9 | Nearly every sentence states a result with numbers. The remaining losses are one inaccurate lead-in (F-15), two stub lead-ins (F-33), a dangling "Finally" and a false-agency pre-emption (F-20). |
| Rhythm | 7 | 9 | Compaction produced about a dozen 45-to-74-word sentences built from semicolon or colon chains (F-6 to F-14, F-18, F-19, F-21 to F-23, F-27, F-29). Splitting them at the existing semicolons restores variety without adding words. |
| Trust | 8 | 9 | The takeaways are gone. Some findings are still stated twice (F-4, F-24), and the disclaimer template repeats (F-28). |
| Authenticity | 8 | 9 | The voice is plain and technical. The remaining templated spots are the "before index funds …" closers (F-3), the Hegde/Biktimirov restatements (F-1, F-2) and one aphoristic closer (F-26). |
| Density | 7 | 8 | Cross-section repetition of the cited findings and of the -0.21 against -1.13 comparison is the main thing left to cut. |
| **Total** | **38/50** | **44/50** | Above the 35/50 revise threshold (v7 scored 34/50). No finding blocks submission. The rhythm splits (F-6 to F-29) give the largest gain. |

## 5. Observations outside stop-slop scope (author decision; no change proposed under the hard constraint)

- **O-1 (B0007).** "The liquidity of likely index stocks improved at each step" overstates B0060. That block finds no discrete step at the constituent list (0.10, *p* = 0.40), and the effective date is not a liquidity-window step. Consider "at the announcement and the confirmation". This is a rung and precision issue for the author.
- **O-2 (B0135).** "Vietnam's reclassification brought liquidity and price gains" is causal wording. B0013 and B0132 limit causal readings of the constituent estimates (the successor of v7's O-1).
- **O-3 (B0094).** "they bought the first tranche at the closing price" states as fact what the next sentence calls an inference ("Without data on who traded, we infer index demand"). A consistent form would be "they were to buy the first tranche…".
- **O-4 (B0094).** "Prices did not respond" is stronger than "no reliable price effect", the wording used everywhere else (v7's O-4, which recurs here).
- **O-5 (B0025).** "benchmark-tracking foreign money changes the investor base more than an S&P 500 addition does" is an uncited comparative claim, and the premise that retail investors dominate turnover in Vietnam is also uncited.
- **O-6 (B0136 against B0009/B0024).** The Biktimirov and Afego (2026) finding is described in two ways. B0009 and B0024 say the index effect comes from institutional demand "rather than trading pressure or liquidity". B0136 says it comes from investor demand "rather than liquidity alone". Check which one matches the source. Also, "in Vietnam, demand and liquidity moved together at disclosure" asserts that demand moved, but B0141 says the data do not identify investors; what is observed is prices and trading.
- **O-7 (B0138).** "index averages … diluted that shift" states a mechanism as fact without re-estimating the index-level result. "could have diluted" would match the evidence. "The results also revise an index-level study" is a strong verb for the authors' own earlier work.
- **O-8 (B0072 / B0071).** B0072 cites "Figure 1, panel B", and `code/figure1.R` does plot two facets (`facet_wrap(~outcome)`). The Figure 1 note does not name them. Suggested note addition: "Panel A: log Amihud; panel B: log trading value."
