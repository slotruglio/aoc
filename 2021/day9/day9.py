from math import prod

def column(matrix, i):
    return [row[i] for row in matrix]

def minsInRange(matrix):
    minimus = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0:
                if j == 0: 
                    if matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j]:
                        minimus.append([matrix[i][j],i,j])
                elif j == len(matrix[i])-1:
                    if matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i+1][j]:
                        minimus.append([matrix[i][j],i,j])
                else:
                    if(
                        matrix[i][j] < matrix[i][j+1] 
                        and matrix[i][j] < matrix[i+1][j]
                        and matrix[i][j] < matrix[i][j-1]
                        ): minimus.append([matrix[i][j],i,j])

            elif i == len(matrix)-1:
                if j == 0: 
                    if matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i-1][j]:
                        minimus.append(matrix[i][j])
                elif j == len(matrix[i])-1:
                    if matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i-1][j]:
                        minimus.append([matrix[i][j],i,j])
                else:
                    if(
                        matrix[i][j] < matrix[i][j+1] 
                        and matrix[i][j] < matrix[i][j-1]
                        and matrix[i][j] < matrix[i-1][j]
                        ): minimus.append([matrix[i][j],i,j])
            
            else:
                if j == 0: 
                    if(
                        matrix[i][j] < matrix[i][j+1] 
                        and matrix[i][j] < matrix[i-1][j]
                        and matrix[i][j] < matrix[i+1][j]
                        ):
                        minimus.append([matrix[i][j],i,j])
                elif j == len(matrix[i])-1:
                    if(
                        matrix[i][j] < matrix[i][j-1] 
                        and matrix[i][j] < matrix[i-1][j]
                        and matrix[i][j] < matrix[i+1][j]
                        ):
                        minimus.append([matrix[i][j],i,j])
                else:
                    if(
                        matrix[i][j] < matrix[i][j+1] 
                        and matrix[i][j] < matrix[i][j-1]
                        and matrix[i][j] < matrix[i-1][j]
                        and matrix[i][j] < matrix[i+1][j]
                    ): minimus.append([matrix[i][j],i,j])
    return minimus

def part1(matrix):
    return sum([e[0]+1 for e in minsInRange(matrix)])

def part2():
    height = {(x,y): int(h) 
                for y,l in enumerate(open("input.txt", "r"))
                for x,h in enumerate(l.strip())}

    def neighbours(x, y):
        return filter(lambda n: n in height,
            [(x,y-1), (x,y+1), (x-1,y), (x+1, y)])

    def is_low(p):
        return all(height[p] < height[n]
            for n in neighbours(*p))

    low_points = [*filter(is_low, height)]

    def count_basin(p):
        if height[p] == 9: return 0
        del height[p]
        return 1 + sum(map(count_basin, neighbours(*p)))

    basins = [count_basin(p) for p in low_points]
    return prod(sorted(basins)[-3:])

matrix = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    
    for line in lines:
        row = []
        for n in line.strip():
            row.append(int(n))
        matrix.append(row)

print("#Day9 - Part 1:", part1(matrix))
print("#Day9 - Part2:",part2())



