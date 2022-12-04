import pandas as pd

my_cols = ["elve_1_start", "elve_1_stop", "elve_2_start", "elve_2_stop"]  # create some col names

data = pd.read_csv("Day_04/input_leo.txt", sep="-|,", names=my_cols, header=None, engine="python")

data = data.astype(int)

overlaps_1 = 0
overlaps_2 = 0

for pair in range(len(data.index)):
    a = data["elve_1_start"][pair]
    b = data["elve_1_stop"][pair]
    c = data["elve_2_start"][pair]
    d = data["elve_2_stop"][pair]

    if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
        overlaps_1 += 1

    if (a <= c <= b or a <= d <= b) or (c <= a <= d or c <= b <= d):
        overlaps_2 += 1


print("Ergebnis Part 1: ", overlaps_1)

print("Ergebnis Part 2: ", overlaps_2)
