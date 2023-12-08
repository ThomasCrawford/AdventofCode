import math

def parse_line(line):
	key, pair = line.split(" = ")
	pair = pair.replace("(","").replace(")","")[:-1]
	return key, pair.split(", ")

def one_walk(start,dictionary,directions):
	steps = 0
	dir_length = len(directions)
	location = start
	while not location.endswith("Z"):
		location = dictionary[location][int(directions[steps%dir_length])]
		steps += 1
	return steps


def main():
	#import
	dictionary = {}
	with open("input.txt") as file:
		directions = file.readline()[:-1]
		file.readline()
		for line in file:
			key, pair = parse_line(line)
			dictionary[key] = pair
	directions = directions.replace("L","0").replace("R","1")

	walk_lengths = []
	for key in dictionary:
		if key.endswith("A"):
			walk_lengths.append(one_walk(key,dictionary,directions))
	# print(walk_lengths)
	print(math.lcm(*[int(x) for x in walk_lengths]))


if __name__ == '__main__':
	main()
