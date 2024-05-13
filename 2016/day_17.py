import hashlib
import copy

seed = 'vwbaicqe'



def location(string):
    loc = [0,0] 
    for x in string:
        if x == "U":
            loc[1] -= 1
        elif x == "D":
            loc[1] += 1
        elif x == "R":
            loc[0] += 1
        elif x == "L":
            loc[0] -= 1
    return loc

def new_route_options(route):
    string = seed + route
    dfour = hashlib.md5(string.encode()).hexdigest()[:4]
    loc = location(seed + route)
    poss_nex_steps = []
    if dfour[0] in "bcdef" and loc[1]>0:
        poss_nex_steps.append("U")
    if dfour[1] in "bcdef" and loc[1]<3:
        poss_nex_steps.append("D")
    if dfour[2] in "bcdef" and loc[0]>0:
        poss_nex_steps.append("L")
    if dfour[3] in "bcdef" and loc[0]<3:
        poss_nex_steps.append("R")
    return [route + step for step in poss_nex_steps]

def main1():
    this_gen = [""]
    while True:
        nex_gen = []
        for route in this_gen:
            if location(route) == [3,3]:
                return route
            nex_gen += new_route_options(route)
        this_gen = copy.deepcopy(nex_gen)

print(f'Part 1: {main1()}')


def main2():
    lengths = []
    this_gen = [""]
    while this_gen:
        nex_gen = []
        for route in this_gen:
            if location(route) == [3,3]:
                lengths.append(len(route))
            else:
                nex_gen += new_route_options(route)
        this_gen = copy.deepcopy(nex_gen)
    return max(lengths)


print(f'Part 2: {main2()}')
