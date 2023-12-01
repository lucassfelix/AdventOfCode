import sys
from typing import List
from tqdm import tqdm

file = open(sys.argv[1])

arq =  file.readline().strip()


class point:
    x = 0
    y = 0

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return __o.x == self.x and __o.y == self.y

    def __add__(self, __o: object):
        return point(self.x + __o.x , self.y + __o.y)

    def __hash__(self) -> int:
        return hash((self.x,self.y))

    def __lt__(self, __o: object) -> bool:
        return self.x < __o.x

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

class shape:
    
    points = []
    origin : point = None

    def __init__(self,points : List[point], height : point):
        self.points = []
        for p in points:
            self.points.append(p + height)

    def move(self,move):
        for p in self.points:
            p.x = p.x + move.x
            p.y = p.y + move.y

    def __str__(self) -> str:
        return str(self.points)

class board:

    mat = []

    origin = point(2,3)

    def __init__(self,size) -> None:
        self.mat = [['.' for _ in range(size)] for _ in range(7)]

    def __str__(self) -> str:
        string = ""
        for i in range(len(self.mat[0])-1,-1,-1):
            string += "|"
            for j in range(len(self.mat)):
                string += self.mat[j][i]
            string += "|\n"
        string += "+-------+"
        return string

    def placeShapeVisualize(self, newShape : shape) -> None:
        for p in newShape.points:
            self.mat[self.origin.x + p.x][self.origin.y + p.y] = "#"

    def placeShape(self, newShape : shape) -> None:
        for p in newShape.points:
            self.mat[self.origin.x + p.x][self.origin.y + p.y] = "#"

    def placePoints(self,points):
        for p in points:
            self.mat[p.x][p.y] = "#"
        



    

lineShape = [point(0,0),point(1,0),point(2,0),point(3,0)]
crossShape = [point(0,1),point(1,1),point(1,2),point(1,0),point(2,1)]
lShape = [point(0,0),point(1,0),point(2,0),point(2,1),point(2,2)]
iShape = [point(0,0),point(0,1),point(0,2),point(0,3)]
squareShape = [point(0,0),point(1,1),point(0,1),point(1,0)]


placedShapes = 0
blockedPoints = set()
height = point(2,3)
placeNewShape = True

shapeIndex = 0
shapes = [lineShape,crossShape,lShape,iShape,squareShape]

fileIndex = 0
jetTurn = True

print(arq)
print(len(arq))


currentShape = None

#currentShape = shape(lineShape,point(0,0))
#print(currentShape)
#currentShape.move(point(1,0))
#print(currentShape)
#exit(0)

nBlocks = 2022

pbar = tqdm(total = nBlocks )
while placedShapes < nBlocks:

    if placeNewShape:
        currentShape = shape(shapes[shapeIndex],height)
        shapeIndex = (shapeIndex + 1) % len(shapes)
        placeNewShape = False
        jetTurn = True


    if jetTurn:
        move = point(1,0) if arq[fileIndex] == ">" else point(-1,0)
        fileIndex = (fileIndex + 1) % len(arq)

        #print(move,currentShape.points)


        for p in currentShape.points:
            np = p + move
            if np in blockedPoints or np.x >= 7 or np.x < 0:
                break
        else:
            currentShape.move(move)
        
    else:
        move = point(0,-1)

        #print(move,currentShape.points)

        blocked = True

        for p in currentShape.points:
            #print(p,move)
            np = p + move
            #print(np,(height.y-4))
            if np in blockedPoints or np.y < 0:
                #print(np,height.y-4)
                break
        else:
            blocked = False
            currentShape.move(move)

        if blocked:


            #print("Set!",currentShape.points)
            blockedPoints.update(currentShape.points)

            for p in currentShape.points:
                newH = p.y + 4
                if newH > height.y:
                    height.y = newH
            placedShapes += 1
            pbar.update(1)


            ###
            ##newPoints = set()
            ##for p in blockedPoints
            ####

            placeNewShape = True
            #print("Height:",height)

    #print("Current",currentShape)


    jetTurn = not jetTurn

#print(blockedPoints)

#print(height.y-3)

#b = board(30)
#b.placePoints(blockedPoints)
#print(b)