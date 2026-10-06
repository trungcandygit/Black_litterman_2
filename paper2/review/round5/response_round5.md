# Response to the round-5 comments (MSJ version)

Skill basis: academic-paper revision mode; `intro_title_rhetoric_guide.md` (no universal negatives), `abstract_writing_guide.md`, `academic_writing_style.md`, `writing_quality_check.md`, `scripts/check_acronyms.py` (no findings). Changes are in `manuscript/msj/revisions_r5.py`, `build_msj.py`, `fill_template.py`.

## Literature
1. **Full texts of Huang et al. (2001), Kim & Rhee (1997), Qi (2023): DONE.** The authors supplied the PDFs. Table 6 now reports their results (Huang: +1.18% overnight and −0.77% in the next session after one-day up-limit closes, Taiwan 1990–1996, 7% band; Kim & Rhee: overnight continuation 65%/49% vs 50%/32% for stocks reaching 90% of the limit, Tokyo 1989–1992; Qi: day-1 abnormal return +0.24%/−3.37% after upper/lower limit closes, ChiNext 2020–2021). The Introduction and Discussion compare magnitudes: our ceiling gap (2.24%) is larger than Huang's, and the session reverses a smaller share (24% vs about two thirds). The Huang DOI (10.1016/S1059-0560(00)00082-4) was added from the article's PII.
2. **Wording that relied on abstracts removed.** "the records we could access had no magnitudes" and "Findings as reported in each source's abstract…" were removed. Table 6 now compares signs, timing, and mechanisms; its note reads "Main published finding of each study, compared with ours by sign, timing, and mechanism." Supplementary Material S1 still states that records and abstracts, not full texts, were read.
3. **Vietnamese studies added** (records verified by web search): Le (2012), *Journal of Economic Development* (UEH), No. 214, pp. 116–128, on narrower bands and stock price risk (GARCH); Farber, Nguyen & Vuong (2006), ULB working paper, on clusters and sequences of limit hits on the early HCMC market. S1 now reports this second search (October 6, 2026, including the VJOL index).
4. **Universal negatives removed.** "our search identified no peer-reviewed study…", "none controlled for multiple testing…", "None of the studies identified by our search reports…" were replaced by statements of what this study adds (Introduction: three open questions; Section 1.1: what the present study does relative to Huang et al., 2001).

## Presentation
5. **Abstract**: four key results (2.2% gap, 24% reversal, 2.7 points vs near-limit moves, 0.7% loss for a buyer at the open) plus sample size and band; 287 words (journal range 250–300).
6. **Dense sentences split**: floor and near-hit results (now three paragraphs), Table 3, Table 4, Table 5/placebo/difference-in-differences (now three paragraphs). One result per sentence where possible.
7. **Section 4.1 "(i)"**: the marker was swallowed by list parsing in the conversion; it is now escaped and appears.
8. **"740 of 2,111 remain without…"** rewritten: "excluding days on which the market fell by more than 2% removes 1,371 of the 2,111 floor events."
9. **H4 restated** as a directional prediction: if the gap already contains the blocked demand, the abnormal return from the next open to the fifth close is zero or negative; the negative estimate (−0.75%) is consistent with it.

## Methods
10. **Two p-value conventions explained** (Section 2.2, Inference): family p-values follow the analysis plan fixed before results (normal reference, no G/(G−1)); Table 1 uses the factor and a t reference as a conservative check; under the conservative settings the four event tests still survive Bonferroni in families of up to 683 tests, so no conclusion changes.
11. **Equations**: numbers moved out of the equation objects; each display equation sits in a borderless two-cell table (equation centred, number right). Symbols in running text are plain Unicode text, so they survive copying and display in Word, LibreOffice, and Google Docs. Verified by rendering to PDF.

Length after revision: about 7,490 words including abstract and references (limit 7,500).

Integrity: round 5 FAIL (F1–F4) → fixed; round 5b FAIL (F5 wording) → fixed with the verifier's prescribed text (see `integrity_round5.md`, `integrity_round5b.md`).
