


data = {}
with open("input_12.txt") as file:
    for line in file:
        x = line.strip().replace(",","").split()
        data[x[0]] = x[2:]

def get_group_containing(string):
    this_group = set()
    new = [string]
    while new:
        x = new.pop()
        this_group.add(x)
        for c in data[x]:
            if c not in this_group and c not in new:
                new.append(c)
    return this_group

print(f'Part 1: {len(get_group_containing("0"))}')

seen = set()

groups = []

for x in data.keys():
    if x not in seen:
        new_group = get_group_containing(x)
        groups.append(new_group)
        for y in new_group:
            seen.add(y)

print(f'Part 2: {len(groups)}')