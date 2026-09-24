# Project rules: FTSE2 paper (run ftse2-20260924-01)

## MANDATORY: Academic Research Skills (ARS) for every task

The author requires that every task on this paper is done under the ARS skill
suite: https://github.com/imbad0202/academic-research-skills (pinned: v3.22.1,
commit 6234edf28114ad7f639269446664cf403f1ad8d6, matching `ars/pipeline_state.json`).

At the start of every session, before any work:

1. Clone ARS outside the repo and register the four skills:
   ```bash
   git clone https://github.com/imbad0202/academic-research-skills "$SCRATCH/academic-research-skills"
   mkdir -p ~/.claude/skills
   for s in academic-pipeline academic-paper academic-paper-reviewer deep-research; do
     ln -sfn "$SCRATCH/academic-research-skills/$s" ~/.claude/skills/$s
   done
   ```
2. Load `academic-pipeline` with the Skill tool and resume from the stage in
   `ars/pipeline_state.json` (`current_stage`).
3. Before a stage, Read the SKILL.md of the dispatched skill and the agent file
   that does the work (e.g. Stage 4.5 -> `academic-pipeline/agents/integrity_verification_agent.md`
   plus `references/integrity_review_protocol.md`, `claim_verification_protocol.md`,
   `ai_research_failure_modes.md`).
4. Every subagent prompt must tell the subagent to Read those skill files
   verbatim first and to record a "Skill load record" in its output. A
   paraphrase of the rules in the prompt is not a substitute.

## Standing author decisions (see `ars/pipeline_state.json` user_decisions)

- Proceed through checkpoints without asking; integrity FAILs are fixed, never overridden.
- Target venue: Finance Research Open (`ars/venue_criteria_FRO.md`).
- Stage 5: APA 7, DOCX + LaTeX/PDF. Stage 6: Vietnamese + English.

## Layout

- `ars/` pipeline artifacts per stage; `code/` R analysis; `output/` CSV results
  (every manuscript number must trace to a file here); `data/raw/` is gitignored.
