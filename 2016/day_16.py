import re

seed = '10001110011110000'
length1 = 272
length2 = 35651584

seed_inverse = "".join("0" if x == "1" else "1" for x in seed)[::-1]

def generate(seed1, seed2, target_length):
    while len(seed1) < target_length:
        seed1, seed2 = seed1 + "0" + seed2, seed1 + "1" + seed2
    return seed1[:target_length]

def checksum(string):
    while len(string)%2 == 0:
        pairs = re.findall('..', string)
        string = "".join('1' if pair[0]==pair[1] else '0' for pair in pairs)
    return string
    

p1 = generate(seed, seed_inverse, length1)
p2 = generate(seed, seed_inverse, length2)

print(f'Part 1: {checksum(p1)}')
print(f'Part 2: {checksum(p2)}')


