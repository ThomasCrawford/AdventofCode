

def one_step(current_number, section_number):
	for direction in maps[section_number]:
		if direction[1] <=current_number < direction[1] + direction[2]:
			return current_number - direction[1] + direction[0]
	return current_number

def trace(seed):
	current_number = seed
	for i in range(7):
		current_number = one_step(current_number,i)
	return current_number

with open("input.txt") as file:

	#process input
	seeds = [int(x) for x in file.readline()[7:-1].split()]
	which_section = -1
	maps = [[],[],[],[],[],[],[]]
	for line in file:
		if line.find(":")>0: 
			which_section +=1
		elif line == "\n": pass
		else: maps[which_section].append([int(x) for x in (line[:-1].split())])

	#run each seed through maps
	print(min([trace(x) for x in seeds]))

