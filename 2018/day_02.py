import itertools

def contains_double(word):
    for l in word:
        if word.count(l) == 2:
            return True
    return False


def contains_triple(word):
    for l in word:
        if word.count(l) == 3:
            return True
    return False

def close(word1, word2):
    common = ""
    for i,l in enumerate(word1):
        if l == word2[i]:
            common += l
    return common



data = []
with open("input_02.txt") as file:
    for line in file:
        data.append(line.strip())

trip_count = sum([1 if contains_triple(word) else 0 for word in data])
dub_count = sum([1 if contains_double(word) else 0 for word in data])

print(trip_count*dub_count)


target = len(data[0])-1
for x,y in itertools.combinations(data,2):
    if len(close(x,y))==target:
        print(close(x,y))


