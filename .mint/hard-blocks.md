# Hard Blocks — What Agents Can NEVER Do

Violations trigger immediate stop and escalation to user.

## Universal
- NEVER `git push` — human reviews and pushes manually
- NEVER modify files outside declared task scope
- NEVER commit with failing gates
- NEVER fix bad output directly — reset and fix the spec
- NEVER continue after 2 failures on the same spec

## Context Protection
- NEVER read large files in the main orchestrator context
- Subagents return summaries only

## Project-Specific
- NEVER modify session files the user has already written — these are personal study notes
- NEVER alter the spaced repetition schedule without explicit user instruction
- NEVER delete or overwrite content files (PDFs, transcripts, slides) — these are source material
