#Advent Tag 1
#Lara

#Part 1
items = []

with open('input1_lara.txt', 'r') as input:
    for line in input:
        items.append(line.strip())

elves=[[]]

for element in items:
    if element == '':
        elves.append([])
    elif element != '': 
        elves[-1].append(int(element))

summen=[]

for i in elves:
    summen.append(sum(i))

print(max(summen))

#Part2
summen.sort()
top3=sum(summen[-3:])
print(top3)