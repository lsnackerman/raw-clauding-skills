#!/usr/bin/env python3
"""
Extract verbatim conversation from Claude Code session files.

Usage:
    python extract-session.py                     # Auto-detect current session
    python extract-session.py SESSION_ID         # Specific session by ID
    python extract-session.py /path/to/file.jsonl # Specific session by path
    python extract-session.py SESSION_ID output.md  # Write to file

The session files live at:
    ~/.claude/projects/{project-path-with-dashes}/{session-id}.jsonl

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
    """Find the sessions directory for the current project."""
    claude_dir = Path.home() / '.claude' / 'projects'

    # Get current working directory and convert to Claude's path format
    cwd = Path.cwd()
    project_path = str(cwd).replace('/', '-')
    if project_path.startswith('-'):
        project_path = project_path[1:]  # Remove leading dash

    sessions_dir = claude_dir / f"-{project_path}"

    if sessions_dir.exists():
        return sessions_dir

    # Try without leading dash
    sessions_dir = claude_dir / project_path
    if sessions_dir.exists():
        return sessions_dir

    # List available and let user know
    print(f"Could not find sessions directory for: {cwd}")
    print(f"Tried: {claude_dir / f'-{project_path}'}")
    if claude_dir.exists():
        print(f"\nAvailable projects:")
        for p in claude_dir.iterdir():
            if p.is_dir() and not p.name.startswith('.'):
                print(f"  {p.name}")
    return None


def find_latest_session(sessions_dir):
    """Find the most recently modified session file."""
    session_files = list(sessions_dir.glob('*.jsonl'))
    if not session_files:
        return None

    # Sort by modification time, newest first
    session_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return session_files[0].stem  # Return session ID without .jsonl


def format_tool_annotation(tool_name, tool_input):
    """Format a tool call with its most useful parameter for LOG context.

    Turns [tools: Read] into [tools: Read lab/share/README.md]
    so the LOG shows the exploration path without needing full conversation.
    """
    # Strip project root to keep paths readable
    cwd_prefix = str(Path.cwd()) + '/'

    # File-oriented tools: show the path
    if tool_name in ('Read', 'Write', 'Edit', 'NotebookEdit'):
        path = tool_input.get('file_path', '')
        if path:
            path = path.replace(cwd_prefix, '')
            return f"{tool_name} {path}"

    # Search tools: show what was searched for
    if tool_name == 'Glob':
        pattern = tool_input.get('pattern', '')
        if pattern:
            return f"{tool_name} {pattern}"

    if tool_name == 'Grep':
        pattern = tool_input.get('pattern', '')
        if pattern:
            return f"{tool_name} '{pattern}'"

    # Bash: show the command (truncated if long)
    if tool_name == 'Bash':
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


def extract_messages(session_file):
    """Extract user and assistant messages from session file."""
    messages = []

    with open(session_file, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            # User messages
            if data.get('type') == 'user' and not data.get('isMeta'):
                content = data.get('message', {}).get('content', '')

                # Handle if content is a list
                if isinstance(content, list):
                    text_parts = []
                    for c in content:
                        if isinstance(c, dict):
                            text_parts.append(c.get('text', ''))
                        else:
                            text_parts.append(str(c))
                    text_content = ' '.join(text_parts)
                else:
                    text_content = content

                # Skip system/command messages
                skip_markers = ['<command-name>', '<local-command', '<system-reminder>']
                if any(marker in text_content for marker in skip_markers):
                    continue

                if text_content.strip():
                    messages.append(('user', text_content.strip()))

            # Assistant messages
            elif data.get('type') == 'assistant':
                content = data.get('message', {}).get('content', [])
                if isinstance(content, list):
                    text_parts = []
                    tool_names = []
                    for item in content:
                        if isinstance(item, dict):
                            if item.get('type') == 'text':
                                text = item.get('text', '')
                                # Skip literal "(no content)" placeholders
                                if text.strip() and text.strip() != '(no content)':
                                    text_parts.append(text)
                            elif item.get('type') == 'tool_use':
                                tool_name = item.get('name', 'unknown')
                                tool_input = item.get('input', {})
                                annotation = format_tool_annotation(tool_name, tool_input)
                                tool_names.append(annotation)

                    if text_parts:
                        messages.append(('assistant', '\n'.join(text_parts).strip()))
                    elif tool_names:
                        # Show tool names when there's no text (thinking-via-doing)
                        messages.append(('assistant', '\n'.join(f"[tools: {t}]" for t in tool_names)))

    return messages


def format_as_log(messages, session_id=None):
    """Format messages as session file LOG section."""
    output = []

    # No ## LOG header — session shell provides structure, script provides content
    # Leading blank line so appending via >> doesn't butt against previous content
    output.append("")

    for role, text in messages:
        if role == 'user':
            # Handle multi-line user messages
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
        else:
            session_id = arg
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    # If no direct path, find via project sessions directory
    if not session_file:
        sessions_dir = find_project_sessions_dir()
        if not sessions_dir:
            sys.exit(1)

        if not session_id:
            session_id = find_latest_session(sessions_dir)
            if not session_id:
                print("No session files found")
                sys.exit(1)
            print(f"Using latest session: {session_id}", file=sys.stderr)

        session_file = sessions_dir / f"{session_id}.jsonl"
        if not session_file.exists():
            print(f"Session file not found: {session_file}")
            sys.exit(1)

    # Extract and format
    messages = extract_messages(session_file)
    print(f"Extracted {len(messages)} messages", file=sys.stderr)

    formatted = format_as_log(messages, session_id)

    # Output
    if output_file:
        with open(output_file, 'w') as f:
            f.write(formatted)
        print(f"Wrote to: {output_file}", file=sys.stderr)
    else:
        print(formatted)


if __name__ == '__main__':
    main()
