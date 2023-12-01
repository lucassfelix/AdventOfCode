import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]

firstStar = (2*(len(input))) + (2*(len(input[0])-2))

def checkVisible(mat,x,y):
    middle = int(mat[x][y])

    for iTop in range(x-1,-1,-1):
        if int(mat[iTop][y]) >= middle:
            break
    else:
        return True
    
    for iBottom in range(x+1,len(mat)):
        if int(mat[iBottom][y]) >= middle:
            break
    else:
        return True

    for iLeft in range(y-1,-1,-1):
        if int(mat[x][iLeft]) >= middle:
            break
    else:
        return True

    for iRight in range(y+1,len(mat[x])):
        if int(mat[x][iRight]) >= middle:
            break
    else:
        return True

    return False

def getScenicScore(mat,x,y):
    middle = int(mat[x][y])

    scoreTop = 0
    scoreBottom = 0
    scoreLeft = 0
    scoreRight = 0

    for iTop in range(x-1,-1,-1):
        #print(middle,mat[iTop][y])
        scoreTop += 1
        if int(mat[iTop][y]) >= middle:
            break

    for iBottom in range(x+1,len(mat)):
        scoreBottom += 1
        if int(mat[iBottom][y]) >= middle:
            break

    for iLeft in range(y-1,-1,-1):
        scoreLeft += 1
        if int(mat[x][iLeft]) >= middle:
            break

    for iRight in range(y+1,len(mat[x])):
        scoreRight += 1
        if int(mat[x][iRight]) >= middle:
            break

    #print(scoreTop,scoreBottom,scoreRight,scoreLeft)
    return scoreTop * scoreRight * scoreLeft * scoreBottom


print(getScenicScore(input,3,2))


for row in range(1,len(input)-1):
    for col in range(1,len(input[row])-1):
        if checkVisible(input,row,col):
            firstStar += 1
        secondStar = max(secondStar,getScenicScore(input,row,col))


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))