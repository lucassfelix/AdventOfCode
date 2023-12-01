import sys
from collections import defaultdict

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]


class node:
    nome = ""
    tamanho = 0
    pai = None
    filhos = {}

    def __init__(self,nome,tamanho,pai):
        self.nome = nome
        self.tamanho = tamanho
        self.filhos = {}
        self.pai = pai

currentDir = ""

root = node("\\",0,None)
currentNode = root

for line in input:

    if line[0] == "$":
        try:
            _,command,dir = line.split(" ")
        except: 
            _,command = line.split(" ")

        if not dir:
            continue

        else:
            if dir == "..":
                currentNode = currentNode.pai
            elif dir == "\\":
                currentNode = root
            else:
                currentDir = dir
                for nodo in currentNode.filhos.keys():
                    if nodo == dir:
                        currentNode = currentNode.filhos[nodo]
                        break

    else:
        type, name = line.split(" ")

        if type == "dir":

            novoNodo = node(name,0,currentNode)
            currentNode.filhos[name] = novoNodo

        else:
            
            currentNode.tamanho += int(type)


secondStarKeep = []

def bfs(node):
    global firstStar

    if len(node.filhos.keys()) == 0:
        if node.tamanho <= 100000:
            firstStar += node.tamanho
        secondStarKeep.append(node.tamanho)
        
        return node.tamanho
    sumOfChild = 0

    for child in node.filhos.values():
        sumOfChild += bfs(child)
    node.tamanho += sumOfChild
    if node.tamanho <= 100000:
            firstStar += node.tamanho
    secondStarKeep.append(node.tamanho)
    return node.tamanho

total = 70000000
used = bfs(root)


needed = 30000000 - (total-used)
secondStarKeep.sort()
for i in secondStarKeep:
    if i > needed:
        secondStar = i
        break



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))