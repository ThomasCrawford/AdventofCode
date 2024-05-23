
steps = 335

def run(steps, ending):
    state = [0]
    position = 0
    for i in range(1,ending +1):
        position = (position + steps)%i 
        state = state[:position+1] + [i] + state[position+1:]
        position += 1
    return state[position+1]

def run_lean(steps, ending):
    position = 0
    for i in range(1, ending+1):
        position = (position + steps) % i +1
        if position == 1:
            current = i
    return current

ans1 = run(steps,2017)
print(f'Part 1: {ans1}')

ans2 = run_lean(steps, 50000000)
print(f'Part 2: {ans2}')

