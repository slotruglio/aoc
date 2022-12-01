# 2022 Solutions

## Day 1
### Part One
We are asked to find the top sum of calories (int) that an Elf is carrying. The input is a simple list of numbers with '\n' as a delimiter.

Proposed solution: calculate local sum and if it is greater than the current max, update the max.

### Part Two
We are asked to find the sum of top three sum of calories (int) that Elves are carrying. The input is the same as in Part One.

Proposed solution: calculate local sum and append to a list. Sort the list and return the sum of the first/last three elements, the greatest elements.