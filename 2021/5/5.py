def exagero(points):
    solution = {}

    for i in range(len(points)):
        for j in range(i,len(points)):
            p1,p2 = points[i]
            x1,y1 = p1
            x2,y2 = p2
            if(x1 != x2 and y1 != y2):
                continue
            p3,p4 = points[j]
            x3,y3 = p3
            x4,y4 = p4
            if(x3 != x4 and y3 != y4):
                continue
            D = (x1 - x2)*(y3-y4) - (y1-y2)*(x3-x4)
            if(D == 0):
                print(p1)
                for x in range(x1,x2+1):
                    for y in range(y1,y2+1):
                        if (x,y) not in solution:
                            solution[(x,y)] = 1
                        else:
                            solution[(x,y)] += 1
            else:
                px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/D
                py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4))/D
                if (px,py) not in solution:
                    solution[(px,py)] = 1
                else:
                    solution[(px,py)] += 1

    result = sum(value >= 2 for value in solution.values())
    return result

def secondStar(points):
    solution = {}

    for line in points:
        p1,p2 = line
        x1,y1 = p1
        x2,y2 = p2
        if x2 != x1 and y2 != y1:
            xinc = 1
            yinc = 1
            if x1 > x2:
                xinc = -1
            if y1 > y2:
                yinc = -1
            for i in range(abs(x2-x1) + 1):
                if (x1,y1) not in solution:
                        solution[(x1,y1)] = 1
                else:
                    solution[(x1,y1)] += 1
                x1 += xinc
                y1 += yinc
            
        else:
            if x2 < x1 or y2 < y1:
                x1,x2 = x2,x1
                y1,y2 = y2,y1
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if (x,y) not in solution:
                        solution[(x,y)] = 1
                    else:
                        solution[(x,y)] += 1
            

            

    result = sum(value >= 2 for value in solution.values())
    return result

def firstStar(points):
    solution = {}

    for line in points:
        p1,p2 = line
        x1,y1 = p1
        x2,y2 = p2
        if x2 < x1 or y2 < y1:
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        if x2 != x1 and y2 != y1:
            continue
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if (x,y) not in solution:
                    solution[(x,y)] = 1
                else:
                    solution[(x,y)] += 1

    result = sum(value >= 2 for value in solution.values())
    return result

input = [line.strip().replace("->",",").split(",") for line in open("input.txt").readlines()]
    
points = [((int(point[0]),int(point[1])),(int(point[2]),int(point[3]))) for point in input]
    

print("Answer first star: {}".format(firstStar(points)))
print("Answer second star: {}".format(secondStar(points)))
