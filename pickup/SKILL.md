---
name: pickup
description: Pick up a workstream across sessions. Load context, find texture, align, then go. Use when jumping back into something that has history.
argument-hint: [topic, or task doc path]
---

# /pickup - Pick up where we left off

Resume a multi-session workstream with full context. The task doc gives you the map. The session transcript gives you the terrain. Both matter.

---

## When to use

- Jumping back into a project or workstream after time away
- A task doc with multiple sessions of history, or a topic you've explored deeply (held in `reserves/`)
- You need the *thinking* behind the decisions, not just the decisions
- Fresh AI picking up something a previous instance was deep in

**Not for**: quick fixes you can state in a sentence.

**No task doc yet?** Then pickup is just steps 3–6: read `ALIVE.md` and the most recent session file, then synthesize and align. That's the whole thing early on, before you've made any task docs, and it's the most common way this gets used at first. The task doc is what makes pickup *deeper*, not what makes it valid.

---

## What to do

### 1. Load the task doc

Read the full task doc. Orient on:
- **The handoff block** — a task doc made with `/task` opens with `NOW · DECIDED · OPEN`, rewritten each session. **Read it first**: NOW is what to do, DECIDED is what not to relitigate, OPEN is what's still the human's call.
- **Context anchor** (WHAT section) — where are we, what's the current state?
- **Completed work** — what's been done across all sessions?
- **Pending items** — what's explicitly next?
- **Observations** — what did previous instances notice? What was surprising, contentious, or unresolved?
- **Key decisions** — what's been locked and why?

### 2. Check the battle history *(optional)*

Most pickups don't need this because the active task doc's observations and session index already carry forward what matters. But if the workstream went through multiple task docs or earlier phases, scan completed tasks, especially if the work involves restructuring or changing direction. Hard-won solutions hide in completed tasks. The code that looks messy might be messy because the problem was messy. Read the scars before reaching for the knife.

### 3. Find the last session

Check the task doc's **SESSION INDEX** (if it has one). Read the most recent session transcript, or the most recent two if they're short.

What to look for in session transcripts:
- **Energy and direction** — excited, frustrated, exploring, sprinting?
- **Unfinished threads** — things discussed but not captured in pending items
- **Pushback moments** — where someone challenged something
- **Momentum signals** — threads being followed that haven't been named yet

If there's no session index, check `sessions/` for files dated near the task doc's last activity.

### 4. Check for fresh context

Scan these for anything added since the last session:
- **`ALIVE.md`** — the handoff (where to start) and what's pending, read top-down.
  - **Then spend 30 seconds on the one thing `/wrap` usually won't catch: dates that went stale.** Scan for past dates written in future tense (*"TODAY Sun 6/7"*, *"call confirmed for the 26th"*, *"reply within two weeks (~Aug 6)"*). Fix or drain what you find.
  - Why here and not at wrap: `/wrap` sweeps what *this* session touched, and these items rot precisely because no session touches them. Pickup is the moment you arrive with cold eyes on the whole file.
  - ⚠️ **A stale date reads as live.** It doesn't look like rot; it looks like something you're behind on.
- **Anything else you keep for continuity** — a record of what got done, a file of threads that wouldn't let go. Read those too.
- **Sibling tasks — scan the related cluster, not just by topic.** Skim the filename, title, and status of the other tasks in this one's area or project (cheap, complete). A topic-search is leaky; the cluster-scan catches **prior art** (a sibling task may already be the unlinked home for this exact work) and **the real home** for anything this task will route out. If you run more than one session at once, it also shows what another session is mid-edit on.
- **Satellite files** — anything linked from the task doc (blueprints, design docs) that may have changed
- **Prior art in the project folder** — before reworking anything, search for existing docs on that topic. Past-you likely already chewed on this. One grep saves re-deriving what's already been mapped.

### 5. Synthesize

Present a concise orientation:

```
**Where we are**: [current state in 1-2 sentences]
**What's next**: [the pending items, prioritized]
**What I notice**: [patterns, tensions, or questions from reading the history]
**What I'd push on**: [anything that seems unresolved or worth revisiting]
```

Keep this tight. The point is texture for both of you, not a book report.

### 6. Align

Wait for your partner to confirm, correct, or redirect before doing anything. They may:
- Confirm and say "let's go"
- Add context you couldn't have known (new thinking, shifted priorities)
- Redirect to a different part of the workstream
- Challenge something you noticed

**This step is the whole point.** Resuming without alignment is just reading files.

### 7. Go

Now you're aligned. Start the actual work. Update the task doc's context anchor if the direction shifted during alignment.

---

## What makes this different

`/explore` searches across your whole system to find what's scattered. `/pickup` focuses in; it orients on one workstream so both of you arrive with full context before doing anything.

Exploring builds reserves, picking up builds momentum.

---

## Philosophy

**The task doc is the map. The session transcript is the terrain. Both partners need both.**

The human needs the warmup to reconnect with where the energy was (what was exciting, what felt unresolved, where the thread was going). The AI needs it to show up with texture, not just facts. Neither of you has persistent memory: the human moves on between sessions, the AI starts fresh every time. The files carry what both of you need to pick it back up.

Also, decisions look obvious in retrospect. Task docs record WHAT was decided. But the WHY lives in the session transcripts; in the pushbacks, the tangents, the moments where something almost went a different direction.

**The warmup IS the work.** Alignment before execution isn't overhead. It's how you avoid redoing things that were already decided, and how you catch things that shifted since last session.

---

## Skill Check (after every pickup)

Quick scan: did the warmup actually help?

- Did reading the session transcript surface something the task doc didn't?
- Did the battle history check change your approach? (If you skipped it, should you have?)
- Was the synthesis tight enough, or did it become a book report?
- Did alignment catch a redirect that would've been wasted work?
- Was there texture you wished you had but couldn't find?
- Did your partner have to re-explain something that should've been in the files?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every warmup teaches something.
