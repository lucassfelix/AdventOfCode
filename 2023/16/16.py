import sys
first = 0

input = [line.strip() for line in open(sys.argv[1])]

#for l in input:
#    print(l)

start = (-1,0,(1,0))

def find_energy(start):

    lasers = []

    visited = set()

    lasers.append(start)

    while len(lasers) != 0:
        toRemove = []
        toAdd = []
        #print("--------------------------------")
        for index,l in enumerate(lasers):
            x,y,step = l
            stepX,stepY = step
            #print("Laser",index,"\n",x,y,"going to", x+stepX,y+stepY)
            x += stepX
            y += stepY
            if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input):
                #print("deleted laser",index)
                toRemove.append(index)
                continue
            piece = input[y][x]
            #print("found: ",piece)
            match piece:
                case '-':
                    if step[1] != 0:
                        if (x,y) in visited:
                            toRemove.append(index)
                            continue
                        lasers[index] = (x,y,(-1,0))
                        toAdd.append((x,y,(1,0)))
                    else:
                        lasers[index] = (x,y,step)
                case '|':
                    if step[0] != 0:
                        if (x,y) in visited:
                            toRemove.append(index)
                            continue
                        lasers[index] = (x,y,(0,-1))
                        toAdd.append((x,y,(0,1)))
                    else:
                        lasers[index] = (x,y,step)
                    pass
                case '/':
                    lasers[index] = (x,y,(-step[1],-step[0]))
                    pass
                case '\\':
                    lasers[index] = (x,y, (step[1],step[0]))
                    pass
                case _:
                    lasers[index] = (x,y,step)
            visited.add((x,y))
            
        offset = 0
        for i in toRemove:
            lasers.pop(i + offset)
            offset -= 1

        for a in toAdd:
            lasers.append(a)

    for i in range(len(input)):
        str = ""
        for y in range(len(input[0])):
            str += '#' if (y,i) in visited else '.'
        #print(str)
            
    return len(visited)

print("First star",find_energy(start))


secondStar = 0

borderRight = len(input[0])
borderDown = len(input)

for i in range(len(input)):
    #print((-1,i,(1,0)))
    secondStar = max(find_energy((-1,i,(1,0))),secondStar)

for i in range(len(input)):
    #print((borderRight,i,(-1,0)))
    secondStar = max(find_energy((borderRight,i,(-1,0))),secondStar)

for i in range(len(input[0])):
    #print((i,-1,(0,1)))
    secondStar = max(find_energy((i,-1,(0,1))),secondStar)

for i in range(len(input)):
    #print((i,borderDown,(0,-1)))
    secondStar = max(find_energy((i,borderDown,(0,-1))),secondStar)

print("Second star:",secondStar)