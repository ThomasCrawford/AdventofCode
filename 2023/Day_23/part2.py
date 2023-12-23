import networkx as nx
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


#Reformatting graph, now just adj_list
adj_list = {}
translate = {}
for i, node_index in enumerate(node_registry.keys()):
	translate[node_index] = i 

for node_index, i in translate.items():
	node_info = node_registry[node_index].connects_to
	adj_list[i] = [ [translate[adj_info[0]],adj_info[1]] for adj_info in node_info]


# Main Loop
def f(index, visited):
	max_route_from_here = 0
	for next_node in adj_list[index]:
		if next_node[0] not in visited:
			new_visited = visited.copy()  # Create a copy of visited set for the recursive call
			new_visited.add(index)
			max_route_from_here = max(max_route_from_here,\
				f(next_node[0], new_visited) + next_node[1] )
	return max_route_from_here

print(f(translate[1],set()))


end_time = time.time()  # End timing
total_time = end_time - start_time
print(f"Program executed in {total_time} seconds.")


# # Graphing the graph

# G = nx.Graph()
# for key in adj_list.keys():
# 	G.add_node(key)

# for key, adjacency in adj_list.items():
# 	for adj in adjacency:
# 		G.add_edge(key, adj[0], weight = 600 - adj[1], color = adj[1])

# pos = nx.spring_layout(G)  
# nx.draw(G, pos, with_labels = True)
# edge_labels = nx.get_edge_attributes(G, 'color')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# plt.show()

# # plt.savefig("out.png")

