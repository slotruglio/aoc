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

## Day 3
### Part One
Each char of a line of the input represents an item inside a rucksack. We have to find the char (and its corresponding value) common in the two compartments of the rucksack. (The compartments are the two halves of the input line.)
In the end, we have to sum the values of the chars common in the two compartments.
### Part Two
Like in the first part, but in this case we have to find the common char in a group of three lines.

## Day 4
### Part One
Each line of the input is two couple of numbers that represent a range of numbers. We have to count how many full overlapsing ranges there are. It can be simply solved by doing the union of the two ranges as set and verify if the length of the union is equal to one or the other range.
### Part Two
This time we have to find ALL overlapsing number. We can do it by doing the intersection of the two ranges as set and verify if the length of the intersection is greater than 0.
