# Brief: Post-Task Retro

Use this brief to author `post-task-retro/SKILL.md` in your assistant’s skills location. Keep the installed skill short; this file is the design intent, not the final package.

## Intended Outcome

After a task is finished (or deliberately stopped), the agent produces a **compact learning retro** the student can keep in personal notes or a learning log.

A successful run yields:

1. **What finished** — one concrete outcome (artifact, decision, or verified behavior), not a diary of every click.
2. **How it was verified** — the check, command, test, or manual proof that made “done” believable.
3. **What worked / what nearly failed** — one win and one risk or mistake, each specific enough to reuse.
4. **Reusable rule** — one heuristic or checklist item for the next similar task.

Target length: roughly **four short blocks** (or four lines if the task was tiny). Prefer specifics (files, commands, constraints) over generic advice.

## When to Activate

Activate this skill when the user has **completed** (or wrapped) work and wants to turn that moment into a learning note. Typical signals:

- They ask for a retrospective, debrief, wrap-up, lessons learned, or “what should I remember from this?”
- They say the task is done / shipped / submitted / merged and want a short learning capture.
- They finish a lab, debug session, research pass, review, or implementation and want a structured close-out—even if they never say the word “retro.”
- They ask to summarize “what I learned” before switching context.

### Suggested `description` direction (for your `SKILL.md` frontmatter)

Write a third-person description that covers **what** (short post-task learning note) and **when** (after finishing implementation, debugging, research, review, or other completed work; wrap-up; debrief; lessons learned). Include trigger phrases like: retrospective, wrap-up, debrief, lessons learned, learning summary, after finishing.

### Phrases that should load it

- “Write a quick retro on what we just finished.”
- “Before I move on, capture what I learned from this lab.”
- “Debrief this debug session in four lines.”

### Phrases that should *not* load it

- “Keep going—implement the next feature.” (still in-flight work)
- “Help me plan the approach before I start.” (use planning / goal skills instead)
- “Explain this error and fix it.” (use Error Autopsy, not a post-mortem of success)

## When *Not* to Activate

- Mid-task: the user still wants code, fixes, or next steps—not a learning note.
- Pure Q&A or explanation with no completed work to reflect on.
- Weekly / multi-day synthesis (that belongs to Weekly Skill Review).
- Incident-style failure analysis while the bug is still open (that belongs to Error Autopsy; run a retro *after* the fix lands if they want both).

## Steps (encode these in the skill body)

1. **Confirm the task is closed enough to reflect.** If work is still open, ask whether they want a mid-point note or to finish first—do not invent a fake “done.”
2. **State the outcome.** Name what completed and the key file, system, or decision if it matters.
3. **State verification.** What check gave confidence (test, command, screenshot, acceptance criteria)?
4. **Extract learning.** One thing that worked; one risk or mistake; turn both into a single reusable rule or check.
5. **Keep it short.** If the task was trivial, collapse to one bullet per section. Prefer concrete over motivational fluff.

## Output Format

Unless the user requests another shape, use:

```markdown
## Outcome
- What I finished:
- How I verified it:

## What I Learned
- Worked:
- Risk or mistake:
- Reusable rule:
```

## Boundaries

- Do not rewrite the whole session transcript.
- Do not invent lessons that were not in the work.
- Do not create durable course files unless the user asks; the retro is for *their* notes or log.
- Stay learning-focused: this is not a status report for a stakeholder.
