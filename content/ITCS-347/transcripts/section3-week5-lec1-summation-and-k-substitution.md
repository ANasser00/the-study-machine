# Section 3 — Week 5 Lecture 1 — Chapter 2: Summation & K-Substitution

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 9th, 2026  
**Coverage:** Chapter 2 continued — Analysis framework recap, summation for counting iterations, variable substitution (K transformation) for non-simple loop iterators

---

## Part 1 — Analysis Framework Recap

**Dr. Ali Alsaffar** *(0:03)*  
So far ITCS 347 Design and Analysis of Algorithms Section 3.

**Dr. Ali Alsaffar** *(0:10)*  
8.

**Dr. Ali Alsaffar** *(0:14)*  
We are still in Chapter 2.

**Dr. Ali Alsaffar** *(0:18)*  
What we have covered last lecture.

**Dr. Ali Alsaffar** *(0:21)*  
Is building analysis framework.

**Dr. Ali Alsaffar** *(0:26)*  
So the framework is basically a guideline that we need to follow whenever we want to analyze an algorithm guideline analysis algorithms. The first step in this framework is.

**Dr. Ali Alsaffar** *(0:45)*  
Determining the problem size because the time complexity will be expressed using this parameter.

**Dr. Ali Alsaffar** *(0:54)*  
Second step you determine the basic operation. A third step you analyze and find the time complexity. But at this step you need to consider whether there are cases or not, and this is the step that we have stopped.

**Dr. Ali Alsaffar** *(1:14)*  
At last lecture.

**Dr. Ali Alsaffar** *(1:20)*  
So.

---

## Part 2 — Summation Techniques & K-Substitution for Non-Simple Iterators

**Dr. Ali Alsaffar** *(49:55)*  
Next one is 1 and so on. And for 2K - 1 to make the first value is 1. Then you have to start K from 1-2 and so on. So both of them will give you the same answer. In this case K represents what?

**Dr. Ali Alsaffar** *(50:11)*  
So we will transform it into EN and as you can see that K is increased by one. See 01. So when K is equal to 0 it will give you one. When K is equal to one it gives you 3.

**Dr. Ali Alsaffar** *(50:27)*  
K is a simple iterator. We can use it in the summation. So we say summation. Now we will change it. We'll start from zero up to K and here we have one. So what we will get here.

**Dr. Ali Alsaffar** *(50:41)*  
We will get — when I is equal to 0 we will get one. This is the first iteration. When K is equal to one we get one. This is the second iteration and for the last value we have one. So this is iteration 1.

**Dr. Ali Alsaffar** *(50:59)*  
This is iteration 2.

**Dr. Ali Alsaffar** *(51:01)*  
And so on. And the answer that we will get because this is a formula will be last value which is K minus first value plus one. So we have K + 1. Now this K.

**Dr. Ali Alsaffar** *(51:17)*  
Will give me number.

**Dr. Ali Alsaffar** *(51:20)*  
Of iterations.

**Dr. Ali Alsaffar** *(51:31)*  
You have one iteration. If it is one, this is the second iteration. I know the mapping is not correct. If you use the other one, it will be more clearer. So if you use the other one, then if you use the other one, so T(N).

**Dr. Ali Alsaffar** *(51:48)*  
Summation I goes from one up to.

**Dr. Ali Alsaffar** *(51:53)*  
To where — now to K again. This will be equal to K - 1 plus 1. So this is equal to K. Now if you start K from one, then K is the number of iterations.

**Dr. Ali Alsaffar** *(52:10)*  
But if you start from zero, then K is what? K will be which iteration? So if 0 first iteration, if 1 second iteration. So if K it is the K-th operation. So this is how we look at the answer.

**Dr. Ali Alsaffar** *(52:29)*  
Both will give me the same answer.

**Dr. Ali Alsaffar** *(52:32)*  
But you need to know what is the value of K. So now the translation of the summation into K.

**Dr. Ali Alsaffar** *(52:40)*  
You get an answer in K. Next you need to find what is K because in the condition we have N. The number of iterations depends on N, not on K. So this is how we will say. We will say that the last iteration.

**Dr. Ali Alsaffar** *(52:55)*  
And anchor iteration — when this is the last iteration, the last iteration.

**Dr. Ali Alsaffar** *(53:04)*  
The last iteration I = 2.

**Dr. Ali Alsaffar** *(53:10)*  
2K plus one for this summation.

**Dr. Ali Alsaffar** *(53:15)*  
For this summation.

**Dr. Ali Alsaffar** *(53:17)*  
The condition is.

**Dr. Ali Alsaffar** *(53:21)*  
Final condition: 2K+1 less than or equal to N.

**Dr. Ali Alsaffar** *(53:28)*  
The last iteration — you solve for K. And if you take an example, if N.

**Dr. Ali Alsaffar** *(53:38)*  
If N is equal to 9, what are the values of I? It will be 1, 3, 5, 7 and 9. If you have 2K plus one less than or equal to.

**Dr. Ali Alsaffar** *(53:54)*  
9. And what will be the last value or what will be the K for the last iteration? You solve for this — the last iteration. The value of K will be — this is 0, 1, 2, 3. It will be 4, but this is the value.

**Dr. Ali Alsaffar** *(54:10)*  
For the last iteration where you have 2 * 4 is 8 plus 1 which is 9. So the value of K for the last iteration is equal to K. So it means you solve for this equation. So you know that if you want to solve for this equation.

**Dr. Ali Alsaffar** *(54:26)*  
You take 1 to the other side and it will be 8 and 2K divided by — 8 / 2 — K. Let me show you here: 2K less than or equal to 8. K is less than or equal to.

**Dr. Ali Alsaffar** *(54:43)*  
4. The last value of K is equal to 4. So you solve for this problem, for this condition.

**Dr. Ali Alsaffar** *(54:53)*  
So you have 2K less than or equal to N - 1, so K is less than or equal to (N - 1) / 2.

**Dr. Ali Alsaffar** *(55:03)*  
Now to get rid of the inequality less than or equal to, assume that the value of I will reach N and you know that if it is odd then you will reach N, but if it is even it will not reach exactly N.

**Dr. Ali Alsaffar** *(55:20)*  
But for simplicity to make the analysis easy, you assume that the last value that we will check or the value of I is equal to N. You solve for K.

**Dr. Ali Alsaffar** *(55:37)*  
So (N - 1) / 2, so this is the value of K. Now from the summation on top.

**Dr. Ali Alsaffar** *(55:44)*  
We started by saying that I starts from zero up to K and we say that this is K + 1. You substitute so K is equal to (N - 1) / 2 + 1 and this is the answer. Number of iterations is this.

**Dr. Ali Alsaffar** *(56:01)*  
I know that the steps are lengthy, but when you get used to it.

**Dr. Ali Alsaffar** *(56:09)*  
Then you will find that it is not difficult to find the answer. So notice here we are dividing by two. That means number of iterations will be half if the iterator is increased by two.

**Dr. Ali Alsaffar** *(56:24)*  
I go over the recording. In the recording I'm given concrete example on values of N and how to relate K with number of iterations for the for loop. So in conclusion.

**Dr. Ali Alsaffar** *(56:40)*  
If you have a simple for loop.

**Dr. Ali Alsaffar** *(56:43)*  
Then number of iterations will be simple summation. But if you have a loop that the iterator is not simple, then you need to transform it using a variable K and K will be the number of iterations. So the answer for the summation will be in terms of K.

**Dr. Ali Alsaffar** *(57:01)*  
Then you relate K to I, correlate K to N and find the value of K in terms of N. You substitute into the summation.

**Dr. Ali Alsaffar** *(57:13)*  
Any question?

**Dr. Ali Alsaffar** *(57:16)*  
We have reached almost the end the lecture, so we will take attendance for the.

---

## Reference Notes — Key Takeaways

### Dr. Alsaffar's Step-by-Step Method for Non-Simple Iterators

When the loop iterator doesn't increment by 1 (e.g., `i = 1, 3, 5, 7, ...`), you can't directly use a simple summation. His method:

1. **Introduce a new variable K** as a simple counter (K = 0, 1, 2, 3, ...)
2. **Express I in terms of K** — e.g., if I = 1, 3, 5, 7... then I = 2K + 1
3. **Rewrite the summation using K** — now you have a simple summation from 0 to K (or 1 to K)
4. **Solve the summation** — with a simple iterator, the answer is K + 1 (starting from 0) or K (starting from 1)
5. **Find K in terms of N** — use the loop's exit condition. Set the last value of I equal to N, substitute the I-to-K formula, solve for K
   - Example: 2K + 1 ≤ N → K ≤ (N-1)/2
6. **Substitute K back** into the summation result to get the final answer in terms of N

### Worked Example (N = 9, I = 1, 3, 5, 7, 9)
- I = 2K + 1, so K = 0, 1, 2, 3, 4
- Summation from K=0 to K=4 of 1 = K + 1 = 5 iterations
- General: K = (N-1)/2, so iterations = (N-1)/2 + 1 = (N+1)/2

### Two Conclusions
- **Simple for loop** (iterator increments by 1) → straightforward summation
- **Non-simple loop** (iterator increments by 2, multiplied, etc.) → K-substitution method, answer in terms of K, then relate K to N

### Gap in Transcript
- ~48 minute gap (1:20 to 49:55) where earlier summation examples and the setup for this K-substitution technique were covered.
