

def manhattan(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

def closest_coord(x,y):
    best = None
    dist = 999
    for i, p in enumerate(data):
        d = manhattan(x,y,p[0],p[1])
        if d == dist:
            best = None
        elif d < dist:
            dist = d
            best = i
    return best

def total_dist(x,y):
    return sum([manhattan(x,y,x2,y2) for [x2,y2] in data])

data = []
with open("input_06.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip().split(',')])


xmin = min([p[0] for p in data])-1
xmax = max([p[0] for p in data])+2
ymin = min([p[1] for p in data])-1
ymax = max([p[1] for p in data])+2


size = {}
for y in range(ymin,ymax):
    for x in range(xmin, xmax):
        c = closest_coord(x,y)
        if c not in size:
            size[c] = 1
        else:
            size[c] += 1

bdry_pts = []
for x in range(xmin, xmax):
    bdry_pts.append([x,ymin])
    bdry_pts.append([x,ymax-1])
for y in range(ymin, ymax):
    bdry_pts.append([xmin,y])
    bdry_pts.append([xmax-1,y])

del size[None]
for p in bdry_pts:
    c = closest_coord(p[0],p[1])
    if c in size:
        del size[c]

ans1 = size[max(size, key=size.get)]
print(f'Part 1: {ans1}')

#Part 2:
ans2 = 0
for y in range(ymin,ymax):
    for x in range(xmin, xmax):
        tot_dist = total_dist(x,y)
        if tot_dist < 10000:
            ans2 += 1
print(f'Part 2: {ans2}')


