import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line for line in file.readlines()]

value = 0
calories = []

for line in input:
    if line == "\n":
        firstStar = max(value,firstStar)
        calories.append(value)
        value = 0
    else:
        value += int(line)

calories.sort(reverse=True)
secondStar = sum(calories[0:3])

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))