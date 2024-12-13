import cmath
from collections import defaultdict


data = defaultdict(str)

directions = [1,1j,-1,-1j]

with open("12.txt") as file:
    for i, line in enumerate(file):
        for k, x in enumerate(line.strip()):
            data[i*1j + k] = x

def get_nbrs (data, p):
    x = data[p]
    nbrs = set()
    nbrs.add(p)
    to_check = [p]
    while to_check:
        p = to_check.pop()
        for d in directions:
            if data[p+d] == x and p+d not in nbrs:
                to_check.append(p+d)
                nbrs.add(p+d)
    return nbrs

def get_perim(data,region):
    borders = 0
    for p in region:
        n = data[p]
        for d in directions:
            if data[p+d] != n:
                borders += 1
    return borders

def conv_corner(data,p):
    l = data[p]
    corner_count = len([r for r in directions if data[p+r] != l and data[p+r*1j] != l])
    return corner_count

def conc_corner(data,p):
    l = data[p]
    corner_count = len([r for r in directions if data[p+r] == l\
                        and data[p+r*1j] == l and data[p+r*1j+r] != l])
    return corner_count


regions = []
checked = set()

for p in set(data.keys()):
    if p not in checked:
        nbrhood = get_nbrs(data,p)
        regions.append(nbrhood)
        checked.update(nbrhood)

ans1 = 0
for region in regions:
    ans1 += get_perim(data, region)*len(region)
print(ans1)


ans2 = 0
for region in regions:
    conv_count = sum([conv_corner(data,p) for p in region]) 
    conc_count = sum([conc_corner(data,p) for p in region])
    area = len(region)
    ans2 += area*(conv_count+ conc_count)
print(ans2)


