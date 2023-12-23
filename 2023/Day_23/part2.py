import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import time

start_time = time.time()

directions = [1,1j,-1,-1j]

class Node:

	def __init__(self,p):
		self.p = p
		# self.poss_out = []
		# self.poss_in = []
		self.connects_to = []
		self.passable_neighbor_tiles = []
		self.find_passable_neighbor_tiles()

	def find_passable_neighbor_tiles(self):
		for d in [1,1j,-1,-1j]:
			if self.p+d in data:
				if is_passable(self.p+d):
					self.passable_neighbor_tiles.append(self.p+d)

	def update_connections(self):
		for neighbor_tile in self.passable_neighbor_tiles:
			next_node = traverse(self.p, neighbor_tile - self.p)
			if next_node:
				self.connects_to.append(next_node)

def traverse(p,d):
	steps = 1
	while p+d not in node_registry:
		# print(f'Leaving {p} for {p+d}, then can move either {which_adjacent(p+d)}')
		if len(which_adjacent(p+d)) != 2:
			return False
		# if (data[p+d] == "v" and d != 1j) or \
		# 		(data[p+d] == ">" and d != 1) or \
		# 		(data[p+d] == "^" and d != -1j) or \
		# 		(data[p+d] == "<" and d != -1):
		# 	return False
		steps +=1
		new_d = which_adjacent(p+d)
		new_d.remove(-1*d)
		p = p + d
		d = new_d[0]
	return [p + d, steps]

def is_passable(p):
	if data[p] in [".",">","<","v","<"]: return True

def which_adjacent(p):
	count = []
	for d in directions:
		if p+d in data:
			if is_passable(p+d):
				count.append(d)
	return count
	

# parse
data = {}
with open("input.txt") as file:
	for y, line in enumerate(file):
		width = y+1
		for x, value in enumerate(line.strip()):
			data[x + y*1j] = value

#Find nodes
node_registry = {}
for p in data:
	if is_passable(p):
		if len(which_adjacent(p)) > 2:
			node = Node(p)
			node_registry[p] = node

#add start and end nodes
node_registry[width-2+ (width-1)*1j] = Node(width-2+ (width-1)*1j)
node_registry[1] = Node(1)

for node in node_registry.values():
	node.update_connections()
	# print(node.p, node.connects_to)

# slight pruning at end (if you get to pennultimate, you should only move to end)
end_node = node_registry[width-2+ (width-1)*1j]
penultimate_index = end_node.connects_to[0][0]
penultimate = node_registry[penultimate_index]
penultimate.connects_to = [conn for conn in penultimate.connects_to if conn[0]==width-2+ (width-1)*1j]



#brute force DFS
def f(p, visited, dis_so_far):
	# if all([new_node in visited for new_node in node_registry[p].connects_to]):
	# 	return 0
	max_route_from_here = 0
	for next_node in node_registry[p].connects_to:
		if next_node[0] not in visited:
			max_route_from_here = max(max_route_from_here,\
				f(next_node[0], visited + [p], dis_so_far + next_node[1]) + next_node[1] )
	return max_route_from_here

print(f(1,[],0))




end_time = time.time()  # End timing
total_time = end_time - start_time
print(f"Program executed in {total_time} seconds.")



# # listing connections
# for node in node_registry.values():
# 	print(f'Node {node.p} has connections: {node.connects_to}')



# # Graphing the graph

# G = nx.Graph()
# for key in node_registry.keys():
# 	G.add_node(key)

# for key, node in node_registry.items():
# 	for adj in node.connects_to:
# 		G.add_edge(key, adj[0], weight = 600 - adj[1], color = adj[1])

# pos = nx.spring_layout(G)  
# nx.draw(G, pos, with_labels = True)
# edge_labels = nx.get_edge_attributes(G, 'color')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# plt.show()

# # matplotlib.pyplot.savefig("out.png")






