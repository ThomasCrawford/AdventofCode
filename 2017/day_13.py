
def run(data, delay):
    severity = 0
    for i in data.keys():
        if (i+delay) % (2*data[i] -2) == 0:
            severity += i*data[i]
    return severity

def fast_run(data,delay):
    for i in data.keys():
        if (i+delay) % (2*data[i] -2) == 0:
            return False
    return True

data = {}
with open("input_13.txt") as file:
    for line in file:
        line = [int(x) for x in line.strip().split(": ")]
        data[line[0]] = line[1]

print(f'Part 1: {run(data,0)}')

for i in range(10000000):
    if fast_run(data,i):
        print(f'Part 2: {i}')
        quit()
