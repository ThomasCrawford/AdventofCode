from functools import lru_cache

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
		if (data[p+d] == "v" and d != 1j) or \
				(data[p+d] == ">" and d != 1) or \
				(data[p+d] == "^" and d != -1j) or \
				(data[p+d] == "<" and d != -1):
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


# brute force:
# f(p)= longest distance to end

@lru_cache(maxsize = 128)
def f(p):
	out = 0
	for choice in node_registry[p].connects_to:
		out = max(choice[1]+f(choice[0]), out)
	return out


print(f(1))

print(f.cache_info())


