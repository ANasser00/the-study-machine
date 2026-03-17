# Spaced Repetition Schedule

## How Spaced Repetition Works

Forgetting follows a curve: memory fades fastest right after learning, then more slowly over time. The trick is to review just *before* you would forget — this resets the forgetting curve and each reset makes the memory more durable than the last.

The intervals used here are a simplified version of the SM-2 algorithm:

1. Review on day 1 (the day after first learning)
2. Review on day 3
3. Review on day 7
4. Review on day 14
5. Review on day 30
6. Continue doubling (60, 120...)

After each review, rate your recall and adjust the next interval:

| Difficulty | What it means | Next interval |
|------------|---------------|---------------|
| Hard | Struggled, needed to look at the answer | 1 day (restart) |
| Medium | Got it but it took effort or was partially wrong | 3 days |
| Easy | Clean, immediate recall | Double the current interval |

Review the active recall questions in your session file. Cover the answers, attempt each question from memory, then check. Be honest — partial answers count as Medium, not Easy.

---

## Due Today

> Update this section each morning. Scan the Master Table below for rows where "Next Review" is today or earlier and list them here.

<!-- Example format:
- [ ] Classical Mechanics — Newton's Laws — Q3 (Hard)
- [ ] Classical Mechanics — Newton's Laws — Q6 (Hard)
-->

*(No items due — update this section daily)*

---

## Master Table

> One row per topic. Update after every review session.
> Difficulty reflects your *most recent* self-assessment for that topic overall.

| Subject | Topic | Difficulty | Last Reviewed | Next Review | Interval (days) | Notes |
|---------|-------|------------|---------------|-------------|-----------------|-------|
| Classical Mechanics | Newton's Laws of Motion | Medium | 2026-03-11 | 2026-03-14 | 3 | Q3 and Q6 still Hard — review those first |

---

## Interval Guide

Use this when deciding the next review date:

```
Hard   → next review in 1 day
         (reset — do not advance the interval)

Medium → next review in 3 days
         (advance slowly — keep interval at 3 until you hit Easy)

Easy   → double the current interval
         3 → 7 → 14 → 30 → 60 → 120...
         (cap at 120 days for exam-critical topics)
```

**Practical tips:**

- Review Hard questions every day until they become Medium. They deserve extra attention.
- If a topic has been Easy for two consecutive reviews, you can de-prioritise it unless an exam is within 2 weeks.
- Before an exam, reset the schedule: treat everything as due regardless of the Next Review date and work through the full master file in `exam-prep/`.
- Do not skip reviews when something is Hard — the discomfort of struggling to recall is exactly what drives retention.
