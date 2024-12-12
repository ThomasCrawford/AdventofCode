from collections import defaultdict
import cmath


neighbors = [1,1j,-1,-1j, 1+1j, 1-1j, -1+1j, -1-1j]

data = defaultdict(list)
with open("04.txt") as file:
    for i,line in enumerate(file):
        for k,x in enumerate(line.strip()):
            data[i*1j+k] = x

ans1 = 0
for z in list(data.keys()):
    if data[z] == "X":
        for d in neighbors:
            if data[z+d] == "M" and data[z+2*d]== "A" and data[z+3*d] == "S":
                ans1 += 1
print(ans1)

ans2 = 0
for z in list(data.keys()):
    if data[z] == "A":
        for r in [1,1j,-1,-1j]:
            if data[z+r*(-1-1j)] == "M" and \
                data[z+r*(1-1j)]== "M" and \
                data[z+r*(-1+1j)] == "S"and \
                data[z+r*(1+1j)] == "S":
                ans2 += 1
print(ans2)
