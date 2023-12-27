puzzle = '1321131112'

def look_and_say(string):
	i = 0
	word = ""
	while i < len(string):
		j = i + 1
		while j < len(string) and string[i] == string[j]:
			j += 1
		word += str(j-i)
		word += string[i]
		i = j
	return word

for _ in range(40):
	puzzle = look_and_say(puzzle)

print(f"Part 1: {len(puzzle)}")

for _ in range(10):
	puzzle = look_and_say(puzzle)

print(f"Part 2: {len(puzzle)}")

