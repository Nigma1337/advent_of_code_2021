from collections import Counter
import numpy as np
with open("input.txt", "r") as f:
    gamma = []
    r = f.read().splitlines()
    for i in range(len(r[0])):
        gamma.append(int(Counter([a[i] for a in r]).most_common(1)[0][0]))
    epsilon = int("".join(str(~a%2) for a in gamma), 2)
    gamma = int("".join(str(a) for a in gamma), 2)
    print(gamma*epsilon)

def part_2_commons(res, default, least_common):
    i=0
    while(len(res)>1):
        if least_common:
            c = Counter([a[i] for a in res]).most_common()[::-1]
        else:
            c = Counter([a[i] for a in res]).most_common()
        if c[0][1] == c[1][1]:
            c = default
        else:
            c = c[0][0]
        res = [a for a in res if a[i]==c]
        i+=1
    return res[0]

with open("input.txt", "r") as f:
    r = f.read().splitlines()
    oxygen = int(part_2_commons(r, "1", False), 2)
    co2 = int(part_2_commons(r, "0", True), 2)
    print(oxygen*co2)