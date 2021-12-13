import numpy as np

def y_fold(fold, paper, ys):
    #amount of rows to flip over
    amount = max(ys)-fold
    count = 0
    for i in range(0, amount+1):
        paper[fold-i] += paper[fold+i]
        count+=1
    paper = np.where(paper > 0, 1, 0)
    return paper[:fold]

def x_fold(fold, paper, ys):
    #amount of rows to flip over
    paper = np.rot90(paper)
    amount = max(ys)-fold
    count = 0
    for i in range(0, amount+1):
        paper[fold-i] += paper[fold+i]
        count+=1
    paper = np.where(paper > 0, 1, 0)
    return paper[:fold]

with open("input.txt", "r") as f:
    res = f.read().splitlines()
    res = [i.split(",") for i in res]
    fold = res[-1]
    res = res[:-2]
    res = [list(map(int, i)) for i in res]
    xs = []
    ys = []
    for i in res:
        xs.append(i[0])
        ys.append(i[1])
    paper = np.zeros((max(ys)+1, max(xs)+1))
    for i in range(len(xs)):
        paper[ys[i]][xs[i]] = 1
    #fold moment
    res = x_fold(655, paper, xs)
    print("part 1: "+str(sum(sum(res))))