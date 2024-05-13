


line = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
row_count = 400000

width = len(line)

def next_line(line):
    l = "." + line + "."
    out = ""
    for i, x in enumerate(l[:-2]):
        if x != l[i+2]:
            out += "^"
        else:
            out += "."
    return out

def count(line):
    return len([x for x in line if x == "."])

safe = count(line)
for i in range(row_count-1):
    line = next_line(line)
    safe += count(line)
print(safe)