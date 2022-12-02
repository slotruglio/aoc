BEATERS = [2,3,1]

SHAPE_SCORE = {
    "A": 1, #ROCK
    "B": 2, #PAPER
    "C": 3, #SCISSORS
    "X": 1, #ROCK
    "Y": 2, #PAPER
    "Z": 3  #SCISSORS
}

OUTCOME_SCORE = {
    "LOST": 0,
    "DRAW": 3,
    "WIN":  6
}

DESIRED_OUTCOME = {
    "X": "LOST",
    "Y": "DRAW",
    "Z": "WIN"
}

# calculate player's outcome given the two shapes 
def outcome_with_array(opponent, shape):
    if opponent == shape:
        return OUTCOME_SCORE["DRAW"]
    if shape == BEATERS[opponent-1]:
        return OUTCOME_SCORE["WIN"]
    else:
        return OUTCOME_SCORE["LOST"]

# calculate shape score for the desired outcome
def outcome_score_for_shape(desired, op_score):
    if desired == "DRAW":
        return op_score
    if desired == "LOST":
        return BEATERS.index(op_score)+1
    else:
        return BEATERS[op_score-1]

def day_2_full(input):
    score_1 = 0
    score_2 = 0
    with open(input, 'r') as file:
        for line in file.readlines():
            opponent, shape = line.strip().split(' ')
            op_score = SHAPE_SCORE[opponent]
            # part one calculus
            score_1 += SHAPE_SCORE[shape]
            score_1 += outcome_with_array(op_score, SHAPE_SCORE[shape])
            # part two calculus
            desired = DESIRED_OUTCOME[shape]
            score_2 += outcome_score_for_shape(desired, op_score)
            score_2 += OUTCOME_SCORE[desired]

    (score_1, score_2)

def main():
    input = "2022/inputs/day2/input.txt"
    one,two = day_2_full(input)
    print("Part One: "+str(one))
    print("Part Two: "+str(two))

if __name__ == '__main__':
    main()
    exit(0)
