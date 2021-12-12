import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line for line in file.readlines()]


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))