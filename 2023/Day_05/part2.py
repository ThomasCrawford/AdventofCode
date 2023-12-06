

def one_step(current_number, section_number):
	for direction in maps[section_number]:
		if direction[1] <=current_number < direction[1] + direction[2]:
			return current_number - direction[1] + direction[0]
	return current_number

#return the location for a specified seed
def trace(seed):
	current_number = seed
	for i in range(7):
		current_number = one_step(current_number,i)
	return current_number

#return the seed that goes in specified location
def back_trace(location):
	current_number = location
	for i in range(7):
		current_number = one_step_back(current_number,6-i)
	return current_number

def one_step_back(current_number,section_number):
	for direction in maps[section_number]:
		if direction[0] <=current_number < direction[0] + direction[2]:
			return current_number + direction[1] - direction[0]
	return current_number


def in_seed_range(seed):
	for i in range(int(len(seeds)/2)):
		if seeds[2*i] <= seed < seeds[2*i] + seeds[2*i + 1]:
			return True
	return False

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
	for i in range(10000000,100000000):
		if i%1000000 ==0: print(f'Checked {i} starting locations')
		if in_seed_range(back_trace(i)):
			print(i,back_trace(i))
			exit()



#returns 24261545