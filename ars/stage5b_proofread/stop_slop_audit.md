# Stop-slop audit: manuscript_v7.md

Input: `/home/user/B-i-FTSE2/ars/stage4_5_integrity/correction_round3/manuscript_v7.md` (read-only; no manuscript file was edited).
Scope: prose blocks in the abstract, Sections 1 to 6, table notes and figure notes. Tables, references and the fixed Elsevier wording in the Declarations section were skipped. Date: 2026-09-24.

## 1. Skill load record

| File (read verbatim with the Read tool) | First heading |
|---|---|
| /root/.claude/skills/stop-slop/SKILL.md | `# Stop Slop` |
| /root/.claude/skills/stop-slop/references/phrases.md | `# Phrases to Remove` |
| /root/.claude/skills/stop-slop/references/structures.md | `# Structures to Avoid` |
| /root/.claude/skills/stop-slop/references/examples.md | `# Before/After Examples` |
| /root/.claude/skills/academic-paper/references/writing_quality_check.md | `# Writing Quality Check` |
| /root/.claude/skills/academic-paper/references/academic_writing_style.md | `# Academic Writing Style Guide` |

## 2. Precedence rule

This is an empirical finance journal article. Where stop-slop conflicts with the ARS academic conventions (writing_quality_check.md, academic_writing_style.md), the ARS conventions win. ARS says the checklist items are "non-blocking prompts for judgment", keeps roadmap sentences in the Introduction, allows passive voice in methods, requires hedging for uncertain claims, and forbids weakening a claim's evidential support. So this audit does **not** flag:
- passive voice in methods and data descriptions where the actor is plainly the authors or the data provider;
- hedges that express statistical uncertainty ("consistent with", "suggests", "significant at 5%");
- technical adverbs that carry meaning ("statistically", "cross-sectionally", "monotonically", "persistently", "gradually", "precisely estimated", "daily/weekly/monthly");
- the absence of reader-address "you" (it will not be introduced);
- lists of three that name three real things (three disclosure windows, three groups, three reasons in B0010);
- the Section 1 roadmap (B0014);
- contrasts that report a tested distinction (for example, a surge for included stocks "but not" for excluded stocks, or "rather than" when it names a rival hypothesis in a cited study).

Suggestions never change a number, citation, significance statement, evidential hedge, or the rung of a claim on the claim-strength ladder. Where a stop-slop fix could touch meaning, the table marks it "possible". Section 5 lists rung issues outside the stop-slop scope for the author to decide.

Mechanical scan results: em dashes 0; en dashes in prose 0; sentence-initial Wh- words 3 (B0007, B0008, B0024); banned filler adverbs ("really", "just", "actually", "simply", "genuinely", "importantly" and similar) 0. Non-technical intensifiers found: "even" (B0024) and "somewhat" (B0073).

## 3. Findings

| ID | Block | Pattern | Offending text (≤120 chars) | Suggested replacement (minimal) | Touches meaning |
|---|---|---|---|---|---|
| SS-1 | B0007 | Wh- sentence opener | "When FTSE Russell reclassified Vietnam from frontier to secondary emerging status, the Amihud (2002) illiquidity…" | "During FTSE Russell's reclassification of Vietnam from frontier to secondary emerging status, the Amihud (2002) illiquidity…" | no |
| SS-2 | B0008 | Wh- sentence opener (clause as subject) | "Whether the promised liquidity reaches individual stocks, which stocks it reaches, and when, bears on issuers' cost of capital…" | "Because liquidity is priced in emerging markets (Bekaert et al., 2007), issuers' cost of capital depends in part on whether the promised liquidity reaches individual stocks, which stocks it reaches, and when." | no |
| SS-3 | B0009 | False agency | "that design could not ask which stocks gained" | "that design could not identify which stocks gained" | no |
| SS-4 | B0011 | Emphasis crutch ("X matters because") | "The last point matters because FTSE selected the final constituents at its September 2026 review…" | "The preliminary list is needed because FTSE selected the final constituents at its September 2026 review…" | no |
| SS-5 | B0011 | Throat-clearing announcement | "We address this in two ways. We remove from the comparison group every stock… and we estimate intention-to-treat…" | "We address this by removing from the comparison group every stock FTSE named as eligible but did not include, and by estimating intention-to-treat effects for the preliminary list." | no |
| SS-6 | B0013 | Colon setup / pull-quote framing | "The paper makes one contribution: it decomposes the stock-level liquidity and price effects…" | "The paper decomposes the stock-level liquidity and price effects…" (or keep if the "single contribution" framing is deliberate for the editor) | possible |
| SS-7 | B0013 | Comma-spliced fragment (dramatic contrast) | "the confirmation brought a discrete step beyond a gradual post-announcement drift, the constituent list did not." | "…beyond a gradual post-announcement drift; the constituent list did not." | no |
| SS-8 | B0024 | Emphasis adverb (no technical meaning) | "and an MSCI index change even moved currency values through this channel (Hau et al., 2010)" | "and an MSCI index change moved currency values through this channel (Hau et al., 2010)" | no |
| SS-9 | B0024 | Wh- sentence opener | "When MSCI included China A-shares in its Emerging Markets Index, the included stocks earned abnormal returns…" | "After MSCI included China A-shares in its Emerging Markets Index, the included stocks earned abnormal returns…" | no |
| SS-10 | B0025 | Meta-commentary (workflow word) plus misplaced sentence | "Beyond Dong et al. (2023), we did not locate a verified stock-level study of liquidity around the MSCI inclusion…" | Move to B0024, directly after the Dong et al. (2023) sentence, and drop "verified": "Beyond Dong et al. (2023), we did not locate a stock-level study of liquidity around the MSCI inclusion of China A-shares, so…" | no |
| SS-11 | B0060 | Binary contrast where Y alone would do (the list result is already given in the previous sentence) | "after it, liquidity kept improving gradually rather than jumping at the list." | "after it, liquidity kept improving gradually." | no |
| SS-12 | B0064 | Colon setup | "Splitting the ITT group shows where the gains concentrated: listed stocks that later entered the index gained…" | "In the split ITT group, listed stocks that later entered the index gained…" | no |
| SS-13 | B0072 | False agency + setup ("tells a similar story with one caveat") | "Trading value tells a similar story with one caveat." | Delete the sentence. The next sentence ("Constituents' trading value rose by 0.68, 1.03 and 1.19… but it was already rising…") states both the pattern and the caveat. | no |
| SS-14 | B0072 / B0118 | Redundancy across sections | B0118: "…and trend-adjusted effects fall to 0.28, 0.39 and 0.43 log points… We describe the trading-value result as an association." | Keep the full statement in B0118 and shorten B0072 to "Trend-adjusted effects are smaller (Section 5.1), and we describe the trading-value result as an association." Alternatively, delete the last sentence of B0118. | no |
| SS-15 | B0073 | Negation framing / vague declarative | "Randomization inference confirms that the declines are not what large HOSE stocks experienced in general." | "Randomization inference confirms that the declines exceed those of large HOSE stocks in general." | possible |
| SS-16 | B0073 | Filler hedge adverb (the magnitude is stated right after it) | "large stocks became somewhat more liquid, by less than one fifth of the constituent effect." | "large stocks became more liquid, by less than one fifth of the constituent effect." | no |
| SS-17 | B0074, B0085, B0095, B0102, B0109, B0133 | Pull-quote one-liners (the bold "Takeaway." device) | "**Takeaway.** …" (six paragraphs) | Preferred: delete all six. Each one restates its declarative section heading and first paragraph, and the device is uncommon in Elsevier empirical finance articles. If they stay, apply SS-18 to SS-22. | no (if deleted) |
| SS-18 | B0074 | Punchy ending, vague superlative | "…; the stocks FTSE finally included gained most." | "…; the stocks FTSE finally included gained more." | no |
| SS-19 | B0085 | Metronomic tricolon (three parallel semicolon clauses) | "…under every benchmark; the confirmation gain persisted under three of four; the constituent list and the first index…" | "Prices rose in the announcement week and at the confirmation under every benchmark, and the confirmation gain persisted under three of four. The constituent list and the first index tranche added no reliable price effect." | no |
| SS-20 | B0095 | Pull-quote closer | "…as index demand would imply, and prices had already adjusted by then." | If kept: "…as index demand would imply; prices did not move at the effective date." See also O-2. | possible |
| SS-21 | B0102 | Word repetition ("largest" x4) and a tense shift within one takeaway | "The rebalancing trade was largest for the constituents with the largest index weights; the liquidity gain is largest…" | "The rebalancing trade scaled with index weight. The liquidity gain was largest for the three large-capitalization stocks, did not rise monotonically across segments, and appeared in every segment before the first tranche took effect." | no |
| SS-22 | B0109 | Pull-quote one-liner | "Rising trading value, which more than offset rising volatility, drove the fall in illiquidity." | If kept: "The fall in illiquidity came from rising trading value, which more than offset rising volatility." (same rung; see O-3) | no |
| SS-23 | B0076 | Emphasis crutch ("shows why X matters") + colon setup | "The last column shows why the portfolio test matters: cross-sectional t-statistics, which ignore the common event date…" | "In the last column, cross-sectional t-statistics, which ignore the common event date, are up to 2.9 times larger." | no |
| SS-24 | B0084 | Binary contrast where Y alone would do (the previous clause already says no list was public) | "…responded to characteristics they could observe, such as size and liquidity, rather than to the lists themselves." | "…responded to characteristics they could observe, such as size and liquidity." | no |
| SS-25 | B0084 / B0137 | Redundancy across sections (near-verbatim repeat) | B0137: "At the confirmation, once the preliminary list was public, only the portfolio of stocks that went on to be included gained." | In B0137, compress to one clause that points back: "…and, once the preliminary list was public, gains at the confirmation were confined to stocks that went on to be included (Section 4.2)." | no |
| SS-26 | B0098 | Redundant caveat in adjacent sentences | "This ordering is consistent with H4, although the two upper segments contain three stocks each." | "This ordering is consistent with H4." (The three-stock caveat already appears two sentences earlier and in the Table 6 note.) | possible |
| SS-27 | B0105 | Negation-then-assertion | "The Corwin and Schultz (2012) spread did not narrow: it rose by 0.09 to 0.13 percentage points for constituents…" | "The Corwin and Schultz (2012) spread rose by 0.09 to 0.13 percentage points for constituents…" | no |
| SS-28 | B0112 | Lazy extreme / vague declarative ("of similar size in every specification") | "The coefficients remain negative and of similar size in every specification." | "The coefficients remain negative in every specification; they are about half the baseline size in the weighted matched sample with a trend and in the drift specification." (Table 8 ratios: 0.48 to 0.59.) | possible (corrects an overstatement) |
| SS-29 | B0116 | Binary contrast where Y alone would do | "so they work against the estimated declines rather than for them." | "so they work against the estimated declines." | no |
| SS-30 | B0013, B0132, B0139 | Repeated sentence template across sections ("This … limits … / sets a boundary on …") | B0132: "This evidence limits how the constituent results can be read." B0139: "The selection evidence sets a boundary on these conclusions." | B0132: "FTSE's screens rest on investability, and at least one stock became eligible after its liquidity rose during the screening window." (delete the first sentence and start with the second). Keep B0139 as it is. | no |
| SS-31 | B0132 / B0139 | Redundancy across sections | B0139: "We therefore report constituent and ITT estimates side by side; both show a large response at disclosure…" | Keep B0139 and shorten B0132's last sentence to "We report both." or delete it. | no |
| SS-32 | B0136 | Quotable mid-paragraph one-liner | "In Vietnam, demand and liquidity moved together, and both moved at disclosure." | Join it to the previous sentence: "…(Biktimirov & Afego, 2026); in Vietnam, demand and liquidity moved together at disclosure." | no |
| SS-33 | B0137 | False agency + vague declarative | "The price evidence also shows how the market learned." | Delete it and begin with "In the announcement week, before any list was public, …". | no |
| SS-34 | B0138 | Vague declarative | "The segment evidence adds a second margin." | Delete it, or "The segment evidence adds a cross-sectional comparison." | no |
| SS-35 | B0138 | Vague declarative ("matter/mattered") | "…which could suggest that classification decisions do not matter for liquidity. The stock-level design shows that the 2025…" | "…which could suggest that classification decisions leave liquidity unchanged. The stock-level design shows that the 2025 and 2026 decisions were followed by liquidity gains in the stocks they concerned, while…" | possible (the author should check the rung; "mattered" reads as causal) |
| SS-36 | B0003, B0007, B0102, B0135 | Repeated closing template ("before the first index tranche took effect") | Abstract last sentence, first sentence of Section 1, B0102, first sentence of Section 6 | Keep it in the abstract and in Section 6. In B0007, use "…before any index fund had to buy." or "…ahead of the 21 September 2026 effective date." In B0102, delete the clause (see SS-21). | no |
| SS-37 | B0141 | Throat-clearing opener + metronomic list of limits | "The study has limits. The sample uses stocks listed on 24 September 2026…" | Delete "The study has limits." and start with "The sample uses stocks listed on 24 September 2026, which omits…". Optionally merge the two data-source limits into one sentence to break the run of same-shape sentences. | no |

Not flagged after checking (for transparency): the passive voice in B0034, B0043, B0044, B0048 and B0050 (methods); "rather than" in B0009, B0024, B0025, B0043, B0105, B0136, B0140 and B0141 (substantive alternatives or rival hypotheses); "but not for stocks FTSE named and then excluded" (B0003) and "moved volume but not prices" (B0094) (tested contrasts); "The four steps carried different information" (B0019, followed at once by the specifics); "Liquidity gains from inclusion also have real consequences" (B0022) and "Liquidity carries particular weight in these markets" (B0025) (topic sentences backed by the next sentence); "the data tell" constructions (none present); "Four findings support the decomposition" (B0013, a standard contribution signpost).

## 4. Stop-slop 5-dimension score

Scored under the precedence rule, so exempt passive voice, statistical hedges and technical adverbs do not lower any score.

| Dimension | Current | Projected after fixes | Basis |
|---|---|---|---|
| Directness | 8 | 9 | Most sentences state results with numbers. The losses come from announcement sentences (SS-4, SS-5, SS-13, SS-23, SS-33, SS-34) and three Wh- openers. |
| Rhythm | 7 | 8 | Sentence length varies well overall. There are metronomic spots in B0085 and B0141 and a comma-spliced fragment in B0013. |
| Trust | 6 | 8 | Six bold "Takeaway." paragraphs repeat the section headings and first paragraphs. Several facts appear twice (SS-14, SS-25, SS-26, SS-31). |
| Authenticity | 7 | 8 | The voice is plain and technical. The pull-quote takeaways, the "how the market learned" line and the repeated closing phrase read as templated. |
| Density | 6 | 8 | Redundancy between adjacent sentences and across sections, plus the takeaway duplication, is the main thing that can be cut. |
| **Total** | **34/50** | **41/50** | The current score is just under the skill's 35/50 revise threshold. Deleting the takeaways (SS-17) accounts for most of the gain. |

## 5. Observations outside stop-slop scope (author decision; no change proposed under the hard constraint)

These fall outside stop-slop's scope. They are wording-precision and rung issues found during the pass. They are not suggested edits, because the hard constraint forbids changing a claim's rung.
- **O-1 (B0007).** "Vietnam's market upgrade raised the liquidity of likely index stocks" uses a causal verb. Elsewhere the text limits causal readings of the constituent estimates (B0013, B0132). The author should check this against the claim-strength ladder.
- **O-2 (B0095, B0136).** "prices had already adjusted" states as fact what B0094 presents as "consistent with other investors having bought earlier".
- **O-3 (B0109).** "drove the fall in illiquidity" is causal wording. Its basis is the Amihud accounting identity plus the volatility control in Table 7. The author should confirm this is intended.
- **O-4 (B0135).** "and no price change" is stronger than "no reliable price effect" (abstract, B0085) for a three-day CAR of -0.5% to 0.9% that is never significant. Using the same wording in both places would remove the mismatch.
