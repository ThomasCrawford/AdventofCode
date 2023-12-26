#4644

data = []
with open("input_03.txt") as file:
	for line in file:
		data.append([x for x in line.strip()])

answer = 0
for route in data:
	# print(route)
	visited = set([0])
	p=0
	for d in route:
		match d:
			case ">":
				p += 1
			case "v":
				p += 1j
			case "<":
				p += -1
			case "^":
				p += -1j
		visited.add(p)
	answer += len(visited)
print(f'Part 1: {answer}')


answer2 = 0
for route in data:
	# print(route)
	visited = set([0])
	p=0
	for d in route[::2]:
		match d:
			case ">":
				p += 1
			case "v":
				p += 1j
			case "<":
				p += -1
			case "^":
				p += -1j
		visited.add(p)
	p2 = 0
	for d in route[1::2]:
		match d:
			case ">":
				p2 += 1
			case "v":
				p2 += 1j
			case "<":
				p2 += -1
			case "^":
				p2 += -1j
		visited.add(p2)
	answer2 += len(visited)
print(f'Part 2: {answer2}')

