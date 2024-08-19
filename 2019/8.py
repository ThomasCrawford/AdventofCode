
width = 25
height = 6


def color(position, levels):
    if levels[0][position] == "2":
        return color(position, levels[1:])
    else:
        return levels[0][position]


with open("input8.txt") as file:
    for line in file:
        data = line.strip()

pixel_count = width*height
levels = [data[i: i + pixel_count] for i in range(0, len(data), pixel_count)]

#Part 1
counts = [[x.count("0"), x.count("1"), x.count("2")] for x in levels]
counts.sort()
print(counts[0][1]*counts[0][2])


# Part 2
disp = [color(position, levels) for position in range(pixel_count)]

for _ in range(height):
    out = ""
    for _ in range(width):
        x = disp.pop(0)
        out += "#" if x == "1" else "."
    print(out)
