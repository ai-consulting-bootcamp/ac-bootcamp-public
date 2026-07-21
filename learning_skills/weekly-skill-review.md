# Brief: Weekly Skill Review

Use this brief to author `weekly-skill-review/SKILL.md` in your assistant’s skills location. Keep the installed skill short; this file is the design intent, not the final package.

## Intended Outcome

At the end of a learning week (or whenever notes have piled up), the agent turns **scattered retros and error notes** into one deliberate-practice plan for the next stretch of work.

A successful run yields:

1. **Inputs acknowledged** — what notes, retros, or error digests were actually used (paste, paths, or “from this chat”).
2. **Theme clusters** — 2–4 themes grouped from the raw notes (e.g. “debugging under time pressure,” “RAG eval gaps,” “tooling setup friction”)—not a rewrite of every entry.
3. **One practice focus** — a single, concrete skill or habit to train next week (measurable enough to notice progress).
4. **How to practice** — 1–3 small drills, checks, or constraints (e.g. “run Error Autopsy before asking for a full rewrite,” “write a four-line retro after every lab”).
5. **What to ignore for now** — themes parked so scope stays honest.

Success looks like a **short weekly brief**, not a performance review essay or a second copy of the entire journal.

## When to Activate

Activate this skill when the user wants to **synthesize** multiple learning moments into next-week focus.

Typical signals:

- End of week / end of module day-block / “Friday review” / “before next sprint.”
- They want to turn scattered retros, error autopsies, or lab notes into deliberate practice.
- They ask what to practice next, what patterns keep showing up, or how to prioritize learning from their own notes.
- They paste two or more short retros/errors and ask for themes + one focus.

Point the agent at **whatever notes they actually keep**—there is no required filename. Chat paste, a folder of markdown, or a learning log all work.

### Suggested `description` direction (for your `SKILL.md` frontmatter)

Write a third-person description that covers **what** (cluster learning notes into themes and pick one deliberate practice focus) and **when** (week’s end, weekly review, turning retros/errors into next-week practice, pattern-finding across notes). Include trigger phrases like: weekly review, week’s end, deliberate practice, learning themes, synthesize retros.

### Phrases that should load it

- “It’s the end of the week—review my retros and pick one practice focus.”
- “Here are three short notes from this week; cluster themes and tell me what to train.”
- “Turn my error digests into a deliberate practice plan for next week.”

### Phrases that should *not* load it

- “Write a retro for the task we just finished.” (Post-Task Retro—single task)
- “This stack trace just failed; run an autopsy.” (Error Autopsy—single incident)
- “Plan tomorrow’s implementation steps for feature X.” (task planning, not learning synthesis)

## When *Not* to Activate

- Only one fresh task or one fresh error with no multi-note synthesis requested.
- Pure scheduling / calendar / standup without learning notes.
- Asking the agent to invent a curriculum from scratch with no student artifacts—insist on at least a few notes or past outputs.
- Replacing a full career coach session; stay bounded to notes → themes → one focus.

## Steps (encode these in the skill body)

1. **Gather inputs.** Ask for or use pasted retros, error autopsies, lab reflections, or linked note paths. If nothing is provided, ask for 2–3 short items before proceeding.
2. **Re-read for patterns.** Skim for repeated blockers, wins, and emotional/time pressure cues—not for prose quality.
3. **Cluster into 2–4 themes.** Name each theme in plain language; cite which notes support it (lightly).
4. **Pick one deliberate practice focus** for the next week. Prefer the theme that is frequent *and* improvable with a small drill.
5. **Define practice:** 1–3 concrete actions (when to trigger Post-Task Retro / Error Autopsy, a constraint, a check).
6. **Park the rest:** list themes explicitly deferred so the user does not feel everything is “failing.”

## Output Format

Unless the user requests another shape, use:

```markdown
## Inputs used
- …

## Themes
1. … (supported by: …)
2. …
3. …

## Next week’s practice focus (one)
- Focus:
- Why this one:

## How I’ll practice
1.
2.
3.

## Parked for later
- …
```

## Boundaries

- Do not invent notes the user did not provide.
- Do not pick more than one primary focus unless the user explicitly asks for a ranked shortlist (still keep #1 obvious).
- Do not turn the review into a grade or personality judgment.
- Keep output short enough to reread on Monday morning.
