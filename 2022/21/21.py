from queue import PriorityQueue
import sys,re,math
import sympy

file = open(sys.argv[1])
firstStar = 0
secondStar = 0



arq = [line.strip() for line in file.readlines()]

monkeys = {}

def getRoot(monkey):

    value = monkeys[monkey]
    
    if type(value) is int:
        return value
    m1,op,m2 = value

    if op == "+":
        return getRoot(m1) + getRoot(m2)

    if op == "-":
        return getRoot(m1) - getRoot(m2)

    if op == "*":
        return getRoot(m1) * getRoot(m2)
    
    
    return getRoot(m1) // getRoot(m2)

def getEqualRoot(monkey):

    if monkey == "humn":
        return ("x")


    value = monkeys[monkey]
    
    if type(value) is int:
        return str(value)
    
    m1,op,m2 = value

    if monkey == "root":
        return "(" + getEqualRoot(m1) + " == " + getEqualRoot(m2) + ")"

    if op == "+":
        return "(" + getEqualRoot(m1) + " + " + getEqualRoot(m2) + ")"

    if op == "-":
        return "(" + getEqualRoot(m1) + " - " + getEqualRoot(m2) + ")"

    if op == "*":
        return "(" + getEqualRoot(m1) + " * " + getEqualRoot(m2) + ")"
    
    
    return "(" + getEqualRoot(m1) + " / " + getEqualRoot(m2) + ")"

for line in arq:

    m1,aux = line.split(":");
    try:
        _,m2,op,m3 = line.split(" ");
        monkeys[m1] = (m2,op,m3)
    except:
        num = int(re.findall(r'\d+',aux)[0])
        monkeys[m1] = num

firstStar = getRoot("root")
m1,_,m2 = monkeys["root"]
expr1 = getEqualRoot(m1)
expr2 = getEqualRoot(m2)

a = sympy.sympify(expr1)
b = sympy.sympify(expr2)
#print(expr1,a)
#print(b)
#print(sympy.Eq(a,b))
secondStar = sympy.solve(sympy.Eq(a,b))[0]
#print(sympy.solve(sympy.parsing.sympy_parser.parse_expr(expr,evaluate=False)))

print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

