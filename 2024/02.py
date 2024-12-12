import re, hashlib, collections, copy, itertools

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

data = []
with open("02.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip().split()])



def ismonotonic(line):
    if all([line[i+1] > line[i] for i in range(len(line)-1)]):
        return True
    elif all([line[i+1] < line[i] for i in range(len(line)-1)]):
        return True
    else:
        return False

def is_safe(line):
    if not ismonotonic(line):
        return False
    for i in range(len(line)-1):
        diff = abs(line[i+1] - line[i])
        if diff > 3:
            return False
        if diff <1:
            return False
    return True

def is_alt_safe(line):
    for i,_ in enumerate(line):
        test = line[:i]+line[i+1:]
        if is_safe(test):
            return True
    else:
        return False

ans1 = sum([is_safe(l) for l in data])
print(ans1)

ans2 = sum([is_alt_safe(l) for l in data])
print(ans2)

