
width = 50
height = 6

data = {}


for i in range(width):
    for j in range(height):
        data[(i,j)] = False

def rect (n,m, data):
    for i in range(n):
        for j in range(m):
            data[(i,j)]=True
    return data

def rot_row(y,n,data):
    new_data = {}
    for i in range(width):
        new_data[(i,y)] = data[((i-n)%width,y)]
    for i in range(width):
        data[(i,y)] = new_data[(i,y)]
    return data

def rot_col(x,n,data):
    new_data = {}
    for i in range(height):
        new_data[(x,i)] = data[(x,(i-n)%height)]
    for i in range(height):
        data[(x,i)] = new_data[(x,i)]
    return data

def display(data):
    for j in range(height):
        out = ""
        for i in range(width):
            if data[(i,j)]:
                out += "#"
            else:
                out += "."
        print(out)



with open("input_08.txt") as file:
    for line in file:
        op = line.strip().split()
        if op[0] == 'rect':
            n,m = op[1].split('x')
            data = rect(int(n),int(m),data)
        elif op[1] == 'row':
            y = op[2][2:]
            data = rot_row(int(y),int(op[4]),data)
        elif op[1] == 'column':
            x = op[2][2:]
            data = rot_col(int(x),int(op[4]),data)

count = len([x for x in data if data[x]])
print(count)

display(data)

