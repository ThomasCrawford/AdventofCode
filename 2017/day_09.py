
def clean(string, removed_count):
    if "<" not in string:
        return string, removed_count
    else:
        i = string.index("<")
        while string[i+1] != ">":
            if string[i+1] == "!":
                string = string[:i+1]+ string[i+3:]
            else:
                string = string[:i+1]+ string[i+2:]
                removed_count += 1
        once_cleaned = clean(string[i+2:], removed_count)
        return string[:i+2] + once_cleaned[0], once_cleaned[1]


def score(string):
    s = 0
    level = 0
    for l in string:
        if l == "{":
            level += 1
            s += level
        elif l == "}":
            level -= 1
    return s


data = []
with open("input_09.txt") as file:
    for line in file:
        data.append(list(line.strip()))


for line in data:
    cleaned_line, removed_count = clean(line,0)
    # print ("".join(line),"".join(cleaned_line),removed_count)
    print(f'Part 1: {score(cleaned_line)}')
    print(f'Part 2: {removed_count}')
