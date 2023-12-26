#232

count = 0
found = False

with open("input_01.txt") as file:
	for line in file:
		for i, x in enumerate(line.strip()):
			if x == "(": 
				count +=1
			else: 
				count = count-1
			if count == -1 and found == False:
				answer = i+1
				found = True
print(f"Part 1: {count}")
print(f"Part 2: {answer}")
