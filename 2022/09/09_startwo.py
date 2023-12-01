import sys, math
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

def placeKnot(mat,num,knot):
    mat[knot[1]][knot[0]] = str(num)

def printMat(mat):
    str = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            str += mat[i][j]
        str += "\n"
    print(str)

directions = {"R":(1,0), "L":(-1,0), "U":(0,-1), "D":(0,1)}

mat = [["." for x in range(30)] for x in range(30)]


knots = [(14,14) for x in range(10)]
lastKnotPos = [(14,14) for x in range(10)]

placeKnot(mat,0,knots[0])
printMat(mat)

visited = set()
visited.add(knots[9])


print(knots)

for line in arq:
    direction, move = line.split(" ")
    dir = directions[direction]

    for i in range(int(move)):
        print("At start knots:",knots)
        print("At start last knots:",lastKnotPos)


        knots[0] = (knots[0][0] + dir[0], knots[0][1] + dir[1])
        for i in range(1,len(knots)):

            print(i,knots[i-1],knots[i],math.dist(knots[i-1],knots[i]))
            
            if math.dist(knots[i-1],knots[i]) > 1.9:
                knots[i] = lastKnotPos[i-1]
                if i == 9:
                    visited.add(knots[i])
            
            placeKnot(mat,i-1,knots[i-1])
            placeKnot(mat,".",lastKnotPos[i-1])
            placeKnot(mat,i,knots[i])
            placeKnot(mat,".",lastKnotPos[i])
           
            print("\t",knots[i],knots[i-1])
            print("\t",lastKnotPos[i],lastKnotPos[i-1])



        for i in range(len(knots)):
            lastKnotPos[i] = knots[i]
        print(knots)
        print(lastKnotPos)


        printMat(mat)
        a = input("...")

secondStar = len(visited)

print("Answer second star: {}".format(secondStar))