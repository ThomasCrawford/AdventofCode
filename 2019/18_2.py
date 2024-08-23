#Assumption about maze: unlocking a door can reveal new keys, but cannot shorten existing routes to keys
# Therefore the distance dictionary can be pre-calculated

#Approx 60 seconds to run

import heapq
import cmath
import time
start_time = time.time()


directions = {1,-1,1j,-1j}


def find_dist(data,p):
    seen = set()
    q = [[p,0,[]]] #[position, distance from start, dependencies]
    dist = {}
    while q:
        p,s,depend = q.pop(0)
        seen.add(p)
        for d in directions:
            if p+d not in seen and data[p+d] != "#":
                if data[p+d] == "." or data[p+d][0] == "@":
                    q.append([p+d,s+1,depend])
                elif data[p+d].islower(): 
                    dist[data[p+d]] = [s+1,depend]
                    q.append([p+d,s+1,depend])
                elif data[p+d].isupper():
                    q.append([p+d, s+1, depend + [data[p+d]]])
    return dist


data = {}
with open("input18.txt") as file:
    for y, line in enumerate(file):
        for x, v in enumerate(line.strip()):
            data[x+y*1j] = v

#change center of maze for part 2
for z in data:
    if data[z] == "@":
        center = z
for d in [0,1,1j,-1,-1j]:
    data[center + d] = "#"
data[center + 1+1j] = "@1"
data[center + 1-1j] = "@2"
data[center + -1+1j] = "@3"
data[center + -1-1j] = "@4"

locations = {}
for x in data:
    if data[x].islower():
        locations[data[x]] = x

distances = {}
for p in data:
    if data[p].islower() or data[p][0] == "@":
        distances[data[p]] = find_dist(data,p)

for x in distances:
    print(x, distances[x].keys())


def bfs_shortest_path():
    # Priority queue stores (steps_taken, key_name (purely so heap is well ordered), current_position, keys_collected)
    start = ("@1","@2","@3","@4")
    q = [(0, "", start, frozenset())]
    seen = {}

    while q:
        steps, _, positions, keys = heapq.heappop(q)
        print(steps, len(q))
        if (positions, keys) in seen and seen[(positions, keys)] <= steps:
            continue
        seen[(positions, keys)] = steps
        
        if len(keys) == len(locations):
            return steps
 
        for bot_num, x in enumerate(positions): 
            for next_key in distances[x]: # add all possible next steps to q
                dist, prereq = distances[x][next_key]
                if next_key.upper() not in keys and all(door in keys for door in prereq):
                    new_keys = keys | frozenset(next_key.upper())
                    new_positions = list(positions)
                    new_positions[bot_num] = next_key
                    to_be_queued = (steps + dist, next_key, tuple(new_positions), new_keys)
                    heapq.heappush(q, to_be_queued)


print(bfs_shortest_path())


print("--- %s seconds ---" % (time.time() - start_time))

