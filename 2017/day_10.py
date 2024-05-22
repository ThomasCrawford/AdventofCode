import copy
marks = 256


def flip(data, current, length):
    new_data = copy.deepcopy(data)
    for i in range(length):
        new_data[(current + i)%marks] = data[(current + length - i - 1)%marks]
    return new_data

def one_round(data, state, current, skip_size):
    for x in data:
        state = flip(state,current,x)
        current = current + skip_size + x
        skip_size += 1
    return state, current, skip_size

def sixtyfour(data):
    state = [x for x in range(256)]
    current = 0
    skip_size = 0
    for _ in range(64):
        state, current, skip_size = one_round(data, state, current, skip_size)
    return state

def xor(lis):
    result = 0
    for x in lis:
        result ^= x 
    return result

def condense(state):
    out = []
    for i in range(16):
        x = hex(xor(state[16*i:16*(i+1)]))[2:]
        if len(x) ==2:
            out.append(x)
        elif len(x) == 1:
            out.append("0"+x)
    return out

def encode(data):
    x = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    return "".join(condense(sixtyfour(x)))


def main():
    #Part 1
    data = []
    state = [x for x in range(marks)]
    current = 0
    skip_size = 0

    with open("input_10.txt") as file:
        for line in file:
            data = [int(x) for x in line.strip().split(",")]

    state = one_round(data, state, current, skip_size)[0]

    print(f'Part 1: {state[0]*state[1]}')



    #Part 2
    to_be_encoded = []
    with open("input_10.txt") as file:
        for line in file:
            to_be_encoded = line.strip()

    print(f'Part 2: {encode(to_be_encoded)}')

if __name__ == '__main__':
    main()





