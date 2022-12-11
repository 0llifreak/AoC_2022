import math

with open("Day_11/input_leo.txt", "r") as f:
    data = f.read()

data_into_list = data.split("\n")


monkeys = [0, 0, 0, 0, 0, 0, 0, 0]


class monkey:
    def __init__(self, name, items, operation, test, if_true, if_false, inspected):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = inspected


j = 0

for i in range(0, len(data_into_list), 7):
    inspected = 0
    name = data_into_list[i][:8]
    items = []
    operation = ""
    test = 0
    if_true = 0
    if_false = 0

    for char in range(17, len(data_into_list[i + 1]), 4):
        items.append(int(data_into_list[i + 1][char : (char + 3)]))

    for char in range(23, len(data_into_list[i + 2])):
        operation = data_into_list[i + 2][char:]
        break

    for char in range(len(data_into_list[i + 3]) - 1, 0, -1):
        if data_into_list[i + 3][char] == " ":
            test = int(data_into_list[i + 3][char:])
            break

    if_true = int(data_into_list[i + 4][-1])
    if_false = int(data_into_list[i + 5][-1])

    monkeys[j] = monkey(name, items, operation, test, if_true, if_false, inspected)
    j += 1


mod = math.prod([m.test for m in monkeys])

for round in range(10000):
    for monkey in range(len(monkeys)):
        for item in monkeys[monkey].items:
            if monkeys[monkey].operation[0] == "+":
                item = (item + int(monkeys[monkey].operation[-1])) % mod
            if monkeys[monkey].operation[0] == "*":
                if monkeys[monkey].operation[2:] == "old":
                    item = (item * item) % mod
                else:
                    for char in range(len(monkeys[monkey].operation) - 1, 0, -1):
                        if monkeys[monkey].operation[char] == " ":
                            val = int(monkeys[monkey].operation[char:])
                            break
                    item = (item * val) % mod

            # item = int(item / 3)

            if (item % monkeys[monkey].test) == 0:
                monkeys[monkeys[monkey].if_true].items.append(item)

            else:
                monkeys[monkeys[monkey].if_false].items.append(item)

            monkeys[monkey].inspected += 1
        monkeys[monkey].items.clear()


inspect = []
for monkey in range(len(monkeys)):
    inspect.append(monkeys[monkey].inspected)

inspect.sort()

print("Solution Part 2: ", inspect[-1] * inspect[-2])
