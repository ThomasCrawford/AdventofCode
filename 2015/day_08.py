
def count_escaped(string):
	escaped = 2
	index = 1
	while index < len(string) -1:
		if string[index] == "\\":
			if string[index+1] == "x":
				escaped += 3
				index += 4
			else:
				escaped += 1
				index += 2
		else:
			index += 1
	return escaped

def count_2(string):
	return 2 + string.count('\\')+ string.count("\"")


data = []
with open("input_08.txt") as file:
	for line in file:
		data.append(line.strip())

count1 = 0
count2 = 0
for line in data:
	count1 += count_escaped(line)
	count2 += count_2(line)
print(f'Part 1: {count1}')
print(f'Part 2: {count2}')

