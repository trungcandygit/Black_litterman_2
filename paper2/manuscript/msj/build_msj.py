# Build the Multidisciplinary Science Journal (Malque) version from manuscript_final.Rmd.
# Output: manuscript_msj.Rmd (rendered by rmarkdown, then poured into the journal template by fill_template.py)
#         S1_supplementary.Rmd (characteristic definitions and literature search).
# Numbers stay as inline R calls.
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, "..", "manuscript_final.Rmd"), encoding="utf-8").read()

i0 = s.index("```{r setup"); i1 = s.index("```", s.index("\n", i0)) + 3
setup = s[i0:i1]
body = s[i1:s.index("# Declarations")]
refs = s[s.index("# References"):s.index("# Appendix A")]
appA = s[s.index("# Appendix A"):s.index("# Appendix B")]
appB = s[s.index("# Appendix B"):]

b = body
m = re.search(r"\*\*Abstract\.\*\* (.+?)\n", b)
abstract = m.group(1)
b = b[m.end():]
b = re.sub(r"\*\*Keywords:\*\*.*?\n", "", b)
b = re.sub(r"\*\*JEL classification:\*\*.*?\n", "", b)

def rep(old, new, cnt=1):
    global b
    assert b.count(old) == cnt, (old, b.count(old)); b = b.replace(old, new)

# ---- abstract: 250-300 words required; added sentences use only saved R outputs ----
abstract = abstract.replace(" (Appendix B)", "")
abstract = abstract.replace(
    "we run 26 tests under false discovery rate control: four price limit event tests and 22 price- and volume-based characteristics.",
    "we run 26 tests under false discovery rate control: four price limit event tests and 22 price- and volume-based characteristics. "
    "About `r f(100 * C13$value[5] / C13$value[1], 1)`% of stock-days close at the upper limit and `r f(100 * C13$value[6] / C13$value[1], 1)`% at the lower limit. "
    "We split the next-day abnormal return into an overnight gap and an intraday return, compare limit closes with stocks that moved almost as far, and cluster standard errors by date, week, and stock.")
abstract = abstract.replace(
    "by `r f(c17(\"ceiling vs 5-6.5% up\",\"gap_mkt\",\"diff_pct\"),1)` percentage points.",
    "by `r f(c17(\"ceiling vs 5-6.5% up\",\"gap_mkt\",\"diff_pct\"),1)` percentage points, and by `r f(c23(\"ceiling vs 5-6.5% up, close = high\",\"gap_mkt\",\"diff_pct\"),1)` points when those stocks also closed at their daily high. "
    "After a floor close the overnight gap is `r f(c16(\"Floor all\",\"gap_mkt\"),1)`%, and the size of the floor effect depends on the benchmark. "
    "The ceiling gap is positive and significant in each of the `r nrow(C29)` calendar quarters and is present before the move of the exchange to a new trading platform in May 2025.")

# ---- headings (journal numbering) ----
rep("# 1. Introduction", "# 1. Introduction")
rep("# 2. Related literature and hypotheses", "## 1.1. Related literature and hypotheses")
rep("# 3. Data and institutional setting", "# 2. Materials and Methods\n\n## 2.1. Data and institutional setting")
rep("# 4. Design", "## 2.2. Research design")
rep("# 5. Results", "# 3. Results")
rep("# 6. Discussion", "# 4. Discussion")
rep("# 7. Limitations", "## 4.1. Limitations")
rep("# 8. Conclusion", "# 5. Conclusions")

# no bold words in the text: run-in heads become italic
b = re.sub(r"(?m)^\*\*([^*\n]+?\.)\*\* ", r"*\1* ", b)

# ---- cross-references ----
rep("Section 2 reviews the literature, Sections 3 and 4 describe the data and design, Section 5 reports the results, Section 6 discusses them, and Sections 7 and 8 provide limitations and conclusions.",
    "")
# length (journal limit 7,500 words including references): drop two paragraphs that repeat other text
b = re.sub(r"\nCeiling closes cover about `r f\(100 \* C13\$value\[5\] / C13\$value\[1\], 1\)`% of stock-days in the event window, and the low-powered characteristic null says little about the cross-section, so we make no claim that limit closes explain the cross-section of returns.\n", "\n", b)
rep("The results support H~1~ to H~4~. The ceiling effect survives alternative benchmarks, clusters, and event definitions and takes the form of a one-day gap with a partial reversal that a buyer at the quoted next open cannot capture. The floor effect combines a gap with drift that appears only before the 2025 platform change, and its size depends on the benchmark.",
    "The results support H~1~ to H~4~ for ceilings; the floor effect depends on the benchmark and its drift appears only before the 2025 platform change.")
rep("(a ceiling close; Section 4)", "(a ceiling close; Section 2.2)")
rep("the search described in Appendix B", "the search described in Supplementary Material S1")
rep("our search (Appendix B)", "our search (Supplementary Material S1)", 2)
rep("(see Section 7 on vendor price adjustment)", "(see Section 4.1 on vendor price adjustment)")
rep("diagnostic only (Section 7)", "diagnostic only (Section 4.1)")
rep("Section 5 reports the event tests under alternative family definitions", "Section 3 reports the event tests under alternative family definitions")
rep("Appendix A defines the 22", "Supplementary Material S1 defines the 22")
rep("(Section 4)", "(Section 2.2)")

# software paragraph (reproducibility; journal asks that code and data be available)
ap = b.index("*Analysis plan.*"); ape = b.index("\n\n", ap)
b = b[:ape] + ("\n\n*Software and code.* We use R 4.3.3 (packages sandwich 3.1.0, lmtest 0.9.40, and ggplot2 3.4.4). One script "
               "reproduces every number, table, and figure; code, data, and output tables are public (Section 6.5).") + b[ape:]

# ---- move figures and tables to the end (journal rule: after the References) ----
figs, tabs = [], []
def take_fig(mm):
    cap = re.sub(r"^Figure (\d+)\. ", r"Figure \1 ", mm.group(2)).replace("Appendix A", "Supplementary Material S1")
    figs.append(f"[[FIG:{mm.group(3)}]]\n\n{cap}\n"); return ""
b = re.sub(r"```\{r (fig\d), fig.cap=\"(.*?)\"\}\nknitr::include_graphics\(file.path\(od, \"(figures/[^\"]+)\"\)\)\n```\n", take_fig, b, flags=re.S)
def take_tab(mm):
    tabs.append(mm.group(0)); return ""
b = re.sub(r"```\{r tab-[a-z]+\}\n.*?```\n", take_tab, b, flags=re.S)
assert len(figs) == 2 and len(tabs) == 6, (len(figs), len(tabs))
b = re.sub(r"\n{3,}", "\n\n", b)

# ---- declarations ----
decl = """# 6. Declarations

## 6.1. Ethical considerations

Not applicable. The study uses public market prices and involves no human or animal participants.

## 6.2. Use of artificial intelligence (AI)

The authors used the generative AI assistant Claude (Anthropic) to run the literature searches (Supplementary Material S1), write R code, draft and edit text, and check reported numbers against the output files. Every number comes from the authors' R code. The authors reviewed all AI-assisted output and take full responsibility for the content. References and the institutional facts in Section 2.1 were checked by web search, not against exchange circulars.

## 6.3. Conflict of interest

The authors declare no conflicts of interest.

## 6.4. Funding

This research did not receive any financial support.

## 6.5. Data availability

The price files (vnstock 4.0.4, source VCI, retrieved on 24 September 2026), the R code, and the output tables are available at https://github.com/trungcandygit/black_litterman_2 (folders data/raw and paper2).

## 6.6. Author contributions

Nguyen Thanh Binh: conceptualization, supervision, validation, and writing (review and editing). Nguyen Van Trung: conceptualization, data curation, formal analysis, methodology, software, visualization, project administration, and writing (original draft). Ha Hong Hanh: methodology, validation, and writing (review and editing). Nguyen Bach Diep: investigation, resources, and writing (review and editing).

"""

# ---- references: web pages get an access date; keep APA ----
r = refs
r = r.replace("*Important changes of new trading system* [Web page]. Ho Chi Minh City Securities Corporation. https://www.hsc.com.vn/en/important-changes-of-new-trading-system",
              "*Important changes of new trading system*. Ho Chi Minh City Securities Corporation. https://www.hsc.com.vn/en/important-changes-of-new-trading-system. Accessed on October 5, 2026.")
r = r.replace("*KRX system officially goes live* [News article]. https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html",
              "*KRX system officially goes live*. Viet Nam News. https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html. Accessed on October 5, 2026.")
assert r.count("Accessed on") == 2
# references cited only in the supplementary material move there
only_si = ["Amihud, Y. (2002)", "Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011)", "Corwin, S. A., & Schultz, P. (2012)", "Parkinson, M. (1980)"]
si_refs = []
for k in only_si:
    mm = re.search(r"(?m)^" + re.escape(k) + r".*$", r); assert mm, k
    si_refs.append(mm.group(0)); r = r.replace(mm.group(0) + "\n", "")
r = re.sub(r"\n{3,}", "\n\n", r)

# ---- tables: caption title above, legend below ("Table 1 Title"), no bold ----
setup_msj = setup.replace(
    'kable <- function(x, caption = NULL, ...) { if (!is.null(caption)) cat("\\n\\n", caption, "\\n\\n", sep = ""); print(knitr::kable(x, ...)); cat("\\n\\n") }',
    'kable <- function(x, caption = NULL, ...) { tt <- caption; nt <- NULL\n'
    '  if (!is.null(caption)) { m <- regmatches(caption, regexec("^Table ([0-9]+)\\\\. (.*?\\\\.)\\\\s+(.*)$", caption, perl = TRUE))[[1]]\n'
    '    if (length(m) == 4) { tt <- paste0("Table ", m[2], " ", m[3]); nt <- m[4] } else tt <- sub("^Table ([0-9]+)\\\\. ", "Table \\\\1 ", caption) }\n'
    '  cat("\\n\\n", tt, "\\n\\n", sep = ""); print(knitr::kable(x, ...)); if (!is.null(nt)) cat("\\n\\n[[NOTE]] ", nt, "\\n\\n", sep = ""); cat("\\n\\n") }')
assert setup_msj != setup

doc = ("---\noutput:\n  word_document:\n    toc: false\n---\n\n" + setup_msj + "\n\n"
       "[[ABSTRACT]] " + abstract + "\n\n"
       "[[KEYWORDS]] Market microstructure, Multiple testing, False discovery rate, Call auction, Emerging markets, Vietnam\n\n"
       + b.strip() + "\n\n" + decl + r.strip() + "\n\n"
       "# Figures\n\n" + "\n".join(figs) + "\n# Tables\n\n" + "\n".join(tabs))
open(os.path.join(HERE, "manuscript_msj.Rmd"), "w", encoding="utf-8").write(doc)

# ---- supplementary material ----
A = appA.replace("# Appendix A. Characteristic definitions", "## S1.1. Characteristic definitions")
B = appB.replace("# Appendix B. Literature search", "## S1.2. Literature search")
B = B.replace("named in the Declarations", "named in Section 6.2 of the article").replace("(Section 3)", "(Section 2.1 of the article)")
sup = ("---\noutput:\n  word_document:\n    toc: false\n---\n\n"
       "**Supplementary Material S1**\n\nClosing at the limit: price limits, overnight gaps and next-day returns on the Ho Chi Minh Stock Exchange\n\n"
       + A.strip() + "\n\n" + B.strip() + "\n\n## References\n\n" + "\n\n".join(sorted(si_refs)) + "\n")
open(os.path.join(HERE, "S1_supplementary.Rmd"), "w", encoding="utf-8").write(sup)
print("ok", len(figs), len(tabs))
