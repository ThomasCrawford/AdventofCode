import networkx as nx
import matplotlib.pyplot as plt


data = {}
nodes = set()
with open("input.txt") as file:
	for line in file:
		a, b = line.strip().split(':')
		b = b.strip()
		b = b.split(' ')
		data[a] = set(b)
		nodes.add(a)
		for c in b:
			nodes.add(c)


G = nx.Graph()
for name in nodes:
	G.add_node(name)

for name in data:
	for other in data[name]:
		G.add_edge(name, other)

for node in nodes:
	if node not in data:
		data[node] = set()


#make bidirectional
for name in data:
	for other in data[name]:
		data[other].add(name)

total = len(data)
group = set()
Q = ['bxf']

while Q:
	new = Q.pop()
	group.add(new)
	Q.extend([x for x in data[new] if x not in group])

print(f'Total: {total}')
print(f'Group 1: {len(group)}')
print(f'Answer: {len(group)*(total-len(group))}')

# # Graphing the grap

# pos = nx.spring_layout(G)  
# nx.draw(G, pos, with_labels = True)
# # edge_labels = nx.get_edge_attributes(G, 'color')
# # nx.draw_networkx_edge_labels(G, pos)

# plt.show()