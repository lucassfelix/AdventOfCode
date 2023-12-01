from queue import PriorityQueue
import sys,re,math
import itertools
from tqdm import tqdm

file = open(sys.argv[1])
firstStar = 0
secondStar = 0


arq = [line.strip() for line in file.readlines()]

class blueprint:

    index = 0
    oreRobotCost = 0
    clayRobotCost = 0
    obsidianRobotOreCost = 0
    obsidianRobotClayCost = 0
    geodeRobotOreCost = 0
    geodeRobotObsidianCost = 0

    def __str__(self) -> str:
        return f"Blueprint {self.index}\n\tOre Robot : {self.oreRobotCost} ores\n\tClay Robot : {self.clayRobotCost} ores\n\tObsidian Robot : {self.obsidianRobotOreCost} ores, {self.obsidianRobotClayCost} clays\n\tGeode Robot : {self.geodeRobotOreCost} ores, {self.geodeRobotObsidianCost} obsidians\n"

    def __init__(self,index,oreRobot,clayRobot,obsidianOre,obsidianClay,geodeOre,geodeObsidian) -> None:
        self.index = index
        self.oreRobotCost = oreRobot
        self.clayRobotCost = clayRobot
        self.obsidianRobotOreCost = obsidianOre
        self.obsidianRobotClayCost = obsidianClay
        self.geodeRobotOreCost = geodeOre
        self.geodeRobotObsidianCost = geodeObsidian

#Stock 0 = ore 1 = clay 2 = obsidian 3 = geodes
def simulate(bp : blueprint, minute,robots,stock):

    if minute == 24:
        print("Finished Cycle with value =",stock[3])
        return stock[3]

    input()


    print(f"Minute ({minute+1}). Before generating resources.\nRobots: {robots}\nStock: {stock}");

    for i in range(len(stock)):
        stock[i] += robots[i]

    input()
    options = []

    print(f"Minute ({minute+1}). After generating resources.\nRobots: {robots}\nStock: {stock}");

    input()

    if stock[0] >= bp.geodeRobotOreCost and stock[2] >= bp.geodeRobotObsidianCost:
        robots[3] += 1
        stock[0] -= bp.geodeRobotOreCost
        stock[2] -= bp.geodeRobotObsidianCost
        print(f"Minute ({minute+1}). Building Geode Robot...\nRobots: {robots}\nStock: {stock}"")
        options.append(simulate(bp,minute+1,robots,stock))
        
        robots[3] -= 1
        stock[0] += bp.geodeRobotOreCost
        stock[2] += bp.geodeRobotObsidianCost

    if stock[0] >= bp.obsidianRobotOreCost and stock[1] >= bp.obsidianRobotClayCost:
        robots[2] += 1
        stock[0] -= bp.obsidianRobotOreCost
        stock[1] -= bp.obsidianRobotClayCost
        print(f"Minute ({minute+1}). Building Obsidian Robot...\n")
        options.append(simulate(bp,minute+1,robots,stock))
        robots[2] -= 1
        stock[0] += bp.obsidianRobotOreCost
        stock[1] += bp.obsidianRobotClayCost

    if stock[0] >= bp.clayRobotCost:
        robots[1] += 1
        stock[0] -= bp.clayRobotCost
        print(f"Minute ({minute+1}). Building Clay Robot...\n")
        options.append(simulate(bp,minute+1,robots,stock))
        robots[1] -= 1
        stock[0] += bp.clayRobotCost

    if stock[0] >= bp.oreRobotCost:
        robots[0] += 1
        stock[0] -= bp.oreRobotCost
        print(f"Minute ({minute+1}). Building Ore Robot...\n")
        options.append(simulate(bp,minute+1,robots,stock))
        robots[0] -= 1
        stock[0] += bp.oreRobotCost

    if len(options) == 0:
        
        print(f"Minute ({minute+1}). Can't Build Robot...\n")
        options.append(simulate(bp,minute+1,robots,stock))
        

    return max(options)



blueprints = []

for line in arq:
    bNumber, oreRobot, clayRobot, obsidianOre, obsidianClay, geodeOre, geodeObsidian = list(map(int, re.findall(r'-?\d+', line)))

    newBlueprint = blueprint(bNumber,oreRobot,clayRobot,obsidianOre,obsidianClay,geodeOre,geodeObsidian)
    blueprints.append(newBlueprint)


stock = [0,0,0,0]
robots = [1,0,0,0]


print(blueprints[0])
print(simulate(blueprints[0],0,robots,stock))


print("Answer first star: {}".format(firstStar))
print("Answer second star: {}".format(secondStar))

