import re







presents = []
trees = []
with open("test.txt") as file:
    blocks = file.read().split("\n\n")
    for block in blocks[:-1]:
        presents.append([x.strip() for x in block.split("\n")[1:]])
    for line in blocks[-1].split("\n"):
        trees.append([int(x) for x in re.findall(r'\d+', line)])


space = [7,7,7,6,7,5]
space = [7]*6

frac = []
for x in trees[:-1]:
    area = x[0]*x[1]
    needed = sum([a*b for a,b in zip(space,x[2:])])
    frac.append(needed/area)

print(frac)
ans1 = len([x for x in frac if x <1])
print(ans1)







