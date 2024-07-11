import re



opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

def evaluate(nums, opcode, abc):
    registers = {0:nums[0], 1:nums[1], 2:nums[2], 3:nums[3]}
    A, B, C = abc
    match opcode:
        case "addr":
            registers[C] = registers[A] + registers[B]
        case "addi":
            registers[C] = registers[A] + B
        case "mulr":
            registers[C] = registers[A] * registers[B]
        case "muli":
            registers[C] = registers[A] * B
        case "banr":
            registers[C] = registers[A] & registers[B]
        case "bani":
            registers[C] = registers[A] & B
        case "borr":
            registers[C] = registers[A] | registers[B]
        case "bori":
            registers[C] = registers[A] | B
        case "setr":
            registers[C] = registers[A]
        case "seti":
            registers[C] = A
        case "gtir":
            registers[C] = 1 if A > registers[B] else 0
        case "gtri":
            registers[C] = 1 if registers[A] > B else 0
        case "gtrr":
            registers[C] = 1 if registers[A] > registers[B] else 0
        case "eqir":
            registers[C] = 1 if A == registers[B] else 0
        case "eqri":
            registers[C] = 1 if registers[A] == B else 0
        case "eqrr":
            registers[C] = 1 if registers[A] == registers[B] else 0
    return list(registers.values())


def is_valid(rule, opcode):
    return rule[2] == evaluate(rule[0], opcode, rule[1][1:])




program = []
with open("input_16.txt") as file:
    content = file.read()
    a,b = content.split("\n\n\n\n")
    rules = []
    for rule in a.split("\n\n"):
        rules.append([[int(x) for x in re.findall(r'\d+',line)] for line in rule.split("\n")])
    program = ([[int(x) for x in line.split()] for line in b.split("\n")])[:-1]


ans1 = 0
for rule in rules:
    c = rule[1][0]
    valid = [opcode for opcode in opcodes if is_valid(rule, opcode)]
    if len(valid)>2:
        ans1+=1
print(f'Part 1: {ans1}')



# Part 2
matches = {x: set(opcodes) for x in range(16)}

for rule in rules:
    c = rule[1][0]
    invalid = [opcode for opcode in matches[c] if not is_valid(rule, opcode)]
    for opcode in invalid:
        matches[c].discard(opcode)

while any([len(matches[x]) > 1 for x in matches]):
    solved = [list(x)[0] for x in matches.values() if len(x) == 1]
    unsolved = [x for x in matches if len(matches[x])>1]
    for s in solved:
        for u in unsolved:
            matches[u].discard(s)

#Final dictionary to look up opcodes
matches = {x:list(matches[x])[0] for x in matches}


# Run the program
values = [0,0,0,0]
for line in program:
    values = evaluate(values, matches[line[0]], line[1:])

ans2 = values[0]
print(f'Part 2: {ans2}')


