with open("Day_05/input_leo.txt") as file:
    data = [line.rstrip() for line in file]

stacks = {}

for stack in range(1, 10):
    stacks[stack] = []

for i in range(0, 8):
    j = 1
    a = 1
    while j < len(data[i]):
        if data[i][j] != " ":
            stacks[a][:0] = [data[i][j]]
        j += 4
        a += 1


move = data[10::]

for movement in range(len(move)):
    if move[movement][6] == " ":
        no_of_elements = int(move[movement][5])
        start = int(move[movement][12])
        stop = int(move[movement][17])
    else:
        no_of_elements = int(move[movement][5:7])
        start = int(move[movement][13])
        stop = int(move[movement][18])

    # Part 1
    # for i in range(0, no_of_elements):
    #     stacks[stop].extend(stacks[start][-1:])
    #     del stacks[start][-1:]

    # Part 2
    stacks[stop].extend(stacks[start][-(no_of_elements):])
    del stacks[start][-(no_of_elements):]


letters = ""
for stack in stacks.keys():
    letters += stacks[stack].pop(-1)

print("Solution:", letters)
