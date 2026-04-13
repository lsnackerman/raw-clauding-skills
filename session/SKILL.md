---
name: session
description: "Saves the full verbatim transcript of a conversation to a markdown file in sessions/, preserving both user and AI messages with timestamps and metadata. Use when the user asks to save, export, log, or archive a conversation, chat history, or session transcript."
---

# /session - Capture Session Verbatim

Capture verbatim. No summarizing, no compression, no reformatting. Human words in blockquotes, AI words in plain text.

---

## Where Sessions Go

Sessions live as standalone markdown files in `sessions/`. Usually invoked as the last step of `/wrap`, but works standalone anytime.

Session file template:

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

The extraction script reads directly from Claude Code session files — no manual transcription.

**The script**: `extract-session.py` (in this skill's directory)

```bash
# Extract current session (outputs to stdout)
python3 extract-session.py

# Direct to file with specific session
python3 extract-session.py SESSION_ID output.md
```

The script auto-detects the project and latest session. If auto-detect fails (working directory isn't repo root), locate the JSONL manually:

```bash
find ~/.claude/projects/ -name "*.jsonl" -newer BACKLOG.md
python3 extract-session.py /path/to/file.jsonl
```

**Critical:** Pipe script output directly into the file. Do not read the output and rewrite it — that introduces compression.

```bash
python3 extract-session.py > /tmp/capture.md
```

### Path B — Desktop Claude / Other Tools

1. **Copy** the conversation from the AI interface
2. **Create** a session file using the template above
3. **Paste** under `## LOG`
4. **Format**: Human words in blockquotes (`>`), AI responses in plain text

---

## Validation

After capture, verify:
- Output file contains both `>` blockquoted human text and plain AI responses
- No summarization or compression crept in
- Session file structure matches the template above

---

## Skill Check

- Did texture get lost?
- Was the process frictionless?
- Did compression sneak in anywhere?

**If yes** → update this skill now. **If no** → move on.
