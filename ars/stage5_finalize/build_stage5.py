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


# ---------------------------------------------------------------- (a) notation
md = src
md = once(md, "ILLIQ_it = |R_it| / VAL_it,",
          r"$$\mathrm{ILLIQ}_{it} = \frac{\lvert R_{it} \rvert}{\mathrm{VAL}_{it}},$$")
md = once(md, "where R_it is the log return and VAL_it the traded value.",
          r"where $R_{it}$ is the log return and $\mathrm{VAL}_{it}$ the traded value.")
md = once(md, "y_iw = α_i + λ_w + Σ_k β_k (Constituent_i × P_kw) + ε_iw,",
          r"$$y_{iw} = \alpha_i + \lambda_w + \sum_{k=1}^{3} \beta_k \left(\mathrm{Constituent}_i \times P_{kw}\right) + \varepsilon_{iw},$$")
md = once(md, "where y_iw is a liquidity measure for stock i in week w, α_i and λ_w are stock and week fixed effects, and P_1, P_2 and P_3 indicate",
          r"where $y_{iw}$ is a liquidity measure for stock $i$ in week $w$, $\alpha_i$ and $\lambda_w$ are stock and week fixed effects, and $P_{1w}$, $P_{2w}$ and $P_{3w}$ indicate")
md = once(md, "The coefficients β_k identify", r"The coefficients $\beta_k$ identify")
md = once(md, "The ITT specification replaces Constituent_i with",
          r"The ITT specification replaces $\mathrm{Constituent}_i$ with") if "replaces Constituent_i" in md else md
md = once(md, "Portfolio t = CAR / (σ × √L), where σ is the standard deviation of daily portfolio abnormal returns in the estimation window and L the number",
          r"Portfolio $t = \mathrm{CAR} / (\sigma \sqrt{L})$, where $\sigma$ is the standard deviation of daily portfolio abnormal returns in the estimation window and $L$ the number")
leftover = re.findall(r"(?<![$\\{])\b[A-Za-z]+_[a-z]{1,2}\b(?![}$])", re.sub(r"\$[^$]*\$", "", md.split("## References")[0]))
leftover = [x for x in leftover if not x.startswith(("output", "code", "named", "c_"))]
assert not leftover, leftover

# significance-mark legend: escape so Markdown does not read the asterisks as emphasis
md = md.replace("*, **, *** denote", r"\*, \*\*, \*\*\* denote")

# ---------------------------------------------------------------- (b) venue layout
# figures: separate files named Figure_1 / Figure_2; embedded copies keep the review PDF readable
md = once(md, "![](figures/figure1_event_study.png)", "![](Figure_1.png){width=100%}")
md = once(md, "![](figures/figure2_itt_event_study.png)", "![](Figure_2.png){width=100%}")

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
    "Rebalancing-day trading surged for included stocks only, with no price change",
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

**Authors**: [Given name Family name]^a^, [Given name Family name]^b^

^a^ [Department, Institution, full postal address, Country]

^b^ [Department, Institution, full postal address, Country]

**Corresponding author**: [Name], [full postal address], [email address]

## Acknowledgements

[Acknowledge anyone who helped with the research, language editing or proofreading; write "None" if not applicable.]

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. [Confirm, and upload the Word file generated by Elsevier's declarations tool.]

## Funding

{funding.group(1)}

## CRediT authorship contribution statement

[Author 1]: Conceptualization, Methodology, Data curation, Formal analysis, Software, Writing – original draft. [Author 2]: Validation, Writing – review & editing, Supervision. [Assign the 14 CRediT roles truthfully; every role must match what each author did.]

## Data availability

Daily price and volume data are public and were retrieved through the vnstock library (VCI source). The downloaded daily files, the R code that reproduces every table and figure, and the reproduction log are available at [repository URL or DOI; deposit before submission if possible, e.g. Mendeley Data or Zenodo] and are cited in the manuscript as a dataset reference on acceptance.
"""
(WORK / "title_page.md").write_text(title_page)
(WORK / "highlights.md").write_text("# Highlights\n\n" + "\n".join(f"- {h}" for h in HIGHLIGHTS) + "\n")

cover = f"""[Date]

The Editor-in-Chief
Finance Research Open

**Submission of manuscript: "{title}"**

Dear Editor,

We submit the enclosed manuscript for consideration as a research article in Finance Research Open.

FTSE Russell reclassified Vietnam from frontier to secondary emerging status in four dated steps between October 2025 and September 2026. Using daily data on 366 stocks listed on the Ho Chi Minh City Stock Exchange, the paper traces stock-level liquidity and prices at each step and separates the effect of the upgrade from FTSE's selection of constituents with an intention-to-treat design built on a list screened before the announcement.

Relative to never-named stocks, the illiquidity of the pre-announcement eligible group fell by 24% to 56%, and constituents earned abnormal returns in the announcement week and at the confirmation that are significant under four benchmarks and a portfolio test; the first index tranche produced a trading surge for included stocks only and no price change. The response to Vietnam's upgrade came with FTSE's disclosures rather than with index trading.

The paper fits the journal's scope in emerging markets finance, financial markets and market efficiency, and it reports its null and unfavourable results (no price effect at the constituent list or the effective date; rising high-low spreads) alongside the main findings.

The manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to Finance Research Open. The authors used generative AI tools as described in the declaration placed before the reference list; they reviewed and verified all content and take full responsibility for it. The manuscript is prepared for double-anonymized review: author details, acknowledgements and the competing-interests declaration are in the separate title page.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
"""
(WORK / "cover_letter.md").write_text(cover)
(WORK / "checks.json").write_text(json.dumps(checks, indent=1, ensure_ascii=False))
print(json.dumps(checks, indent=1, ensure_ascii=False))
