import re


def slide_left(string):
	new_string = ""
	for chunk in string.split("#"):
		new_string = new_string + "O"*chunk.count("O") + "."*chunk.count(".") + "#"
	return new_string[:-1]

def rotate_clockwise(data):
	return tuple(["".join(word[i] for word in data)[::-1] for i in range(len(data))])

def rotate_clockwise_slide_left(data):
	rotated_data = ["".join(word[i] for word in data)[::-1] for i in range(len(data))]
	new_data = []
	for line in rotated_data:
		new_data.append(slide_left(line))
	return tuple(new_data)

def score_board(data):
	for _ in range(3):
		data = rotate_clockwise(data)
	answer = 0
	for x in data:
		for i in range(len(x)):
			if x[i] == "O":
				answer += i+1
	return answer


with open("input.txt") as file:
	data = tuple([line.strip() for line in file])
width = len(data[0])

#some pre-rotating so that I only have to slide to the left
for _ in range(2):
	data = rotate_clockwise(data)

#Caching the results from rotate_clockwise_slide_left(), also recording how many steps we've done
diy_cache = {}
i=1
while data not in diy_cache:
	new_data = rotate_clockwise_slide_left(data)
	diy_cache[data]=[new_data,i]
	data = new_data
	i += 1
cycle_start = diy_cache[data][1]
cycle_length = i - diy_cache[data][1]

#a spin is a 1/4 rotation and a shift left
#1000000000 steps should be the same as:
num_of_spins = (1000000000*4-cycle_start)%(cycle_length)+cycle_start

#look up the num_of_spins-th entry in the dictionary
for _, x in diy_cache.items():
	if x[1]==num_of_spins:
		print (score_board(x[0]))