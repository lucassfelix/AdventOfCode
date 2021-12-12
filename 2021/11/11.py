input = [[int(c) for c in line.strip("\n")] for line in open("input.txt")]

for a in input:
    a.append(-1)
    a.insert(0,-1)
input.append([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
input.insert(0,[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

def flash(input,line,column,flashed,firstStar):
    for i in range(-1,2):
        for j in range(-1,2):
            if (line+i,column+j) not in flashed and input[line + i][column+j] != -1 :
                input[line + i][column+j] += 1
                if input[line + i][column+j] > 9:
                    firstStar.append(1)
                    flashed.add((line+i,column+j))
                    flash(input,line+i,column+j,flashed,firstStar)
                    input[line+i][column+j] = 0
            
    
firstStar = []
#for line in input:
#        print(line)
keepScore = []
for step in range(10000000):
    flashes = []
    flashed = set()

    for i in range(1,len(input)-1):
        for j in range(1,len(input[0])-1):
            input[i][j] += 1
            if input[i][j] > 9:
                firstStar.append(1)
                flashes.append((i,j))
                flashed.add((i,j))
                input[i][j] = 0
                
    for line,column in flashes:
        flash(input,line,column,flashed,firstStar)
        
    if(len(flashed) == 100):
        secondStar = step
        break
    if step < 100:
        keepScore = firstStar
    
firstStar = keepScore
#    for line in input:
#        print(line)
#    print("--------")
secondStar += 1


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))
            
    