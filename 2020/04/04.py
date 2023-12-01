import sys
from functools import reduce
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = [line.strip() for line in file.readlines() if line.strip() != ""]

print(input.join(""))

required = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}

for line in input:
    data = line.split(" ")

    if len(data) < 7:
        continue
    elif len(data) == 7:
        if "cid" in data:
            continue
        else:
            firstStar += 1
    else:
        firstStar += 1


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))