def move(p, steps, d):
	match d:
		case 0:
			new_p = [p[0], p[1]+steps]
		case 1:
			new_p = [p[0]+steps, p[1]]
			v_lines.append([p[0],new_p[0],p[1],False])
		case 2:
			new_p = [p[0], p[1]-steps]
		case 3:
			new_p = [p[0]-steps, p[1]]	
			v_lines.append([new_p[0],p[0],p[1],True])
	return new_p

def find_width(row):
	width = 1
	relevant_lines = [line[2:] for line in v_lines if line[0] <= row <= line[1]]
	relevant_lines.sort(key = lambda x:x[0])
	for i in range(len(relevant_lines)-1):
		if relevant_lines[i][1]:
			width += relevant_lines[i+1][0] - relevant_lines[i][0]
		else: width += 1
	return width

#part 2 import
data = [] # [direction, numbers of steps]
v_lines = [] # [y start, y end, x, True if start]
with open("input.txt") as file:
	for line in file:
		a = line.strip().split(" ")
		data.append([int(a[2][-2]),int(a[2][2:-2],16)])

# traverse the path
p=[0,0]
for x in data:
	p = move(p,x[1],x[0])

# get cutoff values in order
cutoffs = set()
for x in v_lines:
	cutoffs.add(x[0])
	cutoffs.add(x[1])
cutoffs = list(cutoffs)
cutoffs.sort()


#add up non cutoff lines
running_total = 0
for i in range(len(cutoffs)-1):
	height = cutoffs[i+1] - cutoffs[i]-1
	width = find_width(cutoffs[i]+1)
	# print(f"looking at crit_row {cutoffs[i]}: width = {find_width(cutoffs[i])}")
	# print(f"looking at row {cutoffs[i]+1}: height = {height}, width = {width}, total = {height*width}")
	running_total += height*width

	#add a cutoff line
	running_total += find_width(cutoffs[i])
running_total += find_width(cutoffs[-1])

# some horrizontal bits aren't yet included.  this adds those
l = len(data)
for i in range(len(data)):
	if (data[i][0] == 3 and data[(i+1)%l][0] == 2 and data[(i+2)%l][0] == 1) or\
			(data[i][0] == 1 and data[(i+1)%l][0] == 0 and data[(i+2)%l][0] == 3) or\
			(data[i][0] == 1 and data[(i+1)%l][0] == 0 and data[(i+2)%l][0] == 1) or\
			(data[i][0] == 1 and data[(i+1)%l][0] == 2 and data[(i+2)%l][0] == 1):
		running_total += data[(i+1)%l][1]-1

print(running_total)
