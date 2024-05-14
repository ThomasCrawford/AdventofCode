import time
start_time = time.time()

x = 0
a = 12
b = 0
c = 0
d = 0




dic = {'a':0,'b':1,'c':2,'d':3}

data = []
with open("input_23.txt") as file:
    for line in file:
        data.append(line.strip().split())

def get_value(x):
    try:
        return(int(x))
    except:
        return globals()[x]


def test_jzn_shortcut(current, jump_target):
    if jump_target >= current:
        return False
    for i in range(jump_target,current):
        if data[i][0] not in ['inc','dec']:
            return False
    return True

def jzn_alt(current,var, jump_target):
    one_trip = {'a':0,'b':0,'c':0,'d':0}
    for row in data[jump_target:current]:
        if row[0] == "inc":
            one_trip[row[1]] += 1
        elif row[0] == "dec":
            one_trip[row[1]] -= 1
    n = -1*globals()[var]//one_trip[var]
    n_trips = {}
    for i in one_trip:
        n_trips[i] = n*one_trip[i]
    return n_trips

def test_jzn_shortcut2(current,jump_target):
    if current - jump_target != 5:
        return False
    these_inst = [line[0] for line in data[jump_target:current]]
    if these_inst != ["cpy","inc","dec","jnz","dec"]:
        return False
    return True



while x < len(data):
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
            if get_value(data[x][1]) != 0:
                target = x + get_value(data[x][2])
                if test_jzn_shortcut2(x,target) and x == 9:
                    a = a + b*d
                    c = 0
                    d = 0
                    x += 1
                elif test_jzn_shortcut(x,target):
                    n_trips = jzn_alt(x,data[x][1],target)
                    for i in n_trips:
                        globals()[i] += n_trips[i]
                    x += 1 
                else:
                    x += get_value(data[x][2])
            else:
                x +=1
        case 'tgl':
            try:
                target = get_value(data[x][1]) + x 
                if len(data[target]) == 2:
                    if data[target][0] == 'inc':
                        data[target][0] = 'dec'
                    else:
                        data[target][0] = 'inc'
                else:
                    if data[target][0] == 'jnz':
                        data[target][0] = 'cpy'
                    else:
                        data[target][0] = 'jnz'
                # print(target, data[target])
            except IndexError:
                pass
            x +=1


print(a)

print("--- %s seconds ---" % (time.time() - start_time))