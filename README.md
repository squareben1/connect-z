# connect-z

### Solution 

In this solution columns  are represented by arrays, rows by positions in those arrays.

Below game params = X = 3, Y = 3, Z = 2, moves [1, 2, 1]

    [
      [1,1,_], ─ Column 1
      [2,_,_], ─ Column 2
      [_,_,_]  ─ Column 3
    ]  | | |
       | | └ ─ Row 3
       | └ ─ Row 2
       └ ─	Row 1

    illegal row:
    [
      [1,2,1], ─ Column 1
      [2,1,2]1, ─ Column 2
      [_,_,_]  ─ Column 3
    ]  | | |
       | | └ ─ Row 3
       | └ ─ Row 2
       └ ─	Row 1

Player 1 wins.

#### Analysis

This made it easier to 'drop' moves into columns. It did mean I sometimes had trouble visualising what was going on though. 

do diff? build in errors from start - do the easy stuff first. Wanted to get game logic though 

**Small note on commenting:** I usually try to avoid leaving comments on my code (Ruby was my first language so I learned to avoid it). I actually really like how doing it here has signposted the code.