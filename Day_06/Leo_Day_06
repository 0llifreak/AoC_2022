with open("Day_06/input_leo.txt") as file:
    data = file.read()

for i in range(len(data)):
    marker = []
    for j in range(4):
        marker.append(data[i + j])
    if len(set(marker)) == 4:
        print("Solution Part 1: ", i + j + 1)
        print(marker)
        break


for i in range(len(data)):
    marker = []
    for j in range(14):
        marker.append(data[i + j])
    if len(set(marker)) == 14:
        print("Solution Part 2: ", i + j + 1)
        print(marker)
        break
