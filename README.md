# connect-z

Solution by Ben Gittins.

Original program contained in connectz.py as stipulated in the challenge. I used TDD to develop this solution so the project also contains my tests and text files containing acceptance tests.

To run program:

    python3 src/app.py <filename>.txt

To run tests:

    python3 python3 -m pytest 

### The Problem


This programming challenge is based on the classic game of Connect Four.

Your goal is to implement a game checker program for Connect Z. In Connect Z the concept of the traditional game of Connect Four is generalized to include playing frames of any size and a target line of any length. When provided with a data file that describes a game of Connect Z your checker program should determine if that game was won, drawn or contains an error of some kind. The format of the data files and expected output is described in detail below.

### Program specification

- This challenge should be written in Python 3. The reference implementation that will be used to assess the submission is Python 3.6.
- Third party libraries are not allowed. The challenge should be completed using only features provided by the standard libraries. https://docs.python.org/3/library/index.html
- The game checker should be submitted as a Python script called ‘connectz.py’.
- The script will read input from a datafile which is a pain ASCII textfile.
- This script takes a single argument ‘inputfilename’ which is the name of the data file containing game information to be checked.
- The script will be called as: ```python connectz.py inputfilename```
- If the game is run with no arguments or more than one argument it should print the following message as a single line to standard out:
  ```connectz.py: Provide one input file```

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

I found this task difficult! I certainly didn't breeze through it - I spent several days working on it and had a couple of false starts and frustrating moments.

However I am pleased with the end result and actually got an awful lot out of it as an exercise. My solution made it easier to code but harder to visualise naturally since arrays represent columns and rows are represented by indexes in those arrays - essentially flipping the 'board' on it's side. This trade-off between ease of coding and ease of visualising contributed to the challenge for me as I sometimes struggled for context.

Overall this was a very challenging but ultimately satisfying problem that I learned a lot from.


**Small note on commenting:** I usually try to avoid leaving comments in my code (Ruby was my first language so I learned to avoid it early on). I actually really like how doing it here has signposted the code though.
