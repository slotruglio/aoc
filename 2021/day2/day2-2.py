with open("input.txt", "r") as f:
    x = 0
    y = 0
    aim = 0

    lines = f.readlines()
    for line in lines :
        tmp = line.split(" ")
        if "forward" in tmp[0]:
            x += int(tmp[1])
            y += aim*int(tmp[1])
        elif "down" in tmp[0]:
            aim += int(tmp[1])
        else:
            aim -= int(tmp[1])
    print("x = ", x)
    print("y = ", y)
    print("x*y = ", x*y)