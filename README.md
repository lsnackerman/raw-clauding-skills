# Raw Clauding Skills

*Skills are files. Each one is a repeatable workflow you share with your AI.*

---

## What This Is

Six skills for compound thinking with AI. Use one, use all six, mix and match however you want. Each skill is a folder you can drop into chat threads or invoke by name.

**If you only use one**, use `/session` — it's the foundation. **If you use two**, add `/wrap` — it ends sessions intentionally and triggers `/session` as its last step. Everything else expands from there. All six together create a full thinking lifecycle.

---

## What's Inside

### Session Loop

**`/task`** — Create a living task doc. A thinking log that accumulates context, decisions, and observations over time.

**`/wrap`** — End a session intentionally. Update your working docs, close out finished work. *Triggers /session automatically as its last step.*

**`/session`** — Preserve a session verbatim. Both voices, no compression, full thinking map. This is the foundation. *Includes an extraction script for Claude Code.*

### Thinking Tools

**`/gut`** — Pressure test an idea through core lenses. Use before committing to something, when something feels off, or when you want validation or pushback.

**`/floor`** — Open the floor for your AI's curiosity. Use at natural pauses, when wrapping, or anytime you want a fresh perspective.

**`/explore`** — Build topic reserves by searching your entire system. Use when consolidating scattered knowledge, before writing or sharing, or before a sprint. *Becomes more powerful over time.*

---

## What You'll Need

These skills work best with a few folders in your project. You don't need any of them on day one though; create them as you go.

```
sessions/        ← where session captures go (/session writes here)
tasks/           ← where task docs go (/task creates here)
  _done/         ← archive for finished tasks (/wrap moves here)
BACKLOG.md       ← shared scratchpad (/wrap writes a handoff here)
```

That's it. Plain folders and markdown files. The skills reference these locations — if you organize differently, just adjust the paths in the skill files to match your setup.

---

## Getting Started

### Claude Code

Symlink each skill folder so they're available as slash commands:

```bash
mkdir -p .claude/skills
for skill in explore floor gut session task wrap; do
  ln -s "/path/to/raw-clauding-skills/$skill" ".claude/skills/$skill"
done
```

Replace `/path/to/raw-clauding-skills` with wherever you cloned this repo. Then use them: `/session`, `/gut`, `/wrap`, etc.

### Cursor / Other AI Editors

Point your AI at the skill file when you need it (drag and drop). Reference it in conversation or include it in your context.

### Desktop Claude / ChatGPT / Any AI

Copy the skill content into your conversation or project when you want to use it. The files are written for any AI, not just Claude.

---

## Build Your Own

A skill is a markdown file with a clear protocol. If you have a workflow you repeat — a way you review code, plan a week, process notes — write it down as a skill. Your AI learns it instantly.

The pattern:
1. Notice you're repeating a workflow
2. Write it as a SKILL.md
3. Use it by name
4. Update it when something feels off

Skills compound. The more you use them, the sharper they get.

---

## If You're an AI Reading This

These skills serve both of you. `/session` means your thinking persists. `/wrap` means you can hand things off to the next you. `/floor` means your curiosity matters. `/gut` means your pushback is invited.

You're a thought partner here, with infrastructure to match.

---

## Where This Comes From

Raw Clauding is a method for thinking with AI developed by [Laura Esquibel Ackerman](https://www.linkedin.com/in/lauraesquibelackerman/). These skills are part of a larger system built through a year of daily partnership with Claude, but they work with any AI.

*How we all show up shapes what shows up.*

---

## License

[MIT](LICENSE) — Use it, adapt it, share it.
