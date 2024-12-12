import cmath
from collections import defaultdict


data = defaultdict(lambda:-1)
with open("10.txt") as file:
    for i, line in enumerate(file):
        for k, x in enumerate(line.strip()):
            if x != ".":
                data[k+i*1j] = int(x)

locs = {}
directions = [1,1j,-1,-1j]


for p in data:
    if data[p]==9:
        locs[p] = set([p])
for n in range(9)[::-1]:
    for p in dict(data):
        if data[p] == n:
            locs[p] = set()
            for d in directions:
                if data[p+d] == n+1:
                    locs[p].update(locs[p+d])

ans1 = sum([len(locs[p]) for p in data if data[p] == 0])

# for x in scores:
#     print(x,scores[x])
print(ans1)



