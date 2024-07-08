def get_meta_sum(cursor):
    child_count = data[cursor]
    meta_count = data[cursor + 1]
    meta_total = 0
    cursor += 2
    for c in range(child_count):
        meta, cursor = get_meta_sum(cursor)
        meta_total += meta
    meta_total += sum(data[cursor: cursor + meta_count])
    cursor += meta_count
    return meta_total, cursor

def part2(cursor):
    child_count = data[cursor]
    meta_count = data[cursor + 1]
    meta_total = 0
    cursor += 2
    children = []
    for c in range(child_count):
        meta, cursor = part2(cursor)
        children.append(meta)
    for m in data[cursor: cursor + meta_count]:
        if m <= child_count:
            meta_total += children[m -1]
    if child_count == 0:
        meta_total = sum(data[cursor: cursor + meta_count])
    cursor += meta_count
    return meta_total, cursor

data = []
with open("input_08.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split()]

print(get_meta_sum(0)[0])

print(part2(0)[0])




