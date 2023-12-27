directions = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]

def in_bounds(p):
    return 0<=p.real<width and 0<=p.imag<height

def get_neighbors(i):
    return [i+d for d in directions if in_bounds(i+d)]


def conway(dictionary):
    new_dictionary = {}
    for p in dictionary:
        neighbor_count = sum([dictionary[x] for x in get_neighbors(p)])
        if neighbor_count == 3:
            new_dictionary[p] = True
        elif neighbor_count == 2:
            new_dictionary[p] = dictionary[p]
        else:
            new_dictionary[p] = False
    return new_dictionary


data = []
with open("input_18.txt") as file:
    for line in file:
        data.append(line.strip())
width = len(data[0])
height = len(data)

lights = {}
for y,line in enumerate(data):
    for x, status in enumerate(line):
        lights[x+y*1j] = status =="#"


for _ in range(100):
    lights = conway(lights)
print(sum(lights.values()))

