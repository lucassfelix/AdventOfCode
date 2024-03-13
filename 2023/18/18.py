import sys, os
from colorist import ColorHex
file = open(sys.argv[1])
firstStar = 0
secondStar = 0


os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def span_fill(current, marked:dict):
    if current in marked.keys():
        return
    q = []
    x,y = current
    q.append((x,x,y,1))
    q.append((x,x,y-1,-1))

    while len(q) != 0:
        i = q.pop(0)
        x1,x2,y,dy = i
        x = x1
        if(x,y) not in marked.keys():
            while (x-1,y) not in marked.keys():
                marked[(x-1,y)] = "#ffffff"
                x -= 1
            if x < x1:
                q.append((x,x1-1,y-dy,-dy))
        while x1 <= x2:
            while (x1,y) not in marked.keys():
                marked[(x1,y)] = "#ffffff"
                x1 += 1
            if x1 > x:
                q.append((x,x1-1,y+dy,dy))
            if x1 - 1 > x2:
                q.append((x2 +1,x1-1,y-dy,-dy))
            x1 += 1
            while x1 < x2 and (x1,y) in marked.keys():
                x1 += 1
            x = x1



    pass


def hole_fill(current,marked:dict):
    q = [current]



    while len(q) != 0:
        n = q.pop(0)
        if n not in marked.keys():
            marked[n] = "#ffffff"
            x,y = n
            q.append((x+1,y))
            q.append((x-1,y))
            q.append((x,y+1))
            q.append((x,y-1))
            q.append((x+1,y+1))
            q.append((x+1,y-1))
            q.append((x-1,y+1))
            q.append((x-1,y-1))


input = [line.strip() for line in file.readlines()]


current = (0,0)
markedPoints = {current:"#ffffff"}

hexCurrent = (0,0)
hexPoints = {hexCurrent:"#ffffff"}

for line in input:
    direction, steps, color = line.split(' ')
    color = color.strip("()")
    hexStep = "0x0" + color[1:6]
    match color[6]:
        case '0':
            hexDir = 'R'
            pass
        case '1':
            hexDir = 'D'
            pass
        case '2':
            hexDir = 'L'
            pass
        case _:
            hexDir = 'U'
            pass
    x = current[0]
    y = current[1]
    match direction:
        case 'R':
            for i in range(x+1,x + int(steps) + 1):
                markedPoints[(i,y)] = color
            current = (i,y)
            pass
        case 'L':
            for i in range(x-1,x - int(steps) - 1,-1):
                markedPoints[(i,y)] = color
            current = (i,y)
            pass
        case 'D':
            for i in range(y,y + int(steps) + 1):
                markedPoints[(x,i)] = color
            current = (x,i)
            pass
        case 'U':
            for i in range(y-1,y - int(steps) - 1,-1):
                markedPoints[(x,i)] = color
            current = (x,i)
            pass
    
    x,y = hexCurrent
    match hexDir:
        case 'R':
            for i in range(x+1,x + int(hexStep,0) + 1):
                hexPoints[(i,y)] = color
            hexCurrent = (i,y)
            pass
        case 'L':
            for i in range(x-1,x - int(hexStep,0) - 1,-1):
                hexPoints[(i,y)] = color
            hexCurrent = (i,y)
            pass
        case 'D':
            for i in range(y,y + int(hexStep,0) + 1):
                hexPoints[(x,i)] = color
            hexCurrent = (x,i)
            pass
        case 'U':
            for i in range(y-1,y - int(hexStep,0) - 1,-1):
                hexPoints[(x,i)] = color
            hexCurrent = (x,i)
            pass


maxX = 0
maxY = 0
minX = 0
minY = 0


for p in markedPoints.keys():
    x = p[0]
    y = p[1]
    if(x > maxX):
        maxX = x
    if(y > maxY):
        maxY = y
    if(x < minX):
        minX = x
    if(y < minY):
        minY = y

for i in range(minY,maxY+1):
    str = ""
    for j in range(minX,maxX+1):
        if (j,i) in markedPoints.keys():
            textColor = ColorHex(markedPoints[(j,i)])
            str += f"{textColor}#{textColor.OFF}"
        else:
            str += "."
    print(str)


print("------------------------------------")

span_fill((1,1),markedPoints)
span_fill((1,1),hexPoints)

for i in range(minY,maxY+1):
    str = ""
    for j in range(minX,maxX+1):
        if (j,i) in markedPoints.keys():
            textColor = ColorHex(markedPoints[(j,i)])
            str += f"{textColor}#{textColor.OFF}"
        else:
            str += "."
    print(str)


firstStar = len(markedPoints)
secondStar = len(hexPoints)

area_plus = sum()


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))