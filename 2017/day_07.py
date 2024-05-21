import copy

data = {}
with open("input_07.txt") as file:
# with open("test.txt") as file:
    for line in file:
        line = line.strip().replace(',','').replace('(','').replace(')','').split()
        if len(line)>2:
            data[line[0]] = [line[3:],int(line[1])]
        else:
            data[line[0]] = [[],int(line[1])]


candidates = list(data.keys())

for children in data.values():
    for x in children[0]:
        if x in candidates:
            candidates.remove(x)

for i in candidates:
    print(f'Part 1: {i}')


def get_weight(name):
    return data[name][1] + sum([get_weight(x) for x in data[name][0]])

mismatched = []
for name in data.keys():
    child_weights = [get_weight(x) for x in data[name][0]]
    if 1 < len(set(child_weights)):
        mismatched.append([min(child_weights),name])

problem = mismatched[0][1]

l = [get_weight(x) for x in data[problem][0]]
v = min(set(l), key = l.count)
delta = max(set(l), key = l.count) - v

for name in data[problem][0]:
    if get_weight(name) == v:
        print(f'Part 2: {data[name][1] + delta}')