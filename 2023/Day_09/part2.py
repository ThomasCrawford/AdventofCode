

def main():
	answer = 0
	with open("input.txt") as file:
		for line in file:
			sequence = [int(x) for x in line.split()]
			answer += predict(sequence)
	print(answer)

def predict(sequence):
	if all(x==0 for x in sequence):
		return 0
	else:
		sub_sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
		return sequence[0] - predict(sub_sequence)

if __name__ == '__main__':
	main()
