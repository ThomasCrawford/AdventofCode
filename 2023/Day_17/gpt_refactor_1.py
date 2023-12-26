import heapq
import cmath

# Read and process data
raw_data = []
with open("input.txt") as file:
    for line in file:
        raw_data.append(line.strip())

width = len(raw_data[0])
height = len(raw_data)

data = {(k, i): int(raw_data[k][i]) for i in range(width) for k in range(height)}

# Using a priority queue

Q = [(0, (0, 0), True), (0, (0, 0), False)]
heapq.heapify(Q)
visited = set()

while Q:
    c, p, d = heapq.heappop(Q)
    print(f"{c} to get to {p,d}\t Q:{len(Q)}")
    if (p, d) in visited:
        continue
    visited.add((p, d))

    if p == (height - 1, width - 1):
        print(c)
        break

    # Add neighboring nodes to Q
    for which_way in [-1, 1]:
        new_c = c
        for i in range(1, 4):
            new_p = (p[0] + i * d * which_way, p[1] + i * (not d) * which_way)
            if not (0 <= new_p[0] < height and 0 <= new_p[1] < width):
                break
            new_c += data[new_p]
            heapq.heappush(Q, (new_c, new_p, not d))

# Output the result
print("No path found" if p != (height - 1, width - 1) else "")
