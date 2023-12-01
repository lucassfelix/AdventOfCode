import sys, math
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]


def printMat(mat):
    for line in mat:
        print(''.join(line))

def checkSpritePos(cycle,x):
    ran = [x-1,x,x+1]
    print(cycle,cycle%40,ran)
    if cycle%40 in ran:
        return "#"
    else:
        return "."

tv = [["x"for y in range(40)] for x in range(7)]


x = 1
milestone = 20
filePointer = 0
toAdd = 0
executing = False


for cycle in range(1,1000):

    if filePointer >= len(arq):
        break

    draw = checkSpritePos(cycle-1,x)
    tv[(cycle-1)//40][(cycle-1)%40] = draw
    
    if cycle == milestone:
        firstStar += x * milestone
        milestone += 40
    
    if executing:
        x += toAdd
        executing = False
        filePointer+=1
        continue
    
    line = arq[filePointer].split(" ")
    command = line[0]

    if command == "noop":
        filePointer+=1
        continue
    
    toAdd = int(line[1])
    executing = True

print("Answer first star: {}".format(firstStar))
print("Answer second star:")
printMat(tv)
