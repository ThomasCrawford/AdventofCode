

data = []
count1 = 0
count2 = 0
with open("input_04.txt") as file:
    for line in file:
        d = line.strip().split()
        if len(d) == len(set(d)):
            count1 +=1
        d2 = [str(sorted(x)) for x in d]
        if len(d) == len(set(d2)):
            count2 +=1
print(count1, count2)
