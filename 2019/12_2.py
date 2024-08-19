import re
import math

moon_set = [[],[],[]]
with open("input12.txt") as file:
    for line in file:
        a,b,c = re.findall(r'-?\d+',line)
        moon_set[0].append([int(a),0])
        moon_set[1].append([int(b),0])
        moon_set[2].append([int(c),0])

def step(moons):
    for moon in moons:
        for other in [other for other in moons if other[0] != moon[0]]:
            delta_p = other[0] - moon[0]
            delta_v = int(delta_p/abs(delta_p))
            moon[1] += delta_v
    for moon in moons:
        moon[0] += moon[1]
    return moons


def detect_loop(moons):
    seen = set()
    while tuple(map(tuple,moons)) not in seen:
        seen.add(tuple(map(tuple,moons)))
        moons = step(moons)
    return len(seen)


a,b,c = [detect_loop(moons) for moons in moon_set]
print(math.lcm(a,b,c))
