keywords = ["turn on", "turn off", "toggle"]
matrix = []
commands = []

for i in range(0,1000):
    row = []
    for j in range(0,1000):
        row.append(0)
    matrix.append(row)

def turnOn(part, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if part == 1: matrix[i][j] = 1
            else: matrix[i][j] +=1

def turnOff(part, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if part == 1: matrix[i][j] = 0
            else: 
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1

def toggle(part, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if part == 1:
                if matrix[i][j] == 1: matrix[i][j] = 0
                else: matrix[i][j] = 1
            else:
                matrix[i][j] += 2

def doSomething(part, command):
    start, end = command.split("through")
    x,y = start.split()[-1].split(',')
    start = [int(x), int(y)]
    x,y = end.split(',')
    end = [int(x), int(y)]

    if command.count("turn on") > 0:
        turnOn(part, start, end)
    elif command.count("turn off") > 0:
        turnOff(part, start, end)
    else: toggle(part, start, end)

def countOn():
    s = 0
    for row in matrix:
        for light in row:
            if light == 1:
                s+=1
    return s

def totalBrightness():
    s = 0
    for row in matrix:
        for light in row:
            s+=light
    return s

def part1():
    for command in commands:
        doSomething(1, command)
    return countOn()

def part2():
    for command in commands:
        doSomething(2, command)
    return totalBrightness()

with open("input.txt", "r") as f:
    commands = f.readlines()


print("#Day6 - Part1:",part1())
matrix = []

for i in range(0,1000):
    row = []
    for j in range(0,1000):
        row.append(0)
    matrix.append(row)

print("#Day6 - Part2:",part2())

