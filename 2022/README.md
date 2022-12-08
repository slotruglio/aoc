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

## Day 5
### Part One
The first input gives items in line, but they correct order is the column. After correctly create a list for each column and put data inside, we need to do the move that are easy to do without using "strange" functions thanks to using list for stacks, where the first item in stack is the last of the list. Acting like that we can get the first item of stack just with pop() and add in the top of the stack just with append().
### Part Two
For this part we have to do the same thing, but instead of insert directly the item returned by pop() of the stack, we have to take last n items in the order they are in the (from) stack and insert them in the (to) stack in the same order.

## Day 6
### Part One
We have to find first 4-chars word without repeating chars. To do that we can simply take a slice of len 4 and verify if the len of the set is equal to the len of the slice.
### Part Two
Like Part One, but this time the number of chars is 14.

## Day 7
The input is a list of strings that represent terminal commands. In this exercise can be useful to use [anytree library](https://pypi.org/project/anytree/), because it can help us to find the relationship between current directory, the command and files
### Part One
We have to find the sum of directories' size less than a given size. Directories' size can be calculated by summing the size of all files inside it.
### Part Two
We know the size of the disk and the size of the update. We have to find the smallest dir to delete in order to install the update.

## Day 8
The input is a matrix of trees' height (int).
### Part One
We have to find the number of trees that are visible (tree has the max height) from at least one side (left, right, top, bottom).
To do that we can iterate for each tree and check if it's visible from at least one side. It can be calculated also by doing part two and verify that the last iteration is equal to the number of trees for that side.
### Part Two
We have to find the highest scenic score (production of the number of trees visible from all sides) of a tree. To do that we have to find the local scenic score by iterating for each tree and count the number of trees visible from all sides. If the local scenic score is greater than the current max, update the max.