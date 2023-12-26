def turn_off(start, end):
	start_x, start_y = start
	end_x, end_y = end
	for x in range(start_x, end_x+1):
		for y in range(start_y, end_y+1):
			lights[y][x] = max(lights[y][x]-1,0)

def turn_on(start, end):
	start_x, start_y = start
	end_x, end_y = end
	for x in range(start_x, end_x+1):
		for y in range(start_y, end_y+1):
			lights[y][x] +=1

def toggle(start, end):
	start_x, start_y = start
	end_x, end_y = end
	for x in range(start_x, end_x+1):
		for y in range(start_y, end_y+1):
			lights[y][x] +=2


lights = [[0 for _ in range(1000)]for _ in range(1000)]


with open("input_06.txt") as file:
	for line in file:
		a, end = line.strip().split(" through ")
		end = [int(x) for x in end.split(',')]
		start = [int(x) for x in a.split(" ")[-1].split(',')]
		action = a.split(" ")[-2]
		match action:
			case "on": 
				turn_on(start, end)
			case "off":
				turn_off(start, end)
			case "toggle":
				toggle(start, end)

count = 0
for row in lights:
	count += sum(row)
print(f'Part 2: {count}')

