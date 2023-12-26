import re

vowels = r'[aeiou]'
pairs_pattern = r'(ab|cd|pq|xy)'

def is_nice(string):
	if len(re.findall(vowels, string)) < 3:
		return False
	if len(re.findall(pairs_pattern, string)) > 0:
		return False
	if not re.search(r'(.)\1', string):
		return False
	return True

def cond_2(string):
	for i in range(len(string)-2):
		if string[i] == string [i+2]:
			return True
	return False

def cond_1(string):
	for i in range(len(string)-3):
		for k in range(i+2, len(string)-1):
			if string[i:i+2] == string[k:k+2]:
				return True
	return False

count = 0
count2 = 0
with open('input_05.txt') as file:
	for line in file:
		word = line.strip()
		if is_nice(word):
			count += 1
		if cond_1(word) and cond_2(word):
			count2 += 1


print(f'Part 1: {count}')
print(f'Part 2: {count2}')



