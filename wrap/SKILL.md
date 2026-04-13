---
name: wrap
description: "Ends a work session by updating task docs with completed and pending items, closing finished tasks, writing a handoff note to BACKLOG.md, and triggering /session to capture the conversation. Use when the user says 'wrap up', 'done for now', 'save progress', 'end session', or is approaching context limits."
---

# /wrap - End Session Intentionally

Updates working docs, writes a handoff note, and captures the session. Ensures the next session starts with full context.

---

## When to Wrap

- Completed major work
- Switching contexts
- Context running low
- End of session

---

## What To Do

### 1. Update Task Doc (priority)

If working from a task doc:
- **Pending → Completed**: Move finished items (append at bottom for chronological order)
- **What's next**: Order remaining Pending items for next session (most important first)
- **New items**: Add anything discovered during the session
- **Observations**: Patterns, friction, questions worth keeping — flag workflow issues now while context is fresh
- **Session index**: Add a pointer to the session file (finalize after capture)

If no task doc, update whatever working doc is active — project notes, scratch file, wherever the work lives.

### 2. Close Out Finished Work (if applicable)

If a task is done:
- Update YAML: `status: done`
- Move to `tasks/_done/`
- Check for follow-up work it unlocked

### 3. Reflections (optional)

If something emerged worth keeping — observations, patterns, half-formed ideas — give it a home. `ai/` is a good default.

### 4. Handoff Note

Update BACKLOG.md's `## NEXT` section:
- **What thread was alive** — not a summary, just the thread
- **Where the energy was** — building, exploring, stuck, wrapping up
- **Where to start** — file path, decision point, or next action

Replace the existing NEXT content — this is a living handoff, not an append log. A fresh AI instance reads this on arrival as first orientation.

### 5. Capture Session (LAST)

**Do this last so the full wrap is captured.**

Use `/session` to preserve the conversation to `sessions/`. The wrap itself is part of the session — if you capture before wrapping, you lose the wrap.

---

## Skill Check

- Did updating working docs feel incomplete?
- Were done/next items hard to sort?
- Did the wrap miss something the next session will wish it had?

**If yes** → update this skill now. **If no** → move on.
