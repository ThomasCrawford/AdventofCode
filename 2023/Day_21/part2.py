
grid = {}
with open("input.txt") as file:
	for y_index, line in enumerate(file):
		width = len(line.strip())
		height = y_index+1
		for x_index, value in enumerate(line.strip()):
			grid[x_index+1j*y_index]= value
			if value == "S":
				active = set([x_index+1j*y_index])
half_width = int((width-1)/2)

def diamond_num(x):
	return 2*x*(x+1)+1


def f(active):
	new_active = set(
	p + d
	for p in active
	for d in [1,-1,1j,-1j]
	if p+d in grid
	if grid[(p+d).real%width + (p+d).imag%height*1j] != "#"
	)
	return new_active

def count_from(first, count):
	x,y = first
	active = set([x+1j*y])
	for _ in range(count):
		active = f(active)
	return(len(active))

sides = [[-1,half_width], [width, half_width],[half_width,-1],[half_width,width]]
corners = [[-1,0],[-1,width-1],[width,width-1],[width-1,-1]]
center = [half_width,half_width]

sid = 0
for p in sides:
	new = count_from(p,width)
	print(new)
	sid += new

big_corn = 0
for p in corners:
	new = count_from(p,width+half_width)
	print(new)
	big_corn += new

small_corn = 0
for p in corners:
	new = count_from(p,half_width)
	print(new)
	small_corn += new

center_even = count_from(center,width*2)
center_odd = count_from(center,width*2+half_width)
print(center_even, center_odd)

n = 202300
# n = 2


answer = (n-1)**2*center_odd + (n**2)*center_even+(n-1)*big_corn + n*small_corn + sid

print(answer)
