from functools import reduce  # forward compatibility for Python 3
import operator
import pprint


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

while line < 1087:
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
        if current_sum < 100001:
            sums.append(current_sum)
        keys.pop()
        keys.pop()
        line += 1


pprint.pprint(Data_structure)

print(sums)

total = 0
for sum in sums:
    total += sum

print(total)
