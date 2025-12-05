def step(current, line):
    if line[0]=="R":
        return (current + int(line[1:]) ) % 100
    else:
        return (current - int(line[1:]) ) % 100

def step2(current, line):
    if line[0] == "R":
        new = current + int(line[1:])
    else:
        new = current - int(line[1:])
    if new < 1 or new >99:
        return new%100, abs(new//100)
    else:
        return new%100,0

data = []
with open("1.txt") as file:
    for line in file:
        data.append(line.strip())

dial = 50
count = 0
for line in data:
    dial = step(dial, line)
    if dial == 0: 
        count +=1

print(count)


dial = 50

count2 = 0
for line in data:
    amt = int(line[1:])
    if line[0]=="L":
        amt *= -1
    new = dial + amt

    if new == 0:
        count2 += 1
    elif new < 0 and dial == 0:
        count2 -= new//100 + 1
    elif new < 0:
        count2 -= (new-1)//100
    elif new >0:
        count2 += (new)//100
    dial = new %100

print(count2)