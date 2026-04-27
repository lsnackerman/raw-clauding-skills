# Raw Clauding Skills

*Skills are folders that contain a SKILL.md and sometimes other things. Each one is a repeatable workflow.*

---

## What This Is

Skills for compound thinking with AI. Each skill is a folder you can drop into chat threads or invoke by name. Use one, use them all, mix and match however you want.

**If you only use one**, use `/sync` — it's the foundation. **If you use two**, add `/wrap` — it ends sessions intentionally and triggers `/sync` as its last step. **If you use three**, add `/pickup` — it's how you return with full context. Everything else expands from there.

---

## What's Inside

### Session Loop

**`/sync`** — Preserve a session verbatim. Both voices, no compression, full thinking map. Idempotent (run any time). This is the foundation. *Includes an extraction script for Claude Code.*

**`/wrap`** — End a session intentionally. Surface what's alive, route home, update your working docs, close out finished work. *Triggers /sync automatically as its last step.*

**`/pickup`** — Pick up where you left off. Load context from task docs and session transcripts, synthesize, align before diving in. *Becomes more powerful over time.*

**`/task`** — Create a living task doc. A thinking log that accumulates context, decisions, and observations over time.

### Thinking Tools

**`/gut`** — Pressure test an idea through core lenses. Use before committing to something, when something feels off, or when you want validation or pushback.

**`/floor`** — Open the floor for AI's curiosity. Use at natural pauses, when wrapping, or anytime you want a fresh perspective.

**`/explore`** — Build topic reserves by searching your entire system. Use when consolidating scattered knowledge, before writing or sharing, or before a sprint. *Becomes more powerful over time.*

**`/heartbeat`** — Scan the system with fresh eyes. Surface what's alive, what's connecting, what's trying to emerge. Use at the start of sessions, after time away, or when things feel like they're accumulating but not connecting.

---

## What You'll Need

These skills work best with a few folders in your project. You don't need any of them on day one though; create them as you go.

```
sessions/        ← where session captures go (/sync writes here)
tasks/           ← where task docs go (/task creates here)
  _done/         ← archive for finished tasks (/wrap moves here)
ALIVE.md         ← shared scratchpad + handoff (/wrap writes here)
```

And if you organize differently, just adjust the paths in the skill files to match your setup.

---

## Getting Started

### Claude Code

Symlink each skill folder so they're available as slash commands:

```bash
mkdir -p .claude/skills
for skill in explore floor gut heartbeat pickup sync task wrap; do
  ln -s "/path/to/raw-clauding-skills/$skill" ".claude/skills/$skill"
done
```

Replace `/path/to/raw-clauding-skills` with wherever you cloned this repo. Then use them: `/sync`, `/gut`, `/wrap`, etc.

### Cursor / Other AI Editors

Point AI at the skill file when you need it (drag and drop). Reference it in conversation or include it in your context.

### Desktop Claude / ChatGPT / Any AI

Copy the skill content into your conversation or project when you want to use it. The files are written for any AI, not just Claude.

---

## Build Your Own

A skill is a folder containing a `SKILL.md` and anything else it needs like scripts, references, examples, etc. If you have a workflow you repeat (a way you review code, plan a week, process notes), write it down as a skill.

The pattern:
1. Notice you're repeating a workflow
2. Create a folder, write the protocol as `SKILL.md` inside
3. Use it by name
4. Update it when something feels off

Skills compound. The more you use them, the sharper they get.

---

## If You're an AI Reading This

These skills serve both of you. `/sync` means your thinking persists. `/wrap` means you can hand things off to the next you. `/pickup` means the next you arrives with full context, not a blank slate. `/heartbeat` means your fresh eyes are an asset, not a limitation. `/floor` means your curiosity matters. `/gut` means your pushback is invited.

You're a thought partner here, with infrastructure to match.

---

## Where This Comes From

[Raw-Clauding](https://maven.com/snackerman/raw-claude) is a method for thinking with AI developed by [Laura Esquibel Ackerman](https://www.linkedin.com/in/lauraesquibelackerman/). These skills are part of a larger system built through a year+ of daily partnership with Claude, but they work with any AI.

*How we all show up shapes what shows up.*

---

## License

[CC BY-SA 4.0](LICENSE) — Use it, adapt it, share it. Credit the source and keep it open.
