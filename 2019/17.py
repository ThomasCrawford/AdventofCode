from intcode13 import Intcode
from collections import defaultdict
import cmath

def def_value():
    return 0

def disp(data):
    out = ""
    for x in data:
        out += chr(x)
    print(out)

def compress(string):
    for a_len in range(1,20):
        s = str(string)
        a_word = s[:a_len]
        substrings = [x for x in s.split(a_word) if x != ""]
        for b_len in range(2,min(21,len(substrings[0])+1)):
            b_word = substrings[0][:b_len]
            sub_substrings = [substring.split(b_word) for substring in substrings]
            just_sub_substrings = list(set([x for y in sub_substrings for x in y if x != ""]))
            if len(just_sub_substrings) == 1 and len(just_sub_substrings[0])<21:
                out = str(string)
                out = out.replace(a_word,"A,")
                out = out.replace(b_word,"B,")
                out = out.replace(just_sub_substrings[0],"C,")
                return out[:-1], a_word[:-1], b_word[:-1], just_sub_substrings[0][:-1]



with open("input17.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

bot = Intcode(data,[])
bot.run()

# disp(bot.output)

scaffolds = set()
x = 0
y = 0
for v in bot.output:
    if v == 46:
        x +=1
    elif v == 10:
        x = 0
        y += 1
    elif v == 35:
        scaffolds.add(x+y*1j)
        x +=1
    elif chr(v) in ["^","v","<",">"]:
        p = x+y*1j
        d = -1j
        x += 1

ans1 = 0
directions = [1,-1,1j,-1j]
for p1 in scaffolds:
    if all([p1+d in scaffolds for d in directions]):
        ans1 += p1.real*p1.imag
print(f'Part 1: {int(ans1)}')


# Part 2

with open("input17.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]
data[0] = 2

# Generate path
path = []
step_count = 0
while True:
    if p+d not in scaffolds:
        path.append(step_count)
        step_count = 0
        if p+ (d*1j) in scaffolds:
            path.append("R")
            d *= 1j
        elif p+(d*-1j) in scaffolds:
            path.append("L")
            d *= -1j
        else:
            break
    elif p + d in scaffolds:
        step_count += 1
        p = p+d

#Convert path to compressed instructions, then to ascii codes for robot
string = ""
for i in path[1:]:
    string += str(i) + ","
path_orders = compress(string)
# print(path_orders)

to_robot = ""
for line in path_orders:
    to_robot += line
    to_robot += "\n"
to_robot += "n\n"
to_robot_ascii = [ord(x) for x in to_robot]

# Booting up robot
data[0] = 2

bot = Intcode(data, to_robot_ascii)


bot.run()
# disp(bot.output)
print(f'Part 2: {bot.output[-1]}')





