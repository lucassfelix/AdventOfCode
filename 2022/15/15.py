import sys,re,math
from tqdm import tqdm
from ast import literal_eval
from itertools import zip_longest
from functools import cmp_to_key

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

arq = [line.strip() for line in file.readlines()]

sensores = set()
beacons = set()
maxDist = 0
nearest = {}

def manhattan(node,end):
    return sum(abs(e1-e2) for e1, e2 in zip(node,end))

def blocked_line(sensor,y):
    toGo = nearest[s] - abs(y - sensor[1])
    x = sensor[0]
    if toGo > 0:
        bigX = x + toGo
        smallX = x - toGo

        if bigX < 0 or smallX > 4000000:
            return None

        return [max(smallX,0), min(bigX,4000000)]


minX = math.inf
maxX = 0
minY = math.inf
maxY = 0

for line in arq:

    sx,sy,bx,by = tuple(map(int, re.findall(r'-?\d+', line)))
    s = (sx,sy)
    b = (bx,by)
    sensores.add(s)
    beacons.add(b)
    maxDist = max(maxDist,manhattan(s,b))
    nearest[s] = manhattan(s,b)
    maxX = max(sx,maxX,bx)
    minX = min(sx,minX,bx)
    maxY = max(sy,maxY,by)
    minY = min(sy,minY,by)

y = 2000000

def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

def count_merged(merged):
    soma = 0
    for m in merged:

        soma += m[1] - m[0]
    return soma

#print(minX,minY,maxX,maxY)
#print(minX-minX,minY-minY,maxX-minX,maxY-minY)
#print(minX-maxDist,minY-maxDist,maxX-maxDist,maxY-maxDist)


for y in tqdm(range(0,4000000)):
    intervals = []
    for s in sensores:
        aux = blocked_line(s,y)
        if aux != None:
            #print(f"aux == {aux}")
            intervals.append(aux)

    merged = merge(intervals)
    if len(merged) != 1:
        break

print(merged,y)

secondStar = ((merged[0][1] + 1) * 4000000) + y


# for x in tqdm(range(minX-maxDist,maxX+maxDist+1)):

#     for s in sensores:
#         #print(s,nearest[s],(x,y))
#         #print(manhattan(s,nearest[s]),manhattan(s,(x,y)))
#         if  manhattan(s,(x,y)) <= nearest[s] and (x,y) not in beacons and (x,y) not in sensores:
#             #print(x)
#             firstStar += 1
#             break







print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

