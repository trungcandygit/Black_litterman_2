# Stage 2.5 Integrity Report — Paper C ("Closing at the limit")

Skill files applied: `academic-pipeline/references/integrity_review_protocol.md` (Stage 2.5, Phases A–E), `references/ai_research_failure_modes.md` (7-mode checklist), `shared/` anti-leakage protocol (session materials over memory). Executed by the same model that drafted the paper; the single-family correlated-error caveat applies (no cross-model verifier was configured, `ARS_CROSS_MODEL` unset).

## Phase A — References (100% of registered references)
20 references cited. Existence and bibliographic accuracy checked against records returned by web search (publisher, IDEAS/RePEc, EconPapers, NBER, SSRN, Semantic Scholar, ScienceDirect): see `04_literature_search_log.md`. Result: 20/20 VERIFIED. No ghost citations (every in-text citation appears in the list and conversely; checked by listing). The two non-journal items are labelled (GitHub repository, grey literature; SSRN working paper). DOIs are included only where the search results supplied them.

## Phase B — Citation context (spot-check, 100% of the 16 theory/empirical claims attributed to sources)
| Claim in manuscript | Source | Support found |
|---|---|---|
| Rationale for price limits in futures markets | Brennan (1986) | title/topic of the paper (theory of price limits in futures markets); wording kept generic |
| Advocates: limits reduce volatility and counter overreaction; critics: delay price discovery, volatility spillover, trading interference | Kim & Rhee (1997) | abstract text returned by search |
| Evidence supports all three critical hypotheses (Tokyo) | Kim & Rhee (1997) | abstract text |
| Serial correlation inversely related to limit range, implying a delaying effect (Taiwan) | Chen (1993) | abstract text |
| More frequent continuations after limit hits; trading interference (Korea) | Berkman & Lee (2002) | abstract text |
| Magnet effect toward the upper limit (Taiwan, high-frequency) | Cho et al. (2003) | abstract text |
| Positive overnight returns followed by intraday reversal, retail attention (U.S.) | Berkman et al. (2012) | abstract text |
| Overnight and intraday persistence differ; investor heterogeneity | Lou et al. (2019) | abstract text |
| Momentum/price limits, Vietnam 2000–2006 | Veeraraghavan et al. (2007) | SSRN abstract text |
| +1.69% next session after ceiling, −0.39% after 3–6.5% rise; 2016–2026 sample; not peer reviewed | tungtran0911 (2026) | README read via fetch, numbers quoted exactly |
| t > 3 hurdle | Harvey et al. (2016) | abstract text |
| BH FDR, Fama–MacBeth, Newey–West, two-way clustering, RD guide, MAX, Corwin–Schultz | respective papers | method/title level; used as method citations only |
Result: no mis-attributed claims found. One earlier phrase attributing a policy rationale to Brennan (1986) was corrected before this check (Kim & Rhee now carries the advocate/critic framing).

## Phase C — Statistical and data surfaces (100% of registered surfaces)
Every number in Tables 1–6, Figures 1–3 and the prose is produced by inline R from `output/tables/C1–C10`; a scan of the prose outside inline code found only design constants, literature numbers and rounded descriptors ("about +1.7%", "about two percentage points") consistent with the tables. Code verification tests (`process/05_verification_tests_C.txt`): look-ahead audit of the 22 characteristics (PASS, max difference 0 after replacing all later data by noise), independent recomputation of one Fama–MacBeth series (PASS to 1e-9), independent brute-force recomputation of the ceiling t+1 event mean and event count (PASS, identical to six decimals), accounting identity gap + intraday vs close-to-close (PASS, 0.05 pp compounding), event-count reconciliation (PASS), family-control reproducibility (PASS). Earlier infrastructure tests for the shared library (QP, BL posterior, ANOVA shares) are in `02_verification_tests.txt`.

## Phase D — Originality
No text copied from sources; the one directly overlapping precedent (tungtran0911, 2026) is acknowledged in the introduction and abstract and its numbers are quoted with attribution. No self-plagiarism: Paper C is distinct from Papers A and B.

## Phase E — Claim verification (risk-stratified: 100% of HIGH-IMPACT claims)
| # | Claim (headline) | Trace | Verdict |
|---|---|---|---|
| 1 | 0/22 characteristics and 4/4 limit tests survive FDR + hold-out | C3 table; test T6 | SUPPORTED |
| 2 | Ceiling: +1.66% next day, t 4.9 (3,187 events, 446 dates) | C2; independent recomputation T3 | SUPPORTED |
| 3 | Floor: −0.71%, t −5.3 | C2 | SUPPORTED |
| 4 | Ceiling effect entirely overnight gap (+2.2%), intraday −0.5% | C6, C4 | SUPPORTED |
| 5 | Discontinuity vs 5–6.5% moves: gap +2.67 pp (t 13.7); floor −1.58 pp (t −9.5) | C8 | SUPPORTED (association, not causal; wording says so) |
| 6 | Buying at next open loses 0.79% through day 5 (t −3.7) | C4 | SUPPORTED |
| 7 | Exact tick rule strengthens the estimates | C7 | SUPPORTED (about half the events; assumptions on tick sizes disclosed) |
| 8 | Robust across halves, crash exclusion, liquidity terciles, locked days | C4 | SUPPORTED, with disclosed exceptions (floor in lowest-liquidity tercile) |
| 9 | "Largest |t| among characteristics 1.55; none passes HLZ 3" | C1 | SUPPORTED |
| 10 | Pile-up of returns at 6.5–7.1% confirms a 7% limit | C9 | SUPPORTED as an inference from the data; exchange rules not independently verified (disclosed) |
Advisories (not issues): scope-conformance — sub-question 3 of the RQ brief concerned bank/broad BL portfolios (Paper B), whereas Paper C addresses the RQ of `03_brainstorm_round2.md`; the two are separate manuscripts. Novelty claims are bounded by the documented search strategy (`SUPPORTED_WITHIN_SEARCH`); no claim of being first for the close-to-close effect.

## AI Research Failure Mode Checklist (7 modes)
| Mode | Outcome | Basis |
|---|---|---|
| 1 Implementation bug passing self-review | RULED OUT (to the extent tests can) | independent recomputations and look-ahead audit pass; no suspiciously round values; CIs vary across conditions |
| 2 Hallucinated citation | RULED OUT | 20/20 verified in search results |
| 3 Hallucinated experimental result | RULED OUT | all numbers trace to saved R output; code and data in repository |
| 4 Shortcut reliance | FLAGGED (non-blocking at 2.5) | the main result could reflect a data artefact (e.g., unadjusted corporate actions near limit hits); mitigated by the exact tick rule, two clustering schemes, sub-samples; residual risk disclosed in Limitations (iv) |
| 5 Bug reframed as insight | RULED OUT | the "surprise" (gap vs intraday) is mirrored by an independent peer-reviewed signature (Berkman et al., 2012) and by the placebo bins; reproduced by two code paths |
| 6 Methodology fabrication | RULED OUT | Methods describe the scripts actually run; post hoc steps are labelled as such (Appendix A) |
| 7 Frame-lock | CHECKED | the original framing ("continuation after limit hits = momentum-like profit") was revised when the decomposition showed it was untradable; the manuscript now states that explicitly |

## Compliance (RAISE principles-only, warn-only)
AI-use disclosure present; data and code availability stated; human accountability stated; reference verification documented. No PRISMA-trAIce scope (not a systematic review).

## Verdict
**PASS** — zero blocking issues; advisories recorded. Per the user's standing no-ask order the pipeline proceeds. (A FAIL would not have been self-overridden.)
