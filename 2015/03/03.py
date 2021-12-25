import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()][0]

pos = (0,0)
visited = set()
visited.add(pos)
for c in input:
    if c == '>':
        pos = (pos[0] + 1, pos[1])
    if c == '<':
        pos = (pos[0] - 1, pos[1])
    if c == '^':
        pos = (pos[0], pos[1] + 1)
    if c == 'v':
        pos = (pos[0], pos[1] - 1)
    visited.add(pos)
firstStar = len(visited)


pos = (0,0)
roboPos = (0,0)
visited = set()
visited.add(pos)
robo = False
for c in input:
    if c == '>':
        if not robo:
            pos = (pos[0] + 1, pos[1])
        else:
            roboPos = (roboPos[0] + 1, roboPos[1])
    if c == '<':
        if not robo:
            pos = (pos[0] - 1, pos[1])
        else:
            roboPos = (roboPos[0] - 1, roboPos[1])
    if c == '^':
        if not robo:
            pos = (pos[0], pos[1] + 1)
        else:
            roboPos = (roboPos[0], roboPos[1] + 1)
    if c == 'v':
        if not robo:
            pos = (pos[0], pos[1] - 1)
        else:
            roboPos = (roboPos[0], roboPos[1] - 1)
    if robo:
        visited.add(pos)
    else:
        visited.add(roboPos)
    robo = not robo
secondStar = len(visited)




print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))