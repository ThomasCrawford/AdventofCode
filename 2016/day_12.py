import time
start_time = time.time()

x = 0
a = 0
b = 0
c = 1
d = 0


data = []
with open("input_12.txt") as file:
    for line in file:
        data.append(line.strip().split())

def get_value(x):
    try:
        return(int(x))
    except:
        return globals()[x]

while x < len(data):
    # if x == 13:
    #     print(x, a,b,c,d)
    match data[x][0]:
        case 'cpy':
            globals()[data[x][2]] = get_value(data[x][1])
            x +=1
        case 'inc':
            globals()[data[x][1]] +=1
            x +=1
        case 'dec':
            globals()[data[x][1]] -=1
            x +=1
        case 'jnz':
            # print(data[x])
            if get_value(data[x][1]) != 0:
                x += get_value(data[x][2])
            else:
                x +=1


print(a)

# print("--- %s seconds ---" % (time.time() - start_time))