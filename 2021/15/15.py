import sys
import copy
from typing import DefaultDict
from queue import PriorityQueue
from dijkstar import Graph, find_path

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [[int(num) for num in line.strip("\n")] for line in file.readlines()]


sizefirstStar = len(input)

##Create 4 columns
old = input
for i in range(4):
    a = [[(num+1) if num != 9 else 1 for num in line] for line in old]
    for index,line in enumerate(a):
        input[index].extend(line)
    old = a

##Replicate the columns 4 times
old = input
for i in range(4):
    a = [[(num+1) if num != 9 else 1 for num in line] for line in old]
    input.extend(a)
    old = a


firstStarGraph = Graph()
secondStarGraph = Graph()

size = len(input)

i = 0
for row in range(sizefirstStar):
    for column in range(sizefirstStar):
        left = True
        right = True
        up = True
        down = True

        #print(row,column,i)
        if row == 0:
            up = False
        if row == sizefirstStar-1:
            down = False
        if column == 0:
            left = False
        if column == sizefirstStar-1:
            right = False

        if up:
            firstStarGraph.add_edge(i, i - sizefirstStar, input[row-1][column])
        if down:
            firstStarGraph.add_edge(i, i + sizefirstStar, input[row+1][column])
        if left:
            firstStarGraph.add_edge(i, i - 1, input[row][column-1])
        if right:
            firstStarGraph.add_edge(i, i + 1, input[row][column+1])

        i+=1
firstStar = find_path(firstStarGraph,0,sizefirstStar*sizefirstStar -1).total_cost


i = 0
for row in range(size):
    for column in range(size):
        left = True
        right = True
        up = True
        down = True

        #print(row,column,i)
        if row == 0:
            up = False
        if row == size-1:
            down = False
        if column == 0:
            left = False
        if column == size-1:
            right = False

        if up:
            secondStarGraph.add_edge(i, i - size, input[row-1][column])
        if down:
            secondStarGraph.add_edge(i, i + size, input[row+1][column])
        if left:
            secondStarGraph.add_edge(i, i - 1, input[row][column-1])
        if right:
            secondStarGraph.add_edge(i, i + 1, input[row][column+1])
        i+= 1

secondStar = find_path(secondStarGraph,0,size*size -1).total_cost

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar)) 