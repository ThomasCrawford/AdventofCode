
def run (line, registers):
    expression = str(registers[line[4]]) +line[5] + line[6]
    if eval(expression):
        if line[1] == 'inc':
            registers[line[0]] += int(line[2])
        elif line[1] == 'dec':
            registers[line[0]] -= int(line[2])
    return registers

data = []
registers = {}
with open("input_08.txt") as file:
    for line in file:
        data.append(line.strip().split())
        registers[line.split()[0]] = 0

ans2 = 0
for line in data:
    registers = run(line,registers)
    ans2 = max([ans2, max(registers.values())])

ans1 = max(registers.values())
print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')



