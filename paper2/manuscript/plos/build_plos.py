# Build the PLOS ONE version of the manuscript from manuscript_final.Rmd.
# Output: manuscript_plos.Rmd (main file) and S1_Appendix.Rmd (supporting information).
# Numbers stay as inline R calls; only layout, citation style, headings and inline-math typography change.
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "manuscript_final.Rmd")
s = open(SRC, encoding="utf-8").read()

# ---------- split the source ----------
i_setup_end = s.index("```", s.index("```{r setup")) + 3
i_setup_end = s.index("```", i_setup_end) + 3          # end of setup chunk
setup = s[s.index("```{r setup"):i_setup_end]
body = s[i_setup_end:s.index("# Declarations")]
refs_txt = s[s.index("# References") + len("# References"):s.index("# Appendix A")]
appA = s[s.index("# Appendix A"):s.index("# Appendix B")]
appB = s[s.index("# Appendix B"):]

# ---------- references: parse APA entries ----------
entries = [e.strip() for e in refs_txt.strip().split("\n\n") if e.strip()]

def initials(x):
    return "".join(re.findall(r"[A-Z]", x))

def parse_authors(a):
    a = a.replace(", & ", ", ").replace(" & ", ", ")
    parts = [p.strip() for p in a.split(",")]
    out, k = [], 0
    while k < len(parts):
        sur = parts[k]; ini = parts[k + 1] if k + 1 < len(parts) else ""
        k += 2
        suffix = ""
        if k < len(parts) and parts[k] in ("Jr.",):
            suffix = " Jr"; k += 1
        out.append(f"{sur} {initials(ini)}{suffix}")
    return out

REFS = {}   # key -> dict
for e in entries:
    m = re.match(r"^(?P<auth>.+?) \((?P<yr>\d{4})\)\. (?P<body>.+)$", e)
    assert m, e
    auth, yr, rest = m["auth"], m["yr"], m["body"]
    if auth == "HSC.":
        key = ("HSC", yr)
        van = ("Ho Chi Minh City Securities Corporation. Important changes of new trading system [Internet]. "
               "Ho Chi Minh City: Ho Chi Minh City Securities Corporation; 2025 [cited 2026 Oct 5]. "
               "Available from: https://www.hsc.com.vn/en/important-changes-of-new-trading-system")
    elif auth == "Viet Nam News.":
        key = ("Viet Nam News", yr)
        van = ("Viet Nam News. KRX system officially goes live. Viet Nam News. 2025 [cited 2026 Oct 5]. "
               "Available from: https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html")
    else:
        mm = re.match(r"^(?P<title>.+?[.?]) \*(?P<jour>[^*]+?)(?:, (?P<vol>\d[^*,]*))?\*(?P<rest>.*)$", rest)
        assert mm, rest
        title = mm["title"].rstrip(".")
        jour = re.sub(r"^The ", "", mm["jour"])
        vol = mm["vol"] or ""
        r2 = mm["rest"].strip()
        doi = None
        md = re.search(r"https://doi.org/(\S+)$", r2)
        if md:
            doi = md.group(1); r2 = r2[:md.start()].strip()
        r2 = r2.rstrip(".")
        iss = ""; pages = ""
        mi = re.match(r"^\(([^)]+)\)(.*)$", r2)
        if mi:
            iss = mi.group(1); r2 = mi.group(2)
        pages = r2.lstrip(", ").strip()
        al = parse_authors(auth)
        astr = ", ".join(al[:6]) + (", et al" if len(al) > 6 else "")
        end = "" if title.endswith("?") else "."
        van = f"{astr}. {title}{end} {jour}. {yr};{vol}" + (f"({iss})" if iss else "") + (f": {pages}" if pages else "") + "."
        if doi: van += f" doi: {doi}"
        key = (al[0].split(" ")[0] if not al[0].startswith("O'") else al[0].split(" ")[0], yr)
        # surname may contain spaces? none here; first token is the surname
        key = (re.match(r"^(\S+)", auth).group(1).rstrip(","), yr)
    assert key not in REFS, key
    REFS[key] = {"van": van, "apa": e}

def lookup(name, yr):
    name = name.strip()
    if "Ho Chi Minh City Securities Corporation" in name or name == "HSC":
        k = ("HSC", yr)
    elif name.startswith("Viet Nam News"):
        k = ("Viet Nam News", yr)
    else:
        sur = re.split(r" and | & | et al\.", name)[0].strip()
        sur = sur.split(" ")[-1] if sur.count(" ") and not sur.startswith("Viet") else sur
        k = (sur, yr)
    if k not in REFS:
        raise KeyError(f"citation not found: {name} {yr}")
    return k

NAME = r"[A-Z][\w'’\-]+"
NARR = re.compile(rf"\b({NAME}(?: and {NAME}| et al\.)?) \((\d{{4}})\)")
PAREN = re.compile(r"\(([^()]*?, \d{4}[^()]*?)\)")

def cite_items(inner):
    """Split a parenthetical group into (text_items, keys)."""
    texts, keys = [], []
    for it in [x.strip() for x in inner.split(";")]:
        m = re.match(r"^(.+?), (\d{4})$", it)
        if m:
            keys.append(lookup(m.group(1), m.group(2)))
        else:
            texts.append(it)
    return texts, keys

def find_order(text):
    order = []
    pos = 0
    # collect (position, key) from both patterns
    hits = []
    for m in NARR.finditer(text):
        hits.append((m.start(), [lookup(m.group(1), m.group(2))]))
    for m in PAREN.finditer(text):
        _, ks = cite_items(m.group(1))
        if ks: hits.append((m.start(), ks))
    for _, ks in sorted(hits, key=lambda h: h[0]):
        for k in ks:
            if k not in order: order.append(k)
    return order

def compress(nums):
    nums = sorted(set(nums)); out = []; k = 0
    while k < len(nums):
        j = k
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
        out.append(f"{nums[k]}–{nums[j]}" if j - k >= 2 else (f"{nums[k]},{nums[j]}" if j > k else f"{nums[k]}"))
        k = j + 1
    return "[" + ",".join(out) + "]"

def replace_cites(text, num):
    def rp(m):
        texts, ks = cite_items(m.group(1))
        if not ks: return m.group(0)
        tag = compress([num[k] for k in ks])
        if texts:
            t = "; ".join(texts)
            if t.startswith("Ho Chi Minh City Securities Corporation"):
                t = "Ho Chi Minh City Securities Corporation, HSC"
            return f"({t}) {tag}"
        return tag
    text = PAREN.sub(rp, text)
    def rn(m):
        k = lookup(m.group(1), m.group(2)); return f"{m.group(1)} [{num[k]}]"
    text = NARR.sub(rn, text)
    return text

# ---------- inline math -> Unicode text (PLOS: no equation objects for symbols in running text) ----------
SYM = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "tau": "τ", "varepsilon": "ε", "Phi": "Φ",
       "geq": "≥", "leq": "≤", "approx": "≈", "cdot": "·", "dots": "…", "lfloor": "⌊", "rfloor": "⌋",
       "lceil": "⌈", "rceil": "⌉", "sum": "Σ", "times": "×", "min": "min"}
COMB = {"hat": "\u0302", "widehat": "\u0302", "overline": "\u0304", "tilde": "\u0303"}

def readgroup(x, i):
    if i < len(x) and x[i] == "{":
        d = 0
        for j in range(i, len(x)):
            if x[j] == "{": d += 1
            elif x[j] == "}":
                d -= 1
                if d == 0: return x[i + 1:j], j + 1
        raise ValueError(x)
    if i < len(x) and x[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", x[i:]); return m.group(0), i + len(m.group(0))
    return x[i], i + 1

def plain(x):
    # plain characters of a group (for accents)
    x = re.sub(r"\\(text|mathrm|operatorname)\{([^}]*)\}", r"\2", x)
    for k, v in SYM.items(): x = x.replace("\\" + k, v)
    return x

def conv(x, script=False):
    out = []; i = 0
    def last_sig():
        t = "".join(out).rstrip()
        return t[-1] if t else ""
    while i < len(x):
        c = x[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", x[i:]); cmd = m.group(1); i += len(m.group(0))
            if cmd in ("text", "mathrm", "operatorname"):
                g, i = readgroup(x, i); out.append(g)
            elif cmd in COMB:
                g, i = readgroup(x, i); p = plain(g)
                acc = p[0] + COMB[cmd] + p[1:]
                out.append(f"*{acc}*" if len(p) == 1 and p.isalpha() and p.isascii() else acc)
            elif cmd in SYM:
                out.append(SYM[cmd])
            elif cmd in (",", ";"):
                out.append("" if script else " ")
            elif cmd in ("!", "left", "right"):
                pass
            else:
                raise ValueError("unknown command " + cmd)
        elif c in "_^":
            g, i = readgroup(x, i + 1)
            inner = conv(g, True).replace(" ", "")
            d = "~" if c == "_" else "^"
            out.append(f"{d}{inner}{d}")
        elif c.isalpha() and c.isascii():
            out.append(f"*{c}*"); i += 1
        elif c == "-":
            prev = last_sig()
            unary = prev in ("", "(", "=", "≤", "≥", "<", ">", "/", "^", "~") or script
            out.append("−" if (unary or script) else " − "); i += 1
        elif c in "+=<>" and not script:
            out.append(f" {c} "); i += 1
        elif c in "{}":
            i += 1
        else:
            out.append(c); i += 1
    r = "".join(out)
    r = re.sub(r" {2,}", " ", r)
    r = r.replace("( ", "(").replace(" )", ")")
    return r.strip()

def inline_math(text):
    # skip code chunks and inline code; convert $...$ (not $$)
    parts = re.split(r"(```.*?```|`[^`]*`|\$\$.*?\$\$)", text, flags=re.S)
    for k, p in enumerate(parts):
        if k % 2 == 0:
            parts[k] = re.sub(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", lambda m: conv(m.group(1)), p)
    return "".join(parts)

# ---------- structural edits of the main text ----------
b = body
abstract_m = re.search(r"\*\*Abstract\.\*\* (.+?)\n", b)
abstract = abstract_m.group(1).replace(" (Appendix B)", "")
b = b[abstract_m.end():]
b = re.sub(r"\*\*Keywords:\*\*.*?\n", "", b)
b = re.sub(r"\*\*JEL classification:\*\*.*?\n", "", b)

def rep(old, new, cnt=1):
    global b
    assert b.count(old) == cnt, (old, b.count(old)); b = b.replace(old, new)

rep("# 1. Introduction", "# Introduction")
rep("# 2. Related literature and hypotheses", "## Related literature and hypotheses")
rep("# 3. Data and institutional setting", "# Materials and methods\n\n## Data and institutional setting")
rep("# 4. Design", "## Research design")
rep("# 5. Results", "# Results")
rep("# 6. Discussion", "# Discussion")
rep("# 7. Limitations", "## Limitations")
rep("# 8. Conclusion", "# Conclusions")
rep("Section 2 reviews the literature, Sections 3 and 4 describe the data and design, Section 5 reports the results, Section 6 discusses them, and Sections 7 and 8 provide limitations and conclusions.",
    "The rest of the Introduction reviews the literature and states the hypotheses. Materials and methods describes the data and the design, Results reports the estimates, Discussion interprets them and lists the limitations, and Conclusions summarizes.")
rep("(a ceiling close; Section 4)", "(a ceiling close; see Materials and methods)")
rep("the search described in Appendix B", "the search described in S1 Appendix")
rep("our search (Appendix B)", "our search (S1 Appendix)", 2)
rep("(see Section 7 on vendor price adjustment)", "(see Limitations on vendor price adjustment)")
rep("diagnostic only (Section 7)", "diagnostic only (see Limitations)")
rep("Section 5 reports the event tests under alternative family definitions", "Results reports the event tests under alternative family definitions")
rep("Appendix A defines the 22", "S1 Appendix defines the 22")
rep("(Section 4)", "(see Materials and methods)")
rep("repository table C31", "table C31 in S1 File")
rep("repository table C32", "table C32 in S1 File")
rep("repository table C28", "table C28 in S1 File")
rep("Figure 1 plots", "Fig 1 plots")
rep("Figure 2 plots", "Fig 2 plots")

# statistical reporting additions required by PLOS (software, alpha, sidedness)
rep("with date-clustered HC1 standard errors (R package *sandwich*).",
    "with date-clustered HC1 standard errors (R package *sandwich*). All tests are two-sided, and the significance level is 5% unless stated otherwise.")
analysis_plan_end = b.index("**Analysis plan.**")
ap_par_end = b.index("\n\n", analysis_plan_end)
software = ("\n\n**Software and code.** All computations use R version 4.3.3 with the packages sandwich 3.1.0 (cluster-robust "
            "covariance), lmtest 0.9.40, ggplot2 3.4.4 (figures), knitr 1.45, and rmarkdown 2.25. Prices were downloaded with the "
            "vnstock Python library 4.0.4. One script (`paper2/R/run_all.R`) reproduces every number, table, and figure with fixed "
            "seeds; the code and the output tables are in the public repository https://github.com/trungcandygit/black_litterman_2 "
            "(folder `paper2/`), and the output tables are also provided as S1 File.")
b = b[:ap_par_end] + software + b[ap_par_end:]

# figures: drop the image chunks, insert PLOS captions right after the paragraph that first cites the figure
fig1 = re.search(r"```\{r fig1, fig.cap=\"(.*?)\"\}\n.*?```\n", b, flags=re.S)
cap1 = fig1.group(1); b = b[:fig1.start()] + b[fig1.end():]
fig2 = re.search(r"```\{r fig2, fig.cap=\"(.*?)\"\}\n.*?```\n", b, flags=re.S)
cap2 = fig2.group(1); b = b[:fig2.start()] + b[fig2.end():]

def figcap(cap, n):
    cap = re.sub(r"^Figure \d+\. ", "", cap).replace("Appendix A", "S1 Appendix")
    m = re.match(r"^(.*?\.)\s+(.*)$", cap)
    title, legend = (m.group(1), m.group(2)) if m else (cap, "")
    return f"**Fig {n}. {title}**\n{legend}" if legend else f"**Fig {n}. {title}**"

def insert_after_par(text, anchor, block):
    i = text.index(anchor); j = text.index("\n\n", i)
    return text[:j] + "\n\n" + block + text[j:]

cap1 = cap1.replace("for the 22 characteristics in the full sample, the discovery half (first 39 weeks), and the confirmation half, ordered by absolute full-sample *t*.",
                    "for the 22 characteristics. Estimates for the full sample, the discovery half (first 39 weeks), and the confirmation half, ordered by absolute full-sample *t*.")
assert "for the 22 characteristics. Estimates" in cap1
b = insert_after_par(b, "Fig 1 plots", figcap(cap1, 1))
b = insert_after_par(b, "Fig 2 plots", figcap(cap2, 2))
b = re.sub(r"\n{3,}", "\n\n", b)

# ---------- citations ----------
order = find_order(b)
num = {k: n + 1 for n, k in enumerate(order)}
b = replace_cites(b, num)
left = re.findall(r"\(\d{4}\)|, \d{4}\)", re.sub(r"```.*?```", "", b, flags=re.S))
assert not left, left
unused_main = [k for k in REFS if k not in num]

# ---------- inline math ----------
b = inline_math(b)
abstract = inline_math(abstract)

# ---------- assemble main file ----------
yaml = """---
output:
  word_document:
    reference_docx: plos_reference.docx
    toc: false
---
"""
# tables: title above (bold), legend below the table
setup_plos = setup.replace(
    'kable <- function(x, caption = NULL, ...) { if (!is.null(caption)) cat("\\n\\n", caption, "\\n\\n", sep = ""); print(knitr::kable(x, ...)); cat("\\n\\n") }',
    'kable <- function(x, caption = NULL, ...) { tt <- caption; nt <- NULL\n'
    '  if (!is.null(caption)) { m <- regmatches(caption, regexec("^(Table [0-9]+\\\\. .*?\\\\.)\\\\s+(.*)$", caption, perl = TRUE))[[1]]; if (length(m) == 3) { tt <- m[2]; nt <- m[3] } }\n'
    '  if (!is.null(tt)) cat("\\n\\n**", tt, "**\\n\\n", sep = ""); print(knitr::kable(x, ...)); if (!is.null(nt)) cat("\\n\\n", nt, "\\n\\n", sep = ""); cat("\\n\\n") }')
assert setup_plos != setup, "kable wrapper not replaced"

title_page = r"""**Closing at the limit: Price limits, overnight gaps, and next-day returns on the Ho Chi Minh Stock Exchange**

Short title: Price limit closes and next-day returns in Vietnam

Nguyen Thanh Binh^a^, Nguyen Van Trung^a,\*^, Ha Hong Hanh^b^, Nguyen Bach Diep^a^

^a^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam

^b^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam

\* Corresponding author: Nguyen Van Trung, Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam. Email: kontrungcany@gmail.com. Tel: +84 355 347 831.

**Author details**

Nguyen Thanh Binh: nguyenthanhbinhapd@apd.edu.vn; ORCID 0009-0007-0042-2835

Nguyen Van Trung: kontrungcany@gmail.com; ORCID 0009-0008-3307-6569

Ha Hong Hanh: hanhhh@neu.edu.vn; ORCID 0000-0003-3581-6571

Nguyen Bach Diep: diepnb@apd.edu.vn; ORCID 0009-0003-0967-7528

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Abstract

"""

ack = ("# Acknowledgments\n\nThe authors used Claude (Anthropic), a generative AI assistant, to run the literature searches (S1 Appendix), "
       "write analysis code, draft text, and check numbers against output files. The authors reviewed all AI-assisted output and "
       "are responsible for the content. References and the institutional facts on the Ho Chi Minh Stock Exchange were checked by "
       "web search; exchange circulars were not consulted.\n\n")

reflist = "# References\n\n" + "\n\n".join(f"{n}. {REFS[k]['van']}" for n, k in enumerate(order, 1)) + "\n\n"

si = ("# Supporting information\n\n"
      "**S1 Appendix. Characteristic definitions and literature search.** Definitions of the 22 price- and volume-based "
      "characteristics and the literature search strategy.\n\n"
      "**S1 File. Output tables.** The C-series tables written by the R code (comma-separated files), including the full regression "
      "and family-control results behind every number in the article.\n")

main = yaml + "\n" + setup_plos + "\n\n" + title_page + abstract + "\n\n" + b.strip() + "\n\n" + ack + reflist + si
open(os.path.join(HERE, "manuscript_plos.Rmd"), "w", encoding="utf-8").write(main)

# ---------- S1 Appendix ----------
A = appA.replace("# Appendix A. Characteristic definitions", "## A. Characteristic definitions")
Bt = appB.replace("# Appendix B. Literature search", "## B. Literature search")
Bt = Bt.replace("named in the Declarations", "named in the Acknowledgments of the article").replace("(Section 3)", "(Materials and methods of the article)")
sitxt = A + "\n" + Bt
o2 = find_order(sitxt); n2 = {k: n + 1 for n, k in enumerate(o2)}
sitxt = inline_math(replace_cites(sitxt, n2))
si_doc = ("---\noutput:\n  word_document:\n    reference_docx: plos_reference.docx\n---\n\n"
          "**S1 Appendix. Characteristic definitions and literature search.**\n\n"
          "Supporting information for: Closing at the limit: Price limits, overnight gaps, and next-day returns on the Ho Chi Minh Stock Exchange.\n\n"
          + sitxt.strip() + "\n\n## References\n\n" + "\n\n".join(f"{n}. {REFS[k]['van']}" for n, k in enumerate(o2, 1)) + "\n")
open(os.path.join(HERE, "S1_Appendix.Rmd"), "w", encoding="utf-8").write(si_doc)

print("main refs:", len(order), "| SI refs:", len(o2), "| unused in main:", unused_main)
print("only in SI:", [k for k in o2 if k not in num])
print("unused anywhere:", [k for k in REFS if k not in num and k not in n2])
