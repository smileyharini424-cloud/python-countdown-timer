# Countdown Timer

## Explanation

The Countdown Timer is a Python program that counts down from a user-specified number of seconds until it reaches zero.

## Problem Statement

Create a Python program that accepts a duration in seconds and displays the remaining minutes and seconds during the countdown.

## Features

* Accepts countdown duration
* Displays remaining minutes and seconds
* Updates the timer every second
* Displays a completion message
* Handles invalid input

## How It Works

1. The user enters the countdown duration in seconds.
2. The program converts the duration into minutes and seconds.
3. The remaining time is displayed.
4. The timer decreases by one second.
5. The process continues until the timer reaches zero.
6. A completion message is displayed.

## Technologies Used

* Python
* `time` module
* Loops
* Functions
* Exception Handling

## Data Structure Used

* Integer variables

## Methods Used

* `countdown()`
* `main()`

## Program Flow

```text id="k5m7xz"
Start
  ↓
Enter Duration
  ↓
Validate Input
  ↓
Display Remaining Time
  ↓
Wait 1 Second
  ↓
Decrease Timer
  ↓
Timer = 0?
  ↓
Display Completion Message
  ↓
End
```

## Sample Input

```text id="x9d2ke"
Enter countdown time in seconds: 5
```

## Sample Output

```text id="p4c7yw"
00:05
00:04
00:03
00:02
00:01
Time's up!
```

## Time Complexity

O(n), where `n` is the number of seconds.

## Space Complexity

O(1)

## Key Learning

* Using the Python `time` module
* Working with loops
* Formatting time
* Using functions
* Handling user input

## File Location

`countdown_timer.py`

## Repository Structure

```text id="g3n6tw"
python-countdown-timer/
│
├── countdown_timer.py
└── README.md
```

## Author

V.Harini
