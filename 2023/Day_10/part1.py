

data = []

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

width = 0
with open("input.txt") as file:
	for line in file:
		data.append(line)
		width = len(line)
	height = len(data)

start = find_s()

state = start[0]-1, start[1],start[0],start[1]

step_count = 1
while not (state[0] == start[0] and state[1] == start[1]):
	state = next_index(*state)
	step_count += 1
print(step_count/2)
