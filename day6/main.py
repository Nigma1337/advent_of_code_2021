import numpy as np
from tqdm import tqdm
from multiprocessing import Pool
from collections import Counter

def solve(a):
    count = len(np.where(a==0)[0])
    a = np.concatenate([a, np.full(count, 9, dtype=np.intc)])
    a = np.where(a==0, 6, a-1)
    return a, len(a)

def solve2(days, start):
    a = np.zeros(days+60)
    for i in start:
        a[i] += 1
    for day in range(days):
        a[day+7] += a[day]
        a[day+9] = a[day]
        a[day]=0
    return a

with open("input.txt", "r") as f:
    a = sorted(list(map(int, f.read().split(","))))
    print(sum(solve2(256, a)))