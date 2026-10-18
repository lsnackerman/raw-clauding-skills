---
name: task
description: Create a living task doc from natural language. Use when you want to track work, capture a new project, or create a thinking log that accumulates context across sessions.
argument-hint: [task description]
---

# /task - Create a living task doc

Create a task doc from natural language. A thinking log that accumulates context, decisions, and observations over time.

---

## What to do

1. **Parse the request** — understand what work is being described
2. **Check for duplicates** — scan `tasks/` for similar titles. If found, ask: "There's already '{similar task}' — is this the same thing or distinct?"
3. **Figure out metadata** — topic, tags, priority
4. **Write the file** — with the structure below
5. **Note the connection** — this doc is what `/wrap` updates each session, including a SESSION INDEX line pointing at the captured session

---

## Task doc structure

**The block at the top is the handoff.** A task doc that lives across sessions mixes the worklist with the record, and the current state ends up somewhere inside a long file. The `NOW · DECIDED · OPEN` block is the one place that stays current: **rewrite it at the end of every session that touches the task** (`/wrap` does this), never append to it, never prefix a line with "done." Everything below the line is the record, which accretes. If a doc grows a second "state as of today" block on top of the first, that's the failure. Drain into the one block; don't stack.

```markdown
---
project: {project-name}     # when the task feeds a named project; also the filename prefix
# OR
area: {area-name}           # when there's no specific project (personal, system, tools)
tags:
  - {tag1}
  - {tag2}
priority: {P0|P1|P2|P3}
status: todo
created_date: {YYYY-MM-DD}
---

# {Title}

> ## ▶ NOW · DECIDED · OPEN — rewritten each session, never appended to
>
> **NOW (next session, in order):** {what to do first — five lines at most}
>
> **DECIDED (don't relitigate):** {calls already made}
>
> **OPEN (the human's calls):** {what's still theirs to decide}
>
> *Everything below this line is record.*

## WHAT

{Description — why this matters, context, what triggered this}

---

## WHO

{People involved — names, roles, current status}

---

## HOW

### Pending (Execute Next)
- [ ] {First action item}

### Completed (Append in order of completion)
<!-- Move items here when done, newest at bottom -->

---

## LINKS

<!-- Related files, docs, other tasks -->

---

## OBSERVATIONS (Cumulative)

*Patterns, friction, questions worth keeping, from you or the AI*

<!-- Add observations as they emerge across sessions -->

---

## SESSION INDEX

<!-- Pointers to captured sessions related to this work -->
<!-- Format: **Session N (YYYY-MM-DD)**: [filename] — one-liner of what happened -->

---
```

---

## Why this structure

Most task trackers give you a title and a checkbox. This gives you a thinking log.

- **NOW · DECIDED · OPEN** is where you land when you come back — current state in five lines, without reading the whole history
- **WHAT** holds the why, which keeps you oriented when you pick this up days later
- **HOW** splits pending from completed so you always know where you left off
- **OBSERVATIONS** is where the real value accumulates: patterns you noticed, friction you hit, questions that emerged
- **SESSION INDEX** links to your captured sessions so you can trace how the thinking evolved

---

## When a task is done

Archive completed tasks to `tasks/_done/` to preserve the thinking. The task doc is a record of how you got somewhere — decisions, dead ends, observations. That's worth keeping even after the work is finished. `/wrap` handles this when you mark a task done.

---

## Example

**Input**: `/task research markdown editors - want to find something that works on mobile and desktop for editing my system on the go`

**AI figures out**:
- area: tools (no named project → `area:`, and it becomes the filename prefix)
- tags: research, mobile
- priority: P2 (no urgency indicated)
- WHAT captures the why (mobile + desktop editing), not just the task

**Creates**: `tasks/tools - research markdown editors.md`. Every task doc takes the `{area or project} - {description}.md` shape, so a plain `ls tasks/` groups tasks by what the work feeds.

---

## Skill Check (after every task creation)

Quick scan: anything about this task creation that felt off or could be smoother?

- Was the WHAT section clear enough for future you?
- Did the structure feel right for this type of work?
- Was anything missing that you'd want next time you pick this up?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every task teaches something.
