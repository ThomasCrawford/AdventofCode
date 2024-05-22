from day_10 import encode
import cmath

key = "hwlqcszp"

def get_nb (z):
    nbs = []
    for d in [1,1j,-1,-1j]:
        if 0<=(z + d).real <128 and 0<=(z + d).imag <128:
            nbs.append(z+d)
    return nbs

def this_group(data, z):
    group = set()
    new = [z]
    while new:
        x = new.pop()
        for y in get_nb(x):
            if data[y]=="1" and y not in new and y not in group:
                new.append(y)
        group.add(x)
    return group


ans1 = 0
grid = {}
for i in range(128):
    to_encode = key + f'-{i}'
    x = encode(to_encode)
    x = list(format(int(x,16), '0>128b'))
    ans1 += x.count('1')
    for k,v in enumerate(x):
        grid[k+i*1j] = v
print(f'Part 1: {ans1}')


groups = []
visited = set()
unchecked = [z for z in grid.keys() if grid[z]=="1"]

while unchecked:
    x = unchecked.pop()
    if x not in visited:
        g = this_group(grid,x)
        groups.append(g)
        for y in g:
            visited.add(y)

print(f'Part 2: {len(groups)}')
