
def nex_gen(state):
    new_state = {}
    for i in range(min(state.keys())-2, max(state.keys())+3):
        p = ""
        for s in range(-2,3):
            p += state.get(i+s,".")
        new_state[i] = rules[p]
    return new_state

rules = {}
with open("input_12.txt") as file:
    init_state = file.readline().strip().split()[2]
    file.readline()
    for line in file:
        x, y = line.strip().split(" => ")
        rules[x] = y

state = {}
for i, x in enumerate(init_state):
    state[i] = x

# Part 1
for i in range(20):
    state = nex_gen(state)
ans1 = sum([x for x in state if state[x] == "#"])
print(ans1)


# Part 2
a = 0
b = 0

for i in range(100):
    state = nex_gen(state)
    a = b
    b = sum([x for x in state if state[x] == "#"])
ans2 = sum([x for x in state if state[x] == "#"]) + (b-a)*(50000000000 - 100)
print(ans2)
