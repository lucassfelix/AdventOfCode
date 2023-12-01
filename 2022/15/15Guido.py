from tqdm import tqdm
class Sensor:

    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
    
    @property
    def beacon_dist(self):
        return Sensor.manhattan_dist(self, self.beacon)

    @staticmethod
    def manhattan_dist(cls, other):
        x = abs(cls.x-other.x)
        y = abs(cls.y-other.y)

        return (x+y)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.beacon))


class Beacon:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __str__(self) -> str:
        return f'Beacon: x={self.x}, y={self.y}'


def blocked(point, sensors):
    for sensor in sensors:
        if Sensor.manhattan_dist(point, sensor) <= sensor.beacon_dist:
            return True
    return False
    
sensors = set([])
beacons = set([])
max_dist = 0

x_dim = (0, 0)
y_dim = (0, 0)

input = [line.strip() for line in open('input.txt')]

for line in input:
    line = line.split()

    beacon_x = int(line[8].split('=')[1][:-1])
    beacon_y = int(line[9].split('=')[1])

    beacon = Beacon(beacon_x, beacon_y)

    if beacon_x < x_dim[0]:
        x_dim = (beacon_x, x_dim[1])

    if beacon_x > x_dim[1]:
        x_dim = (x_dim[0], beacon_x)

    if beacon_y < y_dim[0]:
        y_dim = (beacon_y, y_dim[1])
    
    if beacon_y > y_dim[1]:
        y_dim = (y_dim[0], beacon_y)

    beacons.add(beacon)

    sensor_x = int(line[2].split('=')[1][:-1])
    sensor_y = int(line[3].split('=')[1][:-1])

    sensor = Sensor(sensor_x, sensor_y, beacon)

    sensors.add(sensor)

    if sensor_x < x_dim[0]:
        x_dim = (sensor_x, x_dim[1])

    if sensor_x > x_dim[1]:
        x_dim = (x_dim[0], sensor_x)

    if sensor_y < y_dim[0]:
        y_dim = (sensor_y, y_dim[1])
    
    if sensor_y > y_dim[1]:
        y_dim = (y_dim[0], sensor_y)

    if sensor.beacon_dist > max_dist:
        max_dist = sensor.beacon_dist

x_dim = (x_dim[0]-max_dist, x_dim[1]+max_dist)
print(x_dim)
line = 2000000
blocked_count = 0

for x in tqdm(range(x_dim[0], x_dim[1]+1)):
    b = Beacon(x, line)
    if b not in beacons and blocked(b, sensors):
        blocked_count += 1

print(blocked_count)