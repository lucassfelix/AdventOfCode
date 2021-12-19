import sys,math
from collections import defaultdict
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines() if line != '\n']

index = -1

scannersRelative = defaultdict(list)
scannersPos = [(0,0,0)]
absolutePoints = set()

for line in input:
    if line[1] == '-':
        index += 1
        continue
    x,y,z = map(int,line.split(","))
    scannersRelative[index].append((x,y,z))
    if index == 0:
        absolutePoints.add((x,y,z))


def rotateX(scanner, turns):
    for i in range(turns):
        newPoints = []
        for point in scannersRelative[scanner]:
            newY = point[2]
            newZ = -point[1]
            newPoints.append((point[0],newY,newZ))
        scannersRelative[scanner] = newPoints

def rotateY(scanner, turns):
    for i in range(turns):
        newPoints = []
        for point in scannersRelative[scanner]:
            newZ = point[0]
            newX = -point[2]
            newPoints.append((newX,point[1],newZ))
        scannersRelative[scanner] = newPoints

def rotateZ(scanner, turns):
    for i in range(turns):
        newPoints = []
        for point in scannersRelative[scanner]:
            newX = point[1]
            newY = -point[0]
            newPoints.append((newX,newY,point[2]))
        scannersRelative[scanner] = newPoints

def manhattanDistance(p1,p2):
    return sum((abs(p1[0] - p2[0]),abs(p1[1] - p2[1]),abs(p1[2] - p2[2])))

def difference(p1,p2):
    return (p2[0] - p1[0], p2[1] - p1[1],p2[2] - p1[2])

def normalizeScanner(scannerPos,scannerIndex):
    newPoints = []
    for point in scannersRelative[scannerIndex]:
        newPoint = (point[0] - scannerPos[0],point[1] - scannerPos[1],point[2] - scannerPos[2])
        newPoints.append(newPoint)
        absolutePoints.add(newPoint)
    scannersRelative[scannerIndex] = newPoints


def getScannerPos(scannerIndex):
    for x in range(4):
        for y in range(4):
            for z in range(4):
                sameDiff = defaultdict(int)
                for zero in absolutePoints:
                    for one in scannersRelative[scannerIndex]:
                        diff = difference(zero,one)
                        sameDiff[diff] += 1
                for a in sameDiff.keys():
                    if sameDiff[a] >= 12:
                        return a,True
                rotateZ(scannerIndex,1)
            rotateY(scannerIndex,1)
        rotateX(scannerIndex,1)
    return None,False



indexes = [i for i in range(1,len(scannersRelative.keys()))]

while len(indexes) != 0:
    newIndexes = []
    for i in indexes:
        pos,found = getScannerPos(i)
        #print(i,found,pos)
        if found:
            scannersPos.append(pos)
            newIndexes.append(i)
            normalizeScanner(pos,i)
    for rem in newIndexes:
        indexes.remove(rem)

firstStar = len(absolutePoints)

for i in range(len(scannersPos)):
    for j in range(i,len(scannersPos)):
        secondStar = max(secondStar,manhattanDistance(scannersPos[i],scannersPos[j]))


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))