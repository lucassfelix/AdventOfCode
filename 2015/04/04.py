import sys, hashlib
#file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = "yzbqklnj"
test = b"abcdef609043"

i = 0
while True:
    i += 1

    newStr = input + str(i)

    md5Hex = hashlib.md5(newStr.encode()).hexdigest()[0:6]

    if md5Hex == "000000":
        firstStar = i
        break


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))