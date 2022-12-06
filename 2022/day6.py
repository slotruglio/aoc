def day_six(input):
    part_one = 0
    part_two = 0
    with open(input, 'r') as f:
        find_one, find_two = False, False
        start = 0
        end_1 = 3
        end_2 = 13
        line = f.readline().strip()

        while end_1 < len(line)-1 and end_2 < len(line)-1:
            signal = line[start:end_1+1]
            if len(set([*signal])) == len(signal) and not find_one:
                part_one = end_1+1
                find_one = True
            signal = line[start:end_2+1]
            if len(set([*signal])) == len(signal) and not find_two:
                part_two = end_2+1
                find_two = True
            if find_one and find_two:
                break
            start += 1
            end_1 += 1
            end_2 += 1

    return (part_one,part_two)





if __name__ == '__main__':
    one,two = day_six("2022/inputs/day6/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)