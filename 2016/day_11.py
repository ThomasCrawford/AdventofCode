import re
import itertools
import copy

translate = {"polonium": 1,
        "thulium": 2,
        "promethium": 3,
        "ruthenium": 4,
        "cobalt": 5,
        }


elevator = 0 


def is_one_valid(state,n):
    if state[n][0]==state[n][1]:
        return True
    elif any([state[n][1]== other[0] for other in state[1:]]):
        return False
    else:
        return True

def is_valid(state):
    return all([is_one_valid(state,i) for i in range(1,6)])


def remove_duplicates(states):
    unique_states = []
    seen = set()
    
    for state in states:
        # Sort each state to make sure order of inner lists doesn't matter
        # Convert inner lists to tuples
        sorted_state = tuple(sorted(tuple(x) for x in state))
        
        # Check if this sorted state has not been seen before
        if sorted_state not in seen:
            seen.add(sorted_state)
            unique_states.append(state)  # Append the original state to result
            
    return unique_states


def possible_moves(state):
    poss = []
    e = state[0][0]
    moveable_single = []
    for i in range(1,6):
        for j in range(2):
            if state[i][j]==e:
                moveable_single.append([i,j])
    moveable_pairs = list(itertools.combinations(moveable_single,2))
    if e < 3:
        for i,j in moveable_single:
            candidate = copy.deepcopy(state)
            candidate[0] = [e + 1]
            candidate[i][j] = e + 1
            if is_valid(candidate):
                poss.append(candidate)
        for [i,j], [i2,j2] in moveable_pairs:
            candidate = copy.deepcopy(state)
            candidate[0] = [e + 1]
            candidate[i][j] = e + 1
            candidate[i2][j2] = e + 1
            if is_valid(candidate):
                poss.append(candidate)
    if e > 0:
        for i,j in moveable_single:
            candidate = copy.deepcopy(state)
            candidate[0] = [e - 1]
            candidate[i][j] = e - 1
            if is_valid(candidate):
                poss.append(candidate)
        for [i,j], [i2,j2] in moveable_pairs:
            candidate = copy.deepcopy(state)
            candidate[0] = [e - 1]
            candidate[i][j] = e - 1
            candidate[i2][j2] = e - 1
            if is_valid(candidate):
                poss.append(candidate)
    poss = remove_duplicates(poss)
    return(poss)

def progress(collection_of_states):
    return max([sum([x for y in state for x in y]) for state in collection_of_states])



state = [[0],[9,9],[9,9],[9,9],[9,9],[9,9]]
end_state = [[3],[3,3],[3,3],[3,3],[3,3],[3,3]]
visited_states = [state]
current_gen = [state]

regex_gen = r'(\w+) generator'
regex_chip = r'(\w+)-compatible microchip'

with open("input_11.txt") as file:
    for i, line in enumerate(file):
        for gen in re.findall(regex_gen, line.strip()):
            state[translate[gen]][0] = i
        for chip in re.findall(regex_chip, line.strip()):
            state[translate[chip]][1] = i

for i in range(1,1000):
    nex_gen = []
    for s in current_gen:
        for move in possible_moves(s):
            if move not in visited_states:
                visited_states.append(move)
                nex_gen.append(move)
    # print(nex_gen)/
    current_gen = remove_duplicates(nex_gen)
    # print(current_gen)
    visited_states = remove_duplicates(visited_states)
    print(f'in generation {i} there are {len(current_gen)} possible next moves.  We have seen {len(visited_states)} states.  Biggest so far is {progress(visited_states)}')
    if end_state in visited_states:
        print(f'We reached the top in {i} moves!')
        quit()


# state1 = [[0],[0,0],[0,0],[0,0],[0,1],[0,1]]
# state2 = [[0,0],[0,0],[0,0],[0,1],[0,1],[0]]
# state3 = [[0,0],[0,0],[0,1],[0,1],[0,0],[0]]
# state4 = [[0,0],[0,0],[0,1],[0,1],[0,1],[0]]
# x = [state1, state2,state3,state4]
# y = remove_duplicates(x)

# for i in y:
#     print(i)

