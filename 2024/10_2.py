import cmath
from collections import defaultdict


data = defaultdict(lambda:-1)
with open("10.txt") as file:
    for i, line in enumerate(file):
        for k, x in enumerate(line.strip()):
            if x != ".":
                data[k+i*1j] = int(x)

scores = {}
directions = [1,1j,-1,-1j]


for p in data:
    if data[p]==9:
        scores[p] = 1
for n in range(9)[::-1]:
    for p in dict(data):
        if data[p] == n:
            score = 0
            for d in directions:
                if data[p+d] == n+1:
                    score += scores[p+d]
            scores[p] = score

ans1 = sum([scores[p] for p in data if data[p] == 0])

# for x in scores:
#     print(x,scores[x])
print(ans1)



