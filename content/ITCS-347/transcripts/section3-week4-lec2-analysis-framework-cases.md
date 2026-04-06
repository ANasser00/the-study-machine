# Section 3 — Week 4 Lecture 2 — Chapter 2: Analysis Framework (Cases)

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 4th, 2026  
**Coverage:** Chapter 2 continued — Analysis framework steps, best/worst/average case, sequential search example

---

## Part 1 — Analysis Framework Recap & Basic Operation

**Dr. Ali Alsaffar** *(0:00)*  
Good morning, class. This is Doctor Al Safar, ITCS 347, Section 3.

**Dr. Ali Alsaffar** *(0:11)*  
We will continue our lecture on the analysis framework. We started Chapter 2. We said that we would build a framework for the analysis. The first step in the framework is to determine the problem size.

**Dr. Ali Alsaffar** *(0:28)*  
And we have discussed this last lecture. The 2nd is to determine the basic operation. In a previous lecture we talked about the measurement that we were going to use for measuring the running time and we said that using seconds, milliseconds time directly.

**Dr. Ali Alsaffar** *(0:46)*  
Is not, yeah, I mean appropriate for the following drawbacks and the metric measure that we will use is to count how many times some operations are executed by the algorithm. The detail analysis you count all.

**Dr. Ali Alsaffar** *(1:04)*  
Operations how many times they are executed, but this method is sometimes difficult and unnecessary to reach the final answer.

**Dr. Ali Alsaffar** *(1:14)*  
The other way is to use a quick analysis and in the quick analysis you identify one operation only that you need to count how many times it is executing. So what is this operation? We call it basic operation after we understand how to determine the basic operation and then we will have an example.

**Dr. Ali Alsaffar** *(1:34)*  
On detail analysis and quick analysis.

**Dr. Ali Alsaffar** *(1:40)*  
Now for the basic operation we need. I think this is not the latest slide, but I need to go out and browse for the latest one.

**Dr. Ali Alsaffar** *(2:03)*  
'Cause it seems that I.

**Dr. Ali Alsaffar** *(2:06)*  
This is the one. Where is it?

---

## Part 2 — Best Case, Worst Case, Average Case

**Dr. Ali Alsaffar** *(49:16)*  
If the first number in the array is negative, how many comparisons we are going to have? Immediately when we start the loop, the first element we tested it is negative. Immediately the loop will stop.

**Dr. Ali Alsaffar** *(49:33)*  
And we return it true. So how many comparisons do we have? We have only one comparison, but this is 1 case. Now what if the array does not have any negative number? Then the loop will exhaust its iterations.

**Dr. Ali Alsaffar** *(49:51)*  
So it will test for the first number. This is the first comparison. It will test the second number not negative, third number not negative until the last one is not negative. So how many comparisons we are going to have? Number of iterations is N.

**Dr. Ali Alsaffar** *(50:07)*  
So we are going to have N comparisons. Again we are having different value. So fix the size but change the values. We have another case. What if the negative number is in the middle? How many comparisons?

**Dr. Ali Alsaffar** *(50:22)*  
What if it is at index three? What if it is index 4? We will have a case that needs to calculate later. We call it the average case. So here we have 3 cases.

**Dr. Ali Alsaffar** *(50:35)*  
One that is the basic operation executed the least — minimum.

**Dr. Ali Alsaffar** *(50:42)*  
The other case that the basic operation executed the most — worst, the other one is we take the average. So here is the conclusion and the first algorithm, the basic operation addition at line 4, which is this one.

**Dr. Ali Alsaffar** *(50:57)*  
Is always executed N times for every instance of the array A.

**Dr. Ali Alsaffar** *(51:04)*  
But in the second algorithm, the basic operation is the comparison.

**Dr. Ali Alsaffar** *(51:09)*  
And which is at line 3 and it is not always executed N times for every instance of the array. And here I'm asking why I have already given you the answer because if we have a negative at index 0.

**Dr. Ali Alsaffar** *(51:27)*  
We have one comparison and if we have no negative then we have N comparisons.

**Dr. Ali Alsaffar** *(51:36)*  
So these are called cases, and this will be step three in the analysis framework. Step one, you determine the input problem size. Step 2, you determine the basic operation. Step 3, you count how many times this basic operation is executed, and here you need to consider if there are cases or not.

**Dr. Ali Alsaffar** *(51:56)*  
So if the number of times.

**Dr. Ali Alsaffar** *(52:00)*  
The basic operation is executed depends not only on the input size but also on the input values. Then we have cases — worst case, best case and average case efficiency.

**Dr. Ali Alsaffar** *(52:14)*  
What is the worst case? The worst case efficiency of an algorithm is the efficiency when the basic operation is executed the maximum. So if we don't have a negative number, then the basic operation comparison will be executed the most.

**Dr. Ali Alsaffar** *(52:30)*  
Which is the maximum.

**Dr. Ali Alsaffar** *(52:33)*  
The second case, which is the best case, and this is the efficiency when the basic operation is executed the least with the minimum number of times and in our problem if the first number in the array is negative.

**Dr. Ali Alsaffar** *(52:50)*  
Finally, we will have an average case, and this is sometimes difficult to find for some algorithms. It is the average case. What if the negative number is at index one? What if it is at index two? At index three? So how many times the basic operation is executed?

**Dr. Ali Alsaffar** *(53:08)*  
We'll have different answers, so we take the average or the expected value, and we get a formula for the average case. For some algorithms we have every case. For others we have different efficiency or different time complexity for each case.

**Dr. Ali Alsaffar** *(53:28)*  
We have a formula for worst case, we have a formula for best case, and we have a formula for average case.

**Dr. Ali Alsaffar** *(53:37)*  
We will analyze or we will find cases as an example on the sequential search. We will show you how to find worst, best and average cases on popular example which is sequential search.

---

## Part 3 — Sequential Search Example

**Dr. Ali Alsaffar** *(53:55)*  
In the sequential search, the algorithm searches for a given value. We call it the key represented by K in an array we call it A. The size of this array is N.

**Dr. Ali Alsaffar** *(54:10)*  
And this sequential search returns the index of the first element in A that matches the key. Otherwise it returns -1 if the key is not found in the array. This is the algorithm. It looks exactly the same as the previous algorithm that tests for.

**Dr. Ali Alsaffar** *(54:30)*  
Negative number we have a loop. So we are looking for K, we have a loop. If we find K that is equal to A[i] we return the index. But if the element K is not in the array so the loop will keep testing testing for the value until it could not.

**Dr. Ali Alsaffar** *(54:50)*  
Find it. It will exit the loop and it returns -1 as an indication that the key was not found.

**Dr. Ali Alsaffar** *(55:00)*  
So where is the basic operation in this example? The basic operation is the comparison — this thing for A[i] equal to K.

**Dr. Ali Alsaffar** *(55:09)*  
Now is this basic operation frequency or the number of times it executes depends only on the size? If it depends only on the size, then we have every case. But if it depends not only on the size, it depends also on the values.

**Dr. Ali Alsaffar** *(55:28)*  
Of the input. Then we have cases and this is the case. If you fix the size and you change the values of the array, we will have different frequency for the comparison. What are these cases?

**Dr. Ali Alsaffar** *(55:45)*  
Let us give a symbol.

**Dr. Ali Alsaffar** *(55:48)*  
The time complexity by C(N). So the comparison A[i] equal to K is the basic operation. Now if the first element is equal to the key, so the algorithm will make only one comparison.

**Dr. Ali Alsaffar** *(56:04)*  
So we say that the formula for or the number of times for the basic operation is 1.

**Dr. Ali Alsaffar** *(56:10)*  
And if the element we are looking for is at the end or it is not in the array, how many comparisons the algorithm will make — it will make N comparisons from zero to N-1.

**Dr. Ali Alsaffar** *(56:27)*  
This is linear — Big Theta of N. So finding best case and finding worst case, only two cases, would be sometimes not difficult. But to find the average case then we have to go over all cases. What if the element is at index one?

**Dr. Ali Alsaffar** *(56:47)*  
How many times the basic operation executed? So we have many answers. We need to take the average or the expected value and this is what we will discuss in shallow next lecture on how to find the average case for some algorithms.

**Dr. Ali Alsaffar** *(57:03)*  
For the moment we have finished. Is there any question?

---

## Reference Notes — Key Takeaways

### Analysis Framework — The 3 Steps
1. **Determine the input/problem size** (N)
2. **Determine the basic operation** (the one contributing most to running time — typically in the innermost loop)
3. **Count how many times the basic operation executes** — and check: does it depend only on size, or also on input values?

### When Do Cases Arise?
- If the basic operation count depends **only on N** → every case is the same (one formula)
- If it depends on **N and the input values** → you get **three cases**:
  - **Best case:** basic operation executed the **minimum** number of times
  - **Worst case:** basic operation executed the **maximum** number of times
  - **Average case:** expected value across all possible inputs (harder to compute)

### Sequential Search — Worked Example
- **Algorithm:** Search for key K in array A of size N, return index or -1
- **Basic operation:** comparison `A[i] == K`
- **Best case:** K is at index 0 → C(N) = 1
- **Worst case:** K is at the end or not in array → C(N) = N → Theta(N)
- **Average case:** to be derived next lecture (expected value over all positions)

### Gap in Transcript
- There is a ~47 minute gap (2:06 to 49:16) where the detailed examples of basic operation identification and the detailed vs quick analysis worked examples were covered.
