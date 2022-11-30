def column(matrix, i):
    return [row[i] for row in matrix]

def countTrue(list):
    trueCounter = 0
    for x in list:
        if x[1] == True: trueCounter += 1
    if trueCounter == 5: return True
    
def boardChecker(board):
    for row in board:
        if countTrue(row): return True
    for i in range(0, len(board)):
        if countTrue(column(board, i)): return True
    return False

def winningBoardAtNumber(numbers, boards):
    curr = -1
    counter = 0
    for extracted in numbers:
        curr = extracted
        for board in boards:
            for row in board:
                for x in row:
                    if x[0] == extracted:
                        x[1] = True
        counter += 1
        # bingo check
        if counter > 4:
            for board in boards:
                if boardChecker(board):
                    return [curr, board, boards.index(board)]
    return []

with open("input.txt", "r") as f:
    numbers = [int(e) for e in f.readline().split(',')]

    lines = f.readlines()

    boards = []
    curr_board = []

    # create boards with numbers as False
    for line in lines:
        if line != "\n":
            line = line.strip()
            row = line.split(" ")
            tmp = []
            for n in row:
                try:
                    x = int(n)
                    tmp.append([x, False])
                except: pass
            curr_board.append(tmp)
            if len(curr_board) == 5:
                boards.append(curr_board)
                curr_board = [] 

    curr_extracted = -1
    winning_board = []

    while len(boards) > 0:
        tmp = winningBoardAtNumber(numbers, boards)
        curr_extracted = tmp[0]
        winning_board = tmp[1]
        index = tmp[2]
        del boards[index]

    sum = 0
    for row in winning_board:
        for x in row:
            if x[1] == False: sum += x[0]
    print("Final score is {}*{} = {}".format(sum, curr_extracted, sum*curr_extracted))