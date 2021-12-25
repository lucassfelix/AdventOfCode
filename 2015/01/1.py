import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()][0]
print
firstStar = input.count('(') - input.count(')')

floor = 0
for index,i in enumerate(input):
    if i == '(':
        floor += 1
    if i == ')':
        floor -= 1
    if floor == -1:
        secondStar = index + 1
        break

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))