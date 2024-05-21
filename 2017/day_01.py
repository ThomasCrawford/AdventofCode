


data = []
with open("input_01.txt") as file:
    for line in file:
        data.append(line.strip())

def main():
    count1 = 0
    count2 = 0
    for line in data:
        count1 += sum([int(x) for i,x in enumerate(line) if x == line[(i + 1)%len(line)]])
        count2 += sum([int(x) for i,x in enumerate(line) if x == line[(i + len(line)//2)%len(line)]])
    return count1, count2



print(main())
