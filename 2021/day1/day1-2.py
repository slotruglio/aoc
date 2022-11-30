with open("input.txt", "r") as f:
    values = [int(e) for e in f.readlines()]
    windowsSum = list()

    index = 0
    for value in values:
        if(index+2 < len(values)):
            sum = value
            sum += values[index+1]
            sum += values[index+2]
            windowsSum.append(sum)
        index += 1

    isFirst = True
    cValue = 0
    counter = 0

    for value in windowsSum :
        if isFirst: isFirst = False
        else:
            if cValue < value :
                counter += 1
        cValue = value

    print("Total increment = ", counter) 

