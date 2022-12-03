import pandas as pd
from collections import Counter

data = pd.read_csv("Day_03/input_leo.txt", sep="\n", names=["Backpacks"])

print(data)

double_letter = []

for i in range(len(data.index)):
    string_all = data["Backpacks"][i]
    index = int(len(string_all) / 2)

    string_a = string_all[:index]
    string_b = string_all[index:]

    for n in range(len(string_a)):
        for m in range(len(string_b)):
            if string_a[n] == string_b[m]:
                double_letter.append(string_a[n])
                break
        else:  # only execute when it's no break in the inner loop
            continue
        break

alphabet = {chr(i + 96): i for i in range(1, 27)} | {chr(j + 64): j + 26 for j in range(1, 27)}

total = 0
for letter in double_letter:
    total += alphabet[letter]


print("Total Part 1:", total)

badge = []
i = 0
while i < 300:
    for a in range(len(data["Backpacks"][i])):
        for b in range(len(data["Backpacks"][i + 1])):
            for c in range(len(data["Backpacks"][i + 2])):
                if data["Backpacks"][i][a] == data["Backpacks"][i + 1][b] == data["Backpacks"][i + 2][c]:
                    badge.append(data["Backpacks"][i][a])
                    break
            else:  # only execute when it's no break in the inner loop
                continue
            break
        else:  # only execute when it's no break in the inner loop
            continue
        break
    i += 3

total2 = 0
for letter in badge:
    total2 += alphabet[letter]


print("Total Part 2:", total2)
