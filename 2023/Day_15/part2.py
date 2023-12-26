import re


def hash_alg(word):
	x = 0
	for l in word:
		x = ((x+ord(l))*17)%256
	return x


with open("input.txt") as file:
	for line in file:
		words = line.split(",")

# placing lenses
hashmap = [[] for _ in range(256)]
for word in words:
	i = re.search(r'[=-]',word).start()
	box = hash_alg(word[:i])
	if word[i] == "=":
		found = False
		for lens in hashmap[box]:
			if lens[0] == word[:i]:
				lens[1] = word[i+1]
				found = True
		if not found:
			hashmap[box].append([word[:i],word[i+1]])
	else:
		for lens in hashmap[box]:
			if lens[0] == word[:i]:
				hashmap[box].remove(lens)


# scoring
answer = 0
for i in range(256):
	for j in range(len(hashmap[i])):
		answer += (i+1)*(j+1)*int(hashmap[i][j][1])
print (answer)