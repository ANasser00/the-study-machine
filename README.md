# The Study Machine

A pure markdown study system built on the two most evidence-backed learning techniques: **active recall** and **spaced repetition**.

No apps, no subscriptions, no setup. Just files, a text editor, and Claude.

---

## Why This Works

Passive re-reading feels productive but produces weak long-term retention. The research is clear:

- **Active recall** — forcing yourself to retrieve information from memory — strengthens the neural pathways that encode that knowledge. Testing yourself is more effective than re-reading by a significant margin.
- **Spaced repetition** — reviewing material at increasing intervals — exploits the "spacing effect": memories consolidate more efficiently when recall is spaced out over time rather than crammed in one session.

This system combines both. Every study session produces a set of questions you test yourself on. The review schedule tells you exactly when to revisit each topic.

---

## Folder Structure

```
the-study-machine/
├── content/                          Source material lives here
│   └── <subject>/
│       ├── notes/                    Your own written notes
│       ├── pdfs/                     Past exam papers, readings
│       ├── slides/                   Lecture slide exports
│       └── transcripts/              Lecture transcripts or recordings
│
├── sessions/                         One file per study session
│   ├── _template.md                  Copy this to start a new session
│   └── <subject>/
│       └── <topic>.md                Completed session file
│
├── review/
│   └── schedule.md                   Spaced repetition tracker
│
└── exam-prep/
    └── <subject>-master.md           Aggregated Q&A for a full subject
```

---

## How to Start a Session

**Step 1 — Drop your material in.**

Put lecture transcripts, slides, PDFs, or notes into the relevant folder under `content/<subject>/`. You can use any file format; what matters is that you can paste or share the content with Claude.

**Step 2 — Create a session file.**

Copy `sessions/_template.md` to `sessions/<subject>/<topic>.md`. Fill in the header: subject, date, and which source files you are using.

**Step 3 — Phase 1: Understand.**

Open a Claude conversation. Paste this at the start:

> "We are doing Phase 1 of a study session. The topic is [topic]. Here is the source material: [paste content]. Explain this to me interactively. Give me analogies, examples, and exercises. Ask me questions to check my understanding. Keep going until I tell you I am ready for Phase 2."

Work through the material with Claude. When something clicks, add a note to the Phase 1 section of your session file. When something stays confusing, mark it.

**Step 4 — Phase 2: Exam Gold.**

Only start this after Phase 1 is complete. Tell Claude:

> "Phase 1 is done. Now produce Phase 2 Exam Gold for [topic]: 5–10 dense bullet points for last-minute review, active recall questions with difficulty ratings, and a list of weak spots I should revisit sooner."

Paste the output into the Phase 2 sections of your session file.

**Step 5 — Update the review schedule.**

Add each question set to `review/schedule.md`. Set the first review date to tomorrow.

---

## Spaced Repetition Scheduling

The tracker lives in `review/schedule.md`. It is a manually maintained table — update it after each review session.

The default intervals are:

| Difficulty | Review again in |
|------------|-----------------|
| Hard (struggled) | 1 day |
| Medium (got it with effort) | 3 days |
| Easy (instant recall) | Double the current interval |

After each review, update the difficulty, last reviewed date, next review date, and interval. Topics with a current interval above 30 days are well-consolidated — you can de-prioritise them unless an exam is coming.

The "Due Today" section in `schedule.md` is a manually curated list. Each morning, scan the table for rows where "Next Review" is today or earlier and copy them into Due Today.

---

## Exam Prep Master Files

As sessions accumulate, `exam-prep/<subject>-master.md` becomes your single source of truth for exam preparation. It aggregates:

- All active recall questions from every session on that subject, grouped by topic
- The hardest questions (flagged Hard) isolated in their own section
- A pre-exam checklist of topics you should be able to explain from memory

Update the master file after completing each new session. Before an exam, work through the master file top-to-bottom, using the Hard questions section as your final drill.

---

## Session File Format

Each session file (`sessions/<subject>/<topic>.md`) has two main sections:

- **Phase 1 — Understanding**: Notes you take during the interactive explanation. Key analogies, moments of clarity, things that needed re-explaining.
- **Phase 2 — Exam Gold**: The structured output for long-term retention. Key concept bullets, the active recall question table, and weak spots.

See `sessions/_example-subject/_example-topic.md` for a fully completed example.
