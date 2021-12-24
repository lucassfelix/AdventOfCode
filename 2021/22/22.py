import sys, re
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]
steps = []
for line in input:
    state = True if line.split(" ")[0] == "on" else False
    x0,x1,y0,y1,z0,z1 = map(int,re.findall('[-]?\d+',line))
    cuboid = ((x0,y0,z0),(x1,y1,z1))
    steps.append((state,cuboid))

def inicialize():
    on = set()
    for step in steps:
        state = step[0]
        x0,y0,z0 = step[1][0]
        x1,y1,z1 = step[1][1]

        if x0 < -50 or x1 > 50 or y0 < -50 or y1 > 50 or z0 < -50 or z1 > 50:
            continue

        if state:
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
    return len(on)

def countCubes(cuboid):
    x0,y0,z0 = cuboid[0]
    x1,y1,z1 = cuboid[1]
    sizeX = (x1-x0)+1
    sizeY = (y1-y0)+1
    sizeZ = (z1-z0)+1
    return sizeX * sizeY * sizeZ

def cuboidIntersection(cuboidX,cuboidA):
    x0,y0,z0 = cuboidX[0]
    x1,y1,z1 = cuboidX[1]
    a0,b0,c0 = cuboidA[0]
    a1,b1,c1 = cuboidA[1]
    

    if (x1 >= a0) and (x0 <= a1) and (y1 >= b0) and(y0 <= b1) and (z1 >= c0) and (z0 <= c1):
        newX0 = max(a0,x0)
        newX1 = min(a1,x1)
        newY0 = max(b0,y0)
        newY1 = min(b1,y1)
        newZ0 = max(c0,z0)
        newZ1 = min(c1,z1)
        newCube = ((newX0,newY0,newZ0),(newX1,newY1,newZ1))
        return (newCube,True)
    else:
        return((),False)


'''
    change = False

    if x1 >= a0 and x0 <= a1:
        change = True
        newX0 = max(a0,x0)
        newX1 = min(a1,x1)

    if y1 >= a0 and y0 <= b1:
        change = True

        newy0 = max(b0,y0)
        newy1 = min(b1,y1)
    
    if z1 >= c0 and z0 <= c1:
        change = True

        newz0 = max(c0,z0)
        newz1 = min(c1,z1)
    
    if change:
        newCuboid = ((newX0,newy0,newz0),(newX1,newy1,newz1))
        return(newCuboid,True)
    else:
        return((),False)
'''

    

            
def pointInCube(point,cube):
    x,y,z = point
    a0,b0,c0 = cube[0]
    a1,b1,c1 = cube[1]

    return x <= a1 and x >= a0 and y >= b0 and y <= b1 and z >= c0 and z <= c1

def splitCuboid(cuboid, intersection):
    x0,y0,z0 = cuboid[0]
    x1,y1,z1 = cuboid[1]

    a0,b0,c0 = intersection[0]
    a1,b1,c1 = intersection[1]

    newCuboids = []

    if x0 < a0:
        newCuboid = ((x0,y0,z0),(a0-1,y1,z1))
        newCuboids.append(newCuboid)
    if y0 < b0:
        newCuboid = ((a0,y0,z0),(a1,b0-1,z1))
        newCuboids.append(newCuboid)
    if z0 < c0:
        newCuboid = ((a0,b0,z0),(a1,b1,c0-1))
        newCuboids.append(newCuboid)

    if x1 > a1:
        newCuboid = ((a1+1,y0,z0),(x1,y1,z1))
        newCuboids.append(newCuboid)
    if y1 > b1:
        newCuboid = ((a0,b1+1,z0),(a1,y1,z1))
        newCuboids.append(newCuboid)
    if z1 > c1:
        newCuboid = ((a0,b0,c1+1),(a1,b1,z1))
        newCuboids.append(newCuboid)      

    return newCuboids


def reboot():
    on = set()
    for step in steps:
        state = step[0]
        cuboid = step[1]
        
        #print("Turn {} cuboid {} with volume {}".format("ON" if state else "OFF", cuboid,countCubes(cuboid)))

        cuboidsToAdd = []
        cuboidToRemove = []
        for c in on:
            intersec, hasIntersec = cuboidIntersection(c,cuboid)
            if hasIntersec:
                #print("\tDetected intersection {} (volume {}) with cuboid {}".format(intersec,countCubes(intersec),c))
                removeCuboid = True
                cuboidToRemove.append(c)
                #print("\tRemoving cuboid {} with volume {}".format(c, countCubes(c)))
                cuboidsToAdd.extend(splitCuboid(c,intersec))
                #print("\tAdding split cuboids {} with volume {}".format(cuboidsToAdd,sum([countCubes(c) for c in cuboidsToAdd])))
            
        on = on - set(cuboidToRemove)
        on.update(cuboidsToAdd)
    
        if state:
            on.add(cuboid)
        
        #print(on,sum([countCubes(c) for c in on]))

    cubes = [countCubes(c) for c in on]
    return sum(cubes)







firstStar = inicialize()
secondStar = reboot()



cube0 = ((10,10,10),(10,12,12))
cube1 = ((4,4,4),(5,5,5))

#print(countCubes(cube0))



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))