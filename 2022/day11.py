import math

class Monkey:
    def __init__(self, num):
        self.inspected = 0
        self.name = "Monkey "+str(num)
        self.items = []
        self.operation = None
        self.test_fn = None
        self.true_m = None
        self.false_m = None
    
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
        self.items[0] = self.operation(self.items[0])
        self.items[0] = math.floor(self.items[0] / 3)
        self.inspected += 1

    def test(self, monkeys):
        item = self.items.pop(0)
        index = self.true_m if self.test_fn(item) else self.false_m
        monkeys[index].add(item)
    
    def do_routine(self, monkeys):
        count = len(self.items)
        for _ in range(count):
            self.inspect()
            self.test(monkeys)

def day_eleven(input):
    monkeys = []
    with open(input, 'r') as f:
        monkey = None
        for line in f.readlines():
            if "Monkey" in line:
                monkey = Monkey(len(monkeys))
            elif "items" in line:
                monkey.items = [int(x) for x in line.split(":")[1].split(",")]
            elif "Operation" in line:
                monkey.operation = Monkey.parse_op(line.split(":")[-1].strip())
            elif "Test" in line:
                monkey.test_fn = Monkey.parse_test(line.split(":")[-1].strip())
            elif "true" in line:
                monkey.true_m = int(line.split(" ")[-1])
            elif "false" in line:
                monkey.false_m = int(line.split(" ")[-1])
                monkeys.append(monkey)
    
    # run the monkeys
    top_2 = [0,0]
    for i in range(20):
        for monkey in monkeys:
            monkey.do_routine(monkeys)

        if i == 19:
            top_2 = sorted([m.inspected for m in monkeys], reverse=True)[:2]

    return (top_2[0]*top_2[1],0)

if __name__ == '__main__':
    one,two = day_eleven("2022/inputs/day11/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)