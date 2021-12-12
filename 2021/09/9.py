input = [[int(char) for char in line.strip("\n")] for line in open("input.txt").readlines()]

def basinFinder(lineIndex, index,input):
    if input[lineIndex][index] == 9 or input[lineIndex][index] == 100:
        return 0;

    input[lineIndex][index] = 9

    return basinFinder(lineIndex,index+1,input) + basinFinder(lineIndex,index-1,input) + basinFinder(lineIndex-1,index,input) + basinFinder(lineIndex+1,index,input) + 1



firstStar = 0
secondStar = 0
a = []
for i in range(1000):
    a.append(100)

input.insert(0,a)
input.append(a)

lowPoints = []

for a in input:
    a.insert(0,100)
    a.append(100)

for lineIndex,line in enumerate(input):
    if lineIndex == 0 or lineIndex == len(input) - 1:
        continue
    
    for index in range(1,len(line)-1):
        if line[index] < line[index-1] and line[index] < line[index+1] and line[index] < input[lineIndex-1][index] and line[index] < input[lineIndex+1][index]:
            firstStar += line[index] + 1
            lowPoints.append((lineIndex,index))

basins = []
for point in lowPoints:
    lineIndex,index = point
    basins.append(basinFinder(lineIndex,index,input))

basins = sorted(basins)

secondStar = basins[-1] * basins[-2] * basins[-3]




print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))