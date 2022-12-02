# 2022 Solutions

## Day 1
### Part One
We are asked to find the top sum of calories (int) that an Elf is carrying. The input is a simple list of numbers with '\n' as a delimiter.

Proposed solution: calculate local sum and if it is greater than the current max, update the max.

### Part Two
We are asked to find the sum of top three sum of calories (int) that Elves are carrying. The input is the same as in Part One.

Proposed solution: calculate local sum and append to a list. Sort the list and return the sum of the first/last three elements, the greatest elements.

## Day 2
We are asked to find the "total score" of a rock, paper, scissors match with N rounds.
### Part One
Every match consists of two chars, one for each player. We have to sum the score for each shape (rock, paper, scissors) and the score for the outcome of the match (win, lose, draw).

### Part Two
Every match consists of two chars, the first is the opponet shape and the second is the "desired outcome", so we have to sum the score for the desired outcome and the score for the shape that "matches" the desired outcome.
