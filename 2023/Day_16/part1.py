import cmath
# Right is the positive real direction, DOWN is the positive imag direction
import sys
sys.setrecursionlimit(10000)

def illuminate(location, direction):
    print(location, direction)
    if location not in data.keys():
            return
    elif direction in light[location]:
        return
    light[location].append(direction)
    if data[location] == "." or (data[location] == "|" and int(direction.imag)) or (data[location] == "-" and int(direction.real)):
            illuminate(location+direction, direction)
    elif data[location] == "\\":
        nd = direction.imag+ direction.real*1j
        illuminate(location + nd, nd)
    elif data[location] == "/":
        nd = -direction.imag - direction.real*1j
        illuminate(location + nd, nd)
    else:
        illuminate(location + direction*1j, direction*1j)
        illuminate(location + direction*-1j, direction*-1j)

data = {}
light = {}
with open("input.txt") as file:
    lines = [line.strip() for line in file]
for i in range(len(lines)):
    for k in range(len(lines[0])):
        data[k+i*1j] = lines[i][k]
for key in data.keys():
    light[key] = []

illuminate(0,1)


print(len([x[0] for x in light.values() if x]))

#print([key for key, x in light.items() if x])
#print(len(data))