

def hand_type(fivecards):
	unique = list(set(fivecards))
	num_unique = len(unique)
	if num_unique == 1: return 6
	elif num_unique == 5: return 0
	elif num_unique ==4: return 1
	elif num_unique ==2: 
		count_of_first = fivecards.count(unique[0])
		if count_of_first == 2 or count_of_first == 3:
			return 4
		else:
			return 5
	elif num_unique == 3:
		count_of_first = fivecards.count(unique[0])
		if count_of_first == 3: return 3
		elif count_of_first == 2: return 2
		else:
			count_of_second = fivecards.count(unique[1])
			if count_of_second == 2: return 2
			else: return 3

def rename(string):
	return string.replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', 'C').replace('T', 'B')



hands = []
with open("input.txt") as file:
	for line in file:
		hands.append(line.split())

for hand in hands:
	hand[0] = rename(hand[0])
	hand.append(hand_type(hand[0]))

hands.sort(key = lambda x:x[0])
hands.sort(key = lambda x:x[2])

answer = 0
for i in range(len(hands)):
	answer = answer + (i+1)*int(hands[i][1])
print(answer)
