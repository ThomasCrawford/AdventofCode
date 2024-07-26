#319 too high

def close(star1, star2):
    return sum([abs(star1[i]-star2[i]) for i in range(4)]) <= 3

def in_const(star, const):
    for star2 in const:
        if close(star, star2):
            return True
    return False

data = []
with open("input_25.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip().split(",")])

constellations = []

for star in data:
    new = [star]
    new_constellations = []
    for constellation in constellations:
        if in_const(star, constellation):
            new += constellation
        else:
            new_constellations.append(constellation)
    new_constellations.append(new)
    constellations = new_constellations

print(len(constellations))





