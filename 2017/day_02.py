#Time: 2:01 for 1, 4:15 for 2

import re, hashlib, collections, copy, itertools


data = []
with open("input_02.txt") as file:
    for line in file:
        data.append(line.strip().split())

count = 0
for line in data:
    line = [int(x) for x in line]
    for x in line:
        for y in line:
            if x%y == 0 and x != y:
                count += x//y
    

print(count)