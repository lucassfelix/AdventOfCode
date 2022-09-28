import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line for line in file.readlines()]

for line in input:
    print(line)

hallway = [False for c in range(6)]

letToNum = {'A':1,'B':10,'C':100,'D':1000}

a1 = letToNum[input[2][3]]
a0 = letToNum[input[3][3]]

b1 = letToNum[input[2][5]]
b0 = letToNum[input[3][5]]

c1 = letToNum[input[2][7]]
c0 = letToNum[input[3][7]]

d1 = letToNum[input[2][9]]
d0 = letToNum[input[3][9]]

stackA = [a0,a1]
stackB = [b0,b1]
stackC = [c0,c1]
stackD = [d0,d1]

print(hallway)
print(stackA)
print(stackB)
print(stackC)
print(stackD)


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))