import functools

splitters = []
with open ("7.txt") as file:
    for i, line in enumerate(file):
        for k, v in enumerate(line.strip()):
            if v== "S":
                start = k
            elif v == "^":
                splitters.append((i,k))

beams = set([start])
ans1 = 0
for splitter in splitters:
    if splitter[1] in beams:
        beams.remove(splitter[1])
        beams.add(splitter[1]-1)
        beams.add(splitter[1]+1)
        ans1 += 1
print(ans1)

#Part 2
end = max([s[0] for s in splitters])

def fall(row,col):
    while row <= end:
        if (row,col) in splitters:
            return (row,col)
        row += 1
    return False

@functools.lru_cache(maxsize=None)
def f(row,col):
    fell = fall(row,col)
    if not fell:
        return 1
    else:
        return f(fell[0], fell[1]-1) + f(fell[0], fell[1]+1)
ans2 = f(0,start)
print(ans2)










