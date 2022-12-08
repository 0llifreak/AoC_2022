import pandas as pd

with open("Day_08/input_leo.txt") as file:
    data = file.read()

data_list = data.split("\n")

visible = 0

for line in range(len(data_list)):
    for char in range(len(data_list[line])):
        val = int(data_list[line][char])
        if line == 0 or char == 0 or line == (len(data_list) - 1) or char == (len(data_list[line]) - 1):
            visible += 1
        elif all(val > int(data_list[i][char]) for i in range(0, line)):
            visible += 1
        elif all(val > int(data_list[i][char]) for i in range(line + 1, len(data_list))):
            visible += 1
        elif all(val > int(data_list[line][i]) for i in range(char + 1, len(data_list[line]))):
            visible += 1
        elif all(val > int(data_list[line][j]) for j in range(0, char)):
            visible += 1

print("Part 1: ", visible)

scenic_score = []

for line in range(len(data_list)):
    for char in range(len(data_list[line])):
        val = int(data_list[line][char])
        up = 0
        down = 0
        left = 0
        right = 0
        if line != 0 and char != 0 and line != (len(data_list) - 1) and char != (len(data_list[line]) - 1):
            for i in range(line - 1, -1, -1):
                if val > int(data_list[i][char]):
                    up += 1
                elif val <= int(data_list[i][char]):
                    up += 1
                    break
                else:
                    break
            for i in range(line + 1, len(data_list)):
                if val > int(data_list[i][char]):
                    down += 1
                elif val <= int(data_list[i][char]):
                    down += 1
                    break
                else:
                    break
            for i in range(char + 1, len(data_list[line])):
                if val > int(data_list[line][i]):
                    right += 1
                elif val <= int(data_list[line][i]):
                    right += 1
                    break
                else:
                    break
            for j in range(char - 1, -1, -1):
                if val > int(data_list[line][j]):
                    left += 1
                elif val <= int(data_list[line][j]):
                    left += 1
                    break
                else:
                    break

        if up * down * left * right > 0:
            scenic_score.append(up * down * left * right)

print("Part 2: ", max(scenic_score))
