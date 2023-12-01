from queue import PriorityQueue
import sys,re,math
import itertools
from tqdm import tqdm

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

def differenceOne(a,b):
    if abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) == 1:
        return True

surfaceArea = {}
cubes = set()


minx = 20
maxx = 0
miny = 20
maxy = 0
minz = 20
maxz = 0

lowerPoint = 0

for line in arq:
    x,y,z = map(int,line.split(","))

    maxx = max(x,maxx)
    maxy = max(y,maxy)
    maxz = max(z,maxz)

    minx = min(x,minx)
    miny = min(y,miny)

    if z < minz:
        minz = z
        lowerPoint = (x,y,z)


    newCube = (x,y,z)

    surfaceArea[newCube] = 6

    for c in cubes:
        if differenceOne(c,newCube):
            surfaceArea[c] -= 1
            surfaceArea[newCube] -= 1

    cubes.add(newCube)

firstStar = sum(surfaceArea.values())


minimo = (minx-1,miny-1,minz-1)
maximo = (maxx+1,maxy+1,maxz+1)

#print(abs(minimo[0]-maximo[0]) * abs(minimo[1]-maximo[1]) * abs(minimo[2]-maximo[2]))


secondStar = firstStar


count = 0

def getExternal(point,cubes,visited,minimo,maximo):

    global count

    count += 1
    #print(count)

    x,y,z = point


    if point in cubes:
        return 1

    if point in visited:
        return 0
    else:
        visited.add(point)

    if x < minimo[0] or y < minimo[1] or z < minimo[2] :
        #print("\tToo low.")
        return 0

    if x > maximo[0] or y > maximo[1] or z > maximo[2] :
        #print("\tToo high.")
        return 0

    vizi = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

    value = 0

    for np in vizi:
        value += getExternal(np,cubes,visited,minimo,maximo) 
    
    return value

def expand(point,visitedExternal,visitedInternal,visitedTemp,cubes,minimo,maximo):

    #print("Expanding:",point)

    x,y,z = point

    if point in cubes:
        #print("\tIs a cube.")
        return (True, 1)

    if point in visitedExternal:
        #print("\tAlready visited.")
        return (False,0)

    if point in visitedInternal:
        #print("\tAlready visited.")
        return (True,0)

    if point in visitedTemp:
        return (True,0)
    else:
        visitedTemp.add(point)

    if x < minimo[0] or y < minimo[1] or z < minimo[2] :
        #print("\tToo low.")
        return (False, 0)

    if x > maximo[0] or y > maximo[1] or z > maximo[2] :
        #print("\tToo high.")
        return (False, 0)


    vizi = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

    value = 0

    for np in vizi:
        aux, v = expand(np,visitedExternal,visitedInternal,visited,cubes,minimo,maximo)
        if not aux:
            return (False , 0)
        else:
            value += v        

    return (True,value)

def surface(point,cubes,visited):

    if point in visited:
        return 0

    visited.add(point)

    x,y,z = point

    vizi = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

    value = 0

    for v in vizi:
        if v in cubes:
            #print("Surface hit at", v)
            value += 1

    if value == 0:
        #print("No surfaces hit, trying again.")
        for v in vizi:
            if v not in cubes:
                value += surfaceSecondChance(v,cubes,visited)

        return value
    
    for v in vizi:
        if v not in cubes:
            value += surface(v,cubes,visited)

    return value

def surfaceSecondChance(point,cubes,visited):

    if point in visited:
        return 0

    visited.add(point)

    x,y,z = point

    vizi = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

    value = 0

    for v in vizi:
        if v in cubes:
            value += 1

    if value == 0:
        return 0
    
    for v in vizi:
        if v not in cubes:
            value += surface(v,cubes,visited)

    return value


visited = set()

secondStar = 0

#print(lowerPoint)

secondStar = surface(lowerPoint,cubes,visited )



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar-1))

