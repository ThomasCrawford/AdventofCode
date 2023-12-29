#275
#288 high
#150


data = []
with open("input_01.txt") as file:
    for line in file:
        data.append(line.strip().split(', '))

visited = set()
first_repeat_found = False
visited_twice = []
p = 0
d = -1*1j
for step in data[0]:
    if step[:1] == 'L':
        d = d * 1j
    elif step[:1] == 'R':
        d = -1*d*1j
    for _ in range(int(step[1:])):    
        p += d
        if p in visited:
            visited_twice.append(p)
        visited.add(p)

def dist (p):
    return int(abs(p.real) + abs(p.imag))

print(dist(p))

print(dist(visited_twice[0]))




