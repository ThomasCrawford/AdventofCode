import copy


fav_num = 1358
target = (31,39)


def passable(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + fav_num
    b = len([x for x in str(bin(n)) if x == '1'])
    return not b%2

def get_neighbors(x,y):
    out = [(x+1, y), (x,y+1)]
    if x > 0:
        out.append((x-1,y))
    if y >0:
        out.append((x,y-1))
    return out


seen = set()
seen.add((1,1))
this_gen = set()
this_gen.add((1,1))
counter = 0

while target not in seen:
    nex_gen = set()
    for (a,b) in this_gen:
        nex_gen.update([(i,j) for (i,j) in get_neighbors(a,b) if (i,j) not in seen and passable(i,j)])
    seen.update(nex_gen)
    this_gen = copy.deepcopy(nex_gen)
    counter += 1
print(f'Part 1: {counter}')

seen = set()
seen.add((1,1))
this_gen = set()
this_gen.add((1,1))

for i in range(50):
    nex_gen = set()
    for (a,b) in this_gen:
        nex_gen.update([(i,j) for (i,j) in get_neighbors(a,b) if (i,j) not in seen and passable(i,j)])
    seen.update(nex_gen)
    this_gen = copy.deepcopy(nex_gen)
print(f'Part 2: {len(seen)}')

## visualization
# for i in range(80):
#     p = ""
#     for j in range(100):
#         if i ==39 and j == 31:
#             p += "X"
#         elif passable(i,j):
#             p += '.'
#         else:
#             p += '#'
#     print(p)
