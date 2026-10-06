# Stage 4.5 narrow re-verification, round 5b (MSJ version)

Agent: integrity_verification_agent (independent, read-only on manuscript and code). Date: 2026-10-06.
Scope: commit 0e3ed35 (`manuscript/msj/revisions_r5.py` LIT_EDITS, TABLE6_NOTE_NEW, INFERENCE_NEW, NEW_REFS; `build_msj.py`), `final/MSJ/Manuscript_MSJ.docx` and `final/MSJ/Supplementary_Material_S1.docx` (pandoc plain render plus `word/document.xml` for the abstract), full-text extracts of Kim & Rhee (1997) and Huang et al. (2001) (read at the coordinator's temporary path after removal from the repository) and Qi (2023) (`review/round5/fulltext_extracts/qi.txt`), `output/tables/C2_price_limit_events.csv`, `C16_subsamples_nasafe.csv`.

## Verdict: FAIL (one new inconsistency, F5). F1–F4 are fixed. Every number checks out.

## 1. F1–F4 from round 5

| Item | Status | Evidence |
|---|---|---|
| F1 Le (2012) | FIXED | Body l.17 "Le (2012)", reference "Le, D. N. (2012) ... *Journal of Economic Development* (University of Economics Ho Chi Minh City), (214), 116–128" with the VJOL URL; S1 says "added Le (2012)". No "Le (2018)" in either docx. Re-addition logged in `process/decisions.md` (Round 5). |
| F2 p-value convention | FIXED | INFERENCE_NEW is word for word the prescribed text, plus the optional 683 / 125 figures (C21 rows 5–6). |
| F3 Liang and Hu | FIXED | Now "Liang and Hu (2025) forecast limit hits." There are no "records we could access" left in either docx. |
| F4 S1 | FIXED | The Farber et al. (2006) exception was added. The "Statements in this paper that no study reports..." sentence was deleted. S1 now says that the three full texts were read on October 6, 2026. |

## 2. Literature numbers against full texts

**Kim & Rhee (1997), J. Finance 52(2).** Sample: daily prices, TSE First Section, 1989–1992 (Section I). Hits are defined intraday (H_t ≥ C_{t−1} + LIMIT_t), not as closes. Table IV Panel A: continuation 0.65 (S_hit) vs 0.50 (S_0.90) for upward moves and 0.49 vs 0.32 for downward moves. The values are frequencies, with binomial z = 13.13 and 8.37. The Table 6 cell ("65% (upper) and 49% (lower) ... against 50% and 32% for stocks reaching 90% of the limit") is correct. The setting "Tokyo, 1989–1992; limit hits" is correct. The comparison column ("Same direction ... we measure its size, not its frequency") does not overstate the evidence: it says plainly that K&R report frequencies. Our near-limit contrast holds for both sides (C17: ceiling +2.66, floor −1.59). PASS.
- Minor precision point (optional): K&R count a "continuation" as a sign pair, a non-negative day-0 open-to-close return followed by an overnight return in the direction of the limit ([+,+] or [0,+]). "Overnight continuation" is their own framing ("the immediate following overnight returns"), so it is acceptable. Panel B (stocks that closed at their high or low) gives 0.70 vs 0.50 and 0.59 vs 0.45. That sample is closer to our limit closes and could be added.

**Huang, Fu & Ke (2001), IREF 10, 263–288.** Sample: TSE (Taiwan), 1990–1996, 7% limit throughout (Section 5.1, l.190, 300–302). The sample is closing limit moves. Opening and closing prices are set by call auction. Abnormal returns come from a market model estimated on days −140 to −16 (Eq. 1–4).
- Table 4, Panel A (1-day up-limit), "All" row: AR1,co = +1.18% (t 45.37), AR1,oc = −0.77% (t 25.66). Section 6.2 reports a ratio of −0.65 to −0.79 and says that "around two thirds of the overnight abnormal returns is offset." Signs: the text calls the overnight return a continuation and the trading-time return a reversal, so +1.18 and −0.77 are right. Panel D (1-day down-limit): −2.17% and +1.24% (34–57% offset). Section 6.3 and Table 5 (near-limit, r0 > 5%, not at the limit): +0.23% and −0.72%. Every value and sign in Table 6 matches.
- Introduction sentence ("one-day up-limit closes gained 1.18% overnight and gave back 0.77% in the next session"): the values, signs and sample are correct, and "also had a 7% band" is correct. The sentence leaves out "abnormal". Table 10 shows that the raw overnight return is 1.23% and the market-adjusted return is 1.17%, so the wording does not mislead. Optional: "gained 1.18% overnight in abnormal terms".
- Discussion ("reverses ... about two thirds"): matches the ratio for 1-day moves, 0.77/1.18 = 0.65, and the authors' own phrase "around two thirds". PASS.
- Setting "Taiwan, 1990–1996; 7% band": correct.
- DOI: the PII printed on the article (huang.txt l.47) is "S 1 0 5 9 - 0 5 6 0 ( 0 0 ) 0 0 0 8 2 - 4", which corresponds to 10.1016/S1059-0560(00)00082-4. The reference "IREF 10(3), 263–288" matches the running head. PASS.

**Qi (2023), PLOS ONE 18(6), e0287548.** The event windows run from February 1 to July 31, 2020 (10% band, closes at the limit) and from October 1, 2020 to March 31, 2021 (closes beyond the 10% threshold). "ChiNext, 2020–2021" is therefore correct. The model is a market model with a value-weighted ChiNext index, estimated on days −120 to −30. AR is the daily close-to-close return, not an overnight return. Table 2, day 1, before the reform: up +0.0024 (N = 1537, significantly > 0), down −0.0337 (N = 1042, significantly < 0). The text (l.407, l.435) confirms +0.24% and −3.37%. The cell reads "Day-1 abnormal return +0.24% after upper-limit closes and −3.37% after lower-limit closes under the 10% band". It does not say "overnight", so it is correct.
- "Opposite asymmetry": in Qi the lower-limit day-1 effect is larger in absolute value (3.37 vs 0.24). Ours is larger at the ceiling (1.66 vs |−0.71|). Both are close-to-close abnormal returns on day d+1: Eq. (4) of our paper is market-adjusted and Qi's is from a market model. The claim is accurate and not overstated. PASS.

## 3. Our numbers (inline R)

| Cell / sentence | Rendered | Source | OK |
|---|---|---|---|
| Huang row: ceiling gap | 2.24% | C16 "Ceiling all" gap_mkt 2.24352 | yes |
| Reversal share (Table 6, Discussion, Intro contribution) | 24% | 100 × 0.53544 / 2.24352 = 23.87 | yes |
| Qi row: day-d+1 ceiling | 1.66% | C2 ceiling t+1 mean_ar_pct 1.66022 | yes |
| Qi row: day-d+1 floor | −0.71% | C2 floor t+1 −0.71297 | yes |

All four come from inline R expressions in the Rmd (`c16(...)`, `ev(...)`), not from typed text.

## 4. Claim strength / consistency

- **F5 (FAIL, new inconsistency).** Introduction, contributions paragraph: "First, we measure the overnight gap and the intraday return after limit closes, a pattern that Huang et al. (2001) **describe qualitatively** for Taiwan, ...". This is now false. Huang et al. report market-model magnitudes (+1.18% and −0.77%), and the manuscript itself cites those magnitudes four paragraphs earlier, in Table 6 and in the Discussion.
- Section 1.1, "Classic evidence": "Huang et al. (2001) reported for Taiwan that the overnight overreaction after limit hits reverses the following day". This matches the full text (overnight continuation, then reversal in the next trading period). Acceptable. It now partly repeats the Introduction sentence; trimming it is optional.
- Table 6 note ("Entries for Kim and Rhee (1997), Huang et al. (2001), and Qi (2023) report results from the full texts; the other entries summarize each study's abstract") is accurate.

## 5. Rendering (PASS)

`word/document.xml` of both docx files contains no "[[", no "<U+", no unevaluated `` `r ``, no literal "−" and no EQNUM. The only "2018)" matches are the Aboody et al. and Tov et al. references, which are legitimate. Minus signs in Table 6 render as U+2212 "−". The abstract is in the text box and is unchanged from round 5 (2.2%, 24%, 2.7 pp, 0.7%), with "lower-powered" restored.

## 6. Process record (minor, not a FAIL item)

`process/decisions.md` (Round 5) says that the text extracts are "kept in `paper2/review/round5/fulltext_extracts/`". The Kim and Huang extracts have since been removed from the repository for copyright reasons, so the entry should say: "extracts of Kim & Rhee and Huang et al. not retained in the repository (copyright); Qi (2023) is open access (CC BY) and its extract is kept."

## Exact fixes

**F5 (required).** Edit the Introduction contributions paragraph through `revisions_r5.py` LIT_EDITS or the Rmd source. Replace
"a pattern that Huang et al. (2001) describe qualitatively for Taiwan, and show"
with
"a split that Huang et al. (2001) applied to Taiwan, and show"
(or "a pattern that Huang et al. (2001) documented for Taiwan with market-model abnormal returns, and show").

**Optional.**
- Introduction: "gained 1.18% overnight" → "gained 1.18% overnight in abnormal terms".
- Table 6, Kim and Rhee cell: add the Panel B values for stocks that closed at their high or low (70% vs 50% upper; 59% vs 45% lower).
- `process/decisions.md`: correct the note on where the extracts are kept (Section 6).

Re-verification needed after F5: a one-sentence text check only. No numbers are affected.

## Closure of F5 (author note, 2026-10-06)
F5 applied with the verifier's prescribed wording ("a split that Huang et al. (2001) applied to Taiwan"); the rendered docx contains it and no "qualitatively" remains. Optional item applied: "in abnormal terms" after Huang's 1.18%. Docx schema validation PASSED; word count 7,486 (limit 7,500). This closure is a text check of the verifier's own replacement string, not a fresh verification.
