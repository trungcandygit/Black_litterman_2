# Response to Reviewer Comments — Paper C, round 1 → revision v7

Manuscript: "Closing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange" (source `paper2/manuscript/manuscript_C.Rmd`; round-1 version preserved as `review/round1/manuscript_C_v6.Rmd`, revised version `review/round2/manuscript_C_v7.Rmd`).
Editorial decision: Major Revision (`review/round1/synthesis.md`). Every roadmap item is answered; declined or partial items stay visible with the reason. Section numbers refer to v7. New numbers come from `paper2/R/48_revision.R` (tables C18–C25).

## Summary of changes
1. The status of the 26-test family is reworded from "pre-specified" to "fixed in a version-controlled project log before computation", with commit hashes and a file hash; the abstract no longer says "hold-out" and the Vietnamese abstract now says what the English text says.
2. New inference for the event tests (calendar-week and 10-day-block clusters, t reference, the specified weeks-39/40 split, survival rule re-run). All four tests still survive. Honest consequence: the five-day tests are carried by day t+1; over days t+2 to t+5 the ceiling effect is not significant and the floor effect fails the confirmation half.
3. The mechanism is downgraded from "delayed price discovery attached to the limit" to one hypothesis among three; "discontinuity" is replaced by "break at the limit". New comparison groups that also close at their high/low, and volume and prior-return terciles, are reported.
4. New sections: platform change of 5 May 2025 (4.8), outlier bound (4.7), tradable-return table (Table 6b), inference table (Table 3b).
5. Literature widened (price-limit theory, Turkish and Chinese evidence); novelty paragraph rewritten around the confirmatory/exploratory split; zoo reframed as a multiplicity device.
6. Declarations and AI-use disclosure extended; limitations updated.

## Roadmap items

**R1 / REV-1 (pre-specified label; EIC W1, W6; Perspective W1; Methodology W2; DA M1) — accepted, partly done.**
Changes: abstract, Section 1, Section 3.1, Section 7 and Appendix A now say "fixed in a version-controlled project log before the results were computed", not registered; the abstract states that the confirmatory result is the part already public and the new content is post hoc (Section 1, "Contributions and novelty"); the Vietnamese abstract is rewritten; "hold-out" removed from the abstract. The specification file (commit 63bdc6d, 07:23:38 UTC, SHA-256 in Appendix A) precedes the first commit with analysis code and results (9b8644b, 07:36:19 UTC). The originally specified t+2..t+5 test is reported (Table 3b, Section 4.2). Not done: an independent external time stamp (not obtainable in this environment; the manuscript says the authors should deposit one before submission). Commit dates are committer-set and the text says so.

**R2 / REV-3 (inference for t+1..t+5; Methodology W1; DA M4) — accepted, done.**
Table 3b and Section 4.2: week-clustered (95 weeks) and 10-day-block (46 blocks) statistics with a t reference. Ceiling five-day t: 4.00 → 3.67 / 3.81. Floor five-day confirmation-half t: −2.16 → −2.22 (week), −2.46 (block). The survival rule re-run on all 26 tests (table C20) leaves four of four surviving. Not done: Driscoll–Kraay or calendar-time portfolio estimates (listed in Limitations vii).

**R3 / REV-4 (mechanism vs news; comparison-group design; Domain W1, Methodology W3, Perspective W3; DA M2, M3) — accepted, partly done.**
Section 4.4: comparison groups restricted to stocks that also close at their high/low (Table 5b: ceiling gap +3.14 pp, t 14.5; floor −1.81 pp, t −8.7), so a strong close does not explain the contrast. Rival readings (unfilled demand, news/attention, auction overshoot) are stated; volume and prior-return terciles (table C24) show the gap grows with both, which fits attention as well as the unfilled-demand reading. "Discontinuity" is replaced by "break at the limit", and "delayed price discovery" is called a hypothesis. Not done: announcement-date split, order-book queue size and a limit-free placebo — no such data exist in the repository.

**R4 / REV-6 (regulatory and investor implications; Perspective W3, Domain W6) — accepted, done.** Section 5 "Implications, conditional on this market and window" no longer states what the limit does to price settlement.

**R5 / REV-7 (HOSE rules sourced; Domain W2) — accepted, partly done.** Section 2 cites HSC (2025) and Viet Nam News (2025) for the 7% band, reference price, and ATO/ATC change, and says explicitly that these are brokerage and press descriptions; exchange circulars were not consulted. Tick sizes and corporate-action reference-price treatment remain assumptions (Limitation iii). Special-band audit: replaced by an outlier exclusion (Section 4.7, table C25): dropping events within five days of a |return| > 8% leaves the ceiling gap at 2.26% (from 2.24%).

**R6 / REV-8 (KRX migration; Domain W3) — accepted, done.** Section 2 and new Section 4.8, Table 9: ceiling gap 1.65% before vs 2.49% after (difference t 1.6); floor gap −0.42% vs −1.37% (difference t −3.2); the post-open floor drift exists only before the change. The text says the split does not isolate an effect of the auction rules. "Single regime" removed (Limitation x).

**R7 / REV-9 (literature; Domain W4) — accepted, partly done.** Added and verified by web search: Subrahmanyam (1994), Bildik and Gülay (2006), Qi (2023). Not done: Vietnamese-language journals, further A-share studies and Le (2012) full text; Appendix C says so and the novelty claim stays bounded by the search.

**R8 / REV-10 (increment over Berkman et al. and the public analysis; EIC W2) — accepted, done by reframing.** Section 1 states that the gap-then-giveback signature exists without a limit (Berkman et al., 2012), that the close-to-close effect is already public, and that what a limit adds is the testable contrast with sub-limit moves.

**R9 / REV-11 (zoo vs limit structure; EIC W3) — accepted, done by reframing.** Sections 1 and 5: the 22 characteristics are a multiplicity device and a null benchmark with limited power, not a separate finding. The zoo section was not shortened.

**R10 / REV-13 (declarations, deposit, AI use; EIC W5, Perspective W2, Methodology W9) — accepted, partly done.** AI-use disclosure now names the agent roles, the shared model family, the absence of a cross-model verifier and that references and press-sourced facts have not been checked by a human; data/code availability states where the raw files are and that the vnstock version and retrieval dates were not recorded. Ethics, funding, competing interests and author contributions remain placeholders for the human authors by design.

**S1 / REV-5 (floor drift; DA M5) — accepted, done.** Section 4.6 reports the floor drift from open to day 5 (−1.23 pp against 5–6.5% fallers at their low, t −2.8) and says a gap-only mechanism does not explain it; Section 4.8 shows it is pre-platform-change only.

**S2 / REV-12 (power qualifier) — done.** Abstract and Section 5 state the 0.1–0.3 pp per week detectable scale.

**S3 / REV-14 (reference status) — partly done.** Veeraraghavan et al. (2007) is labelled a working paper. Le (2012), Chen (1993) and Berkman and Lee (2002) were not re-read against the originals; descriptions rest on abstracts (Appendix C).

**S4 / REV-15 (executability) — done.** Section 4.6 says the figures are quoted-open prices and reports the number of ceiling events locked at the open.

**S5 / REV-16 (table for −0.75%; count reconciliation) — done.** Table 6b; Section 4.7 reconciles the exact-tick counts (1,666 / 1,654 / 1,648 / 1,583).

**S6 / REV-17 (floor benchmark) — partly done.** The abstract flags the benchmark dependence (−0.71% vs −1.65%); Limitation xiii states that no beta- and size-matched five-day control was built.

**S7 / REV-18 (reference distribution) — done.** t reference stated; programme bound recomputed: 683 (t, date clusters), 125 (t, week clusters), against 816 with the normal reference.

**S8 / REV-19 (outliers, snapshot) — partly done.** Outlier exclusion done (C25); the post-sample listing snapshot cannot be bounded with the available data and remains a stated limitation.

**S9 / REV-20 (presentation) — done.** Duplicate table captions removed (captions now printed once); abstract restructured.

## Points where the revision changed the paper's claim
- "4 of 4 limit tests survive" holds for the implemented horizons, but the multi-day horizon adds nothing beyond day t+1. The abstract and conclusion now say so.
- The "discontinuity" and "attached to the limit itself" wording is withdrawn.
