import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

def print_cases(v:list):
    for c in v:
        for l in c:
            print(l)
        print()

def get_diff(line1, line2):
    d = 0
    for a, b in zip(line1, line2):
        if a != b: d += 1
        if d > 1: break
    #print(line1,line2,d)
    return d

def find_reflection(p, partTwo = False):
    for index in range(len(p)):
        reflecting = True
        diff = 0
        for offset in range(len(p) - index):
            before = index-offset
            after = index+1+offset
            if(before < 0 or after >= len(p)):
                break
            #print(index,before,after)
            if partTwo:
                diff += get_diff(p[before],p[after])
                if diff > 1:
                    reflecting = False
                    break
            elif(p[before] != p[after]):
                reflecting = False
                break
        if reflecting and index != len(p) -1:
            if partTwo:
                if diff == 0:
                    continue
                else:
                    return index
            return index
    return -2
            

input = [line.strip() for line in file.readlines()]

patterns = [[]]

for line in input:
    if line == '':
        patterns.append([])
        continue
    patterns[-1].append(line)

#print_cases(patterns)

columns = []



for index, p in enumerate(patterns):
    columns= ["".join([p[f][i] for f in range(len(p))]) for i in range(len(p[0]))]

    print("----------------------",index)

    h_reflection = find_reflection(p) + 1
    v_reflection = find_reflection(columns) + 1
    h_two = find_reflection(p,True) + 1
    v_two = find_reflection(columns, True) + 1

    print("Horizontal:",h_reflection)
    print("Vertical:",v_reflection)
    print("Horizontal 2:",h_two)
    print("Vertical 2:",v_two)
    
    if h_reflection == -1:
        firstStar += v_reflection
    else:
        firstStar += 100*(h_reflection)

    if h_two == -1:
        secondStar += v_two
        print("Chose Vertical 2:",v_two)
    elif v_two == -1:
        secondStar += 100*(h_two)
        print("Chose Horizontal 2:",h_two)
    elif h_reflection == h_two:
        secondStar += v_two
        print("Chose Vertical 2:",v_two)
    else:
        secondStar += 100*(h_two)
        print("Chose Horizontal 2:",h_two)




print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))