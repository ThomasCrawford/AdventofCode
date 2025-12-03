import cmath
import heapq

data = {}
with open("test.txt") as file:
    for k, line in enumerate(file):
        for i, v in enumerate(line.strip()):
            data[i+k*1j] = int(v)

infty = 2**31

start = 0
end = max([key.real for key in data.keys()]) + 1j*max([key.imag for key in data.keys()])
directions = [1,1j,-1,-1j]
q = [(0,start)]
seen = {}
seen[0] = 0
visited = {}


while end not in visited:
    z = min(seen, key=seen.get)
    v = seen[z]
    del seen[z]
    visited[z]=v
    for d in directions:
        if z+d in data and z+d and z+d not in visited:
            new_v = min(seen.get(z+d,infty), v+data[z+d])
            seen[z+d] = new_v
print(visited[end])