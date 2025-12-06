import math

def calc(lis):
    oper = lis[-1]
    if oper == "*":
        return math.prod([int(x) for x in lis[:-1]])
    elif oper == "+":
        return sum([int(x) for x in lis[:-1]])

data = []
with open("6.txt") as file:
    for line in file:
        data.append(line.strip().split())

ans1 = sum([calc(line) for line in zip(*data)])
print(ans1)



#Part 2

def reformat(line):
    if all([x==" " for x in line]):
        return False
    op = line[-1].strip()
    nums = line[:-1]
    number = int("".join([char.strip() for char in nums]))
    return number, op

data = []
with open("6.txt") as file:
    for line in file:
        data.append(list(line[:-1]))
data[-1].append(" ")


transposed = [reformat(x) for x in zip(*data)]


ans2 = 0
running = 0
oper = False
for line in transposed:
    if not line:
        ans2 += running
        oper = False
        running = 0
    else:
        if not oper:
            oper = line[-1]
            running = line[0]
        elif oper == "+":
            running += line[0]
        elif oper == "*":
            running *= line[0]
ans2 += running

print(ans2)


