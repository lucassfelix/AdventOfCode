import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = file.readlines()[0].strip().split(",")

def HASH(s):
    current = 0
    for c in s:
        a = ord(c)
        current += a
        current = current*17
        current = current%256
    return current

def print_boxes(boxes:list):
    for i,b in enumerate(boxes):
        if len(b) > 0:
            print("Box",i,b)
    print("----------------------------------")


boxes = [[] for _ in range(256)]


for s in input:
    value = HASH(s)
    firstStar += value


    if(s[-1].isdigit()):
        label = s[:-2]
        box = HASH(label)
        lensFocus = s[-1]
        replaced = False
        for i in range(len(boxes[box])):
            labelSize = len(label)
            if boxes[box][i][:labelSize] == label:
                boxes[box].pop(i)
                boxes[box].insert(i,label + " " + lensFocus)
                replaced = True
                break
        if not replaced:
            boxes[box].append(label + " " + lensFocus)
    else:
        label = s[:-1]
        box = HASH(label)
        for i in range(len(boxes[box])):
            labelSize = len(label)
            if boxes[box][i][:labelSize] == label:
                boxes[box].pop(i)
                break
    
    #print_boxes(boxes)

for index,b in enumerate(boxes):
    for slot,lens in enumerate(b):
        secondStar += (index+1) * (slot+1) * int(lens[-1]) 


    

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))