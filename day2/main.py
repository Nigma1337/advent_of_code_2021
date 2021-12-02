import re
with open("input.txt", "r") as f:
    hoz, dep=0,0
    res = f.read().replace("forward", "hoz+=").replace("down", "dep+=").replace("up", "dep-=")
    exec(res)
    #pt1
    print(hoz*dep)
with open("input.txt", "r") as f:
    hoz, dep, aim=0,0,0
    res = f.read().replace("down", "aim+=").replace("up", "aim-=")
    res = re.sub(r"forward (\d)", r"hoz+=\1;dep+=aim*\1", res)
    exec(res)
    print(hoz, dep, hoz*dep)