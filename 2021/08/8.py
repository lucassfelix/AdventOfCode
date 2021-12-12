def allDigits(a,b):
    for char in a:
        if char not in b:
            return False
    return True

def solve(inputs):
    solution = {}
    numToDigits = {}
    for digits in inputs:
        digits = "".join(sorted(digits))
        if len(digits) == 3:
            solution[digits] = 7
            numToDigits[7] = digits
        elif len(digits) == 4:
            solution[digits] = 4
            numToDigits[4] = digits
        elif len(digits) == 2:
            solution[digits] = 1
            numToDigits[1] = digits
        elif len(digits) == 7:
            solution[digits] = 8
            numToDigits[8] = digits

    for digits in inputs:
        digits = "".join(sorted(digits))
        if len(digits) == 5 and allDigits(numToDigits[7],digits):
            solution[digits] = 3
            numToDigits[3] = digits
        elif len(digits) == 6 and allDigits(numToDigits[4],digits):
            solution[digits] = 9
            numToDigits[9] = digits
        elif len(digits) == 6 and allDigits(numToDigits[1],digits) and not allDigits(numToDigits[4],digits):
            solution[digits] = 0
            numToDigits[0] = digits
        elif len(digits) == 6 and not allDigits(numToDigits[1],digits):
            solution[digits] = 6
            numToDigits[6] = digits
        elif len(digits) == 5 and allDigits(numToDigits[8],"".join(sorted(dict.fromkeys(digits + numToDigits[4])))):
            solution[digits] = 2
            numToDigits[2] = digits
        elif len(digits) == 5 and not allDigits(numToDigits[7],digits):
            solution[digits] = 5
            numToDigits[5] = digits
    
    return solution

lines = [x.strip("\n") for x in open("input.txt").readlines()]
inputs = []
outputs = []
for line in lines:
    inputs.append(line.split("|")[0].strip().split(" "))
    outputs.append(line.split("|")[1].strip().split(" "))

secondStar = 0

for i in range(len(inputs)):
    solution = solve(inputs[i])
    s = ""
    for digits in outputs[i]:
        digits = "".join(sorted(digits))
        s += str(solution[digits])
    print(s)
    secondStar += int(s)
        


firstStar = 0
for line in outputs:
    for digits in line:
        if len(digits) == 3 or len(digits) == 4 or len(digits) == 2 or len(digits) == 7:
            firstStar += 1


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))