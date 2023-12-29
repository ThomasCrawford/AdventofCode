
translate = {
    0: '5',
    1: '6',
    2: '7',
    3: '8',
    4: '9',
    1+1j: "A",
    2+1j: "B",
    3+1j: "C",
    2+2j: "D",
    1-1j: "2",
    2-1j: "3",
    3-1j: "4",
    2-2j: "1"
}


data = []
with open("input_02.txt") as file:
    for line in file:
        data.append(line.strip())

direct = {"R": 1, "D": 1j, "L": -1, "U": -1j}

p = 0

def step(p,d):
    new_p = p + d
    if new_p in translate:
        return new_p
    else:
        return p

answer1 = ""
for word in data:
    for x in word:
        p = step(p,direct[x])
    answer1 += str(translate[p])

print(answer1)
