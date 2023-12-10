
data = []
potential_interior = []
actual_interior = []


def find_s():
	for i in range(height):
		for j in range(width):
			if data[i][j] == "S": return j,i


def next_index (x,y,prev_x,prev_y):
	if data[y][x] == "|": 
		return x,2*y-prev_y, x, y
	elif data[y][x] == "-":
 		return 2*x - prev_x, y, x, y
	elif data[y][x] == "F": 
		if x == prev_x: return x+1, y, x, y
		else: return x, y+1, x, y
	elif data[y][x] == "J": 
		if x == prev_x: return x-1, y, x, y
		else: return x, y-1, x, y
	elif data[y][x] == "L": 
		if x == prev_x: return x+1, y, x, y
		else: return x, y-1, x, y
	elif data[y][x] == "7": 
		if x == prev_x: return x-1, y, x, y
		else: return x, y+1, x, y


def add_to_potential_interior(state):
	x,y,prev_x,prev_y = state
	if (data[y][x] == "|" and y>prev_y) or \
	(data[y][x] == "7" and y==prev_y) or \
	(data[y][x] == "J" and x==prev_x): 
		potential_interior.append([x,y])


width = 0
with open("input.txt") as file:
	for line in file:
		data.append(line)
		width = len(line)
	height = len(data)


start = find_s()
state = start[0]-1, start[1],start[0],start[1] #start by moving to the left

sieve = [[x,y] for x in range(1,width) for y in range(height)] #all tiles in total
sieve.remove([start[0],start[1]])	#remove starting tile

while not (state[0] == start[0] and state[1] == start[1]):
	sieve.remove([state[0],state[1]]) #remove tiles that are a part of main loop
	state = next_index(*state)
	add_to_potential_interior(state) 

for [x,y] in sieve:
	if [x-1,y] in potential_interior or [x-1,y] in actual_interior:
		actual_interior.append([x,y])

print(len(actual_interior))

