"""Build the Scientific Reports package from manuscript_scirep.md and the saved output tables.
Outputs (paper2/final/SciRep): Manuscript_SciRep.docx, Supplementary_Information.docx, Cover_letter.docx, figures.
Formatting only: numbers come from the MSJ manuscript (tables 1-6) and from paper2/output/tables."""
import math, os, re, subprocess, sys
import pandas as pd
from scipy.stats import norm
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import refs_scirep as RF

OUT = os.path.join(HERE, "..", "..", "final", "SciRep")
TAB = os.path.join(HERE, "..", "..", "output", "tables")
WORK = os.path.join(HERE, "work")
os.makedirs(WORK, exist_ok=True)
MSJ_MD = os.path.join(WORK, "msj_text.md")
subprocess.check_call(["pandoc", os.path.join(HERE, "..", "..", "final", "MSJ", "Manuscript_MSJ.docx"),
                       "-t", "markdown-grid_tables-simple_tables-multiline_tables+pipe_tables", "--wrap=none", "--columns=100000", "-o", MSJ_MD])
MINUS = "−"


# ------------------------------------------------------------------ helpers
def pstr(t):
    p = 2 * norm.sf(abs(t))
    return "*P* < 0.001" if p < 0.001 else f"*P* = {p:.3f}" if p < 0.01 else f"*P* = {p:.2f}"


def tok_t(m):
    t = float(m.group(1))
    s = f"{abs(t):.1f}" if abs(t) >= 1 or True else f"{abs(t):.2f}"
    if abs(t) < 0.1:
        s = f"{abs(t):.2f}"
    s = (MINUS if t < 0 else "") + s
    return f"*t* = {s}, {pstr(t)}"


def cite_numbers(text, order, key_prefix=""):
    def repl(m):
        keys = [k.strip() for k in m.group(1).split(",")]
        nums = []
        for k in keys:
            assert k in RF.R, k
            if k not in order:
                order.append(k)
            nums.append(order.index(k) + 1)
        nums = sorted(set(nums))
        parts, i = [], 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            parts.append(f"{nums[i]}–{nums[j]}" if j - i >= 2 else ",".join(str(n) for n in nums[i:j + 1]))
            i = j + 1
        return "[" + ",".join(parts) + "]"
    return re.sub("⟦([^⟧]+)⟧", repl, text)


def minus_fix(text):
    """True minus sign for negative numbers outside math blocks and links."""
    parts = re.split(r"(\$\$.*?\$\$|\$[^$\n]*\$|https?://\S+)", text, flags=re.S)
    out = []
    for p in parts:
        if p.startswith("$") or p.startswith("http"):
            out.append(p)
        else:
            out.append(re.sub(r"(?<=[\s(\[|,;])-(?=\d)", MINUS, p))
    return "".join(out)


def word_count(md):
    t = re.sub(r"\$\$.*?\$\$", " ", md, flags=re.S)
    t = re.sub(r"\$[^$\n]*\$", " ", t)
    t = re.sub(r"[\*\^~\\\[\]#|:_-]+", " ", t)
    return len(t.split())


# ------------------------------------------------------------------ tables from the MSJ version
def msj_blocks():
    lines = open(MSJ_MD, encoding="utf-8").read().split("\n")
    i0 = next(i for i, l in enumerate(lines) if l.startswith("**Table 1**"))
    blocks, cur = {}, None
    i = i0
    while i < len(lines):
        m = re.match(r"\*\*Table (\d)\*\* (.*)", lines[i])
        if m:
            cur = int(m.group(1)); blocks[cur] = dict(title=m.group(2).strip(), table=[], note="")
        elif cur and lines[i].startswith("|"):
            blocks[cur]["table"].append(lines[i])
        elif cur and lines[i].startswith("*Note.*"):
            blocks[cur]["note"] = lines[i]
        i += 1
    return blocks


def drop_empty_rows(tbl_lines):
    return tbl_lines


NOTE_P = "*P* values are from the standard normal distribution (|*t*| ≥ 3.29 gives *P* ≤ 0.001; |*t*| = 1.96 gives *P* = 0.05)."


def table_md(n, blocks, label, title, note):
    b = blocks[n]
    return f"**{label}.** {title}\n\n" + "\n".join(b["table"]) + f"\n\n{note}\n"


# ------------------------------------------------------------------ pandoc + docx styling
def set_cell_border(cell, **kw):
    tcPr = cell._tc.get_or_add_tcPr()
    b = tcPr.find(qn("w:tcBorders"))
    if b is None:
        b = OxmlElement("w:tcBorders"); tcPr.append(b)
    for edge, val in kw.items():
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), val); e.set(qn("w:sz"), "6"); e.set(qn("w:space"), "0"); e.set(qn("w:color"), "000000")
        b.append(e)


def style_docx(path, line_numbers=True, title_first=True, base_pt=12, spacing=1.5):
    d = Document(path)
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Cm(2.54)
    for st in d.styles:
        if st.type == 1 and st.font is not None:
            st.font.name = "Times New Roman"
            rpr = st.element.get_or_add_rPr()
            rf = rpr.find(qn("w:rFonts"))
            if rf is None:
                rf = OxmlElement("w:rFonts"); rpr.append(rf)
            for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
                rf.set(qn(a), "Times New Roman")
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
            st.font.color.rgb = None
    sizes = {"Normal": base_pt, "Body Text": base_pt, "First Paragraph": base_pt, "Compact": base_pt,
             "Heading 1": 16, "Heading 2": 14, "Heading 3": 12, "Title": 18}
    for st in d.styles:
        if st.name in sizes:
            st.font.size = Pt(sizes[st.name])
            if st.name.startswith("Heading") or st.name == "Title":
                st.font.bold = True; st.font.italic = (st.name == "Heading 3")
                st.paragraph_format.space_before = Pt(12); st.paragraph_format.space_after = Pt(6)
                st.paragraph_format.keep_with_next = True
    # body paragraphs: left aligned, 1.5 spacing
    for p in d.paragraphs:
        pf = p.paragraph_format
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if not p.style.name.startswith("Heading") and p.style.name != "Title":
            pf.line_spacing = spacing
            pf.space_after = Pt(6)
    # tables
    for t in d.tables:
        cols = len(t.columns)
        is_eq = cols == 2 and any(re.fullmatch(r"\(\d+\)", c.text.strip()) for r in t.rows for c in [r.cells[1]])
        if is_eq:
            # remove empty header row, no borders, number right-aligned
            first = t.rows[0]
            if all(not c.text.strip() for c in first.cells):
                t._tbl.remove(first._tr)
            t.autofit = False
            for r in t.rows:
                r.cells[0].width = Cm(14.0); r.cells[1].width = Cm(2.0)
                r.cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
                r.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                for c in r.cells:
                    for p in c.paragraphs:
                        p.paragraph_format.line_spacing = 1.0
            continue
        n = len(t.rows)
        wts = [max(len(re.sub(r"\s+", " ", r.cells[ci].text)) for r in t.rows) for ci in range(cols)]
        hdr = [max(len(w) for w in t.rows[0].cells[ci].text.split() or [""]) for ci in range(cols)]
        wts = [min(max(w, 16, h + 3), 26) for w, h in zip(wts, hdr)]
        total = 16.0
        t.autofit = False
        for ci in range(cols):
            for r in t.rows:
                r.cells[ci].width = Cm(total * wts[ci] / sum(wts))
        grid = t._tbl.find(qn("w:tblGrid"))
        for gc, w in zip(grid.findall(qn("w:gridCol")), wts):
            gc.set(qn("w:w"), str(int(total * w / sum(wts) / 2.54 * 1440)))
        for ri, r in enumerate(t.rows):
            for ci, c in enumerate(r.cells):
                for p in c.paragraphs:
                    p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.space_after = Pt(1)
                    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT if ci == 0 else WD_ALIGN_PARAGRAPH.CENTER
                    for run in p.runs:
                        run.font.size = Pt(8.5)
                        if ri == 0:
                            run.font.bold = True
                if ri == 0:
                    set_cell_border(c, top="single", bottom="single")
                if ri == n - 1:
                    set_cell_border(c, bottom="single")
    # footer page number
    footer = sec.footer
    fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp._p.get_or_add_pPr().append(OxmlElement("w:suppressLineNumbers"))
    for tag, txt in (("begin", None), (None, " PAGE "), ("end", None)):
        r = fp.add_run()
        if tag:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), tag); r._r.append(f)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)
    if line_numbers:
        sp = sec._sectPr
        ln = OxmlElement("w:lnNumType")
        ln.set(qn("w:countBy"), "1"); ln.set(qn("w:restart"), "continuous")
        sp.append(ln)
    d.save(path)


def pandoc(md_path, docx_path):
    subprocess.check_call(["pandoc", md_path, "-f", "markdown+smart-auto_identifiers", "-o", docx_path,
                           "--resource-path", OUT, "--wrap=none"])


PB = "```{=openxml}\n<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```\n"


# ------------------------------------------------------------------ main manuscript
def build_main():
    src = open(os.path.join(HERE, "manuscript_scirep.md"), encoding="utf-8").read()
    blocks = msj_blocks()
    order = []
    src = re.sub(r"<<t (-?[\d.]+)>>", tok_t, src)
    src = cite_numbers(src, order)
    # title
    src = src.replace("::: title\n", "::: {custom-style=\"Title\"}\n")
    src = src.replace("::: pagebreak\n:::\n", PB)
    # references
    refs = "\n".join(f"{i + 1}. {RF.fmt_ref(k)}" for i, k in enumerate(order))
    src = src.replace("::: references\n:::\n", refs + "\n")
    # figure legends and tables
    figs = (
        "![](Figure_1.png){width=13.5cm}\n\n"
        "**Figure 1. Fama–MacBeth *t*-statistics of 22 characteristics.** Circles show the full sample, triangles the discovery half "
        "(first 39 weeks) and squares the confirmation half. Characteristics are ordered by absolute full-sample *t*. Dashed lines mark "
        "|*t*| = 1.96 and dotted lines |*t*| = 3. *n* = 79 weekly cross-sections; Newey–West standard errors with four lags. "
        "Supplementary Note 1 defines the labels.\n\n"
        "![](Figure_2.png){width=16cm}\n\n"
        "**Figure 2. Next-day abnormal return by the size of the day-*d* move.** **a**, Overnight gap. **b**, Intraday return. "
        "**c**, Close-to-close return. Circles show 1-point bins inside the band, triangles ceiling and floor closes, and squares other "
        "moves of 6.5% to 10%. Error bars are 95% confidence intervals clustered by date. Market weights are lagged to day *d*.\n"
    )
    src = src.replace("::: figures\n:::\n", figs)
    T = []
    T.append(table_md(1, blocks, "Table 1", "Market-adjusted returns after ceiling and floor closes",
                      blocks[1]["note"] + " *P* values from the *t* distribution with *G* − 1 degrees of freedom are below 0.001 for every *t* (date), "
                      "*t* (week) and *t* (10-day) except for ceiling days *d*+2 to *d*+5 (*P* = 0.13, 0.27, 0.22) and floor days *d*+2 to *d*+5 "
                      "(*P* = 0.004, 0.003, 0.007). *n* is the number of events."))
    T.append(table_md(2, blocks, "Table 2", "Decomposition of the next-day abnormal return", blocks[2]["note"] + " " + NOTE_P))
    T.append(table_md(3, blocks, "Table 3", "Limit closes versus near-limit moves", blocks[3]["note"] + " " + NOTE_P))
    T.append(table_md(4, blocks, "Table 4", "Returns before and after the KRX platform change of 5 May 2025", blocks[4]["note"] + " " + NOTE_P))
    T.append(table_md(5, blocks, "Table 5", "Events and overnight gaps by calendar quarter", blocks[5]["note"] + " " + NOTE_P))
    src = src.replace("::: tables\n:::\n", "\n\n".join(T))
    src = re.sub(r"^\| \$\$(.*?)\$\$ \| (\(\d\)) \|$", lambda m: "| $" + m.group(1) + "$ | " + m.group(2) + " |", src, flags=re.M)
    src = minus_fix(src)
    path = os.path.join(WORK, "manuscript_scirep.build.md")
    open(path, "w", encoding="utf-8").write(src)
    out = os.path.join(OUT, "Manuscript_SciRep.docx")
    pandoc(path, out)
    style_docx(out)
    # word counts
    body = src.split("## Introduction")[1].split("## Methods")[0]
    absr = src.split("## Abstract")[1].split("**Keywords")[0]
    print("abstract words:", word_count(absr), "| main text words (Introduction-Discussion):", word_count(body),
          "| references:", len(order))
    return order


# ------------------------------------------------------------------ supplementary information
def f2(x, d=2):
    return (MINUS if x < 0 else "") + f"{abs(x):.{d}f}"


def build_si():
    blocks = msj_blocks()
    order = []
    s = []
    s.append("::: {custom-style=\"Title\"}\nDo price limits delay price discovery? Overnight gaps after limit closes in Vietnam\n:::\n")
    s.append("Ha Hong Hanh, Nguyen Van Trung & Nguyen Thanh Binh\n")
    s.append("**Supplementary Information**\n")
    s.append(PB)
    src = open("/home/user/Black_litterman_2/paper2/manuscript/msj/S1_supplementary.Rmd", encoding="utf-8").read()
    n1 = src.split("## S1.1. Characteristic definitions")[1].split("## S1.2.")[0].strip()
    n2 = src.split("## S1.2. Literature search")[1].split("## References")[0].strip()
    n1 = re.sub(r"\(([A-Z][A-Za-z]+(?: et al\.)?),? (\d{4})\)", lambda m: "⟦" + {"Amihud": "amihud", "Parkinson": "parkinson", "Corwin": "corwin", "Bali": "bali"}[m.group(1).split()[0]] + "⟧", n1)
    n1 = n1.replace("Parkinson (1980)", "Parkinson⟦parkinson⟧").replace("(Amihud, 2002)", "⟦amihud⟧")
    n1 = n1.replace("(Bali et al., 2011)", "⟦bali⟧").replace("Corwin and Schultz (2012)", "Corwin and Schultz⟦corwin⟧")
    n1 = n1.replace("Section 2.2 of the article", "Methods").replace("(Amihud, 2002)", "")
    n2 = n2.replace("with the web search tool of the AI assistant named in Section 6.2 of the article", "with a web search engine").replace("(Section 2.1 of the article)", "(Methods)")
    n2 = n2.replace("(Kim & Rhee, 1997; Huang et al., 2001; Qi, 2023)", "⟦kimrhee,huangy,qi⟧").replace("Farber et al. (2006)", "Farber et al.⟦farber⟧")
    n2 = n2.replace("Le (2012)", "Le⟦le⟧").replace("Table 6 reports their results", "Supplementary Table S1 reports their results")
    n2 = n2.replace("the working paper of Farber et al.⟦farber⟧", "the working paper of Farber et al.⟦farber⟧")
    s.append("## Supplementary Note 1: Characteristic definitions\n\n" + n1 + "\n")
    s.append("## Supplementary Note 2: Literature search\n\n" + n2 + "\n")
    s.append("## Supplementary Tables\n")
    b6 = blocks[6]
    s.append(f"**Supplementary Table S1.** Comparison with earlier studies\n\n" + "\n".join(b6["table"]) + "\n\n" +
             "*Note.* Entries for Kim and Rhee⟦kimrhee⟧, Huang et al.⟦huangy⟧ and Qi⟦qi⟧ report results from the full texts; the other entries summarize each study's abstract.\n")
    # S2: event definitions (C28)
    c28 = pd.read_csv(os.path.join(TAB, "C28_event_definitions.csv"))
    names = {"gap_mkt": "Overnight gap", "intraday_mkt": "Intraday", "cc1_mkt": "Close-to-close", "f5o_mkt": "Open to day *d*+5"}
    rows = ["| Event definition | Overnight gap | Intraday | Close-to-close | Open to day *d*+5 | Events |", "|:---|:---:|:---:|:---:|:---:|:---:|"]
    for d_, g in c28.groupby("definition", sort=False):
        cells = {r.measure: f"{f2(r.mean_pct)} ({f2(r.t_twoway, 1)})" for r in g.itertuples()}
        n = int(g[g.measure == "gap_mkt"].n.iloc[0])
        rows.append(f"| {d_.replace('>=', '≥').replace('<=', '≤')} | " + " | ".join(cells[k] for k in ("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt")) + f" | {n:,} |")
    s.append("**Supplementary Table S2.** Next-day abnormal returns under alternative event definitions\n\n" + "\n".join(rows) +
             "\n\n*Note.* Market-adjusted returns in percent; two-way-clustered *t*-statistics in parentheses (two-sided *P* < 0.001 for |*t*| ≥ 3.29). Source: authors' calculations.\n")
    # S3: family sensitivity (C32)
    c32 = pd.read_csv(os.path.join(TAB, "C32_family_sensitivity.csv"))
    fam = list(dict.fromkeys(c32.family))
    rows = ["| Family definition | Ceiling, *d*+1 | Ceiling, *d*+1 to *d*+5 | Floor, *d*+1 | Floor, *d*+1 to *d*+5 |", "|:---|:---:|:---:|:---:|:---:|"]
    tests = ["ceiling t+1", "ceiling t+1..t+5", "floor t+1", "floor t+1..t+5"]
    for f_ in fam:
        g = c32[c32.family == f_].set_index("test")
        rows.append(f"| {f_.replace('t+', '*d*+').replace('d*+1..*d*+5', 'd*+1 to *d*+5')} | " + " | ".join(f"{g.loc[t_, 'adjusted_p']:.1e}" for t_ in tests) + " |")
    s.append("**Supplementary Table S3.** Adjusted *P* values of the four event tests under alternative family definitions\n\n" + "\n".join(rows) +
             "\n\n*Note.* BH, Benjamini–Hochberg; Holm and Bonferroni as named. All adjusted *P* values are below 0.05. Source: authors' calculations.\n")
    # S4: DiD at platform change (C31)
    c31 = pd.read_csv(os.path.join(TAB, "C31_krx_did.csv"))
    rows = ["| Contrast | Outcome | Excess before the change | *t* | Change after | *t* | Events | Comparison stock-days |", "|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for r in c31.itertuples():
        rows.append(f"| {r.contrast.replace('5-6.5%', '5–6.5%')} | {names.get(r.outcome, r.outcome)} | {f2(r.limit_minus_control_pre_pct)} | {f2(r.t_pre, 1)} | {f2(r.change_after_krx_pct)} | {f2(r.t_change, 1)} | {int(r.n_limit):,} | {int(r.n_control):,} |")
    s.append("**Supplementary Table S4.** Difference-in-differences around the KRX platform change of 5 May 2025\n\n" + "\n".join(rows) +
             "\n\n*Note.* Percentage points; date-clustered *t*-statistics; limit closes compared with 5–6.5% movers that also closed at the extreme. Source: authors' calculations.\n")
    text = "\n".join(s)
    text = cite_numbers(text, order)
    text += "\n## Supplementary references\n\n" + "\n".join(f"{i + 1}. {RF.fmt_ref(k)}" for i, k in enumerate(order)) + "\n"
    text = minus_fix(text)
    path = os.path.join(WORK, "si.build.md")
    open(path, "w", encoding="utf-8").write(text)
    out = os.path.join(OUT, "Supplementary_Information.docx")
    pandoc(path, out)
    style_docx(out, line_numbers=False, base_pt=11, spacing=1.15)


if __name__ == "__main__":
    build_main()
    build_si()
