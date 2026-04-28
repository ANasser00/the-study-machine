# Session: Test 2 — Recursive Analysis, Brute-Force, Divide-and-Conquer

**Subject:** ITCS-347
**Date:** 2026-04-26
**Source material:**
- [x] Past exams: T2 Sem1 2025/2026, T1 Sem1 2025/2026, Mid Sem2 2024/2025, T1 Sem1 2024/2025
- [ ] Slides: Chapter 2, Chapter 3 (Brute-Force), Chapter 5 (D&C)

**Status:**
- [x] Phase 1 — Understanding
- [x] Phase 2 — Exam Gold
- [ ] Complete (revisit for final)

**Doctor's confirmed scope for Test 2:**
- Chapter 2 (Recursive Analysis) — recurrences + Master Theorem only. Back substitution is NOT included.
- Brute-Force — algorithm design, Selection Sort trace, Bubble Sort trace
- Divide-and-Conquer — Mergesort, x^n, Quicksort partition

---

## Phase 2 — Exam Gold

### Key Concepts

- **Master Theorem:** T(n) = aT(n/b) + Θ(n^d). Extract a, b, d. Compare a vs b^d. Case 1: a < b^d → Θ(n^d). Case 2: a = b^d → Θ(n^d log n). Case 3: a > b^d → Θ(n^(log_b a)). Always simplify the final exponent.
- **d is the exponent of n in f(n).** If f(n) = constant → d = 0. If f(n) = n → d = 1. If f(n) = n² → d = 2.
- **Writing T(n):** Cover all recursive calls → count how many (→ a), what size each takes (→ n/b), then count how many times the basic operation runs in what's left (→ f(n)). Base case = 0 if no basic op runs there.
- **Basic operation priority:** multiplication > addition > comparison. The dominant arithmetic op in the non-recursive code.
- **Manager's work trick:** Cover every F(...) call. Read remaining code top-to-bottom. Count how many times the basic operation runs. That's f(n).
- **Brute-force algorithm pattern:** one loop (O(n)) or nested loops (O(n²)). Track a running variable (min/max/k). Use `if i ≤ j then return` to exit early. Never "delete" — use index k to overwrite in place.
- **Selection Sort:** each pass finds the minimum of the unsorted part and swaps it to the front. Write the full array after every pass.
- **Bubble Sort:** each pass compares adjacent pairs left-to-right, largest bubbles to end. Never go backwards within a pass.
- **Mergesort recurrences:** Best: T(n) = 2T(n/2) + ⌊n/2⌋. Worst: T(n) = 2T(n/2) + n−1. Both → Θ(n log n). Worst case input for merge: alternating elements e.g. [1,3,5,7] and [2,4,6,8].
- **x^n multiplications:** odd exponent → 2 multiplications at that level. Even exponent → 1 multiplication. Halve exponent each step (floor if odd). Stop at x^1. Count total.
- **Quicksort Partition:** p = A[l]. i scans right while A[i] < p (moves through small). j scans left while A[j] > p (moves through big). Pre-increment i and pre-decrement j before inner scans. If i ≤ j → swap. End: swap A[l] with A[j], return j.
- **String Matching worst case:** (n − m + 1) × m comparisons. Worst input: T = AAAAAA, P = AAB.

---

### Active Recall Questions

| # | Question | Difficulty | Last Reviewed | Next Review |
|---|----------|------------|---------------|-------------|
| 1 | T(n) = 3T(n/2) + 4n. Apply Master Theorem — full working. | 🟢 Easy | 2026-04-26 | 2026-04-29 |
| 2 | Given a recursive algorithm, how do you identify the basic operation? How do you write T(n)? | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 3 | What is the d trap in Master Theorem? Give an example where f(n) = constant. | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 4 | Write the full Partition(A[l..r]) algorithm from memory. | 🔴 Hard | 2026-04-26 | 2026-04-27 |
| 5 | Why does j start at r+1 in Partition? What does the pre-decrement do? | 🔴 Hard | 2026-04-26 | 2026-04-27 |
| 6 | Why does i scan while A[i] < p, not A[i] > p? Memory trick? | 🔴 Hard | 2026-04-26 | 2026-04-27 |
| 7 | Write Mergesort recurrence for best and worst case. What input causes the merge worst case? | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 8 | How many multiplications to compute x^21 using D&C? Show all steps. | 🟢 Easy | 2026-04-26 | 2026-04-29 |
| 9 | Trace Selection Sort on [5, 3, 8, 1, 9, 2]. Write full array after each pass. | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 10 | Write a brute-force algorithm to remove all odd numbers from A[0..n-1] in-place. | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 11 | What is the Mergesort diagram structure? What levels must you show? | 🟡 Medium | 2026-04-26 | 2026-04-29 |
| 12 | T(n) = 4T(n/2) + n³. Apply Master Theorem — full working. | 🟢 Easy | 2026-04-26 | 2026-04-29 |

<details>
<summary>Answers</summary>

**Q1:** a=3, b=2, d=1. b^d=2. a > b^d → Case 3. T(n) ∈ Θ(n^(log₂ 3)).

**Q2:** Basic op = most expensive arithmetic op in the non-recursive body (mult > add > compare). T(n): count recursive calls (→ a), subproblem size (→ n/b), cover recursive calls and count basic op executions in what's left (→ f(n)). Base case = 0 if no basic op runs there.

**Q3:** d comes from the exponent of n in f(n). If f(n) = 1 (constant), d = 0 not 1. Example: T(n) = 2T(n/2) + 1 → d = 0, b^d = 2^0 = 1. Trap: writing d = 1 because you see no n.

**Q4:**
```
Algorithm Partition(A[l..r])
  p ← A[l]
  i ← l
  j ← r + 1
  while i < j do
    i ← i + 1
    while A[i] < p and i ≤ r do i ← i + 1
    j ← j − 1
    while A[j] > p do j ← j − 1
    if i ≤ j then
      Swap(A[i], A[j])
  Swap(A[l], A[j])
  return j
```

**Q5:** j starts at r+1 so that after the pre-decrement (j ← j−1), j lands on r (the actual last element). If j started at r, the pre-decrement would skip the last element.

**Q6:** i scans from the LEFT looking for a big element (≥ p) that's out of place. It moves while seeing small elements (A[i] < p). Memory: i moves through small, j moves through big.

**Q7:** Best: T(n) = 2T(n/2) + ⌊n/2⌋. Worst: T(n) = 2T(n/2) + n−1. Both Θ(n log n). Worst case merge input: alternating elements e.g. Left=[1,3,5,7], Right=[2,4,6,8] — every element requires a comparison.

**Q8:** x^21(odd)→2, x^10(even)→1, x^5(odd)→2, x^2(even)→1, x^1(base)→0. Total = 6 multiplications.

**Q9:** Start:[5,3,8,1,9,2] → 1:[1,3,8,5,9,2] → 2:[1,2,8,5,9,3] → 3:[1,2,3,5,9,8] → 4:[1,2,3,5,9,8] → 5:[1,2,3,5,8,9]

**Q10:**
```
Algorithm KeepOdd(A[0..n-1])
  k ← 0
  for i ← 0 to n-1 do
    if A[i] % 2 ≠ 0 then
      A[k] ← A[i]
      k ← k + 1
  n ← k
```

**Q11:** 5 levels: (1) full array, (2) two halves split, (3) individual elements, (4) two halves merged separately, (5) final merged array. Never skip level 4 — the intermediate merges must be shown explicitly.

**Q12:** a=4, b=2, d=3. b^d=2^3=8. a < b^d (4 < 8) → Case 1. T(n) ∈ Θ(n^d) = Θ(n³).

</details>

---

### Weak Spots

- **Partition algorithm** — consistently forgetting: (1) A[i] < p direction, (2) if i ≤ j condition, (3) pre-increment before inner while. Drill this until it's automatic.
- **d = 0 trap** — when f(n) is a constant, d = 0. Written d = 1 twice under pressure.
- **Manager's work** — initially missed for loops sitting above the return line. Always read the full non-recursive body top-to-bottom.
- **Mergesort diagram** — tends to skip the intermediate merge level (level 4). Must show two halves merged separately before the final combine.
- **Base case value** — confused the return value of the algorithm with the number of basic operations. Base case = count of basic ops there, almost always 0.

---

## Session Notes

- Test 2 is April 27, 2026 @ 10:45–11:45 AM, on campus, one hour.
- Back substitution explicitly removed by Dr. Alsaffar announcement.
- Heap/Heapify skipped — confirmed not on Test 2.
- Exam pattern: 3 questions × 10 points = 30 points total (based on T2 Sem1 2025/2026 structure).
- New past exam added: ITCS347_T2_Sem1_2025_2026_FA.pdf → content/ITCS-347/past-tests/
- String matching is low-probability for Test 2 but worth 2 mins to know the formula: (n−m+1)×m.
