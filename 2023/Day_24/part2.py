import numpy as np 
from scipy.optimize import fsolve, root


data = []
with open('input.txt') as file:
	for line in file:
		p , d = line.strip().split('@')
		p = [int(x) for x in p.strip().split(',')]
		d = [int(x) for x in d.strip().split(',')]
		data.append([p,d])
height = len(data)


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


def 





# v = [t1, t2, t3, x0, y0, z0, dx0, dy0, dz0, t4, t5]
#       0   1   2   3   4   5   6    7    8

x1, y1, z1, = data[1][0]
dx1, dy1, dz1 = data[1][1]
x2, y2, z2, = data[2][0]
dx2, dy2, dz2 = data[2][1]
x3, y3, z3, = data[3][0]
dx3, dy3, dz3 = data[3][1]
x4, y4, z4, = data[4][0]
dx4, dy4, dz4 = data[4][1]
x5, y5, z5, = data[0][0]
dx5, dy5, dz5 = data[0][1]
x6, y6, z6, = data[6][0]
dx6, dy6, dz6 = data[6][1]

# v = [x0, y0, z0, dx0, dy0, dz0, t1, t2, t3, t4, t5, t6, s1, s2, s3, s4, s5, s6 ]
#		0   1   2   3    4    5    6   7  8    9   10  11  12  13  14


def func2(v):
	return [
		x1 + v[6]*dx1 - v[0]-v[12]*v[3],
		y1 + v[6]*dy1 - v[1]-v[12]*v[4],
		z1 + v[6]*dz1 - v[2]-v[12]*v[5],

		x1 + v[7]*dx1 - v[0]-v[13]*v[3],
		y1 + v[7]*dy1 - v[1]-v[13]*v[4],
		z1 + v[7]*dz1 - v[2]-v[13]*v[5],

		x1 + v[8]*dx1 - v[0]-v[14]*v[3],
		y1 + v[8]*dy1 - v[1]-v[14]*v[4],
		z1 + v[8]*dz1 - v[2]-v[14]*v[5],

		x1 + v[9]*dx1 - v[0]-v[15]*v[3],
		y1 + v[9]*dy1 - v[1]-v[15]*v[4],
		z1 + v[9]*dz1 - v[2]-v[15]*v[5],

		x1 + v[10]*dx1 - v[0]-v[16]*v[3],
		y1 + v[10]*dy1 - v[1]-v[16]*v[4],
		z1 + v[10]*dz1 - v[2]-v[16]*v[5],

		x1 + v[11]*dx1 - v[0]-v[17]*v[3],
		y1 + v[11]*dy1 - v[1]-v[17]*v[4],
		z1 + v[11]*dz1 - v[2]-v[17]*v[5],

		]



def func(v):
	return [v[0]*(v[6]-dx1)+v[3]-x1,
		v[1]*(v[6]-dx2)+v[3]-x2,
		v[2]*(v[6]-dx3)+v[3]-x3,
		v[9]*(v[6]-dx4)+v[3]-x4,
		v[10]*(v[6]-dx5)+v[3]-x5,
		v[0]*(v[7]-dy1)+v[4]-y1,
		v[1]*(v[7]-dy2)+v[4]-y2,
		v[2]*(v[7]-dy3)+v[4]-y3,
		v[9]*(v[7]-dy4)+v[4]-y4,
		v[10]*(v[7]-dy5)+v[4]-y5,
		v[0]*(v[8]-dz1)+v[5]-z1,
		v[1]*(v[8]-dz2)+v[5]-z2,
		v[2]*(v[8]-dz3)+v[5]-z3,
		v[9]*(v[8]-dz4)+v[5]-z4,
		v[10]*(v[8]-dz5)+v[5]-z5,

		]

# for i, stone in enumerate(data[:5]):
# 	print(f'{stone[0][0]}+t{i+1}*{stone[1][0]} ==x0 + t{i+1}*dx0 ,{stone[0][1]}+t{i+1}*{stone[1][1]} ==y0 + t{i+1}*dy0 ,{stone[0][2]}+t{i+1}*{stone[1][2]} ==z0 + t{i+1}*dz0 ')
# 	print(",")


root = fsolve(func2, [393358484426865,393358484426865,393358484426865,1,1,1,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477,498859436477],\
		 xtol = 0.01)
for x in root:
	print (x)
# print(f'x0, y0, z0, ')

# root = root(func, [10**10,10**10,10**10,10**10,10**10, 152059913859832,152059913859832,152059913859832,152059913859832,152059913859832, 1,1,1,1,1],\
# 		 options={'maxfev': 10000, 'xtol': 1e-12}, method='hybr')

# root = fsolve(func, [10**10,10**10,10**10,10**10,10**10,10**10, 152059913859832,152059913859832,152059913859832,152059913859832,152059913859832,152059913859832, 1,1,1,1,1,1],\
# 		 xtol = 0.01)


# print(func([3, 4, 6, 24, 13, 10, -3, 1, 2,]))

