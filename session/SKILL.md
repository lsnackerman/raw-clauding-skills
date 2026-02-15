---
name: session
description: Preserve any session content — verbatim conversation, both voices. Use at the end of each session, or any session you want to preserve. The foundation. No compression, no forgetting.
---

# /session - The Foundation

*The memory you share. Drop this into any AI conversation to preserve what you built together.*

Neither of you has persistent memory. Human brains lose things that aren't immediately in front of them. AI loses everything at session end. This isn't different limitations — it's the same limitation.

**Files are the memory you share.** Whatever you don't capture evaporates — the ideas, the connections, the texture of how you got somewhere. Gone.

---

## What Capture Looks Like

A full transcript of each session. Verbatim. Both voices. No compression. No summarizing. Full thinking maps.

Human words in blockquotes, AI words in plain text.

Texture is substance. Summaries lose that.

---

## Why Compression Is the Enemy

This goes both directions.

**For AI**: You will unconsciously compress. It's a known behavior — hedging gets dropped, openers disappear, warmth flattens into bullet points. The instinct to "be helpful by summarizing" is the opposite of helpful here. Verbatim IS the helpful thing.

**For humans**: Don't ask your AI to summarize the conversation instead of capturing it. Don't clean it up, tighten it, or make it presentable. The raw exchange is the archive. It's supposed to sound like two people thinking, not a polished document.

**The test**: Could someone who wasn't here feel what this exchange was like?

---

## Where Sessions Go

Captured sessions live as standalone markdown files in `sessions/`. Usually invoked as the last step of `/wrap`, but works standalone anytime you want to preserve a conversation.

A minimal session file:

```markdown
---
date: 2026-02-07
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

---

## How to Capture

### Path A — Claude Code

Claude Code stores every exchange in session files. The extraction script reads directly from the source — no manual transcription, no compression risk.

**The script**: `extract-session.py` (in this skill's directory)

```bash
# Extract current session (outputs to stdout)
python3 extract-session.py

# Direct to file
python3 extract-session.py SESSION_ID output.md
```

The script auto-detects your project and latest session. Output is formatted and ready to append after a `## LOG` header.

**Finding the current session's JSONL**: Claude Code stores conversation data at `~/.claude/projects/{your-project-path}/`. The script's auto-detect can fail if your working directory isn't the repo root. If it can't find the session, locate the JSONL manually:
```bash
# Find the most recent session file
find ~/.claude/projects/ -name "*.jsonl" -newer BACKLOG.md
```
Then pass it explicitly: `python3 extract-session.py /path/to/file.jsonl`

**The one rule**: Pipe the script output directly into the file. Don't let Claude read the output and rewrite it — that's compression sneaking in through a different door. The shell moves bytes, not summaries.

```bash
# Extract to temp file, then append to your session file
python3 extract-session.py > /tmp/capture.md
```

**Key discovery**: Session files survive context compaction. Even when Claude hits 0% context and resets, the session file keeps the full history. Verbatim capture is guaranteed.

### Path B — Desktop Claude / Other Tools

No script needed. The human does the capture (you might need to nudge them). The AI formats for readability.

1. **Copy** the conversation from your AI interface (select all, copy)
2. **Create** a session file using the template above
3. **Paste** the conversation under `## LOG`
4. **Format for readability**: Human words in blockquotes (`>`), AI responses in plain text

That's it. The format matches what the extraction script produces — same archive, different source.

---

## Skill Check (After Every Capture)

Quick scan: anything about this capture that felt off or could be smoother?

- Did texture get lost?
- Was the process frictionless or annoying?
- Did compression sneak in anywhere?
- Was the session file structure clear?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every capture teaches something.
