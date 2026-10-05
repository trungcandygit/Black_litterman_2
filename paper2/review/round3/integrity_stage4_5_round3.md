# Stage 4.5 Final Integrity Check, Mode 2 (final verification), round 3

Manuscript under test: `paper2/manuscript/manuscript_final.Rmd`. It is byte-identical to `paper2/final/Paper_C_Closing_at_the_limit.Rmd`, and `final/Paper_C_Closing_at_the_limit.docx` is byte-identical to `manuscript/manuscript_final_styled.docx`. The rendered text was read with `pandoc ... -t plain --wrap=none`; equations appear as raw TeX, which is expected.
Verifier: an independent integrity_verification_agent with a fresh context. It did not write or review the paper. Run on 2026-10-05.
Protocol followed: `academic-pipeline/references/integrity_review_protocol.md` (Stage 4.5), `agents/integrity_verification_agent.md` (Mode 2) and `references/ai_research_failure_modes.md`.
No manuscript, code, data or output file was edited. `R/46_verify_C.R` was run from a scratch copy whose only change was the output path. The independent recomputation used the verifier's own script (`scratchpad/indep.R`), which sources no repository code. `git status` was unchanged before and after both runs: the only entry is the untracked `paper2/R/run_all.R`, which was already present.
Scope: the PASS/FAIL decision covers only the registered populations: 51 reference entries; every citation context in Sections 1, 2, 5 and 6 and in Table 5; every inline number in the abstract, the text, Tables 1-5 and the figure captions; Equations (1)-(8); and the E1 claim registry listed in Phase E. It does not certify global correctness.

## Verdict: FAIL

Counts:
- MAJOR_DISTORTION: 1 (IL-SERIOUS-1).
- UNVERIFIABLE: 0.
- MINOR or MINOR_DISTORTION items: 4 (IL-MINOR-1 to IL-MINOR-4). At Stage 4.5 the agent's verdict table also counts these as issues.
- Notes, which never block: UNVERIFIABLE_ACCESS 3 and process notes 4.

The blocking item is one sentence in Section 2. It reverses the finding of Zhang et al. (2022) on information asymmetry. The fix is text only and needs no re-analysis.

Everything else passes:
- All 51 references exist and match their bibliographic records.
- All re-review items NEW-1 to NEW-12 are resolved, and NEW-13 is resolved on the replication side.
- `R/46_verify_C.R` passes T1-T6.
- The independent recomputation reproduces 30 headline quantities from `data/raw`, including the new C27 tick-grid shares and the near-hit medians.
- Every inline number checked against the saved tables agrees.
- Equations (1)-(8) match the code.

## Issue list (by severity)

### SERIOUS (must fix)

| ID | Category | Location | Issue | Correct information | Source |
|---|---|---|---|---|---|
| IL-SERIOUS-1 | Citation context (Phase B/E), MAJOR_DISTORTION | Section 2, "Recent evidence from band changes", Rmd line 57 | The manuscript says Zhang et al. (2022) "find higher liquidity and lower information asymmetry after the widening". The published finding has the opposite sign on information asymmetry. After the ChiNext widening from 10% to 20%, stock liquidity rises (transaction speed and depth), return volatility rises, and the probability of informed trading (VPIN) rises. The authors read this as an *increase* in information asymmetry ("individual investors have become less informed, leading to an increase in the possibility of informed trading and thus in the degree of information asymmetry"). The error comes from evidence-file entry 16 in `process/08_literature_review_benchmark.md` ("market information asymmetry decreases"), which appears to mix this paper up with Jia et al. (2024), whose channel is lower information asymmetry. | OLD: `Zhang et al. (2022) find higher liquidity and lower information asymmetry after the widening, and Jia et al. (2024) find lower crash risk.` NEW: `Zhang et al. (2022) find higher liquidity, higher volatility, and a higher probability of informed trading after the widening, and Jia et al. (2024) find lower crash risk.` Also correct evidence-file entry 16 and the Theme 2 sentence in `08_literature_review_benchmark.md` ("lower information asymmetry in China (Zhang et al., 2022; Jia et al., 2024)" should read "lower information asymmetry in Jia et al. (2024) but more informed trading in Zhang et al. (2022)"). The Section 5 citation of Zhang et al. ("Band changes in other markets changed volatility, liquidity, and execution quality") is correct and stays. | Search records: ScienceDirect `S0927538X22000737` and IDEAS `pacfin/v74y2022ics0927538x22000737`. Abstract-level summaries from two independent searches agree: "significantly improves market liquidity and increases market volatility and the probability of informed trading"; "the VPIN for ChiNext stocks increases ... thus increases the degree of information asymmetry". One search summary that said "decreases" restated the crash-risk and bad-news-hoarding channel of Jia et al. (2024), so it was not attributable to this paper. The publisher page could not be fetched (egress block). If the authors hold the full text and it shows a decrease on a different measure, they should cite that measure explicitly. |

### MEDIUM

None.

### MINOR (at Stage 4.5 these must be fixed before Stage 5)

| ID | Category | Location | Issue | Suggestion (exact strings) |
|---|---|---|---|---|
| IL-MINOR-1 | Internal consistency / data interpretation (C2) | Section 7, limitation (iv), Rmd line 228 | "against 100% for stocks below 10 thousand dong" is mechanical. Every price in `data/raw` has at most two decimals (checked: 157,144 two-decimal and 49,273 one-decimal close values). The 0.01 tick for prices below 10 therefore equals the data's resolution, and the 100% carries no evidence that those prices are unadjusted. As written, the contrast reads as evidence. | OLD: ``against `r f(c27(1),0)`% for stocks below 10 thousand dong`` NEW: ``against `r f(c27(1),0)`% for stocks below 10 thousand dong, where the 0.01 tick equals the two-decimal resolution of the files and the check is uninformative`` |
| IL-MINOR-2 | Claim strength, internal consistency (Phase E, MINOR_DISTORTION) | Section 6, policy paragraph, Rmd line 218 | Section 5 concludes "We cannot attribute the differences between the periods to the auction rules". Section 6 says the floor pattern "suggests that auction design shapes how the opening absorbs overnight pressure". The caveat is present, but the verb attributes the change to the auction rules, which goes beyond what Section 5 allows. | OLD: `The floor gap grows and the intraday return after floor closes turns positive after at-the-open orders lose priority (Table 4), which suggests that auction design shapes how the opening absorbs overnight pressure, although the market period changed at the same time (Section 5).` NEW: `The floor gap grows and the intraday return after floor closes turns positive after at-the-open orders lose priority (Table 4). This is consistent with auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time, so the split cannot isolate the auction rules (Section 5).` |
| IL-MINOR-3 | Bibliographic completeness (A2) | References, Rmd lines 298 and 320 | Huang, Liu and Shu (2023) and Lin, Qiu and Zheng (2023) lack article numbers and DOIs. This was carried over from the round-2 report (n10) and is still unfixed. Huang et al.: PBFJ 82, article 102176, confirmed by the journal PDF header "Pacific-Basin Finance Journal 82 (2023) 102176". Lin et al.: JBF 150, article 106818, DOI 10.1016/j.jbankfin.2023.106818 (two independent search records; publisher pii S0378426623000432). | OLD: `*Pacific-Basin Finance Journal, 82*.` NEW: `*Pacific-Basin Finance Journal, 82*, 102176.` OLD: `*Journal of Banking & Finance, 150*.` NEW: `*Journal of Banking & Finance, 150*, 106818. https://doi.org/10.1016/j.jbankfin.2023.106818` (confirm the article number on the publisher page before submission) |
| IL-MINOR-4 | Reference-list format (B2) | References, Rmd lines 284-286 | In APA alphabetical order "Gu, M." precedes "Gutierrez, R. C., Jr." (nothing precedes something), but the list has them the other way round. | Move the `Gu, M., Hu, Y., & Xiong, Z. (2025)...` entry above the `Gutierrez, R. C., Jr., & Kelley, E. K. (2008)...` entry. |

### Notes (UNVERIFIABLE_ACCESS and advisory; not issues)

- N-A1 (UNVERIFIABLE_ACCESS). Section 3 cites HSC (2025) for the 7% band, the reference price and the KRX change.
  - The cited page ("Important changes of new trading system") cannot be fetched because of the egress block. Search records confirm the 5 May 2025 launch and the loss of ATO/ATC priority.
  - The 7% band and the previous-close reference price appear in search records of a different HSC page ("1.1. HSX Trading Regulations", hsc.com.vn/en/hsx-trading-regulations) and in TCBS guides. They were not seen in the cited page.
  - Optional: add that page as a second HSC reference for the band sentence. The manuscript already calls these facts assumptions (Section 3 and limitation iii), so this is not a distortion.
- N-A2 (UNVERIFIABLE_ACCESS). The following were verified at abstract or record level only, with no full text:
  - Huang et al. (2001): IDEAS and ResearchGate record ("price continuations for the overnight period following limit moves and price reversals for the subsequent trading time period").
  - Berkman and Lee (2002): bibliographic record.
  - Kim and Limpaphayom (2000): no public abstract (IDEAS shows none).
  - Liang and Hu (2025).
  The manuscript's wording stays within these records. Table 5 discloses that it is based on "abstract or records we could access".
- N-A3 (UNVERIFIABLE_ACCESS / precision). Zeng et al. (2024): the published FRL abstract speaks of "high net price limit hitting ratios". The SSRN predecessor (Zeng and Tang) says "stocks that frequently hit the upper limit generate substantially lower future stock returns". The manuscript's "frequency of upper-limit hits" (Section 2) and "frequent upper-limit hits" (Table 5) follow the SSRN wording and do not change the meaning. Optional precision: "relate a high net (upper minus lower) limit-hit ratio to lower future returns".
- ADV-E5-1 (novelty classification, advisory). The novelty claims are all bounded by the authors' search and acknowledge the nearest prior work:
  - Section 1: "of the studies we reviewed, only Huang et al. (2001) describe ... none measures ... against a benchmark".
  - Section 2: "Apart from Huang et al. (2001)"; "We found no peer-reviewed study of post-limit returns on HOSE".
  - Section 6: "No source reports ... in a form that matches ours".
  Classification: SUPPORTED_WITHIN_SEARCH in substance. The search log has no machine-readable `last_searched_at`, so the formal class is UNRESOLVED. A non-peer-reviewed repository with a HOSE close-to-close estimate (recorded in `process/04_literature_search_log.md`) is still not named. The peer-reviewed bound makes this acceptable.
  The abstract's "Few studies trace prices after limit closes in emerging markets" is loose, given that Section 2 itself reviews Taiwan, Istanbul, Korea, Shenzhen and ChiNext studies. Optional: "Few studies measure the return that follows a limit close in emerging markets".
- ADV-E4 (scope, advisory). All claims stay within one exchange, 2024-2026, and daily data. No broadening was found.
- Process notes:
  - P1. Evidence-file entry 2 (Berkman and Lee) still says "abstract not retrieved". This was the process half of NEW-13 and remains unchanged.
  - P2. `paper2/R/run_all.R` exists but is untracked in git, so the repository does not yet contain the entry point that the data and code statement implies.
  - P3. The machine contracts of Phase E (`claim-registry/1.0`, `claim_registry_coverage.py`, `evidence_rows.py`, E6 drift companion) were not run, because this project keeps no passport inputs for them. The claim registry is the markdown table in Phase E below. E1.1 is therefore `not_run` (E1-COVERAGE-UNRESOLVED; the orchestrator must decide at the checkpoint), and E6 is recorded as `[E6-SKIPPED: no machine revision-evidence bundle]`. Claim-strength changes this round were checked by hand against `review/round3/manuscript_before_round3.Rmd` (see E6 below).
  - P4. The data and code statement writes the repository name in lower case (`trungcandygit/black_litterman_2`), whereas the remote is `trungcandygit/Black_litterman_2`. GitHub resolves either form.

## Phase A: references (51 entries; every one searched this session)

The DOI resolver is blocked, so each DOI was matched against the identifier on a publisher or index page returned by search (Wiley `doi/10.1111/...`, ScienceDirect pii, IDEAS handle, JSTOR, Cambridge, Springer, PLOS, Tandfonline). Verdicts:
- 51 of 51 VERIFIED for existence.
- Bibliographic fields match, apart from IL-MINOR-3 (missing article numbers) and IL-MINOR-4 (order).
- No NOT_FOUND and no MISMATCH. No DOI conflicts with any record.

Ghost-citation check: a script matched every surname-year pair in the body against the reference list and vice versa. No orphan and no dangling citation. HSC and Viet Nam News are group-author citations and are cited.

Audit trail (query → top result → confirmed fields):

| Reference | Top result | Confirmed |
|---|---|---|
| Gu, Hu & Xiong (2025) **new** | Wiley `10.1111/acfi.13354`; IDEAS `acctfi/v65y2025i1p883-911` | Ming Gu, Yi Hu, Zhitao Xiong; A&F 65(1) 883-911; DOI matches; finding (overnight component drives the lottery anomaly, stronger with gambling preference and limits to arbitrage) matches Section 2 |
| Cameron, Gelbach & Miller (2011) **new** | IDEAS `jnlbes/v29y2011i2p238-249`; Semantic Scholar | JBES 29(2) 238-249, April 2011; DOI 10.1198/jbes.2010.07136 matches; two-way/multiway non-nested estimator matches the Section 4 use |
| Aboody et al. (2018) | Cambridge JFQA 53(2) | 485-505 ✓ |
| Akbas et al. (2022) | ResearchGate/SMU | JFE 145(3) 850-875 ✓ |
| Amihud (2002) | Journal PDF | JFM 5(1) 31-56 ✓ |
| Bali et al. (2011) | NYU PDF | JFE 99 427-446 ✓ |
| Benjamini & Hochberg (1995) | Wiley RSS | 57(1) 289-300; DOI ✓ |
| Berkman et al. (2012) | KU / Cambridge front matter | JFQA 47(4) 715-741 ✓ |
| Berkman & Lee (2002) | ScienceDirect `S0927538X02000409` | PBFJ 10(5) 517-530; pii = DOI string ✓ |
| Bildik & Gülay (2006) | Wiley `j.1475-6803.2006.00185.x` | JFR 29(3) 383-403 ✓ |
| Bogousslavsky (2021) | EconPapers | JFE 141(1) 172-194 ✓ |
| Brennan (1986) | multiple index records | JFE 16(2) 213-233 ✓ |
| Chen, Petukhov, Wang & Xing (2024) | Wiley `jofi.13310` | JF 79(2) 1405-1455 ✓ |
| Chen, Gao, He, Jiang & Xiong (2019) | IDEAS `econom/v208y2019i1p249-264` | DOI ✓ |
| Chen Y.-M. (1993) | ScienceDirect `0927538X93900053` | PBFJ 1(2) 139-153; DOI string matches ✓ |
| Cho et al. (2003) | IDEAS `empfin/v10y2003i1-2p133-168` | JEF 10(1-2) 133-168 ✓ |
| Chordia et al. (2020) | EconPapers | RFS 33(5) 2134-2179; 3.38 cross-sectional ✓ |
| Corwin & Schultz (2012) | Wiley | JF 67(2) 719-760; DOI ✓ |
| Deb et al. (2013) | ScienceDirect `S104244311200100X` | JIFMIM 24 66-84 ✓ |
| Fama & MacBeth (1973) | IDEAS | JPE 81(3) 607-636; DOI 10.1086/260061 ✓ |
| Greenwald & Stein (1991) | EconPapers | JB 64(4) 443-462 ✓ |
| Gutierrez & Kelley (2008) | Wiley | JF 63(1) 415-447; DOI ✓ |
| Harvey & Liu (2020) | Wiley | JF 75(5) 2503-2553; DOI ✓ |
| Harvey, Liu & Zhu (2016) | IDEAS | RFS 29(1) 5-68; "t > 3.0" ✓; DOI 10.1093/rfs/hhv059 (standard) |
| Holm (1979) | multiple | SJS 6(2) 65-70 ✓ |
| Hou, Xue & Zhang (2020) | OUP | RFS 33(5) 2019-2133; "with microcaps mitigated ... 65% of the 452" ✓ |
| HSC (2025) | hsc.com.vn page exists in search | content: N-A1 |
| Huang X. et al. (2023) | journal PDF header "PBFJ 82 (2023) 102176" | IL-MINOR-3 |
| Huang Y.-S. et al. (2001) | IDEAS `reveco/v10y2001i3p263-288` | IREF 10(3) 263-288 ✓ |
| Jia et al. (2024) | ScienceDirect `S1544612323010875` | FRL 59, 104715 ✓ |
| Jones et al. (2025) | IDEAS `jfinqa/v60y2025i1p68-104` | JFQA 60(1) 68-104 ✓ |
| Kelly & Clark (2011) | Springer `10.1057/jam.2011.2` | JAM 12 132-145 ✓ |
| Kim & Limpaphayom (2000) | IDEAS `finmar/v3y2000i3p315-332` | JFM 3(3) 315-332 ✓ |
| Kim & Rhee (1997) | Wiley | JF 52(2) 885-901; DOI ✓ |
| Kim & Jun (2019) | IDEAS `apeclt/v26y2019i7p582-586` | AEL 26(7) 582-586 ✓ |
| Kodres & O'Brien (1994) | EconPapers | AER 84(4) 919-932 ✓ |
| Liang & Hu (2025) | Wiley `for.3197`; IDEAS | JoF 44(2) 297-319 ✓ |
| Lien et al. (2019) | IDEAS `pacfin/v55y2019icp239-258` | PBFJ 55 239-258 ✓ |
| Lin et al. (2023) | ScienceDirect `S0378426623000432` | JBF 150 ✓ (article number: IL-MINOR-3) |
| Lou et al. (2019) | EconPapers | JFE 134(1) 192-213 ✓ |
| Lu et al. (2023) | ScienceDirect `S0304405X23000491` | JFE 148(3) 175-200 ✓ |
| Newey & West (1987) | JSTOR 1913610 | Econometrica 55(3) 703-708; DOI ✓ |
| Parkinson (1980) | IDEAS | JB 53(1) 61-65; DOI 10.1086/296071 ✓ |
| Petersen (2009) | EconPapers | RFS 22(1) 435-480 ✓ |
| Qi (2023) | PLOS | 18(6) e0287548; DOI ✓ |
| Qiao & Dam (2020) | RUG PDF `S1386418120300033` | JFM 50, 100534 ✓ |
| Qiu et al. (2025) | IDEAS `riibaf/v75y2025ics0275531925000327` | RIBF 75, 102776 ✓ |
| Subrahmanyam (1994) | Wiley | JF 49(1) 237-254; DOI ✓ |
| Viet Nam News (2025) | vietnamnews.vn/economy/1717047 | exists; 5 May 2025 launch ✓ |
| Zeng et al. (2024) | ScienceDirect `S1544612323011753` | FRL 60, 104803 ✓ |
| Zhang et al. (2022) | ScienceDirect `S0927538X22000737` | PBFJ 74, 101778 ✓ (context: IL-SERIOUS-1) |

## Phase B: citation contexts (100% of Sections 1, 2, 5, 6 and Table 5)

All contexts were checked against the abstract or record returned this session. All agree except IL-SERIOUS-1 (Zhang et al., 2022). Notes N-A2 and N-A3 apply to the access-limited records. Points of interest:

- **Huang et al. (2001)**, the novelty anchor. The record says "price continuations for the overnight period following limit moves and price reversals for the subsequent trading time period ... overreaction is delayed by price limits and corrected in the trading time period following limit moves". This matches:
  - Section 1 ("describe the overnight-then-intraday pattern ... the records we could access give no magnitudes");
  - Section 2 ("the overnight overreaction after limit hits reverses during the following trading day");
  - Section 5 ("The signs match ...");
  - Table 5 ("Same timing").
- **Gu et al. (2025)**, new. Matches the record.
- **Cameron et al. (2011)**, new. Cited for the two-way variance (date plus stock minus heteroskedasticity-robust), which is the CGM estimator. The 10⁻¹² floor is the authors' own implementation detail and is not attributed to CGM.
- **Theory paragraph.** Matches the abstracts:
  - Brennan: rationale for limits in futures markets.
  - Kodres and O'Brien: Pareto-superior limits under fundamental news; implementation risk.
  - Greenwald and Stein: "imperfections in transactional mechanisms".
  - Subrahmanyam: halts "advance trades in time", higher variability.
  - Chen et al. (2024): volatility rises toward the breaker; magnet effect.
- **Classic evidence.** Matches the abstracts:
  - Kim and Rhee: all three criticisms supported.
  - Bildik and Gülay: "price locks at limits ... provide significantly stronger evidence ... than ... limit moves only".
  - Chen (1993): "serial correlations ... inversely related to the range of price limits, implying a delaying effect".
  - Cho et al.: acceleration toward the upper limit.
  - Deb et al.
- **Recent evidence.** Matches the abstracts:
  - Qi: three hypotheses confirmed, stronger at the lower limit, no magnet effect.
  - Jia et al.: lower crash risk.
  - Lien et al.: spreads and intraday volatility up, execution quality better, 2015.
  - Kim and Jun: intraday variance up after the 2015 change.
  - Chen et al. (2019): buy on the limit day, sell the next day; long-run reversal.
  - Lin et al.: exposure, attention, lower returns, stronger with retail holdings.
  - Zeng et al.: N-A3.
  - Liang and Hu: the reworded "the record we could access reports no returns after the hit" is accurate.
- **Overnight and intraday returns.** Matches the abstracts:
  - Kelly and Clark: QQQQ.
  - Berkman et al.
  - Aboody et al.
  - Lou et al.: "offsetting cross-period reversal".
  - Akbas et al.
  - Bogousslavsky: overnight margin and lending fees.
  - Lu et al.: retail imbalances filled by market makers near the open.
  - Qiao and Dam: negative average overnight return; T+1 discount on the open.
  - Qiu et al.: the open and the close.
  - Jones et al.: small retail investors with poor selection.
- **Multiple testing.** Matches the abstracts:
  - Harvey et al.: t > 3.0.
  - Chordia et al.: 3.38, given in the text as "near 3.4".
  - Hou et al.: the microcap condition is stated.
  - Petersen.
  - Gutierrez and Kelley.
  - Huang X. et al.: significant size effect; EP dominates value.
- **Table 5.** All twelve rows agree with the records except the Zhang-related content. Zhang et al. are not in Table 5. No UNVERIFIED magnitude from the evidence file appears (Chen et al. 2.44%/2.59%/83.6%, Hendershott 14/15 bp, Lou "2% per month", Qiao-Dam 14 bp: all absent).

## Phase C: statistical and data surfaces

**R/46_verify_C.R** (scratch copy, exit 0):
- T1: look-ahead difference 0. PASS.
- T2: MOM3M slope 0.12287 equals the table. PASS.
- T3: ceiling t+1 mean 1.66022% on 3,187 events equals the table. PASS.
- T4: gap + intraday − close-to-close = 0.0457 pp. PASS.
- T5: counts reconcile. PASS.
- T6: 4 of 26 tests survive. PASS.

**Independent recomputation from `data/raw`** (verifier's own code; no repository code sourced):

| # | Quantity | Manuscript / table | Recomputed |
|---|---|---|---|
| 1 | Files; trading days; span | 405; 519; 21 Aug 2024 to 23 Sep 2026 | 405; 519; 2024-08-21 to 2026-09-23 |
| 2 | Stocks kept; stock-days | 347; 178,773 | 347; 178,773 |
| 3 | Mean / SD / median daily return (%) | 0.018; 2.10; 0.00 | 0.01788; 2.0982; 0 |
| 4 | Pile-up +6.5..7.1 / −7.1..−6.5 / +6.0..6.5 (%); beyond ±8% | 1.98; 1.30; 0.29; 96 | 1.984; 1.303; 0.288; 96 |
| 5 | Window ceilings / floors / denominator; shares | 3,207; 2,115; 2.0%; 1.4% | 3,207; 2,115; 156,653; 2.047%; 1.350% |
| 6 | Ceiling t+1, t+1..5 (date clusters, G/(G−1)) | 1.66 (4.90), 1.45 (4.00); 3,187 events, 446 dates | 1.6602 (4.902), 1.4497 (4.0035); 3,187; 446 |
| 7 | Floor t+1, t+1..5 | −0.71 (−5.32), −1.76 (−4.74); 2,105; 319 | −0.7130 (−5.318), −1.7602 (−4.744); 2,105; 319 |
| 8 | Ceiling gap / intraday / close-to-close / open-to-d+5 (lagged weights) | 2.24; −0.54; 1.66; −0.75; 3,199 | 2.2435; −0.5354; 1.6643; −0.7486; 3,199 |
| 9 | Floor gap / intraday / close-to-close / open-to-d+5 | −0.97; 0.30; −0.69; −0.82; 2,111 | −0.9722; 0.3040; −0.6917; −0.8162; 2,111 |
| 10 | Exact-hit ceiling gap (N) / near-hit gap (N) | 2.79 (1,642) / 1.67 (1,557) | 2.7856 (1,642) / 1.6719 (1,557) |
| 11 | Ceilings locked all day | 522 | 522 |
| 12 | KRX split: ceiling gap pre / post; N | 1.65 / 2.49; 936 / 2,263 | 1.6455 / 2.4909; 936 / 2,263 |
| 13 | Post-change share of events, ceiling / floor | 71% / 58% | 70.7% / 57.8% |
| 14 | KRX split floor N | 891 / 1,220 | 891 / 1,220 |
| 15 | **C27** closes on tick grid, price ≥ 10: 2024 / 2025 / 2026 | 25% / 31% / 58% (C27: 24.53 / 30.57 / 57.97) | 24.529 / 30.566 / 57.969 (n 22,263 / 64,365 / 44,843) |
| 16 | **C27** closes on tick grid, price < 10 | 100% | 100 (mechanical; IL-MINOR-1) |
| 17 | **C27** exact / near-hit counts (no outcome requirement) | 1,648 / 1,559 | 1,648 / 1,559 |
| 18 | **Near-hit medians**: day-d return exact vs near | 6.90% vs 6.89% | 6.8978 vs 6.8934 |
| 19 | **C27** near hits off the tick grid | 83% | 82.745% |
| 20 | **C27** near-hit share, reference price < 10 / ≥ 10 | 23% / 62% | 22.736 / 61.788 |
| 21 | Ceiling vs 5-6.5% rises, gap difference (date-clustered HC1), comparison N | 2.66 (t 14.0); 1,751 | 2.6582 (t 13.981); 1,751 |

Further surfaces were checked against the saved CSVs under the manuscript's rounding. All agree.
- **Abstract.** 347; 26 = 4 + 22; 1.7 = 2.2 − 0.5; 2.7; 0.7.
- **Section 5 and Figure 1 (C1, C14).**
  - Largest |t| 1.45 (MOM3M 1.452, IMOM 1.448), confirmation 1.17 / 1.14.
  - VOL −0.09, IVOL −0.54, MAX −0.02.
  - 18 of 22 net spreads negative (four positive: MOM3M, MOM6M, IMOM, LNDVOL).
  - MDE 0.12-0.31 (0.1226-0.3089).
  - Lag-8 maximum 1.79.
  - Least-liquid exclusion maximum 1.62 (MIN 1.620).
- **Table 1 (C18).** All 36 t-statistics and both half-sample columns agree.
- **Survival and Bonferroni (C3, C20, C21).**
  - BH adjusted p at most 0.0004 (max 3.98e-4).
  - Week-cluster rule: all four survive.
  - m_max 683 / 125.
  - Largest p 0.00007 / 0.00040.
- **Table 2 (C11, C16).** All 16 rows × 4 columns plus Events agree.
  - First-of-streak exact 2.39.
  - Liquid tercile 1.52.
  - Controls 2.70 / −1.65.
  - 740 of 2,111.
  - Least-liquid floor t −1.0.
  - Floor next-open to day 5: −0.82 (t −1.7).
- **Table 3 (C17, C23).** All 8 rows agree; 3.14 (14.5), −1.81, 2.40, −1.14, −0.31.
- **Attention proxies (C24).** 1.97 / 2.16 / 2.63; 1.41 / 2.18 / 3.16; t 4.8 / 4.2; floors −1.20 to −0.68; the prior-return pattern is not monotone.
- **Table 4 (C22).** All 8 rows agree; the NEW-8 t-statistics (1.0, −1.9) agree.
- **Outliers (C25).** 2.24 to 2.26 and −0.97 to −0.98.
- **Section 3 (C26).** 2.6 bn / 51.2 bn; 18 sectors; 15%; 743 listing rows.
- **Figure 2 caption and text (C5).** The interior close-to-close bins decline from +1.10 (−6%) to −0.61 (+6%). The ceiling and floor gaps jump to +2.24 / −0.99. Squares show moves beyond 6.5% that do not close at the limit. All match the caption ("moves beyond 10% omitted", lagged weights, days up to nd−1, date clusters, normal reference, no factor).

**Equations (1)-(8) against the code** (`40_zoo.R`, `47_da_response.R`, `48_revision.R`, `42_rd.R`, `51_tick_grid_diagnostic.R`):

| Equation | What was checked | Result |
|---|---|---|
| (1) | `Cc[t]/Cc[t-1]-1` | ✓ |
| Event rule | `R ≥ 0.065` and `C ≥ H − 1e-9`; window `61:(nd-5)` | ✓ |
| (2) | 60-day mean dollar volume through d; stocks with a return and full history | ✓ |
| (3) | floor/ceiling with ±1e-9; tolerance 1e-6; tick by reference price | ✓ |
| (4) | `mk_all[t+k]` weights through d+k for Table 1; CAR = Πstock − Πmarket | ✓ |
| (5) | GAP / INTRA; market counterparts with `adv` at d | ✓ |
| Control benchmark | ≥ 30 controls, terciles from controls, equal weights | ✓ |
| (6) | `cl1` with sqrt(G/(G−1)); family p without the factor and with a normal reference; two-way `max(d + s − i, 1e-12)` | ✓ |
| Comparison regression | `vcovCL(..., type = "HC1")`: G/(G−1)·(N−1)/(N−2) | ✓ |
| (7) | rank-normal scores with average ties; cov/var slope; NeweyWest lag 4, Bartlett, no prewhitening; t(78) | ✓ |
| Characteristic filters and lookbacks | 115 days, ≥ 50 of 60 trade days, next five returns | ✓ (Appendix A as revised per NEW-11, including DOWNVOL and the BETA market, matches `40_zoo.R` lines 25-32) |
| MDE | 2.8 × SE | ✓ |
| (8) | `p.adjust("BH")` | ✓ |
| Survival rule | discovery weeks 1-39 or events up to the median date; \|t_conf\| > 1.96 with sign agreement | ✓ |
| Bonferroni | floor(0.05 / p_max) with the t reference | ✓ |

Methods text checked against the code:
- Plan deviations and the commit time stamp: commit `63bdc6d` (07:23:38) is earlier than the first commit of `40_zoo.R` (`9b8644b`, 07:36:19). ✓
- ISO calendar weeks (`%G-%V`) and 10-day blocks (`t %/% 10`). ✓
- KRX split on the date of the opening. ✓
- Outlier rule (±5 trading days around |R| > 8%). ✓

## Phase D: originality

- **Coverage.** 100% of new or modified paragraphs. The diff of `manuscript_after_round3_edits.Rmd` against `manuscript_final.Rmd` shows that nearly every prose paragraph changed in style round 2. The rest were sampled above 50%.
- **Search.** Distinctive-phrase exact searches were run, including:
  - "carry a queue of unfilled buy orders into the night";
  - "the limit acts as an amplifier";
  - "Models predict protection or distortion, depending on the source of the shock";
  - "Early empirical work infers the costs of limits from volatility and serial correlation across days";
  - "The vendor appears to adjust earlier prices for later corporate actions";
  - the next-open buyer sentence.
- **Result.** No verbatim or close match to any web source. The literature sentences track the cited abstracts in content only, at a normal paraphrase distance.
- **Self-plagiarism.** The earlier BL-K_IO manuscript is neither cited nor reused. No text from it surfaced.
- **Grades.** Every prose paragraph is ORIGINAL or COMMON_KNOWLEDGE. None is PARAPHRASE, CLOSE_MATCH or VERBATIM. Paragraphs were not counted individually.

## Phase E: claims (E1 registry, 100% verified)

Registry: high-impact claims were extracted from the abstract, the Section 1 novelty and contributions statements, the Section 2 gap and hypotheses, the H₁-H₄ resolutions, the Table 2 near-hit paragraph, the platform-change paragraphs (Sections 5 and 6), the summary paragraph, Table 5 relations, limitation (iv) and the conclusion. These were joined by every numerical sentence covered in Phase C.

| Verdict | Claims |
|---|---|
| VERIFIED | all others, including every numerical sentence covered in Phase C |
| MINOR_DISTORTION | 1 (IL-MINOR-2) |
| MAJOR_DISTORTION | 1 (IL-SERIOUS-1) |
| UNVERIFIABLE | 0 |
| UNVERIFIABLE_ACCESS | 1 (HSC band sentence, N-A1) |

Key verdicts:
- **Abstract.** Every number reproduced. The hedge is retained ("news and attention fit it as well"). VERIFIED. ("Few studies ..." is ADV-E5-1.)
- **Novelty versus Huang et al. (2001).**
  - Section 1 now says only Huang et al. describe the pattern and that the records give no magnitudes.
  - Contributions: "a pattern that Huang et al. (2001) describe qualitatively".
  - Section 2: "Apart from Huang et al. (2001), these studies do not split ...".
  - Gap paragraph: "Apart from Huang et al. (2001), none combines the two".
  - These are consistent with the record and with Table 5 ("Same timing"). The NEW-2 contradiction is gone. VERIFIED (bounded).
- **H₁-H₄ resolution.**
  - H₁: Table 1, four tests survive; the reworded NEW-9 sentence states only what is shown.
  - H₂: gap 2.24 against intraday −0.54.
  - H₃: 2.66 (14.0) and 3.14 (14.5), close-at-high comparisons.
  - H₄: −0.75 (t −2.7) against the market; −0.53 (t −1.8) against controls, not significant but not positive.
  - "The tests of H₂ to H₄ therefore rest on exploratory analyses" is disclosed.
  - "The results support H₁ to H₄" is consistent. VERIFIED.
- **Near-hit interpretation (NEW-1).**
  - The text now gives the medians (6.89 against 6.90), 83% off the grid, and "we do not read the difference as a gradient toward the limit".
  - The summary no longer says "grows as the close approaches the limit".
  - Section 4 points to Section 7.
  - Limitation (iv) gives 25/31/58% and 62/23%.
  - All of this traces to C27, reproduced independently. VERIFIED, with IL-MINOR-1 on the mechanical 100%.
- **Platform-change statement (NEW-8).**
  - Section 5 states the pre-change non-significance (t = 1.0 and −1.9) and that significance "rests mainly on the post-change events"; 71% / 58%.
  - "We cannot attribute the differences between the periods to the auction rules". VERIFIED.
  - The Section 6 policy sentence over-attributes: IL-MINOR-2.
- **Conclusion.** 26 tests; four survive FDR and the confirmation check; 1.7 / 2.2 / 0.5; 2.7 / 3.1; floor gap −1.0; 0.7. Explanations are hedged. VERIFIED.
- **Discussion.** "ends after the first day" is restricted to ceiling closes (NEW-10). The floor drift appears only before the change (−1.73 against −0.15). VERIFIED.
- **E6 (claim-strength drift, manual).** Claims touched this round, compared with `manuscript_before_round3.Rmd`:
  - Novelty: weakened, as NEW-2 authorised.
  - Near-hit gradient: withdrawn, as NEW-1 authorised.
  - H₁ wording: weakened, as NEW-9 authorised.
  - Platform stability: weakened, as NEW-8 authorised.
  - Section 6 timing: narrowed to ceilings, as NEW-10 authorised.
  No unauthorised strengthening was found. The only residual is IL-MINOR-2, a policy sentence that was not in the roadmap.

## Re-review NEW-1 to NEW-13: fix verification

| Item | Status | Evidence |
|---|---|---|
| NEW-1 near hits | RESOLVED | Table 2 paragraph, summary, Section 4 sentence and limitation (iv) all changed; numbers from C27 (`R/51_tick_grid_diagnostic.R`), reproduced independently; residual IL-MINOR-1 |
| NEW-2 novelty vs Huang et al. | RESOLVED | Sections 1 and 2 and the gap paragraph bounded and attributed (see Phase E) |
| NEW-3 caption character | RESOLVED | Figure 1 caption reads "Corwin and Schultz spread"; no `<U+...>` string in the final docx |
| NEW-4 period definition | RESOLVED | "on trading days 120, 125, and so on to day 510 ... T = 79 formation dates"; matches `ts <- seq(120, nd - 5, by = 5)` with nd = 519 |
| NEW-5 antecedent | RESOLVED | "All four event tests survive a Bonferroni correction" |
| NEW-6 Table 1 caption | RESOLVED | "we judge all three against a t distribution with G − 1 degrees of freedom" |
| NEW-7 generalisation | RESOLVED | "The band-change studies compare periods with different bands, and the cross-sectional studies sort stocks by limit exposure" |
| NEW-8 platform | RESOLVED | see Phase E |
| NEW-9 H₁ | RESOLVED | "limit closes predict the next day's abnormal return, whereas none of the 22 characteristics passes the same screen at its weekly horizon" |
| NEW-10 attribution | RESOLVED | Zeng "upper-limit hits" (see N-A3); Liang "the record we could access reports no returns after the hit"; Section 6 "after ceiling closes" |
| NEW-11 Appendix A | RESOLVED | DOWNVOL and the BETA/IVOL market text match `40_zoo.R` lines 25-32 |
| NEW-12 p-value format | RESOLVED | "at most 0.0004"; "0.00007 and 0.00040" |
| NEW-13 replication | PARTLY | `R/run_all.R` exists, lists scripts 40 → 42 → 47 → 48 → 50 → 51 → 49 → 46 and documents the line-1-44 dependency (still fragile but documented); the file is untracked (P2); evidence-file entry 2 not updated (P1) |

Comparison with the earlier integrity reports (`integrity_stage4_5_final_v2.md` and its narrow re-verification):
- N1 (priority claim) stays resolved.
- Round-2 n10 (article numbers) is still open: IL-MINOR-3.
- No regression in any item verified earlier.
- The new defect IL-SERIOUS-1 is `previously_missed`: the same sentence is in `manuscript_before_round3.Rmd`. It was missed because earlier checks trusted evidence-file entry 16.

## AI research failure-mode checklist (7 modes)

| Mode | Outcome | Evidence | Blocks? |
|---|---|---|---|
| 1 Implementation bug passing self-review | CLEAR | R/46 T1-T6 pass. 21 groups (30 quantities) reproduced from raw by independent code, including C27 and the Table 3 regression. Equations match the code. | no |
| 2 Hallucinated citation | CLEAR | 51/51 references exist and match. The one context error (IL-SERIOUS-1) is a mis-stated finding of a real paper, handled as a Phase B/E issue. | no (the issue itself blocks via the verdict) |
| 3 Hallucinated result | CLEAR | Every inline number is `r`-generated from a saved CSV. The checked values match the CSVs and the raw-data recomputation. | no |
| 4 Shortcut reliance | CLEAR | Close-at-high comparison group, control benchmark, locked days, outlier exclusion, platform split and the tick-grid diagnostic are present. The exact/near split is now correctly demoted to a data check. Limitations disclosed. | no |
| 5 Bug reframed as insight | CLEAR | No surprise language (grep: none). The former "gradient toward the limit" reading, which was a data artefact, has been withdrawn and explained by C27. This is the corrective direction. | no |
| 6 Methodology fabrication | CLEAR | Methods, Appendix A, clustering, the HC1 factor, weights and windows all match the code line by line. Plan deviations are disclosed and timestamps verified. | no |
| 7 Frame-lock | CLEAR | The novelty frame has been narrowed to a benchmarked measurement, consistent with the evidence. Rival readings are kept open, with no causal or efficiency claim. | no |

Internal-process language: a grep of the rendered text for pipeline, stage, round, reviewer, agent, Paper A/B/C, DA, integrity, checkpoint, pre-registration, surprising, unexpected, first to, novel, "to our knowledge" and "for the first time" found nothing outside the legitimate AI-use disclosure ("Claude (Anthropic)"). The analysis-plan paragraph uses "written analysis plan", not "pre-registered".

## Tool limitation disclaimer

The originality check (Phase D) used WebSearch for heuristic comparison. It is not professional plagiarism-detection software such as Turnitin or iThenticate. Coverage is limited to publicly searchable text, and there is a risk of missed detection.

Citation-context checks rest on search-returned abstracts and records, because publisher pages, SSRN, IDEAS and hsc.com.vn are behind an egress block for direct fetch. A full-text check of the access-limited items (N-A1, N-A2) is recommended before submission.

## Required to reach PASS

1. Fix IL-SERIOUS-1: the Zhang et al. (2022) sentence. Correct evidence-file entry 16 and the Theme 2 sentence as well.
2. Fix IL-MINOR-1 to IL-MINOR-4. Each is a one-line text or reference edit.
3. Re-render the manuscript, then re-verify only these five locations plus a C2 check of the changed sentences. No re-analysis is needed.

## Narrow re-verification (Stage 4.5, round 3 corrections)

Run on 2026-10-05 by an independent integrity_verification_agent with a fresh context, under the Stage 4.5 rule "FAIL -> fix -> re-verify -> PASS -> Stage 5". The scope is limited to IL-SERIOUS-1 and IL-MINOR-1 to IL-MINOR-4, plus a C2 consistency check of the changed sentences and a character check of the rendered text. No manuscript, code or data file was edited. Sources checked: `manuscript/manuscript_final.Rmd` and `manuscript/manuscript_final.docx` (both dated 2026-10-05 11:58), rendered with `pandoc -t plain --wrap=none`. `manuscript_final_styled.docx` was also rendered, and it differs from `manuscript_final.docx` only in table column widths.

### Verdict: PASS

| ID | Status | Evidence |
|---|---|---|
| IL-SERIOUS-1 | RESOLVED | Rmd line 57 and docx now read: "Zhang et al. (2022) find higher liquidity, higher volatility, and a higher probability of informed trading after the widening, and Jia et al. (2024) find lower crash risk." This session's WebSearch abstract record (ScienceDirect `S0927538X22000737`; SSRN 4019883; DOI 10.1016/j.pacfin.2022.101778) says the change "significantly improves market liquidity, increases market volatility and the probability of informed trading". The sentence matches that finding. The Section 5 citation (line 195, "changed volatility, liquidity, and execution quality") is unchanged and still correct. Evidence file `process/08_literature_review_benchmark.md`: entry 16 now records that liquidity, volatility and VPIN all rise, read as more information asymmetry, and flags the earlier error. Theme 2 (line 120) now separates "a higher probability of informed trading (Zhang et al., 2022)" from "lower information asymmetry (Jia et al., 2024)". Both are corrected. |
| IL-MINOR-1 | RESOLVED | Limitation (iv), Rmd line 228 and docx: "against 100% for stocks below 10 thousand dong, where the 0.01 tick equals the two-decimal resolution of the files and the check is uninformative". This is accurate given the round-3 check that every close in `data/raw` has at most two decimals. The 100% figure is now presented as mechanical, not as evidence. The rest of the sentence is unchanged and its rendered numbers match the round-3 table (25/31/58%, 62% vs 23%). The added clause adds no new claim. |
| IL-MINOR-2 | RESOLVED | Section 6, Rmd line 218 and docx: "... turns positive after at-the-open orders lose priority (Table 4). This is consistent with auction design shaping how the opening absorbs overnight pressure, but the market period changed at the same time, so the split cannot isolate the auction rules (Section 5)." This is consistent with the Section 5 statement "We cannot attribute the differences between the periods to the auction rules." The Table 4 numbers cited in Section 5 are unchanged (floor gap −0.42 → −1.37, intraday after floor closes 0.64). |
| IL-MINOR-3 | RESOLVED | Huang, Liu and Shu (2023): `*Pacific-Basin Finance Journal, 82*, 102176`. WebSearch confirms the journal PDF header "Pacific-Basin Finance Journal 82 (2023) 102176" and ScienceDirect `S0927538X23002470`. Lin, Qiu and Zheng (2023): `*Journal of Banking & Finance, 150*, 106818`. WebSearch confirms JBF 150 (May 2023), article 106818, DOI 10.1016/j.jbankfin.2023.106818 (ScienceDirect `S0378426623000432`; IDEAS `jbfina/v150y2023ics0378426623000432`). Both article numbers are correct. |
| IL-MINOR-4 | RESOLVED | "Gu, M., Hu, Y., & Xiong, Z. (2025)" (Rmd line 284) now precedes "Gutierrez, R. C., Jr., & Kelley, E. K. (2008)" (line 286). A scripted surname-key check of the whole rendered reference list (accents folded, punctuation stripped) found no adjacent pair out of APA alphabetical order. |

Changed-sentence C2 check: no new inconsistency was found.
- The new Zhang wording does not conflict with the Section 5 citation or with Table 5.
- The Section 6 sentence now defers to Section 5 instead of going beyond it.
- The limitation (iv) clause is consistent with the Table 2 paragraph, which already treats exact and near hits as a data check.

Rendered-character check: `manuscript_final.docx` contains no U+FFFD and no `<U+...>` strings.
- The only non-ASCII characters in the changed lines are no-break spaces in "et al." citations, which are intended.
- The reference list contains only en dashes, curly quotes, "ü", an ellipsis, and "×" and "²".
- The thin spaces (U+2005/U+2006) occur in the Appendix A math text, not in the references.

Remaining issues: none blocking. Advisory only (A2, not a defect under this round's correction): the Lin et al. (2023) and Huang et al. (2023) entries still carry no DOI. The round-3 suggestion for Lin offered `https://doi.org/10.1016/j.jbankfin.2023.106818`, and APA 7 prefers a DOI when one exists. Several other entries also lack DOIs (e.g., Hou et al., 2020; Zhang et al., 2022), so DOI completeness can be handled as a single pass at Stage 5. The earlier notes N-A1 to N-A3 and the process notes stand unchanged.

Next step: Stage 4.5 PASS -> Stage 5 (FINALIZE).
