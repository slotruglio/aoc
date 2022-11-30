def part1(moves):
    x = 0
    y = 0
    old_positions = []
    for i in range(0, len(moves)):
        old_positions.append("{},{}".format(x,y))
        if moves[i] == "<":
            x -= 1
        elif moves[i] == ">":
            x += 1
        elif moves[i] == "v":
            y -= 1
        elif moves[i] == "^":
            y += 1
    return len(set(old_positions))

moves = ""
with open("input.txt", "r") as f:
    moves = f.readline().strip()

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
santaTurn = True
isFirst = True
old_position = []

for move in moves:
    if isFirst:
        isFirst = False
        old_position.append("0,0")
    else:
        old_position.append("{},{}".format(santa_x, santa_y))
        old_position.append("{},{}".format(robo_x, robo_y))
    if santaTurn:
        if move == "<":
            santa_x -= 1
        elif move == ">":
            santa_x += 1
        elif move == "v":
            santa_y -= 1
        elif move == "^":
            santa_y += 1
    else:
        if move == "<":
            robo_x -= 1
        elif move == ">":
            robo_x += 1
        elif move == "v":
            robo_y -= 1
        elif move == "^":
            robo_y += 1
    santaTurn = not santaTurn


print("#Day3 - Part 1:", part1(moves))
print("#Day3 - Part 2", len(set(old_position)))
