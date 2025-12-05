def get_factors(num):
    return [factor for factor in range(1,num) if num%factor==0]

def is_invalid(word):
    word = str(word)
    l = len(word)
    if l%2 != 0: 
        return False
    if word[:l//2]==word[l//2:]:
        return True
    else:
        return False


def is_invalid2(word):
    word = str(word)
    l = len(word)
    for factor in get_factors(l):
        parts = [word[i*factor:i*factor+factor] for i in range(l//factor)]
        if len(set(parts))==1:
            return True
    return False

with open("2.txt") as file:
    for line in file:
        data = line.split(",")

count = 0
count2 = 0

for r in data:
    start, stop = r.split("-")
    for number in range(int(start), int(stop)+1):
        if is_invalid(number):
            count += number
        if is_invalid2(number):
            count2 += number
            print(number)

print(count)
print(count2)