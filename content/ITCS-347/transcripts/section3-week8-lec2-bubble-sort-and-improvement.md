# Section 3 — Week 8 Lecture 2 — Chapter 3: Brute Force — Bubble Sort & Improvement

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** April 1st, 2026  
**Coverage:** Chapter 3 continued — Bubble sort implementation (swap flag, range reduction), improved bubble sort (early termination), complexity analysis, brute force debate

---

## Part 1 — Midterm Exam Instructions

**Dr. Ali Alsaffar** *(0:00)*  
In class, this is Doctor Alice Safar, ITCS 347 Introduction to the Design and Analysis of Algorithms, Section 3.

**Dr. Ali Alsaffar** *(0:14)*  
Before we start the lecture, I would like to talk briefly about the exam that is scheduled next week on April 6.

**Dr. Ali Alsaffar** *(0:28)*  
The time I did not specify in the announcement, we will make the time in the evening which will be at three o'clock 3:00 PM. It will be for one hour. Now I would like to talk about the instructions.

**Dr. Ali Alsaffar** *(0:45)*  
And now I am recording for those who join late the class session or if are absent, they need to follow the instructions that I will tell you now. So if you have WhatsApp group, please tell the students.

**Dr. Ali Alsaffar** *(1:04)*  
To go to the recorded lecture for today to listen to the announcement that I will make. Also I will write the announcement and I will give you the steps on how to take the exam.

**Dr. Ali Alsaffar** *(1:18)*  
You will take the exam using Blackboard with Lockdown Browser and Respondus. So you follow the sample test. I hope that you have taken the sample test exactly the same steps that you will do in the sample test you will do in the exam.

**Dr. Ali Alsaffar** *(1:35)*  
Now if you have any technical issues, you have to solve it. You will not be able to take the exam if the webcam is not working. If you don't have good laptop, I mean it is the student.

**Dr. Ali Alsaffar** *(1:51)*  
Responsibility to provide, you know, an appropriate environment for taking the test. Make sure to restart the computer.

**Dr. Ali Alsaffar** *(2:04)*  
Make sure to restart the browser whenever you have a problem and try to connect to a router that it's not connected by many users.

**Dr. Ali Alsaffar** *(2:20)*  
And it is preferable if you have fiber optics at home, you join with Wi-Fi.

---

## Part 2 — Bubble Sort Implementation

**Dr. Ali Alsaffar** *(1:00:04)*  
As soon as a swap occurs, we set the swap flag to true, so we write swap.

**Dr. Ali Alsaffar** *(1:00:14)*  
Is set to true.

**Dr. Ali Alsaffar** *(1:00:18)*  
So whenever the algorithm makes a swap, setting the flag to true serves as a signal to the while loop that the array needs to be scanned for another pass.

**Dr. Ali Alsaffar** *(1:00:30)*  
After exiting the for loop, the next range for comparing adjacent elements must be reduced by one element, and this can be done by incrementing the value of I. When we exit the for loop, we increase the value by 1.

**Dr. Ali Alsaffar** *(1:00:45)*  
31.

**Dr. Ali Alsaffar** *(1:00:47)*  
And this completes the implementation of the algorithm and the conclusion. Whenever the algorithm makes a swap to any adjacent element, a flag is set to the while loop to continue scanning the array again and if no swap occur.

**Dr. Ali Alsaffar** *(1:01:03)*  
This is an indication that the array is sorted and no need to continue and the loop stops.

---

## Part 3 — Improved Bubble Sort: Complexity Analysis

**Dr. Ali Alsaffar** *(1:01:13)*  
Even though the improvement helps with sorted or nearly sorted data, the worst case and even the average case remains Big Theta of N square. If the list is in reverse order or if the elements are randomly arranged, the algorithm still performs about Big Theta of N square comparisons and many swaps.

**Dr. Ali Alsaffar** *(1:01:32)*  
So the improvement only affects the best case scenario.

**Dr. Ali Alsaffar** *(1:01:37)*  
Let us do the average case.

**Dr. Ali Alsaffar** *(1:01:42)*  
Now I am talking live in the class session. As you see that the bubble sort the original implementation, it goes over every two consecutive elements and swap when necessary.

**Dr. Ali Alsaffar** *(1:01:58)*  
Now what if the array is already sorted?

**Dr. Ali Alsaffar** *(1:02:02)*  
So there is no need to go over the array many times, and the worst case is that if the array is in reverse order, you want to sort it in ascending order and it is already sorted in descending order and the bubble sort.

**Dr. Ali Alsaffar** *(1:02:18)*  
It will work the worst so we can make some improvement to the algorithm in the first pass. If there is any swap in the first pass, then we need another pass. Now in the second pass, if there is a swap, we need to have another pass.

**Dr. Ali Alsaffar** *(1:02:36)*  
So whenever in any pass there is no swap, that means all elements are in the correct position and algorithm should stop and this we call it improved version. Now in our discussion when we add this improvement.

**Dr. Ali Alsaffar** *(1:02:52)*  
Can we still consider the algorithm brute force or not? As we discussed for the selection sort, here we are just reducing some of the cases, so you are still comparing every element.

**Dr. Ali Alsaffar** *(1:03:08)*  
So to some people they say it is still a brute force because you did not avoid, you know, avoid visiting some of the elements. You are still visiting every element and every pass and the worst case is you are getting.

**Dr. Ali Alsaffar** *(1:03:27)*  
N square, which is the same as the original one. Others they say no. Here we are reducing some cases, so it might not be considered as a brute force, but it is just an enhanced version of the bubble sort.

**Dr. Ali Alsaffar** *(1:03:42)*  
So we finished bubble sort. Our next discussion will be examples from searching problems types and I have already prepared a recorded video. Not ready. It is ready, but I will stop here today.

**Dr. Ali Alsaffar** *(1:04:01)*  
We will stop and in sha Allah next lecture we will continue with the rest of the algorithms that are categorized as brute force algorithms. So we will stop here now and for those who joined us late.

---

## Part 4 — Exam Details Recap

**Dr. Ali Alsaffar** *(1:04:18)*  
Just to repeat whatever I have said in the beginning of the lecture, the exam will be next week as I specified in the announcement will be at 10:45 AM.

**Dr. Ali Alsaffar** *(1:04:38)*  
Lockdown browser and Respondus for proctoring. You make sure that everything is working when you take the test. Any technical issues, I will not have a solution for that. That's why we have a practice sample exam.

**Dr. Ali Alsaffar** *(1:04:55)*  
Go over the practice exam to get familiar on the steps when you take the exam.

**Dr. Ali Alsaffar** *(1:05:04)*  
We will not have multiple choice and we will not have true false questions. These type of questions we will use them only in quizzes and we have finished one quiz. I have already graded it and posted the results. You can see the results for the next one. Also we will have multiple choice and essay questions.

**Dr. Ali Alsaffar** *(1:05:23)*  
And the test, all the questions will be you write answers. Some of the questions we will ask you to write the solution directly using the editor. Either you use the math editor or you use the abbreviations. Others you will have the choice.

**Dr. Ali Alsaffar** *(1:05:39)*  
So if you prefer to take a screenshot of your work, you should do this at the end of the exam. So when you click submit the Blackboard or the Respondus will allow you to take photos of your work.

**Dr. Ali Alsaffar** *(1:05:56)*  
Do this if you want to submit your work as an attachment.

**Dr. Ali Alsaffar** *(1:06:01)*  
Sometimes the resolution of the picture you are taking is not high and maybe dark. So you have a chance if you have a problem. I'm saying if you have a problem, but everybody should take photos.

**Dr. Ali Alsaffar** *(1:06:18)*  
If they prefer to attach screenshots.

**Dr. Ali Alsaffar** *(1:06:34)*  
After finishing the exam, there will be a link open for late submissions. It will open for 10 minutes after the official end time of the exam has reached. I will open it for 10 minutes so you have a chance to upload unfinished attachment of your work.

**Dr. Ali Alsaffar** *(1:06:53)*  
But if you want to attach using the late submission, when you take a screenshot, put your ID on the answer for each page. Helpful ID. OK, so I want to make sure that this is your answer.

**Dr. Ali Alsaffar** *(1:07:09)*  
Not somebody else's answer.

**Dr. Ali Alsaffar** *(1:07:17)*  
Anybody has any question?

---

## Reference Notes — Key Takeaways

### Bubble Sort — How It Works
- Compare every two **adjacent** elements, swap if out of order
- Each complete pass "bubbles" the largest unsorted element to its correct position
- After each pass, reduce the range by 1 (increment i) — the last elements are already sorted

### Bubble Sort — Implementation Details
- **Swap flag:** boolean variable, reset to false at start of each pass
- When a swap occurs → set flag to true → signals while loop to do another pass
- When no swap occurs in a pass → flag stays false → array is sorted → loop terminates
- **Range reduction:** after each pass, increment i to shrink the comparison range by 1
- Swapping requires 3 assignment statements (same as selection sort)

### Improved Bubble Sort — Complexity

| Case | Original Bubble Sort | Improved Bubble Sort |
|------|---------------------|---------------------|
| **Best case** | Theta(N^2) | **Theta(N)** — one pass, no swaps, done |
| **Average case** | Theta(N^2) | Theta(N^2) — no improvement |
| **Worst case** | Theta(N^2) | Theta(N^2) — no improvement |

- **Best case:** array already sorted → one pass, no swaps detected, algorithm stops → Theta(N)
- **Worst case:** array in reverse order → must do all N-1 passes → Theta(N^2)
- The improvement **only helps the best case**

### Is Improved Bubble Sort Still Brute Force?
Two perspectives (exam-worthy discussion):
1. **Yes, still brute force** — you still visit every element in every pass, worst case is still N^2, you didn't fundamentally change the approach
2. **No, it's enhanced** — you're reducing some cases by early termination, so it's an optimization beyond pure brute force

### Next Topic
- Brute force searching algorithms (sequential search, etc.)

### Midterm Exam Details
- **Date:** April 6th, 2026
- **Time:** Initially said 3:00 PM, later corrected to 10:45 AM
- **Duration:** 1 hour
- **Platform:** Blackboard + Lockdown Browser + Respondus (proctoring)
- **Format:** All written answers (no multiple choice, no true/false — those are quiz-only)
- **Options:** Write in editor (math editor or abbreviations) OR take photo via webcam after submit
- **Late submission link:** Opens for 10 minutes after exam ends — put student ID on each page
- **Technical prep:** Practice with sample test, restart computer, good Wi-Fi connection

### Gap in Transcript
- ~57 minute gap (2:20 to 1:00:04) where bubble sort algorithm was explained theoretically and implementation was built step by step in Java.
