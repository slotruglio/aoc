import numpy as np

def day_nine(input):
    knots = np.zeros((10,2), dtype=int)
    positions_one = set()
    positions_two = set()

    directions = {"R": [1,0], "L": [-1,0], "U": [0,1], "D": [0,-1]}
    with open(input, 'r') as f:
        for line in f.readlines():
            direction, steps = line.strip().split(" ")
            for step in range(int(steps)): 
                knots[0] += directions[direction] # move head
                for tail in range(1, len(knots)): # move each knot fo the tail
                    diff = knots[tail-1] - knots[tail]
                    if any(np.abs(diff) == 2):
                        knots[tail] += np.sign(diff)
                positions_one.add((knots[1,0], knots[1,1])) # add visited position for first knot of tail
                positions_two.add((knots[9,0], knots[9,1])) # add visited position for last knot of tail
    return (len(positions_one), len(positions_two))    

if __name__ == '__main__':
    one,two = day_nine("2022/inputs/day9/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)