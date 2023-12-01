import sys
from ast import literal_eval
from itertools import zip_longest
from functools import cmp_to_key

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

def getPointsInRange(p1,p2):
    points = []
    x1,y1 = p1
    x2,y2 = p2
    if x1 > x2:
        for i in range(x2+1,x1):
            points.append((i,y1))
        return points
    if x1 < x2:
        for i in range(x1+1,x2):
            points.append((i,y1))
        return points
    if y1 > y2:
        for i in range(y2+1,y1):
            points.append((x1,i))
        return points
    if y1 < y2:
        for i in range(y1+1,y2):
            points.append((x1,i))
        return points

blocked = set()

maxHeight = 0

for line in arq:
    points = line.split("->")
    pRange = []
    for p in points:
        x,y = p.split(",")
        x = int(x.strip())
        y = int(y.strip())
        maxHeight = max(y,maxHeight)
        pRange.append((x,y))
        blocked.add((x,y))
    for i in range(len(pRange)-1):
        blocked.update(getPointsInRange(pRange[i],pRange[i+1]))

print(blocked)

sandOrigin = (500,0)

floor = maxHeight + 2

blocked.update(getPointsInRange((0,floor),(1000,floor)))

stopCountingFirstStar = False

while True:
 

    newSand = sandOrigin
    #print("Sand Number",firstStar)

    while True:
        
        #print("\t",newSand)


        if (newSand[0], newSand[1]+1) not in blocked:
            newSand = (newSand[0], newSand[1]+1)
            continue
        
        #print("\t Blocked Down")

        if (newSand[0]-1, newSand[1]+1) not in blocked:

            newSand = (newSand[0]-1, newSand[1]+1)
            continue

        #print("\t Blocked Down-Left")

        if (newSand[0]+1, newSand[1]+1) not in blocked:

            newSand = (newSand[0]+1, newSand[1]+1)
            continue
        #print("\t Blocked Down-Right")
        
        #print("\t Unit Set At:",newSand)

        blocked.add(newSand)
        break

    if not stopCountingFirstStar:
        firstStar += 1
    secondStar += 1
    if newSand[1] > maxHeight:
        stopCountingFirstStar = True

    if newSand == (500,0):
        break

    pass




print("Answer first star: {}".format(firstStar-1))
print("Answer second star: {}".format(secondStar))

