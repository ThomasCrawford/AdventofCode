import re, hashlib, collections, copy, itertools


data = [[],[]]
with open("test.txt") as file:
    for line in file:
        x,y = line.strip().split()
        data[0].append(int(x))
        data[1].append(int(y))

data[0].sort()
data[1].sort()

ans1 = 0
for i,x in enumerate(data[0]):
    ans1 += abs(x-data[1][i])
print(ans1)

ans2 = 0

for x in data[0]:
    ans2 += x*data[1].count(x)
print(ans2)

