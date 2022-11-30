lines = []
def part1(lines):
    vowelsList = ["a", "e", "i", "o", "u"]
    notLines = ["ab", "cd", "pq", "xy"]
    nice = 0
    for line in lines:
        vowels = False
        twice = False
        banned = False

        count = 0
        for e in vowelsList:
            count += line.count(e)
        if count > 2 : vowels = True

        count = 1
        curr = line[0]
        for i in range(1, len(line)):
            if count > 1:
                twice = True
                break
            if curr == line[i]:
                count += 1
            else:
                count = 1
                curr = line[i]
        
        count = 0
        for e in notLines:
            if line.count(e) > 0:
                count += 1
                break
        if count == 0 : banned = True

        if vowels and twice and banned: nice += 1

    return nice

def part2(s):

    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second


with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0
for s in lines:
    if part2(s):
        count += 1

print("#Day5 - Part1:", part1(lines))
print("#Day5 - Part2:", count)

