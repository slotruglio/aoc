import numpy as np

def day_eight(input):
    matrix = []
    with open(input) as f:
        for line in f.readlines():
            matrix.append([ int(x) for x in line.strip() ])

    visibles = 2*(len(matrix)-1) + 2*(len(matrix[0])-1) # Part 1
    scenic_score = 0 # Part 2
    for i in range(1, len(matrix) -1):
        for j in range(1, len(matrix[i]) - 1):
            left, right, up, down = 0, 0, 0, 0
            visible = [False, False, False, False]
            # row left
            for k in range(j-1, -1, -1):
                left += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
                if k == 0:
                    visible[0] = True

            # row right
            for k in range(j+1, len(matrix[i])):
                right += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
                if k == len(matrix[i]) - 1:
                    visible[1] = True
            # col up
            for k in range(i-1, -1, -1):
                up += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
                if k == 0:
                    visible[2] = True
            # col down
            for k in range(i+1, len(matrix)):
                down += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
                if k == len(matrix) - 1:
                    visible[3] = True
            scenic_score = max(scenic_score, left*right*up*down)
            if any(visible):
                visibles += 1

    return (visibles,scenic_score)


if __name__ == '__main__':
    one,two = day_eight("2022/inputs/day8/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)