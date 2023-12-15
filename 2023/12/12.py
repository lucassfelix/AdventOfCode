import sys, itertools
from functools import cache
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

memoi = {}

@cache
def evaluate(data, currentNumbers:tuple,nivel):

    if(len(data) < sum(currentNumbers) + len(currentNumbers)-1):
        return 0

    #print("  "*nivel, data if len(data) > 0 else "VAZIO", currentNumbers )
    if len(data) == 0 and len(currentNumbers) > 0:
        #print("  "*nivel,"ZERO")

        return 0

    if len(data) ==0 and len(currentNumbers) == 0:
        #print("  "*nivel,"UM")

        return 1
    
    if len(currentNumbers) > 0 and currentNumbers[-1] > len(data):
        return 0
    

    current = data[-1]
    
    result = 0
    
    match current:
        case '.':
            newData = data[:-1]
            result += evaluate(newData, currentNumbers,nivel+1)
            pass



        case '#':
            if(len(currentNumbers) == 0):
                #print("  "*nivel,"ERRADO: Não tem NUM")
                return 0
            if(len(data) < currentNumbers[-1]-1):
                #print("  "*nivel,"ERRADO: Não tem espaço")
                return 0
            if '.' in data[-currentNumbers[-1]:]:
                return 0
            newData = data[:-currentNumbers[-1]]
            if(len(newData) > 0 and newData[-1] == '#'):
                #print("  "*nivel,"ERRADO: DELETA #")
                return 0
            newData = newData[:-1]
            
            #print("  "*nivel,"BOTA:",n)

            result += evaluate(newData,currentNumbers[:-1],nivel+1)
            pass





        case '?':
            newData = data[:-1] + '.'
            result += evaluate(newData, currentNumbers,nivel)
            newData = data[:-1] + '#'
            result += evaluate(newData, currentNumbers,nivel)
            pass
        case _:
            pass
            ##print("Deu ruim!")

    return result
        


input = [line.strip() for line in file.readlines()]
i = 0
for l in input:
    data, aux = l.split(' ')
    number =  [int(x) for x in aux.split(',')]

    dataTwo = "".join([data + '?' for _ in range(5)])[:-1]
    numberTwo = number * 5

###PARSE OVER
    
    print(i,l)
    i += 1
    s =  evaluate(data,tuple(number),0)
    #print(s)
    firstStar += s

    w = evaluate(dataTwo,tuple(numberTwo),0)
    secondStar += w

    



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))