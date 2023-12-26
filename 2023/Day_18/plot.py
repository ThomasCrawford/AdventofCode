data = []
trench = []
potential_interior = []
actual_interior = []

#returns 1 if clockwise, -1 if counter
def is_clockwise():
	rl_count = 0
	for x in data:
		if x[0]=="R": rl_count +=1
		elif x[0]=="L": rl_count += -1
	if rl_count == -1: return True
	else: return False


def move(p, steps, d):
	for i in range(steps):
		match d:
			case 3: 
				potential_interior.append([p[0],p[1]+1])
				p = [p[0]-1, p[1]]
			case 1: 
				p = [p[0]+1, p[1]]
			case 2: p = [p[0], p[1]-1]
			case 0: p = [p[0], p[1]+1]
		trench.append(p)
	return p


cutoffs = set([])
with open("input.txt") as file:
	for line in file:
		a = line.strip().split(" ")
		data.append([int(a[2][-2]),int(int(a[2][2:-2],16)/50000)])

p = [0,0]
for x in data:
	p = move(p, int(x[1]), x[0])


xmin = min([x[1] for x in trench])
xmax = max([x[1] for x in trench])
ymin = min([x[0] for x in trench])
ymax = max([x[0] for x in trench])
print(len(data))

print(xmin, xmax)
print(ymin, ymax)

f = open("output.txt", "w")
for y in range(ymin, ymax +1):
	for x in range(xmin, xmax+1):
		if [y,x] in potential_interior:
			f.write("%")
		elif [y,x] in trench:
			f.write("#")
		else:
			f.write(".")
	f.write("\n")
f.close()

# print (trench)

# print (potential_interior)

print(len(trench))







