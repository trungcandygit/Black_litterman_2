# Language edit log: author's copy-edit of the MSJ version (2026-10-06)

Standard applied: `academic-research-skills/academic-paper/references/academic_writing_style.md` (precision, conciseness, hedging, tense table: literature findings and completed procedures in past tense), `writing_quality_check.md`, and `scripts/check_acronyms.py` (advisory; no findings after edits, ISO allowed). About 195 word-level differences were screened. Accepted edits are in `paper2/manuscript/msj/lang_edits.py`.

## Accepted (examples)
- Past tense for reported literature findings (found, showed, argued, linked, examined, reported, studied…) and completed procedures (kept, used, was dropped).
- Commas after introductory phrases; split long sentences ("…variability. In the model of…"; ". Table 1 *t*-statistics…"; ". Section 3 reports…").
- "the HOSE" used consistently; US date format (May 5, 2025; September 24, 2026; October 4 and 5, 2026); numbers below ten in words (eight quarters, seven of them, four placebo dates).
- Word choice: requires (for needs), remained, whereas, compared with, maintain, presents the results of, accounts for, reapplied, an overnight gap and an intraday return, limit exposures, a stronger long-run reversal, a similar size.

## Not applied (meaning or correctness would change)
| Proposed | Kept | Reason |
|---|---|---|
| "after a limit closes", "after the limit closes", "After a floor closes" | after a limit close / limit closes / a floor close | "close" is the noun (a closing price at the limit); the verb form says the limit itself closes |
| "control for the false discovery rate" | control the FDR | statistical term: a procedure controls the FDR |
| "split events during the 2025 platform change" | split the events at the 2025 platform change | the change is the split point, not a period |
| "weights throughout the day d+k" | weights through day d+k | weights use data up to day d+k |
| "abnormal values minus the market counterpart" | subtract | verb needed |
| "A buyer in the next open… less of the" | at the next open… less the | idiom |
| "Table 1 shows the returns", "Figure 2 shows the event days" | requires / uses | the sentence states sample requirements |
| "The family has m = 26 22 characteristics" | m = 26 tests: 22 characteristics… | the count was lost |
| "The limit closes the cluster in market episodes" | Limit closes cluster in market episodes | garbled |
| "our null hypothesis does not contradict theirs" | our null result | the null here is an estimate, not a hypothesis |
| "…below the MDE and limits that censor…, can each" | original comma structure | the two causes would merge into one clause |
| "leaves all four significant differences" | leaves all four significant | they are tests, not differences |
| "confirmation-half-week-clustered t" | confirmation-half week-clustered t | two separate modifiers |
| "A stock that closes its ceiling" | closes at its ceiling | meaning |
| floor close-to-close return "1.65%" | −1.65% (from R output) | sign lost |
| "stocks that are also closed", "stocks that are closed at their high" | stocks that also closed at their high (low) | meaning |
| "quantifies the breaks", "a gap of 1.59 points lower" | the break; a gap 1.59 points lower | one break; comparative |
| "news and retail attention persists… produces" | persist… produce | compound subject |
| "stock days", "corporate action adjustment", "regression discontinuity claim", "standard error estimators", "day d move" | hyphenated compound modifiers | hyphenation of compound modifiers before a noun |
| "These studies compared…, sorted…, and split" | or split | different studies do different things |
| "common, and call auctions set…" | no comma | both conditions define where the question is sharpest |
| "the record we access" | we could access | tense and meaning |
| "mostly where retail investors…" | especially where | the effect is strongest there, not mostly located there |
| "The minimum detectable effect… was" | is | definition |
| "We depart from it" | departed | completed procedure (past) |
| "appeared in both periods", "contained" | present tense in Results | Results describe the estimates in the present tense throughout; a single past-tense verb would be inconsistent |
| "As the events are unbalanced" | Because | "as" is ambiguous (causal or temporal) |
| Limitations without "(i)" | (i) kept | the list continues with (ii)–(viii) |
| "Viet" / citation changes | Viet Nam News (2025) | reference integrity |

Also fixed: table notes printed the Unicode minus and en dash as "<U+2212>"/"<U+2013>" (R string encoding); they now render as − and –.
