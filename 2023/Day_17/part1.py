import cmath
import heapq


#processing
raw_data = []
with open("input.txt") as file:
	for line in file:
		raw_data.append(line.strip())
width = len(raw_data[0])
height = len(raw_data)

data = {}
for i in range(width):
	for k in range(height):
		data[(k,i)] = int(raw_data[k][i])


#(c, p, d) cost, 
#		position ((row,column)) 
#		direction entered node (T = east-west, F = north-south)

Q = [[0,(0,0),True],[0,(0,0),False]]
heapq.heapify(Q) 
visited = []


while Q:
	c, p, d = heapq.heappop(Q)
	if p == (height-1,width-1):
		print(c)
		exit()
	print(f"{c} to get to {p,d}")
	visited.append((p,d))

	# add neighboring nodes to Q
	for which_way in [-1,1]:
		new_c = c
		for i in range(1,4):
			new_p = (p[0] + i * d * which_way, p[1]+i * (not d) * which_way)
			if not (0<=new_p[0]<height and 0<=new_p[1]<width): 
				break
			new_c += data[new_p]
			if (new_p,not d) not in visited: 
				found = False
				for x in Q:
					if x[1]==new_p and x[2] != d:
						x[0] = min(x[0],new_c)
						found = True
				if not found:
					Q.append([new_c, new_p, not d])

