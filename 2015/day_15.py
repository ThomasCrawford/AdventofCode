import re
import numpy as np

#parsing
regex = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'

data = []
calories = []
with open("input_15.txt") as file:
    for line in file:
        n, a1, a2, a3, a4, a5 = re.match(regex, line.strip()).groups()
        data.append([int(a1), int(a2), int(a3), int(a4)])
        calories.append(int(a5))
kitchen = np.array(data)
calories = np.array(calories)

## funciton to optimize
# v = [1,2,3,4]
def score(v):
	p = v @ kitchen
	p = [max(0,x) for x in p]
	s = np.prod(p)
	return s

def calorie_count(v):
	return v @ calories

answer1 = 0
answer2 = 0
for n1 in range(101):
	for n2 in range(101-n1):
		for n3 in range(101-n1-n2):
			n4 = 100-n1-n2-n3
			v = [n1,n2,n3,n4]
			this_score = score(v)
			answer1 = max(answer1, this_score)
			if v @ calories == 500:
				answer2 = max(answer2, this_score)


print(f'Part 1: {answer1}')
print(f'Part 2: {answer2}')

