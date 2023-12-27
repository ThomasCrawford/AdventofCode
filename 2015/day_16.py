import re

regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'


readout = {'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
    }

def check(category, num):
    if category in ['cats', 'trees']:
        return num > readout[category]
    elif category in ['pomeranians', 'goldfish']:
        return num < readout[category]
    else: 
        return num == readout[category]
    return False

data = []
with open("input_16.txt") as file:
    for line in file:
        num, cat1, n1, cat2, n2, cat3, n3 = re.match(regex, line.strip()).groups()
        if readout[cat1] == int(n1) and readout[cat2] == int(n2) and readout[cat3] == int(n3):
            print(f'Part 1: {num}')
        if check(cat1, int(n1)) and check(cat2,int(n2)) and check(cat3,int(n3)):
            print(f'Part 2: {num}')

