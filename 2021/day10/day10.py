import statistics

chunks = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}

def part1(lines):

    chunksPoint = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
    }

    illegals = []
    for line in lines:
        queue = []
        for c in line:
            if c in chunks.values():
                queue.append(c)
            elif c in chunks.keys():
                if queue[-1] == chunks[c]:
                    queue.pop()
                else: 
                    illegals.append(c)
                    break
    return sum([chunksPoint.get(c) for c in illegals])

def part2(lines):
    ends = {']': '[', ')': '(', '}': '{', '>': '<'}
    scores = []
    for line in lines:
        blocks = []
        err = False
        for char in line:
            if char in ends.values():
                blocks.append(char)
            elif char in ends.keys():
                if blocks[-1] == ends[char]:
                    blocks.pop()
                else:
                    err = True
                    break
        if not err:
            score = 0
            blocks.reverse()
            for b in blocks:
                score *= 5
                score += {'(': 1, '[': 2, '{': 3, '<': 4}[b]
            scores.append(score)
    return statistics.median(scores)

    
        

lines = []
with open("input.txt", "r") as f:
    lines = [e.strip() for e in f.readlines()]

print("#Day10 - Part1:", part1(lines))
print("#Day10 - Part2:", part2(lines))
