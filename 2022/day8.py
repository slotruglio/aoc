import numpy as np

def day_eight(input):
    matrix = []
    with open(input) as f:
        for line in f.readlines():
            matrix.append([ int(x) for x in line.strip() ])

    visibles = 2*(len(matrix)-1) + 2*(len(matrix[0])-1) # Part 1
    scenic_score = 0 # Part 2
    for i in range(1, len(matrix) -1):
        # PART 1
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
            
        # PART 2
        for j in range(1, len(matrix[i]) - 1):
            left = 0
            # row left
            for k in range(j-1, -1, -1):
                left += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
            # row right
            right = 0
            for k in range(j+1, len(matrix[i])):
                right += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
            # col up
            up = 0
            for k in range(i-1, -1, -1):
                up += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
            # col down
            down = 0
            for k in range(i+1, len(matrix)):
                down += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
            scenic_score = max(scenic_score, left*right*up*down)

    return (visibles,scenic_score)


if __name__ == '__main__':
    one,two = day_eight("2022/inputs/day8/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)