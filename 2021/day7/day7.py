
positions = []
with open("input.txt", "r") as f:
    positions = [int(e) for e in f.readline().split(',')]

distance = [0 for e in positions]
distance2 = [0 for e in positions]
for i in range(0, len(positions)):
    for x in range(0, len(positions)):
        counter = abs(positions[x]-positions[i])
        distance[i] += counter
        distance2[i] += int(counter*(counter+1)/2)

print("#Day7 - Part1:", min(distance))
print('#Day7 - Part2:', min(distance2))   

