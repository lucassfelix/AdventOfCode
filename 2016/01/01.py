from math import radians,sin,cos
from pprint import pprint
import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]


x = 0
y = 0
dir = (0,1)

visited = set()


def rotateL(dir):
    x2 = int(cos(radians(90)))*dir[0] - int(sin(radians(90)))*dir[1]
    y2 = int(sin(radians(90)))*dir[0] + int(cos(radians(90)))*dir[1]
    return (x2,y2)

def rotateR(dir):
    x2 = int(cos(radians(-90)))*dir[0] - int(sin(radians(-90)))*dir[1]
    y2 = int(sin(radians(-90)))*dir[0] + int(cos(radians(-90)))*dir[1]
    return (x2,y2)

foundSecond = False

for command in input:
    if command[0] == 'R':
        dir = rotateR(dir)
    elif command[0] == 'L':
        dir = rotateL(dir)
    steps = int(command[1:])
    x += dir[0] * steps
    y += dir[1] * steps
    print(visited)
    if (x,y) in visited and foundSecond == False:
        secondStar = x+y
        foundSecond = True
    visited.add((x,y))


firstStar = x + y

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))