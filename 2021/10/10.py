input = [lines.strip("\n") for lines in open("input.txt").readlines()]

results = {')':0,']':0,'>':0,'}':0}
opposite = {')':'(',']':'[','>':'<','}':'{'}
stack = []

def findFirstIllegal(results, line):
    stack = []
    for char in line:
        if char in results.keys():
            if stack[-1] != opposite[char] and len(stack) != 0:
                results[char] += 1
                return True
            else:
                stack.pop()
        else:
            stack.append(char)
    return False
discard = []
for lineIndex, line in enumerate(input):
    if findFirstIllegal(results,line):
        discard.append(lineIndex)

input = [input[i] for i in range(len(input)) if i not in discard]
print(input)
firstStar = results[')'] * 3 + results[']'] * 57 + results['}']*1197 + results['>']*25137

results = {'(':1,'[':2,'<':4,'{':3}
flip = {'(':')','[':']','<':'>','{':'}'}

secondStar = 0
scores = []
for line in input:
    stack = []
    for char in line:
        if char in opposite.keys():
            stack.pop()
        elif char in flip.keys():
            stack.append(char)
    score = 0
    stack.reverse()
    for char in stack:
        print(results[char])
        score = score * 5 + results[char]
    scores.append(score)
    
scores = sorted(scores)

secondStar = scores[len(scores)//2]

print(firstStar)
print(secondStar)
