# style_docx.py -- journal styling for the reference docx and post-processing of tables
import sys, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_font(style, name="Times New Roman", size=None, bold=None, color=RGBColor(0, 0, 0), italic=None):
    f = style.font; f.name = name; f.color.rgb = color
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    rpr = style.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]

def make_reference(path):
    d = Document(path)
    for s in d.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7); s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
    for name in ("Normal", "Body Text", "First Paragraph", "Compact", "Table Caption", "Image Caption", "Block Text"):
        st = {x.name: x for x in d.styles}.get(name)
        if st is None: continue
        set_font(st, size=11); pf = st.paragraph_format; pf.line_spacing = 1.15; pf.space_after = Pt(6); pf.space_before = Pt(0)
    byname = {st.name: st for st in d.styles}
    for name, size in (("Title", 16), ("Heading 1", 13), ("Heading 2", 11.5), ("Heading 3", 11)):
        st = byname[name]; set_font(st, size=size, bold=True); st.paragraph_format.space_before = Pt(12); st.paragraph_format.space_after = Pt(4); st.paragraph_format.keep_with_next = True
    byname["Title"].paragraph_format.alignment = 1
    d.save(path)

def borders(cell_or_tbl_pr, **kw):
    pass

def set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr(); b = tcPr.find(qn("w:tcBorders"))
    if b is None: b = OxmlElement("w:tcBorders"); tcPr.append(b)
    for edge, val in kwargs.items():
        el = b.find(qn("w:" + edge))
        if el is None: el = OxmlElement("w:" + edge); b.append(el)
        el.set(qn("w:val"), val.get("val", "single")); el.set(qn("w:sz"), str(val.get("sz", 6))); el.set(qn("w:color"), "000000"); el.set(qn("w:space"), "0")

def style_tables(path, out):
    d = Document(path)
    for t in d.tables:
        tbl = t._tbl; tblPr = tbl.tblPr
        for tag in ("w:tblBorders",):
            e = tblPr.find(qn(tag))
            if e is not None: tblPr.remove(e)
        lay = tblPr.find(qn("w:tblLayout"))
        if lay is None: lay = OxmlElement("w:tblLayout"); tblPr.append(lay)
        lay.set(qn("w:type"), "fixed")
        ncol = len(t.columns); total = 9070  # DXA text width at 2.5 cm margins on A4 (~16 cm)
        # width proportional to the longest cell text, first column wider
        lens = []
        for j in range(ncol):
            m = 0
            for r in t.rows:
                txt = r.cells[j].text
                m = max(m, (max(len(w) for w in txt.split(' ')) + 3) if j > 0 else min(len(txt), 34) * 0.6)
            if j > 0: m = max(m, min(sum(len(r.cells[j].text) for r in t.rows) / len(t.rows), 70) * 0.45)
            lens.append(max(m, 4))
        lens[0] = max(lens[0], 12) * 1.2
        tot = sum(lens); widths = [int(total * l / tot) for l in lens]
        grid = tbl.find(qn("w:tblGrid"))
        if grid is not None:
            for gc, w in zip(grid.findall(qn("w:gridCol")), widths): gc.set(qn("w:w"), str(w))
        tw = tblPr.find(qn("w:tblW"))
        if tw is None: tw = OxmlElement("w:tblW"); tblPr.append(tw)
        tw.set(qn("w:type"), "dxa"); tw.set(qn("w:w"), str(total))
        avg = [sum(len(r.cells[j].text) for r in t.rows) / len(t.rows) for j in range(ncol)]
        for ri, r in enumerate(t.rows):
            trPr = r._tr.get_or_add_trPr()
            if ri == 0:
                h = OxmlElement("w:tblHeader"); trPr.append(h)
            cs = OxmlElement("w:cantSplit"); trPr.append(cs)
            for j, c in enumerate(r.cells):
                tcPr = c._tc.get_or_add_tcPr(); tcW = tcPr.find(qn("w:tcW"))
                if tcW is None: tcW = OxmlElement("w:tcW"); tcPr.insert(0, tcW)
                tcW.set(qn("w:type"), "dxa"); tcW.set(qn("w:w"), str(widths[j]))
                for p in c.paragraphs:
                    p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1); p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.alignment = 0 if (j == 0 or avg[j] > 30) else 1
                    if ri < len(t.rows) - 1 and len(t.rows) <= 12: p.paragraph_format.keep_with_next = True
                    for run in p.runs:
                        run.font.size = Pt(8.5); run.font.name = "Times New Roman"
                        if ri == 0: run.font.bold = True
                if ri == 0: set_cell_border(c, top={"sz": 8}, bottom={"sz": 6})
                if ri == len(t.rows) - 1: set_cell_border(c, bottom={"sz": 8})
    body = d.element.body
    for tb in d.tables:
        nx = tb._tbl.getnext()
        if nx is not None and nx.tag == qn('w:p'):
            ppr = nx.find(qn('w:pPr'))
            if ppr is None: ppr = OxmlElement('w:pPr'); nx.insert(0, ppr)
            sp = ppr.find(qn('w:spacing'))
            if sp is None: sp = OxmlElement('w:spacing'); ppr.append(sp)
            sp.set(qn('w:before'), '160')
    for p in d.paragraphs:  # heading keep-with-next
        if p.style.name.startswith('Heading'): p.paragraph_format.keep_with_next = True
    # caption paragraphs: paragraph directly before a table starting with "Table " keeps with next, 10 pt, not bold
    for p in d.paragraphs:
        if re.match(r"^(Table|Figure) \d+\. ", p.text):
            for run in p.runs: run.font.size = Pt(9.5)
            if p.text.startswith("Table "): p.paragraph_format.keep_with_next = True; p.paragraph_format.space_after = Pt(3)
    d.save(out)

if __name__ == "__main__":
    if sys.argv[1] == "ref": make_reference(sys.argv[2])
    else: style_tables(sys.argv[2], sys.argv[3])
