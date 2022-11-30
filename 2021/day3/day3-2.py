def getBit(n,list, i):
    zero = 0
    one = 0
    toReturn = ""

    for line in list:
        if line[i] == "0":
            zero += 1
        else: one += 1
    if zero > one:
        if n == 1: toReturn = "0"
        else: toReturn = "1"
    else:
        if n == 1:
            toReturn = "1"
        else: toReturn = "0"
    return toReturn

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    oxygen = lines.copy()
    co2 = lines.copy()

    oxygen_pattern = ""
    co2_pattern = ""
    for i in range(0, len(lines[0])):
        if len(oxygen) == len(co2) == 1: break

        if len(oxygen) > 1:
            oxygen_pattern = oxygen_pattern + getBit(1, oxygen, i)
            oxygen = [e for e in oxygen if e.startswith(oxygen_pattern)]

        if len(co2) > 1:
            co2_pattern = co2_pattern + getBit(0, co2, i)
            co2 = [e for e in co2 if e.startswith(co2_pattern)]

    oxygen_value = int(oxygen[0], 2)
    co2_value = int(co2[0], 2)

    print("oxygen: {}, co2: {}, life: {}".format(oxygen_value, co2_value, oxygen_value*co2_value))
