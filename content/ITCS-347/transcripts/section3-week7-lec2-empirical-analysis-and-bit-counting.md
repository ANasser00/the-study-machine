# Section 3 — Week 7 Lecture 2 — Chapter 2: Empirical Analysis & Bit Counting Comparison

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 25th, 2026  
**Coverage:** Chapter 2 wrap-up — Empirical analysis (counting ops vs timing, averaging, graph shapes), recursive vs non-recursive bit counting (why log2(N) vs log2(N)+1)

---

## Part 1 — Quiz Logistics

**Dr. Ali Alsaffar** *(0:03)*  
Is Dr. Al Safar ITCS 347 Section 3. Before we start the lecture, just to ensure that everybody has.

**Dr. Ali Alsaffar** *(0:14)*  
Yeah.

**Dr. Ali Alsaffar** *(0:15)*  
Received the announcement on Blackboard. Our first quiz will be on Sunday, this coming Sunday in the afternoon and it will be on Blackboard. It will be only on growth functions.

**Dr. Ali Alsaffar** *(0:33)*  
It will be multiple choice, second true and false. Third you need to write a solution and it will be around 7 minutes. So you have to finish as soon as possible. Get the practice on the mock quiz.

**Dr. Ali Alsaffar** *(0:51)*  
Or mock test that I have provided. Watch the recorded video for demonstration on how to answer it, either when you want to directly type the answer or if you want to include a picture of your answer.

**Dr. Ali Alsaffar** *(1:06)*  
You need to turn on your camera as an invigilation. So you have to be in a place suitable, well dressed.

**Dr. Ali Alsaffar** *(1:22)*  
And yeah, so and the OK, so that you need to show yourself that you are taking the test. Maybe we will ask you to do this on teams.

**Dr. Ali Alsaffar** *(1:38)*  
You need to use a laptop so that you log in into Teams to show yourself and you need to go to Blackboard to take the quiz. Or we can use Lockdown browser so you can use any one device.

**Dr. Ali Alsaffar** *(1:54)*  
And again, you need to use the laptop so that you can make the responders and monitor you. At the same time, the browser will be locked, so you can only answer the questions on the blackboard. So we will see the appropriate way.

**Dr. Ali Alsaffar** *(2:10)*  
And maybe the test will use Lockdown browser, but for the midterm I'm planning to use Microsoft Teams. So get the practice, make sure that you're all set. So if you have any technical problem, I'm not in front of you to help you on how to answer this technical issue.

---

## Part 2 — Empirical Analysis of Algorithms

**Dr. Ali Alsaffar** *(1:01:40)*  
And we would like to see what is the time complexity for this algorithm. So we can run it on one computer but with different inputs and you know that the time is affected by some factors. So we can run this for the same input. We can run it more than one time and we take average and we'll check about this in a moment.

**Dr. Ali Alsaffar** *(1:01:59)*  
So you have two choices. Either you count number of basic operations and here you need to put a counter in front of each basic operation and at the end you print this counter and you will have the number of times of the basic operation. The other way is to decide on the time.

**Dr. Ali Alsaffar** *(1:02:16)*  
So you decide on the characteristics of the input sample, prepare a program implementing implementation for the algorithm. Either you can use Java or C++ or whatever, you just need to implement it.

**Dr. Ali Alsaffar** *(1:02:32)*  
And generate a sample of inputs and then run the algorithm on the samples input and record the data observed and then at the end you analyze the data obtained.

**Dr. Ali Alsaffar** *(1:02:46)*  
What are the alternatives that we should do in here? As you said, either we count or we find the time.

**Dr. Ali Alsaffar** *(1:02:56)*  
So the first alternative is to count the basic operation. So you insert the variable into the program to count the number of basic operations.

**Dr. Ali Alsaffar** *(1:03:05)*  
Alternative 2, you use system call that is provided by the operating system that will record the time when you just start the algorithm, that the algorithm executes. At the end you record the time again.

**Dr. Ali Alsaffar** *(1:03:21)*  
Then you take the difference, it will give you the amount of time elapsed for executing the algorithm and we will do this and we will show you how to do this using Java. In sha Allah next lecture we will have an experiment on our first algorithm on brute force.

**Dr. Ali Alsaffar** *(1:03:37)*  
Which is the selection sort. We will show you how to do this implementation and how to do the empirical analysis on that algorithm.

**Dr. Ali Alsaffar** *(1:03:48)*  
But this method has many drawbacks as the obtained time is not only running for the program. So the solution is that you take input sizes that can change or you can make random input and at the same time the same input size could be tested many times and we take the average. For example if you are.

**Dr. Ali Alsaffar** *(1:04:08)*  
Sorting an array of size 100, the same array of size 100, same values. You run it for example 10 times and you record the time. Take the average because for every run we don't expect that we have exact.

**Dr. Ali Alsaffar** *(1:04:24)*  
A number of seconds elapsed for the execution of the algorithm.

**Dr. Ali Alsaffar** *(1:04:30)*  
After that you draw after taking the samples of the output, you draw the graph of the time complexity. Depends on the shape. If you have this shape then this is logarithm. If you have this shape it is a quadratic. If it is this shape then it is linear and so on.

**Dr. Ali Alsaffar** *(1:04:47)*  
In sha Allah the next lecture when we discuss the first design technique which is the brute force and when we present the selection sort after presenting the analysis, mathematical analysis of the selection sort, we will show you how practically we can implement it and measure its running time using empirical.

**Dr. Ali Alsaffar** *(1:05:06)*  
Analysis. Now is there any question?

---

## Part 3 — Recursive vs Non-Recursive Bit Counting: Why the +1 Difference

**Dr. Ali Alsaffar** *(1:05:14)*  
Now let us go back to our question that we have presented in the lecture. Why for non-recursive algorithm for determining the number of bits of a number, the equation was log 2 of N + 1.

**Dr. Ali Alsaffar** *(1:05:30)*  
But for recursive version we have only log 2 of N. Some of you have mentioned that because of the comparison that we need to add 1 for the exit. That is correct. But I have already asked you, are we looking for the comparison as the basic operation?

**Dr. Ali Alsaffar** *(1:05:49)*  
So the answer is there. Anybody has any answer different than what it is written by other students?

**Dr. Ali Alsaffar** *(1:06:02)*  
Why for recursion the formula is log 2 of N, non-recursion log 2 of N + 1? There's a plus one. Some said because we are counting the exit operation.

**Dr. Ali Alsaffar** *(1:06:15)*  
Then we are comparing the exit operation.

**Dr. Ali Alsaffar** *(1:06:20)*  
What's the relationship?

**Dr. Ali Alsaffar** *(1:06:23)*  
Yes?

**Dr. Ali Alsaffar** *(1:06:29)*  
OK, the answer is.

**Dr. Ali Alsaffar** *(1:06:31)*  
For the nonrecursive algorithm, what was the basic operation? It was comparison. So you were counting number of comparisons. Now for the recursive algorithm, what was the basic operation? It was multiplication.

**Dr. Ali Alsaffar** *(1:06:48)*  
You were counting multiplication, not comparison. So now if you go to the recursive analysis, recursive algorithm analysis, notice for the initial value. For the initial value we don't have any multiplication, we have 0.

**Dr. Ali Alsaffar** *(1:07:04)*  
But if you are counting comparison then you will have one. Therefore at the end the formula will be the initial value plus log 2 of N so you will have log 2 of N + 1. So the difference is because in the non-recursive algorithm you were counting comparisons.

**Dr. Ali Alsaffar** *(1:07:20)*  
But for recursive algorithm you were counting multiplication. So this was the answer. Now I need to check attendance. OK, so I will let me just.

**Dr. Ali Alsaffar** *(1:07:38)*  
I will go now. We don't see what I'm doing. I will go to — this is.

**Dr. Ali Alsaffar** *(1:07:45)*  
Let me just go to — give me a few seconds. I will stop recording.

---

## Reference Notes — Key Takeaways

### Empirical Analysis — Two Alternatives

| Alternative | Method | How |
|-------------|--------|-----|
| 1. Count operations | Insert a counter variable before the basic operation, print at end | Exact count, no OS noise |
| 2. Measure time | Use system calls to record start/end time, take the difference | Real-world timing, but noisy |

### Empirical Analysis — Steps (for Alternative 2)
1. **Decide input characteristics** — size, distribution, type
2. **Implement the algorithm** (Java, C++, etc.)
3. **Generate sample inputs** — varying sizes, random values
4. **Run multiple times per input size** — same input, run 10+ times, take the **average** (OS noise varies per run)
5. **Record and plot** — draw graph of time vs input size
6. **Match the curve shape** to a known growth rate:
   - Logarithmic curve → O(log N)
   - Linear curve → O(N)
   - Quadratic curve → O(N^2)

### Preview: Next Lecture
- Chapter 3: Brute Force — selection sort
- Will do both mathematical analysis AND empirical analysis (Java implementation with timing)

### Recursive vs Non-Recursive Bit Counting — The +1 Mystery

**Problem:** Count number of bits in a number N

| Version | Basic Operation | Formula | Why |
|---------|----------------|---------|-----|
| Non-recursive | **Comparison** (loop condition) | log2(N) + 1 | Loop checks condition one extra time to exit |
| Recursive | **Multiplication** | log2(N) | Base case has 0 multiplications (initial value = 0) |

**Key insight:** The +1 difference is NOT because of "the exit comparison." It's because the two versions count **different basic operations**:
- Non-recursive counts **comparisons** → the base/initial value includes 1 (the final comparison to exit)
- Recursive counts **multiplications** → the base case has 0 multiplications

**Lesson:** The choice of basic operation directly affects the formula. Same algorithm logic, different basic operation = different constant in the result.

### Announcements
- **Quiz 1:** This Sunday afternoon, Blackboard, ~7 minutes
- Format: multiple choice + true/false + written solution
- Camera on (Teams or Lockdown browser)
- Midterm will use Microsoft Teams

### Gap in Transcript
- ~59 minute gap (2:10 to 1:01:40) where the main lecture content was covered (likely finishing element uniqueness analysis, more recursion examples, and transition to empirical analysis).
