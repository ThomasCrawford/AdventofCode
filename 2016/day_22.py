#1049 too high
#0

import re, hashlib, collections, copy, itertools

regex = r'-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T'

width = 30
height = 35

data = []
with open("input_22.txt") as file:
    for line in file:
        try:
            x,y,size,used,avil = re.search(regex, line.strip()).groups()
            data.append([int(x),int(y),int(size),int(used),int(avil)])
        except:
            pass

data2 = [line[3:] for line in data]
data2.sort()

count = 0
for x in data:
    for y in data:
        if x[3] < y[4] and x != y and x[3]>0:
            count += 1
print(count)


for line in data:
    if line[2]>100:
        print(line[0],line[1])


dic = {}

for line in data:
    dic[tuple([line[0],line[1]])] = line[3]

for j in range(height):
    # print(j)
    out = ""
    for i in range(width):
        if dic[(i,j)] >100:
            out += "#"
        elif dic[(i,j)] == 0:
            out += "0"
        else:
            out += "."
    print(out)


#Part 2:

# 0 is at 4,24
# 5 moves to do: 
#              ..._G
#              .._G.

ans = 4+24+width-1 + 5*28 + 1
print(f'Part 2:{ans}')