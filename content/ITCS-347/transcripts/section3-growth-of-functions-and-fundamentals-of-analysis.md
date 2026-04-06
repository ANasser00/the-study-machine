# Section 3 — Growth of Functions (Finish) + Chapter 2: Fundamentals of Analysis (Start)

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Coverage:** End of asymptotic notations (limits method) → Beginning of Chapter 2 (analysis fundamentals, slide 6)

---

## Part 1 — Finishing Asymptotic Notations (Limits Method)

**Dr. Ali Alsaffar** *(0:00)*  
And today's lecture we will continue and we need to finish the asymptotic notations and efficiency classes. Just one announcement that for the quiz it will be postponed.

**Dr. Ali Alsaffar** *(0:19)*  
It will be postponed until for further notice because quizzes and algorithms, it's not like other subjects that it is easy to do it online. So we will find a way for the students to take the quiz, but don't leave the subject.

**Dr. Ali Alsaffar** *(0:37)*  
Just keep up, you know, reviewing the subject. Don't leave it until you have a quiz.

**Dr. Ali Alsaffar** *(0:46)*  
This is the last thing that we have covered in the previous lecture and let us continue. So we need to finish it and start Chapter 2. Now in this method if we want to find order.

**Dr. Ali Alsaffar** *(1:01)*  
Of any function.

**Dr. Ali Alsaffar** *(1:06)*  
Or if so, if you are given two functions, this is F of X and this is G of X and we want to know which one belongs to Big O or Big Omega or big Theta to the other one.

**Dr. Ali Alsaffar** *(1:21)*  
Or which one grows faster? We use limit. We divide both of them, or we divide.

**Dr. Ali Alsaffar** *(1:31)*  
Both of them F of X over G of X — order doesn't matter — and you look for the value when the limit for the variable X goes to infinity.

**Dr. Ali Alsaffar** *(1:44)*  
Now if we have.

---

## Part 2 — Chapter 2: Fundamentals of Analysis of Algorithm Efficiency

**Dr. Ali Alsaffar** *(51:04)*  
But if you are using C compiler then the machine code will be faster.

**Dr. Ali Alsaffar** *(51:13)*  
The difficulty of clocking the actual running time of the program. Now if you want to run your algorithm, definitely you will run it on an operating system. Either you have let's say on your mobile or Windows or Linux or iOS, but the operating system is not only.

**Dr. Ali Alsaffar** *(51:33)*  
Running your algorithm. It is running other algorithms in the background and it is switches between them. Yeah, it how well min algorithm min program is a program. So during your execution of your time, the operating system sometimes pause it.

**Dr. Ali Alsaffar** *(51:49)*  
Your work to serve other processes, to serve other problems. And now as you can see, I am moving the mouse and also the operating system is responsible for running the PowerPoint.

**Dr. Ali Alsaffar** *(52:05)*  
So these are two tasks should be done at once if your algorithm is running. So there is the third task. So while I move the mouse, now the operating system is stopping your algorithm, serving the mouse and then returns back. This time is also measured if you use it as.

**Dr. Ali Alsaffar** *(52:24)*  
And for measuring the running time. So these are the drawbacks, some of the drawbacks that we will not use seconds or milliseconds as a measurement for the running time. So what is the?

**Dr. Ali Alsaffar** *(52:39)*  
What is the metric that we should use for?

**Dr. Ali Alsaffar** *(52:46)*  
Measuring the running time. Here it says that we need to have a metric that does not depend on these extraneous factors. Extraneous means that they generate errors.

**Dr. Ali Alsaffar** *(52:59)*  
This will be the number of steps. As you remember we discussed that before on the growth of functions. So to find the running time, basically find how many steps this algorithm is taking.

**Dr. Ali Alsaffar** *(53:15)*  
And from these steps you can find the actual running time if you know the exact number of steps that computer is making per second. So we will have two analysis and the time will not allow us to discuss these two.

**Dr. Ali Alsaffar** *(53:32)*  
We will have detailed analysis, so we will count how many steps the algorithm is making for each operation. So if we have multiplication, if we have division, if we have comparison and so on, then we make a table.

**Dr. Ali Alsaffar** *(53:47)*  
We go over the algorithm and we count each of these operations how many times they are executed. Some of them will depend on the problem size. If you have the operation inside the loop and the loop goes from one to N, so the number of execution of this operation will be a formula depends on N.

**Dr. Ali Alsaffar** *(54:08)*  
At the end, when we add all of these operations, we will have a formula in terms of the problem size.

**Dr. Ali Alsaffar** *(54:15)*  
The second method which is the quick analysis. As you will see that for the detail analysis for some operations there is no need to count how many times they are executed and we will see that when we go over.

**Dr. Ali Alsaffar** *(54:31)*  
Examples and the quick analysis. You don't count all operations how many times they are executed. You focus on one that you think that this one is taking the execution of the algorithm that it is spending most of the time.

**Dr. Ali Alsaffar** *(54:48)*  
Over this operation, it's called the basic operation. So we identify the most important operation called basic operation contributing the most to the total running time. We focus on this operation and we count how many times it is executed.

**Dr. Ali Alsaffar** *(55:08)*  
Focus on one operation, not all operations. We focus only on one and it will give the same result.

**Dr. Ali Alsaffar** *(55:22)*  
And for comparing these two methods.

**Dr. Ali Alsaffar** *(55:26)*  
The detailed analysis for some problems is difficult and it is unnecessary to count all operations, but for the quick analysis it will be more practical. Here I'm just given an example that if you have nested loops where to find the basic operation, the basic operation basically.

**Dr. Ali Alsaffar** *(55:46)*  
You will find it in the innermost loop, so you will go deep level into the nested loops. You will find the basic operation there. Why? Because it will be executed the most during the time of the algorithm.

**Dr. Ali Alsaffar** *(56:03)*  
Now I think we will stop here. We have only a few minutes to finish the lecture, so we will stop here. So we stopped at slide 6.

**Dr. Ali Alsaffar** *(56:19)*  
So slide 6. I'll put a note for myself slide.

**Dr. Ali Alsaffar** *(56:26)*  
6.

**Dr. Ali Alsaffar** *(56:30)*  
Chapter 2. Is there any question?

---

## Reference Notes — Key Takeaways from This Lecture

### Chapter Mapping

- **Part 1** (0:00–1:44) — Tail end of **Growth of Functions** — the limits method for comparing Big O / Big Omega / Big Theta. Matches slide `Chapter 2-Growth of Functions.pptx`.
- **Part 2** (51:04–56:30) — Start of **Chapter 2: Fundamentals of Analysis of Algorithm Efficiency**, stopping at slide 6. Matches slide `Chapter 2-Fundamentals of Analysis V2.pptx` and exercise `ITCS347_Exercises_2_Fundamentals_of_the_Analysis_of_Algorithm_Efficiency.pdf`.

### Dr. Alsaffar's Problem-Solving Approach

#### 1. Limits Method for Comparing Functions
- Given two functions f(x) and g(x), compute **lim(x->infinity) f(x)/g(x)**
- The result of the limit tells you the relationship:
  - If limit = 0 → f is O(g) (f grows slower)
  - If limit = constant (c > 0) → f is Theta(g) (same growth rate)
  - If limit = infinity → f is Omega(g) (f grows faster)
- He emphasizes: "order doesn't matter" when setting up the fraction

#### 2. Why Not Measure Wall-Clock Time?
- Different hardware speeds (compiler choice matters — C is faster)
- OS multitasking: the OS pauses your program to serve other processes (mouse, PowerPoint, background tasks)
- These "extraneous factors" introduce measurement errors
- **Solution:** Count the **number of steps**, not seconds/milliseconds

#### 3. Two Methods for Analyzing Algorithm Efficiency

**Detailed Analysis:**
- Count every operation type (multiplication, division, comparison, etc.)
- Build a table: for each operation, how many times it executes
- Operations inside loops depend on N (problem size)
- Sum all operations → formula in terms of N
- Drawback: tedious and often unnecessary

**Quick Analysis (Preferred):**
- Identify the **basic operation** — the one that contributes most to total running time
- Count only that one operation
- Gives the same asymptotic result as detailed analysis
- More practical for most problems

#### 4. Finding the Basic Operation
- In nested loops, the basic operation is in the **innermost loop**
- Why? Because it gets executed the most times during the algorithm's run

### Gap in Transcript
- There is a ~49 minute gap (1:44 to 51:04) where worked examples of the limits method were likely covered. If the full recording is available, that middle section would contain the step-by-step solving process.
