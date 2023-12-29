import re

regex = r'([a-z-]+)-(\d{3})\[[a-z]*([a-z]{5})\]'

def remove_duplicates_preserve_order(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def get_checksum(name):
    word = sorted(name, key=lambda x: (-name.count(x), x))
    check = remove_duplicates_preserve_order(word)
    check.remove('-')
    checksum = ""
    for letter in check[:5]:
        checksum += letter
    return checksum

def shift_letter(letter):
    if letter == 'z':
        return 'a'
    else:
        return chr(ord(letter)+1)

def shift(string):
    word = ""
    for x in string:
        if x == '-' or x == ' ':
            word += " "
        else:
            word += shift_letter(x)
    return word

count = 0
real_data = []
with open("input_04.txt") as file:
    for line in file:
        name, sector, checksum = re.match(regex, line.strip()).groups()
        if get_checksum(name) == checksum:
            count += int(sector)
            for _ in range(int(sector)%26):
                name = shift(name)
            if name == 'northpole object storage':
                print(f'Part 2: {sector}')
print(f'Part 1: {count}')


