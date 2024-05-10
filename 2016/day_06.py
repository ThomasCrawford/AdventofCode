from collections import Counter


def most_frequent(lis):
    counts = {}
    for x in lis:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return max(counts, key=counts.get)

def least_frequent(lis):
    counts = {}
    for x in lis:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return min(counts, key=counts.get)

lis = [2, 1, 2, 2, 1, 3]
print(most_frequent(lis))

data = []
with open("input_06.txt") as file:
    for line in file:
        data.append(list(line.strip()))

tdata = [list(i) for i in zip(*data)]

ans1 = ""
for letter in tdata:
    ans1 += most_frequent(letter)

ans2 = ""
for letter in tdata:
    ans2 += least_frequent(letter)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')