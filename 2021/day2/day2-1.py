with open("input.txt", "r") as f:
    x = 0
    y = 0

    lines = f.readlines()
    for line in lines :
        tmp = line.split(" ")
        if "forward" in tmp[0]:
            x += int(tmp[1])
        elif "down" in tmp[0]:
            y += int(tmp[1])
        else:
            y -= int(tmp[1])
    print("x = ", x)
    print("y = ", y)
    print("x*y = ", x*y)