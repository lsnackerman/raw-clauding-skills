---
name: wrap
description: End work session intentionally. Use at natural stopping points, before context limits, or when switching contexts.
---

# /wrap - End Session Intentionally

Quick, intentional session ending. Preserves work, ensures continuity.

---

## What To Do

### 1. Update Task Doc (priority)

If you're working from a task doc:

- **Pending → Completed**: Move finished items. Append at bottom so chronological order is preserved.
- **What's next**: Order remaining Pending items for next session (most important first)
- **New items**: Add anything discovered during the session
- **Observations**: Patterns, friction, questions worth keeping. Did anything about your tools or workflow cause friction? Fix it now or flag it — you have the context, next-you won't.
- **Session index**: Add a pointer to the session file (finalize after capture)

If you're not working from a task doc, update whatever working doc is active — project notes, scratch file, wherever the work lives.

### 2. Close Out Finished Work (if applicable)

If a task is done-done:
- Update YAML: `status: done`
- Move to `tasks/_done/` — the thinking is worth keeping
- Check for follow-up work it unlocked

### 3. Reflections (optional)

If something emerged worth keeping — for you or your AI:
- Observations, curiosities, patterns noticed
- Things that surfaced but didn't fit the main work
- Half-formed ideas worth returning to

Give these a home somewhere. `ai/` is a good default. Don't let them evaporate with the session.

### 4. Handoff Note

Update BACKLOG.md's `## NEXT` section with a pointer for next-you (human and AI):

- **What thread was alive** — not a summary, just the thread
- **Where the energy was** — building, exploring, stuck, wrapping up
- **Where to start** — file path, decision point, or next action

Replace the existing NEXT content — this is a living handoff, not an append log. Keep it short. A fresh AI instance reads this on arrival; it's their first orientation after AGENTS.md/CLAUDE.md/etc. The human reads it when they forget where they were.

BACKLOG.md is 50/50 — the human writes brain dumps and ideas there, you write the handoff. Both of you use it.

### 5. What Stuck? (optional)

Quick scan: anything click this session?
- A pattern you'd want to remember
- Something that surprised you
- A question that's still forming

Jot it in your task doc's observations section, or drop it in BACKLOG.md. You're teaching future-you — that's how the thinking compounds.

### 6. Capture Session (LAST)

**Do this last so the full wrap is captured.**

Use `/session` to preserve the conversation to `sessions/`. The wrap itself is part of the session — decisions made, items reordered, observations noted. If you capture before wrapping, you lose the wrap.

---

## When to Wrap

- Completed major work
- Switching contexts
- Context running low
- End of session

---

## Skill Check (After Every Wrap)

Quick scan: anything about this wrap that felt off or could be smoother?

- Did updating working docs feel incomplete?
- Were done/next items hard to sort?
- Did observations get lost or feel forced?
- Did the wrap miss something the next session will wish it had?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every wrap teaches something.
