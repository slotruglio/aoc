def day_14(input):
    rocks = []
    with open(input, 'r') as f:
        for line in f.readlines():
            points = line.strip().split("->")
            for i in range(1, len(points)):
                curr = points[i].split(",")
                prev = points[i-1].split(",")
                if curr[0].strip() == prev[0].strip():
                    start = min(int(curr[1]), int(prev[1]))
                    end = max(int(curr[1]), int(prev[1]))+1
                    for n in range(start, end):
                        rocks.append((int(curr[0]), n))
                else:
                    start = min(int(curr[0]), int(prev[0]))
                    end = max(int(curr[0]), int(prev[0]))+1
                    for n in range(start, end):
                        rocks.append((n, int(prev[1])))
    def part_1(rocks):
        sim = set(rocks)
        lowest = max([x[1] for x in sim])

        run = True
        while run:
            sand = (500, 0)
            while True:
                x,y = sand
                if y >= lowest:
                    run = False
                    break
                elif (x,y+1) not in sim:
                    sand = (x,y+1)
                elif (x-1, y+1) not in sim:
                    sand = (x-1, y+1)
                elif (x+1, y+1) not in sim:
                    sand = (x+1, y+1)
                else:
                    sim.add(sand)
                    break
        return len(sim)-len(set(rocks))

    def part_2(rocks):
        sim = set(rocks)
        lowest = max([x[1] for x in sim]) + 2

        run = True
        while run:
            sand = (500, 0)
            while True:
                x,y = sand
                if y >= lowest:
                    run = False
                    break
                elif (x,y+1) not in sim and y+1 < lowest:
                    sand = (x,y+1)
                elif (x-1, y+1) not in sim and y+1 < lowest:
                    sand = (x-1, y+1)
                elif (x+1, y+1) not in sim and y+1 < lowest:
                    sand = (x+1, y+1)
                else:
                    sim.add(sand)
                    if sand == (500,0):
                        run = False
                    break
        return len(sim)-len(set(rocks))

    return (part_1(rocks),part_2(rocks))

if __name__ == '__main__':
    one,two = day_14("2022/inputs/day14/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)