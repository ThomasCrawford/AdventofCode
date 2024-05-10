import re

regex = r'\[(\w+)\]'


def is_abba(word):
    n = len(word)
    for i in range(n-3):
        if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]:
            return True
    return False

def is_TLS(in_brackets, out_brackets):
    if any(is_abba(x) for x in out_brackets) and not any(is_abba(x) for x in in_brackets):
        return True
    return False

data = []
count = 0
with open("input_07.txt") as file:
    for line in file:
        in_brackets = re.findall(regex,line)
        for x in in_brackets:
            line = line.replace(f'[{x}]'," ")
        out_brackets = line.split()
        if is_TLS(in_brackets,out_brackets): 
            count +=1

print(f'Part 1: {count}')