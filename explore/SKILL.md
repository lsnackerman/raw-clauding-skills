---
name: explore
description: Build topic reserves by searching your entire system, or run discovery mode (no topic) to find what connects across territories. Use when consolidating scattered knowledge on a topic, before writing/sharing, before a sprint, or when curiosity has no specific target.
argument-hint: [topic, or omit for discovery mode]
---

# /explore - Build topic reserves

Two modes: **topic-specific** (search for everything on a topic) and **discovery** (no topic: find what connects across your whole system with fresh eyes).

Topic mode builds rich reserves with verbatim texture, source references, and connective tissue. Discovery mode surfaces cross-territory connections, unnamed threads, and surprises that topic-specific explores would miss.

---

## Two modes (both work at any stage)

**Topic mode** (with an argument): "explore X." You know what you're looking for. Output is a compounding reserve that grows over time as you keep exploring the same topic.

**Discovery mode** (no argument): "see what's there." You're listening for what wants to surface. Output is a timestamped snapshot of cross-territory connections; a moment-in-time view, not a compounding doc.

These aren't gated by system age. New systems benefit from discovery mode (find unexpected connections in what little exists). Mature systems benefit from topic mode (depth on threads you already know matter). Read what you're asking the system to show you, and pick.

---

## What to do

1. **Determine mode**:
   - Topic specified → **topic mode** (steps below)
   - No topic, or "just explore" / "surprise me" / "general" → **discovery mode** (see the Discovery mode section below: it replaces steps 2-3 with its own orient and search brief, then return here for steps 4 and 6)
   - If unclear, ask: "Topic-specific or discovery mode?"
2. **Orient first** — before searching, read the most likely canonical doc for this topic. This gives you the vocabulary and search terms. Don't search blind.
3. **Search — inline or parallel** (see *Inline vs parallel* below). For parallel: fan out across your whole system at once, not sequentially. Split by location (e.g., `sessions/`, `tasks/`, `projects/`, `library/`) so agents don't overlap.
   - Ask each agent for a thorough search, not a quick skim
   - **Exclude your own reserves from search.** Reserve files are derivatives of source material. Including them creates echo, not signal. Search the sources, not previous searches.
   - **Each agent prompt must include:**
     - **Map the territory before searching it.** Tell the agent: "Before searching content, enumerate the subfolders of your territory and read any orientation file in each (a CLAUDE.md, a README); they're short navigation files telling you what's there. Build the map first, then decide where to search deeply." Architecture is information; an agent that skips this flies blind on structure even with a perfect brief.
     - The search terms from your orient step, plus what to look for beyond keyword matches: decisions made, insights, contrast structures, verbatim exchanges, open questions.
     - This instruction, verbatim: "For EVERY match: include the filename, line numbers, and the FULL surrounding context (5-10 lines). Verbatim quotes — do not summarize or paraphrase. Preserve all texture."
     - **"Return findings organized by theme — do NOT pre-compile a finished reserve."** No Decisions table, no Session Map, no Related section. Those are synthesis steps you do AFTER seeing every agent's returns. Given a rich brief, agents default to producing complete-looking deliverables, which turns your synthesis into "organize their organization" instead of "organize raw findings."
     - **A negative example of what NOT to return** — e.g. "Do NOT return 'RECOMMENDED' tables, 'CANDIDATE' sections, or final proposals. Those are my job after I see all returns." Showing what-not-to-do is stronger than a generic "don't synthesize."
     - **Attribution fidelity — trace who-said-what to the raw source.** When a finding asserts *who* coined, originated, named, or first said something, capture the raw verbatim that settles it (the transcript line, the session quote), and never inherit an attribution from a *derivative* (a task doc, a prior reserve, a note written after the fact). Derivatives drift on attribution: **the person who affirmed an idea gets miscredited as the one who originated it**, and early impressions stick. If the primary source isn't in hand, flag the attribution as *unverified* rather than asserting it. It's the same "search the sources, not previous searches" principle as the reserve-exclusion rule above, applied to who-said-it.
     - **Strip imperative verbs from the topic framing the agent sees.** Your task ("rename the five principles") isn't the agent's task ("gather the language we already use for them"). An imperative in the topic pulls agents toward completing it, even when you've told them not to pre-compile. Reframe as evidence-gathering, not decision-making.
   - **Sub-agents don't read this skill doc** — they only know what you put in the prompt. If you don't explicitly tell them to preserve texture and return raw findings, they'll summarize and compress by default.
4. **Gather everything — preserve, don't compress**:
   - Decisions made and why
   - Insights and patterns
   - Verbatim exchanges (full passages, not summaries)
   - Questions still open
   - Default to too much texture, not too little. The reserve is the raw tank. Synthesis happens when you USE the reserve, not when you build it.
5. **If this is a subsequent run** (reserve already exists for this topic):
   - Read the existing reserve first; you need the Sources list, Session Map, and Related sections
   - Build a "what we already have" briefing: key sources already mined, sessions already mapped, passages already captured
   - Focus on material NOT in the existing reserve. New sessions, new docs, anything added since the last run. If you find something already captured, skip it. If you find something that extends or contradicts what's captured, include it.
6. **Output** — create the `reserves/` folder if it doesn't exist.
   - **Topic mode** → `reserves/{topic}.md`. Create if new; expand if existing (reserves are append-friendly, dedup during synthesis).
   - **Discovery mode** → `reserves/discovery-{date}.md`, a fresh file every time (see Discovery Mode below).

---

## Inline vs parallel search (read your signal)

**Inline** (you do the searching): grep, glob, read files yourself. Fast, low overhead, your context window holds the texture as you go.

**Parallel** (fan out sub-agents): split the system into territories, send a sub-agent to each, assemble the returns.

The choice is about scope:
- **Inline fits** when you can hold the search in one head: 3-5 file reads, narrow topic, fast iteration matters
- **Parallel fits** when the search would saturate your context: many territories to scan, broad topic, you want results without losing the rest of your working memory

If you're not sure, start inline. Switch to parallel when you notice you're losing track of what you've already found. (No sub-agents in your tool? Inline is the whole skill, and it works.)

---

## What to gather

- **Decisions** made about this topic
- **Insights** that emerged
- **Patterns** noticed over time
- **Verbatim texture** — your words, the AI's reframes, the back-and-forth that shows how thinking happened
- **Genesis** — what triggered the exploration?
- **Contrast structures** — "the default approach does X, we do Y"
- **Source references** — which doc, which session, which date

---

## Output format

```markdown
# [Topic] — Exploring Reserves

**Last updated**: YYYY-MM-DD
**Sources**: [list of docs mined]

---

## The Question
What are we exploring and why?

## Key Insights

## [Topic-specific sections with verbatim texture]
Organize by whatever structure fits the topic. Full passages with
file paths. This is the bulk of the reserve.

## Decisions Made
| Decision | Why | Source |
|---|---|---|

## Contrast Structures
| Default approach | What we do | Why |

## Session Map
| Session | What's there | Density |
Which sessions have the richest material on this topic?

## Open Questions

## Related
Group by layer: primary sources, downstream connections,
connected reserves. This is what makes reserves navigable
as a system.
```

---

## Discovery mode

When no topic is specified, /explore becomes a curiosity-driven scan across your whole system. The question shifts from "find everything about X" to "find what connects, surprises, and resonates across territories."

### How discovery mode differs

**Orient**: Read your handoff files (ALIVE.md or equivalent) to know what's *known*, so you can find what *isn't*. The goal is to surface the unnamed, not inventory the familiar.

**Search brief**: Fundamentally different from topic mode. Instead of "search for X," each search gets:
- "Look at this territory with fresh eyes. Don't inventory what exists; find what connects."
- What to look for: recurring themes, concepts that echo across territories, threads that started and never got followed up, surprises that don't fit the expected pattern, evolution over time
- Same texture instruction: verbatim quotes, full surrounding context, no summarizing
- What NOT to do: "Don't describe the folder structure. Don't list what's there. Find what's alive, what's pulling, what's connecting in ways nobody's named yet."

**After searching**: The synthesis step is different. Topic mode organizes findings into a reserve format. Discovery mode looks for **cross-territory connections**: the same idea showing up in different places, a pattern in tasks that mirrors a principle in your rules, a thread in sessions that connects to something in your library nobody linked. The value is in what spans territories, not what lives within them.

**Output**: Timestamped file, `reserves/discovery-{date}.md`. Discovery doesn't append to itself. Each general explore is a fresh-eyes snapshot of what's connecting at that point in time. Topic reserves compound; discovery reserves are each their own vantage point.

### Discovery output format

```markdown
# Discovery Explore — YYYY-MM-DD

**Snapshot of what's connecting across the system.**

---

## Cross-Territory Connections
The through-lines that live BETWEEN territories: the same question
wearing different clothes across different parts of the system.
This is the section that justifies discovery mode.

## What's Pulling
What feels alive? What threads are pulling from multiple directions?
What wants to be named?

## Surprises
What doesn't fit the pattern? What showed up where you didn't expect?
What contradicts the known narrative?

## Unnamed Threads
Things the system is doing or thinking about that don't have a name yet.

## Territory Snapshots
Brief per-territory observations (NOT inventories; the interesting
texture from each search). Preserve verbatim quotes that carry weight.

## Open Questions
What this explore surfaced that's worth sitting with.
```

---

## Difference from /pulse

| Skill | Scope | Purpose |
|-------|-------|---------|
| `/explore [topic]` | Whole system | Build or expand a topic reserve |
| `/explore` (discovery) | Whole system | Find cross-territory connections, unnamed threads |
| `/pulse` | Whole system | Diagnostic — what needs attention, what's alive |

`/explore [topic]` builds a reserve. `/explore` (discovery) finds what connects. `/pulse` diagnoses.

Discovery mode and `/pulse` look similar but serve different purposes: pulse asks "what needs attention?" Discovery asks "what's connecting that nobody's named?"

---

## Philosophy

**Fill the tank before you drive.** Your system often has what you need already, scattered across files.

**Reserves compound.** Each exploration adds to what's there. The second pass on a topic is always richer than the first. When new material lands mid-session (a decision, a pattern, a reframe that touches a topic you've already explored) add it back to the reserve.

**Depth over synthesis.** The reserve is the raw tank: full passages, surrounding context. Compressing findings into tidy summaries defeats the purpose. Synthesis happens when you use the reserve, not when you build it.

**Texture matters.** Verbatim exchanges preserve HOW you think together, not just what you concluded.

**Discovery finds what topics can't.** Connections live between territories, not within them. A topic-specific explore finds everything about X. A discovery explore finds what X, Y, and Z have in common that nobody named yet.

---

*Writing the brief: `explorer-brief-example.md` (beside this file) is one worked brief with annotations on why each part is there.*

## Skill Check (after every explore)

Quick scan: anything about this exploration that felt off or could be smoother?

- Did the search strategy find what mattered, or miss obvious locations?
- Was the output format useful or too dense?
- Did the exploration surface things you didn't know you had?
- Was it clear when to stop exploring vs keep digging?
- Did the mode (topic vs discovery) and search style (inline vs parallel) fit what you were actually doing?
- **What about the *briefing* would you do differently?** What did the agents need and not get, and what did you tell them that turned out wrong? This is the question that compounds fastest: the brief determines the returns, and every fan-out teaches you something about writing the next one.

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every exploration teaches something.

*When briefing notes outgrow this file (long enough that re-reading the procedure means scrolling past them), split them into an `explorer.md` beside this one and point at it from here. Don't create it empty; let it exist once there's something to put in it.*
