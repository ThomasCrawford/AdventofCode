import re


data = []
with open("input_01.txt") as file:
    for line in file:
        data.append(int(line.strip()))

print(sum(data))

seen = set()
curr = 0
for i in range(1000000):
    if curr in seen:
        print(curr)
        quit()
    seen.add(curr)
    curr += data[i%len(data)]



