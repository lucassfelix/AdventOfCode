import sys,copy
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]

code = input[0]
#print(code)

points = set()

def countSurroundingPixels(pixel,rangeX,rangeY,iter):
    bin = ""
    mat = ""
    aa = []
    for i in range(-1,2):
        for j in range(-1,2):
            newpoint = (pixel[0] + j, pixel[1] + i)
            aa.append(newpoint)
            if newpoint in points:
                mat += "#"
                bin += "1"
            elif newpoint[0] < rangeX[0] or newpoint[0] > rangeX[1] or newpoint[1] < rangeY[0] or newpoint[1] > rangeY[1]:
                bin += "1" if iter%2 == 1 else "0"
                mat += "@" if iter%2 == 1 else "%"
            else:
                bin += "0"
                mat += "."
                #print(pixel[0] + j, pixel[1] + i)
        if i != 1:
            mat += "\n"
    #print(aa)
    #print(mat)
    #print(bin,int(bin,2))
    return int(bin,2)

def printMatrix(matrix):
    for line in matrix:
        print(''.join(line))

def createMatrix(points):

    minX = min(points, key = lambda t: t[0])[0]
    minY = min(points, key = lambda t: t[1])[1]

    maxX = max(points, key = lambda t: t[0])[0] + abs(minX)
    maxY = max(points, key = lambda t: t[1])[1] + abs(minY)

    #print(points)
    #print(minX,maxX,minY,maxY)
    #newPoints = set()
    drawing = [['.' for column in range(maxY+1) ] for row in range(maxX+1)]
    for point in points:
        #newPoint = (point[0]+abs(minX),point[1]+abs(minY))
        drawing[point[1]+abs(minY)][point[0]+abs(minX)] = '#'
        #newPoints.add(newPoint)
    #points = newPoints
    return drawing


for row in range(2,len(input)):
    for column in range(len(input[row])):
        if input[row][column] == '#':
            points.add((column,row-2))

#print("At start:", len(points))

#printMatrix(createMatrix(points))
for iter in range(50):
    newPoints = set()
    visitedPoints = set()
    minX = min(points, key = lambda t: t[0])[0]
    minY = min(points, key = lambda t: t[1])[1]
    maxX = max(points, key = lambda t: t[0])[0]
    maxY = max(points, key = lambda t: t[1])[1]
    #print("X:{} Y:{}".format((minX,maxX),(minY,maxY)))
    #print(sorted(points))

    for row in range(minX-1,maxX+2):
        for column in range(minY-1,maxY+2):
            #print(visitedPoints)
            #print("Point:",(column,row))
            for i in range(-1,2):
                for j in range(-1,2):
                    newPoint = (column + j, row + i)
                    if newPoint not in visitedPoints:
                        #print(newPoint)
                        charIndex = countSurroundingPixels(newPoint,(minX,maxX),(minY,maxY),iter)
                        #print(code[charIndex])
                        if (code[charIndex] == '#'):
                            #print("Add point")
                            newPoints.add(newPoint)
                        visitedPoints.add(newPoint)
    points = copy.deepcopy(newPoints)
    if iter == 1:
        firstStar = len(points)

    #print("Iter:",iter+1, "Len:",len(points))
    
printMatrix(createMatrix(points))



secondStar = len(points)




print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))