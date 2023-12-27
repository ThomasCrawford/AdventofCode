word = 'hxbxwxba'

def next_in_english(letter):
    digits = "abcdefghijklmnopqrstuvwxyz"
    letter_index = digits.find(letter)
    if letter_index == len(digits)-1:
        return False
    else:
        return digits[letter_index+1]

def increment(string):
    if string == "z":
        return "aa"
    digits = "abcdefghjkmnpqrstuvwxyz"
    letter_index = digits.find(string[-1])
    if letter_index == len(digits)-1:
        return increment(string[:-1]) + digits[0]
    else:
        return string[:-1] + digits[letter_index+1]

def is_valid(password):
    found_trip = False
    for i in range(len(password)-3):
        if next_in_english(password[i]) == password[i+1] and \
                next_in_english(password[i+1]) == password[i+2]:
            found_trip = True

    pair_count = 0
    i = 0
    while i < len(password)-1:
        if password[i] == password [i+1]:
            pair_count += 1
            i +=2
        else:
            i += 1
    return pair_count >= 2 and found_trip

word = increment(word)
while not is_valid(word):
    word = increment(word)

print(f"Part 1: {word}")

word = increment(word)
while not is_valid(word):
    word = increment(word)

print(f"Part 2: {word}")