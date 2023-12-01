import sys, math, re
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

class monkey:
    segurando = []
    somaOp = False
    multOp = False
    quadOp = False
    constante = 0
    divisivel = 0
    trueMonkey = 0
    falseMonkey = 0
    nInspected = 0

    def doOp(self,item):
        if self.quadOp:
            return item * item
        
        if self.multOp:
            return item * self.constante

        if self.somaOp:
            return item + self.constante

    def inspectItens(self):
        throws = []
        itens = self.itens
        for _ in range(len(itens)):
            self.nInspected += 1
            item = self.itens.pop(0)
            newValue = self.doOp(item)
            #newValue = newValue//3
            newValue = newValue % mmc
            if newValue%self.divisivel == 0:
                throws.append((newValue,self.trueMonkey))
            else:
                throws.append((newValue,self.falseMonkey))

        return throws
            
    def __repr__(self):
        return "MAMACO"
        
    def __str__(self):
        aux = ""
        for a in self.itens:
            aux += str(a)+", "
        return f"Segurando: {aux}\nOperação Soma? {self.somaOp}\n Operação Mult? {self.multOp}\
            \nOperação Quadrado? {self.quadOp}\nConstante: {self.constante}\nDivisível por: {self.divisivel}\n\
            Se verdadeiro, joga para: {self.trueMonkey}\nSenão: {self.falseMonkey}\n"


macacos = [[] for _ in range(8)]

for index in range(0,8):
    
    newMonkey = monkey()

    monkeyId = int(re.search("\d+", file.readline()).group())

    startingItens = list(map(int, re.findall(r'\d+', file.readline())))

    line = file.readline()
    squaredOp = re.search("\d+", line) == None
    if not squaredOp:
        num = int(re.search(r'\d+', line).group())
    else:
        num = 0
    somaOp = re.search("\+", line) != None
    multOp = re.search("\*", line) != None

    test = int(re.search(r'\d+', file.readline()).group())

    trueMonkey = int(re.search(r'\d+', file.readline()).group())

    falseMonkey = int(re.search(r'\d+', file.readline()).group())

    file.readline()

    newMonkey.itens = startingItens
    newMonkey.constante = num
    newMonkey.somaOp = somaOp
    newMonkey.multOp = multOp
    newMonkey.quadOp = squaredOp
    newMonkey.divisivel = test
    newMonkey.trueMonkey = trueMonkey
    newMonkey.falseMonkey = falseMonkey

    macacos[index] = newMonkey

mmc = 1
for m in macacos:
    mmc *= m.divisivel

print(macacos)

for round in range(10000):

    for i in range(len(macacos)):
        items = macacos[i].inspectItens()
        for item in items:
            t,m = item
            macacos[m].itens.append(t)

    #print(round)

    #for m in range(len(macacos)):
    #    print(m,macacos[m].itens,macacos[m].nInspected)
   # print("=========")



#for m in range(len(macacos)):
    #print(m,macacos[m].nInspected)
inspections = []
for m in macacos:
    inspections.append(m.nInspected)        

inspections.sort()

firstStar = inspections[-1] * inspections[-2]



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

