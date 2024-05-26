import cmath

import time
start_time = time.time()

graph_height = 25
graph_width = 60

def step2(carrier, data, count):
    if carrier[0] not in data or data[carrier[0]] == 0 :
        data[carrier[0]] = 0
        carrier[1] *= 1j
    elif data[carrier[0]] == 1:
        count += 1
    elif data[carrier[0]] == 2:
        carrier[1] *= -1j
    elif data[carrier[0]] == 3:
        carrier[1] *= -1
    data[carrier[0]] = (data[carrier[0]] + 1) % 4
    carrier[0] += carrier[1]
    return carrier, data, count

def step1(carrier, data, count):
    if carrier[0] not in data or data[carrier[0]] == 0:
        data[carrier[0]] = 2
        carrier[1] *= 1j
        count +=1
    elif data[carrier[0]] == 2:
        data[carrier[0]] = 0
        carrier[1] *= -1j
    carrier[0] += carrier[1]
    return carrier, data, count



carrier = [0,1j]
count = 0
data = {}
with open("test.txt") as file:
    for y,line in enumerate(file):
        d = len(line.strip())//2
        for x,v in enumerate(line):
            if v == "#":
                data[x-d + -1*(y-d)*1j] = 2
            else:
                data[x-d + -1*(y-d)*1j] = 0

def graph(data):
    out = ""
    for y in range(-1*graph_height,graph_height)[::-1]:
        line = ""
        for x in range(-1*graph_width,graph_width):
            if x+y*1j not in data or data[x+y*1j] == 0:
                if carrier[0] == x + y*1j:
                    line += "O"
                else:
                    line += "."
            elif data[x+y*1j] == 2:
                if carrier[0] == x + y*1j:
                    line += "0"
                else:
                    line += "#"
            elif data[x+y*1j] == 1:
                if carrier[0] == x + y*1j:
                    line += "0"
                else:
                    line += "W"
            elif data[x+y*1j] == 3:
                if carrier[0] == x + y*1j:
                    line += "0"
                else:
                    line += "F"
        out += line + "\n"
    print(out)


for i in range(10000000):
    carrier, data, count = step1(carrier, data, count)
    if i%100000 == 0:
        print(i)
    graph(data)

# print(len(data))
print(count)

print("--- %s seconds ---" % (time.time() - start_time))

