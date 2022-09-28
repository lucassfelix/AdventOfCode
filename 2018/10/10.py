from ctypes import pointer
import sys
import re
from typing import Dict
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

iter = 0

positions = {}
velocities = {}
i = 0
for line in file.readlines():
    aux = re.findall(r'-?\d+', line)
    pos = (int( aux[0]), int(aux[1]))
    vel = (int( aux[2]), int(aux[3]))
    positions[i] = pos
    velocities[i] = vel
    i += 1

def manhattan(p,q):
    return abs(p[0] - q[0]) + abs(p[1]  - q[1])

def draw():
    offset_x = 99999999999999
    offset_y = 99999999999999
    max_x = 0
    max_y = 0
    for pos in positions.values():
        offset_x = min(offset_x,pos[0])
        offset_y = min(offset_y,pos[1])
        max_x = max(max_x,pos[0])
        max_y = max(max_y,pos[1])


    grid = []
    for i in range(offset_y,max_y+1):
        grid.append([])
        for _ in range(offset_x,max_x+1):
            grid[i-offset_y].append('.')


    for pos in positions.values():
        grid[pos[1] - offset_y][pos[0] - offset_x] = "#"
    
    for line in grid:
        print(''.join(line))
    print()
    
def iterate(n):
    global iter
    iter += n
    for index in positions.keys():
        positions[index] = (positions[index][0] + (velocities[index][0] * n) ,positions[index][1] + (velocities[index][1] * n ))


min_x = 99999999999999
min_y = 99999999999999
max_x = 0
max_y = 0
for pos in positions.values():
    min_x = min(min_x,pos[0])
    min_y = min(min_y,pos[1])
    max_x = max(max_x,pos[0])
    max_y = max(max_y,pos[1])

print((max_x,max_y),(min_x,min_y))

last_distance = manhattan((max_x,max_y),(min_x,min_y))
new_distance = last_distance
while (new_distance <= last_distance):
    iterate(2)
    #print("Last: {} | New: {}".format(last_distance,new_distance))
    min_x = 99999999999999
    min_y = 99999999999999
    max_x = -99999999999999
    max_y = -99999999999999
    for pos in positions.values():
        min_x = min(min_x,pos[0])
        min_y = min(min_y,pos[1])
        max_x = max(max_x,pos[0])
        max_y = max(max_y,pos[1])
    #print((max_x,max_y),(min_x,min_y))
    last_distance = new_distance
    new_distance =  manhattan((max_x,max_y),(min_x,min_y))
#print("Last: {} | New: {}".format(last_distance,new_distance))
iterate(-3)
draw()


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(iter))