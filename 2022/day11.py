import numpy as np
import copy
from tqdm import tqdm

def get_top_2(monkeys, rounds, LCM=None): 
    top_2 = [0,0]
    for i in tqdm(range(rounds)):
        for monkey in monkeys:
            monkey.do_routine(monkeys, LCM)

        if i == rounds - 1:
            top_2 = sorted([m.inspected for m in monkeys], reverse=True)[:2]
    return top_2

class Monkey:
    def __init__(self, name=None, num=None, items=None, operation=None, test_val=None, true_m=None, false_m=None):
        self.inspected = 0
        self.name = name if name else "Monkey " + str(num)
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.true_m = true_m
        self.false_m = false_m
    
    def __deepcopy__(self, memo):
        return Monkey(name = self.name, items = copy.deepcopy(self.items), operation = self.operation, test_val = self.test_val, true_m = self.true_m, false_m = self.false_m)

    def parse_op(operation):
        _, op = operation.split("=")
        def fn(old):            
            return eval(op)
        return fn

    def add(self, item):
        self.items = np.append(self.items, item)

    def inspect(self, LCM=None):
        self.items = self.operation(self.items)
        if LCM:
            self.items = self.items % LCM
        else:
            self.items = self.items // 3

        count = len(self.items)
        self.inspected += count
        return count

    def test(self, monkeys):
        for item in self.items:
            index = self.true_m if item % self.test_val == 0 else self.false_m
            monkeys[index].add(item)
    
    def do_routine(self, monkeys, LCM=None):
        count = self.inspect(LCM)
        rounds = range(count)
        self.test(monkeys)
        self.items = np.delete(self.items, rounds)

def day_eleven(input):
    monkeys = []
    with open(input, 'r') as f:
        monkey = None
        for line in f.readlines():
            if "Monkey" in line:
                monkey = Monkey(len(monkeys))
            elif "items" in line:
                monkey.items = np.array([int(x) for x in line.split(":")[1].split(",")], dtype=np.uint64)
            elif "Operation" in line:
                monkey.operation = Monkey.parse_op(line.split(":")[-1].strip())
            elif "Test" in line:
                monkey.test_val = int(line.split(":")[-1].strip().split(" ")[-1])
            elif "true" in line:
                monkey.true_m = int(line.split(" ")[-1])
            elif "false" in line:
                monkey.false_m = int(line.split(" ")[-1])
                monkeys.append(monkey)
    
    divisors = []
    for monkey in monkeys:
        divisors.append(monkey.test_val)
    LCM = np.lcm.reduce(divisors)

    # run the monkeys
    part_one = get_top_2(copy.deepcopy(monkeys), 20)
    part_two = get_top_2(monkeys, 10_000, LCM)
    return (part_one[0]*part_one[1], part_two[0]*part_two[1])

if __name__ == '__main__':
    one,two = day_eleven("2022/inputs/day11/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)