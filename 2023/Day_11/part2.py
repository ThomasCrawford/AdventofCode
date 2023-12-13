

star_locations = []


def sum_of_distances(star_locations,direction):
	integers = [star[direction] for star in star_locations]
	integers.sort()
	result = 0
	n = len(integers)
	for i in range(n):
		result += (n-i)*integers[n-i-1] - (n-i)*integers[i]
	return(result)



# process data
with open("input.txt") as file:
	for count, line in enumerate(file):
		for i in range(len(line)):
			if line[i] == "#":
				star_locations.append([count,i])

#where is the universe expanding?
where_to_expand_y = list(range(count))
where_to_expand_x = list(range(count))
for star in star_locations:
	if star[0] in where_to_expand_y: 
		where_to_expand_y.remove(star[0])
	if star[1] in where_to_expand_x: 
		where_to_expand_x.remove(star[1])
where_to_expand_x.reverse()
where_to_expand_y.reverse()


#expand the universe

expansion_rate = 999999 # how many extra rows/columns. should be 1 for part 1

expanded_star_locations = []
for x_expand in where_to_expand_x:
	star_locations = [[star[0],star[1]+expansion_rate] if star[1]>x_expand else star for star in star_locations]
for y_expand in where_to_expand_y:
	star_locations = [[star[0]+expansion_rate,star[1]] if star[0]>y_expand else star for star in star_locations]


print(sum_of_distances(star_locations,0)+sum_of_distances(star_locations,1))