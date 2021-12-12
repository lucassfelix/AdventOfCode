import sys

input = [int(line.strip("\n")) for line in open(sys.argv[1]).readlines()]

firstStar = 0
secondStar = 0
for i in range(1,len(input)):
    if input[i] > input[i-1]:
        firstStar += 1

sums = []

for i in range(0,len(input)-2):
    sums.append(input[i] + input[i +1] +input[i+2])

for i in range(1,len(sums)):
    if sums[i] > sums[i-1]:
        secondStar += 1

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))