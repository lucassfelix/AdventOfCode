import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip().replace("X","A").replace("Y","B").replace("Z","C").split(" ") for line in file.readlines()]

points = {"A":1,"B":2,"C":3}
winsFrom = {"A":"C","B":"A","C":"B"}

victoryPoints = {"A":0,"B":3,"C":6}

for play in input:
    oponnent,player = play

    firstStar += points[player]

    secondStar += victoryPoints[player]

    if winsFrom[player] == oponnent:
        firstStar += 6
    elif player == oponnent:
        firstStar += 3
    else:
        firstStar += 0


    if player == "A":
        secondStar += points[winsFrom[oponnent]]
    elif player == "B":
        secondStar += points[oponnent]
    else: 
        secondStar += points[winsFrom[winsFrom[oponnent]]]

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))