

start = 5

with open("input5.txt") as file:
    for line in file:
        inp = [int(x) for x in line.strip().split(',')]

def step(data, cursor):
    code = data[cursor]
    opcode = code%100

    try:
        i = cursor + 1 if (code%1000)//100 == 1 else data[cursor + 1]
        d1 = data[i]
    except IndexError:
        pass

    try:
        i = cursor + 2 if (code%10000)//1000 == 1 else data[cursor + 2]
        d2 = data[i]
    except IndexError:
        pass

    try:
        i = cursor + 3 if (code%100000)//10000 == 1 else data[cursor + 3]
        d3 = data[i]
    except IndexError:
        pass

    if opcode == 1:
        data[data[cursor + 3]] = d1 + d2
        cursor += 4
    elif opcode == 2:
        data[data[cursor + 3]] = d1 * d2
        cursor += 4
    elif opcode == 3: # Input
        data[data[cursor + 1]] = int(start)
        cursor += 2
    elif opcode == 4: #Output
        print(f'OUTPUT: {d1}')
        cursor += 2
    elif opcode == 5: #Jump if True
        if d1:
            cursor = d2
        else:
            cursor += 3
    elif opcode == 6: # Jump if False
        if not d1:
            cursor = d2
        else:
            cursor += 3
    elif opcode == 7: # Less than
        data[data[cursor + 3]] = 1 if d1 < d2 else 0
        cursor += 4
    elif opcode == 8: # Equals
        data[data[cursor + 3]] = 1 if d1 == d2 else 0
        cursor += 4
    else:
        return data, -1
    return data, cursor

def run(data):
    cursor = 0
    while cursor>=0:
        data, cursor = step(data,cursor)

run(inp)
