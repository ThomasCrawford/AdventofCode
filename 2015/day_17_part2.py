from itertools import combinations

buckets = []
with open("input_17.txt") as file:
    for line in file:
        buckets.append(int(line.strip()))

bit_count = len(buckets)
start = 150

count = 0
size = 1

while not count:
    count = sum([sum(com)==start for com in combinations(buckets,size)])
    size += 1

print(count)
