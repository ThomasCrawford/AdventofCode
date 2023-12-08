

def parse_line(line):
	key, pair = line.split(" = ")
	pair = pair.replace("(","").replace(")","")[:-1]
	return key, pair.split(", ")

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

	#follow directions
	dir_length = len(directions)

	steps = 0
	location = "AAA"
	while location != "ZZZ":
		location = dictionary[location][int(directions[steps%dir_length])]
		steps += 1
	print(steps)

if __name__ == '__main__':
	main()