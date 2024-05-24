import cmath


def find_start():
    for z in data:
        if z.real == 0 and data[z] == "-":
            return z, 1
        if z.real == width -1 and data[z] == "-":
            return z, -1
        if z.imag == 0 and data[z] == "|":
            return z, 1j
        if z.imag == length -1 and data[z] == "|":
            return z, -1j

def step(z, d, seen):
    if z+d not in data or data[z+d] == " ":
        return z, 0, seen
    elif data[z+d] == "+":
        for new_d in [d*1j, -1*d*1j]:
            new_z = z+d+new_d
            if new_z in data and data[new_z] not in ["+"," "]:
                return new_z, new_d, seen + ["+"] + [data[new_z]]
    else:
        return z+d, d, seen + [data[z+d]]

data = {}
with open("input_19.txt") as file:
    for y, line in enumerate(file):
        width = len(line) - 1
        length = y + 1
        for x, v in enumerate(line[:-1]):
            data[x+y*1j] = v 

z, d = find_start()
seen = []
while d:
    z,d,seen = step(z,d,seen)

ans1 = "".join(seen).replace("|","").replace("-","").replace("+","")
print(ans1)

ans2 = len(seen)+1
print(ans2)
