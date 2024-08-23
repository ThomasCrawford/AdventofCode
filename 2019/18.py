#Assumption about maze: unlocking a door can reveal new keys, but cannot shorten existing routes to keys
# Therefore the distance dictionary can be pre-calculated


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
                if data[p+d] == "." or data[p+d] == "@":
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

locations = {}
for x in data:
    if data[x].islower() or data[x] == "@":
        locations[data[x]] = x

distances = {}
for p in data:
    if data[p].islower() or data[p] == "@":
        distances[data[p]] = find_dist(data,p)



def bfs_shortest_path():
    # Priority queue stores (steps_taken, current_position, keys_collected)
    q = [(0, "@", start, frozenset())]
    seen = {}

    while q:
        steps, _, p, keys = heapq.heappop(q)
        v = data[p]
        if (p, keys) in seen and seen[(p, keys)] <= steps:
            continue
        seen[(p, keys)] = steps
        
        if len(keys) == len(locations) - 1:
            return steps
        
        for next_key in distances[v]: # add all possible next steps to q
            dist, prereq = distances[v][next_key]
            if next_key.upper() not in keys and all(door in keys for door in prereq):
                new_keys = keys | frozenset(next_key.upper())
                to_be_queued = (steps + dist, next_key, locations[next_key], new_keys)
                heapq.heappush(q, to_be_queued)
    print("Solution not found")
    return 0





start = locations["@"]
print(bfs_shortest_path())


print("--- %s seconds ---" % (time.time() - start_time))
