import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [int(line) for line in file.readlines()]

index = 0


while index >= 0 and index < len(input):
    aux = input[index]
    if input[index] >= 3: 
        input[index] -= 1
    else:
        input[index] += 1

    index += aux
    secondStar += 1


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))