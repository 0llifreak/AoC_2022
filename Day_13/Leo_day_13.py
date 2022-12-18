import json
import ast

with open("Day_13/test.txt", "r") as f:
    data = f.read()

x = data.split("\n")

y = []

for n in range(len(x)):
    if x[n].strip():
        y.append(ast.literal_eval(x[n]))

right_order = []
set = 0
j = 0
b = 0


for i in range(0, len(y), 2):
    set += 1
    b = 0
    x = 0

    comp = []

    comp.append(y[i])
    comp.append(y[i + 1])

    while comp:
        # if len(y[i]) > len(y[i + 1]):
        #     rgn = len(y[i + 1])
        # else:
        #     rgn = len(y[i])
        # j = 0
        right = comp.pop()
        left = comp.pop()
        while b == 0:

            if type(left[0]) == int and type(right[0]) == int:
                if left[0] == right[0]:
                    continue
                elif left[0] < right[0]:
                    right_order.append(set)
                    b == 1
                else:
                    b == 1
            else:
                comp.append(left[0])
                comp.append(right[0])
                b == 1

    #     for j in range(0, rgn):
    #         # if b == 1:
    #         #     break
    #         if type(y[i][j]) == type(y[i + 1][j]):
    #             if type(y[i][j]) == int:
    #                 if y[i][j] == y[i + 1][j]:
    #                     continue
    #                 elif y[i][j] < y[i + 1][j]:
    #                     right_order.append(set)
    #                     b = 1
    #                     break
    #                 else:
    #                     b = 1
    #                     break
    #             else:
    #                 for h in range(len(y[i][j])):
    #                     if type(y[i][j][h]) == int and type(y[i][j][h]) == type(y[i + 1][j][h]):
    #                         if y[i][j][h] == y[i + 1][j][h]:
    #                             continue
    #                         elif y[i][j][h] < y[i + 1][j][h]:
    #                             right_order.append(set)
    #                             b = 1
    #                             break
    #                         else:
    #                             b = 1
    #                             break

    #         else:
    #             if type(y[i][j]) == int:
    #                 y[i][j] = [y[i][j]]
    #             else:
    #                 y[i + 1][j] = [y[i + 1][j]]

    #             for h in range(len(y[i][j])):
    #                 if y[i][j][h] == y[i + 1][j][h]:
    #                     continue
    #                 elif y[i][j][h] < y[i + 1][j][h]:
    #                     right_order.append(set)
    #                     b = 1
    #                     break
    #                 else:
    #                     b = 1
    #                     break

    # if (j == len(y[i]) - 1 or (j == 0 and rgn = len(y[i]))) and set not in right_order and b == 0:
    #     right_order.append(set)
