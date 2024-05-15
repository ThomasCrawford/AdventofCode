import re, cmath, copy, itertools

directions = {1, -1, 1j, -1j}

data = {}
nodes = {}
with open("input_24.txt") as file:
    for i, line in enumerate(file):
        for x,v in enumerate(line.strip()):
            data[x+i*1j] = v 
        digits = re.finditer(r'(\d)', line.strip())
        for digit in digits:
            x = digit.group()
            l = digit.span()[0]
            nodes[digit.group()] = l+i*1j


def flood(data, node):
    distances = {}
    visited = set()
    visited.add(node)
    this_gen = set()
    this_gen.add(node)
    gen = 0
    while this_gen:
        gen += 1
        nex_gen = set()
        for p in this_gen:
            for d in directions:
                new = p+d
                if new in visited or data[new] == '#':
                    continue
                nex_gen.add(new)
                visited.add(new)
                if data[new] != '.':
                    distances[data[new]] = gen
        this_gen = copy.deepcopy(nex_gen)
    return distances

def total_distance(distances, order):
    position = "0"
    distance = 0
    for node in order:
        distance += distances[position][node]
        position = node 
    return distance 


#Use floodfill to find distances connecting any two nodes
distance_between_nodes = {}
for node_name in nodes:
    distance_between_nodes[node_name] = flood(data, nodes[node_name])

#Solve traveling salesman

node_names = [x for x in nodes]
node_names.remove("0")
orders = [list(order) for order in itertools.permutations(node_names)]
ans = min([total_distance(distance_between_nodes,order) for order in orders])
print(f'Part 1: {ans}')

orders = [list(order) + ["0"] for order in itertools.permutations(node_names)]
ans = min([total_distance(distance_between_nodes,order) for order in orders])
print(f'Part 1: {ans}')


