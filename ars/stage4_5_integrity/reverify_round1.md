# Stage 4.5 Final Integrity Check: Re-verification after Integrity-Correction Round 1

Agent: `integrity_verification_agent` (Mode 2, final-check). This pass re-verifies the corrected items only, per the agent's "Correction Process on FAIL", step 3. I did not write the corrections and treated them as unverified.
Date: 2026-09-24. The manuscript was not edited.

## Skill load record

Each file was read in full with the Read tool before any checking began. ARS root: `…/scratchpad/academic-research-skills`, v3.22.1.

| File | First heading |
|---|---|
| academic-pipeline/SKILL.md | `# Academic Pipeline v3.22.1 — Full Academic Research Workflow Orchestrator` |
| academic-pipeline/agents/integrity_verification_agent.md (lines 1–887) | `# Integrity Verification Agent — Academic Integrity Verification Gatekeeper` |
| academic-pipeline/references/claim_verification_protocol.md | `# Claim Verification Protocol (Phase E)` |
| shared/references/claim_strength_ladder.md | `# Claim-Strength Ladder` |

## Inputs and bindings

| Artifact | SHA-256 |
|---|---|
| manuscript_v4.md (pre) | a4ceddce5c7a0f7f5964a8719753c252adc2577b6f543581501e17d25812a6c5 |
| manuscript_v5.md (anchored post) | b66cf82fca29aaa4086cf8bb9bd876878a3c921b088314f59cc9870e9e092e28 |
| manuscript_v5.clean.md (post, audited) | a1783491551fbec22f4f2f745cf4ba045e1ce1295aacf779d61a239fbadde377 |
| integrity_patch_round1.json (33 ops) | 0b85bda1dd343019e95d1617a71d1048079738b822b571a0feb4d32094ca6385 |
| integrity_correction_list_round1.json (27 issues) | 8362668cfb5196732a95c20290cb91435f41578576fc2e99cf74c5e9f351fa93 |

Mechanical checks:
- All 33 `new_text` strings appear verbatim in v5.clean.
- v5.clean equals v5.md with the block anchors removed.
- token_conservation_round1.json lists 15 ADV-REV rows. Each numeric or citation delta belongs to one of the IL IDs claimed by its op. No delta is unclaimed.

Numbers were checked against the CSVs in `/home/user/B-i-FTSE2/output/`. Code (`code/analysis_revision2.R`, `car_port2`) confirms that t_portfolio = CAR / (s_est·√L), where L is the length of the event window.

## Verdict (corrected items): **FAIL**

- **Why FAIL.** The corrections introduce two new MEDIUM issues:
  - N-1: the new GEIS reference names a superseded version.
  - N-2: the new Burnham et al. sentence closely matches the source abstract (CLOSE_MATCH).
- **Resolution status.** 24 of 27 IL items are RESOLVED, 3 are PARTIAL (all MINOR), and none is NOT_RESOLVED.
  - Both SERIOUS items are resolved.
  - All 15 MEDIUM items are resolved.
- **Remaining MINOR items.** The PARTIALs are IL-MINOR-2 (Shleifer), IL-MEDIUM-7's title residue (logged as N-3; the MEDIUM part itself is resolved) and IL-MEDIUM-10's wording residue (logged as N-4).
- **Rule applied.** The agent's criteria say any MEDIUM means FAIL, so correction round 2 is required. Only N-1 and N-2 must be fixed. The MINOR items are recommended.
- **E6.** Two new STRENGTH-DRIFTED rows, both downward, close the checkpoint until the author disposes of them. Round-2 row ADV-E6-2 also has no recorded disposition.

## 1. Per-issue table

| IL ID | Op(s) | Verdict | Evidence / reason |
|---|---|---|---|
| IL-SERIOUS-1 | 5 (B0022) | RESOLVED | "whereas Gregoriou and Nguyen (2010) find no significant effect of FTSE 100 deletions on investment". The source finds "no effect of liquidity on future investments" in firms deleted from the FTSE 100. The MAJOR_DISTORTION is gone. MINOR precision note in §2 (B-6). |
| IL-SERIOUS-2 | 0 (B0009) | RESOLVED | "for years" becomes "persistently". The source says "sustained increase in the liquidity". |
| IL-MEDIUM-1 | 14 (B0084) | RESOLVED | named_excluded, Announcement [-1,5]: CARs 6.248% / 2.334% / 4.738% / 5.857%, so the range is 2.3% to 6.2%. t = 2.97 / 0.94 / 3.10 / 3.14, so "three of four" is correct. |
| IL-MEDIUM-2 | 12, 15 (B0076, B0094) | RESOLVED | Constituent, Effective date [-1,1]: CARs -0.139% / 0.948% / 0.032% / -0.543%, so the range is -0.5% to 0.9%. All \|t\| < 0.9. |
| IL-MEDIUM-3 | 19 (B0105) | RESOLVED | t_matched_weighted.csv cs: 0.00110 / 0.00140 / 0.00134, so 0.11 to 0.14 pp. This matches Table 2, column 6 (0.0011 / 0.0014 / 0.0013). The label "weighted matched sample" is correct. |
| IL-MEDIUM-4 | 11 (B0068) | RESOLVED | output/revision/t_pretrend_wald.csv, lamihud treated_matched_sample: F = 1.7208, p = 0.0924. Full sample: F = 6.66, p = 8e-11. ITT: F = 7.59, p = 1.6e-12. The added df sentence matches REPRO_REPORT.md. "Does not reject at 5%" still holds. No leftover 0.056 anywhere. |
| IL-MEDIUM-5 | 16, 17, 18 (B0096/98/102) | RESOLVED | Heading now covers the surge only. "Supports H4" becomes "consistent with H4, although … three stocks each". H4 (line 62) concerns the surge only, so the text is consistent. Takeaway is descriptive. Surge means are 1.231 / 0.976 / 0.645, which is monotone. |
| IL-MEDIUM-6 | 1, 3, 28 (B0011, B0018, +ref) | RESOLVED (reference defect: N-1) | The 30 June date is no longer attributed to the FAQ or VIR. The June cut-off is now cited to the GEIS ground rules, which support it (§2, B-1). The new reference entry itself has a version defect (N-1). |
| IL-MEDIUM-7 | 29 (B0169) | RESOLVED (MINOR residue: N-3) | "Version 1.3, August" is removed; year 2026 matches v1.2 (April 2026). The title was also changed to the notice title rather than the PDF title (N-3). |
| IL-MEDIUM-8 | 3 (B0018) | RESOLVED | The 49% → 4.9% example is now the paper's own arithmetic, with no FTSE attribution ("(10% of 49%)"). The FAQ confirms the 10/30/65/100 tranche factors. |
| IL-MEDIUM-9 | 30, 31 (B0176, B0177) | RESOLVED | Both headlines match the press releases exactly (audit A-3, A-4). |
| IL-MEDIUM-10 | 8, 13 (B0044, B0082) | RESOLVED (MINOR wording residue: N-4) | Brown & Warner (1985) is now cited only for the portfolio approach to dependence. √L scaling is stated as the paper's own assumption. The B0082 formula matches the code. The B0044 prose is ambiguous (N-4). |
| IL-MEDIUM-11 | 26 (B0150) | RESOLVED | All six scripts exist in code/. The versions R 4.3.3, fixest 0.14.2, MatchIt 4.5.5 and data.table 1.14.10 match repro/sessionInfo.txt. |
| IL-MEDIUM-12 | 6 (B0024) | RESOLVED | The Biktimirov & Afego clause is reworded: "separate return and trading-volume responses when a country changes class". It is now a PARAPHRASE. Phase D's optional advice to vary the sentence order was not taken (advisory). |
| IL-MEDIUM-13 | 0, 6, 27 | RESOLVED (new sentence triggers N-2) | Burnham et al. (2018) is added to B0009 and B0024 and to the reference list. The reference is VERIFIED (A-1). The new B0024 sentence is a close match to the source abstract (N-2). |
| IL-MEDIUM-14 | 22 (B0132) | RESOLVED | "reliable" becomes "significant under three of four benchmarks". ITT [-1,5] t = 3.97 / 1.91 / 3.72 / 3.75. |
| IL-MEDIUM-15 | 2, 14, 21, 24 | RESOLVED | ADV-E6-1: the causal caveat is restored in B0013. ADV-E6-3: B0084 now reads "suggests that investors responded to…". ADV-E6-4: B0122 now reads "for GEE … selection, for BSR it does not", which matches B0123 (BSR -0.39 by 31 Dec). ADV-E6-6: "portfolio" is restored in B0084 and B0137. |
| IL-MINOR-1 | 7 (B0041) | RESOLVED | The text now separates Amihud's definition (absolute return over dollar volume) from the paper's adaptation (log return, VND). |
| IL-MINOR-2 | 4 (B0021) | **PARTIAL** | Harris & Gurel: resolved; "on the effective date" is dropped. Hegde & McDermott: resolved; "mainly to lower direct trading costs" matches "due primarily to a decrease in the direct cost of transacting". Shleifer: not fully resolved. "Excess returns that do not reverse after inclusion" gives no horizon, while the source says the return "does not disappear for at least ten days after the inclusion". This is still a MINOR_DISTORTION: it implies permanence. Suggested wording: "excess returns that persist for at least ten days after inclusion". |
| IL-MINOR-3 | 25 (B0138) | RESOLVED | Raddatz et al. (2017) is scoped to the country level, and the three-stock pattern is called descriptive. |
| IL-MINOR-4 | 3 (B0018) | RESOLVED | November 2025 is cited to Viet Nam News (2025). The 31 Dec 2024 data date is cited to The Investor (2026a). |
| IL-MINOR-5 | 3 (B0018) | RESOLVED | "reflects its free float and foreign-ownership limits". |
| IL-MINOR-6 | 15 (B0094) | RESOLVED | The Vietnam-specific facts are now cited to FTSE Russell (2026) and VIR (2026). Harris & Gurel (1986) is removed from this sentence. |
| IL-MINOR-7 | 32 (B0192) | RESOLVED | "lists … for foreign institutional investors among the reforms". The source says it "recognized … progress … including the removal of the prefunding requirement for Foreign Institutional Investors … and … failed trades". |
| IL-MINOR-8 | 9 (B0055) | RESOLVED | Cited as (FTSE Russell, 2018; LSEG, 2025). |
| IL-MINOR-9 | 20 (B0115) | RESOLVED | EIB is no longer counted among the constituent banks. The counts agree with B0192: 8 banks + 5 securities firms = 13 constituents, and 7 constituents + EIB = 8 in the ITT group. Note: SHB, STB and VCB are also in the ITT group, and the phrase "EIB in the ITT group" does not say so. This is cosmetic. |
| IL-MINOR-10 | 10, 12, 23 | RESOLVED | B0064: "confirm" becomes "indicate". B0135: "under three of four benchmarks" is added. B0076: "up to 2.9 times". Table 4's last column is the cross-sectional t for the first (equal-weighted) benchmark. The constituent ratios t_cross / t_portfolio are at most 6.481 / 2.265 = 2.86, which rounds to 2.9. Ratios across all benchmarks reach 3.09, but those are not what the column shows. |

Summary: 24 RESOLVED, 3 PARTIAL (IL-MINOR-2 Shleifer, plus the MINOR residues on IL-MEDIUM-7 and IL-MEDIUM-10), 0 NOT_RESOLVED. The residues are logged as N-3 and N-4.

## 2. Phase A / B audit trail for new and changed citations

A0 (Semantic Scholar) was API_UNAVAILABLE, and egress to lseg.com and research.ftserussell.com is blocked, so all checks used WebSearch.

### Phase A: new references

| ID | Reference | Queries | Top result(s) | Fields confirmed | Verdict |
|---|---|---|---|---|---|
| A-1 | Burnham, T. C., Gakidis, H., & Wurgler, J. (2018). Investing in the presence of massive flows: The case of MSCI country reclassifications. *FAJ, 74*(1), 77–87. doi 10.2469/faj.v74.n1.8 | Q1 authors + title + FAJ; Q2 `"10.2469/faj.v74.n1.8"` | tandfonline.com/doi/abs/10.2469/faj.v74.n1.8; rpc.cfainstitute.org/…/faj-v74-n1-8; NBER w23557 | Three authors in order; title exact; FAJ vol 74 no 1 pp 77–87; DOI resolves to this article; year 2018 | **VERIFIED** (A2 clean) |
| A-2 | FTSE Russell. (2025). *FTSE Global Equity Index Series ground rules* (v13.4). lseg.com/…/ftse-global-equity-index-series-ground-rules.pdf. Accessed 24 September 2026 | Q1 GEIS v13.4 + "last business day of June"; Q2 `"FTSE Global Equity Index Series" ground rules "v13.4" 2025`; Q3 GEIS 2026 versions; Q4 September-review liquidity rule phrasing; WebFetch of the PDF was egress-blocked | research.ftserussell.com notices id=2616684 (31 Jul 2025), 2617565 (23 Oct 2025), 2618101; research.ftserussell.com/products/downloads/FTSE_Global_Equity_Index_Series.pdf (indexed "August 2026"); lseg.com GEIS PDF | The document exists. v13.4 is dated March 2025. Later versions exist: v13.5 (Jul 2025), v13.7 (Oct 2025), v13.8 (for the March 2026 review) and one indexed "August 2026" (v14.x). The cited URL is the always-current PDF. On the 24 Sep 2026 access date it served a later version, not v13.4. | **VERIFIED, with A2 MEDIUM defect (version/date mismatch), N-1** |
| A-3 | LSEG (2025, Oct 7), retitled | Exact-title query | wealthdfm.com reprint with the same headline; lseg.com 2025 press-release URL | Headline "FTSE Russell announces results of September 2025 semi-annual country classification review for equities and fixed income"; date 7 Oct 2025 | **VERIFIED** |
| A-4 | LSEG (2026, Apr 7), retitled | Exact-title query | mondovisione.com reprint; lseg.com 2026 URL (dated April 07, 2026) | Headline exact | **VERIFIED** |
| A-5 | FTSE Russell (2026). *Reclassification of Vietnam to secondary emerging market status: FAQ*. lseg.com/…/ftse-faq-document-vietnam-reclassification.pdf | Q1 title + filename; Q2 version query | research.ftserussell.com notice id=2619334, titled "Reclassification of Vietnam to Secondary Emerging Market Status FAQ"; the PDF at the cited URL | The title matches the notice. The PDF's own title, confirmed at Stage 4.5, is "Reclassification of Vietnam from Frontier to Secondary Emerging Market Status – FAQ". Year 2026 is consistent with v1.2 (April 2026). | **VERIFIED, MINOR title imprecision (N-3)** |

The other references touched by ops were already VERIFIED at Stage 4.5, and their entries are byte-identical: Gregoriou & Nguyen 2010, Hegde & McDermott 2003, Shleifer 1986, Harris & Gurel 1986, Brown & Warner 1985, Amihud 2002, Raddatz et al. 2017, The Investor 2026a, VIR 2026 and FTSE Russell 2018. I re-checked Hegde & McDermott (ScienceDirect PII S1386418102000460, consistent with the DOI) and Shleifer (Wiley, 41(3) 579–590) in passing.

### Phase B: every citation context changed by an op

| # | Block | Citation | New context (abridged) | Source text relied on | Verdict |
|---|---|---|---|---|---|
| B-1 | B0011, B0018 | FTSE Russell (2025) GEIS | September review screens liquidity on data up to the last business day of June | Guide to Calculation Methods for GEIS Liquidity / GEIS: "For the September review, liquidity will be tested from the first business day of July of the previous year to the last business day of June"; "data cut-off for the September review will be the last business day in June" | SUPPORTED (30 June 2026 was a Tuesday) |
| B-2 | B0009 | Burnham et al. (2018) | Among "studies of market reclassification [that] work with aggregate indices or country-level flows" | The abstract describes country-level MSCI market price effects | SUPPORTED |
| B-3 | B0024 | Burnham et al. (2018) | "prices of markets that MSCI reclassifies overshoot between the announcement and the effective date and largely revert within a year" | "reclassified markets' prices substantially overshoot between the announcement date and the effective date … but largely revert within a year" | SUPPORTED in content. Phase D flags the wording as CLOSE_MATCH (N-2). |
| B-4 | B0024 | Biktimirov & Afego (2026) | Persistent price gains for additions; separate return and volume responses on class change; institutional demand rather than trading pressure or liquidity | Abstract (Stage 4.5 Phase D rendering) | SUPPORTED; PARAPHRASE |
| B-5 | B0021 | Harris & Gurel (1986) | "additions lead index funds to buy, which produces temporary volume and price effects that reverse afterwards" | "immediately after an addition is announced, prices increase by more than 3 percent, and this increase is nearly fully reversed after 2 weeks" | SUPPORTED |
| B-6 | B0022 | Gregoriou & Nguyen (2010) | "find no significant effect of FTSE 100 deletions on investment" | "finds no effect of liquidity on future investments in a sample of U.K. firms deleted from the FTSE100 index" | SUPPORTED, with a MINOR precision note: the null result is for the liquidity decline's effect on investment, not for deletion as such. Suggested wording: "…find that the liquidity loss from FTSE 100 deletion has no significant effect on investment". Not blocking. |
| B-7 | B0021 | Shleifer (1986) | "excess returns that do not reverse after inclusion" | "does not disappear for at least ten days after the inclusion" | **MINOR_DISTORTION** (IL-MINOR-2 is PARTIAL) |
| B-8 | B0021 | Hegde & McDermott (2003) | "attribute mainly to lower direct trading costs" | "due primarily to a decrease in the direct cost of transacting and a smaller decline in the asymmetric information component" | SUPPORTED |
| B-9 | B0009 | Hegde & McDermott (2003) | "raise trading activity and narrow spreads persistently" | "sustained increase in the liquidity" | SUPPORTED |
| B-10 | B0044, B0082 | Brown & Warner (1985) | Portfolio approach addresses cross-sectional dependence; √L scaling stated as the paper's own assumption | Stage 4.5 CDA snippet: portfolio time-series SD over the estimation window | SUPPORTED. The UNVERIFIABLE_ACCESS part is no longer attributed to the source. |
| B-11 | B0041 | Amihud (2002) | "divides the absolute daily return by dollar volume" | "daily ratio of absolute stock return to dollar volume" | SUPPORTED |
| B-12 | B0138 | Raddatz et al. (2017) | "at the country level, benchmark weights shape fund allocations" | Stage 4.5 abstract basis (country-level, benchmark-driven allocations) | SUPPORTED |
| B-13 | B0018 | Viet Nam News (2025); The Investor (2026a) | November 2025 appearance; 31 Dec 2024 data date | Stage 4.5 R27 findings: 2026a supports the count and the data date | SUPPORTED |
| B-14 | B0018, B0094 | FTSE Russell (2026) FAQ; VIR (2026) | 27 constituents, effective after the close of 18 Sep; first tranche bought at the 18 Sep close; investability weight reflects free float and foreign-ownership limits | FAQ and VIR snippets from Stage 4.5 R13 ("implemented after the close of trading on September 18"; "assessed for liquidity using its 49% investability weight") | SUPPORTED. The foreign-limit gloss follows the Stage 4.5 finding that investability weight is capped by the foreign-ownership limit. |
| B-15 | B0055 | FTSE Russell (2018); LSEG (2025) | Seven years on the watch list | Start: Sep 2018. End: 7 Oct 2025 decision. | SUPPORTED |
| B-16 | B0192 | LSEG (2026) | Pre-funding removal for foreign institutional investors listed among the reforms | Press release text quoted in the IL-MINOR-7 row above | SUPPORTED |

## 3. A3 ghost-citation check (manuscript_v5.clean.md)

- Reference list: 33 entries, up from 31 in v4 (added Burnham et al. 2018 and FTSE Russell 2025).
- Body citations, extracted by regex and checked by first author and year: every one resolves to a reference entry.
  - Burnham et al. is cited twice.
  - FTSE Russell 2025 is cited twice.
  - FTSE Russell 2026 has a single entry and is unambiguous.
  - LSEG 2025 and 2026 are cited 2 times each.
  - The Investor 2026a and 2026b are both cited.
  - Harris & Gurel is cited twice (B0021 and §4.2); removing it from B0094 leaves no orphan.
- Orphan references: **0**. Dangling citations: **0**.
- Ordering: Burnham is placed after Brown; FTSE Russell 2025 sits between the 2018 and 2026 entries.
- A3: **PASS**.

## 4. E6 on correction round 1 (claim-strength drift)

I compared each claim-bearing op's `old` and `new_text` and checked every rung move or dropped qualifier against the claimed IL IDs. All 33 ops carry `claim_strength_changes: []`.

**Authorized moves (recorded and closed):**

| Op / block | Move | Authorized by |
|---|---|---|
| 0 / B0009 | "for years" → "persistently" (down) | IL-SERIOUS-2 |
| 2 / B0013 | Causal caveat restored | IL-MEDIUM-15 |
| 3 / B0018 | "FTSE's own illustration" removed | IL-MEDIUM-8 |
| 5 / B0022 | "mirror pattern" → "no significant effect" | IL-SERIOUS-1 |
| 10 / B0064 | "confirm" → "indicate" | IL-MINOR-10 |
| 14 / B0084 | "reflects … rather than" → "suggests that investors responded to…"; "portfolio" restored | IL-MEDIUM-15 |
| 17, 18 / B0098, B0102 | "supports H4" → "consistent with H4, although…"; "Index weight scales" → "was largest for…" | IL-MEDIUM-5 |
| 21 / B0122 | GEE / BSR split | IL-MEDIUM-15 |
| 22 / B0132 | "reliable" → "significant under three of four" | IL-MEDIUM-14 |
| 23 / B0135 | "under three of four benchmarks" added | IL-MINOR-10 |
| 24 / B0137 | "portfolio" restored | IL-MEDIUM-15 |
| 25 / B0138 | "suggests" → "is consistent with" (same bottom rung) + descriptive hedge | IL-MINOR-3 (its text names the three-stock segment) |
| 32 / B0192 | "credits" → "lists … among" | IL-MINOR-7 |
| 8 / B0044 | Independence assumption added (limitation added) | IL-MEDIUM-10 |

No hedge, null result or limitation was dropped by any op.

**STRENGTH-DRIFTED rows (checkpoint-closing; each needs `restore`, `authorize_with_reason` or `pause`):**

| ID | Round | Claim location | Prior rung → current rung | Roadmap items the op claimed | Direction |
|---|---|---|---|---|---|
| ADV-E6-R1-1 | integrity-correction 1 (op 23) | B0135, §6 Conclusion, first paragraph, last sentence | "a trading surge at the rebalancing close, **scaled by index weight**" (causal/proportional: affects) → "**largest for the largest constituents**" (descriptive ordering) | IL-MINOR-10 only. That item covers the "three of four" qualifier. IL-MEDIUM-5, which motivates this weakening, does not target B0135. | down |
| ADV-E6-R1-2 | integrity-correction 1 (op 4) | B0021, §2.2, price-pressure sentence | "additions **force** passive funds to buy" (determines) → "additions **lead** index funds to buy" (leads to) | IL-MINOR-2, which authorizes dropping "on the effective date" but not changing the verb | down |

Recommendation for both rows: `authorize_with_reason`. Each move aligns the text with the evidence: three-stock segment means for R1-1, and Harris & Gurel's general mechanism for R1-2. The ladder still requires the author's explicit choice.

**Carried-over open row:** ADV-E6-2 from e6_semantic_review_round2.md (B0013, "raised" → "rose", down) is not in the correction list. No disposition sidecar or author-input record for it exists under `ars/`. It stays checkpoint-closing until the author disposes of it.

**Status:**
- These rows are model-mediated: "detected by the recorded semantic review".
- No `claim-strength-drift-findings/1.0` companion or disposition sidecar has been built for round 1 yet. The orchestrator must persist one and run `scripts/claim_strength_drift_disposition.py` before the checkpoint can advance.
- E6 rows do not enter the PASS/FAIL count.

## 5. New issues introduced by the corrections (IL-style, fresh numbering for this report)

### MEDIUM (must fix)

| ID | Category | Location | Issue | Correct information | Source |
|---|---|---|---|---|---|
| IL-MEDIUM-1 (N-1) | Bibliographic (A2 version/date) | References, new FTSE Russell (2025) entry (op 28); cited in B0011 and B0018 | The entry names v13.4 (March 2025) with the always-current lseg.com URL and "Accessed 24 September 2026". On that date the URL served a later version (v13.8 or later; a version indexed "August 2026"). v13.4 was also superseded before the September 2026 review whose rule the text cites. This is the same defect class as the FAQ version issue in the previous round. | Cite the version actually consulted and in force at the September 2026 review, with its version number and date. Or cite the *Guide to Calculation Methods for GEIS Liquidity*, which states the rule. The rule itself is correct. | research.ftserussell.com notices 2616684 / 2617565 / 2618101; FTSE_Global_Equity_Index_Series.pdf (indexed Aug 2026) |
| IL-MEDIUM-2 (N-2) | Originality (Phase D CLOSE_MATCH, cited) | B0024, new Burnham sentence (op 6) | "overshoot between the announcement and the effective date and largely revert within a year" repeats the abstract nearly word for word: "overshoot between the announcement date and the effective date … but largely revert within a year" (13 of 14 words in order). This is the same MODERATE class as the Biktimirov clause this round fixed. | Reword in the authors' own terms, for example: "Burnham et al. (2018) show that country-level prices move too far between MSCI's announcement and implementation and give back most of the move within twelve months." Or quote the passage. | Burnham et al. (2018) abstract (tandfonline, NBER w23557) |

### MINOR (recommended)

| ID | Category | Location | Issue | Suggestion |
|---|---|---|---|---|
| IL-MINOR-1 (carried; IL-MINOR-2 PARTIAL) | Citation context | B0021, Shleifer (1986) | "do not reverse after inclusion" implies permanence. The source says "at least ten days". | "excess returns that persist for at least ten days after inclusion" |
| IL-MINOR-2 (N-3) | Bibliographic | References, FTSE Russell (2026) FAQ (op 29) | The title was changed to the index-notice title. The PDF at the cited URL is titled "Reclassification of Vietnam from Frontier to Secondary Emerging Market Status – FAQ". | Use the PDF title, which the old entry had, keep the year 2026, and add "(Version 1.2)" if that is the copy used. |
| IL-MINOR-3 (N-4) | Clarity / internal consistency | B0044 (op 8) | "the portfolio CAR is divided by the standard deviation …, multiplied by the square root of the number of days" can be read as (CAR/σ)·√L. The code and the Table 4 note (B0082) use CAR/(σ·√L). | "…is divided by the product of the standard deviation … and the square root of the number of days in the event window…" |
| IL-MINOR-4 (B-6) | Citation context | B0022, Gregoriou & Nguyen (2010) | The null is for the effect of lower liquidity on investment after deletion, not for deletion as such. | "…find that the liquidity loss from FTSE 100 deletion has no significant effect on investment" |

Checked and found no problem:
- Table references in the changed blocks: Table 2 col. 3 and col. 6, Table 4 panels A–C, Table 6, Table 8, Table 9 panels A and C.
- The H4 wording, the §4.4 heading and the takeaway are consistent with each other.
- §3 line 119 ("data as of 30 June 2026", uncited) is consistent with the GEIS rule.
- No grammar error changes meaning.
- No leftover 0.056, 6.3%, 1.0%, "for years" or "FTSE's own illustration" anywhere in v5.

## 6. Verification summary (corrected-item scope)

| Category | Total | Passed | Issues |
|---|---|---|---|
| IL items re-verified | 27 | 24 RESOLVED | 3 PARTIAL (MINOR) |
| New reference existence (A1) | 2 | 2 | 0 |
| Bibliographic accuracy of new or changed entries (A2) | 5 | 3 | 1 MEDIUM (N-1), 1 MINOR (N-3) |
| Ghost citations (A3, whole manuscript) | 33 refs | PASS | 0 orphan / 0 dangling |
| Citation contexts changed by ops (B) | 16 | 14 SUPPORTED | 1 MINOR_DISTORTION (Shleifer), 1 precision note (Gregoriou & Nguyen) |
| Numbers changed by ops (C) | 8 | 8 | 0 |
| Originality of new or rewritten sentences (D1, 100%) | 3 | 2 | 1 CLOSE_MATCH (N-2) |
| E6 drift (op-level) | 33 ops | 31 no drift or authorized | 2 STRENGTH-DRIFTED (ADV-E6-R1-1, -2), plus ADV-E6-2 carried open |

**Verdict: FAIL.** It rests on two MEDIUM issues (N-1 and N-2) and nothing else. Round 2 should fix those two and, preferably, the four MINOR items. It should then re-verify only those blocks and run E6 again on the round-2 ops. The author must dispose of ADV-E6-R1-1, ADV-E6-R1-2 and ADV-E6-2 before the Stage 4.5 checkpoint can advance. This pass is round 1 of the maximum 3 correction rounds.

## Tool limitation note

- Phase A0 APIs, lseg.com and research.ftserussell.com were blocked, so these checks rely on WebSearch snippets and publisher or index pages.
- The GEIS version finding (N-1) rests on indexed version listings, not on opening the PDF.
- Phase D is heuristic and is not professional plagiarism software.
