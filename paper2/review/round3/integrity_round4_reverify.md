# Integrity re-verification of the round-4 integrity fixes (Stage 4.5, narrow scope)

Date: 2026-10-06. Verifier: independent integrity_verification_agent. Scope: Issues 1–7 of `review/round3/integrity_round4.md` and advisory A4 (response letter item 4), nothing else. Read-only: no manuscript, code or output file was edited.

Files compared:
- `manuscript/manuscript_final.Rmd` (fixed) against `review/round3/manuscript_before_integrity4_fixes.Rmd`. Seven hunks differ (lines 101, 119, 199, 203, 210, 247, 363), and each one maps to an issue.
- Rendered text: `pandoc manuscript/manuscript_final_styled.docx -t plain`. The docx was built 14 s after the Rmd.
- `final/Paper_C_Closing_at_the_limit.Rmd` and `.docx` are byte-identical to the manuscript files. The `.md` diff in the commit is rewrapping only.
- `R/52_reviewer_round4.R`; `output/tables/C22`, `C28`, `C29`, `C30` and `C31`; `review/round3/response_round4.md`; `process/04_literature_search_log.md`; `process/08_literature_review_benchmark.md`.
- Git: I checked the uncommitted diff first. After the author's commit 6338562, I checked `git diff HEAD~1`.

## Verdict: PASS

All seven fixes are applied as suggested, and every number they add matches a saved table. They introduce no new error. The rendered text contains no U+FFFD characters and no unevaluated inline R. The response letter's item 4 is accurate. Three advisory notes follow; none of them blocks.

## Issue-by-issue

**Issue 1 (floor placebo): FIXED.**
- Rendered text: "positive at the 4 placebo dates before the platform change and negative at all 11 later ones … −0.95 points (t = −3.2) … 2025-Q2 (−0.34%) … (802)".
- Checks against C30:
  - The 4 pre-May-2025 floor differences are all positive: 0.54, 0.18, 0.41, 0.70.
  - The 11 later differences are all negative, from −0.63 to −0.99.
  - The KRX split is −0.9515 with t = −3.172.
  - "Close to the differences at the placebo dates that follow it" holds, since those run from −0.63 to −0.99.
- Checks against C29:
  - The 2025-Q2 floor gap is −0.337%.
  - The 2025-Q2 floor count of 802 is the largest of any quarter.
  - The quarterly floor gaps (−1.50, −1.70, −0.34, −0.86, −1.39, −1.39, −1.46, −1.55) show no trend, so "no trend" is supported.

**Issue 2 (DiD qualifiers): FIXED.**
- "gives the same answer" became "points the same way for the ceiling". This is supported by C31: the ceiling change is 0.38 with t = 0.8.
- The closing clause now reads "…the raw ceiling close-to-close return and of the raw floor gap does (Table 4). Like the split in Table 4, these comparisons describe timing and do not identify an effect of the auction rules."
- C22 supports the clause. The ceiling cc1 t is 0.95 before the change and 14.6 after it. The floor gap t is −1.85 before and −7.05 after. Table 4 is the KRX split table (call-out at line 190).

**Issue 3 (C29 counts): FIXED by code.**
- `52_reviewer_round4.R` now uses `ceiling_n = unname(a["n"])` and `floor_n = unname(b["n"])`.
- Only the counts in 2026-Q2 and 2026-Q3 changed: 298→297, 100→99, 246→239 and 178→175. The gap means and *t* values in C29 are unchanged.
- The columns now sum to 3,199 and 2,111, which equals C16 and C28 baseline n.
- The only output file changed in the commit is C29.
- Caption: "Counts are events with a day-*d*+1 open. The first and last quarters are partial." This is accurate.
- The 2025-Q2 count stays at 802 and remains the largest floor count, so the Issue 1 sentence still holds.

**Issue 4 (t bound): FIXED.**
- The rendered text reads "all t above 2.9".
- The C28 minimum ceiling gap_mkt *t* is 2.998 (locked days), so the statement is true.

**Issue 5 (ex-dates): FIXED.**
- The clause now reads "…leaves unchanged except on ex-dates;". This matches Section 7.

**Issue 6 (Appendix B and Declarations): FIXED.**
- The new paragraph matches the logs on each point:
  - The dates are 4 Oct (04 log) and 5 Oct (08 log).
  - The search used the AI assistant's web search tool. Both logs record "WebSearch".
  - No Scopus or WoS access was available.
  - Pages could not be opened (08 log, line 7).
  - Every listed topic appears in the 04 query list or the 08 scope, including band changes (08 §1B) and HOSE/HNX (08, line 91).
  - The appendix says "exact query strings were not logged", which is true: the logs list only topics.
  - About 100 records were screened (08, line 16).
  - The appendix states the exclusions: Vietnamese-language journals and incomplete coverage of Chinese A-share studies (04, line 42).
  - It describes the reading as "abstract text returned by the search tool".
  - Its last sentence is now limited to peer-reviewed studies.
- The Declarations line now reads "…used Claude (Anthropic) to run the literature searches (Appendix B), write analysis code, …".

**Issue 7: FIXED.** The sentence now reads "…pays for every candidate signal in the plan;".

**Response letter item 4 (A4): accurate.**
- The letter now says the floor difference is positive at every placebo date before May 2025 and negative at every later one, and that the placebos cannot separate this pattern from a break.
- It gives the Table 5 counts as 3,199 / 2,111.
- The other numbers in the item (2.91 pp, t = 6.2; 0.38 pp, t = 0.8) match C31.

## Advisory notes (non-blocking; record only)

- R1. The letter says the pattern is "tied to a weak 2025-Q2 floor gap", while the manuscript says "coincides with". "Coincides with" is the safer wording; aligning the letter to it is optional.
- R2. `sum(pl$break_date > "2025-05-05")` counts the later dates, not the negative ones. It is correct for the current C30 (all 11 are negative). If C30 is ever regenerated, a guard such as `sum(pl$floor_gap_diff < 0 & pl$break_date > "2025-05-05")` would keep the sentence true by construction.
- R3. The 04 log says WebFetch worked "for some hosts", while the 08 log says no page could be opened. The appendix's "publisher pages could not be opened" agrees with 08, and no log records a publisher page being opened. It is consistent as written.
