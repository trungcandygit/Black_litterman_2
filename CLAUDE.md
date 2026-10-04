# Project Rules

## MANDATORY INSTRUCTION — Academic Research Skills
For every task involving research, quantitative analysis, finance, or data processing in this project:

1. LOAD FIRST: before executing any request, automatically load and read the documentation, standards and scripts in `academic-research-skills/` — `README.md`, `QUICKSTART.md`, the relevant `SKILL.md`, and every file those documents reference for the task at hand.
2. FOLLOW STRICTLY (100%): comply with the workflows, steps and academic standards defined in the skill.
3. DO NOT ASK AGAIN: do not ask for confirmation on steps already defined in the skill; apply and execute them end to end, professionally.
   - Exception: still confirm before irreversible or outward-facing actions (deleting data, force-push, publishing, opening PRs) that the skill does not define.

### Skill entry points (inside `academic-research-skills/`)
Start with `academic-research-skills/README.md` and `QUICKSTART.md`, then read the relevant `SKILL.md` before acting:
- `deep-research/SKILL.md` — literature review, data fetching, research methodology
- `academic-paper/SKILL.md` — writing / structuring papers (econometric & quant finance write-ups)
- `academic-paper-reviewer/SKILL.md` — reviewing and critiquing papers or models
- `academic-pipeline/SKILL.md` — end-to-end research → paper → review pipeline
- `sr-screener/SKILL.md` — systematic-review screening

## Git sync
- Before starting work and before each push, `git fetch origin main` and merge `origin/main` into the working branch (merge, no rebase/force-push); resolve conflicts without asking unless both sides changed the same logic.
- Pushes go to the designated working branch only; never push directly to `main`.

## Project: BL-K_IO upgrade paper (new manuscript, R only)
- Goal: a brand-new, stronger journal manuscript that inherits the strengths of the earlier BL-K_IO paper (Round 2 under review elsewhere — do NOT cite it and do NOT reuse its text; it is unpublished). The user said no citation of the unpublished work is needed.
- All computation is in **R** (scripts under `paper2/R/`, one `run_all.R` entry point, seeds fixed, outputs in `paper2/output/`). Every number in the manuscript must come from a saved R output — no hand-typed or remembered results.
- Follow `academic-research-skills/` **absolutely** (academic-pipeline → deep-research → academic-paper → integrity gates → reviewer → revision → finalize → process record). Keep its integrity rules: no fabricated citations/results, every reference must be verifiable (DOI check), AI-use disclosure, failure-mode checklist, anti-leakage (session data over memory).
- Per the user's standing no-ask instruction, non-integrity checkpoints are auto-proceeded and recorded as such in `paper2/process/`; an integrity FAIL/override is never self-approved.
- Data: `Data_fetch/` (25 banks monthly close and market cap, 2014-06 to 2026-05) and `data/raw/` (daily OHLCV, 2024-08 onward). Risk-free = annual 10-year VGB yield by calendar year (values in `paper2/data/rf_vgb10y.csv`, read from the authors' own earlier figure; flagged approximate).
