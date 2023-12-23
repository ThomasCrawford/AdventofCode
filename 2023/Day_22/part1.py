class Block:
	def __init__(self, string, i):
		a,b = string.strip().split("~")
		self.x_min, self.y_min, self.z_min = [int(i) for i in a.split(",")]
		self.x_max, self.y_max, self.z_max = [int(i) for i in b.split(",")]
		self.name = i
		self.dist_to_fall = 999
		self.supported_by = []
		self.supports = []
		self.update_fall_dist()


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

	def is_removable(self):
		for other_block in self.supports:
			if len(other_block.supported_by) == 1:
				return False
		return True



	# def how_many_others(self):
	# 	if self.chain_count >=0:
	# 		return self.chain_count
	# 	count = 0
	# 	for other_block in self.supports:
	# 		if 
	# 		count += other_block.how_many_others()
	# 	self.chain_count = count
	# 	return count

def update_base(block):
	for x in range(block.x_min,block.x_max+1):
		for y in range(block.y_min,block.y_max+1):
			base[(x,y)] = block.z_max

# Setup
block_registry = {}
base = {(x,y):0 for x in range(10) for y in range(10)}

with open("test.txt") as file:
	for i, line in enumerate(file):
		block = Block(line,i)
		block_registry[i] = block
unsettled_blocks = block_registry.keys
settled_blocks = []


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


part1 = len([block for block in block_registry.values() if block.is_removable()])

print(part1)

## print end state
# for y in range(10):
# 	print(" ".join(map(str,[base[(x,y)] for x in range(10)])))
