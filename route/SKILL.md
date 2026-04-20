---
name: route
description: Route conversation content to the right files mid-session. Use after a decision, update, correction, or new datum lands in conversation. Lightweight capture, session continues after.
---

# /route — Land It Where It Lives

Mid-session routing. Takes what was just discussed and lands it in the right files without wrapping.

**When to use:** After something lands in conversation that needs to be in the system — a scheduling update, a decision, a correction, new texture on an existing topic, a factual change. Anytime you'd say "update the files" but the session isn't done.

**When NOT to use:** End of session (use /wrap). Nothing worth capturing yet. Deep in flow and routing would break momentum.

---

## The Flow: Surface → Grep → Read → Map → Route → Confirm

### 1. Surface

State back what just happened that needs routing. Keep it concise. One to three bullets max.

Example: *"Decision to switch from weekly to biweekly standups. New deadline for the v2 launch is May 6. Budget cap raised to $5k for the project."*

This is what your partner approves before anything gets touched.

### 2. Grep

Search the system for everywhere this topic already lives. Don't assume you know — **grep first.**

```
Search for: the topic name, the person's name, related keywords
Across: the full system (working docs, projects, tasks, references)
```

This is what prevents missed files. A scheduling update might live in `ALIVE.md` AND a project CLAUDE.md AND a task doc. Without grepping, you'd likely hit two and miss two.

### 3. Read

For every file the grep found, **read the section that needs updating.** Understand what's already there before touching it.

**This is the anti-tribble guard.** You are reading to:
- See the full existing content (not just the line that matched the grep)
- Identify what must be **preserved** (details, dates, context, links, attribution)
- Identify what needs to be **changed** (the outdated or incomplete part)
- Identify what needs to be **added** (the new information from conversation)

If the section is long or detailed, read it carefully. The risk is not adding wrong information — it's **silently losing correct information** during the edit.

### 4. Map

Present the routing plan to your partner. For each file:

- **File + section**: which file, which part
- **Preserving**: what existing detail stays (name the specifics)
- **Changing**: what's being updated
- **Adding**: what's new
- **Removing**: what's being deleted outright, **with a "why stale" justification**

Example (with removal):
> **`ALIVE.md` → What's Next**
> - Preserving: all other pending items, existing format, sequencing
> - Changing: standup cadence entry (currently shows weekly)
> - Adding: new budget cap with date and reason
> - Removing: "old launch date May 1" — why stale: superseded by new May 6 decision

Removal is first-class but skeptical. /route's default is preserve — if a verb doesn't explicitly mark something for Change or Remove, it stays. That bias is a feature. When removal is the right call, make it deliberate: name the item, name why it's stale, confirm the texture lives somewhere else (or doesn't need to). Don't fold removals into a replace ("change X to nothing") — call them out separately so your partner can sanity-check the deletion.

**Wait for approval before editing.** This is where lost information gets caught (before the edit, not after).

### 5. Route

Make the edits. One file at a time.

**Rules:**
- **Read before replacing.** The Edit tool does string replacement. Make sure the old text captures the full block being replaced and the new text carries forward everything that matters.
- **Contradiction check.** Before writing a new fact, verify it doesn't conflict with something elsewhere in the same file. If it does, flag it (don't silently overwrite).
- **Append-then-prune on durable files.** For files that accumulate (ALIVE.md, project READMEs, reserves), read existing entries first. Don't accidentally drop items that weren't part of this conversation. Only change the entries relevant to what's being routed.
- **Removals need justification.** If the Map step flagged something for Remove, the "why stale" reason surfaces in the Confirm step too, not buried in the diff. A removal without a stated reason is a red flag so pause and re-check.
- **Preserve voice.** If the existing text has a specific voice or phrasing, carry it forward. Don't flatten it into AI summary voice.
- **Temporal markers.** Add `(as of YYYY-MM-DD)` to facts with a shelf life — scheduling, pricing, project status, relationships, anything that changes over time.

### 6. Confirm + Flag

After edits are done:

**Confirm:** One line per file showing what landed where. Quick and scannable.

> - `ALIVE.md`: standup cadence updated, budget cap added (as of 2026-04-19)
> - `projects/v2-launch/README.md`: Key Decisions — new deadline noted

**Flag (optional):** If the conversation also surfaced something that connects to another topic but doesn't need immediate routing, name it. Don't force it, just flag it.

> *Flag: the budget conversation touched on team capacity; potential future texture for the staffing doc if we want to capture it later.*

If the flag is worth resurfacing (not just in this session's record), park it in `ALIVE.md` with a `[flag]` prefix. /wrap triages flags: convert to real items, route elsewhere, or leave as-is.

If the flag is just conversational context — a secondary connection that'll resurface naturally if it matters — leave it in the session capture. Not every flag needs to persist.

Then: **"What's next?"** — the session continues.

---

## Quick Version

1. **Surface** — what needs routing? (1-3 bullets, partner approves)
2. **Grep** — find everywhere this topic lives
3. **Read** — read each section before touching it (anti-tribble guard)
4. **Map** — show preserving / changing / adding / removing (with why-stale) per file (partner approves)
5. **Route** — make the edits (contradiction check, append-then-prune, removals-need-justification, preserve voice, temporal markers)
6. **Confirm + Flag** — what landed where, plus optional secondary connections

**Then keep working.** /route is not /wrap. The session continues.

---

## Common Routing Destinations (Examples, Not Exhaustive)

- **`ALIVE.md`** — what's next, ideas, brain dumps
- **Project READMEs / CLAUDE.md / AGENTS.md** — key decisions, landscape shifts, new vocabulary for a project
- **Task doc OBSERVATIONS section** — patterns, friction, decisions that surface while working
- **Skills** — when something changes how you do a skill (update the skill now, don't wait for /wrap)
- **Reserves** — feeding a concept hub with new texture mid-session (if you use `/explore`, the reserve it built)
- **Strategy / reference docs** — positioning, decisions, working notes
- **AI's space** (`ai/` is a good default) — when the new texture is reflective rather than operational

---

## What /route Is NOT

- **Not /wrap.** No `ALIVE.md` rewrite. No session capture. No AI compound scan. No task doc housekeeping. Those happen at end of session.
- **Not a brain file sweep.** /route is topic-scoped (route what we just discussed), not session-scoped (route everything from this session).
- **Not a place to create new files.** /route updates existing files. If something genuinely needs a new file, that's a separate decision — flag it, don't auto-create. (Anti-tribble: one good doc beats three scattered ones.)

---

## The Boundary Between /route and /wrap

| | /route | /wrap |
|---|---|---|
| **When** | Mid-session | End of session |
| **Scope** | One topic / conversation thread | Full session |
| **Touches `ALIVE.md` handoff** | No | Yes (full rewrite during /wrap) |
| **Session capture** | No | Yes (`/sync`) |
| **AI compound scan** | No | Yes (Step 0) |
| **Task doc housekeeping** | No | Yes |
| **Pattern check** | No (flag if you notice one) | Yes |

/route is the scalpel. /wrap is the full surgery. Use both — /route as many times as needed during the session, /wrap once at the end.

---

## Skill Check (After Every Route)

Quick scan: anything about this routing that felt off or could be smoother?

- Did the Grep step find everywhere the topic lived, or did we miss a file?
- Did the Map step catch something that would have been silently lost in a direct edit?
- Did the Confirm step accurately reflect what landed, or was something off?
- Anything in the flow that slowed us down without adding signal?
- Does this route earn its ceremony, and if not — is it the skill or the work?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. /route worked, keep going.
