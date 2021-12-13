import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]

points = set()
folds = []

for index,line in enumerate(input):
    if line == '':
        break
    x,y = line.split(",")

    points.add((int(x),int(y)))

for i in range(index+1, len(input)):
    axis = input[i].split(" ")[2].split("=")
    folds.append((axis[0],int(axis[1])))

for i, fold in enumerate(folds):
    remove = []
    add = []
    if fold[0] == 'y':
        axis = 1
    else:
        axis = 0
    for point in points:
        if point[axis] > fold[1]:
            remove.append(point)
            newAxis =  point[axis] - (point[axis] - fold[1]) * 2
            if axis == 0:
                add.append((newAxis,point[1]))
            else:
                add.append((point[0],newAxis))
    for point in remove:
        points.remove(point)
    for point in add:
        points.add(point)
    if i == 0:
        firstStar = len(points)

maxX = 0
maxY = 0

for p in points:
    maxX = max(maxX,p[0])
    maxY = max(maxY,p[1])

draw = [['.' for x in range(maxX+1)] for y in range(maxY+1) ]

for p in points:
    draw[p[1]][p[0]] = '#'


print("Answer first star: {}".format(firstStar))
print("Answer second star:")
for line in draw:
    print(line)