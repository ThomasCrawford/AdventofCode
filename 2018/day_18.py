import cmath


def iterate(state):
    directions = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
    new_state = {}
    for p in state:
        if state[p] == "." and len([d for d in directions if state.get(p+d) == "|" ]) >=3:
            new_state[p] = "|"
        elif state[p] == "|" and len([d for d in directions if state.get(p+d) == "#" ]) >=3:
            new_state[p] = "#"
        elif state[p] == "#" and (not any([d for d in directions if state.get(p+d) == "|" ]) \
                                or not any([d for d in directions if state.get(p+d) == "#" ]) ):
            new_state[p] = "."
        else:
            new_state[p] = state[p]
    return new_state

# def display(state):

#     os.system('cls' if os.name == 'nt' else 'clear')
#     y_max = int(max([z.imag for z in state]))
#     x_max = int(max([z.real for z in state]))
#     for y in range(y_max+1):
#         out = ""
#         for x in range(x_max+1):
#             out += state[x+y*1j]
#         print(out)
#     print("")


def main(state, gens):
    for _ in range(gens):
        state = iterate(state)
    ans = len([z for z in state if state[z] =="|"])*len([z for z in state if state[z] =="#"])
    return ans


def find_cycle(state, max_iterations):
    seen = {}
    for i in range(max_iterations):
        state = iterate(state)
        if state in seen.values():
            start = [k for k in seen if seen[k] == state][0]
            return start, i
        else:
            seen[i] = state


state = {}

with open("input_18.txt") as file:
    for y, line in enumerate(file):
        for x, v in enumerate(line.strip()):
            state[x + y*1j] = v

#Part 1
print(f'Part 1: {main(state, 10)}')


#Part 2

goal = 1000000000 
start, end = find_cycle(state, 100000)
goal = (goal - start) % (end-start) + start

print(f'Part 2: {main(state, goal)}')




