import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

class Part:
    def __init__(self,x,m,a,s) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def value(self) -> int:
        return self.x + self.m + self.a + self.s
    def mult(self) -> int:
        return self.x * self.m * self.a * self.s
    def __str__(self):
        return f"({self.x},{self.m},{self.a},{self.s})"

def is_accepted(procedures,name, part : Part):
    
    for p in procedures[name]:

        if len(p) <= 3:
            if len(p) == 1:
                if p == 'A':
                    return True
                else:
                    return False
            else:
                return is_accepted(procedures,p,part)

        test,toGo = p.split(':')
        id = test[0]
        op = test[1]
        value = int(test[2:])

        match id:
            case 'x':
                toTest = part.x
                pass
            case 'm':
                toTest = part.m
                pass
            case 'a':
                toTest = part.a
                pass
            case 's':
                toTest = part.s
                pass
        
        
        match op:
            case '>':
                result = toTest > value
                pass
            case _:
                result = toTest < value
                pass

        if not result:
            continue
        
        if len(toGo) <= 3:
            if len(toGo) == 1:
                if toGo == 'A':
                    return True
                else:
                    return False
            else:
                return is_accepted(procedures,toGo,part)
            
def get_possibility(procedures,name,index, pMin : Part, pMax :Part, depth):
    
    print("  "*depth,name,index,pMin,pMax)

    if pMin.x > pMax.x or pMin.m > pMax.m or pMin.a > pMax.a or pMin.s > pMax.s:
        return 0

    if len(name) == 1:
        if name == 'A':
            return (pMax.x - pMin.x) *  (pMax.m - pMin.m) *  (pMax.a - pMin.a) *  (pMax.s - pMin.s)
        else:
            return 0
    
    test = procedures[name][index]
    
    print("  "*depth,test,len(test))

    if len(test) <= 3:
        if len(test) == 1:
            if test == 'A':
                return (pMax.x - pMin.x) *  (pMax.m - pMin.m) *  (pMax.a - pMin.a) *  (pMax.s - pMin.s)
            else:
                return 0
        else:
            return get_possibility(procedures,test,0, pMin,pMax,depth+1)
            


    test,toGo = test.split(':')
    id = test[0]
    op = test[1]
    value = int(test[2:])

    newMin = Part(pMin.x,pMin.m,pMin.a,pMin.s)
    newMax = Part(pMax.x,pMax.m,pMax.a,pMax.s)


    match id:
        case 'x':
            if op == '>':
                newMin.x = value+1
            else:
                newMax.x = value-1
            pass
        case 'm':
            if op == '>':
                newMin.m = value+1
            else:
                newMax.m = value-1
            pass
        case 'a':
            if op == '>':
                newMin.a = value+1
            else:
                newMax.a = value-1
            pass
        case 's':
            if op == '>':
                newMin.s = value+1
            else:
                newMax.s = value-1
            pass
    
    return get_possibility(procedures,toGo,0,newMin,newMax,depth+1) + get_possibility(procedures,name,index+1,pMin,pMax,depth+1)

input = [line.strip() for line in file.readlines()]

procedures = {}
xmas = []

for index,l in enumerate(input):
    if l == "":
        break
    name, test = l.split("{")
    procedures[name] = []
    test = test[:-1]
    print(name,test)
    tests = test.split(',')
    for t in tests:
        procedures[name].append(t)
    
for i in range(index+1,len(input)):
    x,m,a,s = [int(k.strip("xmas=")) for k in input[i].strip("{}").split(',')]
    #print(x,m,a,s)
    part = Part(x,m,a,s)
    if is_accepted(procedures,"in",part):
        firstStar += part.value()

print("------------Start--------------")

secondStar = get_possibility(procedures,"in",0,Part(1,1,1,1),Part(4000,4000,4000,4000),0)


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))