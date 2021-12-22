import sys, re
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]


on = set()

cubesOn = set()
cubesOff= set()



def cubeIntersectionVolume(cubeX,cubeA):
    x0,y0,z0 = cubeX[0]
    x1,y1,z1 = cubeX[1]
    a0,b0,c0 = cubeA[0]
    a1,b1,c1 = cubeA[1]

    return max(min(a1,x1)-max(a0,x0),0) * max(min(b1,y1)-max(b0,y0),0) * max(min(c1,z1)-max(c0,z0),0)

def cubeVolume(cube):
    x0,y0,z0 = cube[0]
    x1,y1,z1 = cube[1]
    sizeX = x1-x0
    sizeY = y1-y0
    sizeZ = z1-z0
    return sizeX * sizeY * sizeZ

def cubeIntersection(cubeX,cubeA):
    x0,y0,z0 = cubeX[0]
    x1,y1,z1 = cubeX[1]
    a0,b0,c0 = cubeA[0]
    a1,b1,c1 = cubeA[1]

    if (x1 > a0) and (x0 < a1) and (y1 > b0) and(y0 < b1) and (z1 > c0) and (z0 < c1):
        newX0 = max(a0,x0)
        newX1 = min(a1,x1)
        newY0 = max(b0,y0)
        newY1 = min(b1,y1)
        newZ0 = max(c0,z0)
        newZ1 = min(c1,z1)
        newCube = ((newX0,newY0,newZ0),(newX1,newY1,newZ1))
        return (newCube,True)
    else:
        return ((),False)

def inicialize():
    for line in input:
        state = line.split(" ")[0]
        x0,x1,y0,y1,z0,z1 = map(int,re.findall('[-]?\d+',line))

        if x0 < -50 or x1 > 50 or y0 < -50 or y1 > 50 or z0 < -50 or z1 > 50:
            continue

        if state == "on":
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    for z in range(z0,z1+1):
                        if (x,y,z) not in on:
                            on.add((x,y,z))
        else:
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    for z in range(z0,z1+1):
                        if (x,y,z) in on:
                            on.remove((x,y,z))
            
def pointInCube(point,cube):
    x,y,z = point
    a0,b0,c0 = cube[0]
    a1,b1,c1 = cube[1]

    return x <= a1 and x >= a0 and y >= b0 and y <= b1 and z >= c0 and z <= c1


def reboot():
    points = 0
    onPoints = set()
    offPoints = set()

    
    newPoints = cubeVolume(newCube)
    if state == "on":
        for cube in cubesOn:
            section, intersec = cubeIntersection(cube,newCube)
            if intersec:
                a0,b0,c0 = section[0]
                a1,b1,c1 = section[1]
                for x in range(a0,a1+1):
                    for y in range(b0,b1+1):
                        for z in range(c0,c1+1):
                            if (x,y,z) not in onPoints:
                                newPoints -= 1
                                onPoints.add((x,y,z))
        points += newPoints
    else:
            pass


#C1 = ((X,Y,Z),(dX/2,dY/2,dZ/2))
#C2 = ((X,Y,dZ/2 + 1),(dX/2,dY/2,Z'))
#C3 = ((dX/2 + 1,Y,Z),(X',dY/2,dZ/2))
#C4 = ((dX/2 + 1,Y,dZ/2 + 1),(X',dY/2,Z'))
#C5 = ((X,dY/2 + 1,Z),(dX/2,Y',dZ/2))
#C6 = ((X,dY/2,dZ/2 + 1),(dX/2,Y',Z'))
#C7 = ((dX/2 + 1,dY/2,Z),(X',Y',dZ/2))
#C8 = ((dX/2 + 1,dY/2,dZ/2 + 1),(X',Y',Z'))



def recursiveReboot(cube, listCommands):
    if len(listCommands) == 0:
        print("Cube {} no more commands".format(cube))
        return 0
    if len(listCommands) == 1:
        if listCommands[0][0]:
            print("Cube {} one TRUE command".format(cube))
            return cubeIntersectionVolume(cube,listCommands[0][1])
        else:
            return 0
    if cubeVolume(cube) == 1:
        return 1 if listCommands[-1][0] else 0
    
    x0,y0,z0 = cube[0]
    x1,y1,z1 = cube[1]

    dX = ((x1 - x0) //2) + x0
    dY = ((y1 - y0) //2) + y0
    dZ = ((z1 - z0) //2) + z0

    C1 = ((x0,y0,z0),(dX,dY,dZ))
    C2 = ((x0,y0,dZ + 1),(dX,dY,z1))
    C3 = ((dX + 1,y0,z0),(x1,dY,dZ))
    C4 = ((dX + 1,y0,dZ + 1),(x1,dY,z1))
    C5 = ((x0,dY + 1,z0),(dX,y1,dZ))
    C6 = ((x0,dY,dZ + 1),(dX,y1,z1))
    C7 = ((dX + 1,dY,z0),(x1,y1,dZ))
    C8 = ((dX + 1,dY,dZ + 1),(x1,y1,z1))

    print("\n",cube,"\n")



    commands1 = [c for c in listCommands if cubeIntersection(c[1,C1])[1]]
    commands2 = [c for c in listCommands if cubeIntersection(c[1,C2])[1]]
    commands3 = [c for c in listCommands if cubeIntersection(c[1,C3])[1]]
    commands4 = [c for c in listCommands if cubeIntersection(c[1,C4])[1]]
    commands5 = [c for c in listCommands if cubeIntersection(c[1,C5])[1]]
    commands6 = [c for c in listCommands if cubeIntersection(c[1,C6])[1]]
    commands7 = [c for c in listCommands if cubeIntersection(c[1,C7])[1]]
    commands8 = [c for c in listCommands if cubeIntersection(c[1,C8])[1]]

    print(C1,commands1)
    print(C2,commands2)
    print(C3,commands3)
    print(C4,commands4)
    print(C5,commands5)
    print(C6,commands6)
    print(C7,commands7)
    print(C8,commands8)

    return recursiveReboot(C1,commands1) + recursiveReboot(C2,commands2) + recursiveReboot(C3,commands3) + recursiveReboot(C4,commands4) + recursiveReboot(C5,commands5) + recursiveReboot(C6,commands6) + recursiveReboot(C7,commands7) + recursiveReboot(C8,commands8)


#inicialize()
#firstStar = len(on)
#reboot()

commands = []

minX = +200
minY = +200
minZ = +200
maxX = 0
maxY = 0
maxZ = 0

for line in input:
    state = True if line.split(" ")[0] == "on" else False
    x0,x1,y0,y1,z0,z1 = map(int,re.findall('[-]?\d+',line))

    minX = min(minX,x0)
    minY = min(minY,y0)
    minZ = min(minZ,z0)

    maxX = max(maxX,x1)
    maxY = max(maxY,y1)
    maxZ = max(maxZ,z1)

    newCube = ((x0,y0,z0),(x1,y1,z1))
    command  = (state,newCube)
    commands.append(command)

minX = minX if minX%2 == 0 else minX -1
minY = minY if minY%2 == 0 else minY -1
minZ = minZ if minZ%2 == 0 else minZ -1

maxX = maxX if maxX%2 == 0 else maxX +1
maxY = maxY if maxY%2 == 0 else maxY +1
maxZ = maxZ if maxZ%2 == 0 else maxZ +1

cube0 = ((0,0,0),(2,2,2))
cube1 = ((-1,-1,-1),(-2,-2,-2))
cube2 = ((0,0,0),(100,100,100))

startCube = ((minX,minY,minZ),(maxX,maxY,maxZ))
print(recursiveReboot(startCube, commands))

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))