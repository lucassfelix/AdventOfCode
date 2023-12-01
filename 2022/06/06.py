import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = file.readline()

visited = []


print(input)

for char in input:

    if len(visited) == 14:
        break

    if char in visited:
        aux = ""
        while aux != char:
            aux = visited.pop(0)
    
    visited.append(char)

    firstStar += 1

print(input[firstStar-4:firstStar])


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))