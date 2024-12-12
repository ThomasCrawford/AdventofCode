

def find_row(string):
    string = string.replace("F","0")
    string = string.replace("B","1")
    return int(string,2)

def find_col(string):
    string = string.replace("L","0")
    string = string.replace("R","1")
    return int(string,2)

def find_id(string):
    row = find_row(string[:7])
    col = find_col(string[7:])
    return row*8+col


data = []
with open("input05.txt") as file:
    for line in file:
        data.append(line.strip())

ids = [find_id(x) for x in data]
ans1 = max(ids)
print(ans1)

for x in range(min(ids), max(ids)):
    if x not in ids:
        print(x)

