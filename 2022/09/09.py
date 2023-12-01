import sys, math
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]


def printMat(mat):
    str = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            str += mat[i][j]
        str += "\n"
    print(str)

directions = {"R":(1,0), "L":(-1,0), "U":(0,-1), "D":(0,1)}

mat = [["." for x in range(6)] for x in range(5)]

headPos = (0,4)
tailPos = (0,4)
lastHeadPos = headPos
lastTailPos = tailPos
mat[tailPos[1]][tailPos[0]] = "T"
mat[headPos[1]][headPos[0]] = "H"


printMat(mat)

visited = set()
visited.add(tailPos)

for line in arq:
    direction, move = line.split(" ")

    dir = directions[direction]

    for i in range(int(move)):
        headPos = (headPos[0] + dir[0], headPos[1] + dir[1])

        if math.dist(headPos,tailPos) > 1.9:
            tailPos = lastHeadPos
            visited.add(tailPos)
        
        #mat[headPos[1]][headPos[0]] = "H"
        #mat[lastHeadPos[1]][lastHeadPos[0]] = "."
        #mat[lastTailPos[1]][lastTailPos[0]] = "."
        #mat[tailPos[1]][tailPos[0]] = "T"   

        #print(headPos,dir,tailPos)
        #printMat(mat)
        #a = input("...")

        lastTailPos = tailPos
        lastHeadPos = headPos

firstStar = len(visited)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))