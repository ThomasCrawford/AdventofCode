

def step (state):
    new_state = state
    instruction = instructions[state[2]]
    match instruction[0]:
        case 'hlf':
            register = instruction[1]
            new_state[register] = state[register]//2
        case 'tpl':
            register = instruction[1]
            new_state[register] = state[register]*3
        case 'inc':
            register = instruction[1]
            new_state[register] = state[register]+1
        case 'jmp':
            new_state[2] += instruction[1]
            return new_state
        case 'jie':
            register = instruction[1]
            if new_state[register]%2 == 0:
                new_state[2] += instruction[2]
                return new_state
        case 'jio':
            register = instruction[1]
            if new_state[register] == 1:
                new_state[2] += instruction[2]
                return new_state
    new_state[2] += 1
    return new_state

instructions = []
with open("input_23.txt") as file:
    for line in file:
        match line[:3]:
            case 'hlf'|'tpl'|'inc':
                x, t = line.strip().split(' ')
                if t == "a":
                    register = 0
                else:
                    register = 1
                instructions.append([x, register])
            case 'jmp':
                x, s = line.strip().split(' ')
                instructions.append([x, int(s)])
            case 'jio'|'jie':
                x, t, s = line.strip().split(' ')
                assert t in ['a,','b']
                if t == "a,":
                    register = 0
                elif t == 'b':
                    register = 1
                instructions.append([x, register, int(s)])


# a, b, line
state1 = [0,0,0]
while state1[2]<len(instructions):
    state1 = step(state1)
print(f'Part 1: {state1[1]}')

state2 = [1,0,0]
while state2[2]<len(instructions):
    state2 = step(state2)
print(f'Part 2: {state2[1]}')
