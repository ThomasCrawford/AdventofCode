
translate = {
    -1-1j: 1,
    -1j: 2,
    1-1j: 3,
    -1: 4, 
    0: 5,
    1: 6,
    -1 +1j: 7,
    1j: 8,
    1+1j:9
}

data = []
with open("input_02.txt") as file:
    for line in file:
        data.append(line.strip())

direct = {"R": 1, "D": 1j, "L": -1, "U": -1j}

p = 0

def step(p,d):
    new_p = p + d
    if -1 <= new_p.real <= 1 and -1 <= new_p.imag <= 1:
        return new_p
    else:
        return p

answer1 = ""
for word in data:
    for x in word:
        p = step(p,direct[x])
    answer1 += str(translate[p])

print(answer1)