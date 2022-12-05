# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?

def day_1_full(path):
    '''Find the top 3 calories carried by the elves and return both top 1 and top 3'''
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

    calories = sorted(calories, reverse=True)[:3]
    return (calories[0], sum(calories))

if __name__ == '__main__':
    input = "./2022/inputs/day1/day1.txt"
    (one, two) = day_1_full(input)
    print("Part 1: "+ str(one))
    print("Part 2: "+str(two))

            
