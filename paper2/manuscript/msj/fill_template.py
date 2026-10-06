# Pour the rendered manuscript (manuscript_msj.docx) into the Malque MSJ Word template without touching
# the template's header, footer, logo, title block layout, or abstract box.
# Usage: python3 fill_template.py template.docx manuscript_msj.docx out.docx
import sys, os, re, copy, zipfile, shutil, tempfile, subprocess
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
def w(t): return f"{{{W}}}{t}"
NS = {"w": W, "m": M, "r": R, "a": A, "wp": WP}

TITLE = "Closing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange"
AUTHORS = [("Nguyen Thanh Binh", "a", "0009-0007-0042-2835", None),
           ("Nguyen Van Trung", "a", "0009-0008-3307-6569", "kontrungcany@gmail.com"),
           ("Ha Hong Hanh", "b", "0000-0003-3581-6571", None),
           ("Nguyen Bach Diep", "a", "0009-0003-0967-7528", None)]
AFFIL = {"a": "Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam.",
         "b": "School of Accounting and Auditing, National Economics University, Hanoi, Vietnam."}

tpl, src, out = sys.argv[1:4]
work = tempfile.mkdtemp()
with zipfile.ZipFile(tpl) as z: z.extractall(os.path.join(work, "t"))
for root, dirs, files in os.walk(work):        # untrusted archive: drop symlinks
    for f in files:
        if os.path.islink(os.path.join(root, f)): os.remove(os.path.join(root, f))
SKILL = "/root/.claude/skills/synced/11ca11bc-7d88-45be-9e04-b817164dcbde_3e245f0b-fa23-48e9-adc5-8ce4eb7e3507/docx/scripts"
subprocess.run([sys.executable, os.path.join(SKILL, "merge_runs.py"), os.path.join(work, "t")], check=True, capture_output=True)

dpath = os.path.join(work, "t", "word", "document.xml")
tree = etree.parse(dpath); doc = tree.getroot(); body = doc.find(w("body"))
rels_path = os.path.join(work, "t", "word", "_rels", "document.xml.rels")
rels = etree.parse(rels_path); rroot = rels.getroot()

def text(el): return "".join(t.text or "" for t in el.iter(w("t")))
def new_rel(target):
    ids = [int(re.sub(r"\D", "", r.get("Id"))) for r in rroot]
    rid = f"rId{max(ids) + 1}"
    e = etree.SubElement(rroot, f"{{{PR}}}Relationship"); e.set("Id", rid)
    e.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"); e.set("Target", target); e.set("TargetMode", "External")
    return rid
max_docpr = [max(int(d.get("id")) for d in doc.iter(f"{{{WP}}}docPr"))]
def fresh_ids(el):
    for d in el.iter(f"{{{WP}}}docPr"):
        max_docpr[0] += 1; d.set("id", str(max_docpr[0]))

# ---------- 1. title ----------
tp = [p for p in doc.iter(w("p")) if text(p).startswith("Only the first letter of the first word")][0]
runs = tp.findall(w("r")); runs[0].find(w("t")).text = TITLE
for r in runs[1:]: tp.remove(r)

# ---------- 2. authors (one paragraph in the template) ----------
ap = [p for p in doc.iter(w("p")) if "Author's full name" in text(p)][0]
rs = ap.findall(w("r"))
name_r = next(r for r in rs if "Author's full name" in text(r))
sup_r = next(r for r in rs if r.find(f"{w('rPr')}/{w('vertAlign')}") is not None and text(r).strip() == "a")
draws = [r for r in rs if r.find(w("drawing")) is not None]
orcid_r = next(r for r in draws if "orcid" in (r.find(f".//{{{WP}}}docPr").get("descr") or "").lower())
env_r = next(r for r in draws if (r.find(f".//{{{WP}}}docPr").get("descr") or "") == "Envelope")
space_r = next(r for r in rs if r.find(f"{w('rPr')}/{w('vertAlign')}") is not None and text(r) == " ")
sep_r = next(r for r in rs if text(r).strip() == "|")
for r in rs: ap.remove(r)
def set_link(run, rid):
    for h in run.iter(f"{{{A}}}hlinkClick"): h.set(f"{{{R}}}id", rid)
for k, (nm, af, orc, mail) in enumerate(AUTHORS):
    r = copy.deepcopy(name_r); r.find(w("t")).text = (" " if k else "") + nm; r.find(w("t")).set("{http://www.w3.org/XML/1998/namespace}space", "preserve"); ap.append(r)
    r = copy.deepcopy(sup_r); r.find(w("t")).text = af; ap.append(r)
    r = copy.deepcopy(orcid_r); fresh_ids(r); set_link(r, new_rel(f"https://orcid.org/{orc}")); ap.append(r)
    if mail:
        ap.append(copy.deepcopy(space_r))
        r = copy.deepcopy(env_r); fresh_ids(r); set_link(r, new_rel(f"mailto:{mail}")); ap.append(r)
    if k < len(AUTHORS) - 1:
        r = copy.deepcopy(sep_r); r.find(w("t")).text = " |"; ap.append(r)

# ---------- 3. affiliations ----------
aff = [p for p in doc.iter(w("p")) if "Institutional affiliation and country of the" in text(p)]
for p in aff:
    rr = p.findall(w("r")); letter = text(rr[0]).strip()
    if letter in AFFIL:
        rr[1].find(w("t")).text = AFFIL[letter]
        for r in rr[2:]: p.remove(r)
    else:
        nxt = p.getnext()
        if nxt is not None and nxt.tag == w("p") and not text(nxt).strip() and nxt.find(f".//{w('sectPr')}") is None:
            nxt.getparent().remove(nxt)
        if p.find(f".//{w('sectPr')}") is not None:   # paragraph mark carries the title-page section break: keep it, empty it
            for r in p.findall(w("r")): p.remove(r)
        else:
            p.getparent().remove(p)
# drop an empty spacer left after the last kept affiliation if it directly follows another empty spacer
# (keeps the template's own spacing otherwise)

# ---------- 4. read the rendered manuscript ----------
with zipfile.ZipFile(src) as z: sx = etree.fromstring(z.read("word/document.xml"))
sbody = sx.find(w("body"))
abstract = keywords = None
for p in sbody.findall(w("p")):
    t = text(p)
    if t.startswith("[[ABSTRACT]]"): abstract = t.replace("[[ABSTRACT]]", "").strip()
    if t.startswith("[[KEYWORDS]]"): keywords = t.replace("[[KEYWORDS]]", "").strip()
assert abstract and keywords

# ---------- 5. abstract box (both the DrawingML and the VML fallback copies) ----------
for box in doc.iter(w("txbxContent")):
    ps = box.findall(w("p"))
    a_p = next(p for p in ps if text(p).startswith("Abstract"))
    ar = a_p.findall(w("r")); ar[1].find(w("t")).text = " " + abstract
    ar[1].find(w("t")).set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for r in ar[2:]: a_p.remove(r)
    for p in ps:
        if text(p).startswith("Calibri font, size 10") or text(p).startswith("300 words"): box.remove(p)
    k_p = next(p for p in box.findall(w("p")) if text(p).startswith("Keywords"))
    kr = k_p.findall(w("r")); kr[2].find(w("t")).text = " " + keywords + "."
    for r in kr[3:]: k_p.remove(r)
# box height: about 118 characters per line of Calibri 10 across 17.6 cm, 12.2 pt per line, plus padding
lines = len(abstract) / 112 + 1 + len(keywords) / 112 + 1 + 1.5
h_pt = int(lines * 12.6 + 14)
for ext in list(doc.iter(f"{{{WP}}}extent")) + list(doc.iter(f"{{{A}}}ext")):
    if ext.get("cx") == "6477000": ext.set("cy", str(h_pt * 12700))
for sh in doc.iter("{urn:schemas-microsoft-com:vml}shape"):
    if "height:168pt" in (sh.get("style") or ""): sh.set("style", sh.get("style").replace("height:168pt", f"height:{h_pt}pt"))

# ---------- 6. template paragraph prototypes ----------
allp = list(body.iter(w("p")))
def proto(pred): return copy.deepcopy(next(p for p in allp if pred(text(p))))
P_BODY = proto(lambda t: t.startswith("Insert text (Calibri font, size 10"))
P_H1 = proto(lambda t: t == "6. Declarations")
P_H2 = proto(lambda t: t == "6.1. Ethical considerations")
P_REFH = proto(lambda t: t == "References")
P_REF = proto(lambda t: t.startswith("Smith, J. A. (2019). Effects of sleep"))
P_FCAP = proto(lambda t: t.startswith("Figure 1 Insert text"))
P_TCAP = proto(lambda t: t.startswith("Table 1 Insert text"))
P_NOTE = proto(lambda t: t.startswith("Source: Smith (2022)"))
TBL = copy.deepcopy(next(t for t in body.iter(w("tbl")) if "Rainfall" in text(t)))

def first_rpr(p, i=0):
    rr = p.findall(w("r")); rp = rr[i].find(w("rPr"))
    return copy.deepcopy(rp) if rp is not None else etree.Element(w("rPr"))
BODY_RPR = first_rpr(P_BODY); REF_RPR = first_rpr(P_REF, 0); REF_IT = first_rpr(P_REF, 1)
H1_RPR = first_rpr(P_H1); H2_RPR = first_rpr(P_H2); RH_RPR = first_rpr(P_REFH)
FC_L, FC_T = first_rpr(P_FCAP, 0), first_rpr(P_FCAP, 1); TC_L, TC_T = first_rpr(P_TCAP, 0), first_rpr(P_TCAP, 1)
NOTE_RPR = first_rpr(P_NOTE, 1)
for rp in (BODY_RPR, REF_RPR, NOTE_RPR, FC_T, TC_T):
    for tag in ("b", "bCs", "i", "iCs", "vertAlign", "u"):
        for e in rp.findall(w(tag)): rp.remove(e)

def empty_like(p):
    q = copy.deepcopy(p)
    for c in list(q):
        if c.tag != w("pPr"): q.remove(c)
    ppr = q.find(w("pPr"))
    if ppr is not None:
        for e in ppr.findall(w("numPr")): ppr.remove(e)
    return q

def mk_run(rpr, txt, italic=False, valign=None):
    r = etree.Element(w("r")); rp = copy.deepcopy(rpr)
    if italic: rp.append(etree.Element(w("i")))
    if valign is not None: va = etree.SubElement(rp, w("vertAlign")); va.set(w("val"), valign)
    r.append(rp); t = etree.SubElement(r, w("t")); t.text = txt; t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return r

def convert_runs(src_p, dst_p, base_rpr, it_rpr=None):
    """copy text, italics, sub/superscripts, inline math from a pandoc paragraph"""
    def handle(node):
        for c in node:
            if c.tag == w("r"):
                rp = c.find(w("rPr")); it = rp is not None and rp.find(w("i")) is not None
                va = rp.find(w("vertAlign")).get(w("val")) if rp is not None and rp.find(w("vertAlign")) is not None else None
                for cc in c:
                    if cc.tag == w("t"):
                        if it and it_rpr is not None: dst_p.append(mk_run(it_rpr, cc.text or "", False, va))
                        else: dst_p.append(mk_run(base_rpr, cc.text or "", it, va))
                    elif cc.tag in (w("tab"), w("br")):
                        r = etree.Element(w("r")); r.append(copy.deepcopy(base_rpr)); r.append(copy.deepcopy(cc)); dst_p.append(r)
            elif c.tag == w("hyperlink") or c.tag == w("smartTag"):
                handle(c)
            elif c.tag in (f"{{{M}}}oMath", f"{{{M}}}oMathPara"):
                dst_p.append(copy.deepcopy(c))
    handle(src_p)

def heading(proto_p, rpr, txt):
    q = empty_like(proto_p); q.append(mk_run(rpr, txt)); return q

# ---------- 7. build the new body ----------
anchor = next(p for p in body if p.tag == w("p") and p.find(f".//{w('txbxContent')}") is not None)
final_sect = body.find(w("sectPr"))
for el in list(body):
    if el is anchor or el is final_sect: continue
    if list(body).index(el) > list(body).index(anchor): body.remove(el)
# the template shows the title block alone on page 1 and the abstract box at the top of page 2;
# with four authors the title table is shorter, so keep that layout with an explicit page break before the box paragraph
appr = anchor.find(w("pPr"))
if appr.find(w("pageBreakBefore")) is None:
    pb = etree.Element(w("pageBreakBefore")); kids = list(appr)
    appr.insert(1 if kids and kids[0].tag == w("pStyle") else 0, pb)
new = []
blank = lambda: empty_like(P_BODY)
in_refs = False; after_table = False; first_fig = True
for el in sbody:
    if el.tag == w("sectPr"): continue
    if el.tag == w("tbl"):
        t = copy.deepcopy(el); new.append(t); after_table = True; continue
    t = text(el); sty = el.find(f"{w('pPr')}/{w('pStyle')}"); sty = sty.get(w("val")) if sty is not None else ""
    if t.startswith("[[ABSTRACT]]") or t.startswith("[[KEYWORDS]]"): continue
    if sty == "Heading1":
        if t in ("Figures", "Tables"):
            in_refs = False; continue
        if t == "References":
            new += [blank(), heading(P_REFH, RH_RPR, t), blank()]; in_refs = True; continue
        new += [blank(), heading(P_H1, H1_RPR, t), blank()]; continue
    if sty == "Heading2":
        new += [blank(), heading(P_H2, H2_RPR, t), blank()]; continue
    if t.startswith("[[FIG:"):
        q = empty_like(P_FCAP); r = mk_run(BODY_RPR, t); q.append(r)
        if first_fig:
            q.find(w("pPr")).insert(0, etree.Element(w("pageBreakBefore"))); first_fig = False
        new.append(q); continue
    mm = re.match(r"^(Figure|Table) (\d+) (.*)$", t, flags=re.S)
    if mm and not in_refs:
        isfig = mm.group(1) == "Figure"
        q = empty_like(P_FCAP if isfig else P_TCAP)
        if not isfig: new.append(blank())
        q.append(mk_run(FC_L if isfig else TC_L, f"{mm.group(1)} {mm.group(2)}"))
        tmp = etree.Element(w("p")); convert_runs(el, tmp, FC_T if isfig else TC_T)
        # drop the "Figure n " / "Table n " prefix from the converted runs
        pref = f"{mm.group(1)} {mm.group(2)}"
        for r in tmp.findall(w("r")):
            tt = r.find(w("t"))
            if tt is not None and tt.text and tt.text.startswith(pref):
                tt.text = " " + tt.text[len(pref):].lstrip(); break
        for c in tmp: q.append(c)
        new.append(q)
        if isfig: new.append(blank())
        continue
    if t.startswith("[[NOTE]]"):
        q = empty_like(P_NOTE); ind = q.find(f"{w('pPr')}/{w('ind')}")
        if ind is not None: q.find(w("pPr")).remove(ind)
        jc = etree.SubElement(q.find(w("pPr")), w("jc")); jc.set(w("val"), "both")
        convert_runs(el, q, NOTE_RPR)
        for r in q.findall(w("r")):
            tt = r.find(w("t"))
            if tt is not None and "[[NOTE]]" in (tt.text or ""): tt.text = tt.text.replace("[[NOTE]] ", "").replace("[[NOTE]]", "")
        new.append(q); continue
    if el.find(f".//{{{M}}}oMathPara") is not None:
        q = copy.deepcopy(el); ppr = q.find(w("pPr"))
        if ppr is not None:
            for e in ppr.findall(w("pStyle")): ppr.remove(e)
        new.append(q); continue
    if in_refs:
        q = empty_like(P_REF); convert_runs(el, q, REF_RPR, REF_IT); new.append(q); continue
    if not t.strip(): continue
    q = empty_like(P_BODY); convert_runs(el, q, BODY_RPR); new.append(q)
pos = list(body).index(anchor) + 1
for i, e in enumerate(new): body.insert(pos + i, e)

# ---------- 8. tables: template look (rules above/below the header and at the end), Calibri 8 ----------
tbl_pr_proto = TBL.find(w("tblPr"))
new_tbls = [e for e in new if e.tag == w("tbl")]
for t in new_tbls:
    tp_ = t.find(w("tblPr"))
    for e in list(tp_):
        if e.tag in (w("tblStyle"), w("tblLook"), w("tblBorders")): tp_.remove(e)
    tw = tp_.find(w("tblW"))
    if tw is None: tw = etree.SubElement(tp_, w("tblW"))
    tw.set(w("type"), "pct"); tw.set(w("w"), "5000")
    jc = tp_.find(w("jc"))
    if jc is None: jc = etree.SubElement(tp_, w("jc"))
    jc.set(w("val"), "center")
    rows = t.findall(w("tr"))
    for ri, tr in enumerate(rows):
        trpr = tr.find(w("trPr"))
        if trpr is None: trpr = etree.Element(w("trPr")); tr.insert(0, trpr)
        if ri == 0 and trpr.find(w("tblHeader")) is None: trpr.append(etree.Element(w("tblHeader")))
        if trpr.find(w("cantSplit")) is None: trpr.append(etree.Element(w("cantSplit")))
        for tc in tr.findall(w("tc")):
            tcpr = tc.find(w("tcPr"))
            if tcpr is None: tcpr = etree.Element(w("tcPr")); tc.insert(0, tcpr)
            for e in tcpr.findall(w("tcBorders")): tcpr.remove(e)
            bd = etree.SubElement(tcpr, w("tcBorders"))
            def edge(name, sz):
                e = etree.SubElement(bd, w(name)); e.set(w("val"), "single"); e.set(w("sz"), str(sz)); e.set(w("space"), "0"); e.set(w("color"), "000000")
            if ri == 0: edge("top", 8); edge("bottom", 6)
            if ri == len(rows) - 1: edge("bottom", 8)
            for p in tc.findall(w("p")):
                ppr = p.find(w("pPr"))
                if ppr is None: ppr = etree.Element(w("pPr")); p.insert(0, ppr)
                for e in ppr.findall(w("pStyle")): ppr.remove(e)
                for e in ppr.findall(w("spacing")): ppr.remove(e)
                sp = etree.SubElement(ppr, w("spacing")); sp.set(w("before"), "10"); sp.set(w("after"), "10"); sp.set(w("line"), "240"); sp.set(w("lineRule"), "auto")
                for r in p.iter(w("r")):
                    rp = r.find(w("rPr"))
                    if rp is None: rp = etree.Element(w("rPr")); r.insert(0, rp)
                    for e in rp.findall(w("rStyle")) + rp.findall(w("b")) + rp.findall(w("bCs")) + rp.findall(w("sz")) + rp.findall(w("rFonts")): rp.remove(e)
                    f = etree.Element(w("rFonts")); f.set(w("asciiTheme"), "minorHAnsi"); f.set(w("hAnsiTheme"), "minorHAnsi"); f.set(w("cstheme"), "minorHAnsi"); rp.insert(0, f)
                    s = etree.SubElement(rp, w("sz")); s.set(w("val"), "16"); s2 = etree.SubElement(rp, w("szCs")); s2.set(w("val"), "16")
                for h in list(p.findall(w("hyperlink"))):
                    for c in list(h): p.insert(list(p).index(h), c)
                    p.remove(h)

# ---------- schema order of property children ----------
ORDER = {
 "pPr": "pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange",
 "rPr": "rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow emboss imprint noProof snapToGrid vanish webHidden color spacing w kern position sz szCs highlight u effect bdr shd fitText vertAlign rtl cs em lang eastAsianLayout specVanish oMath",
 "tblPr": "tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd tblLayout tblCellMar tblLook tblCaption tblDescription",
 "trPr": "cnfStyle divId gridBefore gridAfter wBefore wAfter cantSplit trHeight tblHeader tblCellSpacing jc hidden",
 "tcPr": "cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar textDirection tcFitText vAlign hideMark",
}
MORDER = {"dPr": "begChr sepChr endChr grow shp ctrlPr", "rPr": "lit nor scr sty brk aln"}
for rp in doc.iter(f"{{{M}}}rPr"):   # schema: m:nor and m:sty are alternatives
    if rp.find(f"{{{M}}}nor") is not None:
        for e in rp.findall(f"{{{M}}}sty") + rp.findall(f"{{{M}}}scr"): rp.remove(e)
for tag, order in MORDER.items():
    rank = {k: i for i, k in enumerate(order.split())}
    for el in doc.iter(f"{{{M}}}{tag}"):
        kids = list(el)
        if any(etree.QName(k).localname not in rank for k in kids): continue
        kids.sort(key=lambda k: rank[etree.QName(k).localname])
        for k in kids: el.remove(k)
        for k in kids: el.append(k)
for tag, order in ORDER.items():
    rank = {k: i for i, k in enumerate(order.split())}
    for el in doc.iter(w(tag)):
        if tag == "rPr" and el.getparent() is not None and el.getparent().tag == w("pPr"): pass
        kids = list(el)
        if any(etree.QName(k).localname not in rank for k in kids if isinstance(k.tag, str)): continue
        kids.sort(key=lambda k: rank[etree.QName(k).localname])
        for k in kids: el.remove(k)
        for k in kids: el.append(k)
tree.write(dpath, xml_declaration=True, encoding="UTF-8", standalone=True)
rels.write(rels_path, xml_declaration=True, encoding="UTF-8", standalone=True)

# ---------- 9. zip, then insert figures and size table columns with python-docx ----------
tmpdocx = os.path.join(work, "tmp.docx")
with zipfile.ZipFile(tmpdocx, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(os.path.join(work, "t")):
        for f in files:
            full = os.path.join(root, f); z.write(full, os.path.relpath(full, os.path.join(work, "t")))
from docx import Document
from docx.shared import Cm
d = Document(tmpdocx)
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(src)), "..", "..", "output")
for p in d.paragraphs:
    mm = re.match(r"^\[\[FIG:(.+)\]\]$", p.text.strip())
    if mm:
        for r in list(p.runs): r._r.getparent().remove(r._r)
        p.add_run().add_picture(os.path.join(FIGDIR, mm.group(1)), width=Cm(16.5))
for t in d.tables[1:]:   # table 0 is the template's title block
    tblPr = t._tbl.tblPr
    lay = tblPr.find(w("tblLayout"))
    if lay is None: lay = etree.SubElement(tblPr, w("tblLayout"))
    lay.set(w("type"), "fixed")
    ncol = len(t.columns); total = 10200
    lens = []
    for j in range(ncol):
        cells = [r.cells[j].text for r in t.rows]
        m = max(max((len(x) for x in c.split(" ")), default=1) for c in cells) + 3
        m = max(m, min(sum(len(c) for c in cells) / len(cells), 60) * 0.5)
        if j == 0: m = max(m, min(max(len(c) for c in cells), 34) * 0.75)
        lens.append(max(m, 5))
    tot = sum(lens); widths = [int(total * l / tot) for l in lens]
    grid = t._tbl.find(w("tblGrid"))
    if grid is not None:
        for gc, wd in zip(grid.findall(w("gridCol")), widths): gc.set(w("w"), str(wd))
    for r in t.rows:
        for j, c in enumerate(r.cells):
            tcPr = c._tc.get_or_add_tcPr(); tcW = tcPr.find(w("tcW"))
            if tcW is None: tcW = etree.Element(w("tcW")); tcPr.insert(0, tcW)
            tcW.set(w("type"), "dxa"); tcW.set(w("w"), str(widths[j]))
# keep captions with their tables and short tables on one page
for p in d.paragraphs:
    if re.match(r"^Table \d+ ", p.text): p.paragraph_format.keep_with_next = True
for t in d.tables[1:]:
    if len(t.rows) <= 24:
        for r in t.rows[:-1]:
            for c in r.cells:
                for p in c.paragraphs: p.paragraph_format.keep_with_next = True
d.save(out)
shutil.rmtree(work)
print("written", out)
