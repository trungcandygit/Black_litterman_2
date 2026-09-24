"""Stage 4.5 integrity-correction round 1 (ARS #390 integrity variant).

Builds integrity-correction-list/1.0 and a patch 1.1 (authorization_context =
integrity_correction) against the anchored manuscript_v4.md. Every edit is an
exact substring replacement asserted to match once inside its block.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v4.md"
raw = BASE.read_bytes()
text = raw.decode("utf-8")
parts = re.split(r"<!--block:(B\d{4})-->\n", text)
blocks = {parts[i]: parts[i + 1].rstrip("\n") for i in range(1, len(parts), 2)}
manifest = json.loads((HERE / "manuscript_v4.md.block-manifest.json").read_text())
old_hash = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}

# ------------------------------------------------------------------ issue list
ISSUES = [
    ("IL-SERIOUS-1", "Phase B MAJOR_DISTORTION: Gregoriou & Nguyen (2010) find no significant effect of FTSE 100 deletions on investment; the manuscript says they find the 'mirror pattern'.", ["B0022"]),
    ("IL-SERIOUS-2", "Phase B MAJOR_DISTORTION: Hegde & McDermott (2003) measure a sustained liquidity gain over months, not 'for years'.", ["B0009"]),
    ("IL-MEDIUM-1", "Phase C: named-but-excluded announcement-week CAR range stated as 2.3% to 6.3%; Table 4 panel C maximum is 6.2%.", ["B0084"]),
    ("IL-MEDIUM-2", "Phase C: effective-date constituent CAR range stated as -0.5% to 1.0%; Table 4 panel A maximum is 0.9%.", ["B0076", "B0094"]),
    ("IL-MEDIUM-3", "Phase C: matched-sample spread rise stated as 0.14 to 0.20 points (unweighted matched sample); the weighted matched estimates in Table 2 column 6 are 0.11 to 0.14.", ["B0105"]),
    ("IL-MEDIUM-4", "Phase C / reproduction: matched-sample pre-trend p = 0.056 depends on residual df; rerun with G-1 cluster df (consistent with clustered t-tests) gives p = 0.092.", ["B0068"]),
    ("IL-MEDIUM-5", "Phase E / internal consistency: Section 4.4 heading, 'This supports H4' and takeaway assert monotone gains by segment; body says the liquidity gain is not monotone and the three-stock segments are descriptive.", ["B0096", "B0098", "B0102"]),
    ("IL-MEDIUM-6", "Phase B UNVERIFIABLE: the 30 June 2026 data date is attributed to the FTSE FAQ and VIR, neither of which states it; the date follows from the GEIS ground rules (September review liquidity data to the last business day of June).", ["B0011", "B0018", "B0168"]),
    ("IL-MEDIUM-7", "Phase A2: FTSE FAQ reference 'Version 1.3, August 2026' not locatable; indexed versions are v1.0 (Nov 2025) and v1.2 (Apr 2026). Drop unverifiable version/month; use the published title.", ["B0169"]),
    ("IL-MEDIUM-8", "Phase B UNVERIFIABLE: 'FTSE's own illustration' of a 49% investability weight entering at 4.9% is not in the FAQ; state it as the paper's own arithmetic.", ["B0018"]),
    ("IL-MEDIUM-9", "Phase A2: LSEG (2025) and LSEG (2026) press-release titles are not the published headlines.", ["B0176", "B0177"]),
    ("IL-MEDIUM-10", "Phase B UNVERIFIABLE_ACCESS: the square-root-of-window scaling is attributed to Brown & Warner (1985); attribute only the portfolio (dependence) approach and state the scaling as the paper's assumption.", ["B0044", "B0082"]),
    ("IL-MEDIUM-11", "Mode 6 / Phase C: Data availability lists four of six scripts (omits analysis_revision2.R, figure2.R) and no software versions; reproduction from raw data now documented.", ["B0150"]),
    ("IL-MEDIUM-12", "Phase D CLOSE_MATCH: 'country reclassification events show distinct return and volume effects' repeats 8 of 9 words of the Biktimirov & Afego (2026) abstract.", ["B0024"]),
    ("IL-MEDIUM-13", "Phase E uncited assertion / E5 nearest prior work: 'Most studies of market reclassification also work with aggregate indices' has no citation; Burnham, Gakidis & Wurgler (2018, FAJ) is the nearest country-level study of MSCI reclassifications and is not cited.", ["B0009", "B0024", "B0161"]),
    ("IL-MEDIUM-14", "Phase E / E6 ADV-E6-5: 'reliable announcement-week price response under three of four benchmarks' applies the defined term 'reliable' (all four) to a result that fails it.", ["B0132"]),
    ("IL-MEDIUM-15", "E6 ADV-E6-1/3/4/6: restore dropped causal caveat (B0013), hedge the unobserved-characteristics reading (B0084), restrict the selection-timing claim to GEE (B0122), restore the portfolio qualifier (B0084, B0137).", ["B0013", "B0084", "B0122", "B0137"]),
    ("IL-MINOR-1", "Phase B MINOR_DISTORTION: Amihud (2002) defines the ratio on absolute return over dollar volume; the paper adapts it (log return, VND).", ["B0041"]),
    ("IL-MINOR-2", "Phase B MINOR: Shleifer (1986) reports excess returns that do not disappear for at least ten days ('permanent' overstates); Harris & Gurel (1986) measure effects after announcement, not specifically on the effective date; Hegde & McDermott attribute the gain mainly to lower direct trading costs.", ["B0021"]),
    ("IL-MINOR-3", "Phase B MINOR: Raddatz et al. (2017) evidence is country-level; the sentence applies it to stock-level attention in a three-stock segment.", ["B0138"]),
    ("IL-MINOR-4", "Phase B MINOR: The Investor (2026a) is a March 2026 article; it supports the list size and data date, not the November 2025 appearance.", ["B0018"]),
    ("IL-MINOR-5", "Phase B MINOR: FTSE's investability weight reflects free float and foreign-ownership limits, not free float alone.", ["B0018"]),
    ("IL-MINOR-6", "Phase B MINOR: Vietnam-specific rebalancing facts are cited to Harris & Gurel (1986) instead of FTSE Russell (2026)/VIR (2026).", ["B0094"]),
    ("IL-MINOR-7", "Phase B MINOR: LSEG (2026) lists the removal of pre-funding among several reforms, for foreign institutional investors; 'credits' overstates.", ["B0192"]),
    ("IL-MINOR-8", "Phase B MINOR: 'seven years' on the watch list cites only the 2018 start; add LSEG (2025) for the end point.", ["B0055"]),
    ("IL-MINOR-9", "Phase C MINOR: Table 8 note lists EIB among bank constituents; EIB is in the ITT group only.", ["B0115"]),
    ("IL-MINOR-10", "Phase E MINOR: B0064 'confirm' sits beside the rejected ITT pre-trend test; B0135 'only the confirmation gain lasted' lacks the three-of-four qualifier; B0076 'up to three times' imprecise (max 2.9).", ["B0064", "B0135", "B0076"]),
]

# ------------------------------------------------------------------ edits
EDITS = {  # block -> list of (old, new)
    "B0009": [
        ("raise trading activity and narrow spreads for years (Hegde & McDermott, 2003)",
         "raise trading activity and narrow spreads persistently (Hegde & McDermott, 2003)"),
        ("Most studies of market reclassification also work with aggregate indices or country-level flows, which cannot",
         "Most studies of market reclassification also work with aggregate indices or country-level flows (e.g., Burnham et al., 2018; Raddatz et al., 2017), which cannot"),
    ],
    "B0011": [
        ("FTSE selected the final constituents on data as of 30 June 2026 (FTSE Russell, 2026), in the middle",
         "FTSE selected the final constituents at its September 2026 review, whose liquidity screen uses data up to the last business day of June 2026 (FTSE Russell, 2025), in the middle"),
    ],
    "B0013": [
        ("This last result is why we report intention-to-treat effects beside the constituent effects.",
         "This last result limits causal readings of the constituent estimates and is why we report intention-to-treat effects beside them."),
    ],
    "B0018": [
        ("A preliminary list of 28 names, screened on data as of 31 December 2024, appeared in November 2025 (Viet Nam News, 2025; The Investor, 2026a).",
         "A preliminary list of 28 names appeared in November 2025 (Viet Nam News, 2025); it was screened on data as of 31 December 2024 (The Investor, 2026a)."),
        ("with 27 constituents, selected on data as of 30 June 2026 and effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026).",
         "with 27 constituents, effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026); under FTSE's ground rules the September review screens liquidity on data up to the last business day of June (FTSE Russell, 2025)."),
        ("using each security's investability weight (free float) in the liquidity test (FTSE Russell, 2026).",
         "using each security's investability weight, which reflects its free float and foreign-ownership limits, in the liquidity test (FTSE Russell, 2026)."),
        ("The same investability weight scales a security's weight in the index: FTSE's own illustration phases in a security with a 49% investability weight at 4.9% after the first tranche and at 49% after the last (FTSE Russell, 2026).",
         "The same investability weight scales a security's weight in the index, and each tranche applies a fraction of it: a security with a 49% investability weight enters at 4.9% after the first tranche (10% of 49%) and at 49% after the last."),
    ],
    "B0021": [
        ("additions force passive funds to buy on the effective date, which produces temporary volume and price effects that reverse afterwards (Harris & Gurel, 1986).",
         "additions lead index funds to buy, which produces temporary volume and price effects that reverse afterwards (Harris & Gurel, 1986)."),
        ("Shleifer (1986) interprets permanent price effects as evidence",
         "Shleifer (1986) interprets excess returns that do not reverse after inclusion as evidence"),
        ("which they attribute to more information and more trading interest.",
         "which they attribute mainly to lower direct trading costs."),
    ],
    "B0022": [
        ("and Gregoriou and Nguyen (2010) find the mirror pattern for FTSE 100 deletions.",
         "whereas Gregoriou and Nguyen (2010) find no significant effect of FTSE 100 deletions on investment."),
    ],
    "B0024": [
        ("an MSCI index change even moved currency values through this channel (Hau et al., 2010).",
         "an MSCI index change even moved currency values through this channel (Hau et al., 2010). At the country level, prices of markets that MSCI reclassifies overshoot between the announcement and the effective date and largely revert within a year (Burnham et al., 2018)."),
        ("Additions earn persistent price gains, country reclassification events show distinct return and volume effects, and the authors attribute the gains to institutional demand rather than to trading pressure or liquidity.",
         "They find persistent price gains for additions and separate return and trading-volume responses when a country changes class, and they trace the gains to institutional demand rather than to trading pressure or liquidity."),
    ],
    "B0041": [
        ("The Amihud (2002) ratio for stock i on day t is",
         "Following Amihud (2002), who divides the absolute daily return by dollar volume, we define illiquidity for stock i on day t with the log return and traded value in VND as"),
    ],
    "B0044": [
        ("dividing the portfolio CAR by the standard deviation of daily portfolio abnormal returns in an estimation window, scaled by the square root of the window length (Brown & Warner, 1985).",
         "which addresses cross-sectional dependence (Brown & Warner, 1985): the portfolio CAR is divided by the standard deviation of daily portfolio abnormal returns in an estimation window, multiplied by the square root of the number of days in the event window, which assumes independent daily abnormal returns."),
    ],
    "B0055": [
        ("Vietnam sat on the FTSE watch list for seven years (FTSE Russell, 2018),",
         "Vietnam sat on the FTSE watch list for seven years (FTSE Russell, 2018; LSEG, 2025),"),
    ],
    "B0064": [
        ("The ITT estimates in Table 3 confirm that the decline is not an artefact of FTSE's later choice.",
         "The ITT estimates in Table 3 indicate that the decline is not an artefact of FTSE's later choice."),
    ],
    "B0068": [
        ("in the matched sample it does not reject at 5% (F = 1.72, p = 0.056).",
         "in the matched sample it does not reject at 5% (F = 1.72, p = 0.092). These p-values use the number of stock clusters minus one as denominator degrees of freedom."),
    ],
    "B0076": [
        ("Around the effective date the three-day CAR lies between -0.5% and 1.0% and is never significant.",
         "Around the effective date the three-day CAR lies between -0.5% and 0.9% and is never significant."),
        ("are up to three times larger.", "are up to 2.9 times larger."),
    ],
    "B0082": [
        ("Portfolio t = CAR divided by the standard deviation of daily portfolio abnormal returns in the estimation window, times the square root of the window length (Brown & Warner, 1985).",
         "Portfolio t = CAR / (σ × √L), where σ is the standard deviation of daily portfolio abnormal returns in the estimation window and L the number of days in the event window; the portfolio approach follows Brown and Warner (1985)."),
    ],
    "B0084": [
        ("The named-but-excluded stocks gained 2.3% to 6.3% in the announcement week",
         "The named-but-excluded stocks gained 2.3% to 6.2% in the announcement week"),
        ("so the announcement-week gain of stocks that later appeared on the lists reflects characteristics investors could observe, such as size and liquidity, rather than the lists themselves.",
         "so the announcement-week gain of stocks that later appeared on the lists suggests that investors responded to characteristics they could observe, such as size and liquidity, rather than to the lists themselves."),
        ("By the confirmation the preliminary list was public, and only stocks that went on to be included gained.",
         "By the confirmation the preliminary list was public, and only the portfolio of stocks that went on to be included gained."),
    ],
    "B0094": [
        ("they bought the first tranche of constituents at the closing price of 18 September, and nothing obliged them to trade the stocks FTSE had named and passed over (Harris & Gurel, 1986).",
         "they bought the first tranche of constituents at the closing price of 18 September (FTSE Russell, 2026; VIR, 2026), and nothing obliged them to trade the stocks FTSE had named and passed over."),
        ("the three-day CAR around the effective date is between -0.5% and 1.0% under every benchmark (Table 4)",
         "the three-day CAR around the effective date is between -0.5% and 0.9% under every benchmark (Table 4)"),
    ],
    "B0096": [
        ("### 4.4 The gains and the rebalancing surge rise with FTSE size segment",
         "### 4.4 The rebalancing surge rises with FTSE size segment"),
    ],
    "B0098": [
        ("0.98 for mid-capitalization and 0.65 for small-capitalization constituents. This supports H4.",
         "0.98 for mid-capitalization and 0.65 for small-capitalization constituents. This ordering is consistent with H4, although the two upper segments contain three stocks each."),
    ],
    "B0102": [
        ("**Takeaway.** Index weight scales the rebalancing trade;",
         "**Takeaway.** The rebalancing trade was largest for the constituents with the largest index weights;"),
    ],
    "B0105": [
        ("and by 0.14 to 0.20 points in the matched sample,",
         "and by 0.11 to 0.14 points in the weighted matched sample,"),
    ],
    "B0115": [
        ("Banks and securities firms are VCB, BID, VPB, HDB, STB, SHB, SSB, MSB and EIB, and SSI, VCI, VIX, VND and HCM.",
         "Banks are VCB, BID, VPB, HDB, STB, SHB, SSB and MSB among constituents and EIB in the ITT group; securities firms are SSI, VCI, VIX, VND and HCM."),
    ],
    "B0122": [
        ("Their gains are concentrated in two stocks, and the timing of those gains points to selection.",
         "Their gains are concentrated in two stocks, GEE and BSR; for GEE the timing of the gain points to selection, for BSR it does not."),
    ],
    "B0132": [
        ("and a reliable announcement-week price response under three of four benchmarks.",
         "and an announcement-week price response significant under three of four benchmarks."),
    ],
    "B0135": [
        ("and only the confirmation gain lasted.",
         "and only the confirmation gain lasted, under three of four benchmarks."),
        ("scaled by index weight and absent for excluded stocks,",
         "largest for the largest constituents and absent for excluded stocks,"),
    ],
    "B0137": [
        ("At the confirmation, once the preliminary list was public, only stocks that went on to be included gained.",
         "At the confirmation, once the preliminary list was public, only the portfolio of stocks that went on to be included gained."),
    ],
    "B0138": [
        ("which suggests that investors weighted their attention by expected index weight, as benchmark-driven allocations would (Raddatz et al., 2017).",
         "which is consistent with investors weighting their attention by expected index weight; at the country level, benchmark weights shape fund allocations (Raddatz et al., 2017). With three stocks in that segment, we read this pattern as descriptive."),
    ],
    "B0150": [
        ("The R code that reproduces all tables and figures (code/analysis.R, code/analysis_extensions.R, code/analysis_revision.R, code/figure1.R) is available from the corresponding author and will be deposited in a public repository on acceptance.",
         "The downloaded daily files and the R code that reproduces all tables and figures (code/analysis.R, code/analysis_extensions.R, code/analysis_revision.R, code/analysis_revision2.R, code/figure1.R, code/figure2.R; R 4.3.3, fixest 0.14.2, MatchIt 4.5.5, data.table 1.14.10) are available from the corresponding author and will be deposited in a public repository on acceptance."),
    ],
    "B0169": [
        ("FTSE Russell. (2026, August). *Reclassification of Vietnam from frontier to secondary emerging market status: Frequently asked questions* (Version 1.3).",
         "FTSE Russell. (2026). *Reclassification of Vietnam to secondary emerging market status: FAQ*."),
    ],
    "B0176": [
        ("*FTSE Russell country classification: September 2025 review* [Press release].",
         "*FTSE Russell announces results of September 2025 semi-annual country classification review for equities and fixed income* [Press release]."),
    ],
    "B0177": [
        ("*FTSE Russell announces results of the March 2026 semi-annual country classification review* [Press release].",
         "*FTSE Russell announces results of March 2026 semi-annual country classification review for equities and fixed income* [Press release]."),
    ],
    "B0192": [
        ("LSEG (2026) credits the removal of pre-funding requirements for foreign investors for Vietnam's upgrade, and that reform applies to every stock foreign investors can buy.",
         "LSEG (2026) lists the removal of pre-funding requirements for foreign institutional investors among the reforms behind Vietnam's upgrade, and that reform applies to every stock foreign investors can buy."),
    ],
}
INSERTS = {  # anchor block -> new block text
    "B0161": "Burnham, T. C., Gakidis, H., & Wurgler, J. (2018). Investing in the presence of massive flows: The case of MSCI country reclassifications. *Financial Analysts Journal, 74*(1), 77–87. https://doi.org/10.2469/faj.v74.n1.8",
    "B0168": "FTSE Russell. (2025). *FTSE Global Equity Index Series ground rules* (v13.4). https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf Accessed 24 September 2026.",
}

issue_ids_for_block = {}
for cid, _, targets in ISSUES:
    for t in targets:
        issue_ids_for_block.setdefault(t, []).append(cid)

ops = []
for bid in sorted(set(EDITS) | set(INSERTS)):
    ids = issue_ids_for_block[bid]
    if bid in EDITS:
        new = blocks[bid]
        for old, rep in EDITS[bid]:
            assert new.count(old) == 1, (bid, old)
            new = new.replace(old, rep)
        ops.append({"op": "replace_block", "block_id": bid, "old_hash": old_hash[bid], "new_text": new,
                    "roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})
    else:
        ops.append({"op": "insert_after", "block_id": bid, "old_hash": old_hash[bid], "new_text": INSERTS[bid],
                    "roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})

base_sha = hashlib.sha256(raw).hexdigest()
def op_for(bid):
    return "insert_after" if bid in INSERTS else "replace_block"
issue_list = {
    "schema_version": "integrity-correction-list/1.0",
    "revision_round": 3,
    "base_draft_sha256": base_sha,
    "issues": [{"correction_id": c, "description": d,
                "proposed_targets": [{"block_id": t, "allowed_operations": [op_for(t)]} for t in sorted(ts)]}
               for c, d, ts in ISSUES],
}
(HERE / "integrity_correction_list_round1.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
issue_list_sha = hashlib.sha256((HERE / "integrity_correction_list_round1.json").read_bytes()).hexdigest()
patch = {
    "patch_format_version": "1.1",
    "authorization_context": "integrity_correction",
    "revision_round": 3,
    "base_draft_hash": manifest["base_draft_hash"],
    "issue_list_sha256": issue_list_sha,
    "emitted_by": "draft_writer_agent",
    "ops": ops,
}
(HERE / "integrity_patch_round1.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), "issues", len(ISSUES))
print("issue_list_sha256", issue_list_sha)
print("patch_sha256", hashlib.sha256((HERE / "integrity_patch_round1.json").read_bytes()).hexdigest())
