from intcode13 import Intcode
from collections import defaultdict
import cmath


def def_value():
    return 0

def sequence(codes):
    out = 1
    bot = Intcode(data[:],[])
    for code in codes:
        bot.input(code)
        out = bot.run()[0]
    return out

def location(codes):
    p = 0
    for d in codes:
        if d == 1:
            p += -1j
        elif d== 2:
            p += 1j
        elif d == 3:
            p += 1
        elif d == 4:
            p += -1
    return p


with open("input15.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

def disp(walls):
    xs = [p.real for p in walls]
    ys = [p.imag for p in walls]
    for y in range(int(min(ys)),int(max(ys)+1)):
        out = ""
        for x in range(int(min(xs)),int(max(xs)+1)):
            if x == 0 and y == 0:
                out += "S"
            elif x+y*1j in walls:
                out += "#" 
            elif x+y*1j in known:
                out += "+"
            else:
                out += "."
        print(out)

walls = set()
known = {}
q = [[]] # route

direction_codes = {1,2,3,4}
longest = 0

while q:
    route = q.pop(0)
    p = location(route)
    if p in walls or p in known:
        continue
    value = sequence(route)
    # print(f'Route: {route}, P:{p}, Value:{value}')
    if value == 0:
        # print(f'{p} is a wall')
        walls.add(p)
    elif value == 1:
        known[p] = route
        longest = max([longest, len(route)])
        for d in direction_codes:
            q.append(route + [d])
    elif value == 2:
        ans1 = len(route)
        print(f'Part 1: {ans1}')
        oxygen = p
    # if walls:
    #     disp(walls)
    #     print()

#Part 2
directions = {1,-1,1j,-1j}

q = [[oxygen, 0]]
seen = set()
record = 0

while q:
    this = q.pop(0)
    p = this[0]
    seen.add(this[0])
    record = max([record, this[1]])
    for d in directions:
        if p+d not in seen and p+d not in walls:
            q.append([p+d, this[1]+1])
print(f'Part 2: {record}')


