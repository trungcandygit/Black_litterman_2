"""Stage 4' (revision round 2) under the #390/#670 patch protocol.
Builds: revision-roadmap/1.0, claim-surface-manifest/1.0, author-adjudication input, patch 1.1 ops.
All replacement texts are fixed here; numbers come from output/revision and output/revision2 CSVs."""
import csv, hashlib, json, sys
from pathlib import Path

ARS = Path("/Users/nguyenvantrung/academic-research-skills")
sys.path.insert(0, str(ARS))
from scripts._block_parser import parse_document, base_draft_hash

PROJ = Path("/Users/nguyenvantrung/Downloads/Python for Algorithmic Trading/NCKH/BAI FTSE2/FTSE2_new")
D = PROJ / "ars/stage4prime"
AUTH = D / "authority"
BASE = D / "manuscript_v3.anchored.md"
MANI = D / "manuscript_v3.anchored.md.block-manifest.json"

base_raw = BASE.read_bytes(); base = base_raw.decode("utf-8")
doc = parse_document(base); blocks = doc.block_by_id()
def txt(bid):
    b = blocks[bid]; return base[b.span[0]:b.span[1]]
def sha(b): return hashlib.sha256(b).hexdigest()
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
def rd(p): return list(csv.DictReader(open(PROJ / p)))
def star(p):
    p = float(p); return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
def f(e, s, p, d=3): return f"{float(e):.{d}f}{star(p)} ({float(s):.{d}f})"
def get(rows, spec, term):
    for r in rows:
        if r["spec"] == spec and r["term"] == term: return r
    raise KeyError((spec, term))
def sub(bid, old, new):
    t = txt(bid); assert t.count(old) == 1, (bid, old[:60]); return t.replace(old, new)

new = {}      # block_id -> replacement text
ins = {}      # block_id -> inserted text (insert_after)

# ---------------------------------------------------------------- tables
t2 = rd("output/revision/t2_baseline_clean.csv"); mw = rd("output/revision2/t_matched_weighted.csv")
lab = {"P1": "Constituent × Announcement", "P2": "Constituent × Confirmation", "P3": "Constituent × List and rebalancing"}
rows = []
for k in ["P1", "P2", "P3"]:
    c = [f(get(t2, f"clean_{y}", f"treated:{k}")["est"], get(t2, f"clean_{y}", f"treated:{k}")["se"], get(t2, f"clean_{y}", f"treated:{k}")["p"], d) for y, d in [("lamihud", 3), ("lval", 3), ("cs", 4)]]
    c += [f(get(mw, f"matched_weighted_{y}", f"treated:{k}")["est"], get(mw, f"matched_weighted_{y}", f"treated:{k}")["se"], get(mw, f"matched_weighted_{y}", f"treated:{k}")["p"], d) for y, d in [("lamihud", 3), ("lval", 3), ("cs", 4)]]
    rows.append(f"| {lab[k]} | " + " | ".join(c) + " |")
new["B0062"] = "\n".join([
    "| | (1) log Amihud | (2) log trading value | (3) CS spread | (4) log Amihud | (5) log trading value | (6) CS spread |",
    "|---|---|---|---|---|---|---|",
    "| Sample | All never-named controls | All never-named controls | All never-named controls | Matched 3:1, weighted | Matched 3:1, weighted | Matched 3:1, weighted |",
    *rows,
    "| Stock and week FE | Yes | Yes | Yes | Yes | Yes | Yes |",
    "| Observations | 34,369 | 34,369 | 34,369 | 4,751 | 4,751 | 4,751 |"])
new["B0063"] = sub("B0063", "Source: output/revision/t2_baseline_clean.csv.",
    "Columns 4 to 6 weight each of the 24 distinct matched controls by its matching weight (three controls per constituent, nearest-neighbour propensity score, with replacement). Sources: output/revision/t2_baseline_clean.csv, output/revision2/t_matched_weighted.csv.")

car = rd("output/revision2/t3_car_portfolio_clean_est.csv")
EV = [("Announcement", "Announcement, 7 Oct 2025"), ("Confirmation", "Confirmation, 7 Apr 2026"), ("Constituent list", "Constituent list, 21 Aug 2026"), ("Effective date", "Effective date, 21 Sep 2026")]
B4 = ["ew", "matched_w", "topsize", "market_model"]
def car_rows(group, crosst):
    out = []
    for e, elab in EV:
        for w in ["[-1,1]", "[-1,5]", "[0,20]"]:
            rs = {r["benchmark"]: r for r in car if r["group"] == group and r["event"] == e and r["window"] == w}
            if not rs: continue
            cells = [f"{100*float(rs[b]['car']):.1f}% ({float(rs[b]['t_portfolio']):.2f})" for b in B4]
            wl = w.replace(",1]", ",+1]").replace(",5]", ",+5]").replace(",20]", ",+20]")
            line = f"| {elab if w == '[-1,1]' else ''} | {wl} | " + " | ".join(cells)
            if crosst: line += f" | {float(rs['ew']['t_cross']):.2f}"
            out.append(line + " |")
    return out
new["B0079"] = "\n".join(["| Event | Window | Never-named, equal-weighted | Matched controls, weighted | Large never-named stocks | Market model | Cross-sectional t (first benchmark) |",
                          "|---|---|---|---|---|---|---|", *car_rows("constituent", True)])
new["B0080"] = "Panel B. Intention-to-treat group (27 stocks on the preliminary list): CAR (portfolio t) by benchmark"
new["B0081"] = "\n".join(["| Event | Window | Never-named, equal-weighted | Matched controls, weighted | Large never-named stocks | Market model |",
                          "|---|---|---|---|---|---|", *car_rows("itt_nov_list", False)])
ins["B0081"] = "\n\n".join(["Panel C. Named-but-excluded stocks (14): CAR (portfolio t) by benchmark",
    "\n".join(["| Event | Window | Never-named, equal-weighted | Matched controls, weighted | Large never-named stocks | Market model |",
               "|---|---|---|---|---|---|", *car_rows("named_excluded", False)])])
new["B0082"] = ("*Notes*: CAR = sum of daily portfolio abnormal returns. Portfolio t = CAR divided by the standard deviation of daily portfolio abnormal returns in the estimation window, times the square root of the window length (Brown & Warner, 1985). "
    "The estimation window runs from trading day -130 to -11 and excludes days -1 to +20 around every earlier disclosure (120 days for the announcement, 98 for the confirmation and the constituent list, 89 for the effective date). "
    "Market-model parameters are estimated per stock over the same window against the never-named benchmark; the matched benchmark weights controls by their matching weights. "
    "Windows are pre-specified and identical for every event; a CAR is called robust when it is significant at 5% under all four benchmarks. The effective-date windows beyond +1 are not reported because the data end on 23 September 2026. Source: output/revision2/t3_car_portfolio_clean_est.csv.")

seg_old = txt("B0100").split("\n")
seg_new = []
for line in seg_old:
    cells = line.split("|")
    if len(cells) > 4 and line.startswith("| log") :
        cells[2] = cells[2].replace("***", "").replace("**", "").replace("*", "")
        cells[3] = cells[3].replace("***", "").replace("**", "").replace("*", "")
    seg_new.append("|".join(cells))
new["B0100"] = "\n".join(seg_new)

t7 = rd("output/revision/t7_robustness.csv"); sec = rd("output/revision2/t_sector.csv"); drift = rd("output/revision2/t_post_drift.csv")
def r3(rows_, spec, var="treated"):
    return " | ".join(f(get(rows_, spec, f"{var}:P{k}")["est"], get(rows_, spec, f"{var}:P{k}")["se"], get(rows_, spec, f"{var}:P{k}")["p"]) for k in (1, 2, 3))
dr = {r["term"]: r for r in drift if r["part"] == "coef"}
drift_row = " | ".join(f(dr[f"treated:P{k}"]["est"], dr[f"treated:P{k}"]["se"], dr[f"treated:P{k}"]["p"]) for k in (1, 2, 3))
t8 = txt("B0114").split("\n")
out8 = []
for line in t8:
    if line.startswith("| Matched sample with constituent-specific trend"):
        line = f"| Weighted matched sample with constituent-specific trend | {r3(mw, 'matched_weighted_trend')} | 4,751 |"
        out8.append(line)
        out8.append(f"| Constituent-specific drift after the announcement | {drift_row} | 34,369 |")
        continue
    if line.startswith("| Controlling for volatility"):
        out8.append(line)
        out8.append(f"| Excluding bank and securities-firm constituents (11 remain) | {r3(sec, 'constituents_ex_fin')} | 33,082 |")
        out8.append(f"| ITT group excluding banks and securities firms (19 remain) | {r3(sec, 'itt_ex_fin', 'itt')} | 33,874 |")
        continue
    if line.startswith("| Wild cluster bootstrap p-value, matched sample (48 clusters)"):
        line = line.replace("matched sample (48 clusters)", "unweighted matched sample (48 clusters)")
    out8.append(line)
new["B0114"] = "\n".join(out8)
new["B0115"] = sub("B0115", "Sources: output/revision/t7_robustness.csv,",
    "The drift row adds a constituent-specific linear trend in weeks since the announcement (-0.012 per week, p = 0.002). Banks and securities firms are VCB, BID, VPB, HDB, STB, SHB, SSB, MSB and EIB, and SSI, VCI, VIX, VND and HCM. Sources: output/revision/t7_robustness.csv, output/revision2/t_matched_weighted.csv, output/revision2/t_post_drift.csv, output/revision2/t_sector.csv,")

new["B0128"] = "\n".join(l if not l.startswith("| Added Apr 2026") else "| Added Apr 2026, not included: GEE, BSR (point estimates only) | -1.15 | -1.67 | -2.51 |" for l in txt("B0128").split("\n"))

# ---------------------------------------------------------------- prose
new["B0003"] = ("FTSE Russell reclassified Vietnam from frontier to secondary emerging status in four public steps between October 2025 and September 2026. Using daily data on 366 stocks listed on the Ho Chi Minh City Stock Exchange, we trace liquidity and prices at each step. "
    "Because FTSE chose the final constituents on mid-2026 data, we estimate effects both for the 24 eventual constituents and, as an intention-to-treat design, for the 27 stocks FTSE had screened as eligible on data from before the announcement. "
    "Relative to never-named stocks, the Amihud illiquidity of the pre-announcement eligible group fell by 24%, 43% and 56% after the announcement, the confirmation and the constituent list; for the constituents the declines were 32%, 59% and 68%. "
    "Constituents earned cumulative abnormal returns of 3.9% to 7.8% in the week around the announcement and 2.7% to 4.5% around the confirmation, significant under four benchmarks and a test that allows for the common event dates; the constituent list and the effective date of the first 10% index tranche produced no robust price effect. "
    "Trading value surged at the rebalancing close for included stocks but not for stocks FTSE named and then excluded. The liquidity and price response to Vietnam's upgrade came with FTSE's disclosures, before the first index tranche took effect.")
new["B0007"] = ("Vietnam's market upgrade raised the liquidity of likely index stocks before the first index tranche took effect. When FTSE Russell reclassified Vietnam from frontier to secondary emerging status, the Amihud (2002) illiquidity of the 27 stocks FTSE had screened as eligible on 2024 data fell relative to never-named stocks on the Ho Chi Minh City Stock Exchange (HOSE) by 43% after FTSE confirmed the upgrade in April 2026 and by 56% after it named the constituents in August 2026. "
    "For the stocks FTSE finally included, the declines were 59% and 68%. On the effective date, which carried the first 10% of the eventual index weight, prices did not move; trading value surged at the rebalancing close for included stocks only.")
new["B0012"] = ("We estimate difference-in-differences and event-study regressions on 35,752 stock-weeks and on daily returns from October 2024 to September 2026. The main liquidity measure is the Amihud ratio computed on traded value in Vietnamese dong; we also report trading value, the Corwin and Schultz (2012) high-low spread, volatility and abnormal returns. "
    "For prices, we pre-specify the same three windows for every disclosure, test cumulative abnormal returns at the portfolio level, which accounts for the common event dates (Brown & Warner, 1985), and call an effect robust only if it is significant at 5% under all four benchmarks we use.")
new["B0013"] = ("The paper makes one contribution: it decomposes the stock-level liquidity and price effects of a frontier-to-emerging reclassification by disclosure stage, with the treatment group also defined on information available before the upgrade. Four findings support the decomposition. "
    "First, the illiquidity of the pre-announcement eligible group fell by 0.27, 0.55 and 0.81 log points across the announcement, confirmation and constituent-list windows, about two thirds of the 0.39, 0.89 and 1.13 log-point declines for the final constituents (Tables 2 and 3); the confirmation brought a discrete step beyond a gradual post-announcement drift, the constituent list did not. "
    "Second, prices rose robustly in the announcement week and at the confirmation, and the confirmation gain persisted under three of four benchmarks; the constituent list and the effective date produced no robust price effect (Table 4). "
    "Third, trading value rose by 0.79 log points relative to never-named stocks at the rebalancing close, rising with FTSE size segment, while named-but-excluded stocks showed no surge (Tables 5 and 6). "
    "Fourth, FTSE's eligibility lists partly followed rising liquidity: GEE, added in April 2026, had become more liquid during the data window FTSE screened (Table 9). This last result is why we report intention-to-treat effects beside the constituent effects.")
new["B0018"] = ("Between these dates the financial press reported FTSE's lists of eligible stocks. A preliminary list of 28 names, screened on data as of 31 December 2024, appeared in November 2025 (Viet Nam News, 2025; The Investor, 2026a). A list of 32 names, screened on data as of 31 December 2025, followed in April 2026; it dropped Petrolimex (PLX) and added BID, FPT, NVL, GEE and BSR (The Investor, 2026b). "
    "On Friday 21 August 2026 FTSE published the September semi-annual review with 27 constituents, selected on data as of 30 June 2026 and effective after the close of 18 September 2026 (FTSE Russell, 2026; VIR, 2026). "
    "FTSE screened Vietnamese securities as non-constituents on its liquidity, minimum-size and foreign-headroom screens, using each security's investability weight (free float) in the liquidity test (FTSE Russell, 2026). "
    "The same investability weight scales a security's weight in the index: FTSE's own illustration phases in a security with a 49% investability weight at 4.9% after the first tranche and at 49% after the last (FTSE Russell, 2026). A constituent's index weight, and the passive demand it attracts, therefore rises with its free-float market capitalization. Appendix Table A.2 lists every stock by list.")
new["B0025"] = txt("B0025") + " Beyond Dong et al. (2023), we did not locate a verified stock-level study of liquidity around the MSCI inclusion of China A-shares, so our comparison with that episode rests on their evidence alone."
new["B0035"] = sub("B0035", "(Appendix Table A2)", "(Appendix Table A.2)") + (" BSR, one of the named-but-excluded stocks, traded on the UPCoM market until 6 January 2025 and on HOSE from 17 January 2025 (VietnamPlus, 2024), so its pre-period series spans two venues; Section 5.2 reports results without it.")
new["B0044"] = ("For prices, the daily abnormal return of stock i is its log return minus a benchmark return. We use four benchmarks: the equal-weighted mean of the 328 never-named stocks; the mean of the matched control stocks described below, weighted by their matching weights; the equal-weighted mean of the 110 never-named stocks in the top tercile of pre-period trading value among never-named stocks; and a market model with intercept and slope estimated for each stock against the first benchmark. "
    "Because every constituent shares the same event dates, abnormal returns are correlated across stocks, and cross-sectional t-statistics overstate precision. We therefore test cumulative abnormal returns (CARs) on the equal-weighted portfolio of the group, dividing the portfolio CAR by the standard deviation of daily portfolio abnormal returns in an estimation window, scaled by the square root of the window length (Brown & Warner, 1985). "
    "The estimation window runs from trading day -130 to -11 before each event and excludes days -1 to +20 around every earlier disclosure, which removes 22 to 31 event days from the windows of the later disclosures. "
    "We pre-specify three windows for every disclosure, [-1,+1], [-1,+5] and [0,+20], report all of them, and call a CAR robust when it is significant at 5% under all four benchmarks.")
t50 = sub("B0050", "(Appendix Table A1)", "(Appendix Table A.1)")
t50 = t50.replace("matching reduces the standardized mean difference", "because matching is with replacement, each control enters the estimates with its matching weight. Matching reduces the standardized mean difference", 1)
t50 = t50.replace("from the 85 never-named stocks in the top tercile of pre-period trading value", "from the 85 never-named stocks whose pre-period trading value lies in the top tercile of all 366 sample stocks", 1)
new["B0050"] = t50
new["B0057"] = sub("B0057", "ITT estimates measure the effect on stocks that were likely constituents before the announcement, and they understate the effect of inclusion to the extent that 12 of the 27 listed stocks were not included.",
    "ITT estimates measure the average effect on stocks that were likely constituents before the announcement, including the 12 listed stocks that FTSE did not include.")
new["B0060"] = ("Constituents' Amihud illiquidity fell relative to never-named stocks in each disclosure window, and the fall deepened at each stage. Table 2, column 1, reports coefficients of -0.39, -0.89 and -1.13 log points, declines of 32%, 59% and 68%. All three are significant at the 0.1% level, and the wild cluster bootstrap p-values are below 0.001. "
    "The matched sample, with each control weighted by its matching weight, gives smaller declines: -0.23 (not significant), -0.47 and -0.69 log points in column 4 (declines of 21%, 38% and 50%). "
    "The confirmation brought a discrete step: allowing constituents a linear drift after the announcement (-0.012 log points per week, p = 0.002), the confirmation-window coefficient still exceeds the announcement-window coefficient by 0.21 log points (standard error 0.10, p = 0.035). The constituent list did not: its additional step is 0.10 (standard error 0.11, p = 0.40). "
    "H2 therefore holds for the confirmation; after it, liquidity kept improving gradually rather than jumping at the list.")
new["B0068"] = txt("B0068") + (" The ITT group shows the same shape (Figure 2): coefficients of 0.26 and 0.22 three and two months before the announcement, which make its joint pre-trend test reject as well (F = 7.59, p < 0.001), followed by a decline from -0.22 in October 2025 to -0.78 in August 2026.")
ins["B0071"] = "\n\n".join(["**Figure 2. Monthly event-study coefficients for the intention-to-treat group**",
    "![](figures/figure2_itt_event_study.png)",
    "*Note*: log Amihud illiquidity of the 27 stocks on FTSE's preliminary eligible list (screened on 2024 data) relative to never-named, never-included HOSE stocks; coefficients relative to September 2025 from a regression with stock and week fixed effects; 95% confidence intervals from stock-clustered standard errors. Source: output/revision2/t_itt_event_study.csv."])
new["B0076"] = ("Constituents earned abnormal returns in the week around the announcement and around the confirmation, and these are the only disclosure-window CARs that are robust in the sense defined in Section 3.2. Table 4, panel A, reports CARs with portfolio t-statistics for every pre-specified window. "
    "Over days -1 to +5 around the announcement, constituents earned between 3.9% and 7.8% depending on the benchmark (t between 2.19 and 3.46). Over days -1 to +1 around the confirmation, they earned between 2.7% and 4.5% (t between 2.22 and 2.93). "
    "The three-day announcement window is significant under one benchmark only, so the announcement response built up over the week. Around the constituent list, three-day CARs of 1.5% to 2.7% are not significant under any benchmark, and the [-1,+5] CARs of 2.0% to 4.4% are significant under two of four. "
    "Around the effective date the three-day CAR lies between -0.5% and 1.0% and is never significant. The last column shows why the portfolio test matters: cross-sectional t-statistics, which ignore the common event date, are up to three times larger.")
new["B0083"] = ("The announcement and confirmation gains behaved differently afterwards. Over days 0 to +20 the announcement CAR lies between -5.5% and 1.6% and is never significant, so the announcement gain faded within a month. "
    "Over the same window after the confirmation, constituents earned 6.2% to 10.6%, significant under three of the four benchmarks (t between 1.94 and 3.03). "
    "The fading after the first, conditional announcement is consistent with temporary price pressure (Harris & Gurel, 1986). The persistent gain after the confirmation, once the upgrade was certain and dated, is consistent with a lasting shift in demand for the stocks (Shleifer, 1986; Chen et al., 2004).")
new["B0084"] = ("Panels B and C separate the stocks that were likely to be included from those that were eventually passed over. The pre-announcement eligible group earned 3.5% to 7.5% in the announcement week, significant under three of four benchmarks (the matched benchmark gives t = 1.91), so the announcement response does not depend on FTSE's later choice. "
    "At the confirmation, its three-day CARs of 1.3% to 3.1% are significant under three of four benchmarks but not against matched controls. "
    "The named-but-excluded stocks gained 2.3% to 6.3% in the announcement week (significant under three of four benchmarks) and nothing at the confirmation (-1.4% to 0.4%, never significant). "
    "No eligibility list was public at the announcement, so the announcement-week gain of stocks that later appeared on the lists reflects characteristics investors could observe, such as size and liquidity, rather than the lists themselves. By the confirmation the preliminary list was public, and only stocks that went on to be included gained.")
new["B0085"] = "**Takeaway.** Prices rose in the announcement week and at the confirmation under every benchmark; the confirmation gain persisted under three of four; the constituent list and the first index tranche added no robust price effect."
new["B0093"] = txt("B0093") + (" An event regression that uses the last session before 21 August 2026 as the reference gives 0.62 (t = 3.54) for 18 September, but that reference session was unusually active and several earlier sessions then show significant negative coefficients; we therefore compare each session with the average of the window.")
new["B0094"] = ("This surge matches the trading that funds tracking FTSE benchmarks had to do: they bought the first tranche of constituents at the closing price of 18 September, and nothing obliged them to trade the stocks FTSE had named and passed over (Harris & Gurel, 1986). "
    "Our data do not identify who traded, so we infer index demand from the timing and from the absence of a surge for named-but-excluded stocks. That absence is a direct falsification test: a general rise in trading among large or eligible stocks would have shown up there. "
    "The surge moved volume but not prices: the three-day CAR around the effective date is between -0.5% and 1.0% under every benchmark (Table 4), consistent with other investors having bought earlier and supplying the stocks at the close. "
    "Because the first tranche carried only 10% of the eventual index weight, this evidence concerns the first tranche; the three later tranches in 2027 may carry larger demand.")
new["B0095"] = "**Takeaway.** Trading concentrated at the first-tranche rebalancing close on included stocks only, as index demand would imply, and prices had already adjusted by then."
new["B0098"] = ("Table 6 splits the constituent coefficients by segment. The three large-capitalization stocks show the largest fall in illiquidity: -0.61, -1.35 and -2.20 log points across the three windows, compared with -0.20, -0.63 and -0.82 for mid-capitalization stocks and -0.39, -0.85 and -1.00 for small-capitalization stocks. "
    "The ordering between mid and small stocks does not follow size, and with three stocks each in the two upper segments clustered inference is unreliable, so we report those estimates without significance marks and read them as descriptive. "
    "The rebalancing surge rises monotonically with segment: abnormal log trading value on 18 September 2026 averaged 1.23 for large-capitalization constituents, 0.98 for mid-capitalization and 0.65 for small-capitalization constituents. This supports H4.")
new["B0101"] = txt("B0101") + " Significance marks are omitted for the large and mid segments, which contain three stocks each."
new["B0102"] = "**Takeaway.** Index weight scales the rebalancing trade; the liquidity gain is largest for the three largest stocks but does not rise monotonically across segments, and every segment gained before the first tranche took effect."
new["B0116"] = ("**Pre-announcement months.** The pre-period deviations in Figure 1 are positive, so they work against the estimated declines rather than for them. Dropping July and August 2025, the two months with the largest positive deviations, changes the estimates to -0.35, -0.85 and -1.09. "
    "A constituent-specific linear trend fitted over the full sample leaves the estimates almost unchanged, with a trend coefficient of -0.0002 per week (standard error 0.003). "
    "The most demanding specification, the weighted matched sample with a trend, gives -0.20, -0.42 and -0.64; the confirmation and list estimates are significant at 5%, the announcement estimate is not. "
    "We therefore rest the announcement-stage conclusion on the full-sample, ITT and trend estimates and treat it as less certain than the later stages.")
new["B0118"] = sub("B0118", "its pre-period trend is strong", "a constituent-specific linear trend fitted over the full sample is strong")
new["B0119"] = sub("B0119", "With only 48 clusters in the matched sample, the wild cluster bootstrap p-values remain at or below 0.003.",
    "In the unweighted matched sample, with 48 clusters, the wild cluster bootstrap p-values remain at or below 0.003.")
ins["B0119"] = ("**Sector composition and the pre-funding reform.** Banks and securities firms make up 13 of the 24 constituents and 8 of the 27 stocks in the ITT group, and their trading co-moves with market turnover. "
    "Dropping them leaves the results intact: the remaining 11 constituents show declines of 0.44, 1.04 and 1.40 log points, and the remaining 19 ITT stocks 0.23, 0.52 and 0.83 (Table 8). "
    "LSEG (2026) credits the removal of pre-funding requirements for foreign investors for Vietnam's upgrade, and that reform applies to every stock foreign investors can buy. "
    "The 85 large never-named stocks in the randomization pool, also open to foreign investors within ownership limits, became more liquid by about one fifth as much as constituents in the list window (-0.21 against -1.13). "
    "This comparison does not separate the reform from the upgrade for the largest stocks, and we list it as a limitation.")
new["B0122"] = txt("B0122") + " Excluding BSR, whose pre-period spans two trading venues, the group estimates are -0.23, -0.46 and -0.73, with only the last significant at 5%."
new["B0123"] = ("FTSE screened the April 2026 list on data as of 31 December 2025, which covers the first twelve weeks after the announcement. GEE entered the list in April; relative to never-named stocks, its illiquidity fell by 1.83 log points between the announcement and 31 December 2025, inside the data window FTSE screened, and by 1.59 by April 2026 (Table 9, panel C). "
    "BSR, the other April addition, improved mostly after the cut-off (-0.39 by 31 December, -1.68 by April), and it moved from UPCoM to HOSE only in January 2025, after the data date of the November list (VietnamPlus, 2024), which gives a reason other than liquidity for its later addition. "
    "The twelve stocks named in November 2025 changed little: -0.02, -0.19 and -0.30 log points across the three windows, none significant at 5%. At the stock level, PLX, which FTSE dropped in April, and DPM were the only November names to fall by more than 0.5 log points by the April list.")
new["B0131"] = txt("B0131") + " The two-stock row reports point estimates only, because clustered inference is not informative with two stocks. Because named-but-excluded stocks enter with their own window interactions, the constituent coefficients in panel A equal those in Table 2 to three decimals."
new["B0132"] = ("This evidence limits how the constituent results can be read. FTSE's screens rest on investability, and at least one stock became eligible after its liquidity rose during the screening window. "
    "The same mechanism can operate among the final constituents, which FTSE chose on June 2026 data, and selection on those data could also favour stocks with large gains on disclosure dates. "
    "The ITT group is not exposed to this selection: fixed on 2024 data, it shows illiquidity declines of 24% to 56% and a robust announcement-week price response under three of four benchmarks. "
    "The constituent estimates combine the upgrade's effect with FTSE's selection; the ITT estimates average the effect over listed stocks that were and were not included. We report both and treat neither as a bound on the other.")
new["B0133"] = "**Takeaway.** FTSE's lists partly followed liquidity, but stocks fixed as likely constituents before the announcement also gained, so selection does not account for the whole liquidity response."
new["B0135"] = ("Vietnam's reclassification brought liquidity and price gains to likely index stocks at FTSE's disclosures, before the first index tranche took effect. Stocks that FTSE had screened as eligible on data from before the announcement became 24% less illiquid within months and 56% less illiquid by the constituent list; the stocks FTSE finally included became 32% and 68% less illiquid. "
    "The confirmation added a discrete step, and after it liquidity kept improving gradually. Constituents' prices rose by 3.9% to 7.8% in the announcement week and by 2.7% to 4.5% around the confirmation, and only the confirmation gain lasted. "
    "The first index tranche added a trading surge at the rebalancing close, scaled by index weight and absent for excluded stocks, and no price change.")
new["B0137"] = ("The price evidence also shows how the market learned. In the announcement week, before any list was public, stocks that FTSE's screens would later deem eligible gained as a group whether or not FTSE later included them, which suggests that investors used observable size and liquidity to anticipate eligibility. "
    "At the confirmation, once the preliminary list was public, only stocks that went on to be included gained.")
new["B0139"] = ("The selection evidence sets a boundary on these conclusions. FTSE's eligibility lists partly followed rising liquidity, and the final constituents were chosen on data from mid-2026. "
    "We therefore report constituent and ITT estimates side by side; both show a large response at disclosure, and the ITT estimates do not depend on FTSE's final choice.")
new["B0140"] = ("The results carry two implications, both drawn from a single event. For regulators, the liquidity and price response arrived with credible, dated announcements rather than with index trading, which is consistent with clear and early communication of reclassification steps bringing the response forward; one event cannot show that earlier communication causes larger gains. "
    "For issuers, the gains concentrated in stocks FTSE could hold, and free float and foreign-ownership headroom enter FTSE's screens and index weights; we do not test whether raising them would change an issuer's outcome.")
new["B0143"] = sub("B0143", "**Table A1.", "**Table A.1.")
new["B0145"] = txt("B0145") + " Table 2, columns 4 to 6, and the matched benchmark in Table 4 use the matching weights."
new["B0146"] = sub("B0146", "**Table A2.", "**Table A.2.")
new["B0155"] = ("**Declaration of generative AI and AI-assisted technologies in the manuscript preparation process.** During the preparation of this work the authors used Claude (Anthropic) in order to organise the analysis code, draft text, simulate peer review and verify references against Crossref. "
    "After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.")
for bid in ["B0168", "B0169", "B0176", "B0177", "B0183", "B0184", "B0185", "B0186"]:
    new[bid] = txt(bid).rstrip() + " Accessed 24 September 2026."
ins["B0185"] = "VietnamPlus. (2024, December 30). *Vietnamese billion dollar oil refinery exits UPCoM to join HoSE*. https://en.vietnamplus.vn/vietnamese-billion-dollar-oil-refinery-exits-upcom-to-join-hose-post307514.vnp Accessed 24 September 2026."

# blocks needing exact-phrase edits checked at run time
t136 = txt("B0136")
new["B0136"] = t136.replace("Investors acted on FTSE's public statements, and the index funds that the first tranche obliged to buy found prices already adjusted.",
                            "Prices and liquidity moved with FTSE's public statements, and by the first-tranche rebalancing prices had already adjusted.")
assert new["B0136"] != t136, "B0136 phrase not found"
t138 = txt("B0138")
new["B0138"] = t138.replace("In Vietnam's case, the classification event redistributed liquidity toward likely index stocks, and index averages diluted that redistribution.",
                            "In Vietnam's case, the classification event shifted liquidity toward likely index stocks relative to the rest of the market, and index averages diluted that shift; we do not test whether other stocks lost liquidity in absolute terms.")
assert new["B0138"] != t138, "B0138 phrase not found"
t141 = txt("B0141")
anchor = "so we cannot observe whether foreign investors drove the gains."
assert t141.count(anchor) == 1
new["B0141"] = t141.replace(anchor, anchor + " For the largest stocks, the upgrade cannot be fully separated from the concurrent removal of pre-funding requirements for foreign investors, and one named-but-excluded stock, BSR, changed trading venue during the pre-period.")

json.dump({"new": new, "ins": ins}, open(D / "round2_edits.json", "w"), ensure_ascii=False, indent=1)
print("replace blocks:", len(new), " inserts:", len(ins))
