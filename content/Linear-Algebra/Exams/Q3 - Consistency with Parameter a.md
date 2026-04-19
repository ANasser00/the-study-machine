# Past Exam Question 3 (7 marks) — Consistency with Parameter $a$

**Topic:** §1.2 Gauss/Jordan Elimination + §1.6 Further Results on Systems of Equations.
**Source:** Old exam (handwritten solution photographed).

---

## Problem

Determine the values of $a$ for which the following system is **consistent** or **inconsistent**.

$$
\begin{cases}
x + y + az &= 1 \\
x + 2y + az &= 2 \\
x + 2y + 3z &= 3
\end{cases}
$$

---

## Solution

### Augmented matrix

$$
\left[\begin{array}{ccc|c}
1 & 1 & a & 1 \\
1 & 2 & a & 2 \\
1 & 2 & 3 & 3
\end{array}\right]
$$

### Step 1: $R_2 \to R_2 - R_1$, $R_3 \to R_3 - R_1$

$$
\left[\begin{array}{ccc|c}
1 & 1 & a & 1 \\
0 & 1 & 0 & 1 \\
0 & 1 & 3 - a & 2
\end{array}\right]
$$

### Step 2: $R_3 \to R_3 - R_2$

$$
\left[\begin{array}{ccc|c}
1 & 1 & a & 1 \\
0 & 1 & 0 & 1 \\
0 & 0 & 3 - a & 1
\end{array}\right]
$$

The pivot in the third row depends on whether $3 - a = 0$. Two cases.

---

### Case 1: $3 - a = 0$, i.e., $\boxed{a = 3}$

The third row becomes $[0\ 0\ 0 \mid 1]$, which represents the equation
$$0 = 1.$$
This is a contradiction $\Rightarrow$ **no solution** $\Rightarrow$ the system is **INCONSISTENT**.

> ⚠️ **Correction on the photographed solution:** the handwriting says *"system would be consistent because $0 \ne 1$"* — that's backwards. $0 \ne 1$ means the equation **cannot be satisfied**, so the system is *inconsistent* (no solution). The "No solution" conclusion is correct; only the label is wrong.

---

### Case 2: $3 - a \ne 0$, i.e., $\boxed{a \ne 3}$

Scale $R_3$ by $\tfrac{1}{3-a}$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & a & 1 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & \dfrac{1}{3-a}
\end{array}\right]
$$

**Back-substitute** (bottom-up):

- Row 3: $z = \dfrac{1}{3-a}$.
- Row 2: $y = 1$.
- Row 1: $x + y + az = 1 \;\Rightarrow\; x = 1 - y - az = 1 - 1 - a \cdot \dfrac{1}{3-a} = -\dfrac{a}{3-a}$.

**Unique solution:**
$$
\boxed{\;S = \left(-\dfrac{a}{3-a},\;\; 1,\;\; \dfrac{1}{3-a}\right), \quad a \in \mathbb{R} \setminus \{3\}.\;}
$$

The system is **CONSISTENT** and has a **unique solution** for every $a \ne 3$.

---

## Summary table

| Value of $a$ | Status | # of solutions |
|---|---|---|
| $a = 3$ | Inconsistent | 0 (no solution) |
| $a \ne 3$ | Consistent | 1 (unique) |

Note: this particular system **never** has infinitely many solutions. The parameter only toggles between "unique solution" and "no solution" — because the first two rows of the coefficient matrix are linearly independent regardless of $a$, and only the third pivot can collapse.

---

## Exam strategy for parametric-consistency problems

1. **Row-reduce without committing to a value of the parameter.** Keep $a$ symbolic.
2. Identify the pivot that has the parameter in it. That pivot being zero or non-zero drives the case split.
3. **Case split** on the parameter:
   - If the pivot equation gives a contradiction ($0 = \text{nonzero}$) → inconsistent.
   - If the pivot equation gives $0 = 0$ (a free-variable row) → consistent with infinitely many solutions.
   - If the pivot is non-zero → unique solution; back-substitute.
4. **Report the full answer**: values of $a$, consistency status, and the solution set where one exists.

---

## Active recall

- 🟢 What does it mean for a row of an augmented matrix to look like $[0\ 0\ \ldots\ 0 \mid c]$ with $c \ne 0$?
- 🟡 Redo this problem without looking at the solution. For which $a$ is the system consistent, and what is the solution set?
- 🟡 Modify the system so that for some value of $a$ you get **infinitely many** solutions. (Hint: the bottom row needs to reduce to $[0\ 0\ 0 \mid 0]$, not $[0\ 0\ 0 \mid 1]$.)
- 🔴 For a general $3 \times 3$ system $Ax = b$ with $A$ depending on a parameter $a$, what three outcomes are possible, and how do you detect each from the row-echelon form?
- 🔴 Connect this to §1.6: when does a homogeneous system ($b = 0$) always have the trivial solution? When does it also have non-trivial solutions? How does this change for non-homogeneous systems?
