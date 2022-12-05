def day_five(input):
    stacks = []
    with open(input, 'r') as f:
        lists = []
        for line in f.readlines():
            if "move" in line:
                # if line is move x from y to z
                (_, n, _, stack_from, _, stack_to) = line.split(' ')
                n, stack_from, stack_to = int(n), int(stack_from), int(stack_to)
                for _ in range(n):
                    stacks[stack_to-1].append(stacks[stack_from-1].pop())
            elif "[" in line:
                # if line is [A] [B] [C] append item to lists
                level = []
                for i in range(1, len(line), 4):
                    level.append(line[i])
                lists.append(level)
            elif "1" in line:
                # if line is 1 2 3 create a [] for each of the stack
                for i in range(1, len(line), 4):
                    stacks.append([])
            else:
                # if line is \n add items to stacks
                for i in range(len(lists)):
                    for j in range(len(lists[i])):
                        letter = lists[i][j].strip()
                        if  len(letter) == 0:
                            continue
                        stacks[j].insert(0, letter)

    result = ""
    for s in stacks:
        result += s.pop()
    return result

if __name__ == '__main__':
    print(day_five("2022/inputs/day5/input.txt"))