import hashlib

inputLine = "yzbqklnj"
part1 = 0
part2 = 0
found1 = False
found2 = False

while not found1 or not found2:
    result = hashlib.md5((inputLine+str(part1)).encode("utf-8")).hexdigest()
    if result[0:5] == "00000" and not found1:
        found1 = True
    elif not found1: part1 += 1
    result = hashlib.md5((inputLine+str(part2)).encode("utf-8")).hexdigest()
    if result[0:6] == "000000" and not found2:
        found2 = True
    elif not found2: part2 += 1

print("#Day4 - Part 1:",part1)
print("#Day4 - Part 2:",part2)

