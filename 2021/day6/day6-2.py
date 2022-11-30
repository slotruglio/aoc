fish = []
with open("input.txt", "r") as f:
    for e in f.readline().split(','):
        fish.append(int(e))

days = int(input("How many days? "))
sonAge = int(input("What is son's timer? "))

ages = []
for i in range(0, sonAge+1):
    ages.append(0)

for f in fish:
    ages[f] += 1

for day in range(1, days+1):
    ages.append(ages.pop(0))
    ages[6] += ages[8]

sum = 0
for age in ages:
    sum += age
print(sum)