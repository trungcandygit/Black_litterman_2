# Process summary — Paper C ("Closing at the limit"), academic-pipeline run of 4 October 2026

## Stages executed
| Stage | What was done | Independent agents | Outcome |
|---|---|---|---|
| 0–1 Research design | Brainstorm of 14 ideas (A: BL with K-means views; B: BL factorial; C: price limits + characteristic zoo), RQ brief, devil's-advocate Checkpoint 1 | DA agent (retrospective: ran after pre-specified results were known) | Paper C advanced because its estimated significance was highest (user rule) |
| 2 Write | R pipeline `paper2/R/40–47`, manuscript v1–v6 | none (single author-agent) | writer Phase 4a/4b and in-pair evaluator 6a/6b of the contract were NOT executed |
| 2.5 Integrity | Author self-check, then independent verifier rounds 1–3 and a narrow round 4 | 4 verifier agents | FAIL, FAIL, FAIL-narrow, then PASS; the three-round cap was exceeded without a recorded user decision (A8) |
| 3 Review | 5-seat panel (EIC, methodology, domain, perspective, devil's advocate), paper-blind Phase 1 then paper-visible Phase 2, conformance and layer-1 checks PASS, independent editorial synthesizer | 6 agents | MAJOR REVISION (D1–D6 warn; no block; no DA-critical) |
| 4 Revise | New analyses `R/48_revision.R` (C18–C25), manuscript v7, response letter | none | all roadmap items answered; partial items declared |
| 3' Re-review | One independent verification-mode reviewer; 16 numbers spot-checked and recomputed | 1 agent | MINOR REVISION (no new major issue) |
| 4.5 Final integrity | Independent verifier, mode 2; all 26 references, all citation contexts, ten headline numbers recomputed from raw data, 7-mode checklist | 1 agent | PASS; 3 MEDIUM defects fixed afterwards (522 label, lookup bug in the attention-proxy sentence, literature log) plus minor items |
| 5 Finalize | `final/Paper_C_Closing_at_the_limit.{docx,md,Rmd}` (journal-neutral, APA-like author-date) | none | PDF not produced (no LaTeX in the environment); no journal template |
| 6 Process record | this file | no collaboration-depth observer agent was run | |

## Protocol deviations the user should know about
1. Stage 2.5 ran past its three-round cap without an explicit, recorded user decision (decisions.md A8); the user's standing no-ask order was applied.
2. Writer Phase 4a/4b and in-pair evaluator contract (6a/6b) were not executed.
3. Devil's-advocate Checkpoint 1 was retrospective.
4. Revision-token-conservation and patch-discipline scripts were not run; the manuscript source was edited directly (A9).
5. All "independent" agents share one model family with the author-agent; no cross-model verifier was configured, so agreement between them is not independent verification.
6. The Stage 5 entry confirmation and the finalization-format choice were taken by default (journal-neutral, DOCX/MD) because the user asked not to be asked.
7. Paper A simulation size/power columns are incomplete (p-values NA from a coding error; not rerun); Paper A/B were not advanced.
8. No collaboration-depth observer agent was run at Stage 6.

## Honest AI self-reflection
- The old BL-K_IO headline (Sharpe 0.94) could not be reproduced on the current data (0.71 against 1/N 0.73); this was reported rather than tuned away.
- The first Paper C draft overclaimed an "independent replication", used a wrong Table 1 population and had an NA-propagation bug that truncated tables; independent verification found these, and they were corrected.
- The review round changed the paper's claim: the five-day tests are carried by day t+1 for ceilings; the mechanism is one hypothesis among three; "pre-specified" was downgraded to "log-specified".
- The main result is mostly already public (close-to-close ceiling effect), is not tradable for an outside buyer, comes from one exchange over about 25 months with a platform change inside the window, and the project selected it among several ideas (winner's curse).

## Items that need the human authors
External time stamp or deposit of the specification; exchange circulars for the HOSE rules; final DOI checks and full-text checks of Le (2012), Chen (1993) and Berkman and Lee (2002); ethics, funding, competing interests and author contributions; choice of target journal and template; decision on the Stage 2.5 cap deviation.
