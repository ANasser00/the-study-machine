# Session: Final — Ch2, Ch3, Ch4, Ch5, Ch6

**Subject:** ITCS-440-Intelligent
**Date:** 2026-04-28
**Source material:**
- [x] PDFs: CH2, CH3, CH4, CH5, CH6

**Status:**
- [x] Phase 1 — Understanding
- [x] Phase 2 — Exam Gold
- [ ] Complete (revisit for final)

**Scope:**
- Chapter 2 — Problem Solving & Production Systems
- Chapter 3 — Search Algorithms (BFS, DFS, Best First, A*, AO*)
- Chapter 4 — Local Search (Hill Climbing, Simulated Annealing, GA)
- Chapter 5 — Game Playing (Minimax, Alpha-Beta)
- Chapter 6 — Knowledge Representation (Propositional, Predicate, Resolution, Semantic Networks, Frames)

---

## Phase 2 — Exam Gold

### Key Concepts

**Ch2 — Problem Solving & Production Systems**
- Production System = Knowledge Base (Rules + Facts) + Control Strategy + Working Memory
- Conflict resolution strategies: Rule Ordering, Size Ordering, LRU, MRU, Data Ordering
- Control strategy MUST cause motion — cannot cycle forever
- Water Jug: State = (X, Y) where X=4-gallon, Y=3-gallon. Goal=(2,Y). 8 rules: fill/empty/pour (2 cases each direction)
- 6 Problem Dimensions: Decomposability, Recoverability, Predictability, Solution Quality, Knowledge Required, Interaction

**6 Problem Dimensions — exam targets:**
- Decomposable → AO*. Non-decomposable → A* or Minimax
- Ignorable (theorem proving) / Recoverable (8-puzzle) / Irrecoverable (chess)
- Chess = irrecoverable. 8-puzzle = recoverable.

**Ch3 — Search Algorithms**

| Algorithm | Data Structure | Complete | Optimal | Function |
|-----------|---------------|----------|---------|----------|
| BFS | Queue | Yes | Yes | — |
| DFS | Stack | No | No | — |
| Best First | Priority Queue | No | No | h(n) |
| A* | Priority Queue | Yes | Yes (admissible) | g(n)+h(n) |
| AO* | AND-OR graph | Yes | Yes | h(n) only |

- BFS = level by level. DFS = deep first, backtrack.
- DFS: NOT complete (infinite branches), NOT optimal (first ≠ shortest), LOW memory
- BFS: complete, optimal, HIGH memory
- A*: g(n) = cost from start to current. h(n) = estimated cost to goal.
- Admissible heuristic = never overestimates actual cost → A* is optimal
- AO* ignores g(n) because longer path may be necessary in decomposable problems
- A* cannot solve decomposable problems — that's AO*

**Ch4 — Local Search**
- Hill Climbing: local search, no memory, only looks at neighbors
  - Simple: first better neighbor
  - Steepest Ascent: check all neighbors, pick best
  - Stochastic: random among better neighbors
- Hill Climbing problems: Local Maximum (stuck at non-global peak), Plateau (all neighbors equal), Ridge (narrow path)
- Simulated Annealing: P = exp(-(f(neighbor)-f(current))/T). High T = accepts worse moves. Low T = only accepts better. Can escape local maxima.
- Genetic Algorithms: global search. Selection → Crossover (split at k, swap tails) → Mutation (flip bit). Works on population.

**Ch5 — Game Playing**
- Minimax: two-player game. MAX = you (maximize). MIN = opponent (minimize).
- Work bottom-up: MIN nodes pick lowest child. MAX nodes pick highest child.
- Minimax = DFS with look-ahead (NOT BFS)
- Alpha-Beta: same result as Minimax, prunes branches that can't affect outcome. Prune when alpha ≥ beta.
- Alpha-Beta never changes the final answer — only skips unnecessary nodes.

**Ch6 — Knowledge Representation**

| Method | Structure | Key Feature |
|--------|-----------|-------------|
| Propositional | Logic statements | True/False only, no variables |
| Predicate | Logic + variables | ∀ (for all), ∃ (there exists) |
| Semantic Networks | Graph | Nodes=objects, Edges=relationships, Inheritance |
| Frames | Template | Slots + values, Inheritance |

- Resolution: prove by contradiction (goal refutation). Assume NOT goal → derive empty clause.
- Frames = last topic in scope (frame-based structure).

---

### Active Recall Questions

| # | Question | Difficulty | Last Reviewed | Next Review |
|---|----------|------------|---------------|-------------|
| 1 | What are the 6 problem dimensions? Give an example for recoverability. | 🔴 Hard | 2026-04-28 | 2026-04-29 |
| 2 | BFS vs DFS — complete? optimal? memory? data structure? | 🔴 Hard | 2026-04-28 | 2026-04-29 |
| 3 | Why does AO* ignore g(n)? | 🔴 Hard | 2026-04-28 | 2026-04-29 |
| 4 | What are the 3 problems with Hill Climbing? | 🟡 Medium | 2026-04-28 | 2026-05-01 |
| 5 | How does simulated annealing escape local maxima? | 🟡 Medium | 2026-04-28 | 2026-05-01 |
| 6 | What are the 3 GA operations? | 🟡 Medium | 2026-04-28 | 2026-05-01 |
| 7 | Minimax — which traversal does it use and why? | 🟡 Medium | 2026-04-28 | 2026-05-01 |
| 8 | What is the difference between propositional and predicate calculus? | 🟢 Easy | 2026-04-28 | 2026-05-01 |
| 9 | What does resolution use to prove a statement? | 🟢 Easy | 2026-04-28 | 2026-05-01 |
| 10 | What is a frame? What are its components? | 🟢 Easy | 2026-04-28 | 2026-05-01 |

<details>
<summary>Answers</summary>

**Q1:** Decomposability, Recoverability, Predictability, Solution Quality, Knowledge Required, Interaction. Recoverability: Ignorable (theorem proving) / Recoverable (8-puzzle — can undo moves) / Irrecoverable (chess — can't undo a move).

**Q2:** BFS: Queue, complete, optimal, high memory. DFS: Stack, NOT complete, NOT optimal, low memory.

**Q3:** In decomposable problems a longer path may be necessary — you must solve all subparts. Penalizing path length doesn't make sense so g(n) is ignored.

**Q4:** Local Maximum (stuck at non-global peak, all neighbors worse), Plateau (all neighbors equal, can't choose direction), Ridge (narrow path, hill climbing can't follow it).

**Q5:** It accepts worse moves with probability P = exp(-(f(neighbor)-f(current))/T). At high temperature it accepts worse moves often. As T decreases it becomes more selective. This lets it escape local maxima that trap hill climbing.

**Q6:** Selection/Reproduction (keep fittest), Crossover (split at point k, swap tails), Mutation (flip a random bit).

**Q7:** DFS. Minimax must reach the bottom of a branch to evaluate leaf scores before it can score parent nodes. BFS would try to score nodes level by level which is impossible without leaf values.

**Q8:** Propositional: only true/false statements, no variables. Predicate: adds variables and quantifiers (∀=for all, ∃=there exists). Predicate is more expressive.

**Q9:** Goal refutation (proof by contradiction). Assume NOT goal, derive contradiction (empty clause = FALSE).

**Q10:** A frame is a template for an object. Components: slots (attributes) and values. Can inherit from parent frames.

</details>

---

### Weak Spots

- **DFS memory** — kept thinking DFS uses more memory. DFS uses LESS (only current path). BFS stores entire frontier.
- **AO* vs A* function** — AO* uses h(n) ONLY. A* uses g(n)+h(n).
- **Hill climbing memory** — it has NONE. Local search only.
- **Minimax traversal** — it's DFS not BFS. Must go to leaves before scoring parents.
- **Chess vs 8-puzzle** — Chess=irrecoverable. 8-puzzle=recoverable.

---

## Session Notes

- Exam was April 28, 2026. Covering Ch2–Ch6 up to frame-based structure.
- User started from zero — built up from scratch in one session.
- Past exam patterns: Q1=T/F (10 marks), Q2=MCQ (6 marks), Q3-Q5=written (traces, rules, trees).
- Highest weight: Ch3 search algorithms + Ch2 production systems.
- Minimax=DFS with look-ahead appears on every exam.
- AO* ignoring g(n) appears on every exam.
- Resolution=goal refutation appears on every exam.
- Session was exam-day cramming — revisit for final with deeper understanding.
