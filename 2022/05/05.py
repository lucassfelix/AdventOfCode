import sys, re

file = open(sys.argv[1])
firstStar = ""
secondStar = ""

parseMode = True

stacks = [[] for x in range(10)]
stacksStarTwo = [[] for x in range(10)]


input = [line for line in file.readlines()]

for line in input:

    if line == "\n":
        #print(stacks)
        parseMode = False
        continue
    
    if parseMode:
        matches = [m.start(0) for m in re.finditer('[A-Z]', line)]
        if not matches:
            continue
        for index in matches:
            stacks[(index-1)//4].append(line[index])
            stacksStarTwo[(index-1)//4].append(line[index])

    else:
        line = line.strip()

        _, qnt, _, indexFrom,_,indexTo = line.split(" ")
        for i in range(int(qnt)):
            stacks[int(indexTo)-1].insert(0,stacks[int(indexFrom)-1].pop(0))
        for i in range(int(qnt)):
            stacksStarTwo[int(indexTo)-1].insert(i,stacksStarTwo[int(indexFrom)-1].pop(0))



        print(stacksStarTwo)
        

#print(stacks)
for stack in stacks:
    if stack:
        firstStar += stack[0]

for stack in stacksStarTwo:
    if stack:
        secondStar += stack[0]



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))