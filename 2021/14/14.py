import sys,copy,time

start = time.time_ns() / (10 ** 9)

file = open(sys.argv[1])
firstStar = 0
secondStar = 0

def most_frequent(List):
    return max(set(List), key = List.count)

def less_frequent(List):
    return min(set(List), key = List.count)

input = [line.strip("\n") for line in file.readlines()]

polymer = input[0]

pairs = {}
numLetter = {}
numPairs = {}

for i in range(2,len(input)):
    key,value = input[i].split("->")
    pairs[key.strip(" ")] = value.strip(" ")
    a = key.strip(" ")[0]
    b = key.strip(" ")[1]
    numPairs[key.strip(" ")] = 0
    numLetter[a] = 0
    numLetter[b] = 0

for i in range(0,len(polymer)-1):
    key = polymer[i] + polymer[i+1]
    numPairs[key] += 1
    numLetter[polymer[i]] += 1
numLetter[polymer[len(polymer)-1]] += 1


size = 40
for step in range(size):
    nextNumPairs = copy.deepcopy(numPairs)
    for pair in pairs.keys():
        if(numPairs[pair] == 0):
            continue
        newLetter = pairs[pair]
        numLetter[newLetter] += numPairs[pair]
        nextNumPairs[pair[0]+pairs[pair]] += numPairs[pair]
        nextNumPairs[pairs[pair]+pair[1]] += numPairs[pair]
        nextNumPairs[pair] -= numPairs[pair]
    numPairs = nextNumPairs
    if(step == 9):
        maxLetter = max(numLetter,key=numLetter.get)
        minLetter = min(numLetter,key=numLetter.get)
        firstStar = numLetter[maxLetter] - numLetter[minLetter]

maxLetter = max(numLetter,key=numLetter.get)
minLetter = min(numLetter,key=numLetter.get)

secondStar = numLetter[maxLetter] - numLetter[minLetter]

end = time.time_ns() / (10 ** 9)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))