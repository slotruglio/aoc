memory = []

def findInMemory(register):
    for mem in memory:
        if mem[0].count(register) > 0:
            return mem[1]
    return -1

def insert(tuplex):
    if memory.count(tuplex[0]) > 0:
        memory[memory.index(tuplex[0])][1] = tuplex[1]
    else:
        memory.append(tuplex)

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines: 
        operation, destination = line.split("->")
        destination = destination.strip()
        operators = operation.strip().split()
        if len(operators) == 1:
            try:
                insert([destination, int(operators[0])])
            except:
                insert([destination, findInMemory(operators[0])])
        elif len(operators) == 2:
            insert([destination, ~findInMemory(operators[1])&65535])
        else:
            if operators[1] == "AND":
                insert([destination, findInMemory(operators[0])&findInMemory(operators[-1])])
            elif operators[1] == "OR":
                insert([destination, findInMemory(operators[0])|findInMemory(operators[-1])])
            elif operators[1] == "LSHIFT":
                insert([destination, findInMemory(operators[0])<<int(operators[-1])])
            else: insert([destination, findInMemory(operators[0])>>int(operators[-1])])

memory.sort()
print(memory)
print("#Day7 - Part1:", findInMemory('a'))