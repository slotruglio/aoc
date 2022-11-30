with open("input.txt", "r") as f:
    lines = [e.strip() for e in f.readlines()]

    max_x = -1
    max_y = -1
    for line in lines:
        tmp = line.split("->")
        start = tmp[0]
        end = tmp[1]
        tmp1 = start.split(',')
        tmp2 = end.split(',')

        if max_x < int(tmp1[0]): max_x = int(tmp1[0])
        if max_x < int(tmp2[0]): max_x = int(tmp2[0])
        if max_y < int(tmp1[1]): max_y = int(tmp1[1])
        if max_y < int(tmp2[1]): max_y = int(tmp2[1])

    matrix = []
    for i in range(0, max_x+1):
        row = []
        for j in range(0, max_y+1):
            row.append(0)
        matrix.append(row)
    
    for line in lines:
        tmp = line.split("->")
        start = tmp[0]
        end = tmp[1]
        x1y1 = start.split(',')
        x2y2 = end.split(',')

        x1 = int(x1y1[0])
        y1 = int(x1y1[1])
        x2 = int(x2y2[0])
        y2 = int(x2y2[1])

        if y1 == y2:
            if x1 < x2:
                for i in range(x1, x2+1):
                    matrix[y1][i] += 1
            else:
                for i in range(x2, x1+1):
                    matrix[y1][i] += 1
        elif x1 == x2:
            if  y1 < y2:
                for i in range(y1, y2+1):
                    matrix[i][x1] += 1
            else:
                for i in range(y2, y1+1):
                    matrix[i][x2] += 1
    counter = 0
    for row in matrix:
        for x in row:
            if x > 1: counter += 1

    print("Solution is: ",counter)

