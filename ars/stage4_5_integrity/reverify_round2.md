# Stage 4.5 Final Integrity Check: Re-verification after Integrity-Correction Round 2

Agent: `integrity_verification_agent` (Mode 2, final-check). This pass re-verifies the round-2 corrections, following the agent's "Correction Process on FAIL", step 3. It also runs a cumulative check against every earlier Stage 4.5 finding. I did not write the corrections, and I treated each one as unverified until checked.
Date: 2026-09-24. The manuscript was not edited.

## Skill load record

I read each file with the Read tool before any checking began. ARS root: `/tmp/claude-0/-home-user-B-i-FTSE2/88a51032-601f-5b56-b6d6-c6001a62ef1c/scratchpad/academic-research-skills`, v3.22.1.

| File | Lines read | First heading |
|---|---|---|
| academic-pipeline/SKILL.md | 1–757 (all) | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| academic-pipeline/agents/integrity_verification_agent.md | 1–887 (all; two reads, 1–730 and 731–887) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| academic-pipeline/references/claim_verification_protocol.md | §E6, lines 122–205 (E6 and E6 structured findings / disposition) | `## E6: Claim-Strength Drift (#569 — non-verdict, checkpoint-closing, revision rounds)` |
| shared/references/claim_strength_ladder.md | 1–93 (all) | `# Claim-Strength Ladder` |
| academic-pipeline/references/plagiarism_detection_protocol.md | 1–239 (all) | `# Plagiarism Detection Protocol — Phase D Originality Verification Protocol` |

Rules applied from these files:
- **Verdict Criteria:**
  - PASS requires zero SERIOUS, zero MEDIUM, zero MAJOR_DISTORTION and zero UNVERIFIABLE.
  - PASS WITH NOTES allows only MINOR, MINOR_DISTORTION or UNVERIFIABLE_ACCESS items.
  - Anything else is FAIL.
- **Gray-Zone Prevention Rule:** every reference gets an explicit VERIFIED, NOT_FOUND or MISMATCH verdict before its Phase B check. NOT_FOUND requires three query variants.
- **A2 severity map:** year, DOI or journal errors are SERIOUS. Title imprecision is MEDIUM. Formatting is MINOR.
- **Phase D:** in Mode 2, revised sentences are checked at 100%. One or two CLOSE_MATCH findings are MODERATE, which counts as FAIL.
- **E6:** runs on every claim-bearing op. A rung move or dropped qualifier that no roadmap item authorized becomes an `ADV-E6-<n>` row. Each row needs `restore`, `authorize_with_reason` or `pause`, and no row may be left open.

## Inputs and bindings

| Artifact | SHA-256 |
|---|---|
| correction_round2/manuscript_v5.md (pre, anchored) | b66cf82fca29aaa4086cf8bb9bd876878a3c921b088314f59cc9870e9e092e28 |
| correction_round2/manuscript_v6.md (post, anchored) | a65557fc42de561d269b6d4fd0fb3c7156709a9cbb24bb621623478bb31e863a |
| correction_round2/manuscript_v6.clean.md (post, audited) | 97c9bac6c5815d82d08295b1bcdb972fbeacbfdb95fc615d1425085664449efd |
| correction_round2/integrity_patch_round2.json (9 ops) | 9dfc92b42ca471f292fb07a18246f68532a0918d193d7a3065f6629f487d84d4 |
| correction_round2/integrity_correction_list_round2.json (6 issues) | 0246f9e0675766b3296760c84357c1f30283b42afea9dfc6c88808c82ccd6dbc |
| correction_round2/token_conservation_round2.json | e046501e72ebeb3b7b5522b51bc87abaa0981feef99fc13456947b1bd6913539 |
| reverify_round1.md (prior report) | f2985041fdc266c4234047e7a5382f442edb70652ddda0b63e8c2146a5d39b36 |
| e6_dispositions.md | e91753d4db0588f4a3da745b7d814da1174476f8742c567745301f84de64a407 |

### Mechanical checks (scripted, on the files above)

- The patch's `base_draft_hash` (b66cf82fca29) and the issue-list hash both match the files. The apply report binds the same patch digest.
- All 8 `new_text` strings appear verbatim in v6.clean. The ninth op is a deletion.
- v6.clean equals v6.md with the block anchors removed (75,178 characters each).
- Scope of change:
  - Only the 9 targeted blocks changed; the other 187 of 195 blocks are byte-identical.
  - B0195 (the old GEIS entry) was removed.
  - B0196 (the new n.d. entry) was inserted after B0167.
  - There are no other additions or deletions.
- Every op's block and operation lie inside the `proposed_targets` of the IL ID it claims, and inside the author's `authorized_targets` (integrity_author_input_round2.json).
- Token conservation shows 6 ADV-REV rows. Each numeric or citation delta belongs to the IL ID its op claims:
  - ADV-REV-1, -2, -4 and -6 are the GEIS 2025 → n.d. swap (IL-MEDIUM-1).
  - ADV-REV-3 changes Burnham from a parenthetical to a narrative citation (IL-MEDIUM-2).
  - ADV-REV-5 adds "Version 1.2" and "(2026, April)" to the FAQ entry (IL-MINOR-2).
  - No delta is unclaimed.

## Verdict: **PASS WITH NOTES**

- **Round-2 issues:** all 6 are RESOLVED (2 MEDIUM, 4 MINOR). None is PARTIAL or NOT_RESOLVED.
- **New issues from the round-2 ops:**
  - 0 SERIOUS, 0 MEDIUM, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE.
  - One MINOR formatting note (N2-1).
- **Cumulative check:**
  - Every round-1 fix still holds in v6, and I found no regression.
  - No SERIOUS or MEDIUM finding remains open in phaseAB_group1-3.md, phaseD_originality.md or reverify_round1.md.
  - Two earlier group-level findings were never put on a correction list: group 1's provisional IL-SERIOUS-1 (Biktimirov & Afego volume, article number and DOI) and group 2's IL-MEDIUM-7 (table membership). This pass closed both with evidence (§7).
- **E6:**
  - Two moves in round 2 are authorized and closed (ops 2 and 3).
  - **No STRENGTH-DRIFTED row (ADV-E6-R2-*) was detected by the recorded semantic review.**
  - Every earlier E6 row has a recorded disposition in e6_dispositions.md.
- **What remains are notes only:** MINOR items, MINOR_DISTORTION items carried from the fresh pass, and documented access limits. None of them blocks under the Verdict Criteria.
- **Stage 4.5 status:** the checkpoint may advance to the MANDATORY Stage 5 entry checkpoint. Correction rounds used: 2 of 3.

## 1. Round-2 issue table

| IL ID (round-2 list) | Op / block | Verdict | Evidence / reason |
|---|---|---|---|
| IL-MEDIUM-1 (was N-1, GEIS version) | ops 0, 1, 6, 8 / B0011, B0018, +B0196, −B0195 | **RESOLVED** | The dated "(2025) … (v13.4)" entry is deleted. The new entry reads "FTSE Russell. (n.d.). *FTSE Global Equity Index Series ground rules*. Retrieved 24 September 2026, from [always-current lseg URL]". This entry no longer names a version that the URL did not serve on the access date. APA 7 treats a continuously updated document as n.d. with a retrieval date. Both in-text citations now read "(FTSE Russell, n.d.)". The document exists (Phase A, A2-1). The rule it is cited for is supported (Phase B, B2-4). The n.d. entry sits before the 2018 and 2026 entries, as APA 7 requires (§2). Retrieval-date format: MINOR N2-1. |
| IL-MEDIUM-2 (was N-2, Burnham CLOSE_MATCH) | op 4 / B0024 | **RESOLVED** | The new sentence shares at most one consecutive word with the abstract ("prices"). The shared content words are only "index", "moves", "prices" and "year". Phase D grade: PARAPHRASE (§4). Phase B: SUPPORTED (B2-1). |
| IL-MINOR-1 (Shleifer) | op 2 / B0021 | **RESOLVED** | "excess returns that persist for at least ten days after inclusion". The abstract says "This return does not disappear for at least ten days after the inclusion." The permanence reading is gone (B2-2). |
| IL-MINOR-2 (FAQ title) | op 7 / B0169 | **RESOLVED** | The title now matches the PDF title in sentence case, and the entry adds "(2026, April)" and "(Version 1.2)". v1.2 is the latest indexed version, effective 20 April 2026. A search for v1.3 found nothing (A2-2). |
| IL-MINOR-3 (CAR test wording) | op 5 / B0044 | **RESOLVED** | "divides the portfolio CAR by the product of two terms, the standard deviation … and the square root of the number of days in the event window". This can only be read as CAR/(σ·√L). It matches code/analysis_revision2.R line 67 (`t_portfolio = sum(ar) / (s_est * sqrt(L))`) and the Table 4 note ("Portfolio t = CAR / (σ × √L)"). The independence assumption is kept. |
| IL-MINOR-4 (Gregoriou & Nguyen) | op 3 / B0022 | **RESOLVED** | "the liquidity lost after FTSE 100 deletions has no significant effect on investment". The source finds "no effect of liquidity on future investments in a sample of U.K. firms deleted from the FTSE100 index" (B2-3). |

Summary: 6 RESOLVED, 0 PARTIAL, 0 NOT_RESOLVED.

## 2. Phase A: changed references (audit trail)

A0 (Semantic Scholar / Crossref) is API_UNAVAILABLE. `curl api.crossref.org` returned CONNECT 403, and WebFetch to lseg.com, research.ftserussell.com, sciencedirect.com and theinvestor.vn was egress-blocked. All checks therefore used WebSearch.

| ID | Reference (v6) | Queries (≥3) | Top result URL(s) | Fields confirmed | Verdict |
|---|---|---|---|---|---|
| A2-1 | FTSE Russell. (n.d.). *FTSE Global Equity Index Series ground rules*. Retrieved 24 September 2026, from lseg.com/…/ground-rules/ftse-global-equity-index-series-ground-rules.pdf | Q1 `"FTSE Global Equity Index Series" ground rules lseg.com pdf`; Q2 `"FTSE Global Equity Index Series" "Ground Rules" 2026 version v14`; Q3 `FTSE GEIS ground rules September review liquidity "last business day of June"`; Q4 `… "data cut-off" September review June semi-annual review` | https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf (exact URL, title "ftse global equity index series ground rules"); research.ftserussell.com ground-rule update notices id=2618101 and 2611724; …/ftse-global-equity-index-series-history-of-ground-rule-updates.pdf | The publisher is FTSE Russell. The title matches the document at the cited URL exactly. The URL is live in the index. Versions range from v13.4 (March 2025) to v13.8 (March 2026 review) and later. This confirms the document is continuously revised, so an n.d. entry with a retrieval date is correct. | **VERIFIED** (A2 clean) |
| A2-2 | FTSE Russell. (2026, April). *Reclassification of Vietnam from frontier to secondary emerging market status: FAQ* (Version 1.2). lseg.com/…/policy-documents/ftse-faq-document-vietnam-reclassification.pdf Accessed 24 September 2026. | Q1 `"Reclassification of Vietnam from Frontier to Secondary Emerging Market Status" FAQ`; Q2 `FTSE Russell Vietnam reclassification FAQ "v1.2" April 2026`; Q3 `FTSE Vietnam reclassification FAQ updated "v1.3" OR "version 1.3"` | research.ftserussell.com notice id=2617682 ("Reclassification of Vietnam from Frontier to Secondary Emerging…"); notice id=2619334 ("An updated copy of the FAQ (v 1.2) is now available", effective from the open on 20 April 2026); the PDF at the cited URL | The title matches the PDF title in sentence case. v1.2 dates to April 2026. Other versions indexed: v1.0 (November 2025) and v1.1 (April 2026). No v1.3 is indexed, so v1.2 is the latest version and matches the 24 September 2026 access date. | **VERIFIED** (A2 clean) |

**APA 7 ordering of the n.d. entry:**
- APA 7 orders same-author references by date, with n.d. entries first, then dated entries in chronological order, then in-press entries.
- v6 order: FTSE Russell (n.d.) → (2018, September 26) → (2026, April). This is **correct**.
- The in-text form "(FTSE Russell, n.d.)" is the APA 7 form. It is unambiguous because only one n.d. entry exists for the author.

**Other references touched by ops.** The entries for Burnham et al. 2018, Shleifer 1986, Gregoriou & Nguyen 2010 and Brown & Warner 1985 are byte-identical to v5 and were VERIFIED at Stage 4.5 and in round 1. I re-confirmed the key fields in passing:
- Burnham et al.: FAJ 74(1), 77–87, per tandfonline, NBER w23557 and RePEc v74y2018i1p77-87.
- Shleifer: JF 41(3), 579–590, per Wiley.
- Gregoriou & Nguyen: ScienceDirect PII S1042443110000089.
- Brown & Warner: JFE 14(1), 3–31, per RePEc and ScienceDirect.

## 3. Phase B: every changed citation context

| # | Block | Citation | New context | Source text relied on (session-held snippet) | Verdict |
|---|---|---|---|---|---|
| B2-1 | B0024 | Burnham et al. (2018) | "when MSCI moves a country to a different index family, the country's stock prices move sharply in the direction implied by the new benchmark before the change is implemented and give back most of that move in the following year" | Abstract: "On average, reclassified markets' prices substantially overshoot between the announcement and effective dates—prices fall when a market moves from an index with more benchmarked ownership to one with less, such as from Emerging to Frontier, and vice versa—but largely revert within a year." (NBER w23557; tandfonline) | **SUPPORTED** in each part: sharp move ≈ substantial overshoot; direction implied by the new benchmark ≈ "prices fall … and vice versa"; before implementation ≈ between announcement and effective date; give back most within the following year ≈ largely revert within a year. The source's "on average" is absent, but it was absent from the v5 wording too. This is not a new omission and does not change meaning for a country-level summary. |
| B2-2 | B0021 | Shleifer (1986) | "interprets excess returns that persist for at least ten days after inclusion as evidence that demand curves for stocks slope down" | "…a significant positive abnormal return at the announcement of the inclusion. This return does not disappear for at least ten days after the inclusion. … consistent with the hypothesis that demand curves for stocks slope down." (Wiley abstract) | **SUPPORTED** (the MINOR_DISTORTION from round 1 is cleared) |
| B2-3 | B0022 | Gregoriou & Nguyen (2010) | "find that the liquidity lost after FTSE 100 deletions has no significant effect on investment" | "find no effect of liquidity on future investments in a sample of U.K. firms deleted from the FTSE100 index" (citing-literature summary; ScienceDirect/ResearchGate record) | **SUPPORTED** (round-1 precision note cleared) |
| B2-4 | B0011, B0018 | FTSE Russell (n.d.) GEIS ground rules | The September review's liquidity screen uses data up to the last business day of June (B0011 adds "2026") | "For the September review, liquidity will be tested from the first business day of July of the previous year to the last business day of June"; "For the September review, the data cut-off is the last business day in June" (GEIS ground rules / FAQ and Guide to Calculation Methods for GEIS Liquidity, indexed August 2026). 30 June 2026 was a Tuesday. | **SUPPORTED**. The ground rules state the June data cut-off. The Guide to Calculation Methods for GEIS Liquidity, a companion to the ground rules, spells out the liquidity period. Citing the ground rules is adequate. |
| B2-5 | B0044 | Brown & Warner (1985) | "We therefore test cumulative abnormal returns (CARs) on the equal-weighted portfolio of the group, which addresses cross-sectional dependence (Brown & Warner, 1985): the test statistic divides … which assumes independent daily abnormal returns." | Brown & Warner discuss dependence adjustment through the time-series SD of portfolio abnormal returns in the estimation period (Stage 4.5 CDA snippet; RePEc/Monash records). | **SUPPORTED**. The attribution is unchanged from round 1 and covers the portfolio approach to dependence. The √L scaling is marked as the paper's assumption ("which assumes independent daily abnormal returns"). The op changed only the arithmetic wording, not the attribution. |
| B2-6 | B0018 (unchanged parts re-read because the block was replaced) | Viet Nam News (2025); The Investor (2026a, 2026b); FTSE Russell (2026); VIR (2026) | November 2025 list; 31 Dec 2024 / 31 Dec 2025 data dates; 27 constituents effective after the close of 18 Sep 2026; investability weight | Byte-identical to v5 apart from the GEIS citation, and all SUPPORTED in round 1 (B-13, B-14). The 27 constituents are re-confirmed below (§7). | **SUPPORTED** |

## 4. Phase D: new text fragments (100% of round-2 new or rewritten sentences)

| Fragment (quoted query) | Top results | Closest source | Longest shared run | Grade |
|---|---|---|---|---|
| "stock prices move sharply in the direction implied by the new benchmark" | arXiv 2606.07811, Wikipedia "Dow theory", NBER digest; no textual match | Burnham et al. abstract (compared by script) | 1 word ("prices") | **PARAPHRASE** (cited) |
| "give back most of that move in the following year" MSCI reclassification | RePEc NBER w23557 listing, Acadian and MSCI pages; the phrase appears in none of them | Burnham et al. abstract ("largely revert within a year") | 0 content words in sequence | **PARAPHRASE** (cited) |
| "excess returns that persist for at least ten days after inclusion" | arXiv 2201.09319, S&P DJI and McKinsey pages; no match | Shleifer abstract ("does not disappear for at least ten days after the inclusion") | 5 words ("for at least ten days"), which is a factual horizon | **PARAPHRASE** (cited) |
| "the liquidity lost after FTSE 100 deletions has no significant effect on investment" | ScienceDirect S1042443110000089, ResearchGate records; no textual match | G&N summary ("no effect of liquidity on future investments … deleted from the FTSE100") | ≤3 words | **PARAPHRASE** (cited) |
| "divides the portfolio CAR by the product of two terms" | USPTO patents, AnalystPrep, Wikipedia "Event study"; no match | none | none | **ORIGINAL** |
| "under FTSE's ground rules the September review screens liquidity on data up to the last business day of June" | FTSE UK ground rules, GEIS v8.8 (biva.mx), GEIS FAQ 2026; the words themselves are not matched | GEIS rule text ("liquidity will be tested … to the last business day of June") | ≤7 words ("to the last business day of June", a defined term) | **COMMON_KNOWLEDGE / PARAPHRASE** (cited). This text is carried over unchanged from v5 except for the citation. |

Result: 0 CLOSE_MATCH, 0 VERBATIM. No Phase D issue.

## 5. A3 ghost-citation check (manuscript_v6.clean.md, whole manuscript)

- **Reference list:** 33 entries, the same count as v5. GEIS (2025) is replaced by GEIS (n.d.).
- **Method:** each entry's first author and year was regex-matched against the body, and every author-year citation found in the body was matched back to the list.
- **Match counts:**
  - Every entry is cited at least once.
  - "FTSE Russell, n.d." is cited 2 times (B0011, B0018).
  - "FTSE Russell, 2018" is cited 2 times and "FTSE Russell, 2026" 5 times.
  - Burnham is cited 2 times (B0009 and B0024, narrative).
  - Shleifer and Gregoriou & Nguyen are cited in their blocks.
- **Leftover "FTSE Russell, 2025":** none (0 occurrences). "v13" appears 0 times.
- **Orphan references: 0. Dangling citations: 0. A3: PASS.**

## 6. E6 on the 9 round-2 ops (claim-strength drift)

Every op carries `claim_strength_changes: []`. For each claim-bearing op I compared the old text (v5) and the new text against the ladder and checked for dropped hedges, nulls and caveats.

| Op / block | Old → new | Ladder assessment | Authorized by | Status |
|---|---|---|---|---|
| 0 / B0011 | Citation (2025) → (n.d.) | No claim text changed | — | no move |
| 1 / B0018 | Citation (2025) → (n.d.) | No claim text changed | — | no move |
| 2 / B0021 | Shleifer: "excess returns that do not reverse after inclusion" → "excess returns that persist for at least ten days after inclusion" | Down: a horizon limit is added, and the implied permanence is removed | IL-MINOR-1 (its text names this exact change) | **authorized, closed** |
| 3 / B0022 | G&N: "no significant effect of FTSE 100 deletions on investment" → "the liquidity lost after FTSE 100 deletions has no significant effect on investment" | The null result is kept and moved to the correct variable. The scope narrows, which counts as a move. | IL-MINOR-4 (its text names this exact change) | **authorized, closed** |
| 4 / B0024 | Burnham: "prices … overshoot … and largely revert within a year" → "show that … prices move sharply in the direction implied … and give back most of that move in the following year" | Same rung. "Overshoot/largely revert" becomes "move sharply/give back most", a description swap. "show that" is a reporting verb for a stated finding of the cited study. Both versions state the finding without a hedge, so the assertion strength is the same. The country-level scope is kept ("the country's stock prices"). No hedge was dropped: v5 had no "on average". | IL-MEDIUM-2 (rewording) | no move |
| 5 / B0044 | CAR test wording | Arithmetic clarification. The limitation "which assumes independent daily abnormal returns" is kept. | IL-MINOR-3 | no move |
| 6, 7, 8 / references | Reference entries | Not claim-bearing | — | n/a |

**ADV-E6-R2 rows (STRENGTH-DRIFTED): none detected by the recorded semantic review.**
- This finding is model-mediated and is not a deterministic no-drift certificate.
- With zero rows, no round-2 disposition is required.

**Earlier rows:**
- e6_dispositions.md records an explicit disposition for every earlier row:
  - `restore`: ADV-E6-1, -3, -4, -5 and -6. Each restore was carried out and verified in round 1.
  - `authorize_with_reason`, each with a non-blank reason: ADV-E6-2, ADV-E6-R1-1 and ADV-E6-R1-2.
- Derived action: `authorized_to_continue`.
- **Contract boundary:** e6_dispositions.md records honestly that `claim-strength-drift-findings/1.0` is `skipped_no_revision_evidence`, because the Revision-Evidence Bundle cannot be built across the v2→v3 re-emission. The semantic review stands in as the supplementary review. I note this and do not change it; it is outside the PASS/FAIL count.

## 7. Cumulative check (all Stage 4.5 findings to date)

### 7a. Round-1 fixes still hold in v6 (no regression)

- **Fixes in untouched blocks.** 26 round-1 ops touched blocks that round 2 left alone, and their `new_text` still appears verbatim in v6.clean. These cover IL-SERIOUS-2 and IL-MEDIUM-1 to 5, 9 to 11, 13 (B0009), 14 and 15, plus IL-MINOR-1, 3 and 6 to 10.
- **Fixes in blocks round 2 re-touched.** Round-1 ops 1, 3, 4, 5, 6, 8 and 29 target blocks that round 2 replaced. I re-read each replacement to confirm the round-1 fix survived:
  - B0011: the June cut-off is still cited to the GEIS rules, not the FAQ or VIR (IL-MEDIUM-6).
  - B0018 still has:
    - "(10% of 49%)" with no FTSE attribution (IL-MEDIUM-8);
    - Viet Nam News (2025) and The Investor (2026a) (IL-MINOR-4);
    - "reflects its free float and foreign-ownership limits" (IL-MINOR-5).
  - B0021: Harris & Gurel has no "on the effective date", and Hegde & McDermott still reads "mainly to lower direct trading costs" (IL-MINOR-2).
  - B0022: the "mirror pattern" wording is gone (IL-SERIOUS-1).
  - B0024: the Biktimirov paraphrase is kept (IL-MEDIUM-12), and Burnham is still cited (IL-MEDIUM-13).
  - B0044: the √L scaling is still stated as the paper's own assumption (IL-MEDIUM-10).
  - B0169: no "Version 1.3, August" (IL-MEDIUM-7).
- **Op 28 (the GEIS 2025 entry)** was deliberately replaced by the n.d. entry.
- **Residue strings:**
  - "for years", "FTSE's own illustration", "mirror pattern", "force passive", "on the effective date", "do not reverse", "v13.4", "Version 1.3" and "supports H4" each occur 0 times.
  - "limits causal readings", "suggests that investors responded", "significant under three of four", "up to 2.9 times", "persistently" and "only the portfolio" are present.
  - "0.056" and "6.3%" do occur, but only as unrelated table cells in untouched blocks:
    - Table 6: a standard error of 0.056 on the Constituent × Confirmation row;
    - Table 4: 6.3% CARs in other rows and panels.
  - Neither is the corrected pre-trend p-value or the corrected CAR range.

### 7b. Earlier findings: nothing SERIOUS or MEDIUM remains open

| Source | SERIOUS / MEDIUM finding | Where it went | Status now |
|---|---|---|---|
| phaseAB_group1 IL-MEDIUM-1, -2 (B&W √L UNVERIFIABLE_ACCESS) | → round-1 IL-MEDIUM-10 | RESOLVED (reverify_round1), holds in v6 (B0044, B0082) | closed |
| phaseAB_group1 **IL-SERIOUS-1** (Biktimirov & Afego vol. 110 / art. 105562 / DOI unconfirmed; marked "provisional, not a detected error") | Not on the round-1 list. The failure-mode checklist counts all references VERIFIED. | **Closed in this pass** (see below) | closed: VERIFIED |
| phaseAB_group2 IL-SERIOUS-1, -2 (G&N, H&M) | → round-1 IL-SERIOUS-1, -2 | RESOLVED; G&N refined in round 2 | closed |
| phaseAB_group2 IL-MEDIUM-1 (FAQ version) | → round-1 IL-MEDIUM-7, round-2 IL-MINOR-2 | RESOLVED | closed |
| phaseAB_group2 IL-MEDIUM-2, -3 (LSEG titles) | → round-1 IL-MEDIUM-9 | RESOLVED | closed |
| phaseAB_group2 IL-MEDIUM-4, -5, -6 (49% illustration, 30 June date) | → round-1 IL-MEDIUM-8, -6 | RESOLVED | closed |
| phaseAB_group2 **IL-MEDIUM-7** (Table A.2 ticker membership, UNVERIFIABLE_ACCESS) | Not on the round-1 list | **Closed in this pass** (see below) | closed: SUPPORTED |
| phaseAB_group3 IL-MEDIUM-1 (VIR cited for 30 June) | → round-1 IL-MEDIUM-6 | RESOLVED | closed |
| phaseD_originality IL-MEDIUM-1 (Biktimirov CLOSE_MATCH) | → round-1 IL-MEDIUM-12 | RESOLVED | closed |
| reverify_round1 N-1, N-2 (MEDIUM) | → round-2 IL-MEDIUM-1, -2 | RESOLVED (§1) | closed |
| reverify_round1 N-3, N-4, B-6, IL-MINOR-2 partial (MINOR) | → round-2 IL-MINOR-1 to 4 | RESOLVED (§1) | closed |

**Biktimirov & Afego (2026): A1/A2 audit trail for this pass**
- Queries:
  - Q1 `"10.1016/j.iref.2026.105562"`: no page carries the DOI string. Search engines index new Elsevier DOIs poorly.
  - Q2 `Biktimirov Afego "Is there an index effect in frontier markets" International Review of Economics and Finance volume 110 105562`: returned the RePEc IREF series listing. Title, authors, journal and study period (FTSE Frontier 50, 2008–2025) are confirmed.
  - Q3 `sciencedirect "Is there an index effect in frontier markets" Biktimirov 2026`: returned **https://www.sciencedirect.com/science/article/pii/S1059056026006751**. This is the publisher page. PII prefix S1059-0560 is the IREF ISSN, and "26" dates the article to 2026.
- DOI registry evidence: `ars/stage2_5_integrity/crossref_recheck.tsv` holds a raw Crossref API response for DOI 10.1016/j.iref.2026.105562 with status OK, first author Biktimirov, year 2026, International Review of Economics & Finance, volume 110, article number 105562 and the exact title.
- Why I rely on that file: it is a raw registry record, not an earlier verdict. Crossref was 403-blocked today, so I could not fetch it again.
- Contradictions: none. Every field matches the reference.
- **Verdict: VERIFIED.** The volume and article number rest on the recorded Crossref response. The open-access publisher page could not be fetched because of egress, which is noted as an access limit.

**Table A.2 membership (group 2, context 9).** Query: `FTSE Vietnam 27 stocks small cap VIX VND VRE VCK VPL …`. Sources: theinvestor.vn "Which Vietnamese stocks made it into the FTSE Global Equity Index Series?", news.laodong.vn and vietnam.vn "FTSE's official list: 27 key stocks revealed".
- The sources list 27 names:
  - large cap: VCB, VIC, VHM;
  - mid cap: BID, HPG, VPB;
  - small cap: FPT, GEX, HDB, HCM, MCH, MSN, NVL, SHB, STB, SSB, SSI, TCX, VNM, VCI, VJC, MSB, VRE, VPL, VIX, VND, VCK.
- These are exactly the 27 constituents in Table A.2: 15 from the preliminary list, 3 added in April, 6 in-sample non-list names and 3 later listings.
- The 28- and 32-name eligible lists were confirmed at Stage 4.5 (theinvestor.vn), including the April change of dropping PLX and adding BID, FPT, NVL, GEE and BSR.
- **Verdict: SUPPORTED.**

## 8. Issue list (fresh numbering for this report)

### SERIOUS
None.

### MEDIUM
None.

### MINOR (recommended; does not block)

| ID | # | Category | Location | Issue | Suggestion |
|---|---|---|---|---|---|
| IL-MINOR-1 (N2-1) | 1 | Citation format (B2) | References, FTSE Russell (n.d.) | "Retrieved 24 September 2026, from URL" uses a different date pattern from APA 7's "Retrieved September 24, 2026, from URL". Every other web entry instead ends "URL Accessed 24 September 2026." The list is therefore internally inconsistent. | Use one pattern throughout at Stage 5 format-convert. In APA 7, add a retrieval date only for the n.d. GEIS entry ("Retrieved September 24, 2026, from …") and drop "Accessed …" from entries with a fixed date. |

### Notes attached to PASS WITH NOTES (not issues)

- **Access limits.** lseg.com, research.ftserussell.com, sciencedirect.com, theinvestor.vn, doi.org and the Crossref, Semantic Scholar and OpenAlex APIs were blocked. The GEIS, FAQ and Burnham judgements rest on indexed snippets and abstracts, and all were consistent. The Biktimirov volume and article number rest on the Stage 2.5 raw Crossref record (§7b).
- **Carried MINOR notes from the fresh pass and round 1.**
  - Any MINOR_DISTORTION rows from phaseAB_group1-3 not covered by an IL-MINOR fix stay MINOR.
  - The round-1 cosmetic note on IL-MINOR-9 is unchanged: "EIB in the ITT group" does not mention that SHB, STB and VCB are also in the ITT group.
- **Burnham "on average".** The source qualifies the overshoot with "on average". Neither v5 nor v6 carries it. An author may add "on average" for extra precision, but it is not required: this is a country-level summary of a sample average.
- **E6 contract artifact.** It is `skipped_no_revision_evidence`, with semantic-review dispositions recorded in e6_dispositions.md (§6).
- **Phase D.** The check is heuristic and uses WebSearch; it is not Turnitin or iThenticate. It covered 100% of the round-2 new or rewritten sentences. A professional overlap check is recommended before submission.

## 9. Verification summary (round-2 scope plus cumulative closure)

| Category | Total | Passed | Issues |
|---|---|---|---|
| Round-2 IL items re-verified | 6 | 6 RESOLVED | 0 |
| Reference existence of changed entries (A1) | 2 (+1 cumulative: Biktimirov) | 3 VERIFIED | 0 NOT_FOUND / 0 MISMATCH |
| Bibliographic accuracy of changed entries (A2) | 2 | 2 | 1 MINOR format (N2-1) |
| Ghost citations (A3, whole manuscript) | 33 refs | PASS | 0 orphan / 0 dangling |
| Citation contexts changed by ops (B) | 6 | 6 SUPPORTED | 0 |
| Numbers changed by ops (C) | 0 numeric claim changes (token check: only reference years/version) | — | 0 |
| Originality of new or rewritten sentences (D1, 100%) | 6 fragments | 6 (ORIGINAL / PARAPHRASE / COMMON_KNOWLEDGE) | 0 CLOSE_MATCH / 0 VERBATIM |
| E6 drift (op-level) | 9 ops | 7 no move, 2 authorized and closed | 0 ADV-E6-R2 rows |
| Cumulative SERIOUS / MEDIUM still open (group1-3, D, round 1) | 17 findings traced (§7b) | 17 closed | 0 |

**Verdict: PASS WITH NOTES.**
- The counts are zero SERIOUS, zero MEDIUM, zero MAJOR_DISTORTION and zero UNVERIFIABLE.
- What remains is one MINOR format item, carried MINOR notes and documented access limits.
- Stage 4.5 has reached a terminal resolution. The pipeline may go to the **MANDATORY** Stage 5 entry checkpoint, which needs explicit user confirmation and the citation-style decision.
- #660, and then #672, run against the exact accepted bytes of manuscript_v6 (clean SHA-256 97c9bac6…449efd).

## Tool limitation note

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 100% of round-2 revised sentences, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

A0 APIs and the publisher, index and news hosts were egress-blocked, so Phase A and B relied on WebSearch result titles, URLs and snippets. E6 classification is semantic and model-mediated.
