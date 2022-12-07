from functools import reduce
import operator
import pprint
import json


def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


def calc_inner_sum(key, value):
    while len(key) > 0:
        key.append("inner_sum")
        current_sum = getFromDict(Data_structure, key)
        new_sum = current_sum + value
        setInDict(Data_structure, key, new_sum)
        key.pop()
        key.pop()


with open("Day_07/input_leo.txt") as file:
    data = [line.rstrip() for line in file]

Data_structure = {}

Data_structure["/"] = {}

keys = []

line = 0

sums = []
sums2 = []

while line < 1090:
    if data[line][0:4] == "$ cd" and data[line][5] != ".":
        keys.append(data[line][5:])
        keys.append("inner_sum")
        setInDict(Data_structure, keys, 0)
        keys.pop()
        i = 1
        line += 1
        if data[line][0:4] == "$ ls":
            line += 1
            while i != 0 and line < len(data):
                if data[line][0] == "d":
                    keys.append(data[line][4:])
                    setInDict(Data_structure, keys, {})
                    keys.pop()
                    line += 1
                elif data[line][0] != "d" and data[line][0] != "$":
                    value = data[line].split(" ")
                    keys.append(value[1])
                    setInDict(Data_structure, keys, int(value[0]))
                    keys.pop()
                    calc_inner_sum(keys.copy(), int(value[0]))
                    line += 1
                else:
                    i = 0
    else:
        keys.append("inner_sum")
        current_sum = getFromDict(Data_structure, keys)
        sums2.append(current_sum)
        if current_sum < 100001:
            sums.append(current_sum)
        keys.pop()
        keys.pop()
        line += 1


pprint.pprint(Data_structure)

with open("Day_07/output_leo.txt", "w") as convert_file:
    convert_file.write(json.dumps(Data_structure, indent=4))


print(sums)
total = 0
for sum in sums:
    total += sum

print("Part 1: ", total)


to_empty = 30000000 - (70000000 - Data_structure["/"]["inner_sum"])

print(to_empty)
possibilities = []
for sum in sums2:
    if sum >= to_empty:
        possibilities.append(sum)

print("Part 2: ", min(possibilities))
