input = [int(num) for num in open("input.txt").readline().split(",")]

fuelFirst = {}
fuelSecond = {}

for i in range(max(input)):
    fuelFirst[i] = 0
    fuelSecond[i] = 0
    for num in input:
        dif = abs(num - i)
        fuelFirst[i] += dif
        fuelSecond[i] += ((1 + dif) * dif)//2

firstStar = min(fuelFirst, key=fuelFirst.get)
secondStar = min(fuelSecond, key=fuelSecond.get)

print("Answer first star: {}".format(fuelFirst[firstStar]))
print("Answer second star: {}".format(fuelSecond[secondStar]))
