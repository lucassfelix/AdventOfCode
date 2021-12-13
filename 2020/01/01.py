def find2020(input):
    for i in input:
        for j in input:
            if i + j == 2020:
                return i * j

def find20203(input):
    for i in input:
        for j in input:
            for k in input:
                if i + j +k == 2020:
                    return i * j *k

import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [int(line.strip("\n")) for line in file.readlines()]

firstStar = find2020(input)
secondStar = find20203(input)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))