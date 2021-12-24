from os import replace
import sys,math
from collections import defaultdict
from multiprocessing import Pool

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [int(line.strip().split(" ")[2]) for indexLine,line in enumerate(file.readlines()) if indexLine % 18 == 5 or indexLine % 18 == 4 or indexLine % 18 == 15]
reversedInput = [line for line in reversed(input)]

#
#22222222222222
blocos = [input[i:i+3] for i in range(0,len(input)-2,3)]

def ULA(entrada, prevZ,index):

    indexEntrada = index
    registradores = {'w':0,'x':0,'y':0,'z':prevZ}
    bloco = blocos[index]

    try:
        registradores['w'] = int(entrada[indexEntrada])
    except IndexError:
        return (registradores['z'],False)
    indexEntrada += 1

    registradores['x'] = registradores['z'] % 26


    registradores['z'] = registradores['z'] // bloco[0]


    aux = registradores['x'] + bloco[1]
    aux = 0 if aux == registradores['w'] else 1



    registradores['x'] = aux
    registradores['z'] =  registradores['z'] * ((25 * aux) + 1)

    registradores['z'] =  registradores['z'] + (registradores['w'] + bloco[2]) * registradores['x']
   
    return (registradores['z'],True)


pilha = []

equations = []

for i,bloco in enumerate(blocos):
    if bloco[0] == 1:
        pilha.append(('w'+str(i) ,bloco[2]))
    else:
        aux = pilha.pop()
        e = ('w'+str(i),aux[0],int(aux[1]) + int(bloco[1]))
        equations.append(e)


entrada = ['#' for i in range(14)]

for e in equations:
    for i in range(9,0,-1):
        first = i + e[2] 
        #print(e,i,first)
        if first > 0 and first < 10:
            second = i
            indexFirst = int(e[0][1:])
            indexSecond = int(e[1][1:])
            entrada[indexFirst] = str(first)
            entrada[indexSecond] = str(second)
            break

firstStar = ''.join(entrada)



entrada = ['#' for i in range(14)]

for e in equations:
    for i in range(1,10,1):
        first = i + e[2] 
        #print(e,i,first)
        if first > 0 and first < 10:
            second = i
            indexFirst = int(e[0][1:])
            indexSecond = int(e[1][1:])
            entrada[indexFirst] = str(first)
            entrada[indexSecond] = str(second)
            break

secondStar = ''.join(entrada)









print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))