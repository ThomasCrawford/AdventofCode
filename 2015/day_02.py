count1 = 0
count2 = 0
with open("input_02.txt") as file:
	for line in file:
		a,b,c = [int(x) for x in line.strip().split("x")]
		count1 += 2*(a*b+b*c+a*c)+min(a*b, a*c, b*c)
		count2 += 2*min(a+b, a+c, b+c) + a*b*c

print(f'Part 1: {count1}')
print(f'Part 2: {count2}')
