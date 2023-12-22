
grid = {}
with open("test.txt") as file:
	for y_index, line in enumerate(file):
		width = len(line)
		height = y_index+1
		for x_index, value in enumerate(line.strip()):
			grid[x_index+1j*y_index]= value
			if value == "S":
				active = set([x_index+1j*y_index])


# def f(active, grid):
# 	new_active = set()
# 	for p in active:
# 		for d in [1,-1,1j,-1j]:
# 			if p+d in grid:
# 				if grid[p+d] != "#":
# 					new_active.add([y,x])
# 	return new_active

def f(active):
	new_active = set(
	p + d
	for p in active
	for d in [1,-1,1j,-1j]
	# if grid[p+d] != "#"
	)
	return new_active

print(active)

for i in range(65):
	active = f(active)
	print(len(active))

# print(active)
# print(len(active))