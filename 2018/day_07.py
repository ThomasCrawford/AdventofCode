#1001 too high
#260 too low


import re
from collections import defaultdict

regex = r"Step (\w) must be finished before step (\w) can begin."

def letter_to_number(letter):
    number = ord(letter) - ord('A') + 1
    return number

def get_avail(seen):
    avail = [x for x in mentioned if x not in seen and all([y in seen for y in tree[x]])]
    return sorted(avail)

tree = defaultdict(set)
mentioned = set()
with open("input_07.txt") as file:
    for line in file:
        b,a = re.match(regex,line).groups()
        mentioned.add(a)
        mentioned.add(b)
        tree[a].add(b)

#Part 1
ans1 = ""
avail = get_avail(ans1)
while avail:
    p = avail.pop(0)
    ans1 += p
    avail = get_avail(ans1)
print(ans1)


#Part 2
todo = {x: letter_to_number(x) + 60 for x in mentioned}
clock = 0
complete = set()
active = {}

while len(complete) < len(mentioned):
    avail = get_avail(complete)
    for task in avail:
        if task not in active and len(active) < 5:
            active[task] = todo[task]

    step = min(active.values())
    clock += step
    for task in list(active):
        active[task] -= step
        if active[task] == 0:
            complete.add(task)
            del active[task]

print(clock)


