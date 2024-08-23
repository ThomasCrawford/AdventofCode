import cmath

import time
start_time = time.time()


data = {}
with open("input20.txt") as file:
    for y,line in enumerate(file):
        for x,v in enumerate(line[:-1]):
            data[x+y*1j] = v

directions = {1,-1,1j,-1j}

portal_locations = {}
for z in data:
    if data[z] not in ["#","."," "]:
        for d in directions:
            if z+d in data and z+2*d in data and data[z+d] not in ["#","."," "] and data[z+2*d] == ".":
                portal_locations[z+2*d] = set([data[z],data[z+d]])

#Which spaces can teleport and where
jumps = {}
for z in portal_locations:
    other = [x for x in portal_locations if portal_locations[x] == portal_locations[z] and x!=z]
    if other:
        jumps[z] = other[0]

#Find start and end of maze
for p in portal_locations:
    if portal_locations[p] == set("A"):
        start = p
    elif portal_locations[p] == set("Z"):
        end = p

inner = set()
for p in portal_locations:
    if all([p+3*d in data for d in directions]):
        inner.add(p)


def flood_fill(start, end):
    q = [(start,0)]
    seen = set()
    while q:
        p, steps = q.pop(0)
        seen.add(p)
        if p == end:
            return steps
        if p in jumps and jumps[p] not in seen:
            q.append((jumps[p],steps+1))
        for d in directions:
            if data[p+d] == "." and p+d not in seen:
                q.append((p+d,steps+1))


def flood_fill2(start, end):
    q = [(start,0,0)] #location, level, steps
    seen = set()
    while q:
        p, level, steps = q.pop(0)
        seen.add((p,level))
        if p == end and level == 0:
            return steps
        if p in jumps and (level > 0 or p in inner): # if at a portal and not at the top level
            new_level = level + 1 if p in inner else level - 1
            if (jumps[p], new_level) not in seen:
                q.append((jumps[p],new_level, steps+1))
        for d in directions:
            if data[p+d] == "." and (p+d,level) not in seen:
                q.append((p+d,level, steps+1))

ans1 = flood_fill(start,end)
print(f'Part 1: {ans1}')

print("--- %s seconds ---" % (time.time() - start_time))


ans2 = flood_fill2(start,end)
print(f'Part 2: {ans2}')

print("--- %s seconds ---" % (time.time() - start_time))



