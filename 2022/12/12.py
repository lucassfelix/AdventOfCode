import sys, math, re
from collections import defaultdict
from queue import PriorityQueue

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

start = (0,0)

def getLetter(node,mat):

    if int(node[1]) < 0 or int(node[0]) < 0 or int(node[0]) >= len(mat[0]) or int(node[1]) >= len(mat):
        return 'x'
    aux = mat[node[1]][node[0]]
    if aux == "S":
        return 'a'
    if aux == "E":
        return 'z'
    return aux

def getNeighbours(node,mat):

    x = node[0]
    y = node[1]
    
    letraMeio = getLetter(node,mat)
    cima = (x,y-1)
    letraCima = getLetter(cima,mat)
    baixo = (x,y+1)
    letraBaixo = getLetter(baixo,mat)
    direita = (x+1,y)
    letraDireita = getLetter(direita,mat)
    esquerda = (x-1,y)
    letraEsquerda = getLetter(esquerda,mat)


    #print("  {}\n{} {} {}\n  {}".format(letraCima,letraEsquerda,letraMeio,letraDireita,letraBaixo))
    vizinhos = []
    if node[0] < (len(mat[0])-1) and ord(letraDireita) <= ord(letraMeio) + 1:
        vizinhos.append(direita)
    if node[0] > 0  and ord(letraEsquerda) <= ord(letraMeio) + 1:
        vizinhos.append(esquerda)
    if node[1] > 0  and ord(letraCima) <= ord(letraMeio) + 1:
        vizinhos.append(cima)
    if node[1] < (len(mat)-1)  and ord(letraBaixo) <= ord(letraMeio) + 1:
        vizinhos.append(baixo)

    return vizinhos

def heuristica(node,end):
    return sum(abs(e1-e2) for e1, e2 in zip(node,end))

def aStar(start,goal,mat):
    current = start

    notVisited = PriorityQueue()
    notVisited.put((0,start))

    path = {}
    estimativas = {}

    path[start] = 0
    estimativas[start] = 0

    while not notVisited.empty():

        v,current = notVisited.get()
        #print("Nodo:",current,getLetter(current,arq),"Valor:",v)

        if current == goal:
            break

        vizinhos = getNeighbours(current,mat)

        for vizi in vizinhos:
            novoCusto = estimativas[current] + 1 
            if vizi not in estimativas.keys() or novoCusto < estimativas[vizi]:
                estimativas[vizi] = novoCusto        
                notVisited.put((novoCusto,vizi))
                path[vizi] = current
    caminho = []


    while current != start:
        caminho.append(current)
        current = path[current]

    return len(caminho)

starts = []
for i in range(len(arq)):
    line = arq[i]
    nodeStart = line.find("S")
    nodeEnd = line.find("E")
    for j in range(len(line)):
        if line[j] == 'b':
            starts.append((j,i))
    if nodeStart != -1:
        starts.append((nodeStart,i))
        start = (nodeStart,i)
    if nodeEnd != -1:
        end = (nodeEnd,i)


print(starts)


firstStar = aStar(start,end,arq)
secondStar = 100000
for i in range(len(arq)):
    secondStar = min(secondStar, aStar((0,i),end,arq))



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

