import re

width = 1000

def check_region(region, quilt):
    for x in range(region[0], region[0] + region[2]):
        for y in range(region[1],region[1]+ region[3]):
            if quilt[tuple([x,y])] != 1:
                return False
    return region[4]

data = []
with open("input_03.txt") as file:
    for line in file:
        id_number, _, pair, area = line.strip().split()
        offset =  [int(x) for x in pair.strip(":").split(",")]
        areas = [int(x) for x in area.split('x')]
        data.append(offset + areas + [id_number])

quilt = {}
for x in range(width):
    for y in range(width):
        quilt[tuple([x,y])] = 0

for region in data:
    for x in range(region[0], region[0] + region[2]):
        for y in range(region[1],region[1]+ region[3]):
            quilt[tuple([x,y])] += 1

ans1 = sum([1 for square in quilt if quilt[square]>1])
print(ans1)


for region in data:
    if check_region(region, quilt):
        print(region[4])
