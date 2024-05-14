


data = []
with open("input_20.txt") as file:
    for line in file:
        a,b = line.strip().split('-')
        data.append([int(a),int(b)])

data.sort()

def search(data):
    m = data[0][1] 
    for line in data:
        if line[0] > m +1:
            return m + 1
        m = max(m, line[1])

print(f'Part 1: {search(data)}')


def is_interior(n):
    for line in data:
        if line[0] < n < line[1]:
            return True
    return False

starts = []
stops = []

for line in data:
    if not is_interior(line[0]):
        starts.append(line[0])
    if not is_interior(line[1]):
        stops.append(line[1])

r=zip(stops[:-1], starts[1:])
ans = sum([x[1]-x[0]-1 for x in r])
print(f'Part 2: {ans}')
