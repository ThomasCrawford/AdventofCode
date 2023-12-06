
answer = 0

with open("Day1in.txt") as file:
	for line in file:
		num = [int(x) for x in line if x.isdigit()]
		answer = answer + num[0]*10 + num[-1]

print(answer)

