import sys
from math import ceil, sqrt
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

strRangeX,strRangeY = file.readline().strip().split(":")[1].split(",")


targetRangeX = (int(strRangeX.split("=")[1].split("..")[0]) , int(strRangeX.split("=")[1].split("..")[1]))
targetRangeY = (int(strRangeY.split("=")[1].split("..")[0]) , int(strRangeY.split("=")[1].split("..")[1]))

#print("Target area: {},{} \n".format(targetRangeX,targetRangeY))

position = (0,0)

corrects = []
failed = set()
succeded = set()

delt = sqrt(abs(1-(8*int(targetRangeX[0])))) 
minx = ceil((-1 + delt)/2)
maxy = abs(targetRangeY[0]) -1

firstStar = sum([i for i in range(1,maxy+1)])

def simulateFall(position,xVel,yVel,velocities):
    #print(position)
    newX = position[0] + xVel
    newY = position[1] + yVel
    velocities.append((position,newX,newY))
    newPosition = (newX, newY)
    if newX > targetRangeX[1] or newY < targetRangeY[0] or (position,newX,newY) in failed:
        #print("\nOvershot!")
        for elem in velocities:
            failed.add(elem)
        return False
    if (newX >= targetRangeX[0] and newX <= targetRangeX[1] and newY >= targetRangeY[0] and newY <= targetRangeY[1]) or (position,newX,newY) in succeded:
        #print("\nIn target position!")
        for elem in velocities:
            succeded.add(elem)
        return True
    yVel -= 1
    if xVel != 0:
        xVel = xVel + 1 if xVel < 0 else xVel - 1
    return simulateFall(newPosition,xVel,yVel,velocities)



for i in range(targetRangeX[1]+1):
    for j in range(targetRangeY[0],maxy+1):
        if simulateFall(position,i,j,[]):
            corrects.append((i,j))

#print("Min X = {}".format(minx))
#print("Max Y = {}".format(maxy))
secondStar = len(corrects)
print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))