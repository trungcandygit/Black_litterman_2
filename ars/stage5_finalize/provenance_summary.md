# Provenance summary (formatter_agent output package)

Accepted draft (Stage 4.5 PASS): ars/stage4_5_integrity/correction_round3/manuscript_v7.clean.md, SHA-256 3331a4dea23bb7dddeabf4ca4d82ea4a60b12937637d1fe89374c93d4f7d132c.

## Cite-time provenance hard gate
The draft carries no `<!--ref:...-->` / `<!--anchor:...-->` markers and none of the refusal literals (rules 1-11); the run did not use the v3.7.1 marker layer. Citation verification is instead documented in the Stage 4.5 report (33/33 references VERIFIED, 100% citation contexts). Gate: PASS (nothing to refuse).

## Advisories
- #660 tortured-phrase screening: `not_checked` (SNAPSHOT_NOT_PROVIDED), HEURISTIC-ADVISORY / UNMEASURED; replay-validated. Not a clean certification. File: entry_checkpoint/tortured_phrase_advisory_v7.json.
- #672 cross-document consistency: ADVISORY_UNAVAILABLE:PREREGISTRATION_SIDECAR_ABSENT (no Stage-1 sidecar exists; not manufactured). File: entry_checkpoint/cross_document_advisory_672.txt.
- Citation existence advisories (C-V6(b)): none; every reference reached VERIFIED in Stage 4.5 (lookups via WebSearch because the Crossref/DOI APIs were blocked; the Biktimirov & Afego volume/article number rests on the raw Crossref record saved at Stage 1).
- Bibliographic integrity signals (#678): none recorded in this run.

## Formatting transforms applied (content-preserving)
1. Plain-text formulas -> TeX math (2 display equations, inline symbols in Sections 3.2-3.3 and the Table 4 note) so the DOCX carries native Word equations (17 OMML objects) and the LaTeX carries math.
2. Significance-legend asterisks escaped.
3. Double-anonymized split: CRediT and competing-interest statements moved to the title page; funding kept without the placeholder.
4. AI declaration rendered as its own section before the references, with the journal's exact title.
5. Figure files renamed Figure_1 / Figure_2 (PDF vector + PNG 600 dpi, 4500 px wide).
Checks: abstract 210 words; 6 keywords; 5 highlights <= 85 characters; 16/16 tables; word-count deviation MD vs DOCX 0.03% (< 1%); no ARS markers or identifying strings in DOCX/PDF/TeX.

## Tooling deviations
- PDF compiled with XeLaTeX (TeX Live 2023) instead of tectonic: tectonic's bundle host is blocked in this environment. formatter_agent allows "tectonic or xelatex"; HTML-to-PDF was not used.
- Template: elsarticle (Elsevier), review mode, author-year; fonts TeX Gyre Termes (Times metric clone; Times New Roman is not installed).
