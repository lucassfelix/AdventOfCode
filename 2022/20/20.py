from queue import PriorityQueue
import sys,re,math
import itertools
from tqdm import tqdm

file = open(sys.argv[1])
firstStar = 0
secondStar = 0


arq = [(int(line.strip()),False)  for line in file.readlines()]

# class node:
#     next = None
#     prev = None
#     value = 0
#     visited = False 

#     def __init__(self,next,prev,value,visited) -> None:
#         self.next = next;
#         self.prev = prev;
#         self.value = value;
#         self.visited = visited;
#         pass

# nodes = []
# for a in range(len(arq)):
#     value = arq[a]
#     next = arq[(a+1)%len(arq)]
#     prev = arq[(a+1)%len(arq)]


#     #nodes.append(node(next,prev,value,visited))



#print(arq)

def getNextFalse(ref,arq):
    for item in range(len(ref)):
        if ref[item][2] == False:
            value = ref[item][0]
            id = ref[item][1]
            ref[item] = (value,id,True)
            return arq.index((value,id,False))
    else:
        return -1

for id in range(len(arq)):
    arq[id] = (arq[id][0]*811589153, id, False)

iter = 0

ref = arq.copy()
#print(arq)
##print(ref)
index = getNextFalse(ref,arq)

#print(arq)
for count in range(10):

    while index != -1:

        value,id,_ = arq.pop(index)
        
        arq.insert(  ((value + index) % len(arq)) , (value,id,True))

        index = getNextFalse(ref,arq)


    for i in range(len(arq)):
        arq[i] = (arq[i][0],arq[i][1],False)
        ref[i] = (ref[i][0],ref[i][1],False)

    index = getNextFalse(ref,arq)
    
    #print(arq)

for i in range(len(arq)):
    value, id, bool = arq[i]
    if value == 0:
        break

zero = i

firstNum = ((1000) % (len(arq)) + zero)%len(arq)
secondNum = ((2000) % (len(arq)) + zero)%len(arq)
thirdNum = ((3000) % (len(arq)) + zero)%len(arq)

print(firstNum,arq[firstNum])
print(secondNum,arq[secondNum])
print(thirdNum,arq[thirdNum])

firstStar = arq[firstNum][0] + arq[secondNum][0] + arq[thirdNum][0]

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

