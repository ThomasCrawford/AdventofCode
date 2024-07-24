import cmath
import heapq
import random

depth = 9465
target = (13,704)

levels = {}
levels[(0,0)] = 0

def get_level(x, y, levels):
    if x == 0:
        out = y * 48271
    elif y == 0:
        out = x * 16807
    elif (x,y) == target:
        out = 0
    else:
        out = levels[(x-1, y)] * levels[(x,y-1)]
    return (out + depth)%20183

def other_tool(score, tool):
    match score:
        case 0:
            return 2 if tool == 1 else 1
        case 1:
            return 0 if tool == 1 else 1
        case 2:
            return 2 if tool == 0 else 0


for s in range(1,3*(target[0]+target[1])):
    for x in range(s+1):
        y = s-x
        levels[(x,y)] = get_level(x,y,levels)

score = {}
for p in levels:
    score[p[0]+p[1]*1j] = (levels[p])%3

## Visualize
# for y in range(12):
#     out = ""
#     for x in range(12):
#         v = score[(x+y*1j)]
#         if v == 0:
#             out += "."
#         if v == 1:
#             out += "="
#         if v == 2:
#             out += "|"
#     print(out)


ans1 = sum([score[x+y*1j] for x in range(target[0]+1) for y in range(target[1]+1)])
print(ans1)

target = target[0] + target[1]*1j
time = {} # z, tool state: time
q = [] # time, random, z, tool state
heapq.heappush(q, (0, 0, 0, 2))
directions = [1,-1,1j,-1j]


while (target,2) not in time:
    t, _, p, s = heapq.heappop(q) # position, state, time
    if (p,s) in time and time[(p,s)] <= t:
        continue
    time[(p,s)] = t
    for d in directions:
        newp = p+d
        if newp in score and (s+score[newp])%3 and (newp,s) not in time:
            heapq.heappush(q, (t+1,random.random(), newp, s))
    news = other_tool(score[p], s)
    heapq.heappush(q, (t+7, random.random(), p, news))

ans2 = time.get((target,2))
print(ans2)



