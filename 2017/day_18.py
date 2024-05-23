import time


def get_value(letter, registers):
    if letter in registers:
        return registers[letter]
    else:
        return int(letter)

def step(line, registers):
    match line[0]:
        case 'set':
            registers[line[1]] = int(get_value(line[2], registers))
        case 'add':
            registers[line[1]] += get_value(line[2], registers)
        case 'mul':
            registers[line[1]] *= get_value(line[2], registers)
        case 'mod':
            registers[line[1]] %= get_value(line[2], registers)
        case 'jgz':
            if get_value(line[1], registers) > 0:
                registers['position'] += get_value(line[2], registers)
                return registers
        case 'snd':
            registers['sound'] = get_value(line[1], registers)
        case 'rcv':
            if get_value(line[1], registers) > 0:
                print(registers['sound'])
                quit()

    registers['position'] += 1
    return registers




def main():
    start_time = time.time()

    registers = {}
    registers['position'] = 0
    registers['sound'] = 0
    data = []
    with open("input_18.txt") as file:
        for line in file:
            line = line.strip().split()
            data.append(line)
            if not line[1].isnumeric():
                registers[line[1]] = 0

    while True:
        registers = step(data[registers['position']], registers)

if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))