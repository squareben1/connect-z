# connect-z

## Intro

Solution by Ben Gittins.

Original program contained in connectz.py as stipulated in the challenge. I used TDD to develop this solution so the project also contains my tests and text files containing acceptance tests.

To run program:

    python3 src/app.py <filename>.txt

To run tests:

    python3 python3 -m pytest 

## Part 1: The Problem

This programming challenge is based on the classic game of Connect Four.

"Your goal is to implement a game checker program for Connect Z. In Connect Z the concept of the traditional game of Connect Four is generalized to include playing frames of any size and a target line of any length. When provided with a data file that describes a game of Connect Z your checker program should determine if that game was won, drawn or contains an error of some kind. The format of the data files and expected output is described in detail below."

### Program specification

- This challenge should be written in Python 3. The reference implementation that will be used to assess the submission is Python 3.6.
- Third party libraries are not allowed. The challenge should be completed using only features provided by the standard libraries. https://docs.python.org/3/library/index.html
- The game checker should be submitted as a Python script called ‘connectz.py’.
- The script will read input from a datafile which is a pain ASCII textfile.
- This script takes a single argument ‘inputfilename’ which is the name of the data file containing game information to be checked.
- The script will be called as: ```python connectz.py inputfilename```
- If the game is run with no arguments or more than one argument it should print the following message as a single line to standard out:
  ```connectz.py: Provide one input file```

### Output Specification

- The output of the program should be a single integer printed to standard out.
- The integer is a code which describes the input.
- Output codes 0 - 3 are for valid game files.
- Output codes 4 - 9 represent errors.

The codes are defined as follows:


| Code | Reason           | Description                                                                                                                                                                                                                                             |
| ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | Draw             | This happens when every possible space in the frame was filled with a counter, but neither player achieved a line of the required length.                                                                                                               |
| 1    | Win for player 1 | The first player achieved a line of the required length.                                                                                                                                                                                                |
| 2    | Win for player 2 | The second player achieved a line of the required length.                                                                                                                                                                                               |
| 3    | Incomplete       | The file conforms to the format and contains only legal moves, but the game is neither won nor drawn by either player and there are remaining available moves in the frame. Note that a file with only a dimensions line constitues an incomplete game. |
| 4    | Illegal continue | All moves are valid in all other respects but the game has already been won on a previous turn so continued play is considered an illegal move.                                                                                                         |
| 5    | Illegal row      | The file conforms to the format and all moves are for legal columns but the move is for a column that is already full due to previous moves.                                                                                                            |
| 6    | Illegal column   | The file conforms to the format but contains a move for a column that is out side the dimensions of the board. i.e. the column selected is greater than X                                                                                               |
| 7    | Illegal game     | The file conforms to the format but the dimensions describe a game that can never be won.                                                                                                                                                               |
| 8    | Invalid file     | The file is opened but does not conform the format.                                                                                                                                                                                                     |
| 9    | File error       | The file can not be found, opened or read for some reason.                                                                                                                                                                                              |


## Part 2: The Solution

### About Solution

In this solution columns  are represented by arrays, rows by positions in those arrays.

Example - in the below game X = 3, Y = 3, Z = 2, moves = [1, 2, 1]:

    [
      [1,1,_], ─ Column 1
      [2,_,_], ─ Column 2
      [_,_,_]  ─ Column 3
    ]  | | |
       | | └ ─ Row 3
       | └ ─ Row 2
       └ ─	Row 1

Player 1 wins.

### Analysis

This made it easier to 'drop' moves into columns. It did mean I sometimes had trouble visualising what was going on though.

### What would I do differently?

In hindsight I probably should have built in the error codes from the start. Some of the work was already done (I included guard clauses to catch out of range errors) but going back in and amending to return the correct codes was innefficent. I'm not too concered about this as it was borne out of a desire to get the main game logic finished before focusing on something else.

I also spent several hours trying to build a visual representation of the game board early on, to aid with debugging. This ended up being an unnecessary distraction but it did at least get me thinking about the problem and provided some visual context which, for me, is absolutely essential in solving this kind of problem.

If not constrained to one file I would also have split out several classes to adhere to SRP (reading and formatting data, checking moves, etc.).

### Summary

I found this problem difficult! I certainly didn't breeze through it - I spent several days working on it and had a couple of false starts and frustrating moments.

However I am pleased with the end result and actually got an awful lot out of it as an exercise. My solution made it easier to code but harder to visualise naturally since arrays represent columns and rows are represented by indexes in those arrays - essentially flipping the 'board' on it's side. This trade-off between ease of coding and ease of visualising contributed to the challenge for me as I sometimes struggled for context.

Overall this was a very challenging but ultimately satisfying problem that I learned a lot from.


**Small note on commenting:** I usually try to avoid leaving comments in my code (Ruby was my first language so I learned to avoid it early on). I prefer to aim for well-named functions with as few lines of code as possible. I actually really like how doing it here has signposted the code though.
