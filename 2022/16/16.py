from queue import PriorityQueue
import sys,re,math
import itertools
from tqdm import tqdm

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

class node:

    name : str
    pressure : int
    connections : list
    distanceTo : dict

    def fillDistances(self) -> None:
        
        visited = set()
        next = []

        visited.add(self)
        next.append((self,0))

        while len(next) != 0:

            n,cost = next.pop(0)

            if n not in self.distanceTo.keys() or cost < self.distanceTo[n]:
                self.distanceTo[n] = cost

            for c in n.connections:
                if c not in visited:
                    visited.add(c)
                    next.append((c,cost+1))

    def getNextBest(self,timeLeft,opened) -> tuple:
        
        openValue = (timeLeft-1) * self.pressure if self not in opened else 0

        print(self, openValue)

        maxValue = openValue
        maxNode = self

        for k in self.distanceTo.keys():
            if k not in opened:
                dst = self.distanceTo[k]
                childValue = n.getNextBest(timeLeft-dst,opened)
                if childValue > maxValue:
                    maxValue = childValue
                    maxNode = k

        opened.add(maxNode)

        return (timeLeft,opened)

    def __init__(self, name, pressure, connections) -> None:
        self.name = name
        self.pressure = pressure
        self.connections = connections
        self.distanceTo = {}

    def __hash__(self) -> int:
        return hash((self.name,self.pressure))

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.pressure == __o.pressure

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return f"{self.name}:{self.pressure} -> {self.connections}"

nodes = []
nameToNode = {}

for line in arq:
    pressure = list(map(int, re.findall(r'-?\d+', line)))[0]
    lineNodes = list(re.findall(r'\w*[A-Z]\w*[A-Z]\w*', line))
    newNode = node(lineNodes[0],pressure,lineNodes[1:])
    nodes.append(newNode)
    nameToNode[lineNodes[0]] = newNode

for n in nodes:
    for i in range(len(n.connections)):
        n.connections[i] = nameToNode[n.connections[i]]

for n in nodes:
    n.fillDistances()


##########################

for n in nodes:
    print(n.distanceTo)


current = nodes[0]


nodes = [n for n in nodes if n.pressure > 0]

visited = set()
visited.add(current)

timeLimit = 30






# for min in range(1,timeLimit):

#     maxValue = 0
#     maxValueNode = current

#     for n in nodes:
#         if n == current:
#             continue

#         value = n.pressure - current.distanceTo[n] if n not in off else 0
        
#         if value > maxValue:
#             maxValue = value
#             maxValueNode = n

#     min += current.distanceTo[maxValueNode]

#     firstStar += maxValue * min

#     off.add(maxValueNode)
#     #print(maxValueNode.name,maxValue)
#     current = maxValueNode


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

