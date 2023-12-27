#137 too low
# 138 low
#168 low

import re
from termcolor import colored

def get_replacement_indices(rule, word):
    return [(match.start(), match.end()) for match in re.finditer(rule[0], word)]

def all_new_words(word, rules):
    new_molecules = set()
    for rule in rules:
        for s_index, e_index in get_replacement_indices(rule, word):
            new_word = word[:s_index] + rule[1] + word[e_index:]
            new_molecules.add(new_word)
    return new_molecules


with open("input_19.txt") as file:
    lines = file.readlines()

forward_rules = []
reverse_rules = []
separator_index = lines.index('\n')
for line in lines[:separator_index]:
    a,b = line.strip().split(" => ")
    forward_rules.append([a,b])
    reverse_rules.append([b,a])

molecule = lines[separator_index + 1].strip()

# Part 1
new_molecules = all_new_words(molecule, forward_rules)
print(f'Part 1: {len(new_molecules)}')

#Part 2

def split_chemicals(compound):
    elements = []
    i = 0
    while i < len(compound):
        # If the next character exists and is lowercase, it's a two-letter element
        if i + 1 < len(compound) and compound[i+1].islower():
            elements.append(compound[i:i+2])
            i += 2  # Skip the next character as it's part of the two-letter element
        else:
            elements.append(compound[i])
            i += 1
    return elements

possible_to_replace = set([rule[0] for rule in forward_rules])
forever_molecules = set()

for rule in forward_rules:
    for out in split_chemicals(rule[1]):
        if out not in possible_to_replace:
            forever_molecules.add(out)


answer2 = len(split_chemicals(molecule))-split_chemicals(molecule).count('Ar')*2 - split_chemicals(molecule).count('Y')*2 -1
print(f'Part 2: {answer2}')


## Investigating the "Rules":

# if all replacements were 1->2, answer would be len(molecule) - 1
# Each Ar and Rn pair reduces by 2
# Each Y reduces by 2
# C's don't affect


# print (possible_to_replace)
# print(forever_molecules)


# for rule in forward_rules:
#     out = ""
#     for x in split_chemicals(rule[1]):
#         if x =="Ar":
#             out += colored(x,'red')
#         elif x == "Rn":
#             out += colored(x,'blue')
#         elif x in ['Y','C']:
#             out += colored(x,'green')
#         else:
#             out += x

#     print( rule[0], out, len(split_chemicals(rule[1])))

# out = ""
# for x in split_chemicals(molecule):
#     if x =="Ar":
#         out += colored(x,'red')
#     elif x == "Rn":
#         out += colored(x,'blue')
#     elif x in ['Y','C']:
#         out += colored(x,'green')
#     else:
#         out += x
# print(out)


# print(len(forward_rules))
# print(len(set([rule[1] for rule in forward_rules])))
#     # is_forever = set(split_chemicals(rule[1])).issubset(possible_to_replace)
#     # print(rule, is_forever)



# for x in forever_molecules:
#     num = split_chemicals(molecule).count(x)
#     print(x, num)

# print(len(split_chemicals(molecule)))



