import re


regex = r'\[(\w+)\]'

regex_aba = r'(?=(.)(?!\1)(.)\1)'




def get_aba(word_list):
    abas = []
    for word in word_list:
        abas.append(re.findall(regex_aba,word))
    return abas
    # return [aba for aba in re.findall(regex_aba, line) for line in word_list]

def is_valid(line):
    in_brackets = re.findall(regex,line)
    babs = []
    for x in in_brackets:
        line = line.replace(f'[{x}]'," ")
    out_brackets = line.split()
    for word in out_brackets:
        babs += [match.group(2)+match.group(1)+match.group(2) for match in re.finditer(regex_aba, word)]
    for bab in babs:
        for word in in_brackets:
            for in_word in in_brackets:
                if bab in in_word:
                    return True
    return False

data = []
count = 0
with open("input_07.txt") as file:
    for line in file:
        if is_valid(line):
            count += 1


print(f'Part 2: {count}')