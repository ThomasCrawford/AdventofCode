



def step(data):
    n = len(data)
    new = []
    for i in range(n):
        next_num = abs(sum([a*b for a,b in zip(data,patterns[i])]))%10
        new.append(next_num)
    return new

def disp(data):
    out = ""
    for x in data[:8]:
        out += str(x)
    print(out)


with open("input16.txt") as file:
    for line in file:
        orig_data = line.strip()
data = [int(x) for x in orig_data]

patterns = []
for i in range(len(data)):
    new_pattern = [0]*(i+1) + [1]*(i+1) + [0]*(i+1) + [-1]*(i+1)
    new_pattern = new_pattern*(len(data)//(4*(i+1)) +1)
    new_pattern = new_pattern[1:len(data)+2]
    patterns.append(new_pattern)


for _ in range(100):
    data = step(data)
disp(data)


#Part 2:

def step2(data):
    new_data = [data[-1]]
    for i in range(1,len(data)):
        new_data.append((new_data[-1] + data[-1-i])%10)
    new_data.reverse()
    return new_data


with open("input16.txt") as file:
    for line in file:
        orig_data = line.strip()
data = [int(x) for x in orig_data]

offset = int(orig_data[:7])
data = (data*10000)[offset:]

for _ in range(100):
    data = step2(data)
disp(data)



