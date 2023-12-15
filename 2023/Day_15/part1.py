


def hash_alg(word):
	x = 0
	for l in word:
		x = ((x+ord(l))*17)%256
	return x


with open("input.txt") as file:
	for line in file:
		words = line.split(",")

answer = 0
for word in words:
	answer += hash_alg(word)
print(answer)