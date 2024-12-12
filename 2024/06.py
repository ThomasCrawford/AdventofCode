import cmath

obst = set()
grid = set()
with open("06.txt") as file:
    for i,line in enumerate(file):
        for k,x in enumerate(line.strip()):
            grid.add(i*1j+k)
            if x == "#":
                obst.add(i*1j+k)
            elif x == "^":
                init_p = i*1j+k
                p = i*1j+k

def will_loop(new_obs, p):
    total_obst = set(obst)
    total_obst.add(new_obs)
    vis = []
    d = -1j
    vis.append([p,d])
    while p+d in grid:
        if p+d in total_obst:
            d *= 1j
        else:
            p += d
            if [p,d] in vis:
                return True
            vis.append([p,d])
    return False






visited = set()
visited.add(init_p)
d = -1j
blockers = set() #the count of these is ans2


while p+d in grid:
    print(p,d, len(visited))
    if p+d in obst:
        d *= 1j
    else:
        if will_loop(p+d, init_p):
            blockers.add(p+d)
        p += d
        visited.add(p)

print(len(visited))
print(len(blockers))

