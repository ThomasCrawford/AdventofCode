
data = []
with open("input_24.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip().split("/")])


def max_strength(remaining_components, port):
    poss_strengths = 0
    for component in remaining_components:
        if port in component:
            new_components = [x for x in remaining_components if x != component]
            strength = sum(component)
            new_port = component[1] if component[0] == port else component[0]
            strength_remaining = max_strength(new_components, new_port)
            poss_strengths = max(poss_strengths, strength_remaining + strength)
    return poss_strengths

print(f'Part 1: {max_strength(data, 0)}')

def find_max_length(remaining_components, port):
    length = 0
    for component in remaining_components:
        if port in component:
            new_components = [x for x in remaining_components if x != component]
            new_port = component[1] if component[0] == port else component[0]
            additional_components_remaining = find_max_length(new_components, new_port)
            length = max(length, additional_components_remaining + 1)
    return length

def max_strength_of_length(remaining_components, port, req_length):
    poss_strengths = 0
    for component in remaining_components:
        if port in component:
            new_components = [x for x in remaining_components if x != component]
            strength = sum(component)
            new_port = component[1] if component[0] == port else component[0]
            strength_remaining = max_strength_of_length(new_components, new_port, req_length - 1)
            poss_strengths = max(poss_strengths, strength_remaining + strength)
    if poss_strengths == 0 and req_length != 0:
        poss_strengths = -10000
    # print(f'Calling {remaining_components, port, req_length} yields {poss_strengths}')
    return poss_strengths

target_length =find_max_length(data, 0)
print(f'longest is: {target_length}')
ans2 = max_strength_of_length(data, 0, target_length)
print(f'Part 2: {ans2}')


