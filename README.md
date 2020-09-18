# connect-z

Solution by Ben Gittins.

Program is contained in connectz.py as stipulated. I used TDD to develop this solution so the project also contains my tests and text files containing acceptance tests.

To run program:

    python3 src/app.py <filename>.txt

To run tests:

    python3 python3 -m pytest 

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
