import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [list(map(int,line.strip().split("\t"))) for line in file.readlines()]


for line in input:
    maxi = max(line)
    mini = min(line)
    firstStar += maxi - mini
    for x in line:
        for y in line:
            if x % y == 0 and x != y:
                print(x,y)
                secondStar += x//y




print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))