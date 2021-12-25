from os import times
import sys
from collections import defaultdict
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]

def printGrid(eastCucumbers,southCucumbers):
    grid = [['.' for i in range(len(input[0]))] for j in range(len(input))]
    
    for e in eastCucumbers:
        grid[e[1]][e[0]] = '>'
    for e in southCucumbers:
        grid[e[1]][e[0]] = 'v'
    for line in grid:
        print(''.join(line))

eastCucumbers = set()
southCucumbers = set()

sizeX = len(input[0])
sizeY = len(input)
for rowIndex,line in enumerate(input):
    for columnIndex, char in enumerate(line):
        if char == '>':
            eastCucumbers.add((columnIndex,rowIndex))
        if char == 'v':
            southCucumbers.add((columnIndex,rowIndex))

moved = True
iter = 0
#printGrid(eastCucumbers.values(),southCucumbers.values())
while moved:
    iter += 1
    moved = False
    newEast = set()
    newSouth = set()
    for pos in eastCucumbers:
        newX = (pos[0]+1) % sizeX
        #print(newX)
        if (newX ,pos[1]) not in eastCucumbers and (newX ,pos[1]) not in southCucumbers:
            moved = True
            #print("Moved id:{} to pos:{}".format(id,(newX,pos[1])))
            newEast.add((newX ,pos[1]))
        else:
            newEast.add(pos)

    eastCucumbers = newEast
    
    for pos in southCucumbers:
        newY = (pos[1]+1) % sizeY
        #print(newY)
        if (pos[0],newY) not in eastCucumbers and (pos[0],newY) not in southCucumbers:
            moved = True
            #print("Moved id:{} to pos:{}".format(id,(pos[0],newY)))
            newSouth.add((pos[0],newY))
        else: 
            newSouth.add(pos)
            
    southCucumbers = newSouth
    #print()
    #printGrid(eastCucumbers.values(),southCucumbers.values())
    #if iter == 3:
    #    break

firstStar = iter


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))