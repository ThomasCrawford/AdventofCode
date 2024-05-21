import copy

data = []
with open("input_05.txt") as file:
    for line in file:
        data.append(int(line.strip()))

def main1(data):
    count = 0
    x = 0
    while 0 <= x < len(data):
        newx = x + data[x]
        data[x] += 1
        x = newx
        count += 1
    return count

print(main1(copy.deepcopy(data)))

def main2(data):
    count = 0
    x = 0
    while 0 <= x < len(data):
        newx = x + data[x]
        if data[x] >=3:
            data[x] -= 1
        else:
            data[x] +=1
        x = newx
        count += 1
    return count

print(main2(copy.deepcopy(data)))