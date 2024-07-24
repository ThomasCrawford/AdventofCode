import re
import math


opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

def evaluate(nums, opcode, abc):
    registers = {0:nums[0], 1:nums[1], 2:nums[2], 3:nums[3], 4:nums[4], 5:nums[5]}
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


## inspection of program translates to:
#generate r2 (using bottom half of rules), not sure how this is done
# count = 0
# for r4 in range(r2+1):
#     for r5 in range(r2):
#         if r4*r5 == r2:
#             count += r4

## Aka, sum of divisors of r2


def sum_of_divisors(n):
    divisors = []
    for i in range(1,int(math.sqrt(n))):
        if n%i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return sum(divisors)



program = []
with open("input_19.txt") as file:
    for line in file:
        if line[0] == "#":
            r = [int(x) for x in re.findall(r'\d+',line)][0]
        else:
            l = line.strip().split()
            program.append(l[:1] + [int(x) for x in l[1:]])


# Run the program
values = [0,0,0,0,0,0]

for _ in range(30):
    rule = program[values[r]]
    values = evaluate(values, rule[0], rule[1:])
    values[r]+=1
    # print(values)

n = values[2]
print(sum_of_divisors(n))



# Run the program
values = [1,0,0,0,0,0]

for _ in range(30):
    rule = program[values[r]]
    values = evaluate(values, rule[0], rule[1:])
    values[r]+=1
    # print(values)

n = values[2]
print(sum_of_divisors(n))
