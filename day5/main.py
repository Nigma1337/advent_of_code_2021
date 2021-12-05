import numpy as np

with open("input.txt", "r") as f:
    a = [b.split(",") for b in f.read().replace(" -> ", ",").splitlines()]
    a = [[int(j) for j in i] for i in a]
    z = np.zeros((2000, 2000))
    for i in a:
        # do x
        if i[1] == i[3] or i[0] == i[2]:
            if i[0] > i[2]:
                for j in range(i[2], i[0] + 1):
                    z[i[1]][j] += 1
            elif i[0] < i[2]:
                for j in range(i[0], i[2] + 1):
                    z[i[1]][j] += 1
        # do y
        if i[0] == i[2] or i[1] == i[3]:
            if i[1] > i[3]:
                for j in range(i[3], i[1] + 1):
                    z[j][i[0]] += 1
            elif i[1] < i[3]:
                for j in range(i[1], i[3] + 1):
                    z[j][i[0]] += 1
    print("Part 1 solution: %i" % sum(sum(np.where(z > 1, 1, 0))))
    # do diagonals
    for i in a:
        x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
        # moving south-east
        if x1 < x2 and y1 < y2:
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 + 1)
            for x, y in zip(x_range, y_range):
                z[y][x] += 1
        # moving north-east
        elif x1 < x2 and y1 > y2:
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 - 1, -1)
            for x, y in zip(x_range, y_range):
                z[y][x] += 1
        # moving north-west
        elif x1 > x2 and y1 > y2:
            x_range = list(range(x2, x1 + 1))
            y_range = range(y2, y1 + 1)
            for x, y in zip(x_range, y_range):
                z[y][x] += 1
        # moving north-east
        elif x1 > x2 and y1 < y2:
            x_range = range(x1, x2 - 1, -1)
            y_range = range(y1, y2 + 1)
            for x, y in zip(x_range, y_range):
                z[y][x] += 1
    print("Part 2 solution: %i" % sum(sum(np.where(z > 1, 1, 0))))
