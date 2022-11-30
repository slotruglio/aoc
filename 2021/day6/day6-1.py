fish = []
with open("dummy.txt", "r") as f:
    for e in f.readline().split(','):
        fish.append(int(e))

days = int(input("How many days? "))

print("Initial state: ", fish)
for i in range(1, days+1):
    old_len = len(fish)
    newFish = 0
    for j in range(0, len(fish)):
        if fish[j] == 0:
            fish[j] = 6
            newFish += 1
        else: fish[j] -= 1
    for k in range(0, newFish):
        fish.append(8)

print("There are",len(fish), "lanternfish")
