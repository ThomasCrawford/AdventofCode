import cmath
from collections import defaultdict
import itertools


grid = set()

ants = defaultdict(list)

with open("08.txt") as file:
    for i, line in enumerate(file):
        for k, x in enumerate(line.strip()):
            grid.add(k+i*1j)
            if x != ".":
                ants[x].append(k+i*1j)

def reduced(n,m):
    for d in range(2,abs(n)+1):
        if n%d == 0 and m%d == 0:
            return reduced(n//d,m//d)
    return n,m

def locations(ants):
    locs = set()
    for a,b in itertools.permutations(ants,2):
        locs.add(2*a-b)
        locs.add(2*b-a)
    return [x for x in locs if x in grid]

def locations2(ants):
    locs = set()
    for a,b in itertools.permutations(ants,2):
        rise = b.imag - a.imag
        run = b.real - a.real
        si,sr = reduced(int(rise),int(run))
        step = sr + si*1j
        while a in grid:
            locs.add(a)
            a += step
        a -= step
        while a in grid:
            locs.add(a)
            a -= step
    return locs

    return [x for x in locs if x in grid]

with_signal = set()
with_signal2 = set()

for ant in ants:
    with_signal.update(locations(ants[ant]))

for ant in ants:
    with_signal2.update(locations2(ants[ant]))

print(len(with_signal))
print(len(with_signal2))

# print(reduced(4,6))
# print(reduced(-10,20))

# for k in range(12):
#     out = ""
#     for i in range(12):
#         if i+k*1j in with_signal:
#             out += "#"
#         elif i+k*1j in ants["0"]:
#             out += "0"
#         elif i+k*1j in ants["A"]:
#             out += "A"
#         else:
#             out += "."
#     print(out)


