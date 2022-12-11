import math

class Monkey:
    inspected = 0
    def __init__(self, name, items, operation, test, true_m, false_m):
        self.name = "Monkey "+str(name)
        self.items = items
        self.operation = Monkey.parse_op(operation)
        self.test = Monkey.parse_test(test)
        self.true_m = true_m
        self.false_m = false_m
    
    def parse_op(operation):
        _, op = operation.split("=")
        def fn(old):            
            return eval(op)
        return fn

    def parse_test(test):
        num = test.split(" ")[-1]
        def fn(value):
            return value % int(num) == 0
        return fn

    def add(self, item):
        self.items.append(item)

    def inspect(self):
        if len(self.items) == 0:
            return
        self.items[0] = self.operation(self.items[0])
        self.items[0] = math.floor(self.items[0] / 3)
        self.inspected += 1

    def test_fn(self, monkeys):
        if len(self.items) == 0:
            return
        item = self.items.pop(0)
        if self.test(item):
            monkeys[self.true_m].add(item)
            return
        monkeys[self.false_m].add(item)

def day_eleven(input):
    monkeys = []
    with open(input, 'r') as f:
        counter = 0
        curr_items = []
        operation = None
        test = None
        true_m = None
        false_m = None
        for line in f.readlines():
            if "Monkey" in line:
                curr_items = []
                counter += 1
                operation = None
                test = None
                true_m = None
                false_m = None
            if "items" in line:
                curr_items = [int(x) for x in line.split(":")[1].split(",")]
            elif "Operation" in line:
                operation = line.split(":")[-1].strip()
            elif "Test" in line:
                test = line.split(":")[-1].strip()
            elif "true" in line:
                num = line.split(" ")[-1]
                true_m = int(num)
            elif "false" in line:
                num = line.split(" ")[-1]
                false_m = int(num)
                monkey = Monkey(counter, curr_items, operation, test, true_m, false_m)
                monkeys.append(monkey)
    
    # run the monkeys
    top_2 = [0,0]
    for i in range(20):
        for monkey in monkeys:
            item_count = len(monkey.items)
            for j in range(item_count):
                monkey.inspect()
                monkey.test_fn(monkeys)

        if i == 19:
            top_2 = sorted([m.inspected for m in monkeys], reverse=True)[:2]

    return (top_2[0]*top_2[1],0)

if __name__ == '__main__':
    one,two = day_eleven("2022/inputs/day11/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)