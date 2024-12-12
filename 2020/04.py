import re

eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
letters = ['a','b','c','e', 'd','f']


def verify(code, value):
    match code:
        case "byr":
            return value.isdigit() and 1920 <= int(value) <= 2002
        case "iyr":
            return value.isdigit() and 2010 <= int(value) <= 2020
        case "eyr":
            return value.isdigit() and 2020 <= int(value) <= 2030
        case "hgt":
            if value[-2:] == "in":
                return value[:-2].isdigit() and 59 <= int(value[:-2]) <= 76
            elif value[-2:] == "cm":
                return value[:-2].isdigit() and 150 <= int(value[:-2]) <= 193
            else:
                return False
        case "hcl":
            if value[0] != "#" or len(value) != 7:
                return False
            elif all([x in letters or x.isdigit() for x in value[1:]]):
                return True
            else:
                return False
        case "ecl":
            return value in eye_colors
        case "pid":
            return len(value) == 9 and value.isdigit()
        case "cid":
            return True





data = []
with open("input04.txt") as file:
    content = file.read()
    for entry in content.split("\n\n"):
        passport = {}
        for match in re.findall(r'(\b[a-z]{3}\b):([\S]+)',entry):
            code, value = match
            passport[code] = value
        data.append(passport)

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

present = [passport for passport in data if all([i in passport for i in required])]
print(len(present))


valid = []
for passport in present:
    if all([verify(code, value) for code, value in passport.items()]):
        valid.append(passport)

print(len(valid))
