def day_ten(input):
    signals = { 20: 0, 60: 0, 100: 0, 140:0, 180:0, 220: 0}
    with open(input) as f:
        cycles = 0
        X = 1
        for line in f.readlines():
            cycles += 1
            if cycles in signals.keys():
                signals[cycles] = cycles*X
            line = line.strip()
            if line == "noop":
                continue
            op, val = line.split(" ")
            cycles += 1
            if cycles in signals.keys():
                signals[cycles] = cycles*X
            X += int(val)
    
    return (sum(signals.values()),0)

if __name__ == '__main__':
    one,two = day_ten("2022/inputs/day10/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)