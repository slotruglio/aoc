def day_ten(input):
    signals = { 20: 0, 60: 0, 100: 0, 140:0, 180:0, 220: 0}
    monitor = [['.']*40, ['.']*40, ['.']*40, ['.']*40, ['.']*40, ['.']*40]

    with open(input) as f:
        cycles = 0
        X = 1
        for line in f.readlines():
            cycles += 1
            if cycles in signals.keys():
                signals[cycles] = cycles*X
            if (cycles-1)%40 in range(X-1, X+2):
                monitor[(cycles-1)//40][(cycles-1)%40] = '#'
            line = line.strip()
            if line == "noop":
                continue
            op, val = line.split(" ")
            cycles += 1
            if (cycles-1)%40 in range(X-1, X+2):
                monitor[(cycles-1)//40][(cycles-1)%40] = '#'

            if cycles in signals.keys():
                signals[cycles] = cycles*X
            X += int(val)

    # parse monitor into a string where each row is a line followed by \n
    monitor = "\n".join(["".join(row) for row in monitor])

    return (sum(signals.values()), "\n"+monitor)

if __name__ == '__main__':
    one,two = day_ten("2022/inputs/day10/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)
