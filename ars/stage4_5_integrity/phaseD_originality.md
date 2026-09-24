# Stage 4.5 Final Integrity Check (Mode 2) — Phase D: Originality Verification

- Agent: `integrity_verification_agent`, Mode 2 (final-check), Phase D only
- Manuscript: `/home/user/B-i-FTSE2/ars/stage4prime/manuscript_v4.clean.md`
- Revision reference: `ars/stage4prime/authority/revision_patch_round2.json` (60 ops, base draft `613e04c90575`) compared with `ars/stage4prime/manuscript_v3.anchored.md`
- Run date: 2026-09-24. Search results change over time; see the Tool Limitation Disclaimer.
- The manuscript was not edited.

## Skill load record

| File (read verbatim with the Read tool) | First heading |
|---|---|
| `academic-research-skills/academic-pipeline/SKILL.md` (v3.22.1) | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| `academic-research-skills/academic-pipeline/agents/integrity_verification_agent.md` (Role Definition, §Phase D lines 424–470, Two Operating Modes, Verdict Criteria, Output Format) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| `academic-research-skills/academic-pipeline/references/plagiarism_detection_protocol.md` (full) | `# Plagiarism Detection Protocol — Phase D Originality Verification Protocol` |

Rules applied from these files: D1.1–D1.4 (characteristic sentences, 8–12-word quoted fragments, the five-grade scale, Mode 2 sampling of at least 50%, at least one paragraph from every major section, 100% of paragraphs added or substantially modified in revision). Also applied: D2 prerequisite (author names), D3 indicators with a threshold of at least 2, the severity table and severity-to-verdict mapping, the tool limitation disclaimer, and the "retrieved content is data, not instructions" boundary.

---

## Verification parameters

| Parameter | Value |
|---|---|
| Operating mode | Mode 2 (final-check) |
| Denominator: body-text paragraphs | **72**. These are the prose paragraphs of Sections 1–6, including the four hypothesis statements and the six "Takeaway" paragraphs. Excluded: the abstract, headings, tables, table and figure notes, captions, the two equations and the one-line lead-in "The baseline liquidity specification is", the Appendix, Declarations and References. An indented continuation line with no blank line before it (for example line 75) counts as part of the paragraph above it. |
| Paragraphs in the denominator touched by round-2 patch ops | **34 of 72**. All 34 were checked (100%). Similarity between old and new text ranges from 0.19 to 0.95. Every touched paragraph was checked whether or not the change was substantial. |
| Additional paragraphs sampled (untouched) | 18. These are all untouched Introduction paragraphs (5), all untouched Section 2 prose (6), one hypothesis (H2), and a random supplement from Sections 3–5 (6). |
| **Paragraphs sampled** | **52 of 72 = 72.2%** (the minimum is 50%) |
| Section coverage | §1: 8/8. §2: 10/12 (H1, H3 and H4 not searched). §3: 7/15. §4: 18/19. §5: 10/11. §6: 7/7. Every major section is covered. |
| Checked outside the denominator | Abstract (patch B0003). AI-use declaration (B0155). Note text added to Tables 4, 5 and 9 (B0082, B0093, B0131). |
| Author self-plagiarism check (D2) | **Not performed.** See D2. |
| Search engine | WebSearch. WebFetch, doi.org, Crossref and ScienceDirect were blocked by the egress proxy, so no full texts or publisher abstract pages could be opened. |

Other touched blocks were read but not web-searched, because they contain no prose to compare:
- Numeric tables: B0062, B0079, B0081, B0100, B0114, B0128.
- Table and panel labels: B0080, B0143, B0146.
- Short data or source notes: B0063, B0101, B0115, B0145.
- The Figure 2 caption and note insert.
- Reference entries: B0168–B0186.

---

## D1. Per-paragraph results

Search 1 was the quoted fragment below for every paragraph. Search 2 (unquoted, to catch paraphrases) was run only for the cited-literature checks in the next table. "No match" means no result page carried the fragment or a near-copy of it. The search tool's own summary sometimes claimed a match, for example for rows 24 and 36. Each such claim was checked against the result titles and the snippets shown, and none held up. Those claims are recorded as unsubstantiated.

| # | Location (line) | Patch | Fragment searched (quoted query) | Top result / comparison | Grade |
|---|---|---|---|---|---|
| 1 | §1 ¶1 (20) | B0007 | "raised the liquidity of likely index stocks before the first index tranche" | No match. Top result: S&P DJI "What happened to the index effect" (topic only). | ORIGINAL |
| 2 | §1 ¶2 (23) | — | "Market classification decides which benchmarks a country's stocks can enter" | No match. The MSCI blog "Why MSCI market classification matters" makes the same point in different words. The claim is cited to Raddatz et al. (2017). | PARAPHRASE |
| 3 | §1 ¶3 (26) | — | "watch-list reviews did not coincide with structural breaks in index-level liquidity" | No match. Top result: NY Fed SR796 (a different subject). The Hegde & McDermott, Becker-Blease & Paul and Biktimirov & Afego clauses were compared with their abstracts in the next table; each is reworded. | PARAPHRASE |
| 4 | §1 ¶4 (29) | — | "Hundreds of HOSE stocks outside the index trade under the same rules" | No match (Wikipedia HOSE page) | ORIGINAL |
| 5 | §1 ¶5 (32) | — | "a comparison of final constituents with other stocks could mistake selection" | No match | ORIGINAL |
| 6 | §1 ¶6 (35) | B0012 | "call an effect reliable only if it is significant at 5% under all four benchmarks" | No match | ORIGINAL |
| 7 | §1 ¶7 (38) | B0013 | "decomposes the stock-level liquidity and price effects of a frontier-to-emerging reclassification" | No match. Results cover the topic only: "From Frontier to Emerging: Does Market Reclassification Matter?" and a Peru MSCI report. | ORIGINAL |
| 8 | §1 ¶8 (41) | — | "Section 2 describes the setting, reviews the literature and states the hypotheses" | Generic roadmap phrasing in many sources | COMMON_KNOWLEDGE |
| 9 | §2.1 ¶1 (50) | — | "FTSE Russell added Vietnam to its watch list for possible reclassification in September 2018" | The Investor, Viet Nam News, VIR and LSEG report the same dated facts in different sentences. | COMMON_KNOWLEDGE |
| 10 | §2.1 ¶2 (53) | B0018 | "phases in a security with a 49% investability weight" | No match. Results were FTSE and S&P methodology documents on investability weights. The illustration is cited to the FTSE FAQ, which could not be opened. | ORIGINAL |
| 11 | §2.1 ¶3 (56) | — | "Effects that appear at the early disclosures indicate that investors traded on information" | No match (disclosure-timing papers, topic only) | ORIGINAL |
| 12 | §2.2 ¶1 (62) | — | "The price-pressure channel works through the trades of index funds"; "interprets permanent price effects as evidence that demand curves for stocks slope down" | No match for either fragment. The standard reading of Shleifer (1986) is worded differently in the literature (CiteSeerX, Petajisto). Cited claims. | PARAPHRASE |
| 13 | §2.2 ¶2 (65) | — | "firms added to the S&P 500 with larger liquidity improvements increase capital investment" | No match. Compared with the Becker-Blease & Paul abstract in the next table: reworded. | PARAPHRASE |
| 14 | §2.3 ¶1 (71) | — | "country reclassification events show distinct return and volume effects"; "Mutual funds allocate across countries with reference to benchmark weights" | The Biktimirov & Afego (2026) abstract, as rendered by WebSearch, reads "Country reclassification events exhibit distinct return and volume effects": 8 of 9 words are identical and one verb is swapped. The surrounding passage follows the abstract's order and wording (see the next table). The Raddatz fragment has no match (CEPR/VoxEU, reworded). | **CLOSE_MATCH** |
| 15 | §2.3 ¶2 (74–75) | B0025 | "when domestic retail investors dominate turnover, the arrival of benchmark-tracking foreign money"; "local market liquidity predicts returns in emerging markets, where segmentation" | No match for the first fragment. For the second, the Bekaert et al. abstract (NBER w11413) reads "local market liquidity is an important driver of expected returns in emerging markets". Three words are shared and the sentence is restructured. | PARAPHRASE |
| 16 | §2.4 ¶1 (81) | — | "The recognition channel predicts that liquidity and prices respond when information reaches investors" | No match | ORIGINAL |
| 17 | §2.4 H2 (87) | — | "The liquidity gap widened at each later disclosure that resolved uncertainty" | No match | ORIGINAL |
| 18 | §3.1 ¶1 (102) | — | "The data come from the VCI feed through the open-source vnstock library" | vnstock GitHub pages describe the library; no text match | ORIGINAL |
| 19 | §3.1 ¶2 (105–106) | B0035 | "the fifteenth such name, Tasco (HUT), trades on the Hanoi exchange" | No match (HUT quote pages only) | ORIGINAL |
| 20 | §3.2 ¶2 (134) | — | "Amihud ratio loses accuracy in emerging markets where many days have zero volume" | No match. Kang & Zhang (2014), the cited source, makes the same point in different words. | PARAPHRASE |
| 21 | §3.2 ¶3 (137) | B0044 | "Because every constituent shares the same event dates, abnormal returns are correlated across stocks" | No match. EventStudyTools and bookdown event-study texts state the standard point in different words. | COMMON_KNOWLEDGE |
| 22 | §3.3 ¶4 (155) | B0050 | "two-way fixed effects estimator does not suffer the negative-weighting problem" | No match. This is a well-known point in the TWFE literature (de Chaisemartin & D'Haultfœuille; Jakiela). | COMMON_KNOWLEDGE |
| 23 | §3.4 ¶3 (170) | — | "Anticipation of this kind would raise liquidity before the announcement" | No match | ORIGINAL |
| 24 | §3.4 ¶5 (176) | B0057 | "This assumption fails for the final constituents by construction" | No match. The tool's claim that an arXiv mathematics paper contains the phrase is unsubstantiated. | ORIGINAL |
| 25 | §4.1 ¶1 (185) | B0060 | "confirmation-window coefficient still exceeds the announcement-window coefficient" | No match | ORIGINAL |
| 26 | §4.1 ¶3 (222–223) | B0068 | "constituents were, if anything, becoming less liquid just before October 2025" | No match (crypto-liquidity articles only) | ORIGINAL |
| 27 | §4.1 ¶5 (247) | — | "Randomization inference confirms that the declines are not what large HOSE stocks experienced" | No match | ORIGINAL |
| 28 | §4.2 ¶1 (256) | B0076 | "cross-sectional t-statistics, which ignore the common event date, are up to three times larger" | No match (Kolari & Pynnönen, topic only) | ORIGINAL |
| 29 | §4.2 ¶2 (316) | B0083 | "The fading after the first, conditional announcement is consistent with temporary price pressure" | No match. The tool's claim of an exact-phrase hit in a UNC policy paper is unsubstantiated. | ORIGINAL |
| 30 | §4.2 ¶3 (319) | B0084 | "announcement-week gain of stocks that later appeared on the lists reflects characteristics" | No match | ORIGINAL |
| 31 | §4.2 Takeaway (322) | B0085 | "Prices rose in the announcement week and at the confirmation under every benchmark" | No match | ORIGINAL |
| 32 | §4.3 ¶1 (328) | — | "Named-but-excluded stocks show no surge on either day" | No match | ORIGINAL |
| 33 | §4.3 ¶2 (358) | B0094 | "That absence is a direct falsification test: a general rise in trading" | No match | ORIGINAL |
| 34 | §4.3 Takeaway (361) | B0095 | "Trading concentrated at the first-tranche rebalancing close on included stocks only" | No match (index-rebalancing practitioner articles, topic only) | ORIGINAL |
| 35 | §4.4 ¶2 (370) | B0098 | "with three stocks each in the two upper segments clustered inference is unreliable" | No match (MacKinnon, Nielsen & Webb guide, topic only) | ORIGINAL |
| 36 | §4.4 Takeaway (389) | B0102 | "Index weight scales the rebalancing trade; the liquidity gain is largest" | No match | ORIGINAL |
| 37 | §4.5 ¶1 (395) | — | "rising volatility pushes the ratio up; the measured decline in illiquidity therefore understates" | No match | ORIGINAL |
| 38 | §5.1 Pre-announcement (453) | B0116 | "The pre-period deviations in Figure 1 are positive, so they work against" | No match | ORIGINAL |
| 39 | §5.1 Trading value (459) | B0118 | "Trading value behaves differently from the Amihud ratio" | No match (Lou & Shu, topic only) | ORIGINAL |
| 40 | §5.1 Inference (462) | B0119 | "Excluding the three Vingroup-family stocks changes the estimates by at most" | No match (The Investor valuation articles, topic only) | ORIGINAL |
| 41 | §5.1 Sector/pre-funding (465) | B0119 | "removal of pre-funding requirements for foreign investors" + Vietnam FTSE (partly unquoted) | The LSEG press release of 7 April 2026 says FTSE "recognised the progress … in removing the prefunding requirement". The manuscript attributes this to LSEG (2026) in different words. | PARAPHRASE |
| 42 | §5.2 ¶1 (474–475) | B0122 | "named as eligible but did not include allow a direct test of selection" | No match | ORIGINAL |
| 43 | §5.2 ¶2 (478) | B0123 | "which gives a reason other than liquidity for its later addition" | No match | ORIGINAL |
| 44 | §5.2 ¶3 (529) | B0132 | "The constituent estimates combine the upgrade's effect with FTSE's selection" | No match | ORIGINAL |
| 45 | §5.2 Takeaway (532) | B0133 | "selection does not account for the whole liquidity response" | No match | ORIGINAL |
| 46 | §6 ¶1 (538) | B0135 | "brought liquidity and price gains to likely index stocks at FTSE's disclosures" | No match (FTSE 100 revision papers, topic only) | ORIGINAL |
| 47 | §6 ¶2 (541) | B0136 | "These findings favour the recognition channel over the price-pressure channel"; also "A frontier-to-emerging upgrade differs from a routine reconstitution because it changes which benchmark family" | No match for either fragment | ORIGINAL |
| 48 | §6 ¶3 (544) | B0137 | "investors used observable size and liquidity to anticipate eligibility" | No match | ORIGINAL |
| 49 | §6 ¶4 (547) | B0138 | "investors weighted their attention by expected index weight" | No match | ORIGINAL |
| 50 | §6 ¶5 (550) | B0139 | "The selection evidence sets a boundary on these conclusions" | No match | ORIGINAL |
| 51 | §6 ¶6 (553) | B0140 | "clear and early communication of reclassification steps bringing the response forward" | No match (HR reclassification pages) | ORIGINAL |
| 52 | §6 ¶7 (556) | B0141 | "cannot be fully separated from the concurrent removal of pre-funding requirements" | No match (Vietcap and Mondaq pre-funding notes, topic only) | ORIGINAL |

**Checked outside the denominator**

| Location | Patch | Fragment searched | Result | Grade |
|---|---|---|---|---|
| Abstract (8) | B0003 | "The liquidity and price response to Vietnam's upgrade came with FTSE's disclosures" | No match (news on the upgrade, topic only) | ORIGINAL |
| Table 4 notes (313) | B0082 | "CAR divided by the standard deviation of daily portfolio abnormal returns in the estimation window" | Standard event-study test described in different words (EventStudyTools, eventstudy.de) | COMMON_KNOWLEDGE |
| Table 5 notes, added sentence (355) | B0093 | "that reference session was unusually active and several earlier sessions then show significant negative coefficients" | No match | ORIGINAL |
| Table 9 notes, added sentence (526) | B0131 | "clustered inference is not informative with two stocks" | No match | ORIGINAL |
| AI-use declaration (609) | B0155 | "After using this tool, the authors reviewed and edited the content as needed and take full responsibility…" | This is Elsevier's required disclosure template, copied word for word as the publisher requires. It is not an originality issue. | Template (exempt) |

### Cited-literature paraphrase check (manuscript wording compared with the source abstract)

The abstract text comes from WebSearch result renderings in this run, cross-checked against the snippets that the Stage 4.5 Phase A/B agents recorded in `phaseAB_group1.md` and `phaseAB_group3.md`. Publisher pages could not be opened.

| Source | Manuscript wording (location) | Source abstract wording | Assessment |
|---|---|---|---|
| **Biktimirov & Afego (2026)** | §2.3 ¶1: "study changes to the FTSE Frontier 50 Index from 2008 to 2025. Additions earn persistent price gains, **country reclassification events show distinct return and volume effects**, and the authors attribute the gains to institutional demand rather than to trading pressure or liquidity." | "examines short-term stock market reactions to changes in the FTSE Frontier 50 Index from 2008 to 2025 … Both new and repeated additions experience persistent stock price increases … **Country reclassification events exhibit distinct return and volume effects.** … consistent with institutional investor demand as the underlying mechanism, rather than temporary trading pressure or liquidity effects" | **CLOSE_MATCH.** One clause is near-verbatim, with 8 of 9 words identical and one verb substituted. The passage follows the abstract's sentence order: data, then additions, then reclassification, then mechanism. The index name and dates are unavoidable facts and are not counted. The source is cited. |
| Biktimirov & Afego (2026) | §1 ¶3: "index additions raise prices persistently, and the evidence points to institutional demand rather than trading pressure or liquidity changes as the cause"; §6 ¶2: "index effects reflect investor demand rather than liquidity alone" | As above | PARAPHRASE. The "rather than … trading pressure or liquidity" frame echoes the source, but the sentence structure differs. The source is cited. |
| Dong et al. (2023) | §2.3 ¶1: "the included stocks earned abnormal returns around the announcement, and market quality changed over the longer run through liquidity, turnover and price synchronization" | "In the short term, the underlying stocks gained cumulative excess returns before and after the announcement date … In the long run, including A-shares in the index may improve market quality by influencing stock market synchronization and liquidity and turnover rate." | PARAPHRASE (borderline). The short-run/long-run structure and the list of variables are shared, but these are the paper's technical variables. The sentence is compressed and reworded. The source is cited. |
| Hegde & McDermott (2003) | §1 ¶3: "raise trading activity and narrow spreads for years"; §2.2 ¶1: "S&P 500 additions narrow spreads and raise trading activity persistently, which they attribute to more information and more trading interest" | "we find a sustained increase in the liquidity of the added stocks … due primarily to a decrease in the direct cost of transacting and a smaller decline in the asymmetric information component" | PARAPHRASE. The wording is clearly different. |
| Becker-Blease & Paul (2006) | §1 ¶3: "added firms with larger liquidity gains invest more"; §2.2 ¶2: "firms added to the S&P 500 with larger liquidity improvements increase capital investment" | "a positive relation between changes in capital expenditures and changes in stock liquidity" | PARAPHRASE. The wording is clearly different. |
| Raddatz et al. (2017) | §1 ¶2, §2.3 ¶1, §4.4 ¶1, §6 ¶4 | "Benchmarks have statistically and economically significant effects on the allocations and capital flows of mutual funds across countries"; "Exogenous, pre-announced changes in benchmarks result in movements in asset allocations and capital flows" | PARAPHRASE. No fragment matched. |
| Bekaert et al. (2007) | §1 ¶2 "liquidity is priced in emerging markets"; §2.3 ¶2 "local market liquidity predicts returns in emerging markets, where segmentation from global capital is only partial" | "Local market liquidity is an important driver of expected returns in emerging markets, and the liberalization process has not fully eliminated its impact" | PARAPHRASE. The term "local market liquidity" is shared, but the rest is restructured. |

---

## D1 grade distribution (52 sampled body paragraphs)

| Grade | Paragraph count | Proportion |
|---|---|---|
| ORIGINAL | 40 | 76.9% |
| COMMON_KNOWLEDGE | 4 | 7.7% |
| PARAPHRASE | 7 | 13.5% |
| CLOSE_MATCH | 1 | 1.9% |
| VERBATIM | 0 | 0.0% |
| **Total** | **52** | 100% |

Among the 34 paragraphs touched in round 2, every one was graded ORIGINAL, COMMON_KNOWLEDGE or PARAPHRASE. The only CLOSE_MATCH is in §2.3 ¶1 (line 71), which the round-2 patch did not touch. The wording has been there since an earlier draft, and neither the Stage 2.5 nor the Stage 3/3' checks flagged it.

---

## D2. Self-plagiarism check

**Status: NOT PERFORMED.** Author names were not supplied, and the manuscript is anonymized for review, so the D2 prerequisite ("User provides author name(s)") is not met.

- §1 ¶3 and §6 ¶4 refer to "an earlier study of the same market by the present authors (anonymized for review)", an index-level study of FTSE watch-list reviews.
- No copy of that study exists under `/home/user/B-i-FTSE2`. A search for `.md`, `.txt`, `.docx`, `.pdf`, `.tex` and `.doc` files outside `.git` found only three kinds of file: ARS pipeline artifacts, run and fetch logs in `output/` and `data/`, and earlier drafts of this same manuscript (`ars/stage2_write/manuscript_v1–v3.md` and their `.docx` previews).
- A quoted web search of the manuscript's one-sentence summary of that study ("watch-list reviews did not coincide with structural breaks in index-level liquidity") found no public match.
- No author was guessed. D2 should be run once the authors supply their names or the earlier paper. Priority targets: §3.1–3.2 method descriptions and the §6 ¶4 summary of the earlier study.

---

## D3. AI writing characteristic alerts (informational, MINOR)

| # | Indicator | Triggered? | Observation |
|---|---|---|---|
| 1 | Excessive smoothness | No | Sentence length across the 292 body sentences: mean 23.2 words, SD 11.8, coefficient of variation 0.51, range 1–62. Rhythm varies normally. |
| 2 | Lack of specificity | No | Paragraphs are dense with coefficients, dates, tickers and table references. |
| 3 | Formulaic transitions | No | "Furthermore", "Moreover", "It is worth noting", "Additionally", "Notably" and "Importantly" each appear 0 times. |
| 4 | Excessive parallelism | **Yes** | §4.1–§5.2 each end with a bolded "**Takeaway.**" paragraph (6 in total), and every §4 heading is a claim sentence. The contrast "X rather than Y" appears 11 times in 9,726 body words (§2.3, §4.2, §4.3, §6). |
| 5 | Hedging overload | No | "may" appears 2 times, "could" 9 times, "might" 0 times. Hedges are tied to specific limitations, and results are stated directly. |
| 6 | Citation-argument gap | No | Citations support specific mechanisms (§2.2–2.3) or methods (§3). Remove them and the arguments lose their support, so they are integrated. |

Indicators triggered: **1 of 6**. This is below the threshold of 2, so no "AI writing characteristic alert" is raised. No determination is made about whether the text was AI-generated. The manuscript's own declaration discloses that Claude was used to draft text. The authors may still want to reduce the uniform "Takeaway" device or vary the "rather than" contrasts.

---

## Phase D issue list

The protocol's severity codes are used. In the agent report format, MODERATE falls in the "MEDIUM (Must Fix)" bucket.

| ID | Severity | Type | Location | Issue | Matching source | Recommended action |
|---|---|---|---|---|---|---|
| IL-MEDIUM-1 | **MODERATE** | CLOSE_MATCH (cited) | §2.3 ¶1, line 71: sentence beginning "Additions earn persistent price gains, …" | The clause "country reclassification events show distinct return and volume effects" is nearly identical to the abstract's "Country reclassification events exhibit distinct return and volume effects": 8 of 9 words, one verb swapped. The Biktimirov & Afego passage also follows the abstract's sentence order. This is one instance at the protocol's "individual paragraph inadequately paraphrased" level. The source is cited, so this is not misconduct. | Biktimirov & Afego (2026), *IREF* 110, 105562, abstract as rendered by WebSearch (ScienceDirect PII S1059056026006751). The publisher page was blocked, so the authors should confirm against the published abstract. | Reword the clause in the authors' own terms, or quote it with a page or abstract reference. Also vary the order of the three-sentence summary. Re-verify only this paragraph afterwards. |
| IL-MINOR-1 | MINOR | PARAPHRASE, borderline | §2.3 ¶1, line 71: the Dong et al. (2023) sentence | Follows the source's short-run/long-run structure and variable list ("market quality … liquidity, turnover … synchronization"). | Dong et al. (2023) abstract | Optional: recast in terms of what matters for this paper's comparison. |
| IL-MINOR-2 | MINOR | AI-writing indicator (informational) | §4.1–§5.2 Takeaways; "rather than" ×11 | 1 of 6 indicators triggered, below the alert threshold | — | Optional stylistic variation. This does not affect the verdict. |
| — | Note | D2 not performed | §1 ¶3, §6 ¶4 | Author names were not supplied, and no copy of the earlier index-level study is in the repository. | — | Run D2 when the author identities or the earlier paper are available, before formal submission. |
| — | Note (outside Phase D; for the Phase E / E5 owner) | Related literature surfaced by search | §2.3 ¶1 absence claim ("No study we know of … estimates the stock-level liquidity effect of a frontier-to-emerging reclassification …") | Searches in this run repeatedly returned Pandolfi & Williams, "Investing in the Presence of Massive Flows: The Case of MSCI Country Reclassifications" (NBER w23557), and "From Frontier to Emerging: Does Market Reclassification Matter?". Both study reclassifications at country or index level, so they do not contradict the stock-level, search-bounded claim, but neither is cited. | NBER w23557; ResearchGate 228123982 | Phase E / E5 to judge. This is not an originality finding. |

**Phase D outcome:**
- **FAIL: 1 MODERATE** (IL-MEDIUM-1). Under the protocol's severity-to-verdict mapping, MODERATE means "FAIL, must fix".
- There are no CRITICAL or SERIOUS findings and no VERBATIM matches.
- All paragraphs added or changed in round 2 passed.
- The fix is one sentence, and only that paragraph needs re-verification.

---

## Tool limitation disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 72.2%, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

This run had further limits beyond the standard disclaimer:
1. WebFetch, doi.org, Crossref and ScienceDirect were blocked by the egress proxy, so source abstracts come from search-result renderings rather than publisher pages.
2. The search tool's summaries sometimes claimed exact-phrase matches that its listed results did not support. Grades were assigned from the result titles and quoted snippets, not from those claims.
3. Unquoted paraphrase searches (search term 2) were run only for the cited-literature comparisons, not for every paragraph.
4. Cross-language similarity with Vietnamese-language sources was not tested.
5. D3 indicators are heuristic, with a high false-positive rate.
