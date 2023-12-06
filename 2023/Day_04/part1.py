


def how_many_overlap(line):
	wins, own = line[line.index(":")+1:].split("|")
	wins = [int(i) for i in wins.split()]
	own = [int(i) for i in own.split()]
	return(len([x for x in wins if x in own]))

with open("input.txt") as file:
	lines = file.readlines()
	card_count = len(lines)
	card_set = [1]*card_count
	for card_id in range(card_count):
		line = lines[card_id]
		overlap_count = how_many_overlap(line)
		if overlap_count:
			for i in range(card_id+1,card_id+overlap_count+1):
				card_set[i] = card_set[i]+card_set[card_id]

print(sum(card_set))