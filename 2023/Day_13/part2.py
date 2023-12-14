

def transpose_strings(grid):
	#assume grid is rectangular, otherwise this shoudl be "max"
	length = len(grid[0])
	return ["".join(word[i] for word in grid) for i in range(length)]

def diff_letters(a,b):
	return sum(a[i] != b[i] for i in range(len(a)))

#now expecting exactly one smudge
def mirror_after_i(grid, i):
	smudges_remaining = 1
	n = len(grid)
	num_to_check = min(i, n-i)
	for x in range(num_to_check):
		if diff_letters(grid[i-x-1],grid[i+x]) == 1 and smudges_remaining == 1:
			smudges_remaining = 0
		elif diff_letters(grid[i-x-1],grid[i+x]) > 0:
			return False
	if smudges_remaining ==0:
		return True

def find_mirror(grid):
	for i in range(1,len(grid)):
		if mirror_after_i(grid,i):
			return i
	return 0



answer = 0

#misses the last chunk unless you add a blank line to the input file
with open("input.txt") as file:
	working_problem = []

	for line in file:
		line = line.strip()
		if line:
			working_problem.append(line)
		else:
			answer += find_mirror(working_problem)*100 + find_mirror(transpose_strings(working_problem))
			working_problem = []

print(answer)