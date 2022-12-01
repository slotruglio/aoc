# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?

def part_one(path):
    '''Find the Elf carrying the most Calories and his total Calories'''
    max = 0
    current_sum = 0

    with open(path, 'r') as file:
        for line in file.readlines():
            if line == "\n":
                current_sum = 0
                continue

            current_sum += int(line)
            if max < current_sum:
                max = current_sum    
    return max

def part_two(path):
    '''Find top 3 elves with most calories and their total calories'''
    calories = []
    current_cal = 0

    with open(path, 'r') as file:
        for line in file.readlines():
            if line == "\n":
                calories.append(current_cal)
                current_cal = 0
                continue

            current_cal += int(line)
        else:
            # End Of File
             calories.append(current_cal)

    return sum(sorted(calories, reverse=True)[:3])


def main():
    input = "./2022/inputs/day1/day1.txt"
    
    max = part_one(input)
    print("Part 1 - output: "+str(max))

    total = part_two(input)
    print("Part 2 - output: "+str(total))

if __name__ == '__main__':
    main()
    exit(0)

            
