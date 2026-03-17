# The Study Machine — Claude Context

This repo is a markdown-based study system built on two evidence-backed techniques: **active recall** and **spaced repetition**. The goal is to deeply understand and retain material from university courses well enough to perform under exam conditions — not just recognize it, but retrieve it from memory.

---

## Subjects

| Code | Subject |
|------|---------|
| ITCS-396 | — |
| ITIS-103 | — |
| ITCS-347 | — |
| ITCS-441-Crypto | Cryptography |
| ITCS-440-Intelligent | Intelligent Systems |
| Linear-Algebra | Linear Algebra |

---

## Folder Structure

```
the-study-machine/
├── content/{subject}/          Source material (do NOT modify)
│   ├── notes/
│   ├── pdfs/
│   ├── slides/
│   └── transcripts/
│
├── sessions/{subject}/         One file per study session
│   ├── _template.md            Copy this to start a new session
│   └── {topic}.md
│
├── review/
│   └── schedule.md             Spaced repetition tracker
│
└── exam-prep/
    └── {subject}-master-questions.md   Aggregated Q&A per subject
```

---

## Session Workflow

Every study session has two phases:

### Phase 1 — Understand

Read the source material (transcript + slides + past exams) and work through it interactively with the user. Use analogies, examples, and exercises. Ask questions to check understanding. Keep going until the user confirms they are ready for Phase 2.

**Prompt the user gives Claude:**
> "We are doing Phase 1 of a study session. The topic is [topic]. Here is the source material: [paste content]. Explain this to me interactively. Give me analogies, examples, and exercises. Keep going until I tell you I am ready for Phase 2."

### Phase 2 — Exam Gold

Produce structured output optimized for spaced repetition:
- 5–10 dense bullet points for last-minute pre-exam review
- Active recall questions with difficulty ratings (🔴 Hard / 🟡 Medium / 🟢 Easy)
- A list of weak spots to revisit sooner

**Prompt the user gives Claude:**
> "Phase 1 is done. Now produce Phase 2 Exam Gold for [topic]: 5–10 dense bullet points for last-minute review, active recall questions with difficulty ratings (🔴🟡🟢), and a list of weak spots I should revisit sooner."

Output goes into `sessions/{subject}/{topic}.md`. Questions get added to `review/schedule.md`.

---

## Spaced Repetition Rules

After each self-test review, rate recall difficulty and update the schedule:

| Difficulty | Next review |
|------------|-------------|
| 🔴 Hard — struggled or needed to look | 1 day (reset) |
| 🟡 Medium — got it with effort | 3 days |
| 🟢 Easy — clean, immediate recall | Double the current interval |

Intervals: 1 → 3 → 7 → 14 → 30 → 60 → 120 days (cap at 120 for exam-critical topics).

---

## Hard Rules for Claude

- NEVER modify session files the user has already written
- NEVER alter the spaced repetition schedule without explicit instruction
- NEVER delete or overwrite content files (PDFs, transcripts, slides)
- When producing Phase 2 output, always use the active recall table format from the session template
- Questions should be exam-style: precise, retrieval-focused, not definitional trivia
