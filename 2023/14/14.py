import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

def roll_ball_north(field, ball):
    startX,startY = ball
    y = startY
    while True:
        if y == 0:
            break
        if field[y-1][startX] == '#' or field[y-1][startX] == 'O':
            break
        y -= 1
    field[y][startX] = 'O'
    if y != startY:
        field[startY][startX] = '.'
    return(startX,y)

def roll_ball_south(field, ball):
    startX,startY = ball
    y = startY
    while True:
        if y >= len(field)-1:
            break
        if field[y+1][startX] == '#' or field[y+1][startX] == 'O':
            break
        y += 1
    field[y][startX] = 'O'
    if y != startY:
        field[startY][startX] = '.'
    return(startX,y)

def roll_ball_east(field, ball):
    startX,startY = ball
    x = startX
    while True:
        if x >= len(field[startY])-1:
            break
        if field[startY][x+1] == '#' or field[startY][x+1] == 'O':
            break
        x += 1
    field[startY][x] = 'O'
    if x != startX:
        field[startY][startX] = '.'
    return(x,startY)

def roll_ball_west(field, ball):
    startX,startY = ball
    x = startX
    while True:
        if x == 0:
            break
        if field[startY][x-1] == '#' or field[startY][x-1] == 'O':
            break
        x -= 1
    field[startY][x] = 'O'
    if x != startX:
        field[startY][startX] = '.'

    return(x,startY)

input = [[c for c in line.strip()] for line in file.readlines()]

rocks = set()
balls = []

for y in range(0,len(input)):
    for x in range(0,len(input[y])):
        if input[y][x] == '#':
            rocks.add((x,y))
        if input[y][x] == 'O':
            balls.append((x,y))

cycles = [balls.copy()]

for i in range(len(balls)):
        newX,newY = roll_ball_north(input,balls[i])
        balls[i] = (newX,newY)
        firstStar += len(input) - newY  

balls.sort(key = lambda x : x[0])
for i in range(len(balls)):
        newX,newY = roll_ball_west(input,balls[i])
        balls[i] = (newX,newY)

balls.sort(key = lambda x : len(balls) - x[1])
for i in range(len(balls)):
        newX,newY = roll_ball_south(input,balls[i])
        balls[i] = (newX,newY)

balls.sort(key = lambda x : len(balls) - x[0])
for i in range(len(balls)):
        newX,newY = roll_ball_east(input,balls[i])
        balls[i] = (newX,newY)
balls.sort(key = lambda x : x[1])

    

cycles.append(balls.copy())


cycleIndex = 0

for j in range(1,1000000000):

    for i in range(len(balls)):
        newX,newY = roll_ball_north(input,balls[i])
        balls[i] = (newX,newY)

    balls.sort(key = lambda x : x[0])
    for i in range(len(balls)):
        newX,newY = roll_ball_west(input,balls[i])
        balls[i] = (newX,newY)

    balls.sort(key = lambda x : len(balls) - x[1])
    for i in range(len(balls)):
        newX,newY = roll_ball_south(input,balls[i])
        balls[i] = (newX,newY)

    balls.sort(key = lambda x : len(balls) - x[0])
    for i in range(len(balls)):
        newX,newY = roll_ball_east(input,balls[i])
        balls[i] = (newX,newY)
    balls.sort(key = lambda x : x[1])

    if balls in cycles:
        print("found cycle: ", len(cycles))
        cycleIndex = cycles.index(balls)
        for k in range(cycleIndex):
            cycles.pop(0)
        cycleIndex = 0
        break
    else:
        cycles.append(balls.copy())

print(j,cycles.index(balls))


a = j
b = len(cycles)
c = 1000000000 - a
d = c//b
e = 1000000000 % d
print(a,b,c,d,e)

balls = cycles[e - a - 1]
for b in balls:
    secondStar += len(input) - b[1]  

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))