goal = 2020

with open("01.txt") as file:
	numbers = [int(x.strip()) for x in file]

def find_pair(nums, target):
	for x in nums:
		if target - x in nums:
			return x*(target-x)

#part 1
print(find_pair(numbers,goal))

#part2
for i in range(len(numbers)):
	if find_pair(numbers[i:],goal-numbers[i]):
		print (numbers[i]*find_pair(numbers[i:],goal-numbers[i]))
		exit()
