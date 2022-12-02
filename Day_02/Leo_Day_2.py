import pandas as pd


data = pd.read_csv("Day_02/input_leo.txt", sep=" ", names=["Gegner", "Antwort"])

# X = 1 Y = 2 Z = 3
# A-Y, B-Z, C-X 6
# A-X, B-Y, C-Z 3
# A-Z, B-X, C-Y 0

result_table = {}

result_table["A", "X"] = 3
result_table["A", "Y"] = 6
result_table["A", "Z"] = 0
result_table["B", "X"] = 0
result_table["B", "Y"] = 3
result_table["B", "Z"] = 6
result_table["C", "X"] = 6
result_table["C", "Y"] = 0
result_table["C", "Z"] = 3

Value_table = {}
Value_table["X"] = 1
Value_table["Y"] = 2
Value_table["Z"] = 3


####PART 1########################
Total = 0

for i in range(len(data.index)):
    Total += Value_table[data["Antwort"][i]] + result_table[data["Gegner"][i], data["Antwort"][i]]


print("Gesamtpunktzahl Part 1:", Total)

####PART 2########################

# X = 0, Y = 3, Z = 6
# A-B, B-C, C-A Z
# A-A, B-B, C-C Y
# A-C, B-A, C-B X

data_2 = pd.read_csv("Day_02/input_leo.txt", sep=" ", names=["Gegner", "Spielergebnis"])

antwort_table2 = {}
antwort_table2["A", "X"] = "C"
antwort_table2["A", "Y"] = "A"
antwort_table2["A", "Z"] = "B"
antwort_table2["B", "X"] = "A"
antwort_table2["B", "Y"] = "B"
antwort_table2["B", "Z"] = "C"
antwort_table2["C", "X"] = "B"
antwort_table2["C", "Y"] = "C"
antwort_table2["C", "Z"] = "A"

result_table2 = {}
result_table2["X"] = 0
result_table2["Y"] = 3
result_table2["Z"] = 6

Value_table2 = {}
Value_table2["A"] = 1
Value_table2["B"] = 2
Value_table2["C"] = 3

Total2 = 0

for i in range(len(data_2.index)):
    Total2 += result_table2[data_2["Spielergebnis"][i]] + Value_table2[antwort_table2[data_2["Gegner"][i], data_2["Spielergebnis"][i]]]


print("Gesamtpunktzahl Part 2:", Total2)
