def day_4(input): 
    with open(input, 'r') as f:
        sum_1 = 0
        sum_2 = 0
        for line in f.readlines():
            one, two = line.strip().split(',')
            range_1 = set(range(int(one.split('-')[0]), int(one.split('-')[1]) + 1))
            range_2 = set(range(int(two.split('-')[0]), int(two.split('-')[1]) + 1))
            union = range_1.union(range_2)
            if union == range_1 or union == range_2:
                sum_1 += 1

            if len(range_1.intersection(range_2)) > 0:
                sum_2 += 1

        return (sum_1, sum_2)



if __name__ == '__main__':
    input = "2022/inputs/day4/input.txt"
    one, two = day_4(input)
    print(f"Part 1: {one}")
    print(f"Part 2: {two}")