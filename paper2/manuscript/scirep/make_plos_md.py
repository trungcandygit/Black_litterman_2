"""Derive the PLOS ONE manuscript source (manuscript_plos.md) from the Scientific Reports source.
Formatting only: section order and names, Fig/S-item labels, tables and figure captions placed after the paragraph that first cites them,
no funding / competing-interest / author-contribution text in the file (entered in the submission system)."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, "manuscript_scirep.md"), encoding="utf-8").read()


def sec(name, nxt):
    a = s.index(f"## {name}\n") + len(f"## {name}\n")
    b = s.index(f"## {nxt}\n") if nxt else len(s)
    return s[a:b].strip("\n")


abstract = sec("Abstract", "Introduction").split("**Keywords:**")[0].strip()
intro, results, discussion, methods = sec("Introduction", "Results"), sec("Results", "Discussion"), sec("Discussion", "Methods"), sec("Methods", "Data availability")


def once(t, old, new, cnt=1):
    assert t.count(old) == cnt, (old[:70], t.count(old))
    return t.replace(old, new)

# ---- Introduction: statement of the overall aim and whether it was achieved
intro = once(intro, "We also split the events at the 2025 platform change.",
             "We also split the events at the 2025 platform change. The aim of the study is to measure these quantities and to judge whether the pattern is consistent with delayed price discovery; the first aim is met, and the second only in part, because the data cannot separate delayed price discovery from news, attention and auction overshooting.")

# ---- Results: no table cited before its place; exact P values with three decimals
results = once(results, "which is below 0.001 for |*t*| ≥ 3.29; Table 1 uses the *t* distribution with *G* − 1 degrees of freedom (Methods).",
               "which is below 0.001 for |*t*| ≥ 3.29; the main close-to-close event tests use the *t* distribution with *G* − 1 degrees of freedom (Materials and methods).")
results = once(results, "(*P* = 0.07)", "(*P* = 0.073)")
results = once(results, "(*P* = 0.11)", "(*P* = 0.105)")
results = once(results, "*P* = 0.03)", "*P* = 0.029)")
results = once(results, "(*P* = 0.25)", "(*P* = 0.254)")
results = once(results, "*P* ≤ 0.013)", "*P* ≤ 0.013)")
results = once(results, "*P* ≥ 0.16)", "*P* ≥ 0.162)")
results = once(results, "none reaches |*t*| = 3 in any sample or 1.96 in the full sample, and none survives the Benjamini–Hochberg (BH) control.",
               "none reaches |*t*| = 3 in any sample or 1.96 in the full sample, and none survives the Benjamini–Hochberg (BH) control (full estimates in S5 Table).")
results = once(results, "Methods, equations (1)–(5)", "Materials and methods, equations (1)–(5)")

# ---- Discussion / Conclusions
d_paras = discussion.split("\n\n")
assert d_paras[-1].startswith("In sum,")
concl = d_paras[-1].replace("In sum, of 26 tests", "Of 26 tests")
discussion = "\n\n".join(d_paras[:-1])

# ---- Methods: ethics and statistical analysis
methods = once(methods, "### Software and ethics\n\nOne R 4.3.3 script (packages sandwich, lmtest and ggplot2) reproduces every number, table and figure; the figures in this version were redrawn from the saved R output tables with Python (matplotlib) without re-estimating any number. The study uses public market prices and involves no human or animal participants, so ethical approval and consent were not required.",
 """### Statistical analysis

*Software and code.* All estimates come from one R 4.3.3 script (packages sandwich 3.1.0, lmtest and ggplot2) that reproduces every number, table and figure; the figures in this version were redrawn from the saved R output tables with Python (matplotlib) without re-estimating any number. The code, the price files and the output tables are in the repository named in the Data availability statement in the submission form (https://github.com/trungcandygit/black_litterman_2, folder paper2, entry script paper2/R/run_all.R).

*Design and tests.* The design is observational and uses events (stock-days) compared with market, control-stock and near-limit benchmarks, not between- or within-subject groups. All tests are two-sided with threshold α = 0.05. Event means use cluster-robust *t*-statistics (equation (6)) with the clusters, reference distributions and small-sample factors given above; the characteristic tests use Newey–West *t*-statistics with 78 degrees of freedom. We report exact *P* values of 0.001 or more and "*P* < 0.001" otherwise. The reference distribution is the standard normal for the event-level statistics, justified by 446 and 319 event dates for ceilings and floors (at least 46 clusters in every alternative clustering); no normality assumption on returns is made beyond that.

*Multiple comparisons, outliers and missing data.* The family of 26 tests is controlled by the Benjamini–Hochberg procedure (equation (8)), with Holm and Bonferroni adjustments as checks. Returns beyond ±8% (96 stock-days) are not removed from the main estimates; we report the estimates with every event within five trading days of such a return removed. Stocks with less than 95% non-missing closes are excluded from the sample (347 of 405 retained), and events without the required prices are excluded from the analysis that needs them, with counts given above. Sample sizes are the numbers of events, stock-days or weeks stated in the tables; no sample-size calculation was performed, and the minimum detectable effect of the characteristic tests is reported in the Results.

*Regression results.* The full estimates of the 22 characteristic regressions (coefficients, standard errors, *P* values and 95% confidence intervals) are in S5 Table; the event comparisons report mean differences with *t*-statistics in the tables. Goodness-of-fit measures are not reported because the regressions are cross-sectional rank regressions estimated week by week.

### Ethics statement

The study uses public market prices and involves no human or animal participants, so ethical approval and consent were not required.""")
methods = methods.replace("### Use of generative AI", "### Use of generative AI")
# "Supplementary" labels
def supp(t):
    t = t.replace("Supplementary Note 1", "S1 Appendix").replace("Supplementary Note 2", "S1 Appendix")
    for i in range(1, 5):
        t = t.replace(f"Supplementary Table S{i}", f"S{i} Table")
    return t
intro, results, discussion, concl, methods = map(supp, (intro, results, discussion, concl, methods))
results = results.replace("Figure 1 plots", "Fig 1 plots").replace("Figure 2 plots", "Fig 2 plots")
methods = methods.replace("Figure 2 uses", "Fig 2 uses")
assert "Figure" not in (intro + results + discussion + methods)

# ---- insert figures and tables after the paragraph that first cites them (placeholders, filled by build_plos.py)
def after(text, start, token):
    paras = text.split("\n\n")
    idx = [i for i, p in enumerate(paras) if p.startswith(start)]
    assert len(idx) == 1, (start, idx)
    paras.insert(idx[0] + 1, token)
    return "\n\n".join(paras)

results = after(results, "Fig 1 plots", "{{FIG1}}")
results = after(results, "Table 1 presents", "{{TABLE1}}")
results = after(results, "Table 2 decomposes", "{{TABLE2}}")
results = after(results, "Fig 2 plots", "{{FIG2}}\n\n{{TABLE3}}")
results = after(results, "Table 4 splits", "{{TABLE4}}")
results = after(results, "Because the events are unbalanced", "{{TABLE5}}")

title_page = """::: {custom-style="Title"}
Do price limits delay price discovery? Overnight gaps after limit closes in Vietnam
:::

**Short title:** Price limit closes and overnight gaps in Vietnam

Ha Hong Hanh^a^, Nguyen Van Trung^b,^\\*, Nguyen Thanh Binh^b^

^a^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam

^b^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam

\\* Corresponding author

E-mail: kontrungcany@gmail.com (NVT)

::: pagebreak
:::
"""
out = f"""{title_page}
## Abstract

{abstract}

## Introduction

{intro}

## Results

{results}

## Discussion

{discussion}

## Conclusions

{concl}

## Materials and methods

{methods}

## Acknowledgments

The authors received no assistance beyond that described in Materials and methods.

## References

::: references
:::

## Supporting information

::: sicaptions
:::
"""
open(os.path.join(HERE, "manuscript_plos.md"), "w", encoding="utf-8").write(out)
print("ok", len(out.split()))
