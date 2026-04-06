# Section 3 — Week 5 Lecture 2 — Chapter 2: If-Else Analysis & Recursion Intro

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 11th, 2026  
**Coverage:** Chapter 2 continued — Analyzing if-else inside loops (take max of branches), transition to recursion (parameter updates, stopping conditions, pre-work vs post-work)

---

## Part 1 — Framework Recap & Program Constructs

**Dr. Ali Alsaffar** *(0:03)*  
Morning class. This is Doctor Al Safar, ITCS 347 Design and Analysis of Algorithms, Section 3.

**Dr. Ali Alsaffar** *(0:11)*  
8.

**Dr. Ali Alsaffar** *(0:13)*  
We are still in Chapter 2. We are now building a framework for analysis and so at the end we are going to build a guideline that we need to follow whenever we want to whenever we want to analyze an algorithm.

**Dr. Ali Alsaffar** *(0:30)*  
Just to remind you about these steps or guidelines, first we discussed how to find the problem size because the time complexity will be expressed in terms of this parameter. That can determine the basic operation and we will follow quick analysis.

**Dr. Ali Alsaffar** *(0:49)*  
Third, you specify the time of analysis, the type of analysis. I mean whether you have cases or you have every case.

**Dr. Ali Alsaffar** *(0:59)*  
Next step as you find the time complexity and this is what we have done at the end of the last lecture, going over some basic program constructs like selection, loops and so on. And then at the end we find the growth rate.

**Dr. Ali Alsaffar** *(1:17)*  
Or the asymptotic the growth rate of this function as the running time of the algorithm. We are still we are still practicing on how to analyze program constructs.

**Dr. Ali Alsaffar** *(1:32)*  
The last lecture let me show you where did we stop last lecture. This is the discussion of our last lecture. We discussed if you have a for loop.

**Dr. Ali Alsaffar** *(1:44)*  
Simple for loop.

**Dr. Ali Alsaffar** *(1:47)*  
That the iterator is simple, it is either increased or decreased. So the number of iterations if you want to find for this for loop can be found by using summation and the value of the summation is 1. Basically.

---

## Part 2 — Analyzing If-Else Inside Loops

**Dr. Ali Alsaffar** *(50:52)*  
For this part, if you go back on top of the.

**Dr. Ali Alsaffar** *(51:04)*  
The 3K plus one or 3K + 2. So we have two choices. So we need to solve the problem in two steps and find which one is the appropriate one. So I will leave this one. Again, this is an optional. So you have you've got the idea on how to do the analysis if we have if-else inside a for loop.

**Dr. Ali Alsaffar** *(51:24)*  
Then you need to find the in both cases the true part and false part, put them together and find the maximum. Sometimes it is obvious that one of the parts is taking too much time than the other one. For example if we have for the if part which is the true.

**Dr. Ali Alsaffar** *(51:41)*  
We have a loop, but for the else we don't have a loop like in our example. So you can figure out that the true part takes more time than the else part, but in our example we're not considering all values of the outer loop.

**Dr. Ali Alsaffar** *(51:57)*  
We are considering only part of it, which means I equal to 3, 6. So we are not considering all numbers. So we cannot guarantee that the true part will take more time than the else part. Therefore we have to do the analysis, find the true part complexity, find the false part complexity and take the maximum.

**Dr. Ali Alsaffar** *(52:17)*  
Now from this example we finished analyzing many examples on program constructs for loops. Now we will turn to recursion. So in recursion I need to switch.

**Dr. Ali Alsaffar** *(52:32)*  
To the slides. So for recursion, let me stop the.

**Dr. Ali Alsaffar** *(52:41)*  
Let me go for the slides for recursion.

**Dr. Ali Alsaffar** *(52:51)*  
Just give me a second for change sharing.

**Dr. Ali Alsaffar** *(53:10)*  
But do you see?

**Dr. Ali Alsaffar** *(53:14)*  
I'm sharing now.

**Dr. Ali Alsaffar** *(53:21)*  
Let me share again.

**Dr. Ali Alsaffar** *(53:26)*  
Do you see anything?

**Dr. Ali Alsaffar** *(53:30)*  
It's still not sharing. Just hold on a second.

**Dr. Ali Alsaffar** *(53:37)*  
Yeah, now it's coming.

---

## Part 3 — Introduction to Recursion

**Dr. Ali Alsaffar** *(53:43)*  
Now for the recursion part.

**Dr. Ali Alsaffar** *(53:48)*  
First what we will do, we will just explain why recursive is useful for some problems and how it works. So we will explain first how to pass parameters if we have arrays to recursive functions or algorithms.

**Dr. Ali Alsaffar** *(54:06)*  
And then we will explain, we will give some motivated example on how to apply recursion and then we will show you a tracing of recursive algorithms and then we will come to the part for analysis.

**Dr. Ali Alsaffar** *(54:21)*  
So I will play the video for you. So I will play the video.

**Dr. Ali Alsaffar** *(54:26)*  
To follow the lecture.

**Dr. Ali Alsaffar** *(55:08)*  
Recursion is a technique used to solve bigger problems by breaking them into smaller, similar problems. A process in which a function calls itself directly or indirectly is called recursion.

**Dr. Ali Alsaffar** *(55:24)*  
The corresponding function is called a recursive function. For some problems, recursion is very useful for developing efficient algorithms, and to others it might add more complexity and overhead calculations with no improvement to efficiency.

**Dr. Ali Alsaffar** *(55:43)*  
In the introduction lesson, we explained how recursion algorithms work and how they are implemented by a conditional statement.

**Dr. Ali Alsaffar** *(55:51)*  
Remember we said that you have to focus on 2 important points if you want to write a recursive algorithm. First is that in the recursive call you have to supply a parameter different from the parameter received by the algorithm. I mean the parameter must be updated.

**Dr. Ali Alsaffar** *(56:10)*  
When the algorithm is called recursively, otherwise the algorithm will never stop and will have a Stack Overflow error.

**Dr. Ali Alsaffar** *(56:19)*  
As an example, if the input to the algorithm is N, as shown in this example, we may call the algorithm recursively with a parameter N - 1, or we might update the parameter by N + 1 or N * 2.

**Dr. Ali Alsaffar** *(56:36)*  
Or N divided by two and so on. Depends on the problem you are solving.

**Dr. Ali Alsaffar** *(56:42)*  
And the second point to focus is to determine the stopping condition to stop the recursive calls.

**Dr. Ali Alsaffar** *(56:49)*  
So in the if part of the conditional statement inside the body of the recursive algorithm, you specify the stopping condition and the else part you do the recursion.

**Dr. Ali Alsaffar** *(57:01)*  
Remember that all operations executed before the recursive call are called pre-work operations and all operations executed after the recursive call are called post-work operations.

**Dr. Ali Alsaffar** *(57:16)*  
Before showing you how to find the time complexity of a recursive algorithm, first we would like to talk briefly how problems are solved recursively and how the recursive algorithms are traced. We will also present couple motivated examples as review on how to write recursive algorithms.

**Dr. Ali Alsaffar** *(57:34)*  
After that we will focus on measuring time complexity of recursive algorithms. So let us start.

**Dr. Ali Alsaffar** *(57:45)*  
I think we are reaching end of the class, so we have only two minutes, so I will share the attendance sheet so you can take attendance.

**Dr. Ali Alsaffar** *(58:04)*  
For those who did not have a chance to take attendance.

**Dr. Ali Alsaffar** *(58:12)*  
Please take attendance.

**Dr. Ali Alsaffar** *(58:17)*  
Lima Ahad attendance.

**Dr. Ali Alsaffar** *(58:28)*  
Anybody needs manual attendance?

**Dr. Ali Alsaffar** *(58:46)*  
OK, then if all has taken attendance and again still we need to find a way to take quizzes and the midterm is approaching, so I don't know how we will take the.

**Dr. Ali Alsaffar** *(59:02)*  
The exam. We need the department to give us the policy on what to do for the exams, but until we receive any instructions, we will inform you about that. I'm thinking about giving you a quiz online, but be prepared for.

**Dr. Ali Alsaffar** *(59:22)*  
That maybe next week, so don't leave the subject any unreviewed. Review the subject, go over the material we have covered so far. First, maybe I will prepare a homework so that you can start with.

**Dr. Ali Alsaffar** *(59:37)*  
And then we will see how we can take the first quiz. If there is no question, then good luck. We wish you the best.

---

## Reference Notes — Key Takeaways

### Analyzing If-Else Inside Loops
- When you have an `if-else` inside a `for` loop, analyze **both branches separately**
- Find T(N) for the **true part** and T(N) for the **false part**
- The time complexity is the **maximum** of the two: T(N) = max(T_true, T_false)
- Sometimes it's obvious (e.g., true part has a loop, else part doesn't → true part dominates)
- But if only some iterations enter the true branch (e.g., only when i is divisible by 3), you **cannot assume** the true part dominates — you must compute both and take max

### Recursion — Two Critical Points
1. **Parameter must change** in the recursive call — otherwise infinite recursion → Stack Overflow
   - Examples: call with N-1, N+1, N*2, N/2 (depends on the problem)
2. **Stopping condition** (base case) — specified in the `if` part of the conditional
   - `if` → stopping condition (base case)
   - `else` → recursive call

### Pre-work vs Post-work Operations
- **Pre-work:** operations executed **before** the recursive call
- **Post-work:** operations executed **after** the recursive call
- This distinction matters for tracing and analysis

### Roadmap for Recursion (upcoming lectures)
1. How to pass parameters (especially arrays) to recursive functions
2. Motivated examples of recursive algorithms
3. Tracing recursive algorithms
4. Finding time complexity of recursive algorithms

### Gap in Transcript
- ~49 minute gap (1:47 to 50:52) where worked examples of analyzing program constructs (loops with if-else) were covered.

### Announcements
- Quiz possibly next week (online format under consideration)
- Midterm approaching — department policy on exam format pending
- Homework may be assigned as preparation
