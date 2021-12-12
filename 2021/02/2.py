import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n").split(" ") for line in file.readlines()]

directions = {"forward":0, "down":0,"up":0,"depth":0}

for line in input:
    directions[line[0]] += int(line[1])
    if(line[0] == "forward"):
        directions["depth"] += (directions["down"] - directions["up"]) * int(line[1])


firstStar = directions["forward"] * (directions["down"] - directions["up"])
secondStar = directions["forward"] * directions["depth"]

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))