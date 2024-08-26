from collections import defaultdict

def def_value():
    return 0


width = 5

nbrs= {}
for i in range(width**2):
    nbrs[i] = []
    if i >= 5:
        nbrs[i].append(i-5)
    if i < 20:
        nbrs[i].append(i+5)
    if i % 5 != 0:
        nbrs[i].append(i-1)
    if i % 5 != 4:
        nbrs[i].append(i+1)


def step(state):
    new_state = 0
    for i in range(width**2):
        count = len([x for x in nbrs[i] if state & 2**x])
        if state & 2**i and count == 1:
            new_state += 2**i
        elif not state & 2**i and count in [1,2]:
            new_state += 2**i
    return new_state

def disp(state):
    for i in range(width):
        out = ""
        for j  in range(width):
            out += "#" if state & 2**(5*i+j) else "."
        print(out)
    print()



state = 0
with open("input24.txt") as file:
    for i, line in enumerate(file):
        for j, v in enumerate(line.strip()):
            if v == "#":
                state += 2**(j+width*i)

seen = set()
while state not in seen:
    seen.add(state)
    state = step(state)

print(state)



# Part 2

nbrs= {}
for i in range(width**2):
    nbrs[i] = []
    if i >= 5:
        nbrs[i].append([i-5,0])
    else:
        nbrs[i].append([7,-1])

    if i < 20:
        nbrs[i].append([i+5,0])
    else:
        nbrs[i].append([17,-1])

    if i % 5 != 0:
        nbrs[i].append([i-1,0])
    else:
        nbrs[i].append([11,-1])

    if i % 5 != 4:
        nbrs[i].append([i+1,0])
    else:
        nbrs[i].append([13,-1])

nbrs[7] = [[2,0],[6,0],[8,0],[0,1],[1,1],[2,1],[3,1],[4,1]]
nbrs[17] = [[16,0],[18,0],[22,0],[20,1],[21,1],[22,1],[23,1],[24,1]]
nbrs[11] = [[6,0],[16,0],[10,0],[0,1],[5,1],[10,1],[15,1],[20,1]]
nbrs[13] = [[8,0],[14,0],[18,0],[4,1],[9,1],[14,1],[19,1],[24,1]]
nbrs[12] = []



state = 0
with open("input24.txt") as file:
    for i, line in enumerate(file):
        for j, v in enumerate(line.strip()):
            if v == "#":
                state += 2**(j+width*i)

states = defaultdict(def_value)
states[0] = state


def count(states, level, i):
    count = 0
    for other in nbrs[i]:
        if states[other[1]+level] & 2**other[0]:
            count += 1
    return count


def step(states):
    relevant_levels = [i for i in states.keys() if states[i] >0]
    lower_bound = min(relevant_levels)-1
    upper_bound = max(relevant_levels)+2
    new_states = defaultdict(def_value)
    for level in range(lower_bound, upper_bound):
        state = states[level]
        new_state = 0
        for i in range(width**2):
            count1 = count(states, level, i)
            if state & 2**i and count1 == 1:
                new_state += 2**i
            elif not state & 2**i and count1 in [1,2]:
                new_state += 2**i
        new_states[level] = new_state
    return new_states

for _ in range(200):
    states = step(states)

# for i in states:
#     print(i)
#     disp(states[i])


ans2 = 0
for level in states:
    for i in range(25):
        if states[level]& 2**i:
            ans2 += 1
print(ans2)