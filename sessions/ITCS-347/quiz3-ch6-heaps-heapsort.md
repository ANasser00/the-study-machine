# Session: Quiz 3 — Chapter 6: Heaps and Heapsort

**Subject:** ITCS-347
**Date:** 2026-05-10
**Quiz:** Monday May 11th, 2026
**Source material:** Chapter6-Transform-and-conquer.pptx, ITCS347_T2_Sem1_2025_2026_FA.pdf

**Status:**
- [x] Phase 1 — Understanding
- [x] Phase 2 — Exam Gold

---

## Phase 2 — Exam Gold

### Dense Bullet Points (last-minute review)

- **Heap = complete binary tree + parental dominance.** Complete = all levels full, last level fills left-to-right. Max-heap = every parent ≥ both children.
- **Array representation H[1..n] (1-indexed).** Read tree level by level left to right. Left child of i = H[2i]. Right child = H[2i+1]. Parent = H[⌊i/2⌋]. Root = H[1] = always the maximum.
- **Non-leaf nodes:** indices 1 to ⌊n/2⌋. Leaves: ⌊n/2⌋+1 to n. Only non-leaves need heapifying.
- **HEAPIFY(H, i):** compare H[i] with H[2i] and H[2i+1], find largest, swap if H[i] not largest, recurse at swapped position. Stops when node is largest OR hits a leaf. Pushes node **down**.
- **BUILD-HEAP:** apply HEAPIFY from i=⌊n/2⌋ down to i=1. Leaves are skipped. Multiple swaps can happen at i=1. Complexity: O(n).
- **Insertion:** add at end (index n+1), bubble **up** — compare with parent H[⌊i/2⌋], swap if new key > parent, repeat. Stops at root or when parent ≥ new key.
- **Heapsort Stage 1:** BUILD-HEAP on the array → O(n).
- **Heapsort Stage 2:** repeat n−1 times: swap H[1] with H[n], freeze last element, reduce heap size by 1, HEAPIFY at root → O(n log n) total.
- **Why "Transform and Conquer":** the array is first transformed into a heap (a more structured form), then the sorting problem is conquered using that structure.
- **Complexity summary:** HEAPIFY = O(log n). BUILD-HEAP = O(n). Insertion = O(log n). Heapsort = O(n log n). Sorts **in-place** (no extra array needed).

---

### Active Recall Questions

| # | Question | Difficulty | Last Reviewed | Next Review |
|---|----------|------------|---------------|-------------|
| 1 | Given a binary tree, identify every parent-child violation and explain why it is not a max-heap. | 🟢 Easy | 2026-05-10 | 2026-05-13 |
| 2 | Given a tree diagram, write its array representation H[1..n]. | 🟢 Easy | 2026-05-10 | 2026-05-13 |
| 3 | What are the formulas for left child, right child, and parent of node i? | 🟢 Easy | 2026-05-10 | 2026-05-13 |
| 4 | Trace HEAPIFY(H, 1) on a given array — show every swap and the array after each. | 🟡 Medium | 2026-05-10 | 2026-05-13 |
| 5 | Trace BUILD-HEAP on a random array — show array after each HEAPIFY call. | 🟡 Medium | 2026-05-10 | 2026-05-13 |
| 6 | Trace insertion of a new key into an existing heap — show every bubble-up swap. | 🟡 Medium | 2026-05-10 | 2026-05-13 |
| 7 | Trace one full deletion in Heapsort (swap root with last, freeze, heapify). | 🟡 Medium | 2026-05-10 | 2026-05-13 |
| 8 | Trace full Heapsort on a 6-element array — both stages. | 🔴 Hard | 2026-05-10 | 2026-05-11 |
| 9 | Why is Heapsort called "Transform and Conquer"? One sentence. | 🟢 Easy | 2026-05-10 | 2026-05-13 |
| 10 | What is the time complexity of HEAPIFY, BUILD-HEAP, and Heapsort? | 🟢 Easy | 2026-05-10 | 2026-05-13 |

<details>
<summary>Answers</summary>

**Q1:** Check every parent-child pair. A violation = any node where parent < child. State which node and which child caused it.

**Q2:** Read level by level left to right starting at H[1]. Root = H[1], then left-to-right per level.

**Q3:** Left child = H[2i]. Right child = H[2i+1]. Parent = H[⌊i/2⌋].

**Q4:** At each step — find largest among H[i], H[2i], H[2i+1]. Swap if H[i] not largest. Follow the swapped node down. Stop when no children or node is largest.

**Q5:** Start at i=⌊n/2⌋, go down to i=1. At each i, run full HEAPIFY (may involve multiple swaps going deep). Show array after each i completes.

**Q6:** Add at end. Parent = H[⌊i/2⌋]. Swap if new key > parent. Follow node up. Stop at root or when parent ≥ node.

**Q7:** Swap H[1] with H[n]. Freeze H[n]. HEAPIFY at i=1 on H[1..n-1]. May involve multiple swaps going down.

**Q8:** Stage 1: BUILD-HEAP (heapify from ⌊n/2⌋ to 1). Stage 2: n−1 deletions each = swap root with last unfrozen + heapify. Result is sorted ascending.

**Q9:** The array is first **transformed** into a heap (structured form), then the sorting is **conquered** using repeated max deletions.

**Q10:** HEAPIFY = O(log n). BUILD-HEAP = O(n). Heapsort = O(n log n).

</details>

---

### Weak Spots

- **Forgetting to HEAPIFY after the swap in deletion** — the swap is only half of a deletion. Always heapify the root after.
- **BUILD-HEAP direction** — must go from ⌊n/2⌋ **down to 1**, not up. Going the wrong direction is a common mistake.
- **HEAPIFY goes multiple levels deep** — especially at i=1, it can cascade down 2-3 levels. Trace every level, don't stop after one swap.
- **Bubble-up vs bubble-down** — insertion bubbles **up** (compare with parent). HEAPIFY pushes **down** (compare with children). Don't mix them.
- **1-indexed arrays** — H[1] is the root, not H[0]. Parent formula is ⌊i/2⌋, not ⌊(i-1)/2⌋.
