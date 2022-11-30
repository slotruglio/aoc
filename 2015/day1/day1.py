line = ""
with open("input.txt", "r") as f:
    line = f.readline()

floor = 0
index = -1
flag = False
for i in range(0, len(line)):
    if floor == -1 and not flag:
        flag = True
        index = i
    if line[i] == '(': floor += 1
    else: floor -= 1
    
print("#Day1 - Part 1:", floor)
print("#Day1 - Part 2:", index)