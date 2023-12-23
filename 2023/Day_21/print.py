
grid = {}
with open("test.txt") as file:
	for y_index, line in enumerate(file):
		width = len(line.strip())
		height = y_index+1
		for x_index, value in enumerate(line.strip()):
			grid[x_index+1j*y_index]= value
			if value == "S":
				active = set([x_index+1j*y_index])
half_width = int((width-1)/2)


def plot(filename, active):
	x_min = -55
	x_max = 50
	y_min = x_min
	y_max = x_max
	f = open(filename,"w")
	for y in range(y_min,y_max):
		for x in range(x_min, y_max):
			if x+y*1j in active:
				f.write("O")
			# elif x%width in [0,width-1]:
			# 	f.write("|")
			# elif y%width in [0, width -1]:
			# 	f.write("-")
			else:
				f.write(grid[x%width + y%width*1j])
		f.write("\n")
	f.close()

def f(active):
	new_active = set(
	p + d
	for p in active
	for d in [1,-1,1j,-1j]
	# if p+d in grid
	if grid[(p+d).real%width + (p+d).imag%height*1j] != "#"
	)
	return new_active

def count_from(first, count):
	x,y = first
	active = set([x+1j*y])
	for _ in range(count):
		active = f(active)
	return(len(active))

for _ in range(width*4+half_width):
	active = f(active)
print(len(active))

plot("snake.txt",active)
