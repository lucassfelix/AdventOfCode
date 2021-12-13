import sys
from functools import reduce
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]

mod = len(input[0])

slopes = [0,0,0,0,0]

row = 0
column = 0
while row < len(input) - 1:
    row = (row + 1)
    column = (column + 1) % mod
    if input[row][column] == '#':
        slopes[0] += 1

row = 0
column = 0
while row < len(input) - 1:
    row = (row + 1)
    column = (column + 3) % mod
    if input[row][column] == '#':
        firstStar += 1
        slopes[1] += 1

row = 0
column = 0
while row < len(input) - 1:
    row = (row + 1)
    column = (column + 5) % mod
    if input[row][column] == '#':
        slopes[2] += 1

row = 0
column = 0
while row < len(input) - 1:
    row = (row + 1)
    column = (column + 7) % mod
    if input[row][column] == '#':
        slopes[3] += 1

row = 0
column = 0
while row < len(input) - 1:
    row = (row + 2)
    column = (column + 1) % mod
    if input[row][column] == '#':
        slopes[4] += 1   
    
secondStar = reduce(lambda x,y:x*y,slopes)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))