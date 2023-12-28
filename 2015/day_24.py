from itertools import combinations
import numpy as np

data = []
with open("input_24.txt") as file:
    for line in file:
        data.append(int(line.strip()))

target = sum(data)/3

QE_scores = []
for i in range(1,7):
    for collection in combinations(data,i):
        # print(sum(collection))
        if sum(collection) == target:
            # print(i, collection, np.prod(collection))
            QE_scores.append(np.prod(collection))

print(min(QE_scores))



target = sum(data)/4

QE_scores = []
for i in range(1,5):
    for collection in combinations(data,i):
        # print(sum(collection))
        if sum(collection) == target:
            # print(i, collection, np.prod(collection))
            QE_scores.append(np.prod(collection))

print(min(QE_scores))