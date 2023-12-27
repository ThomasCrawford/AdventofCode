import re

def sum_string(string):
    regex = r'-?\d+'
    return sum([int(x) for x in re.findall(regex,string)])

#together with find_open, finds the indices corresponding to the block containing\
# something that is "red" 

def find_close(string,index):
    level = 1
    while level:
        if string[index] == "{":
            level += 1
        elif string[index] == "}":
            level -= 1
        index += 1
    return index

def find_open(string,index):
    level = -1
    while level:
        assert index > 0, string
        if string[index] == "{":
            level += 1
        elif string[index] == "}":
            level -= 1
        index -= 1
    return index

def remove_red(string):
    while string.find(":\"red\"")>0:
        red_index = string.find(":\"red\"")
        start = find_open(string, red_index)
        end = find_close(string, red_index)
        string = string[:start] + string[end:]
    return string

with open("input_12.txt") as file:
    for line in file:
        print(f'Part 1: {sum_string(line.strip())}')
        print(f'Part 2: {sum_string(remove_red(line))}')
