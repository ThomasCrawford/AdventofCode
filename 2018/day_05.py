


def match(letter1, letter2):
    if letter1 == letter2:
        return False
    if letter1 == letter2.upper() or letter1.upper() == letter2:
        return True
    else:
        return False

def collapse(word):
    i = 0
    while i < len(word) - 1:
        if match(word[i], word[i + 1]):
            word = word[:i] + word[i + 2:]
            i = max(i - 1, 0)
        else:
            i += 1
    return word


with open("input_05.txt") as file:
    for line in file:
        word = line.strip()

ans1 = len(collapse(word))
print(ans1)

# Part 2

options = []
for removed_letter in set(word):
    new_word = word.replace(removed_letter.upper(),"").replace(removed_letter.lower(),"")
    options.append(len(collapse(new_word)))

print(min(options))