# Section 3 — Week 6 Lecture 1 — Chapter 2: Recursion Deep Dive & Recurrence Relations

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 16th, 2026  
**Coverage:** Chapter 2 continued — Recursion: passing parameters, solving by reducing problem size, tracing, intro to recurrence relations and identifying basic operation in recursive algorithms

---

## Part 1 — Announcements & Framework Recap

**Dr. Ali Alsaffar** *(0:13)*  
Yes, this is Doctor Al Safar.

**Dr. Ali Alsaffar** *(0:19)*  
Introduction to Design and Analysis of Algorithms Section 3.

**Dr. Ali Alsaffar** *(0:24)*  
I would like to make this announcement probably next week. No, next week. It's not probably it is confirmed that next week after the Eid holiday we will have our first quiz.

**Dr. Ali Alsaffar** *(0:40)*  
Now for the moment it will be online. It will be on a growth of functions. I will announce for that. I have uploaded on a blackboard mock quiz.

**Dr. Ali Alsaffar** *(0:57)*  
You can practice on this mock quiz. It includes the material that will come in the quiz.

**Dr. Ali Alsaffar** *(1:14)*  
We will see regarding the test how we will do it. Anyhow, we will have it either either online.

**Dr. Ali Alsaffar** *(1:30)*  
OK, what we will do today? Today we will continue our lecture on design or on analysis of algorithms. We are building a framework. We are building a guideline that we need to follow whenever we want to analyze an algorithm.

**Dr. Ali Alsaffar** *(1:48)*  
In this guideline, first step you determine the problem size because you will express the time complexity using this parameter. Second step you determine the basic operation. Third you determine the case of the analysis or efficiency.

**Dr. Ali Alsaffar** *(2:06)*  
Do you have every case or you have cases? Next, as you analyze the algorithm, you come up with a time complexity equation. You find the growth rate of this equation.

**Dr. Ali Alsaffar** *(2:19)*  
We showed you how to analyze basic program concept constructs like loops and last lecture we stopped at recursion. Whenever you have recursive algorithm, how to analyze recursive algorithm?

**Dr. Ali Alsaffar** *(2:35)*  
In the beginning what we will do, we will just start a quick introduction on why recursion is used and what is the purpose of it, and then we will show you how to trace recursive algorithms.

**Dr. Ali Alsaffar** *(2:51)*  
Basically, if you have one call or if you have more than one call recursively, how to trace the algorithm and then we will show you how to analyze our recursive algorithms, how to come up with time complexity, how to count how many times the basic operation is executed when we have.

**Dr. Ali Alsaffar** *(3:10)*  
Recursion. In the beginning you will see that for some examples we will talk briefly about passing parameters, because remember that for recursive algorithms the algorithm is calling itself and the parameter should change.

**Dr. Ali Alsaffar** *(3:26)*  
So for this parameter what you should supply. So you have to be careful because in every recursive call the parameters are saved in the memory. So if you are passing array, make sure that this array is not always saved in every call and we will show you that in the.

**Dr. Ali Alsaffar** *(3:44)*  
In the lecture.

**Dr. Ali Alsaffar** *(3:48)*  
We will share now the lecture.

**Dr. Ali Alsaffar** *(3:52)*  
Again, the lecture that we will address is the same lecture that is recorded. So instead of repetition, I will play the recorded lecture and in case you have any question, just speak up.

**Dr. Ali Alsaffar** *(4:07)*  
And I will pause the video, take your question and goes back.

---

## Part 2 — Recursion Fundamentals (Video Lecture)

**Dr. Ali Alsaffar** *(4:20)*  
In the introduction lesson, we explained how recursion algorithms work and how they are implemented by a conditional statement.

**Dr. Ali Alsaffar** *(4:29)*  
Remember we said that you have to focus on 2 important points if you want to write a recursive algorithm. First is that in the recursive call you have to supply a parameter different from the parameter received by the algorithm. I mean the parameter must be updated.

**Dr. Ali Alsaffar** *(4:47)*  
When the algorithm is called recursively, otherwise the algorithm will never stop and will have a Stack Overflow error.

**Dr. Ali Alsaffar** *(4:56)*  
As an example, if the input to the algorithm is N, as shown in this example, we may call the algorithm recursively with the parameter N - 1, or we might update the parameter by N + 1 or N multiplied by two.

**Dr. Ali Alsaffar** *(5:13)*  
Or N divided by two and so on. Depends on the problem you are solving.

**Dr. Ali Alsaffar** *(5:19)*  
And the second point to focus is to determine the stopping condition to stop the recursive calls.

**Dr. Ali Alsaffar** *(5:27)*  
So in the if part of the conditional statement inside the body of the recursive algorithm, you specify the stopping condition and the else part you do the recursion.

**Dr. Ali Alsaffar** *(5:38)*  
Remember that all operations executed before the recursive call are called pre-work operations and all operations executed after the recursive call are called post-work operations.

**Dr. Ali Alsaffar** *(5:53)*  
Before showing you how to find the time complexity of a recursive algorithm, first we would like to talk briefly how problems are solved recursively and how the recursive algorithms are traced. We will also present couple motivated examples as a review on how to write recursive algorithms.

**Dr. Ali Alsaffar** *(6:12)*  
After that we will focus on measuring time complexity of recursive algorithms. So let us start.

**Dr. Ali Alsaffar** *(6:21)*  
Recursive algorithms solve a larger problem by applying themselves to a part of the problem and then using the solution of that part to solve the larger problem. So what do we mean by part of the problem?

**Dr. Ali Alsaffar** *(6:37)*  
We mean in the recursive calls, the algorithm must supply data of sizes smaller than the size of the received data.

**Dr. Ali Alsaffar** *(6:46)*  
Let me show you how by an example.

---

## Part 3 — Analyzing Recursive Algorithms: Recurrence Relations

**Dr. Ali Alsaffar** *(57:09)*  
The question is asking for the time complexity without specifying whether a detailed or a quick analysis is required. In this case, assume that a quick analysis is expected by default, so start by identifying the basic operation.

**Dr. Ali Alsaffar** *(57:26)*  
Then construct T(N) the recurrence relation for the time complexity based on that operation.

**Dr. Ali Alsaffar** *(57:35)*  
To determine the basic operation in this algorithm, consider which operations are frequently executed in each call of the algorithm. Every time the algorithm is invoked or called, it first evaluates the if condition. This means a comparison is performed in every call.

**Dr. Ali Alsaffar** *(57:55)*  
While the comparison happens in each call, it may not be the best candidate for the basic operation because the condition is usually false and only evaluates to true once, so when execution goes to the else block.

**Dr. Ali Alsaffar** *(58:11)*  
There might be operations in the else block that occur more frequently or more costly to execute than comparison.

**Dr. Ali Alsaffar** *(58:19)*  
Now let us — I am pausing the video. We are almost running out of time so I will put the attendance website so that you can take attendance.

**Dr. Ali Alsaffar** *(58:34)*  
Just give me a few seconds.

**Dr. Ali Alsaffar** *(58:42)*  
So please take attendance.

**Dr. Ali Alsaffar** *(58:45)*  
And if there is any question, please let me know. I will stop the recording.

---

## Reference Notes — Key Takeaways

### Recursion Fundamentals (Reinforced from Last Lecture)
1. **Parameter must change** in each recursive call → otherwise Stack Overflow
   - Common updates: N-1, N+1, N*2, N/2
2. **Stopping condition** (base case) in the `if` part; recursion in the `else` part
3. **Pre-work** = operations before the recursive call; **Post-work** = operations after

### Key Concept: Reducing Problem Size
- Recursive algorithms solve a **larger problem** by applying themselves to a **smaller part**
- In each recursive call, the data size must be **smaller** than what was received
- This is what guarantees termination (along with the base case)

### Memory Warning: Passing Parameters
- Every recursive call saves parameters in memory (stack frames)
- If passing an **array**, be careful not to copy the entire array each call
- Pass by reference or use index bounds instead of creating new arrays

### Analyzing Recursive Algorithms — His Method
1. If the question doesn't specify detailed or quick analysis → **assume quick analysis**
2. **Identify the basic operation** — not necessarily the if-condition comparison:
   - The comparison in the `if` happens every call but is usually true only once (base case)
   - Look at operations in the `else` block — they may execute more frequently or be more costly
3. **Construct T(N)** — the recurrence relation for the time complexity based on the basic operation
4. Solve the recurrence to get a closed-form formula

### Announcements
- **Quiz 1** confirmed for after Eid holiday — topic: **Growth of Functions**
- Mock quiz uploaded to Blackboard for practice
- Quiz format: online (for now)

### Gap in Transcript
- ~50 minute gap (6:46 to 57:09) where recursion examples, parameter passing demonstrations, tracing of recursive algorithms, and motivated examples were covered.
