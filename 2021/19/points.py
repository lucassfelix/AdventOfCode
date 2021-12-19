import sys,math
from collections import defaultdict

file = open(sys.argv[1])

input = [line.strip() for line in file.readlines()]

index = 0

scannersRelative = defaultdict(list)

for line in input:
    if len(line) == 0:
        index += 1
        continue
    x,y,z = map(int,line.split(","))
    scannersRelative[index].append((x,y,z))

def rotateY(scanner, turns):
    for i in range(turns):
        newPoints = []
        for point in scannersRelative[scanner]:
            newZ = point[0]
            newX = -point[2]
            newPoints.append((newX,point[1],newZ))
        scannersRelative[scanner] = newPoints

def distanceBetweenPoints(p1,p2):
    return math.pow(p2[0]-p1[0],2) + math.pow(p2[1]-p1[1],2) + math.pow(p2[2]-p1[2],2)

def difference(p1,p2):
    return (p2[0] - p1[0], p2[1] - p1[1],p2[2] - p1[2])

for index in range(len(scannersRelative[0])):
    print(scannersRelative[0][index],scannersRelative[1][index], difference(scannersRelative[0][index],scannersRelative[1][index]))

rotateY(1,1)
print("---")
for index in range(len(scannersRelative[0])):
    print(scannersRelative[0][index],scannersRelative[1][index], difference(scannersRelative[0][index],scannersRelative[1][index]))

rotateY(1,1)
print("---")

for index in range(len(scannersRelative[0])):
    print(scannersRelative[0][index],scannersRelative[1][index], difference(scannersRelative[0][index],scannersRelative[1][index]))

rotateY(1,1)
print("---")
