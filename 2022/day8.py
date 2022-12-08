import numpy as np

def day_eight(input):
    matrix = []
    with open(input) as f:
        for line in f.readlines():
            matrix.append([ int(x) for x in line.strip() ])

    visibles = 2*(len(matrix)-1) + 2*(len(matrix[0])-1)
    for i in range(1, len(matrix) -1):
        for j in range(1, len(matrix[i]) - 1):
            # row left
            if matrix[i][j] > max(matrix[i][:j]):
                visibles += 1
                continue
            # row right
            if matrix[i][j] > max(matrix[i][j+1:]):
                visibles += 1
                continue
            # col up
            if matrix[i][j] > max(e[j] for e in matrix[:i]):
                visibles += 1
                continue
            # col down
            if matrix[i][j] > max(e[j] for e in matrix[i+1:]):
                visibles += 1
                continue

    return (visibles,0)


if __name__ == '__main__':
    one,two = day_eight("2022/inputs/day8/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)