import numpy as np

maxX = 0
maxY = 0
fold = []
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    tmp = line.split(',')
    if len(tmp) == 2:
        if maxX < int(tmp[0]):
            maxX = int(tmp[0])
        if maxY < int(tmp[1]):
            maxY = int(tmp[1])
    else:
        tmp2 = line.split('=')
        if len(tmp2) == 2:
            if tmp2[0][-1] == 'y':
                fold.append(['y',int(tmp2[1])])
            else: fold.append(['x',int(tmp2[1])])

matrix = np.zeros((5000, 5000), dtype=bool)

for line in lines:
    tmp = line.split(',')
    if len(tmp) == 2:
        matrix[int(tmp[1])][int(tmp[0])] = True
counters = []
for op, val in fold:
    if op == 'x': 
        half1 = matrix[:,:val]
        half2 = matrix[:,2*val:val:-1]
        matrix = half1 | half2
    else:
        half1 = matrix[:val]
        half2 = matrix[2*val:val:-1,:]
        matrix = half1 | half2
    counter = 0
    for row in matrix:
        for val in row:
            if val: counter+= 1
    counters.append(counter)

print("#Day13 - Part1:",counters[0])

for row in matrix:
    for w in row:
        if w: print('█', end='')
        else: print(' ', end='')
    print(' ')
