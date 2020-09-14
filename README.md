# Sudoku Solver

A basic sudoku solver algorithm for learning and fun.
## Use

* solve_sudoku.py
  * contains all supporting functions
  * run as main


* puzzle_set.py
  * contains a dictionary of 5 test puzzles
    * empty: empty puzzle
    * easy: easy according to _United Airlines in-flight magazine_
    * medium: medium according to _United Airlines in-flight magazine_
    * hard: hard according to_United Airlines in-flight magazine_
    * hardest: allegedly **The Worlds Hardest Sudoku Puzzle** according to this
    [Gizmodo article](https://gizmodo.com/can-you-solve-the-10-hardest-logic-puzzles-ever-created-1064112665)

```console
$ python solve_sudoku.py
empty, easy, medium, hard, or hardest?: easy
Solving...
[7, None, None, 1, None, None, None, None, 8]
[None, 3, 6, 2, None, 8, 7, None, None]
[8, None, 4, None, 6, None, None, None, None]
[None, 8, None, None, 5, None, 2, 1, None]
[None, None, 2, 4, None, 7, 3, None, None]
[None, 9, 1, None, 8, None, None, 7, None]
[None, None, None, None, 9, None, 8, None, 5]
[None, None, 8, 5, None, 3, 6, 9, None]
[5, None, None, None, None, 4, None, None, 7]
Time to Complete: 0.03936266899108887
Number of Iterations: 20
[7, 2, 5, 1, 3, 9, 4, 6, 8]
[9, 3, 6, 2, 4, 8, 7, 5, 1]
[8, 1, 4, 7, 6, 5, 9, 2, 3]
[3, 8, 7, 9, 5, 6, 2, 1, 4]
[6, 5, 2, 4, 1, 7, 3, 8, 9]
[4, 9, 1, 3, 8, 2, 5, 7, 6]
[2, 7, 3, 6, 9, 1, 8, 4, 5]
[1, 4, 8, 5, 7, 3, 6, 9, 2]
[5, 6, 9, 8, 2, 4, 1, 3, 7]
```
## Potentially Funny Backstory for 3D Educational Game

After finishing the in-flight magazine crossword puzzle together,
my friend asked me if I knew how Sudoku puzzles worked.
I explained the basic idea and she began an attempt to
solve one of the Sudoku puzzles.

2 minutes she exclaimed:

> This sucks! Crosswords are much more fun and I feel like I may as well be doing expense reports.

I had solved a few easy Sudoku puzzles a few times before and although I didn't share my friend's dreadful opinion of them, 
I could see her point. While I am sure proficient solvers have sophisticated heuristics that give the puzzle richness and interesting complexity, as naive, average amateurs like us it kind of
does seem like a tedious accounting problem.  Still, what one human may deem tedious another deems entertaining and to each their own. For others, even if tedious, it is preferred over worrying about the turbulence, the crying child, the claustrophobic conditions, the exposure to higher radiation levels at 35K feet and the potential malicious exploitation of the plane's auto-pilot in an era where everyone, everything and their mother seems to get hacked.

The following sequence of questions filled my mind:

1. Given the well-defined constraints and well-defined structure of the puzzle, how
difficult would it be to write and implement an algorithm to solve any possible Sudoku puzzle?

2. Could my MacBook Air and my brain's ability to write a Python program be used to solve each of the 3 Sudoku puzzles (Easy, Medium, Hard) in the _United Airlines Hemispheres June 2019_ issue before landing?

3. What if the survival of the **entire flight** depended on a single person accomplishing this feat as in a _90s-fabulous_, hacker-action-_Saw_ movie hybrid? 

    > Hello, do you wanna play a game?
    
    _Says Saw the sadistic hacker over the flight intercom as it hijacks the auto-pilot controls only releasing them if an adequate Python algorithm is written to solve each of the 3 puzzles._

4. Ok Well, how many possible 9X9 arrays exist with a single value from the set `{None, 1, 2, 3, 4, 5, 6, 7, 8, 9}` at each location in the array? 
   
    `ANSWER = 10**81` or "10 raised to the 81st power"

    _Whoa! That is a large number. A very naive brute force approach would stand no chance.
    The possibilities are larger than the output space of SHA-256_ i.e. `(10**81 > 2**256)` is `True`



Cut off from the internet being too broke to justify in-flight Wi-Fi, I could not Google for help. I gazed out at all of the peaceful passengers snoring away the red-eye and the few night owls scrolling their smart phones. A vivid imagination conjured the _Saw_ voice from the in-flight intercom:

> Hello, do you wanna play a game?

So, I spent the remainder of the flight writing a Sudoku Solver under simulated duress.

## The Essence of the Puzzle

Sudoku is a puzzle that involves 81 squares arranged in a 9X9 array.
Each locus in the array can be empty (i.e. `None`, null) or contain a digit `1-9`.
In order to be considered a solution, each square must contain a digit as well as 27 other constraints met:

+ Each of the 9 rows must contain one each of 1-9
+ Each of the 9 columns must contain one each of 1-9
+ Each of the 9 3X3 sub-grids must contain one each the 1-9

`TODO: insert image`
 
A fresh puzzle is given as incompletely filled in with the usual expectation that there is a unique solution. Each incompletely filled in 9X9 grid can either have:

* a unique solution `1`
* more than one solution `> 1`
* no solutions `{}`

_This is reminiscent of the classic linear algebra problem of n unknowns and m equations._
 
[Wikipedia: Mathematics of Sudoku](https://en.wikipedia.org/wiki/Mathematics_of_Sudoku)

### Puzzle State Representation

The state of the 9X9 Sudoku puzzle is represented as a 9 element list of lists, each with 9 elements. This is what the empty puzzle looks like:

```python
s0 = [[None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None]]
```
This will allow easy access to each location in the array with `s0[row][col]`

### The general algorithm

1. Extract the `(row, col)` address of each `None` into a sequence as a single Python list reading the fresh puzzle from left to right on each row starting from the top left.

2. Try a value in the first `None` of the sequence starting with `1`, then `2`... until a compatible value is found

3. Move to next `None`, Repeat 2 on this `None`. If exhausted to 9, roll-back and find the next value in the previous `None`

Note: This algorithm is essentially a depth-first, rollback similar to **Knuth's Algorithm X.**


## Results

|puzzle|solve time (seconds)| number of iterations|
|------|---------|----|
|empty| 0.27 | 291 |
|easy | 0.039  | 20  |
|medium|0.087  | 72  |
|hard  |14.51 | 15682  |
|hardest|37.25|38380|

It is satisfying that they are ranked intuitively by solve time. There is probably a puzzle that could be designed to be a really bad scenario for this algorithm.

### The Empty Puzzle

A solution to the empty puzzle 


### Comparison to Biological Computer

It just so happens the copy of my in-flight magazine was once in the possession of a biological Sudoku solver. It gives non-zero information that indeed the hard puzzle is 

As they say:

> n of 1 is infinitely greater than n of zero

## Discussion Puzzle Complexity
If we begin with only the 9 X 9 matrix that can contain None-9, there are

```python
import math
# number of possible board states:
N0 = 10**81

# number of possible filled board states:
N1 = 9**81

# number of possible satisfied 9 row constraints only
N2 = math.factorial(9)**9

# number of possible satisfied 9 row and 9 col constraints only
# i.e. "9X9 Latin Squares"
N3 = math.factorial(9)*math.factorial(8)*?

# number of possible Sudoku puzzles
N4 = ?

```


```python
>>> math.log2(N0)
269.07617568587636
>>> math.log2(N1)
256.7639251168273
>>> math.log2(N2)
166.22219717846633

print(str(math.ceil(math.log2(math.factorial(9)**9))) + ' bits')
>>> 167 bits
```



