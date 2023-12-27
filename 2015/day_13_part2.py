import re
from functools import lru_cache


data = []
regex = r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).'

def update(a, d, b):
    if a in dists:
        if b in dists[a]:
            dists[a][b] += d
        else:
            dists[a][b] = d
    else:
        dists[a] = {}
        dists[a][b] = d

data = []
with open("input_13.txt") as file:
    for line in file:
        a, s, d, b = re.match(regex, line.strip()).groups()
        data.append([a,s,int(d),b])
names = list(set([x[0] for x in data]))

#add myself to data
for name in names:
    data.append(["Tom", "gain", 0, name])
names.append("Tom")

dists = [[0 for _ in names] for _ in names]


for line in data:
    a, s, d, b = line
    if s == "lose":
        d = -1*d
    dists[names.index(a)][names.index(b)] += d 
    dists[names.index(b)][names.index(a)] += d 


def f(p, remaining, start):
    if not remaining:
        return dists[p][start]
    else:
        poss = [ dists[p][new_p] + \
                f(new_p, tuple([x for x in remaining if x != new_p]), start) \
                for new_p in remaining]
        out = max(poss)
        return out

answer = max([f(p, tuple([x for x in range(len(dists)) if x != p]),p) for p in range(len(dists))])
print(f'Part 1: {answer}')

