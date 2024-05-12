

def decompress(string):
    index = string.find('(')
    if index < 0:
        return string
    else:
        index2 = string.find(')')
        letter_count, duplicate_count = string[index+1:index2].split('x')
        letter_count = int(letter_count)
        duplicate_count = int(duplicate_count)
        return string[:index] + string[index2+1:1+ index2 + letter_count]*duplicate_count + decompress(string[index2 + letter_count +1:])

def string_length(string):
    index = string.find('(')
    if index < 0:
        return len(string)
    else:
        index2 = string.find(')')
        letter_count, duplicate_count = string[index+1:index2].split('x')
        letter_count = int(letter_count)
        duplicate_count = int(duplicate_count)
        return index + \
                string_length(string[index2+1:1+ index2 + letter_count])*duplicate_count + \
                string_length(string[index2 + letter_count +1:])


word = 'A(2x2)BCD(2x2)EFG'
print(decompress(word))

with open("input_09.txt") as file:
    for line in file:
        print(f'Part 1: {len(decompress(line.strip()))}')
        print(f'Part 2: {string_length(line.strip())}')