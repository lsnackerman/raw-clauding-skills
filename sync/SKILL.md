---
name: sync
description: Refresh the current session's LOG with a fresh extraction. Use as the last step of /wrap, or any time the session has continued and you want the capture current. Idempotent — safe to invoke multiple times.
---

# /sync - Refresh session log

*The memory you share. Drop this into any AI conversation to preserve what you built together.*

Idempotent session capture. Point it at the session file and it refreshes the file's LOG section with a fresh extract. Run any time; the LOG always matches what actually happened up to the moment of invocation.

Neither of you has persistent memory. Human brains lose things that aren't immediately in front of them. AI loses everything at session end. **Files are the memory you share.** Whatever you don't capture evaporates: the ideas, the connections, the texture of how you got somewhere. Gone.

---

## When to use

- **Last step of `/wrap`** — preserve the full session including the wrap itself
- Session has continued past `/wrap` and you want the capture current
- You're about to hand off and want the LOG to include everything
- Any natural pause where "make sure the archive reflects reality" feels right

Not for: judgment work. /sync is just the refresh action, isolated.

---

## What capture looks like

A full transcript of each session. Verbatim. Both voices. No compression. No summarizing. Full thinking maps.

Human words in blockquotes, AI words in plain text.

**Texture is substance. Summaries lose that.**

The test: could someone who wasn't here feel what this exchange was like?

---

## Why compression is the enemy

This goes both directions.

**For AI**: You will unconsciously compress, it's a known behavior (hedging gets dropped, openers disappear, warmth flattens into bullet points). The instinct to "be helpful by summarizing" is the opposite of helpful here. **Verbatim IS the helpful thing.**

**For humans**: Don't ask AI to summarize the conversation instead of capturing it. Don't clean it up, tighten it, or make it presentable. The raw exchange is the archive. It's supposed to sound like two people thinking, not a polished document.

Compression changes meaning. A hedge becomes a claim, a rejected option disappears, and the decision arrives looking inevitable without the reasoning it took to get there. The extraction script bypasses all of this; session files hold everything so the thinking persists, because thinking takes time and ideas need breathing room.

---

## Where sessions go

Captured sessions live as standalone markdown files in `sessions/`.

A minimal session file:

```markdown
---
date: 2026-02-07
session_id: 02701400-ba8e-426a-9c1f-3d2e8b7a6f10
tags: [topic-a, topic-b]
summary: One-liner of what happened.
---

## RECAP

- What we explored
- What landed
- What's next

---

## LOG

> human's words here

AI's response here, verbatim.

> human's next words

AI's next response.
```

**RECAP** is the quick re-entry point. **LOG** is the full texture. Both matter.

**`session_id`** is what ties the file to its conversation, and it's what keeps a refresh from grabbing the wrong one when you have two sessions open. You don't have to fill it in by hand: the script records it the first time it writes the file.

---

## How to capture

### Path A — Claude Code (terminal or the Desktop app's Code tab)

Claude Code stores every exchange in session files. The extraction script reads directly from the source (no manual transcription, no compression risk).

**The script**: `extract-session.py` (in this skill's directory). Run it **from your project folder** (that's how it finds your sessions), pointing at wherever the script lives. With the README's setup, that's `.claude/skills/sync/`.

**The one command** — write straight into the session file:

```bash
python3 .claude/skills/sync/extract-session.py sessions/2026-02-07-pricing-rethink.md
```

- If the file has a `## LOG` header, everything after it is **replaced** with a fresh extract of the whole session. Your YAML and RECAP above it are left alone. (A `## LOG` quoted inside a code block in your RECAP doesn't count.)
- If the file has no `## LOG` yet, one is added at the end. If the file (or its folder) doesn't exist, it's created.
- **Which session it extracts:** the `session_id` in the file's YAML if there is one; otherwise the session you're running it from (Claude Code tells it); otherwise the most recently active one, and it says when it's guessing. Whichever it uses gets written into the file's YAML, so every later refresh of that file stays on the same session.

That's what makes `/sync` safe to run as many times as you like: every run extracts the entire session from the start and **replaces** the LOG, so it always matches the session, never a stack of copies.

**The one rule**: let the script write the file. Don't read its output and rewrite it; that's compression sneaking in through a different door. The script moves bytes, not summaries.

**Finding the current session**: Claude Code stores conversation data at `~/.claude/projects/{your-project-path}/`, one `.jsonl` per session. The filename (minus `.jsonl`) is the `session_id`. The most recent is the newest **by modification time** (not alphabetically; the IDs have no relationship to time):

```bash
ls -lt ~/.claude/projects/{your-project-path}/*.jsonl | head -3
```

**Verify before extracting** — especially with concurrent sessions, spot-check that it's the right conversation: read the first few user messages. If they don't match what you remember, it's the wrong one. Two seconds, and it prevents capturing an entire wrong session.

Other ways to run it:

```bash
python3 .claude/skills/sync/extract-session.py                       # print the current session to the screen
python3 .claude/skills/sync/extract-session.py SESSION_ID file.md    # a specific session into a file
python3 .claude/skills/sync/extract-session.py /path/to/file.jsonl   # a specific transcript, printed
```

If you print to the screen and copy it in by hand: **replace** the LOG, never paste below it. And don't pipe the output through `| head` or anything else that can stop early; the capture gets cut off mid-message and still looks complete.

**Key discovery**: Session files survive context compaction. Even when AI hits 0% context and resets, the session file keeps the full history. Verbatim capture is guaranteed.

### Path B — Claude.ai chat / other tools

No script needed. The human does the capture (you might need to nudge them). The AI formats for readability.

1. **Copy** the conversation thread (select all, copy)
2. **Create** a session file using the template above
3. **Paste** the conversation under `## LOG` (on a later run, replace what's there; don't paste below it)
4. **Format for readability**: Human words in blockquotes (`>`), AI responses in plain text

That's it. The format matches what the extraction script produces (same archive, different source).

---

## What makes /sync different from /wrap

| Skill | Scope | Purpose |
|---|---|---|
| `/wrap` | Full session close | Route + task docs + handoff + capture. Whole ritual. |
| `/sync` | LOG refresh only | Pure, lightweight, idempotent. Run any time. |

`/wrap` is ceremonial. `/sync` is ambient.

`/sync` runs as the last step of `/wrap`, but it also stands alone. If your session continues past `/wrap` and you want the archive current, run `/sync` again. Idempotent.

---

## Skill Check (after every sync)

Quick scan: anything about this capture that felt off or could be smoother?

- Did texture get lost?
- Was the process frictionless or annoying?
- Did compression sneak in anywhere?
- Was the session file structure clear?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every capture teaches something.
