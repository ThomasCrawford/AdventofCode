class Block:
	def __init__(self, string, i):
		a,b = string.strip().split("~")
		self.x_min, self.y_min, self.z_min = [int(i) for i in a.split(",")]
		self.x_max, self.y_max, self.z_max = [int(i) for i in b.split(",")]
		self.name = i
		# self.is_supported = False
		self.dist_to_fall = 999
		self.supported_by = []
		self.supports = []
		self.update_fall_dist()
		self.chain_reaction = set()

	def __lt__(self, other):
		return self.z_min < other.z_min

	def update_fall_dist(self):
		distance = self.dist_to_fall
		for x in range(self.x_min, self.x_max+1):
			for y in range(self.y_min, self.y_max+1):
				distance = min(self.z_min - base[(x,y)], distance)
		self.dist_to_fall = distance

	def fall_by(self, distance):
		self.z_min = self.z_min - distance
		self.z_max = self.z_max - distance

	def now_supported(self):
		# self.is_supported = True
		for block_index in settled_blocks:
			other_block = block_registry[block_index]
			if other_block.z_max == self.z_min -1:
				if self.overlap(other_block):
					other_block.supports.append(self)
					self.supported_by.append(other_block)

	def overlap(self, other_block):
		for x in range(self.x_min,self.x_max+1):
			for y in range(self.y_min,self.y_max+1):
				if (other_block.x_min <= x <= other_block.x_max) and \
						(other_block.y_min <= y <= other_block.y_max):
					return True
		return False

	def will_it_fall(self, other_block):
		for third_block in other_block.supported_by:
			if third_block not in self.chain_reaction and third_block != self:
				return False
		return True

	def update_chain(self):
		to_check = self.supports
		while to_check:
			other_block = to_check[0]
			to_check = to_check[1:]
			if self.will_it_fall(other_block):
				self.chain_reaction.add(other_block)
				to_check.extend(other_block.supports)


def update_base(block):
	for x in range(block.x_min,block.x_max+1):
		for y in range(block.y_min,block.y_max+1):
			base[(x,y)] = block.z_max

# Setup
block_registry = {}
base = {(x,y):0 for x in range(10) for y in range(10)}

with open("input.txt") as file:
	for i, line in enumerate(file):
		block = Block(line,i)
		block_registry[i] = block
unsettled_blocks = block_registry.keys
settled_blocks = []


# Blocks Fall
s = [x for x in block_registry.values()]
s.sort()

for block in s[:]:
	block.fall_by(block.dist_to_fall-1)
	settled_blocks.append(block.name)
	block.now_supported()
	update_base(block)
	s.remove(block)
	for other_block in s:
		other_block.update_fall_dist()

count = 0
for block in block_registry.values():
	block.update_chain()
	count += len(block.chain_reaction)
print(count)
