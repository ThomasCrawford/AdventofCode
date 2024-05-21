import copy

def index_max(l):
    return l.index(max(l))

def loop(l):
    m = max(l)
    i = l.index(m)
    l[i]=0
    for k in range(m):
        l[(i+k+1)%banks] += 1
    return l


with open("input_06.txt") as file:
    for line in file:
        state = [int(x) for x in line.strip().split()]

banks = len(state)

mem = set()

counter1 = 0
while tuple(state) not in mem:
    mem.add(tuple(state))
    state = loop(state)
    counter1 += 1

target = copy.deepcopy(state)
counter2 = 1
state = loop(state)
while state != target:
    counter2 +=1
    state = loop(state)


print(counter1, counter2)

