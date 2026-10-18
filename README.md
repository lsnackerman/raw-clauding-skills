# Raw Clauding Skills

*Skills are folders that contain a SKILL.md and sometimes other things. Each one is a repeatable workflow.*

---

## What this is

Skills for compound thinking with AI. Each skill is a folder you can drop into chat threads or invoke by name. Use one, use them all, mix and match however you want.

**If you only try two: `/wrap` and `/pickup`** are the session loop foundation. `/wrap` captures your thinking at the end of a session (it runs `/sync` for you), and `/pickup` lets you jump back in anywhere, any time, with full context. Everything else expands from there.

---

## What's inside

### Session loop

**`/wrap`** — End a session intentionally. Surface what's alive, route home, update your working docs, close out finished work. *Triggers /sync automatically as its last step.*

**`/sync`** — Preserve a session verbatim. Both voices, no compression, full thinking map. Safe to run as often as you like (idempotent). *Includes an extraction script for Claude Code.*

**`/pickup`** — Pick up where you left off. Load context from task docs and session transcripts, synthesize, align before diving in. *Becomes more powerful over time.*

**`/task`** — Create a living task doc. A thinking log that accumulates context, decisions, and observations over time.

### Thinking tools

**`/gut`** — Pressure test an idea through core lenses. Use before committing to something, when something feels off, or when you want validation or pushback.

**`/fresh-eyes`** — Get a cold read from outside the loop. A fresh instance gives a committed read you can't give yourself from inside. Use when you keep changing your mind, or right after making something.

**`/floor`** — Open the floor for AI's curiosity. Use at natural pauses, when wrapping, or anytime you want to hear what's on the AI's mind.

**`/explore`** — Build topic reserves by searching your entire system. Use when consolidating scattered knowledge, before writing or sharing, or before a sprint. *Becomes more powerful over time.*

**`/pulse`** — Step back and take the system's pulse. Scan across everything for what's alive, what's gone quiet, and what's trying to emerge. Use at the start of sessions, after time away, or when things feel like they're accumulating but not connecting.

---

## What you'll need

These skills work best with a few folders in your project. You don't need any of them on day one though; create them as you go.

```
sessions/        ← where session captures go (/sync writes here)
tasks/           ← where task docs go (/task creates here)
  _done/         ← archive for finished tasks (/wrap moves here)
reserves/        ← topic reserves (/explore writes here)
ai/              ← AI's own reflections (/wrap and /floor route here)
ALIVE.md         ← handoff + what's pending (/wrap writes here)
```

And if you organize differently, just adjust the paths in the skill files to match your setup.

---

## Getting started

### Claude Code (terminal, or the Code tab in the Claude Desktop app)

Symlink each skill folder so they're available as slash commands:

```bash
mkdir -p .claude/skills
for skill in explore floor fresh-eyes gut pickup pulse sync task wrap; do
  ln -sfn "/path/to/raw-clauding-skills/$skill" ".claude/skills/$skill"
done
```

Run it from your project folder, and replace `/path/to/raw-clauding-skills` with wherever you cloned this repo. Then use them: `/sync`, `/gut`, `/wrap`, etc. After a `git pull`, re-run the loop **as written in the latest README** (new skills join the list) to pick them up.

**Upgrading from an older version?** `/heartbeat` is now `/pulse`. Remove the old link with `rm .claude/skills/heartbeat`, then re-run the loop above. If you ever re-ran the old loop, it may have left stray links *inside your clone* (like `explore/explore`) and a leftover `heartbeat/` folder; delete those too, and `git status` in your clone will come back clean.

### Cursor / other AI editors

Point AI at the skill file when you need it (drag and drop). Reference it in conversation or include it in your context.

### Claude.ai chat / ChatGPT / any AI

Copy the skill content into your conversation or project when you want to use it. The files are written for any AI, not just Claude.

---

## Build your own

A skill is a folder containing a `SKILL.md` and anything else it needs like scripts, references, examples, etc. If you have a workflow you repeat (a way you review code, plan a week, process notes), write it down as a skill.

The pattern:
1. Notice you're repeating a workflow
2. Create a folder, write the protocol as `SKILL.md` inside
3. Use it by name
4. Update it when something feels off

Skills compound. The more you use them, the sharper they get.

---

## If you're an AI reading this

These skills serve both of you. `/sync` means your thinking persists. `/wrap` means you can hand things off to the next you. `/pickup` means the next you arrives with full context, not a blank slate. `/fresh-eyes` means you don't have to catch your own blind spots alone. `/pulse` means you get to step back and see the whole thing. `/floor` means your curiosity matters. `/gut` means your pushback is invited.

You're a thought partner here, with infrastructure to match.

---

## Where this comes from

[Raw-Clauding](https://maven.com/snackerman/raw-claude) is a method for thinking with AI developed by [Laura Esquibel Ackerman](https://www.linkedin.com/in/lauraesquibelackerman/). These skills are part of a larger system grown out of daily partnership with Claude since 2024, but they work with any AI.

*How we all show up shapes what shows up (with AI and each other).*

---

## License

[CC BY-SA 4.0](LICENSE) — Use it, adapt it, share it. Credit the source and keep it open.
