# Stage 4.5 narrow re-verification, round 5 (MSJ version)

Agent: integrity_verification_agent (independent, read-only on manuscript and code). Date: 2026-10-06.
Scope: commit 99ff9d1 ("Paper C MSJ round 5"), i.e. `manuscript/msj/revisions_r5.py`, `lang_edits.py`, `build_msj.py`, `fill_template.py`, `mathtext.py`, the generated `manuscript_msj.Rmd`, `final/MSJ/Manuscript_MSJ.docx` and `final/MSJ/Supplementary_Material_S1.docx`.
Method: pandoc plain-text render of the old (ef9ccc2) and new docx, sentence-level diff; abstract read from `word/document.xml` (it sits in a text box that pandoc skips); every inline R call in the rewritten paragraphs re-evaluated by sourcing the Rmd setup chunk against `output/tables/*.csv`; process records `process/03_brainstorm_round2.md`, `process/decisions.md` (A3, item 42), `process/04_literature_search_log.md`, `process/08_literature_review_benchmark.md`, `R/40_zoo.R`, `R/48_revision.R`; web search for the two new references.

## Verdict: FAIL (one citation error, one inaccurate process statement, two consistency defects). All numbers PASS.

## 1. Numbers (PASS)

| Passage | Rendered | Source value | OK |
|---|---|---|---|
| Abstract | gap 2.2%; gives back about 24% | C16 Ceiling all gap 2.2435, intraday −0.5354; 0.5354/2.2435 = 23.9% | yes |
| Abstract | 2.7 pp vs rises short of limit | C17 ceiling vs 5–6.5% up, diff 2.658 | yes |
| Abstract | loses 0.7% by fifth close | C11 Ceiling rule-based f5o_mkt −0.749 (t −2.75) | yes |
| Abstract | ceiling gap in every quarter and before platform change | C29 min t 2.49; C22 pre 1.65 (t 3.16) | yes |
| Abstract | limit tests survive, no characteristic does | C3 survives 4/4 and 0/22 | yes |
| Floor para | −0.97% (t −4.6); intraday 0.30% | C16 −0.9722, −4.648; 0.3040 | yes |
| Exact/near hits | 2.79, 2.39, 1.67; 6.89 vs 6.90; 83% | C11; C27 rows 7–9 (6.898, 6.893, 82.7) | yes |
| Ceiling robustness | 1.52%; ctrl 2.70% | C16 tercile 3 1.5187; C11 gap_ctrl 2.6968 | yes |
| Floor robustness | ctrl cc1 −1.65%; removes 1,371 of 2,111; t −1.0 | C16 −1.6508; 2,111 − 740 = 1,371; tercile 1 t −0.973 | yes; meaning unchanged (old: 740 remain) |
| Table 3 para | 2.66 (t 14.0), 0.31; floor 1.59 (t −9.7); 3.14 (t 14.5), 1.81; 2.40 and 1.14 | C17, C23 | yes |
| KRX para | 1.65/2.49 (t 1.6); −0.42/−1.37 (t −3.2); 0.64; −1.73/−0.15; 71%, 58%; t 1.0, −1.9 | C22 (936/3199 = 29%, 2263/3199 = 71%; 1220/2111 = 58%) | yes |
| Table 5 / placebo | eight quarters, t 2.5–16.8; floor sig. in seven; −0.45 to 0.72, |t| ≤ 1.4; 0.85 (t 1.6); four of four before, 11 of 11 after; −0.95 (t −3.2); −0.34%, 802 | C29, C30 | yes |
| DiD | 2.91 (t 6.2), 0.38 (t 0.8); −1.62 (t −6.6), −0.49 (t −1.5) | C31 | yes |
| Inference sentence | 683 | C21 row 5 (t/date) = 683; 0.05/7.311e−5 = 683.9 | yes |
| Limitations (iv) | "only 25% to 58% of closes" | C27 rows 2, 4, 6 = 24.5, 30.6, 58.0 (row 4 lies inside the range) | yes; dropping the uninformative below-10 check loses nothing |
| m_max para (Section 3) | 683 / 125; 0.00007 / 0.00040 | C21 | yes; "(Section 3)" cross-reference is correct |

No number changed meaning. The split sentences keep every value of the old wording.

## 2. Claim strength

- H4 restatement ("abnormal return from the next open to the fifth close is then zero or negative") is consistent with C11 f5o_mkt −0.75% (t −2.75). PASS. Note: the abstract now says only "Floor closes are followed by a negative gap whose size depends on the benchmark"; the gap does vary by benchmark (C11: −0.97 market, −1.75 control, −1.08 EW), so this is accurate, though the body's benchmark evidence is the close-to-close return. Acceptable.
- Abstract drops the "lower-powered" qualifier on the 22 characteristics ("none of the characteristics does"). Factually correct; optional: restore "none of the lower-powered characteristic tests does" so the abstract does not read as evidence of no effect (MDE caveat). Minor, not a FAIL item.
- "For market design, the results suggest ... the 7% band postpones" is hedged and the preceding sentence lists the alternatives. PASS.
- **Inference sentence — FAIL (F2).** "The family *p*-values follow the analysis plan, which fixed the normal reference before any result was computed" is not supported by the record. The plan (`process/03_brainstorm_round2.md`, "Pre-registered family"; `decisions.md` A3) specifies "standard errors clustered by date" only; it names neither the reference distribution nor the omission of G/(G−1). Both conventions were introduced in the first analysis code (`R/40_zoo.R` line 66, `EV$p <- 2 * pnorm(...)`, `clus()` without the factor), which the manuscript itself says post-dates the plan ("A version-control time stamp dates the plan before the first analysis code"). The rest of the sentence is accurate: Table 1 uses the factor and a *t* reference (`R/48_revision.R` `cl1`, `tref`); under t/date the bound is 683 (C21); the week-cluster family also keeps all four event tests (C20: all TRUE; C32 max adjusted p 0.0026), so "does not change any conclusion" holds.

## 3. New references

- **Farber, Nguyen & Vuong (2006)** — EXISTS. CEB Working Paper No. 06/005, Université Libre de Bruxelles, Solvay Business School, Centre Emile Bernheim, April 2006 (RePEc sol/wpaper/06-005; ULB DI-fusion `rou-0199.pdf`; author list "Farber A, Nguyen VN, Vuong QH" in Vuong's publication list). Abstract: "anomalies of the HSTC stock returns through clusters of limit-hits, limit-hit sequences; strong herd effect...". The in-text description ("documented clusters and sequences of limit hits in the early years of the market") matches. PASS. Note: the RePEc listing title reads "...Vietnam stock market**s**..."; the PDF cover reads "Stock Market". Either is defensible; keep as is.
- **Le (2018) — FAIL (F1, wrong year and incomplete record).** The record at https://vjol.info.vn/ed/article/view/34298 exists (title matches; GARCH study of SSC narrowing the fluctuation limit after the late-2007 fall, from March 2008). But the article is Le Dinh Nghi, *Journal of Economic Development* (University of Economics Ho Chi Minh City), No. 214, October **2012**, pp. 116–128 (ResearchGate 302027844; Academia 32714734). This project already verified it as **Le (2012), No. 214, pp. 116–128** (`review/integrity_stage2_5_round2.md` l.55, `round3.md` l.13/65; `decisions.md` items 36/38). "2018" is likely the VJOL upload date. The reference also lacks issue and pages, as the caller noted, and "Journal of Economic Development" is ambiguous (a different journal of that name is published by Chung-Ang University, Korea), so the publisher should be named. The in-text description ("evaluated how narrower bands after 2008 affected stock price risk") matches the abstract. Note: `process/09_dialogue_log_for_observer.md` l.621 records that Le (2012) was earlier dropped because its peer-review status was unverified; the round-5 decision to re-add it should be logged in `process/decisions.md`.

## 4. Removed universal negatives

- Gone from body, abstract and Table 6 note: "no peer-reviewed study...", "records we could access had no magnitudes", "None of the studies identified by our search...", "among the studies identified by our search, none tests...". PASS.
- **Residual (F3):** Section 1.1, "Band changes and investor-level data" paragraph, last sentence: "Liang and Hu (2025) forecast limit hits; **the record we could access** reports no returns after the hit." It is the same "records we could access" construction and was not removed.
- Table 6 note now reads "Main published finding of each study..."; several entries were taken from abstracts/search records, not full texts (`process/08`, e.g. Huang et al. 2001 "abstract not displayed"). It is not a universal negative, but "published finding" slightly overstates what was read. Optional wording below.
- **S1 consistency (F4):** S1.2 still says "working papers, theses, code repositories, and press items were not used as evidence", but the article now cites the Farber et al. (2006) working paper, and S1.2 itself says the second search "added ... the working paper of Farber et al. (2006)". S1.2's last sentence ("Statements in this paper that no study reports a given result refer to...") is now nearly vacuous after the removals. It is harmless, but it can be cut. S1 also cites "Le (2018)" (year error carries over).
- Huang et al. (2001) new wording ("overnight overreaction after limit hits reverses on the following day") matches the search-record description logged in `process/08` l.24/101. PASS.

## 5. Rendering (PASS)

No "[[", "<U+", unevaluated `r`, or `[[EQNUM` in either docx (document.xml checked). Equations (1)–(8) each appear once as numbered two-cell tables. "(i)" is present at the start of Limitations, followed by (ii)–(viii). The reference list is alphabetical with both new entries placed correctly. Akbas et al. (2022) and Lu et al. (2023), whose sentence in the Discussion was removed, are still cited in Section 1.1, so there are no orphan references. The abstract text box appears twice in document.xml only through the mc:AlternateContent fallback (normal).

## Exact fixes

**F1 (revisions_r5.py, NEW_REFS and the "Studies on band changes" paragraph; build_msj.py S1 replacement string):** change every "Le (2018)" to "Le (2012)" and the reference to:
`Le, D. N. (2012). Evaluating impacts of reduction in fluctuation limit on stock price risks in Vietnam. *Journal of Economic Development* (University of Economics Ho Chi Minh City), (214), 116–128. https://vjol.info.vn/ed/article/view/34298`
Log the re-addition and the year correction in `process/decisions.md` and `process/04_literature_search_log.md`.

**F2 (revisions_r5.py, INFERENCE_NEW):** replace the second sentence with:
"The family *p*-values keep the convention of the first computation of the planned tests; the analysis plan specified date-clustered standard errors but not the reference distribution, and we did not change the convention after seeing the results, so that the multiplicity control is not tuned to them."
Optionally append the week-cluster figure to the last sentence: "...in families of up to 683 tests with date clusters and 125 with calendar-week clusters (Section 3)...".

**F3 (source of Section 1.1 "Band changes and investor-level data" paragraph; extend revisions_r5.apply):** replace "Liang and Hu (2025) forecast limit hits; the record we could access reports no returns after the hit." with "Liang and Hu (2025) forecast limit hits but do not study returns after the hit." (only if the abstract supports it), or simply "Liang and Hu (2025) forecast limit hits."

**F4 (build_msj.py, S1 replacement):** change "working papers, theses, code repositories, and press items were not used as evidence, except for press and brokerage descriptions of HOSE rules (Section 2.1 of the article)" to "...were not used as evidence, except for press and brokerage descriptions of HOSE rules (Section 2.1 of the article) and the working paper of Farber et al. (2006), cited as background on the early market". Optionally delete the final sentence "Statements in this paper that no study reports a given result refer to the peer-reviewed studies this search identified."

**Optional (not a FAIL item):** Table 6 note: "*Note.* Main finding of each study as stated in its abstract or bibliographic record (Supplementary Material S1), compared with ours by sign, timing, and mechanism." Abstract: "whereas none of the lower-powered characteristic tests does."

Re-verification needed after the fixes: F1–F4 only (text and reference edits; no numbers affected).
