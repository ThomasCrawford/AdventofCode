import re

size = 140

regex = r'(\d+)'



def coords_to_check(line_index,start,end):
	to_check = []
	if line_index > 0:
		for x in range(start,end):
			to_check.append([line_index-1,x])
		if start > 0:
			to_check.append([line_index-1,start-1])	
		if end < size:
			to_check.append([line_index-1,end])
	if line_index < size -1:
		for x in range(start,end):
			to_check.append([line_index+1,x])
		if start > 0:
			to_check.append([line_index+1,start-1])	
		if end < size:
			to_check.append([line_index+1,end])
	if start > 0:
			to_check.append([line_index,start-1])	
	if end < size:
			to_check.append([line_index,end])		
	return(to_check)

def check_these_coords(to_check):
	for [y,x] in to_check:
		if lines[y][x] != ".": return True
	return False

answer = 0
with open("input.txt") as file:
	lines = file.readlines()
	for y in range(size):
		line = lines[y]
		nums = re.finditer(regex,line)
		for num in nums:
			if check_these_coords(coords_to_check(y,num.start(),num.end())):
				answer = answer + int(num.group())

print(answer)


