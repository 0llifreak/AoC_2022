import pandas as pd
from numpy.linalg import norm
import numpy as np

data = pd.read_csv("Day_09/input_leo.txt", sep=" ", names=["Direction", "Value"])
print(data)

visited_by_t = {(0, 0): True}

# (0: 0) (x: y)

pos_H = np.array([0, 0])
pos_T = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9):
    pos_T[i] = np.array([0, 0])

print(pos_T)
move_h = []

for i in data.index:
    val = int(data["Value"][i])
    for j in range(val):
        move_h.append(data["Direction"][i])

# print(move_h)

for char in move_h:
    if char == "U":
        pos_H[1] += 1
    elif char == "D":
        pos_H[1] -= 1
    elif char == "L":
        pos_H[0] -= 1
    elif char == "R":
        pos_H[0] += 1

    if norm(pos_H - pos_T[0]) > np.sqrt(2):
        if pos_H[0] - pos_T[0][0] > 0 and pos_H[1] - pos_T[0][1] == 0:
            pos_T[0][0] += 1
        elif pos_H[0] - pos_T[0][0] < 0 and pos_H[1] - pos_T[0][1] == 0:
            pos_T[0][0] -= 1
        elif pos_H[1] - pos_T[0][1] > 0 and pos_H[0] - pos_T[0][0] == 0:
            pos_T[0][1] += 1
        elif pos_H[1] - pos_T[0][1] < 0 and pos_H[0] - pos_T[0][0] == 0:
            pos_T[0][1] -= 1
        elif pos_H[1] - pos_T[0][1] < 0 and pos_H[0] - pos_T[0][0] < 0:
            pos_T[0][1] -= 1
            pos_T[0][0] -= 1
        elif pos_H[1] - pos_T[0][1] > 0 and pos_H[0] - pos_T[0][0] < 0:
            pos_T[0][1] += 1
            pos_T[0][0] -= 1
        elif pos_H[1] - pos_T[0][1] < 0 and pos_H[0] - pos_T[0][0] > 0:
            pos_T[0][1] -= 1
            pos_T[0][0] += 1
        elif pos_H[1] - pos_T[0][1] > 0 and pos_H[0] - pos_T[0][0] > 0:
            pos_T[0][1] += 1
            pos_T[0][0] += 1

        for i in range(0, 8):
            if norm(pos_T[i] - pos_T[i + 1]) > np.sqrt(2):
                if pos_T[i][0] - pos_T[i + 1][0] > 0 and pos_T[i][1] - pos_T[i + 1][1] == 0:
                    pos_T[i + 1][0] += 1
                elif pos_T[i][0] - pos_T[i + 1][0] < 0 and pos_T[i][1] - pos_T[i + 1][1] == 0:
                    pos_T[i + 1][0] -= 1
                elif pos_T[i][1] - pos_T[i + 1][1] > 0 and pos_T[i][0] - pos_T[i + 1][0] == 0:
                    pos_T[i + 1][1] += 1
                elif pos_T[i][1] - pos_T[i + 1][1] < 0 and pos_T[i][0] - pos_T[i + 1][0] == 0:
                    pos_T[i + 1][1] -= 1
                elif pos_T[i][1] - pos_T[i + 1][1] < 0 and pos_T[i][0] - pos_T[i + 1][0] < 0:
                    pos_T[i + 1][1] -= 1
                    pos_T[i + 1][0] -= 1
                elif pos_T[i][1] - pos_T[i + 1][1] > 0 and pos_T[i][0] - pos_T[i + 1][0] < 0:
                    pos_T[i + 1][1] += 1
                    pos_T[i + 1][0] -= 1
                elif pos_T[i][1] - pos_T[i + 1][1] < 0 and pos_T[i][0] - pos_T[i + 1][0] > 0:
                    pos_T[i + 1][1] -= 1
                    pos_T[i + 1][0] += 1
                elif pos_T[i][1] - pos_T[i + 1][1] > 0 and pos_T[i][0] - pos_T[i + 1][0] > 0:
                    pos_T[i + 1][1] += 1
                    pos_T[i + 1][0] += 1

        visited_by_t[(pos_T[8][0], pos_T[8][1])] = True

# print(visited_by_t)

print("Solution Part 2:", len(visited_by_t))
