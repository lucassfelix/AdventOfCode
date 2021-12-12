import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]

gamma = ""
epsilon = ""

for i in range(len(input[0])):
    ones = [a for a in input if a[i] == '1']
    zeroes = [a for a in input if a[i] == '0']
    if len(ones) > len(zeroes):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

most = input
less = input
co2 = ""
oxy = ""
for i in range(len(input[0])):

    if(len(most) == 1):
        oxy = most[0]
    if(len(less) == 1):
        co2 = less[0]
    #oxygen
    ones = [a for a in most if a[i] == '1']
    zeroes = [a for a in most if a[i] == '0']
    if len(ones) >= len(zeroes):
        most = ones
    else:
        most = zeroes
    #Co2
    ones = [a for a in less if a[i] == '1']
    zeroes = [a for a in less if a[i] == '0']
    if len(ones) >= len(zeroes):
        less = zeroes
    else:
        less = ones

if(len(most) == 1):
        oxy = most[0]
if(len(less) == 1):
    co2 = less[0]


firstStar = int(gamma,2) * int(epsilon,2)
secondStar = int(co2,2) * int(oxy,2)

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))