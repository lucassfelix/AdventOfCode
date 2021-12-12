import copy

timers = [int(n) for n in open("input.txt").readline().split(",")]

newborns = 0
result = len(timers)
ages = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for time in timers:
    ages[time] += 1

for i in range(80):

    aux = ages[0]

    for time in range(8):
        ages[time] = ages[time + 1]

    newborns = aux
    ages[8] = newborns
    ages[6] += newborns
    result += newborns

firstStar = result

newborns = 0
result = len(timers)
ages = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for time in timers:
    ages[time] += 1

for i in range(256):

    aux = ages[0]

    for time in range(8):
        ages[time] = ages[time + 1]

    newborns = aux
    ages[8] = newborns
    ages[6] += newborns
    result += newborns

 



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(result))
