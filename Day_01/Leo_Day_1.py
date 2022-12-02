# import pandas as pd
import numpy as np


#my_file = open("Day_01/input_leo.txt", "r")


# data = my_file.read()
# data_into_list = data.split("\n")
# my_file.close()

# Using a context manager
with open("Day_01/input_leo.txt", "r"):
    data = my_file.read()
data_into_list = data.split("\n")

i = 0
for element in data_into_list:
    if element == "":
        data_into_list[i] = "0"
    i = i + 1

data_into_list = list(map(int, data_into_list))
print(data_into_list)

####PART 1######################

j = 0
totals = []
while j < len(data_into_list):
    total1 = 0
    while data_into_list[j] != 0:
        total1 += data_into_list[j]
        j = j + 1
    totals.append(total1)
    j = j + 1

print("Ergebnis PART 1:", max(totals))


####PART 2######################

print("Ergebnis PART 2:", sum(sorted(totals, reverse=True)[:3]))
