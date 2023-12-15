import sys, itertools
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines()]

for l in input:
    data, aux = l.split(' ')
    number =  [int(x) for x in aux.split(',')]

###PARSE OVER
    spaceNeeded = sum(number) + len(number) -1 

    print(len(data),spaceNeeded,number,"\n")
    
    possibilities = []

    for n in number:

        localPossibility = len(data) - spaceNeeded + 1
        print(n,localPossibility)
        symbols = ['.' for _ in range(localPossibility-1)]
        symbols += ['#'*n]
        for a in itertools.permutations(symbols,localPossibility):
            print('\t',a)
            s = "".join(a)
            for p in possibilities:
                p += s
        
    for p in possibilities:
        print(p)


    exit(0)


    



print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))