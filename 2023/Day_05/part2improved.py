

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

	#generate list of candidate endpoints to check
	cutoff_list = seeds
	for i in range(7):
		cutoff_list = [one_step(x,i) for x in cutoff_list] +[direction[0] for direction in maps[i]]
	cutoff_list.sort()	

	#run each seed through maps
	for i in cutoff_list[1:]:
		if in_seed_range(back_trace(i)):
			print(i)
			exit()



#returns 24261545