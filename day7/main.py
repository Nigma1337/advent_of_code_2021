import numpy as np
import math
from collections import Counter
from tqdm import tqdm
def part_1():
    with open("input.txt", "r") as f:
        a = list(map(int, f.read().split(",")))
        b = np.array(a)
        med = np.median(b)
        diffs = np.subtract(a, np.full(len(a), med, dtype=np.intc))
        return sum(np.where(diffs<0, abs(diffs), diffs))

def part_2():
    with open("input.txt", "r") as f:
        a = list(map(int, f.read().split(",")))
    used = math.inf
    for avg in tqdm([math.floor(np.mean(a)), round(np.mean(a))]):
        with open("input.txt", "r") as f:
            a = list(map(int, f.read().split(",")))
            usage = 0
            used_here=0
            while(len(Counter(a))!=1):
                usage += 1
                for index, value in enumerate(a):
                    if value<avg:
                        used_here += usage
                        a[index] += 1
                    elif value>avg:
                        used_here += usage
                        a[index] -= 1
        if used_here<used:
            used = used_here
    return used
print(part_2())