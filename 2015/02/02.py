import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]


for line in input:
    x,y,z = map(int,line.split("x"))

    ribbon = x*2 + y*2 + z*2 - max(max(x,y),z) * 2
    bow = x*y*z

    side0 = x * y
    side1 = y * z
    side2 = x * z
    firstStar += side0*2 + side1*2 + side2*2 + min(min(side2,side0),side1)
    secondStar += ribbon + bow


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))