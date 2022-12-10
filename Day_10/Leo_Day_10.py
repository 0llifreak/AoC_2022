import pandas as pd
import pprint


data = pd.read_csv("Day_10/input_leo.txt", sep=" ", names=["action", "Value"])
print(data)

cycle = 1
line = 0
X = 1
X_vals = []

while line < len(data.index):
    if data["action"][line] == "noop":
        cycle += 1
        line += 1
        if cycle == 20 or ((cycle - 20) / 40).is_integer():
            X_vals.append(X * cycle)
    elif data["action"][line] == "addx":
        cycle += 1
        if cycle == 20 or ((cycle - 20) / 40).is_integer():
            X_vals.append(X * cycle)
        cycle += 1
        X += int(data["Value"][line])
        if cycle == 20 or ((cycle - 20) / 40).is_integer():
            X_vals.append(X * cycle)

        line += 1


print("Solution Part 1:", sum(X_vals))


cycle = 1
line = 0
X = 1
X_vals = []
arr = [[], [], [], [], [], []]

while line < len(data.index) - 1:
    if data["action"][line] == "noop":
        print_line = int((cycle - 1) / 40)
        if cycle - print_line * 40 == X or cycle - print_line * 40 == X + 1 or cycle - print_line * 40 == X + 2:
            arr[print_line].append("#")
        else:
            arr[print_line].append(" ")
        cycle += 1
        line += 1

    elif data["action"][line] == "addx":
        print_line = int((cycle - 1) / 40)
        if cycle - print_line * 40 == X or cycle - print_line * 40 == X + 1 or cycle - print_line * 40 == X + 2:
            arr[print_line].append("#")
        else:
            arr[print_line].append(" ")
        cycle += 1
        print_line = int((cycle - 1) / 40)
        if cycle - print_line * 40 == X or cycle - print_line * 40 == X + 1 or cycle - print_line * 40 == X + 2:
            arr[print_line].append("#")
        else:
            arr[print_line].append(" ")
        cycle += 1
        X += int(data["Value"][line])

        line += 1


for i in range(6):
    # print(len(arr[i]))
    print(*arr[i], sep="")
