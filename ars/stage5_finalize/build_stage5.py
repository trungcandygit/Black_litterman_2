"""Stage 5 FINALIZE (academic-paper format-convert, formatter_agent) for run ftse2-20260924-01.

Deterministic build of the Finance Research Open submission package from the exact
Stage 4.5-accepted draft. Formatting only: every transform below is either
(a) notation (plain-text formulas -> TeX math so DOCX gets native Word equations and
LaTeX gets proper math), (b) venue layout (double-anonymized split, AI-declaration
section heading, figure file names), or (c) ARS marker stripping. Word-count deviation
is checked (< 1%, formatter quality gate).

Usage: python3 build_stage5.py <accepted_clean_draft.md>
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "submission"
WORK = Path(__file__).resolve().parent / "work"
SRC = Path(sys.argv[1]).resolve()
raw = SRC.read_bytes()
src = raw.decode("utf-8")
assert "<!--" not in src, "ARS markers must be stripped before Stage 5 (use the clean draft)"
SRC_SHA = hashlib.sha256(raw).hexdigest()


def once(text, old, new):
    assert text.count(old) == 1, (old[:60], text.count(old))
    return text.replace(old, new)


def once_if(text, old, new):
    """Plain-text formula conversion for drafts up to v7; from v8 the draft carries TeX math itself."""
    return once(text, old, new) if old in text else text


# ---------------------------------------------------------------- (a) notation
md = src
md = once_if(md, "ILLIQ_it = |R_it| / VAL_it,",
          r"$$\mathrm{ILLIQ}_{it} = \frac{|R_{it}|}{\mathrm{VAL}_{it}},$$")
md = once_if(md, "where R_it is the log return and VAL_it the traded value.",
          r"where $R_{it}$ is the log return and $\mathrm{VAL}_{it}$ the traded value.")
md = once_if(md, "y_iw = α_i + λ_w + Σ_k β_k (Constituent_i × P_kw) + ε_iw,",
          r"$$y_{iw} = \alpha_i + \lambda_w + \sum_{k=1}^{3} \beta_k \left(\mathrm{Constituent}_i \times P_{kw}\right) + \varepsilon_{iw},$$")
md = once_if(md, "where y_iw is a liquidity measure for stock i in week w, α_i and λ_w are stock and week fixed effects, and P_1, P_2 and P_3 indicate",
          r"where $y_{iw}$ is a liquidity measure for stock $i$ in week $w$, $\alpha_i$ and $\lambda_w$ are stock and week fixed effects, and $P_{1w}$, $P_{2w}$ and $P_{3w}$ indicate")
md = once_if(md, "we define illiquidity for stock i on day t with", r"we define illiquidity for stock $i$ on day $t$ with")
md = once_if(md, "the daily abnormal return of stock i is its log return", r"the daily abnormal return of stock $i$ is its log return")
md = once_if(md, "The coefficients β_k identify", r"The coefficients $\beta_k$ identify")
md = once_if(md, "The ITT specification replaces Constituent_i with",
          r"The ITT specification replaces $\mathrm{Constituent}_i$ with") if "replaces Constituent_i" in md else md
md = once_if(md, "Portfolio t = CAR / (σ × √L), where σ is the standard deviation of daily portfolio abnormal returns in the estimation window and L the number",
          r"Portfolio $t = \mathrm{CAR} / (\sigma \sqrt{L})$, where $\sigma$ is the standard deviation of daily portfolio abnormal returns in the estimation window and $L$ the number")
leftover = re.findall(r"(?<![$\\{])\b[A-Za-z]+_[a-z]{1,2}\b(?![}$])", re.sub(r"\$[^$]*\$", "", re.sub(r"\$\$.*?\$\$", "", md.split("## References")[0], flags=re.S)))
leftover = [x for x in leftover if not x.startswith(("output", "code", "named", "c_"))]
assert not leftover, leftover

# true minus signs for negative numbers outside math (proofreading finding M4); the source keeps ASCII
# hyphens so numbers stay byte-comparable with the output CSVs and the token-conservation check
def _minus(seg):
    return re.sub(r"(?<=[\s(\[|,;:])-(?=\d)", "\u2212", seg)
parts = re.split(r"(\$\$.*?\$\$|\$[^$\n]*\$)", md, flags=re.S)
md = "".join(p if p.startswith("$") else _minus(p) for p in parts)

# significance-mark legend: escape so Markdown does not read the asterisks as emphasis
md = md.replace("*, **, *** denote", r"\*, \*\*, \*\*\* denote")

# ---------------------------------------------------------------- (b) venue layout
# figures: separate files named Figure_1 / Figure_2; embedded copies keep the review PDF readable
for n, old in ((1, "figure1_event_study.png"), (2, "figure2_itt_event_study.png")):
    src_ref = f"![](figures/{old})" if f"![](figures/{old})" in md else f"![](figures/Figure_{n}.png)"
    md = once(md, src_ref, f"![](Figure_{n}.png){{width=100%}}")

# AI declaration as its own section before the references (guide: "new section before the references list")
ai_para = re.search(r"\*\*Declaration of generative AI and AI-assisted technologies in the manuscript preparation process\.\*\* (.+)\n", md)
ai_text = ai_para.group(1)
md = md.replace(ai_para.group(0), "")
md = once(md, "## References",
          "## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process\n\n\n" + ai_text + "\n\n\n## References")

# double-anonymized split: identifying or author-only statements go to the title page
title = re.search(r"^# (.+)$", md, re.M).group(1)
credit = re.search(r"\*\*Author contributions \(CRediT\)\.\*\* .+\n", md).group(0)
funding = re.search(r"\*\*Funding\.\*\* (.+?) \[Authors to confirm\.\]\n", md)
coi = re.search(r"\*\*Declaration of competing interest\.\*\* .+\n", md).group(0)
anon = md.replace(credit, "").replace(coi, "")
anon = anon.replace(funding.group(0), "**Funding.** " + funding.group(1) + "\n")
assert "[Authors to confirm" not in anon and "[To be supplied" not in anon
anon = re.sub(r"\n{4,}", "\n\n\n", anon)

# ---------------------------------------------------------------- checks
def words(t):
    t = re.sub(r"\$\$.*?\$\$", " EQ ", t, flags=re.S)
    t = re.sub(r"!\[.*?\]\(.*?\)(\{.*?\})?", " ", t)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,%'’\-]*", t))

abstract = re.search(r"## Abstract\n+(.+?)\n", md, re.S).group(1).strip()
keywords = [k.strip() for k in re.search(r"\*\*Keywords\*\*: (.+)", md).group(1).split(";")]
body = md.split("## Abstract")[1].split("## Declarations")[0]
checks = {
    "source_draft_sha256": SRC_SHA,
    "abstract_words": words(abstract),
    "abstract_le_250": words(abstract) <= 250,
    "abstract_has_no_references": not re.search(r"\((?:[A-Z][^()]*?)(?:19|20)\d\d", abstract),
    "keywords": keywords,
    "keywords_1_to_7": 1 <= len(keywords) <= 7,
    "keywords_no_and_of": not any(re.search(r"\b(and|of)\b", k) for k in keywords),
    "body_words_prose_and_tables": words(body),
}

# ---------------------------------------------------------------- highlights
HIGHLIGHTS = [
    "Vietnam's FTSE upgrade cut illiquidity of likely index stocks by 24% to 56%",
    "Liquidity and prices moved at FTSE's disclosures, before the first index tranche",
    "Prices rose at the announcement and confirmation, not at the list or effective date",
    "Rebalancing-day trading surged for included stocks only, with no price effect",
    "Intention-to-treat on a pre-announcement list separates effects from selection",
]
checks["highlights"] = [(h, len(h)) for h in HIGHLIGHTS]
checks["highlights_3_to_5_le_85"] = 3 <= len(HIGHLIGHTS) <= 5 and all(len(h) <= 85 for h in HIGHLIGHTS)

# ---------------------------------------------------------------- write sources
if OUT.exists():
    shutil.rmtree(OUT)
(OUT / "figures").mkdir(parents=True)
WORK.mkdir(exist_ok=True)
for n in (1, 2):
    for ext in ("png", "pdf"):
        shutil.copy(ROOT / f"output/figures/Figure_{n}.{ext}", OUT / "figures" / f"Figure_{n}.{ext}")
        shutil.copy(ROOT / f"output/figures/Figure_{n}.{ext}", WORK / f"Figure_{n}.{ext}")

(WORK / "manuscript_anonymized.md").write_text(anon)

title_page = f"""# {title}

Nguyen Thanh Binh^a^, Nguyen Van Trung^a,\\*^, Nguyen Bach Diep^a^, Ha Hong Hanh^b^

^a^ Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam

^b^ School of Accounting and Auditing, National Economics University, Hanoi, Vietnam

\\* Corresponding author: Nguyen Van Trung, Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam. Email: 15233582@st.neu.edu.vn. Tel: +84 355 347 831.

## Author details

Nguyen Thanh Binh: nguyenthanhbinhapd@apd.edu.vn; ORCID 0009-0007-0042-2835

Nguyen Van Trung: 15233582@st.neu.edu.vn; ORCID 0009-0008-3307-6569

Nguyen Bach Diep: diepnb@apd.edu.vn; ORCID 0009-0003-0967-7528

Ha Hong Hanh: hanhhh@neu.edu.vn; ORCID 0000-0003-3581-6571

## Acknowledgements

None.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Funding

{funding.group(1)}

## CRediT authorship contribution statement

Nguyen Thanh Binh: Conceptualization, Supervision, Validation, Writing – review & editing. Nguyen Van Trung: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – original draft, Writing – review & editing. Nguyen Bach Diep: Methodology, Formal analysis, Writing – original draft. Ha Hong Hanh: Validation, Writing – review & editing.

## Data availability

Daily price and volume data are public and were retrieved through the vnstock library (VCI source). The downloaded daily files, the R code that reproduces every table and figure, and the reproduction log are provided as supplementary material (Supplementary_Replication_Package.zip) and will be deposited in a public repository on acceptance.
"""
(WORK / "title_page.md").write_text(title_page)
declaration = f"""# Declaration of interests

**Manuscript title:** {title}

**Journal:** Finance Research Open

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Authors:** Nguyen Thanh Binh, Nguyen Van Trung (corresponding author), Nguyen Bach Diep, Ha Hong Hanh

**Date:** 24 September 2026
"""
(WORK / "declaration_of_competing_interest.md").write_text(declaration)

# non-anonymized version: title page + manuscript (declarations from the title page, ethics kept)
ethics = re.search(r"\*\*Ethics\.\*\* (.+)\n", anon).group(1)
body_named = anon.split("\n", 1)[1]  # drop the title line; the title page carries it
body_named = re.sub(r"## Declarations\n.*?(?=## Declaration of generative AI)", "", body_named, flags=re.S)
tp = title_page.replace("## Data availability", "## Ethics\n\n" + ethics + "\n\n## Data availability")
(WORK / "manuscript_with_author_details.md").write_text(tp + "\n\\newpage\n\n" + body_named)


(WORK / "highlights.md").write_text("# Highlights\n\n" + "\n".join(f"- {h}" for h in HIGHLIGHTS) + "\n")

cover = f"""24 September 2026

The Editor-in-Chief
Finance Research Open

**Submission of manuscript: "{title}"**

Dear Editor,

We submit the enclosed manuscript for consideration as a research article in Finance Research Open.

FTSE Russell reclassified Vietnam from frontier to secondary emerging status in four dated steps between October 2025 and September 2026. Using daily data on 366 stocks listed on the Ho Chi Minh City Stock Exchange, the paper traces stock-level liquidity and prices at each step and separates the effect of the upgrade from FTSE's selection of constituents with an intention-to-treat design built on a list screened before the announcement.

Relative to never-named stocks, the illiquidity of the pre-announcement eligible group fell by 24% to 56%, and constituents earned abnormal returns in the announcement week and at the confirmation that are significant under four benchmarks and a portfolio test; the first index tranche produced a trading surge for included stocks only and no reliable price effect. The response to Vietnam's upgrade came with FTSE's disclosures rather than with index trading.

The paper fits the journal's scope in emerging markets finance, financial markets and market efficiency, and it reports its null and unfavourable results (no price effect at the constituent list or the effective date; rising high-low spreads) alongside the main findings.

The manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to Finance Research Open. The authors used generative AI tools as described in the declaration placed before the reference list; they reviewed and verified all content and take full responsibility for it. The manuscript is prepared for double-anonymized review: author details, acknowledgements and the competing-interests declaration are in the separate title page.

Sincerely,

Nguyen Van Trung (corresponding author), on behalf of all authors
Academy of Policy and Development, Nam An Khanh Urban Area, Hoai Duc District, Hanoi, Vietnam
Email: 15233582@st.neu.edu.vn; Tel: +84 355 347 831
"""
(WORK / "cover_letter.md").write_text(cover)
(WORK / "checks.json").write_text(json.dumps(checks, indent=1, ensure_ascii=False))
print(json.dumps(checks, indent=1, ensure_ascii=False))
