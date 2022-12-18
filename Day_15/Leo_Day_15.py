import re
from scipy.spatial.distance import cityblock

with open("Day_15/test.txt", "r") as f:
    data = f.read()

x = data.split("\n")

Sensor = []
Beacon = []

for line in x:
    splited = re.split("x=|, y=|:", line)

    Sensor.append([int(splited[1]), int(splited[2])])
    Beacon.append([int(splited[4]), int(splited[5])])

man_dist = []

for i in range(len(Sensor)):
    man_dist.append(cityblock(Sensor[i], Beacon[i]))

possibilities = []
for i in range(len(Sensor)):
    for x_val in range(-10, 30):
        if cityblock(Sensor[i], [x_val, 10]) <= man_dist[i] and x_val not in possibilities:
            possibilities.append(x_val)
            print(x_val)


print(len(possibilities))
