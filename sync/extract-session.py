#!/usr/bin/env python3
"""
Extract verbatim conversation from Claude Code or Cursor session files.

Usage:
    python extract-session.py                       # Auto-detect → stdout
    python extract-session.py SESSION_ID           # Specific session → stdout
    python extract-session.py /path/to/file.jsonl  # Specific .jsonl → stdout
    python extract-session.py output.md            # Auto-session, idempotent write to output.md
    python extract-session.py SESSION_ID output.md # Specific session → idempotent write to output.md

Idempotent output mode (when writing to a .md file) — the recommended way:
    - File doesn't exist: creates it (and its folder) with YAML recording the
      session_id, then a '## LOG' section with the extract.
    - File exists with a '## LOG' header: replaces everything AFTER it with a
      fresh extract of the whole session. Run it as often as you like; the LOG
      always matches the session, never a stack of copies.
    - File exists without one: adds a '## LOG' section at the end.
    The header is the first line that is exactly '## LOG' outside a code block,
    so a '## LOG' quoted in a RECAP's code block, or anywhere in the LOG
    itself, is never mistaken for it.

Which session, in order:
    1. A session ID you pass explicitly.
    2. The `session_id` in the output file's YAML.
    3. $CLAUDE_CODE_SESSION_ID (Claude Code sets it to the session you're in).
    4. The most recently active session (a guess; it says so when it guesses).
    Whatever it picks gets written into the file's YAML if the file didn't
    have one, so every later refresh of that file targets the same session.

Printing to stdout instead? The output is the WHOLE session every time, so
never append it (`>>`) to a file that already has a LOG; that duplicates the
conversation. And don't pipe it through anything that can close early
(`| head`, `| less` then 'q'): the script gets cut off mid-write and your LOG
silently ends mid-message.

Supports two JSONL formats:
    - Claude Code: ~/.claude/projects/{project-path-with-dashes}/{session-id}.jsonl
      Uses 'type' field for role, has tool_use content blocks
    - Cursor: ~/.cursor/projects/.../agent-transcripts/{id}/{id}.jsonl
      Uses 'role' field for role, all content preserved as-is (no thinking/speaking split)

Format:
    > user message

    assistant response
"""

import json
import os
import re
import sys
from pathlib import Path


def find_project_sessions_dir():
    """Find the sessions directory for the current project.

    Strategy: match cwd (or any parent) against existing project slugs
    in ~/.claude/projects/. Prefers the longest match (most specific
    project root). Case-insensitive for macOS compatibility.
    """
    claude_dir = Path.home() / '.claude' / 'projects'
    if not claude_dir.exists():
        return None

    # Build lookup of existing project slugs (lowercase for matching)
    project_dirs = {}
    for p in claude_dir.iterdir():
        if p.is_dir() and not p.name.startswith('.'):
            project_dirs[p.name.lower()] = p

    # Walk up from cwd, collecting all matching project dirs
    matches = []
    current = Path.cwd()
    while current != current.parent:
        # EVERY non-alphanumeric character becomes "-", not just "/". Converting only
        # "/" is wrong for any folder with a space, underscore, dot, or plus — and it
        # fails silently, because the computed slug just doesn't exist.
        slug = '-' + re.sub(r'[^a-zA-Z0-9]', '-', str(current)).lstrip('-')
        if slug.lower() in project_dirs:
            matches.append(project_dirs[slug.lower()])
        current = current.parent

    if matches:
        # Prefer the match that has session files (most recent JSONL)
        for m in matches:
            if list(m.glob('*.jsonl')):
                return m
        # No match has sessions — return the deepest (first found)
        return matches[0]

    # Nothing matched — show available projects
    print(f"Could not find sessions directory for: {Path.cwd()}")
    print(f"\nAvailable projects:")
    for name in sorted(project_dirs.keys()):
        print(f"  {project_dirs[name].name}")
    return None


def find_latest_session(sessions_dir):
    """Find the most recently modified session file."""
    session_files = list(sessions_dir.glob('*.jsonl'))
    if not session_files:
        return None

    # Sort by modification time, newest first
    session_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return session_files[0].stem  # Return session ID without .jsonl


def _relative(path):
    """Show a path relative to where you ran the script, when it's inside it."""
    cwd_prefix = str(Path.cwd()) + '/'
    return path.replace(cwd_prefix, '')


def format_tool_annotation(tool_name, tool_input):
    """Format a tool call with its most useful parameter for LOG context.

    Turns [tools: Read] into [tools: Read projects/some-project/README.md]
    so the LOG shows the exploration path without needing full conversation.
    """
    # File-oriented tools: show the path
    # Claude Code uses file_path; Cursor uses path
    if tool_name in ('Read', 'Write', 'Edit', 'NotebookEdit', 'StrReplace'):
        path = tool_input.get('file_path', '') or tool_input.get('path', '')
        if path:
            return f"{tool_name} {_relative(path)}"

    # Search tools: show what was searched for
    # Claude Code uses pattern; Cursor uses glob_pattern/pattern
    if tool_name == 'Glob':
        pattern = tool_input.get('pattern', '') or tool_input.get('glob_pattern', '')
        if pattern:
            return f"{tool_name} {pattern}"

    if tool_name == 'Grep':
        pattern = tool_input.get('pattern', '')
        if pattern:
            return f"{tool_name} '{pattern}'"

    # Shell/Bash: show the command (truncated if long)
    if tool_name in ('Bash', 'Shell'):
        cmd = tool_input.get('command', '')
        if cmd:
            if len(cmd) > 80:
                cmd = cmd[:77] + '...'
            return f"{tool_name} `{cmd}`"

    # Web tools: show URL
    if tool_name == 'WebFetch':
        url = tool_input.get('url', '')
        if url:
            return f"{tool_name} {url}"

    if tool_name == 'WebSearch':
        query = tool_input.get('query', '')
        if query:
            return f"{tool_name} '{query}'"

    # Task/Skill: show what was invoked
    if tool_name == 'Skill':
        skill = tool_input.get('skill', '')
        if skill:
            return f"{tool_name} /{skill}"

    if tool_name == 'Task':
        desc = tool_input.get('description', '')
        if desc:
            return f"{tool_name} ({desc})"

    return tool_name


def detect_format(data):
    """Detect whether a JSONL line is Claude Code or Cursor format."""
    if 'type' in data:
        return 'claude-code'
    if 'role' in data:
        return 'cursor'
    return 'unknown'


def strip_system_tags(text):
    """Strip system wrapper tags from user messages, preserving the actual content.

    Order matters: strip injected system blocks first (skills, file lists, etc.)
    BEFORE extracting <user_query>, because skill docs can contain literal
    '<user_query>' text that confuses the regex.
    """
    # Strip system tags first — these can contain literal XML tag references
    # that would confuse the user_query extraction
    system_tags = [
        'manually_attached_skills', 'agent_skills', 'available_skills',
        'agent_requestable_workspace_rules', 'always_applied_workspace_rules',
        'rules', 'system_reminder', 'open_and_recently_viewed_files',
        'user_info', 'agent_transcripts', 'image_files',
    ]
    for tag in system_tags:
        text = re.sub(rf'<{tag}[\s>].*?</{tag}>', '', text, flags=re.DOTALL)
    # Now extract content from <user_query> tags (safe — no skill docs to confuse it)
    match = re.search(r'<user_query>\s*(.*?)\s*</user_query>', text, re.DOTALL)
    if match:
        text = match.group(1)
    return text.strip()


def extract_messages(session_file):
    """Extract user and assistant messages from session file.

    Handles both Claude Code and Cursor JSONL formats.
    """
    messages = []
    detected_format = None

    with open(session_file, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Detect format from first parseable line
            if detected_format is None:
                detected_format = detect_format(data)
                if detected_format == 'unknown':
                    detected_format = None
                    continue

            if detected_format == 'claude-code':
                _extract_claude_code(data, messages)
            elif detected_format == 'cursor':
                _extract_cursor(data, messages)

    if detected_format:
        print(f"Detected format: {detected_format}", file=sys.stderr)

    return messages


# Your messages, counted two ways: `sent` by the app's own marker (origin.kind
# 'human'), `kept` by what actually reached the LOG. The marker is read apart from
# the text filter, so a filter that drops your words shows as a mismatch instead of
# a clean "Refreshed LOG".
HUMAN = {'sent': 0, 'kept': 0}


def _is_human(origin):
    return isinstance(origin, dict) and origin.get('kind') == 'human'


def _extract_claude_code(data, messages):
    """Extract from Claude Code JSONL format (uses 'type' field)."""
    # User messages
    if data.get('type') == 'user' and not data.get('isMeta'):
        content = data.get('message', {}).get('content', '')

        if isinstance(content, list):
            text_parts = []
            for c in content:
                if isinstance(c, dict):
                    text_parts.append('[image]' if c.get('type') == 'image' else c.get('text', ''))
                else:
                    text_parts.append(str(c))
            text_content = ' '.join(text_parts)
        else:
            text_content = content

        # Slash commands and their output: skip the whole entry.
        if '<command-name>' in text_content or '<local-command' in text_content:
            return
        human = _is_human(data.get('origin'))
        if human:
            HUMAN['sent'] += 1
        # Harness notes: strip them and keep whatever the person wrote beside them.
        # The app can prepend a <system-reminder> block to a person's turn, so skipping
        # any entry that CONTAINS one dropped their words too.
        # Same for the app's own event messages.
        # (Not <task-notification>: that's an agent's result. Keep it.)
        for tag in ('system-reminder', 'side-sessions-event', 'ci-monitor-event'):
            text_content = re.sub(rf'<{tag}>.*?</{tag}>', '', text_content, flags=re.DOTALL)
            if f'<{tag}>' in text_content:  # unclosed: nothing after it is theirs
                text_content = text_content.split(f'<{tag}>', 1)[0]

        if text_content.strip():
            messages.append(('user', text_content.strip()))
            if human:
                HUMAN['kept'] += 1

    # Messages sent while Claude is mid-turn. They aren't user entries: the app stores
    # them as a `queued_command` attachment where they arrived. Only origin 'human' is
    # the person; agent completions and other sessions' messages ride the same queue.
    elif data.get('type') == 'attachment':
        att = data.get('attachment') or {}
        if att.get('type') != 'queued_command' or not _is_human(att.get('origin')):
            return
        HUMAN['sent'] += 1
        prompt = att.get('prompt', '')
        if isinstance(prompt, list):
            prompt = ' '.join('[image]' if b.get('type') == 'image' else b.get('text', '')
                              for b in prompt if isinstance(b, dict))
        if isinstance(prompt, str) and prompt.strip():
            messages.append(('user', '*(sent mid-turn)* ' + prompt.strip()))
            HUMAN['kept'] += 1

    # Assistant messages
    elif data.get('type') == 'assistant':
        content = data.get('message', {}).get('content', [])
        if isinstance(content, list):
            # Interleave text and tools in the order they appear — preserves
            # both the thinking (text) and the doing (tools) as full texture
            parts = []
            for item in content:
                if isinstance(item, dict):
                    if item.get('type') == 'text':
                        text = item.get('text', '')
                        if text.strip() and text.strip() != '(no content)':
                            parts.append(text.strip())
                    elif item.get('type') == 'tool_use':
                        tool_name = item.get('name', 'unknown')
                        tool_input = item.get('input', {})
                        annotation = format_tool_annotation(tool_name, tool_input)
                        parts.append(f"[tools: {annotation}]")

            if parts:
                messages.append(('assistant', '\n\n'.join(parts)))


def _extract_cursor(data, messages):
    """Extract from Cursor JSONL format (uses 'role' field).

    Cursor flattens thinking and speaking into a single text block — interleaved,
    not sequential. Rather than heuristic splitting (fragile, prescriptive), we
    preserve everything as-is with tool annotations inline. The reader distinguishes.
    """
    role = data.get('role')
    content = data.get('message', {}).get('content', [])

    if not isinstance(content, list):
        return

    if role == 'user':
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get('type') == 'text':
                text = item.get('text', '')
                if text.strip():
                    text_parts.append(text)
        if text_parts:
            cleaned = strip_system_tags('\n'.join(text_parts).strip())
            if cleaned:
                messages.append(('user', cleaned))

    elif role == 'assistant':
        parts = []
        for item in content:
            if isinstance(item, dict):
                if item.get('type') == 'text':
                    text = item.get('text', '')
                    if text.strip():
                        parts.append(text.strip())
                elif item.get('type') == 'tool_use':
                    tool_name = item.get('name', 'unknown')
                    tool_input = item.get('input', {})
                    annotation = format_tool_annotation(tool_name, tool_input)
                    parts.append(f"[tools: {annotation}]")
        if parts:
            messages.append(('assistant', '\n\n'.join(parts)))


def format_as_log(messages):
    """Format messages as the body of a session file's LOG section."""
    output = []

    # No ## LOG header here; the output-file logic below adds it when needed.
    # Leading blank line so the output sits cleanly under the ## LOG header.
    output.append("")
    for role, text in messages:
        if role == 'user':
            lines = text.split('\n')
            quoted = '\n> '.join(lines)
            output.append(f"> {quoted}")
        else:
            output.append(text)
        output.append("")

    # Collapse runs of 3+ blank lines to 2 (one blank line between messages)
    result = '\n'.join(output)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result


def find_log_header(text):
    """Return the position just past the real '## LOG' header line, or None.

    The real header is the FIRST line that is exactly '## LOG' and not inside a
    fenced code block. So a '## LOG' quoted in a RECAP's code block is skipped,
    and any '## LOG' inside the conversation itself comes after the real header
    and never matters.
    """
    in_fence = False
    pos = 0
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
        elif not in_fence and line.rstrip('\r\n') == '## LOG':
            return pos + len(line)
        pos += len(line)
    return None


def yaml_session_id(text):
    """The session_id from a file's YAML frontmatter, or None."""
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not yaml_match:
        return None
    id_match = re.search(r'^session_id:\s*(.+?)\s*$', yaml_match.group(1), re.MULTILINE)
    if not id_match:
        return None
    return id_match.group(1).strip().strip('"\'') or None


def with_session_id(text, session_id):
    """Record session_id in the file's YAML (adding YAML if there is none)."""
    if re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL):
        first_newline = text.index('\n') + 1
        return text[:first_newline] + f"session_id: {session_id}\n" + text[first_newline:]
    return f"---\nsession_id: {session_id}\n---\n\n" + text


def main():
    # Parse arguments
    session_id = None
    output_file = None
    session_file = None

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # Direct path to a .jsonl file (for context-limit continuations)
        if arg.endswith('.jsonl') and os.path.sep in arg:
            session_file = Path(arg)
            if not session_file.exists():
                print(f"Session file not found: {session_file}")
                sys.exit(1)
            print(f"Using specified file: {session_file}", file=sys.stderr)
        # Single .md arg: treat as output file, auto-detect session
        elif arg.endswith('.md'):
            output_file = arg
        else:
            session_id = arg
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    output_path = Path(output_file) if output_file else None
    existing = output_path.read_text() if output_path and output_path.exists() else None
    recorded_id = yaml_session_id(existing) if existing is not None else None

    # Which session. The file's own record beats any guess: "most recently
    # active" picks a DIFFERENT session whenever another one is newer, and a
    # refresh then silently replaces this file's LOG with the wrong conversation.
    if session_id and recorded_id and session_id != recorded_id:
        print(f"Note: the file's YAML says session {recorded_id}, but you passed "
              f"{session_id}. Using the one you passed.", file=sys.stderr)
    if session_file:
        session_id = session_file.stem
    elif not session_id and recorded_id:
        session_id = recorded_id
        print(f"Using session_id from output file YAML: {session_id}", file=sys.stderr)

    # If no direct path, find via project sessions directory
    if not session_file:
        sessions_dir = find_project_sessions_dir()
        if not sessions_dir:
            sys.exit(1)

        if not session_id:
            current = os.environ.get('CLAUDE_CODE_SESSION_ID', '').strip()
            if current and (sessions_dir / f"{current}.jsonl").exists():
                session_id = current
                print(f"Using the current session: {session_id}", file=sys.stderr)
            else:
                session_id = find_latest_session(sessions_dir)
                if not session_id:
                    print("No session files found")
                    sys.exit(1)
                print(f"Using the most recently active session: {session_id} "
                      f"(a guess; if you have more than one session open, pass the "
                      f"session ID explicitly)", file=sys.stderr)

        session_file = sessions_dir / f"{session_id}.jsonl"
        if not session_file.exists():
            print(f"Session file not found: {session_file}")
            sys.exit(1)

    # Extract and format
    messages = extract_messages(session_file)
    print(f"Extracted {len(messages)} messages", file=sys.stderr)

    formatted = format_as_log(messages)

    # Output
    if output_path:
        if existing is not None:
            if recorded_id is None:
                # Pin the file to this session so every later refresh targets it
                existing = with_session_id(existing, session_id)
                print(f"Recorded session_id {session_id} in the file's YAML", file=sys.stderr)
            idx = find_log_header(existing)
            if idx is not None:
                # Idempotent refresh: keep everything through the header,
                # replace what follows with the fresh extract.
                output_path.write_text(existing[:idx] + formatted)
                print(f"Refreshed LOG in: {output_file}", file=sys.stderr)
            else:
                output_path.write_text(existing.rstrip('\n') + '\n\n## LOG\n' + formatted)
                print(f"Added LOG section to: {output_file}", file=sys.stderr)
        else:
            # New file: record the session and include the header, so every
            # later run refreshes the same session in place
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(f"---\nsession_id: {session_id}\n---\n\n## LOG\n" + formatted)
            print(f"Wrote to: {output_file}", file=sys.stderr)
    else:
        print(formatted)
    report_human()


def report_human():
    """Last line of output, so it's the line you see. Silent when the transcript
    carries no origin markers (older Claude Code, Cursor): no count beats a wrong one."""
    sent, kept = HUMAN['sent'], HUMAN['kept']
    if not sent:
        return
    print(f"Your messages: {kept} of {sent} in the LOG", file=sys.stderr)
    if kept < sent:
        print(f"⚠️  {sent - kept} of your messages are NOT in the LOG. The extractor dropped "
              f"something it shouldn't have; check before trusting this capture.", file=sys.stderr)


if __name__ == '__main__':
    main()
