import time, copy
start_time = time.time()




# dic = {'a':0,'b':1,'c':2,'d':3}

data = []
with open("input_25.txt") as file:
    for line in file:
        data.append(line.strip().split())

def get_value(x, registers):
    try:
        return(int(x))
    except:
        return registers[x]


def test_jzn_shortcut(current, jump_target, data):
    if jump_target >= current:
        return False
    for i in range(jump_target,current):
        if data[i][0] not in ['inc','dec']:
            return False
    return True

def jzn_alt(current,var, jump_target, data, registers):
    one_trip = {'a':0,'b':0,'c':0,'d':0}
    for row in data[jump_target:current]:
        if row[0] == "inc":
            one_trip[row[1]] += 1
        elif row[0] == "dec":
            one_trip[row[1]] -= 1
    n = -1*registers[var]//one_trip[var]
    n_trips = {}
    for i in one_trip:
        n_trips[i] = n*one_trip[i]
    return n_trips

def test_jzn_shortcut2(current,jump_target,data):
    if current - jump_target != 5:
        return False
    these_inst = [line[0] for line in data[jump_target:current]]
    if these_inst != ["cpy","inc","dec","jnz","dec"]:
        return False
    return True

def dict_hash(dic):
    return hash(tuple(sorted(dic.items())))


def main(data,initial_a):
    x = 0
    registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0, 'output':0}
    seen_state_at_out = set()
    out_successes = 0
    while x < len(data):
        # print(x, registers, data[x])
        match data[x][0]:
            case 'cpy':
                registers[data[x][2]] = get_value(data[x][1], registers)
                x +=1
            case 'inc':
                registers[data[x][1]] +=1
                x +=1
            case 'dec':
                registers[data[x][1]] -=1
                x +=1
            case 'jnz':
                if get_value(data[x][1],registers) != 0:
                    target = x + get_value(data[x][2],registers)
                    if test_jzn_shortcut2(x,target,data) and x == 7:
                        registers['d'] = registers['d'] + 365*registers['c']
                        registers['c'] = 0
                        registers['b'] = 0
                        x += 1
                    elif test_jzn_shortcut2(x,target,data) and x == 9:
                        registers['a'] = registers['a'] + registers['b']*registers['d']
                        registers['c'] = 0
                        registers['d'] = 0
                        x += 1
                    elif test_jzn_shortcut(x,target,data):
                        n_trips = jzn_alt(x,data[x][1],target, data, registers)
                        for i in n_trips:
                            registers[i] += n_trips[i]
                        x += 1 
                    else:
                        x += get_value(data[x][2],registers)
                else:
                    x +=1
            case 'tgl':
                try:
                    target = get_value(data[x][1],registers) + x 
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
                except IndexError:
                    pass
                x +=1
            case 'out':
                out_successes += 1
                if registers['b'] != registers['output']:
                    return False
                if dict_hash(registers) in seen_state_at_out:
                    return True
                seen_state_at_out.add(dict_hash(registers))
                registers['output'] = not registers['output']

                x+=1
    # return registers


i = 0
while not main(data,i):
    i += 1
print(i)


print("--- %s seconds ---" % (time.time() - start_time))