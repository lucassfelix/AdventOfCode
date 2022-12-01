import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = file.readline()

start,end  = input.split("-")

start = int(start)
end = int(end)

    

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))