

def get_count(data, counts, obj):
    if obj in counts:
        return counts
    orb = data[obj]
    if orb not in counts:
        counts = get_count(data, counts, orb)
    counts[obj] = counts[orb] + 1
    return counts



data = {}
counts = {}
counts["COM"] = 0

with open("input6.txt") as file:
    for line in file:
        # print(line)
        a,b = line.strip().split(')')
        data[b] = a

for obj in data:
    counts = get_count(data, counts, obj)

ans1 = sum(counts.values())
print(ans1)



#Part 2

data2 = {}
for a in data:
    if data[a] in data2:
        data2[data[a]].append(a)
    else:
        data2[data[a]] = [a]

adjacencies = {}
for x in data:
    adjacencies[x] = [data[x]]
    if x in data2:
        adjacencies[x] += data2[x]

dist = {}
dist["YOU"] = 0

q = ["YOU"]
while "SAN" not in dist:
    a = q.pop()
    for b in adjacencies[a]:
        if b not in dist:
            dist[b] = dist[a] + 1
            q.append(b)


ans2 = dist["SAN"] - 2
print(ans2)




