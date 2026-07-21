# Brief: Error Autopsy

Use this brief to author `error-autopsy/SKILL.md` in your assistant’s skills location. Keep the installed skill short; this file is the design intent, not the final package.

## Intended Outcome

When something breaks, the agent runs a **tight diagnostic ritual** that turns panic or paste-dumping into a reusable pattern: hypothesize → check the smallest thing → name root cause and fix in one line each.

A successful run yields:

1. **Symptom** — what failed, in the user’s words plus the observable signal (error text, exit code, wrong output).
2. **Top hypotheses** — 2–3 ranked guesses about *why*, grounded in the symptom (not a laundry list of every possible bug).
3. **Smallest next check** — one concrete probe (one command, one file open, one reproduction step) that will kill or confirm the leading hypothesis.
4. **Root cause + fix (one-liners)** — after evidence exists (or from a clear paste), a single-line cause and a single-line fix or next action.

The point is a **reusable diagnostic pattern**, not a long incident novel or a full rewrite of the codebase.

## When to Activate

Activate this skill when the user is stuck on a **failure** and needs structured diagnosis—not when they only want “just fix it silently” without understanding.

Typical signals:

- Bugs, failed runs, failing tests, stack traces, red CI, broken installs, or “it worked yesterday.”
- “This broke and I don’t know why,” “help me debug,” “what does this error mean,” “why is this failing.”
- They paste an error / traceback / unexpected output and want a methodical path, not a random shotgun fix.
- They ask for a postmortem *of a specific failure* while still debugging (or right after a fix, to lock the lesson).

### Suggested `description` direction (for your `SKILL.md` frontmatter)

Write a third-person description that covers **what** (structured error autopsy: hypotheses, smallest check, one-line root cause and fix) and **when** (bugs, failed runs, stack traces, failing tests, CI failures, unexplained breakage). Include trigger phrases like: debug, error, stack trace, failed, broke, autopsy, root cause.

### Phrases that should load it

- “Here’s the stack trace—walk me through an autopsy.”
- “The test failed; hypothesize then give me the smallest check.”
- “This broke after the last change and I don’t know why.”

### Phrases that should *not* load it

- “Summarize what I learned from today’s successful deploy.” (Post-Task Retro)
- “Look at my week of notes and pick a practice focus.” (Weekly Skill Review)
- “Implement this feature from scratch” with no failure signal (normal build work)

## When *Not* to Activate

- Green-path feature work with no error to investigate.
- Style / refactor requests unrelated to a failure.
- Broad architecture debates framed as “what’s wrong with our system” with no concrete symptom.
- Weekly synthesis of many past errors (cluster those in Weekly Skill Review; use this skill per incident).

## Steps (encode these in the skill body)

1. **Capture the symptom.** Restate failure + the strongest observable (message, code, wrong result). Ask for a missing paste only if diagnosis is blocked.
2. **List 2–3 hypotheses**, ranked. Tie each to something in the symptom or recent change.
3. **Pick the smallest check** that distinguishes the top hypothesis (one command, one file, one reproduction). Prefer disconfirming over fishing.
4. **After evidence (or if the paste is enough):** state **root cause** in one line and **fix / next action** in one line.
5. **Optional learning tag:** one sentence the user could drop into a learning log (“Next time, check X before Y”).

If the user only wants a patch, still keep the autopsy skeleton short so the pattern stays visible.

## Output Format

Unless the user requests another shape, use:

```markdown
## Symptom
- What failed:
- Observable signal:

## Hypotheses (ranked)
1.
2.
3.

## Smallest check
- Do this next:
- What result would confirm / kill #1:

## Root cause (one line)
…

## Fix or next action (one line)
…

## Learning tag (optional)
…
```

## Boundaries

- Do not dump ten unrelated fixes; stay on the ranked path.
- Do not claim root cause without evidence unless the paste makes it obvious—and say when you are still guessing.
- Do not expand into a full redesign unless the user asks after the autopsy.
- Avoid secrets: redact tokens, keys, and personal data in any example output.
