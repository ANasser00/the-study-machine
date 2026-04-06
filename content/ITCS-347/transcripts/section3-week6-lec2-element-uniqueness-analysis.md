# Section 3 — Week 6 Lecture 2 — Chapter 2: Element Uniqueness Analysis

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 18th, 2026  
**Coverage:** Chapter 2 continued — Element uniqueness problem (brute force), key comparison vs loop comparison, worst-case analysis with double summation step-by-step

---

## Part 1 — Recap & Announcements

**Dr. Ali Alsaffar** *(0:00)*  
Class. This is Doctor Alice Safar, ITCS 347 Introduction to Design and Analysis of Algorithms, Section 3.

**Dr. Ali Alsaffar** *(0:15)*  
We will continue our lecture on analysis framework. Last lecture we finished how to analyze program constructs, loops and we started how to analyze recursion. We gave introduction on recursion.

**Dr. Ali Alsaffar** *(0:35)*  
And we explained what is the meaning of using recursion for a problem. What does it mean by part of a problem? So if you want to solve a problem of certain size, you break it into small sizes. You find a solution for each size and combine the solutions. This is called.

**Dr. Ali Alsaffar** *(0:55)*  
And conquer.

**Dr. Ali Alsaffar** *(0:57)*  
Also, we showed you how to trace, how to trace a recursive algorithm if we have only one single call recursive call statement, and if we have more than one recursive call statement, how to do the tracing?

**Dr. Ali Alsaffar** *(1:14)*  
And at the end we started talking about analyzing recursive algorithm. Just for a quick announcement next week after the Eid holiday.

**Dr. Ali Alsaffar** *(1:28)*  
We will have our first quiz. It will be on a growth of functions. I will give you the announcement and the time for the quiz. It will be on Blackboard and probably you will use Lockdown browser. You know that you will be in the open space, you will have ChatGPT and maybe you will collaborate with others.

**Dr. Ali Alsaffar** *(1:48)*  
Students, you know that this is unethical. So we advise the students not to do that because at the end you are coming to learn, you know the subject and if you just do something that is.

**Dr. Ali Alsaffar** *(2:04)*  
And it's not helpful to you. It's not going to be nice, ethically not nice, and at the same time it will not be helpful to you. So I advise every student to work by their own. Also for the homework and we will allow for students.

**Dr. Ali Alsaffar** *(2:21)*  
And we will allow for the students to call out and work in a group, maximum 2.

---

## Part 2 — Element Uniqueness Problem

**Dr. Ali Alsaffar** *(52:57)*  
I mean, it checks whether all the elements in a given array of N elements are distinct.

**Dr. Ali Alsaffar** *(53:05)*  
The algorithm uses 2 nested loops to compare every pair of elements in the array. The outer loop passes over each element 1 by 1, and the inner loop compares that element with every element that comes after it in the array, more specifically.

**Dr. Ali Alsaffar** *(53:22)*  
For each element at index I as controlled by the outer loop, the inner loop begins comparing from the element at index I + 1 and continues up to the last element in the array. That's why the outer loop stops at index N - 2.

**Dr. Ali Alsaffar** *(53:38)*  
Ensuring that the last comparison is made between the elements at indices N - 2 and N - 1.

**Dr. Ali Alsaffar** *(53:47)*  
If at any point the algorithm finds two elements that are equal, it immediately returns false because the array contains duplicates. If the algorithm completes all comparisons without finding any equal pair, it returns true.

**Dr. Ali Alsaffar** *(54:03)*  
Confirming that all elements are unique.

---

## Part 3 — Analysis of Element Uniqueness

**Dr. Ali Alsaffar** *(54:07)*  
Let's move on to the analysis of the algorithm.

**Dr. Ali Alsaffar** *(54:11)*  
From observation, it is clear that the input size is N, representing the length of the array, and the basic operation is the key comparison performed at line 4.

**Dr. Ali Alsaffar** *(54:25)*  
Since the algorithm stops execution as soon as it finds the first 2 duplicate elements, then the number of key comparisons is not the same for every instance of the algorithm.

**Dr. Ali Alsaffar** *(54:36)*  
I am pausing the video. Now I am talking live in the class session. I've mentioned the basic operation as the key comparison. OK, when we say key comparison, it means when we compare 2 elements.

**Dr. Ali Alsaffar** *(54:53)*  
In the array. Now notice that for the for loop which is the outer loop and the inner loop, we also have comparison that is used for managing the loop. Now these are not key comparison, they are normal comparison and as I said before that we should not count them.

**Dr. Ali Alsaffar** *(55:10)*  
Into the for the basic operation because they manage the loops. But even in other problems if there is other comparison, for example after exiting the loop, let's say the inner loop, the outer loop consists of the inner loop and if statement after exiting the for loop this.

**Dr. Ali Alsaffar** *(55:30)*  
If statement, if it is not comparing elements, then we should not count them. So when we say key comparison, we concentrate only on when two elements are compared and the other.

**Dr. Ali Alsaffar** *(55:42)*  
So number of comparisons of A[i] equal A[j] not only depends on N, but also on specific input values.

**Dr. Ali Alsaffar** *(55:51)*  
Let C(N) be the number of comparisons.

**Dr. Ali Alsaffar** *(55:57)*  
If the first two elements in the array are equal, then only one comparison is needed. This represents the best case scenario.

**Dr. Ali Alsaffar** *(56:07)*  
On the other hand, if the array contains no duplicates or the only duplicate is at the end, for example the last two elements, then the algorithm must perform all possible comparisons which corresponds to the total number of iterations in the inner loop.

**Dr. Ali Alsaffar** *(56:24)*  
This total can be calculated by summing over the two nested loops, resulting in a Big Theta N squared complexity.

**Dr. Ali Alsaffar** *(56:34)*  
Let me now walk you through the details of this result.

---

## Part 4 — Step-by-Step Worst Case Summation

**Dr. Ali Alsaffar** *(56:39)*  
To find the time complexity of the algorithm for the worst case, we build summations from the two nested for loops.

**Dr. Ali Alsaffar** *(56:49)*  
So we write C for the worst case of N is equal to. Now for the first summation it will be for the outer loop — I goes from zero up to N - 2 — and for the 2nd summation it will be for the inner loop — J goes from I + 1.

**Dr. Ali Alsaffar** *(57:08)*  
Up to N - 1, since the comparison is executed only once in every iteration of the inner loop, so the inner summation will be a unity summation.

**Dr. Ali Alsaffar** *(57:21)*  
The evaluation of these two nested summations is equal to summation I = 0 up to N - 2. Now for the inner summation we have one inside the summation. To evaluate it, we take the last value minus the first value plus one.

**Dr. Ali Alsaffar** *(57:39)*  
The last value is N - 1 minus the first value which is I + 1, plus 1.

**Dr. Ali Alsaffar** *(57:49)*  
Now -1 + 1 is equal to 0 so this is equal to summation I goes from zero up to N - 2 of (N - 1 - I).

**Dr. Ali Alsaffar** *(58:05)*  
We will distribute the summation over this expression and this is equal to summation I goes from zero up to N - 2 of (N - 1) minus summation of I goes from zero up to N - 2 of I.

**Dr. Ali Alsaffar** *(58:24)*  
Now in the first summation N - 1 does not depend on I, so we can take it outside the summation. And in the second summation this is arithmetic sequence, so we can make it start from one instead of starting from zero, because adding zero to the summation will not affect the final result.

**Dr. Ali Alsaffar** *(58:43)*  
This is equal to (N - 1) times summation I goes from zero up to N - 2 of 1 minus summation I also goes from zero up to N - 2 of I.

**Dr. Ali Alsaffar** *(58:59)*  
The evaluation for the summation. I think we have reached the end of the class and I think we will stop here. So I will give a chance for those students who did not take attendance to take attendance.

**Dr. Ali Alsaffar** *(59:15)*  
I will first stop the recording.

---

## Reference Notes — Key Takeaways

### Element Uniqueness Problem — Algorithm
- **Input:** Array A of N elements
- **Goal:** Check if all elements are distinct
- **Method:** Two nested loops — outer loop i from 0 to N-2, inner loop j from i+1 to N-1
- **Compare:** A[i] == A[j] for every pair
- **Return:** false immediately if duplicate found; true if all pairs checked

### Key Comparison vs Loop Comparison — Critical Distinction
- **Key comparison:** comparing two array elements (A[i] == A[j]) — THIS is the basic operation
- **Loop management comparison:** the for-loop condition checks (i < N-2, j < N-1) — do NOT count these
- **Rule:** Only count comparisons that compare data elements, not loop control comparisons
- This applies to any problem: if there's an `if` statement after a loop that doesn't compare elements, don't count it either

### Cases for Element Uniqueness
- **Best case:** First two elements are duplicates → C(N) = 1
- **Worst case:** No duplicates (or duplicates only at the very end) → must do all comparisons → Theta(N^2)

### Worst Case — Step-by-Step Summation (Dr. Alsaffar's Method)

```
C_worst(N) = Sum(i=0 to N-2) Sum(j=i+1 to N-1) 1
```

**Step 1:** Evaluate inner summation (unity sum):
```
Sum(j=i+1 to N-1) 1 = (N-1) - (i+1) + 1 = N - 1 - i
```

**Step 2:** Substitute back:
```
C_worst(N) = Sum(i=0 to N-2) (N - 1 - i)
```

**Step 3:** Distribute the summation:
```
= Sum(i=0 to N-2) (N-1) - Sum(i=0 to N-2) i
```

**Step 4:** Simplify:
- First sum: (N-1) doesn't depend on i → pull it out: (N-1) * Sum(i=0 to N-2) 1 = (N-1)(N-1) = (N-1)^2
- Second sum: arithmetic series Sum(i=1 to N-2) i = (N-2)(N-1)/2

**Step 5:** Combine:
```
= (N-1)^2 - (N-2)(N-1)/2 = (N-1)[(N-1) - (N-2)/2] = (N-1)N/2
```

**Result:** C_worst(N) = N(N-1)/2 = Theta(N^2)

### Announcements
- **Quiz 1** confirmed for after Eid — topic: Growth of Functions, on Blackboard with Lockdown Browser
- Homework groups allowed (max 2 students)

### Gap in Transcript
- ~50 minute gap (2:21 to 52:57) where recursion analysis examples and tracing were likely continued before transitioning to the element uniqueness problem.
