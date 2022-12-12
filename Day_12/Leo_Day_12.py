from collections import deque

x = open("Day_12/input_leo.txt", "r").read().splitlines()
x = [list(i) for i in x]

for i in range(len(x)):
    for j in range(len(x[0])):
        if x[i][j] == "S":
            S = (i, j)
            x[i][j] = "a"
        if x[i][j] == "E":
            E = (i, j)
            x[i][j] = "z"

q = deque([(S[0], S[1], 0)])

visited_points = set()

while q:
    a, b, step = q.popleft()
    if (a, b) == E:
        print("Solution Part 1: ", step)
        break
    if (a, b) in visited_points:
        continue
    visited_points.add((a, b))
    for h in range(a - 1, a + 2):
        for v in range(b - 1, b + 2):
            if len(x) > h > 0 and len(x[0]) > v > 0 and (h == a or v == b):
                if ord(x[h][v]) <= ord(x[a][b]) + 1:
                    q.append((h, v, step + 1))


t = 1e99

for ii in range(len(x)):
    for rr in range(len(x[0])):
        if x[ii][rr] != "a":
            continue
        q = deque([(ii, rr, 0)])
        visited_points = set()

        while q:
            a, b, step = q.popleft()
            if (a, b) == E:
                t = min(t, step)
                break
            if (a, b) in visited_points:
                continue
            visited_points.add((a, b))
            if step >= t:
                continue
            for h in range(a - 1, a + 2):
                for v in range(b - 1, b + 2):
                    if len(x) > h >= 0 and len(x[0]) > v >= 0 and (h == a or v == b):
                        if ord(x[h][v]) <= ord(x[a][b]) + 1:
                            q.append((h, v, step + 1))

print("Solution Part 2: ", t)
