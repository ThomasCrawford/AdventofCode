import re
import heapq

def dist(bot1, bot2):
    return sum([abs(bot1[i] - bot2[i]) for i in range(3)])

def volume(box):
    out = 1
    for i in range(3):
        out *= abs(box[0][i] - box[1][i])+1
    return out

def box_corners(box):
    mins, maxs = box
    out = []
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                out.append([mins[0] if a else maxs[0], \
                            mins[1] if b else maxs[1], \
                            mins[2] if c else maxs[2]])
    return out

def oct_corners(bot):
    center = bot[:3]
    r = bot[3]
    out = []
    for i in range(3):
        new = list(center)
        new[i] += r
        out.append(list(new))
        new[i] -= 2*r
        out.append(new)
    return out

def overlap(box, bot): # box: [ [0,0,0],[1,2,3]]    # bot: [1,2,3,4]
    box_pts = box_corners(box)
    oct_pts = oct_corners(bot)
    for pt in box_pts:
        if dist(pt,bot) <= bot[3]:
            return True
    for pt in oct_pts:
        if all([box[0][i] <= pt[i] <= box[1][i] for i in range(3) ]):
            return True
    return False

def count_overlaps(box, data):
    return len([bot for bot in data if overlap(box, bot)])

def divide(box):
    mins, maxs = box
    mids = [(mins[i] + maxs[i]) // 2 for i in range(3)]
    out = []
    
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                new_mins = [
                    mins[0] if a == 0 else mids[0] + 1,
                    mins[1] if b == 0 else mids[1] + 1,
                    mins[2] if c == 0 else mids[2] + 1,
                ]
                new_maxs = [
                    mids[0] if a == 0 else maxs[0],
                    mids[1] if b == 0 else maxs[1],
                    mids[2] if c == 0 else maxs[2],
                ]
                out.append([new_mins, new_maxs])
                
    return out


data = []
with open("input_23.txt") as file:
    for line in file:
        data.append([int(x) for x in re.findall(r'(-?\d+)', line)])

data = sorted(data, key = lambda x: x[3])

largest = data[-1]
in_range = [bot for bot in data if dist(bot, largest) <= largest[3]]
ans1 = len(in_range)
print(ans1)


init_box = [[-1*10**10, -1*10**10, -1*10**10], [1*10**10, 1*10**10, 1*10**10]]

q = [] # max poss overlaps, volume, dist from origin, box
heapq.heappush(q,[-1*count_overlaps(init_box, data), volume(init_box), dist(init_box[0],[0,0,0]), init_box])

while True:
    this = heapq.heappop(q)
    if this[1] == 1:
        print(sum(this[3][0]))
        break
    for box in divide(this[3]):
        heapq.heappush(q,[-1*count_overlaps(box, data), volume(box), dist(box[0],[0,0,0]), box])

