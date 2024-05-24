import re
import math
from itertools import permutations, combinations

regex = r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>'


def quad(a,b,c):
    if a == 0 and b == 0 and c == 0:
        return ["all"]
    if a == 0 and b == 0:
        return []
    elif a == 0:
        return [float(-1*c/b)]
    dis = float(b*b - 4*a*c)
    if dis < 0:
        return []
    else:
        vals = [(-1*b + math.sqrt(dis))/(2*a), (-1*b - math.sqrt(dis))/(2*a)]
        return [float(x) for x in vals if x >=0]

def intersect_time(zero,one):
    p0,v0,a0 = zero
    p1,v1,a1 = one
    a = a0/2 - a1/2
    b = v0 - v1 + a0/2 - a1/2
    c = p0 - p1
    q = quad(a,b,c)
    return q

def det_col (a, b):
    timings = []
    for dim in range(3):
        zero = [a[0][dim], a[1][dim], a[2][dim]]
        one = [b[0][dim], b[1][dim], b[2][dim]]
        timings.append(intersect_time(zero,one))
    if len(timings) != 3:
        return False
    for i in range(3):
        if "all" in timings[i]:
            timings[i] += timings[(i+1)%3]
            timings[i] += timings[(i+2)%3]
    for t in timings[0]:
        if t in timings[1] and t in timings[2]:
            return t
    return False

def get_location(line,t):
    pos = []
    for i in range(3):
        pos.append(line[0][i] + line[1][i]*t + line[2][i]*t*(t+1)/2)
    return pos

acc = {}
data = {}
with open("input_20.txt") as file:
    for i, line in enumerate(file):
        px, py, pz, vx, vy, vz, ax, ay, az = re.match(regex, line).groups()
        acc[i] = abs(int(ax))+abs(int(ay))+abs(int(az))
        s = [float(x) for x in re.match(regex, line).groups()]
        data[i] = [s[i*3:i*3+3] for i in range(3)]

ans1 = min(acc, key = acc.get)
print(ans1)


for i,j in combinations(data,2):
    col = det_col(data[i],data[j])
    if col:
        if i in acc:
            acc.pop(i)
        if j in acc:
            acc.pop(j)
print(len(acc))




