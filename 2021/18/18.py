import sys,copy
from math import floor,ceil
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]

parsedInput = []
parsedInputStar2 = []
def sumPair(a,b):
    return [a,b]
    
def findExplode(a,path):
    if type(a) == int:
        return False
    if len(path) >= 4 and isinstance(a[0],int) and isinstance(a[1],int):
        return True
    path.append(0)
    if findExplode(a[0],path):
        return True
    path.pop()
    path.append(1)
    if findExplode(a[1],path):
        return True
    path.pop()
    return False

def findSplit(a,path):
    if isinstance(a, int):
        if a >= 10:
            return True
        else:
            return False
    path.append(0)
    if findSplit(a[0],path):
        return True
    path.pop()
    path.append(1)
    if findSplit(a[1],path):
        return True
    path.pop()
    return False
    
def checkExplode(t):
    try:
        return 1+max(map(checkExplode,t))
    except:
        return 0
        
def checkSplit(tup):
    for v in tup:
        if isinstance(v, int) and v >= 10:
            return True
        if isinstance(v, list) and checkSplit(v):
            return True
    return False  

def moreToRight(a,b,index):
  newSTR = "".join(map(str,a)).ljust(max(len(a),len(b)),'0')
  pathSTR = "".join(map(str,b)).ljust(max(len(a),len(b)),'0')
  newpath = int(newSTR,2)
  path = int(pathSTR,2)
  #print(a,">",b)
  #print(newSTR,">",pathSTR)
  #print(newpath,">",path)
  return newpath > path

def moreToLeft(a,b,index):  
  newSTR = "".join(map(str,a)).ljust(max(len(a),len(b)),'0')
  pathSTR = "".join(map(str,b)).ljust(max(len(a),len(b)),'0')
  newpath = int(newSTR,2)
  path = int(pathSTR,2)
  #print(a,"<",b)
  #print(newSTR,"<",pathSTR)
  #print(newpath,"<",path)
  return newpath < path


def noOverlap(a,b):
  for i in range(min(len(a),len(b))):
    if a[i] != b[i]:
      #print("Not Equal",True)
      return True
  #print("Not Equal",False)
  return False
  
def addLeft(a,value,path,newpath):
    #print(a,newpath)
    if isinstance(a[1],int):
      newpath.append(1)
      if moreToLeft(newpath,path,0) and noOverlap(newpath,path):
        #print("Added to ",a,"[1]")

        a[1] += value
        return True
      newpath.pop()
    else:
      newpath.append(1)
      if addLeft(a[1],value,path,newpath):
        return True    
      newpath.pop()
        
    if isinstance(a[0],int):
      newpath.append(0)
      if moreToLeft(newpath,path,0) and noOverlap(newpath,path):
        #print("Added to ",a,"[0]")
        a[0] += value
        return True
      newpath.pop()
    else:
      newpath.append(0)
      if addLeft(a[0],value,path,newpath):
        return True
      newpath.pop()
    return False
    
    
    
def addRight(a,value,path,newpath):

    #print(a,newpath)
    if isinstance(a[0],int):
      newpath.append(0)
      if moreToRight(newpath,path,0) and noOverlap(newpath,path):
        #print("Added to ",a,"[0]")
        a[0] += value
        return True
      newpath.pop()
    else:
      newpath.append(0)
      if addRight(a[0],value,path,newpath):
        return True
      newpath.pop()
    
    if isinstance(a[1],int):
      newpath.append(1)
      if moreToRight(newpath,path,0) and noOverlap(newpath,path):
        #print("Added to ",a,"[1]")
        a[1] += value
        return True
      newpath.pop()
    else:
      newpath.append(1)
      if addRight(a[1],value,path,newpath):
        return True    
      newpath.pop()
    return False   

def printTree(a,level):
  if not isinstance(a,int):
    print(level,'\t' * level , a)
    printTree(a[0],level+1)
    printTree(a[1],level+1)

def split(a,path):
  aux = a
  for index in range(len(path)-1):
      aux = aux[path[index]]
  
  value = aux[path[-1]]
  
  aux[path[-1]] = [floor(value/2),ceil(value/2)]


def explode(a,path):
    aux = a
    for index in range(len(path)-1):
        aux = aux[path[index]]
    
    left = aux[path[-1]][0]
    right = aux[path[-1]][1]
    '''
    if isinstance(left,list):
      print(left)
      aux = aux[path[-1]]
      path.append(0)
      right = left[1]
      left = left[0]
    if isinstance(right,list):
      print(right)
      aux = aux[path[-1]]
      path.append(1)
      left = right[0]
      right = right[1]
    '''
    #print("EXPLODING: [{},{}]".format(left,right))
    addRight(a,right,path,[])
    addLeft(a,left,path,[])
    aux[path[-1]] = 0    
    
def reducePair(a):
    #printTree(a,1)
    doExplode = False
    doSplit = False
    pathExplode = []
    pathSplit = []
    if checkExplode(a) >= 5:
        findExplode(a,pathExplode)
        aux = a
        for index in range(len(pathExplode)):
            aux = aux[pathExplode[index]]
        #print("Found explode at ",pathExplode,aux)
        doExplode = True

    if checkSplit(a):
        findSplit(a,pathSplit)
        aux = a
        for index in range(len(pathSplit)):
            aux = aux[pathSplit[index]]
        #print("Found split at ",pathSplit,aux)
        doSplit = True

    if not doSplit and not doExplode:
        return a

    if doExplode:
      #print("EXPLODE",pathExplode)
      explode(a,pathExplode)
      return reducePair(a)
    if doSplit:
      #print("SPLIT",pathSplit)
      split(a,pathSplit)
      return reducePair(a)

    '''
    if doSplit and doExplode:
      if (moreToLeft(pathExplode,pathSplit,0) and noOverlap(pathExplode,pathSplit)):
        print("EXPLODE1",pathExplode)
        explode(a,pathExplode)
      else:
        if not noOverlap(pathExplode,pathSplit) and len(pathExplode) < len(pathSplit):
          print("EXPLODE5",pathExplode)
          explode(a,pathExplode)
        else:
          print("SPLIT2",pathSplit)
          split(a,pathSplit)
    elif doSplit:
      print("SPLIT3",pathSplit)
      split(a,pathSplit)
    else:
      print("EXPLODE4",pathExplode)
      explode(a,pathExplode)
    print("\nRESULT:",a,"\n")
    '''

def magnitude(a):
  if isinstance(a,int):
    return a
  return 3*magnitude(a[0]) + 2* magnitude(a[1])


for line in input:
    parseQueue = []
    for char in line:
        parseQueue.append(char)
        if parseQueue[-1] == ']':
            parseQueue.pop()
            y = parseQueue.pop()
            if type(y) == str:
                y = int(y)
            parseQueue.pop()
            x = parseQueue.pop()
            if type(x) == str:
                x = int(x)
            parseQueue.pop()
            parseQueue.append([x,y])
    parsedInputStar2.append(copy.deepcopy(parseQueue[0]))        
    parsedInput.append(parseQueue[0])


#print(parseQueue)
for line in parsedInput:
  print(line)

sum = reducePair(sumPair(parsedInput[0],parsedInput[1]))

for indexNum in range(2,len(parsedInput)):
    sum = reducePair(sumPair(sum,parsedInput[indexNum]))
    #print(indexNum,sum)

firstStar = magnitude(sum)
print("--------")
for line in parsedInputStar2:
  print(line)


maxSum = 0
for i in range(len(parsedInputStar2)):
  for j in range(i,len(parsedInputStar2)):
    aux = copy.deepcopy(parsedInputStar2)
    maxSum = max(maxSum,magnitude(reducePair(sumPair(aux[i],aux[j]))))
    aux = copy.deepcopy(parsedInputStar2)
    maxSum = max(maxSum,magnitude(reducePair(sumPair(aux[j],aux[i]))))

print("--------")
for line in aux:
  print(line)


secondStar = maxSum

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))