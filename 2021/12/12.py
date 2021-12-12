import copy

def countPaths(origin, directions, lowercases,paths):
    for node in origin:
        if node.islower() and node in lowercases and node != "end":
            aux = copy.deepcopy(lowercases)
            aux.remove(node)
            countPaths(directions[node],directions, aux, paths)
        if node.isupper():
            countPaths(directions[node],directions, copy.deepcopy(lowercases),paths)
    if "end" in origin:
        paths.append(1)
        return

def countPathsSecondStar(nextNode, directions, lowercases,paths,localPath,smallDouble):

    if nextNode == 'end':
        paths.append(localPath)
        return    
    

    origin = directions[nextNode]
    for node in origin:
        newPath = copy.deepcopy(localPath)
        newPath.append(node)
        if node == "end":
            countPathsSecondStar(node,directions, copy.deepcopy(lowercases), paths,newPath,smallDouble)

        if node.islower() and node in lowercases:
            if node == smallDouble:
                countPathsSecondStar(node,directions, copy.deepcopy(lowercases), paths,newPath,"done")
            else:
                aux = copy.deepcopy(lowercases)
                aux.remove(node)
                countPathsSecondStar(node,directions, aux, paths,newPath,smallDouble)

        if node.isupper():
            countPathsSecondStar(node,directions, copy.deepcopy(lowercases),paths,newPath,smallDouble)
    
        
        





input = [line.strip("\n") for line in open("input.txt").readlines()]

directions = {}
lowercases = set()

for line in input:
    o,d = line.split("-")


    if o.islower():
        lowercases.add(o)
    if d.islower():
        lowercases.add(d)

    if o in directions.keys():
        directions[o].append(d)
    else:
        directions[o] = [d]

    
    if d in directions.keys():
        directions[d].append(o)
    else:
        directions[d] = [o]

lowercases.remove("start")
lowercases.remove("end")

paths = []
countPaths(directions["start"], directions, copy.deepcopy(lowercases), paths)
firstStar = len(paths)

paths2 = []
localPaths = ["start"]
for small in lowercases:
    countPathsSecondStar("start", directions, copy.deepcopy(lowercases), paths2,localPaths,small)


secondStar = len(set(map(tuple,paths2)))



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))