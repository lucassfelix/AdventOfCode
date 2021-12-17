import sys,math
file = open(sys.argv[1])
firstStar = 0
secondStar = 0

input = file.readline().strip()
num_of_bits = len(input) * 4
res = bin(int(input, 16))[2:].zfill(num_of_bits)


def parseLiteralPacket(index,nums):
    if res[index] == '0':
        nums.append(res[index+1:index+5])
        return res[index:index+5]
    else:
        nums.append(res[index+1:index+5])
        return res[index:index+5] + parseLiteralPacket(index+5,nums)
    

parseQeue = []

operators = {0:'+',1:'*',2:'min',3:'max',5:'>',6:'<',7:'=',}
#print(res)
def parsePacket(index):
    if len(res[index:]) < 10:
        pass
    #print("Start index:", index)
    #print(res[index:])
    packetVersion = res[index:index+3]
    packetTypeId = res[index+3:index+6]
    #print("Packet Version:", int(packetVersion,2))
    #print("Packet Type:", int(packetTypeId,2))

    if packetTypeId == '100':
        nums = []
        groups = parseLiteralPacket(index+6,nums)
        num = int(''.join(nums),2)
        #print("Len packet:",len(groups) + 6)
        #print("Literal packet size: ", len(packetVersion + packetTypeId + groups))
        #print(packetVersion + packetTypeId + groups)
        index += len(groups)+6
        parseQeue.append(num)
        #print(num)
        return (num, index, int(packetVersion,2))

    else:
        op = operators[int(packetTypeId,2)]
        #print("OP:",op)
        versionSum = int(packetVersion,2)
        lenghtType = res[index+6]
        subpackets = 0
        nums = []
        index += 7
        #print("Operator with lenghtType: ", lenghtType)
        if lenghtType == '0':
            subpacketType = res[index:index+15]
            lenOfBitsSubpacket = int(subpacketType,2)
            #print("Lenght of bits in subpackets" ,lenOfBitsSubpacket)
            index += 15
            while subpackets != lenOfBitsSubpacket:
                #print("subpackets",subpackets)
                if(lenOfBitsSubpacket - subpackets) < 6:
                    break
                num,tam,version = parsePacket(index)
                versionSum += version
                subpackets += tam - index
                index = tam
                nums.append(num)
        else:
            subpacketType = res[index:index+11]
            numSubpackets = int(subpacketType,2)
            index += 11
            #print("Num of subpackets" ,numSubpackets)
            for i in range(numSubpackets):
                num,index,version = parsePacket(index)
                versionSum += version
                nums.append(num)

        result = 0
        if op == '+':
            result = sum(nums)
        elif op == '*':
            result = math.prod(nums)
        elif op == 'min':
            result = min(nums)
        elif op == 'max':
            result = max(nums)
        elif op == '>':
            if nums[0] > nums[1]:
                result = 1
        elif op == '<':
            if nums[0] < nums[1]:
                result = 1
        elif op == '=':
            if nums[0] == nums[1]:
                result = 1
        #print(result)
        return(result, index, versionSum)

secondStar,a,firstStar = parsePacket(0)


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))