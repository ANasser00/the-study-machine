# Section 3 — Week 8 Lecture 1 — Chapter 3: Brute Force — Selection Sort (Java Implementation)

**Course:** ITCS-347 — Design and Analysis of Algorithms  
**Instructor:** Dr. Ali Alsaffar  
**Date:** March 30th, 2026  
**Coverage:** Chapter 3 begins — Brute Force: selection sort Java implementation, testing correctness with small arrays, empirical analysis setup (two stages), isSorted concept

---

## Part 1 — Quiz Feedback & Announcements

**Dr. Ali Alsaffar** *(0:03)*  
Welcome and good morning class. This is Doctor Al Safar, ITCS 347 Introduction to the Design and Analysis of Algorithms, Section 3.

**Dr. Ali Alsaffar** *(0:16)*  
Before we start the lecture, I would like to briefly and talk about the online quiz that the students has taken yesterday. I did not go through the quiz. I will go over the quiz and any students.

**Dr. Ali Alsaffar** *(0:35)*  
Has any problem, I will look into the messages sent by the student and the problem. Next time what we will do because in the last attempt there was no option that you can upload your work if you write it on a piece of paper.

**Dr. Ali Alsaffar** *(0:54)*  
I have already said that in the class is that for answering the question, I mean for answering the online quiz, you would not need to write anything on piece of paper. You will write directly into the editor, the Blackboard editor.

**Dr. Ali Alsaffar** *(1:12)*  
I have already posted a mock quiz and sample test for practicing. For those students who did not make a practice and they just went directly to the quiz, well, they can, yeah.

**Dr. Ali Alsaffar** *(1:28)*  
Put up the responsibility if they make mistakes in taking the online course. What we will do next? I will change the options for the Lockdown browser and I will have the option that after the student submit.

**Dr. Ali Alsaffar** *(1:45)*  
The answer it will give a choice for the student to upload or take a picture from the webcam. There is an option in the responders after you. This is for proctoring — after you submit in the system or the lockdown, not the lockdown browser, the responders, which is a different.

**Dr. Ali Alsaffar** *(2:05)*  
Software. It will give you a chance to take a photo of any notes that you would like to attach through the webcam. So the webcam that you are going to use for proctoring will allow you to take screenshots for any.

**Dr. Ali Alsaffar** *(2:21)*  
Thing that you would like to attach in the exam. But to do this you have to submit by yourself. If the system submits, if the time finishes and the system submits your answers, I don't know what happens. Is it going to give you a chance to upload photos or not? Then then.

**Dr. Ali Alsaffar** *(2:41)*  
And then this needs to be tested and I will provide this in the sample test. I will put this option. You try it by yourself so that in the test you don't get the problems or any issues. So you can take the quiz and exam freely without any stress.

---

## Part 2 — Selection Sort: Java Implementation

**Dr. Ali Alsaffar** *(1:04:50)*  
And list minimum will take the value of TO. For swapping we need three assignment statements. This completes the implementation for the selection sort.

**Dr. Ali Alsaffar** *(1:05:06)*  
We will test selection sort in two stages. First we write a smaller program to make sure our implementation works correctly by sorting a small array and checking the result. Then in the second stage we shift to performance testing.

**Dr. Ali Alsaffar** *(1:05:23)*  
We sort much larger arrays and measure how long the algorithm takes. This helps us see how selection sort behaves as the input size increases. So let's get started.

**Dr. Ali Alsaffar** *(1:05:36)*  
We click the main class tab to go to the main class and then inside the main method we begin our first stage program.

**Dr. Ali Alsaffar** *(1:05:45)*  
We will generate a small array, display it before sorting, run selection sort on it and then choose the result. So let's begin by creating our array. Now inside the main method we create a local array of integer.

**Dr. Ali Alsaffar** *(1:06:03)*  
We call it list. Then we call the makeRandom method from our ArrayUtils class to generate a list of random numbers. ArrayUtils.makeRandom. In our case we will generate an array with 20 integers.

**Dr. Ali Alsaffar** *(1:06:23)*  
Size of the array is 20 and each value will fall somewhere between -1000 and positive 1000, so the range will be from -1000 up to 1000.

**Dr. Ali Alsaffar** *(1:06:38)*  
Before we sort anything, we want to see the original contents of the array. So we print a message indicating that this is the array before sorting and then we call the print method from our utility class to display all the numbers on the screen, 15 values per line.

**Dr. Ali Alsaffar** *(1:06:55)*  
So we print this message. The message will be "the array before sorting".

**Dr. Ali Alsaffar** *(1:07:07)*  
And then we call the method print from our ArrayUtils class. ArrayUtils.print. We supply the list as an input parameter and we want to print 15 values per line.

**Dr. Ali Alsaffar** *(1:07:24)*  
So the second parameter will be 15.

**Dr. Ali Alsaffar** *(1:07:29)*  
Now right before we begin the sorting process, we print also another simple message to let the user know that the selection sort is about to start working. So after this line we need to print a message that says "sorting has just started" with some dots.

**Dr. Ali Alsaffar** *(1:07:47)*  
Has just started with some dots.

**Dr. Ali Alsaffar** *(1:07:53)*  
Now we call the selection sort algorithm from our ArrayUtils class and pass in the list we just printed. So ArrayUtils.selectionSort and we supply the array list as input parameter.

**Dr. Ali Alsaffar** *(1:08:12)*  
Once the sorting is finished, we need to print another message to indicate that the process is complete. So we print the message.

**Dr. Ali Alsaffar** *(1:08:25)*  
And the message says "sorting has completed".

**Dr. Ali Alsaffar** *(1:08:35)*  
To make sure our selection sort method works, we could print the whole array and check it by hand. I mean by looking at the output. But that only works for small arrays, and with large arrays that's not realistic.

**Dr. Ali Alsaffar** *(1:08:51)*  
So first let us print the array and check by looking at the output if the array is sorted and then after that we will make a utility method that can automatically help us check if this array is actually sorted. Let us print the sorted array.

**Dr. Ali Alsaffar** *(1:09:06)*  
ArrayUtils.print. We supply the list and we want to print 15 values per line. This completes the implementation of our starting program.

**Dr. Ali Alsaffar** *(1:09:23)*  
Now let us run the code to see the result by pressing Shift F10.

**Dr. Ali Alsaffar** *(1:09:29)*  
This is the output of the program.

**Dr. Ali Alsaffar** *(1:09:33)*  
As you can see in the output, the program displays the contents of the array before sorting and after sorting by printing 15 values per line as specified in the print method.

**Dr. Ali Alsaffar** *(1:09:46)*  
But there is a slight problem on the output. Notice that after printing the content of the array, the print method is not adding a new line. This makes the printed messages after calling the print method not printed on separate lines.

**Dr. Ali Alsaffar** *(1:10:02)*  
So let's go back to the utility class and modify it to add a new line. After displaying the content of the array, close the output screen, go to the ArrayUtils class, go to the print method and at the end add a new line.

**Dr. Ali Alsaffar** *(1:10:18)*  
Go back to the main program and run the program again.

**Dr. Ali Alsaffar** *(1:10:24)*  
Now from the output we can manually tell whether the array is sorted by scanning through the printed values and checking if each element is smaller than the one next to it. But as we mentioned earlier, that approach isn't practical for large arrays.

**Dr. Ali Alsaffar** *(1:10:42)*  
So let's go ahead to our utility class and create a method.

---

## Part 3 — isSorted Concept & Wrap-up

**Dr. Ali Alsaffar** *(1:10:48)*  
Now I am pausing the recorded lecture. I am talking now in the class session live talking live in the class session. I think we are reaching the end of the class. We need to take attendance.

**Dr. Ali Alsaffar** *(1:11:02)*  
And as you see that how to verify that our algorithm selection sort is implemented correctly. I'm not saying it is not correct, the algorithm is correct, but the implementation. How to make sure that our implementation really sorts the array?

**Dr. Ali Alsaffar** *(1:11:20)*  
By displaying the array on the screen for a few elements, we can test whether the elements are sorted or not, but for large ones probably there is a glitch in the implementation that makes the implementation incorrectly, so we need to write a method.

**Dr. Ali Alsaffar** *(1:11:37)*  
That we call it isSorted. It will go over each consecutive elements and make sure that each element is smaller than the next element. So we are running out of time. We will not be able to implement it and this lecture is optional. I made it practical so that the students not only see.

**Dr. Ali Alsaffar** *(1:11:57)*  
Theories algorithms written on paper. We want to show them how to implement them and how to test these algorithms for their running time on real computer. So now I will stop.

**Dr. Ali Alsaffar** *(1:12:12)*  
Here and I will go to the attendance sheet. I will call your and see your name and I will call your name. Either you say yes or present. Otherwise I will make you absent. I mean for those with the green line, let me stop the recording.

**Dr. Ali Alsaffar** *(1:12:29)*  
Yeah, I need to stop the recording first.

---

## Reference Notes — Key Takeaways

### Chapter 3: Brute Force — Selection Sort

**Selection sort algorithm:**
- Outer loop: for each position i from 0 to N-2
- Find the minimum element in the remaining unsorted portion (i to N-1)
- Swap it with element at position i
- Swapping requires **3 assignment statements** (temp variable)

### Two-Stage Testing Approach
1. **Stage 1 — Correctness testing:** Sort a small array (e.g., 20 elements), print before/after, visually verify
2. **Stage 2 — Performance testing:** Sort much larger arrays, measure execution time, observe how time grows with input size

### Java Implementation Structure (ArrayUtils class)
```
ArrayUtils utility class:
├── makeRandom(size, min, max)  → generates random int array
├── print(array, perLine)       → displays array values, perLine per row
├── selectionSort(array)        → sorts array in place
└── isSorted(array)             → verifies consecutive elements are in order (to be implemented)
```

### Main Program Flow
```java
int[] list = ArrayUtils.makeRandom(20, -1000, 1000);
System.out.println("The array before sorting");
ArrayUtils.print(list, 15);
System.out.println("Sorting has just started...");
ArrayUtils.selectionSort(list);
System.out.println("Sorting has completed");
ArrayUtils.print(list, 15);
```

### isSorted Verification Method (Concept)
- Goes over each consecutive pair of elements
- Checks that each element ≤ next element
- Essential for large arrays where visual inspection isn't practical
- Implementation deferred to next lecture

### Bug Fix Noted in Lecture
- The `print` method initially didn't add a newline after output → messages ran together
- Fix: add `System.out.println()` at end of print method

### Announcements
- Quiz 1 taken yesterday — will be reviewed
- Future quizzes will have webcam photo upload option after submission (via Respondus)
- Midterm will use Microsoft Teams
- This lecture is labeled **optional/practical** — showing real implementation, not just theory

### Gap in Transcript
- ~62 minute gap (2:41 to 1:04:50) where the brute force technique was introduced, selection sort algorithm was explained theoretically, and the ArrayUtils class methods (makeRandom, print, selectionSort) were implemented step by step.
