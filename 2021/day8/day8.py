lines = []

def part1():
    count = 0
    for line in lines:
        output = line.split('|')[1]
        digits = output.split()
        for digit in digits:
            if len(digit) in (2,4, 3, 7):
                count += 1
    return count

def part2():
    s = 0
    for pattern,output in [line.split('|') for line in lines]:
        l = {len(s): set(s) for s in pattern.split()}

        n = ''
        for o in map(set, output.split()): 
            if len(o) == 2: n += '1'
            if len(o) == 3: n += '7'
            if len(o) == 4: n += '4'
            if len(o) == 7: n += '8'
            if len(o) == 5 and len(o&l[4]) == 2: n += '2'
            if len(o) == 5 and len(o&l[4]) == 3 and len(o&l[2]) == 1: n += '5'
            if len(o) == 5 and len(o&l[4]) == 3 and len(o&l[2]) == 2: n += '3'
            if len(o) == 6 and len(o&l[4]) == 4: n += '9'
            if len(o) == 6 and len(o&l[4]) == 3 and len(o&l[2]) == 1: n += '6'
            if len(o) == 6 and len(o&l[4]) == 3 and len(o&l[2]) == 2: n += '0'
            
        s += int(n)
    return s

with open("input.txt", "r") as f:
    lines = f.readlines()

print("#Day8 - Part1:",part1())
print("#Day8 - Part2:", part2())