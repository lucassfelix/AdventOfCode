import sys
from ast import literal_eval
from itertools import zip_longest
from functools import cmp_to_key

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

def compareTuple(pair):
    l,r = pair

    #print("Comparando {} e {}".format(l,r))

    if l == None:
        return 1
    if r == None:
        return -1

    if type(l) == type(r) and type(l) == type(0):
        if l < r:
            return 1
        if l > r:
            return -1
        if l == r:
            return 0

    if type(l) != type(r):
        if type(l) == type(0):
            l = [l]
        if type(r) == type(0):
            r = [r]

    return compareTuples(l,r)

    
def compareTuples(item1,item2):

    tups = list(zip_longest(item1,item2))


    for t in tups:
        r = compareTuple(t)
        if r == 0:
            continue
        if r == -1:
            #print("Direita Menor")
            return -1
        if r == 1:
            #print("Esquerda Menor")
            return 1
    else:
        return 0


pairs = []
amigos = []
index = 1

for i in range(len(arq)):
    line = arq[i]
    if line == "":
        
        left, right = pairs
        #print(left,right)

        if compareTuples(left,right) ==1:
            #print(index)
            firstStar += index 

        pairs.clear()
        #print()
        index += 1
        continue
        
    eval = literal_eval(line)
    pairs.append(eval)
    amigos.append(eval)

amigos.append([[2]])
amigos.append([[6]])

print(len(amigos),amigos)

amigos = sorted(amigos, key = cmp_to_key(lambda item1, item2: compareTuples(item1,item2)))

amigos.reverse()

print(amigos)

secondStar = (amigos.index([[2]])+1) * (amigos.index([[6]])+1)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

