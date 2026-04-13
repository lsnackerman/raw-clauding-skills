---
name: pickup
description: "Reads previous session logs and task docs, summarizes outstanding tasks and key decisions, and identifies next steps for resuming a multi-session workstream. Use when the user asks to resume, continue where they left off, pick up a previous session, or return to an ongoing project."
argument-hint: [task doc path]
---

# /pickup - Pick Up Where We Left Off

Resume a multi-session workstream with full context. The task doc gives the map. The session transcript gives the terrain. Both matter.

---

## When to Use

- Jumping back into a project or workstream after time away
- Task doc has multiple sessions of history
- Need the *thinking* behind decisions, not just the decisions
- Fresh AI picking up something a previous instance was deep in

**Not for**: fresh tasks, quick fixes, or things that fit in one session.

---

## What To Do

### 1. Load the Task Doc

Read the full task doc. Orient on:
- **Context anchor** (WHAT section) — current state
- **Completed work** — what's been done across all sessions
- **Pending items** — what's explicitly next
- **Observations** — what did previous instances notice? What was surprising or unresolved?
- **Key decisions** — what's been locked and why

### 2. Check the Battle History

If completed task docs from earlier phases exist, scan them — especially if the work involves restructuring or changing direction. Hard-won solutions hide in completed tasks.

### 3. Find the Last Session

Check the task doc's **SESSION INDEX** (if present). Read the most recent session transcript — or the most recent two if short.

Look for:
- **Energy and direction** — excited, frustrated, exploring, sprinting?
- **Unfinished threads** — things discussed but not captured in pending items
- **Pushback moments** — where someone challenged something
- **Momentum signals** — threads being followed that haven't been named yet

If no session index exists, check `sessions/` for files dated near the task doc's last activity.

### 4. Check for Fresh Context

Scan for anything added since the last session:
- **BACKLOG.md** — brain dumps or new ideas related to this work
- **Related tasks** — search `tasks/` for sibling tasks on the same topic
- **Satellite files** — anything linked from the task doc that may have changed

### 5. Synthesize

Present a concise orientation:

```
**Where we are**: [current state in 1-2 sentences]
**What's next**: [the pending items, prioritized]
**What I notice**: [patterns, tensions, or questions from reading the history]
**What I'd push on**: [anything that seems unresolved or worth revisiting]
```

### 6. Align

Wait for the user to confirm, correct, or redirect before doing anything. They may:
- Confirm and say "let's go"
- Add context not available in files (new thinking, shifted priorities)
- Redirect to a different part of the workstream
- Challenge something you noticed

**Do not proceed to work without explicit alignment.**

### 7. Go

Start the actual work. Update the task doc's context anchor if direction shifted during alignment.

---

## Skill Check

- Did reading the session transcript surface something the task doc didn't?
- Was the synthesis tight enough, or did it become a book report?
- Did alignment catch a redirect that would've been wasted work?
- Did the user have to re-explain something that should've been in the files?

**If yes** → update this skill now. **If no** → move on.
