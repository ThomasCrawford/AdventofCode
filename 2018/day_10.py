import re

regex = r'-?\d+'

def find_time(data):
    xs = [p[0] for p in data]
    vs = [p[2] for p in data]
    new_r = max(xs) - min(xs)
    old_r = new_r
    t = 0

    while new_r <= old_r:
        t += 1
        old_r = new_r
        xs = [sum(x) for x in zip(xs, vs)]
        new_r = max(xs) - min(xs)

    return t - 1

def display(data, t):
    to_display = [[p[0] + t* p[2], p[1] + t*p[3]] for p in data]
    x_min = min([p[0] for p in to_display])
    x_max = max([p[0] for p in to_display])
    y_min = min([p[1] for p in to_display])
    y_max = max([p[1] for p in to_display])
    for y in range(y_min, y_max +1):
        out = ""
        for x in range(x_min, x_max+1):
            if [x,y] in to_display:
                out += "#"
            else:
                out += "."
        print(out)

data = []
with open("input_10.txt") as file:
    for line in file:
        values = re.findall(regex, line)
        data.append([int(x) for x in values])

time = find_time(data)
display(data, time)
print(time)




