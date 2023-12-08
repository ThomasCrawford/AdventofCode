
#rework because now J is wild.
def hand_type(fivecards):
	unique = list(set(fivecards.replace("1","")))
	num_unique = len(unique)
	if num_unique == 1 or num_unique==0: return 6
	elif num_unique == 5: return 0
	elif num_unique ==4: return 1
	elif num_unique ==2: 
		largest = max([fivecards.count(x) for x in unique]) + fivecards.count("1")
		if largest ==4: return 5
		else: return 4
	elif num_unique == 3:
		largest = max([fivecards.count(x) for x in unique]) + fivecards.count("1")
		if largest == 3: return 3
		else: return 2



#now J is the weakest
def rename(string):
	return string.replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', '1').replace('T', 'B')



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
