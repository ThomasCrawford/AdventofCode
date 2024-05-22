import copy 


def spin(state, x):
    return state[-x:] + state[:-x]

def exchange(state,a,b):
    # print(a,b)
    new_state = copy.deepcopy(state)
    new_state[a] = state[b]
    new_state[b] = state[a]
    return new_state

def partner(state,a,b):
    new_state = copy.deepcopy(state)
    i = state.index(a)
    k = state.index(b)
    new_state[i] = state[k]
    new_state[k] = state[i]
    return new_state

def loop(state, data):
    for line in data:
        match line[0]:
            case 's':
                state = spin(state,int(line[1:]))
            case 'x':
                a,b = line[1:].split('/')
                state = exchange(state, int(a), int(b))
            case 'p':
                a,b = line[1:].split('/')
                state = partner(state, a, b)
    return state

def main():
    data = []
    with open("input_16.txt") as file:
        for line in file:
            data = line.strip().split(',')

    state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

    state = loop(state,data)
    print("".join(state))

    #Part 2
    init = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    state = copy.deepcopy(init)
    for i in range(1000000):
        state = loop(state,data)
        if state == init:
            orbit = i+1
            break
    for _ in range(1000000000%orbit):
        state = loop(state,data)
    print("".join(state))



if __name__ == '__main__':
    main()