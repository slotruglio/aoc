def day_3(input):
    sum_1 = 0 
    sum_2 = 0
    with open(input, 'r') as file:
        group = []
        for line in file.readlines():
            # part one calculus
            first, second = line[:len(line)//2], line[len(line)//2:]
            for char in first:
                if char in second:
                    sum_1 += ord(char)
                    sum_1 -= 96 if char.islower() else 38
                    break
            # part two calculus
            group.append(line.strip())
            if len(group) == 3:
                for char in group[0]:
                    if char in group[1] and char in group[2]:
                        sum_2 += ord(char)
                        sum_2 -= 96 if char.islower() else 38
                        group = []
                        break

    return (sum_1, sum_2)

if __name__ == '__main__':
    input = "2022/inputs/day3/input.txt"
    one, two = day_3(input)
    print(f"Part 1: {one}")
    print(f"Part 2: {two}")