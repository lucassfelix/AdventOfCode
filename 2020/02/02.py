import sys
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip("\n") for line in file.readlines()]

invalid = 0
newInvalid = 0

for line in input:
    rule, password = line.split(":")
    occ, letter = rule.split(" ")
    lower,higher = occ.split("-")

    password = password.strip(" ")

    if password.count(letter) < int(lower) or password.count(letter) > int(higher):
        invalid += 1
    
    if password[int(lower)-1].count(letter) + password[int(higher)-1].count(letter)  == 1:
        secondStar += 1

firstStar = len(input) - invalid


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))