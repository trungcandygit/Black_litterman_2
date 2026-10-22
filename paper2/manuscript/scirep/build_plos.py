"""Build the PLOS ONE package (paper2/final/PLOS_ONE) from manuscript_plos.md and the saved output tables.
Formatting only; numbers come from the MSJ manuscript (tables) and paper2/output/tables."""
import os, re, shutil, subprocess, sys, zipfile
import pandas as pd
from scipy.stats import t as tdist
from docx import Document
from docx.shared import Pt, Cm
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_scirep as B
import refs_scirep as RF

OUT = os.path.join(HERE, "..", "..", "final", "PLOS_ONE")
TAB = B.TAB
WORK = B.WORK
os.makedirs(OUT, exist_ok=True)
MINUS = B.MINUS

# ------------------------------------------------------------------ Vancouver references
ABBR = {"J. R. Stat. Soc. Ser. B": "J R Stat Soc Series B", "PLOS ONE": "PLoS One",
        "J. Econ. Dev. (Univ. Econ. Ho Chi Minh City)": "J Econ Dev", "Pac.-Basin Finance J.": "Pac Basin Finance J"}


def van_authors(a):
    out = []
    for x in a:
        if x.endswith("."):          # organisation author
            out.append(x); continue
        sur, ini = x.split(", ", 1)
        jr = ""
        if sur.endswith(" Jr."):
            sur, jr = sur[:-4], " Jr"
        ini = re.sub(r"[^A-Z\-]", "", ini.replace(".-", "-"))
        out.append(f"{sur} {ini}{jr}")
    s = ", ".join(out[:6])
    return s + (", et al" if len(out) > 6 else "")


def van_ref(key):
    r = RF.R[key]
    au = van_authors(r["authors"]).rstrip(".")
    title = r["title"].rstrip(".")
    if key == "hsc":
        return "Ho Chi Minh City Securities Corporation. Important changes of new trading system [Internet]. Ho Chi Minh City: Ho Chi Minh City Securities Corporation; 2025 [cited 2026 Oct 5]. Available from: https://www.hsc.com.vn/en/important-changes-of-new-trading-system"
    if key == "vnnews":
        return "Viet Nam News. KRX system officially goes live. Viet Nam News. 2025 [cited 2026 Oct 5]. Available from: https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html"
    if key == "farber":
        return f"{au}. {title}. CEB Working Paper No. 06/005. Brussels: Université Libre de Bruxelles; 2006. Available from: https://ideas.repec.org/p/sol/wpaper/06-005.html"
    j = ABBR.get(r["journal"], r["journal"].replace(".", ""))
    pages = r["pages"].replace("–", "-") if r["pages"] else ""
    s = f"{au}. {title}. {j}. {r['year']};{r['vol']}" + (f": {pages}" if pages else "") + "."
    if r["doi"]:
        s += f" doi: {r['doi']}"
    if r["tail"]:
        s += " Available from: " + r["tail"]
    return s


def cites(text, order):
    return B.cite_numbers(text, order)


# ------------------------------------------------------------------ main manuscript
def table_blocks():
    blocks = B.msj_blocks()
    notes = {
        1: blocks[1]["note"] + " *P* values from the *t* distribution with *G* − 1 degrees of freedom are below 0.001 for every *t* (date), *t* (week) and *t* (10-day) except for ceiling days *d*+2 to *d*+5 (*P* = 0.127, 0.271, 0.218) and floor days *d*+2 to *d*+5 (*P* = 0.004, 0.003, 0.007). *n* is the number of events.",
        2: blocks[2]["note"] + " " + B.NOTE_P, 3: blocks[3]["note"] + " " + B.NOTE_P,
        4: blocks[4]["note"] + " " + B.NOTE_P, 5: blocks[5]["note"] + " " + B.NOTE_P}
    titles = {1: "Market-adjusted returns after ceiling and floor closes", 2: "Decomposition of the next-day abnormal return",
              3: "Limit closes versus near-limit moves", 4: "Returns before and after the KRX platform change of 5 May 2025",
              5: "Events and overnight gaps by calendar quarter"}
    return {n: B.table_md(n, blocks, f"Table {n}", titles[n], notes[n]) for n in range(1, 6)}


FIG1 = ("**Fig 1. Fama–MacBeth *t*-statistics of 22 characteristics.** Circles show the full sample, triangles the discovery half (first 39 weeks) "
        "and squares the confirmation half. Characteristics are ordered by absolute full-sample *t*. Dashed lines mark |*t*| = 1.96 and dotted lines "
        "|*t*| = 3. *n* = 79 weekly cross-sections; Newey–West standard errors with four lags. S1 Appendix defines the labels.")
FIG2 = ("**Fig 2. Next-day abnormal return by the size of the day-*d* move.** Panels show the overnight gap (a), the intraday return (b) and the "
        "close-to-close return (c). Circles show 1-point bins inside the band, triangles ceiling and floor closes, and squares other moves of 6.5% to 10%. "
        "Error bars are 95% confidence intervals clustered by date. Market weights are lagged to day *d*.")
SI_CAPTIONS = [
    ("S1 Appendix", "Characteristic definitions and literature search.", "Definitions of the 22 price- and volume-based characteristics and the record of the literature search."),
    ("S1 Table", "Comparison with earlier studies.", "Setting, reported finding and relation to our result for the closest studies."),
    ("S2 Table", "Next-day abnormal returns under alternative event definitions.", "Overnight gap, intraday, close-to-close and open-to-day-*d*+5 returns for different return thresholds, close conditions and locked days."),
    ("S3 Table", "Adjusted *P* values of the four event tests under alternative family definitions.", "Benjamini–Hochberg, Holm and Bonferroni adjustments and alternative family sizes."),
    ("S4 Table", "Difference-in-differences around the KRX platform change of 5 May 2025.", "Excess gap of limit closes over 5–6.5% movers that closed at the extreme, before and after the change."),
    ("S5 Table", "Fama–MacBeth estimates for the 22 characteristics.", "Coefficients, standard errors, 95% confidence intervals and *P* values, with Benjamini–Hochberg and Holm adjustments."),
    ("S1 File", "Output tables.", "CSV files with the output tables behind every table and figure of the article (zip archive)."),
]


def build_main():
    src = open(os.path.join(HERE, "manuscript_plos.md"), encoding="utf-8").read()
    order = []
    src = re.sub(r"<<t (-?[\d.]+)>>", B.tok_t, src)
    src = cites(src, order)
    src = src.replace("::: pagebreak\n:::\n", B.PB).replace("::: title\n", "::: {custom-style=\"Title\"}\n")
    tabs = table_blocks()
    for n in range(1, 6):
        src = src.replace("{{TABLE%d}}" % n, tabs[n])
    src = src.replace("{{FIG1}}", FIG1).replace("{{FIG2}}", FIG2)
    src = src.replace("::: references\n:::\n", "\n".join(f"{i + 1}. {van_ref(k)}" for i, k in enumerate(order)) + "\n")
    cap = "\n\n".join(f"**{a}.** {b} {c}" for a, b, c in SI_CAPTIONS)
    src = src.replace("::: sicaptions\n:::\n", cap + "\n")
    src = B.minus_fix(src)
    path = os.path.join(WORK, "manuscript_plos.build.md")
    open(path, "w", encoding="utf-8").write(src)
    out = os.path.join(OUT, "Manuscript_PLOS_ONE.docx")
    B.pandoc(path, out)
    B.style_docx(out, line_numbers=True, spacing=2.0, justify=True)
    absr = src.split("## Abstract")[1].split("## Introduction")[0]
    print("abstract words:", B.word_count(absr), "| references:", len(order))
    return order


# ------------------------------------------------------------------ supporting information
def si_doc(name, md, justify=True, landscape=False):
    path = os.path.join(WORK, name + ".md")
    open(path, "w", encoding="utf-8").write(B.minus_fix(md))
    out = os.path.join(OUT, name + ".docx")
    B.pandoc(path, out)
    B.style_docx(out, line_numbers=False, base_pt=11, spacing=1.15, justify=justify, landscape=landscape)


def f2(x, d=2):
    return (MINUS if x < 0 else "") + f"{abs(x):.{d}f}"


def build_si():
    blocks = B.msj_blocks()
    src = open(os.path.join(HERE, "..", "msj", "S1_supplementary.Rmd"), encoding="utf-8").read()
    n1 = src.split("## S1.1. Characteristic definitions")[1].split("## S1.2.")[0].strip()
    n2 = src.split("## S1.2. Literature search")[1].split("## References")[0].strip()
    n1 = n1.replace("Parkinson (1980)", "Parkinson⟦parkinson⟧").replace("(Amihud, 2002)", "⟦amihud⟧")
    n1 = n1.replace("(Bali et al., 2011)", "⟦bali⟧").replace("Corwin and Schultz (2012)", "Corwin and Schultz⟦corwin⟧")
    n1 = n1.replace("Section 2.2 of the article", "Materials and methods")
    n2 = n2.replace("with the web search tool of the AI assistant named in Section 6.2 of the article", "with a web search engine")
    n2 = n2.replace("(Section 2.1 of the article)", "(Materials and methods)")
    n2 = n2.replace("(Kim & Rhee, 1997; Huang et al., 2001; Qi, 2023)", "⟦kimrhee,huangy,qi⟧").replace("Farber et al. (2006)", "Farber et al.⟦farber⟧")
    n2 = n2.replace("Le (2012)", "Le⟦le⟧").replace("Table 6 reports their results", "S1 Table reports their results")
    order = []
    t = "::: {custom-style=\"Title\"}\nS1 Appendix. Characteristic definitions and literature search\n:::\n\nDo price limits delay price discovery? Overnight gaps after limit closes in Vietnam\n\n"
    t += "## Characteristic definitions\n\n" + n1 + "\n\n## Literature search\n\n" + n2 + "\n"
    t = B.cite_numbers(t, order)
    t += "\n## References\n\n" + "\n".join(f"{i + 1}. {van_ref(k)}" for i, k in enumerate(order)) + "\n"
    si_doc("S1_Appendix", t)

    def head(lbl, title):
        return f"::: {{custom-style=\"Title\"}}\n{lbl}. {title}\n:::\n\n"
    # S1 Table
    keys = ["kimrhee", "berkmanlee", "huangy", "cho", "chen19", "qi", "lin", "zeng", "berkman12", "lou", "qiao", "hou", "hlz"]
    refl = "\n".join(f"{i + 1}. {van_ref(k)}" for i, k in enumerate(keys))
    note = ("*Note.* Entries for Kim and Rhee (1997), Huang et al. (2001) and Qi (2023) report results from the full texts; the other entries summarize each study's abstract.\n\n"
            "References for this table:\n\n" + refl)
    si_doc("S1_Table", head("S1 Table", "Comparison with earlier studies") + "\n".join(blocks[6]["table"]) + "\n\n" + note + "\n", landscape=True)
    # S2 Table
    c28 = pd.read_csv(os.path.join(TAB, "C28_event_definitions.csv"))
    rows = ["| Event definition | Overnight gap | Intraday | Close-to-close | Open to day *d*+5 | Events |", "|:---|:---:|:---:|:---:|:---:|:---:|"]
    for d_, g in c28.groupby("definition", sort=False):
        cells = {r.measure: f"{f2(r.mean_pct)} ({f2(r.t_twoway, 1)})" for r in g.itertuples()}
        n = int(g[g.measure == "gap_mkt"].n.iloc[0])
        rows.append(f"| {d_.replace('>=', '≥').replace('<=', '≤')} | " + " | ".join(cells[k] for k in ("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt")) + f" | {n:,} |")
    si_doc("S2_Table", head("S2 Table", "Next-day abnormal returns under alternative event definitions") + "\n".join(rows) +
           "\n\n*Note.* Market-adjusted returns in percent; two-way-clustered *t*-statistics in parentheses (two-sided *P* < 0.001 for |*t*| ≥ 3.29). Source: authors' calculations.\n")
    # S3 Table
    c32 = pd.read_csv(os.path.join(TAB, "C32_family_sensitivity.csv"))
    tests = ["ceiling t+1", "ceiling t+1..t+5", "floor t+1", "floor t+1..t+5"]
    rows = ["| Family definition | Ceiling, *d*+1 | Ceiling, *d*+1 to *d*+5 | Floor, *d*+1 | Floor, *d*+1 to *d*+5 |", "|:---|:---:|:---:|:---:|:---:|"]
    for f_ in dict.fromkeys(c32.family):
        g = c32[c32.family == f_].set_index("test")
        rows.append(f"| {f_.replace('t+1..t+5', '*d*+1 to *d*+5').replace('t+', '*d*+')} | " + " | ".join(f"{g.loc[t_, 'adjusted_p']:.1e}" for t_ in tests) + " |")
    si_doc("S3_Table", head("S3 Table", "Adjusted *P* values of the four event tests under alternative family definitions") + "\n".join(rows) +
           "\n\n*Note.* BH, Benjamini–Hochberg; Holm and Bonferroni as named. All adjusted *P* values are below 0.05. Source: authors' calculations.\n")
    # S4 Table
    c31 = pd.read_csv(os.path.join(TAB, "C31_krx_did.csv"))
    names = {"gap_mkt": "Overnight gap", "cc1_mkt": "Close-to-close"}
    rows = ["| Contrast | Outcome | Excess before the change | *t* | Change after | *t* | Events | Comparison stock-days |", "|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for r in c31.itertuples():
        rows.append(f"| {r.contrast.replace('5-6.5%', '5–6.5%')} | {names.get(r.outcome, r.outcome)} | {f2(r.limit_minus_control_pre_pct)} | {f2(r.t_pre, 1)} | {f2(r.change_after_krx_pct)} | {f2(r.t_change, 1)} | {int(r.n_limit):,} | {int(r.n_control):,} |")
    si_doc("S4_Table", head("S4 Table", "Difference-in-differences around the KRX platform change of 5 May 2025") + "\n".join(rows) +
           "\n\n*Note.* Percentage points; date-clustered *t*-statistics; limit closes compared with 5–6.5% movers that also closed at the extreme. Source: authors' calculations.\n")
    # S5 Table: full Fama-MacBeth results
    c1 = pd.read_csv(os.path.join(TAB, "C1_characteristics_FM.csv")).set_index("characteristic")
    c3 = pd.read_csv(os.path.join(TAB, "C3_family_control.csv")).set_index("test")
    rows = ["| Characteristic | Slope (% per week per SD) | Standard error | 95% CI | *t* (Newey–West) | *P* | BH-adjusted *P* | Holm-adjusted *P* | *t*, discovery half | *t*, confirmation half | Quintile spread (%) | Spread net of cost (%) |",
            "|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    crit = tdist.ppf(0.975, 78)
    def pf(p):
        return "< 0.001" if p < 0.001 else f"{p:.3f}"
    for ch, r in c1.iterrows():
        se = abs(r.slope_pct_per_week / r.t_nw)
        lo, hi = r.slope_pct_per_week - crit * se, r.slope_pct_per_week + crit * se
        rows.append(f"| {ch} | {f2(r.slope_pct_per_week, 3)} | {se:.3f} | {f2(lo, 3)} to {f2(hi, 3)} | {f2(r.t_nw)} | {pf(r.p)} | {pf(c3.loc[ch, 'p_bh'])} | {pf(c3.loc[ch, 'p_holm'])} | {f2(r.t_disc)} | {f2(r.t_conf)} | {f2(r.quintile_spread_pct)} | {f2(r.quintile_net25_pct)} |")
    si_doc("S5_Table", head("S5 Table", "Fama–MacBeth estimates for the 22 characteristics") + "\n".join(rows) +
           "\n\n*Note.* Weekly Fama–MacBeth regressions of equation (7) with rank-normalized characteristics (*n* = 79 weekly cross-sections, 78 degrees of freedom); standard errors are slope/*t*; 95% confidence intervals use the *t* distribution with 78 degrees of freedom; two-sided *P* values; BH, Benjamini–Hochberg; quintile spread is the long–short return of the extreme quintiles and the net spread subtracts a 25-basis-point cost. Goodness-of-fit measures are not reported for the week-by-week cross-sectional regressions. Source: authors' calculations.\n", justify=False, landscape=True)
    # S1 File: output tables
    zp = os.path.join(OUT, "S1_File.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(os.listdir(TAB)):
            if re.match(r"C\d+b?_.*\.csv$", fn):
                z.write(os.path.join(TAB, fn), fn)


# ------------------------------------------------------------------ figures, cover letter, notes
def build_figs():
    import figures_scirep as F
    F.figure1(); F.figure2()
    for n in (1, 2):
        im = Image.open(os.path.join(HERE, "..", "..", "final", "SciRep", f"Figure_{n}.png")).convert("RGB")
        im.save(os.path.join(OUT, f"Fig{n}.tif"), compression="tiff_lzw", dpi=(300, 300))


def build_cover():
    d = Document()
    s = d.sections[0]; s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.2)
    st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(11)
    paras = [
        "Dear Editors,",
        "We submit the Research Article “Do price limits delay price discovery? Overnight gaps after limit closes in Vietnam” for consideration in PLOS ONE.",
        "Contribution. Exchanges worldwide use daily price limits, but little is known about how prices adjust after a stock closes at its limit. Using daily prices of 347 stocks on the Ho Chi Minh Stock Exchange (August 2024 to September 2026), we split the next-day abnormal return into an overnight gap and an intraday return. After a ceiling close the stock opens on average 2.2% above the market and the following session gives back about 24% of the gap; the gap is 2.7 percentage points larger than after rises that stop short of the limit; and a buyer at the next open trails the market by 0.7% by the fifth close. We test the four limit tests together with 22 price- and volume-based characteristics under false discovery rate control, and we report the floor-close result that depends on the benchmark and the explanations that our data cannot separate.",
        "Relation to previous work. The study extends the Taiwanese evidence on overnight and intraday returns after limit hits, the Tokyo and Istanbul evidence on delayed price discovery, and the evidence on band changes in China and Korea, with a new market, a call-auction setting and the 2025 change of trading platform. PLOS ONE has published a closely related study of the ChiNext band change, which we cite.",
        "Article type: Research Article. The manuscript is original, is not under consideration elsewhere, and all authors have approved it. Data and code are public, as described in the Data Availability statement. We have had no prior interaction with PLOS about this manuscript.",
        "Suggested Academic Editors: none; we leave the choice to the journal. Opposed reviewers: none.",
        "Sincerely,\nNguyen Van Trung, on behalf of all authors",
    ]
    for p in paras:
        para = d.add_paragraph(p); para.paragraph_format.space_after = Pt(5); para.paragraph_format.alignment = 3
    d.save(os.path.join(OUT, "Cover_letter.docx"))


NOTES = """# PLOS ONE: submission package and form entries

Title: Do price limits delay price discovery? Overnight gaps after limit closes in Vietnam
Short title: Price limit closes and overnight gaps in Vietnam
Authors (order): Ha Hong Hanh; Nguyen Van Trung (corresponding, kontrungcany@gmail.com, ORCID 0009-0008-3307-6569, enter it in the profile); Nguyen Thanh Binh.

## Files to upload

| Item type | File |
|---|---|
| Cover Letter | `Cover_letter.docx` (1 page; no fee-waiver request) |
| Manuscript | `Manuscript_PLOS_ONE.docx` (title page, abstract, text, tables, figure captions, references, supporting information captions) |
| Figure | `Fig1.tif`, `Fig2.tif` (TIFF, 300 dpi, LZW; figures are not in the manuscript file) |
| Supporting Information | `S1_Appendix.docx`, `S1_Table.docx`, `S2_Table.docx`, `S3_Table.docx`, `S4_Table.docx`, `S5_Table.docx`, `S1_File.zip` |

## Form entries (copy and paste)

**Article type:** Research Article

**Keywords:** market microstructure; multiple testing; false discovery rate; call auction; emerging markets; Ho Chi Minh Stock Exchange

**Financial disclosure:** The author(s) received no specific funding for this work.

**Competing interests:** The authors have declared that no competing interests exist.

**Ethics statement:** Not applicable. The study uses publicly available daily market prices of listed stocks and involves no human or animal subjects.

**Data availability statement:** All data and code underlying the findings are publicly available. The daily price files (retrieved with the vnstock Python library, version 4.0.4, from the VCI data source on 24 September 2026), the R code that reproduces every number, table and figure (paper2/R/run_all.R) and the output tables are in the GitHub repository https://github.com/trungcandygit/black_litterman_2 (folders data/raw and paper2). The output tables are also provided as S1 File.

**Author contributions (CRediT):**

| Author | Roles |
|---|---|
| Ha Hong Hanh | Conceptualization; Writing – review & editing |
| Nguyen Van Trung | Data curation; Formal analysis; Methodology; Software; Visualization; Project administration; Writing – original draft |
| Nguyen Thanh Binh | Conceptualization; Supervision; Writing – review & editing |

**Generative AI:** Gemini (Google) was used only to edit the language; stated in Materials and methods.

**Suggested Academic Editors / opposed reviewers:** none (the authors leave the choice to the journal).

## To check before submitting

1. Confirm CRediT roles, funding and competing interests with all three authors; PLOS emails every author at submission.
2. PLOS prefers a repository with a DOI: make a GitHub release linked to Zenodo and add the DOI to the Data availability statement; check the vnstock/VCI terms before publishing the price files.
3. Open the .docx files in Microsoft Word to see the equations (LibreOffice does not draw them).
4. Check the publication fee and fee assistance in the submission system (not in the cover letter).
"""


if __name__ == "__main__":
    build_figs()
    build_main()
    build_si()
    build_cover()
    open(os.path.join(OUT, "submission_info.md"), "w", encoding="utf-8").write(NOTES)
