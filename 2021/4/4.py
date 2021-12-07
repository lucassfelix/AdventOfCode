import copy

def firstStar(numbers, boards):
    for num in numbers:
        for boardIndex,board in enumerate(boards):
            for lineIndex,line in enumerate(board):
                try:
                    line.remove(num)
                except ValueError:
                    pass
                if(len(line) == 0):
                    #print("Winner number : {}  Winner board: {}  Winner line: {}".format(num, boardIndex, lineIndex ))
                    result = 0
                    for auxLine in range(5):
                        result += sum(board[auxLine])
                    return result * num
    return -1


def notminusone(number):
    if number == -1:
        return False
    return True

def secondStar(numbers, boards):
    lastWinner = 0
    results = {}
    for num in numbers:
        for boardIndex,board in enumerate(boards):
            for lineIndex,line in enumerate(board):
                try:
                    line.remove(num)
                except ValueError:
                    pass
                if(len(line) == 0):
                    #print("Winner number : {}  Winner board: {}  Winner line: {}".format(num, boardIndex, lineIndex ))
                    if boardIndex not in results.keys():
                        result = 0
                        for auxLine in range(5):
                            result += sum(board[auxLine])
                        results[boardIndex] = result * num
                        lastWinner = boardIndex
    return results[lastWinner]
                        



with open("input.txt") as f:
    numbers = [int(aux) for aux in f.readline().split(",")]
    lines = [[line for line in board.split("\n") if line != ''] for board in f.read().split("\n\n")] 

boards = [[] for i in range(len(lines))]

for i in range(len(lines)):
    for num in lines[i]:
        boards[i].append([int(aux) for aux in num.split(" ") if aux != ''])

for i in range(len(boards)):
    for j in range(5):
        boards[i].append([boards[i][0][j], boards[i][1][j],boards[i][2][j],boards[i][3][j],boards[i][4][j]])



print("Answer first star: {}".format(firstStar(numbers,copy.deepcopy(boards))))
print("Answer second star: {}".format(secondStar(numbers,boards)))


