import re

regex = '[0-9]|one|two|three|four|five|six|seven|eight|nine'
regex2 = '[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'


number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0':0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


number_dict2 = {
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9,
    '0':0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

firsts = 0

with open("Day1Bin.txt") as file:
# with open("Day1_test.txt") as file:
	for line in file:
		num = re.search(regex,line)
		firsts = firsts + number_dict[num.group()]


seconds = 0
with open("Day1Bin.txt") as file:
# with open("Day1_test.txt") as file:
	for line in file:
		num = re.search(regex2,line[::-1])
		seconds = seconds + number_dict2[num.group()]

print(firsts*10 + seconds)
