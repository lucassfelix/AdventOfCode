import sys, itertools
from collections import defaultdict
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

player1Start = int(arq[0].split(":")[1].strip(" "))
player2Start = int(arq[1].split(":")[1].strip(" "))


p1Pos = player1Start
p2Pos = player2Start

p1Score = 0
p2Score = 0

dice = 1

iter = 0

p1Turn = True

while p1Score < 1000 and p2Score < 1000:
#for i in range(100):#
    #print(p1Pos,p1Score,p2Pos,p2Score)
    iter += 3
    if p1Turn:
        p1Pos =  (p1Pos + (3*dice + 3)) % 10
        p1Score += 10 if p1Pos == 0 else p1Pos
    else:
        p2Pos =  (p2Pos + (3*dice + 3)) % 10
        p2Score += 10 if p2Pos == 0 else p2Pos
    p1Turn = not p1Turn
    dice = 100 if (dice + 3) % 100 == 0 else (dice + 3) % 100
#print(p1Pos,p1Score,p2Pos,p2Score)


p1Wins = 0
p2Wins = 0

recordedWins = {}

dice = [sum(i) for i in itertools.product([1,2,3],repeat =3)]


p1 = (player1Start,0)
p2 = (player2Start,0)

winScore = 21

def quantumGame(p1,p2,p1Turn):
    global p1Wins, p2Wins

    #print("{} P1:{} P2:{}".format("P1 Turn" if p1Turn else "P2 Turn",p1,p2))    
    #input()
    state = (p1,p2,p1Turn)
    if state in recordedWins:
        #print("Found pair {} in recorded wins. Value {}".format((p1,p2),recordedWins[(p1,p2)]))
        p1Wins += recordedWins[state][0]
        p2Wins += recordedWins[state][1]
        return (recordedWins[state][0],recordedWins[state][1])
    localP1Wins = 0
    localP2Wins = 0

    

    if p1Turn:

        for i in dice:
            newPos = (p1[0] + i) % 10
            newScore = p1[1] + (10 if newPos == 0 else newPos)
            newP1 = (newPos,newScore)
            #print("\tNew P1:{}".format(newP1))
            #input()
            #print(newP1)
            if (newScore >= winScore):
                #print("\tFound Win for P1")
                p1Wins += 1
                localP1Wins += 1
                pair = (newP1,p2)
                #print("Local wins {}".format((localP1Wins,localP2Wins)))
                #input()
            else:
                p1Aux, p2aux = quantumGame(newP1,p2,False)
                localP1Wins += p1Aux
                localP2Wins += p2aux
                #print("Received more wins {}".format((localP1Wins,localP2Wins)))

    

    else:

        for i in dice:
            newPos = (p2[0] + i) % 10
            newScore = p2[1] + (10 if newPos == 0 else newPos)
            newP2 = (newPos,newScore)
            #print("\tNew P2:{}".format(newP2))
            #input()
            if (newScore >= winScore):
                #print("\tFound Win for P2")
                pair = (p1, newP2)
                p2Wins += 1
                localP2Wins += 1
                #print("Local wins {}".format((localP1Wins,localP2Wins)))
                #input()
            else:
                p1Aux, p2aux = quantumGame(p1,newP2,True)
                localP1Wins += p1Aux
                localP2Wins += p2aux
                #print("Received more wins {}".format((localP1Wins,localP2Wins)))


    
    pair = (p1,p2,p1Turn)
    if pair in recordedWins:
        recordedWins[pair] = (recordedWins[pair][0] + localP1Wins, recordedWins[pair][1] + localP2Wins)
    else:
        recordedWins[pair] = (localP1Wins,localP2Wins)
    #print("Pair {} ended execution and saved recorded wins as {}".format(pair,recordedWins[pair]))
    return (localP1Wins,localP2Wins)


    

quantumGame(p1,p2,True)
#print(recordedWins)


firstStar = min(p1Score,p2Score) * iter
secondStar = max(p1Wins,p2Wins)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))