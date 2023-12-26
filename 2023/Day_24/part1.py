cutoff_min = 200000000000000
cutoff_max = 400000000000000

data = []
with open('input.txt') as file:
	for line in file:
		p , d = line.strip().split('@')
		p = [int(x) for x in p.strip().split(',')]
		d = [int(x) for x in d.strip().split(',')]
		data.append([p,d])
height = len(data)


def moving_towards_intersection(x,y, x1, y1, dx1, dy1):
	assert dx1 != 0
	assert dy1 != 0
	if ((x-x1>0 and dx1>0) or (x-x1<0 and dx1<0)) and \
			((y-y1>0 and dy1>0) or (y-y1<0 and dy1<0)):
		return True
	return False

def find_intersection(stone1,stone2):
	p1, d1 = stone1
	p2, d2 = stone2
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	dx1, dy1, dz1 = d1
	dx2, dy2, dz2 = d2
	m1 = dy1/dx1
	m2 = dy2/dx2
	if m1 == m2: 
		return False
	b1 = y1-m1*x1
	b2 = y2 -m2*x2
	x = (b2-b1)/(m1-m2)
	y = m2*(b2-b1)/(m1-m2)+b2
	if cutoff_min <= x <= cutoff_max and cutoff_min<= y<= cutoff_max: 
		if moving_towards_intersection(x,y, x1, y1, dx1, dy1) and \
				moving_towards_intersection(x,y, x2, y2, dx2, dy2):
			return True

count = 0
missed = 0
for i, stone in enumerate(data):
	for other_stone_index in range(i,height):
		other_stone = data[other_stone_index]
		if find_intersection(stone, other_stone):
			# print(f'Stones {i} and {other_stone_index} collide')
			count += 1
		else: missed += 1

print(count, missed)


