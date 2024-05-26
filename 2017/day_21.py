import math
import itertools


def print_block(block):
    sq = int(math.sqrt(len(block)))
    for i in range(sq):
        print("".join(block[sq*i:sq*i+sq]))
    print("\n")

def reflect(b):
    w = int(math.sqrt(len(b)))
    out = []
    for i in range(w):
        out += b[w*i:w+w*i][::-1]
    return out

def rotate(b):
    w = int(math.sqrt(len(b)))
    out = []
    for i in range(w):
        out += b[i::w][::-1]
    return out

def all_variants(block):
    var = []
    for a,b,c in itertools.product([False, True], repeat = 3):
        v = block
        if a:
            v = rotate(v)
        if b:
            v = reflect(v)
        if c:
            v = list(reversed(v))       
        var.append(v)
    return (var)

def to_bin(l):
    return sum(v<<i for i, v in enumerate([1 if x == "#" else 0 for x in l][::-1]))

def get_id(s):
    return max([to_bin(v) for v in all_variants(s)])

def decompose(block):
    w = int(math.sqrt(len(block)))
    out = []
    if w%2 == 0:
        d = 2
    else:
        d = 3
    for a in range(w//d):
        for b in range(w//d):
            this = []
            for l in range(d):
                start = w*l + d*b+w*a*d
                this += block[start : start + d]
            out.append(this)

    return out, d-2

def recompose(blocks):
    out = []
    c = int(math.sqrt(len(blocks)))
    w = int(math.sqrt(len(blocks[0])))
    for block_row in range(c):
        row = []
        for sub_row in range(w):
            for block_col in range(c):
                row += blocks[block_col+ c*block_row][sub_row*w:sub_row*w+w]
        out += row
    return out



def step(inp):
    old_blocks, d = decompose(inp)
    #Optional
    print_block(inp)
    new_blocks = [rules[d][get_id(block)] for block in old_blocks]
    return recompose(new_blocks)

first = '.#...####'
rules = [{},{}]
with open("input_21.txt") as file:
    for line in file:
        s,t = line.strip().replace("/","").split(" => ")
        key = get_id(s)
        if len(s) == 4:
            rules[0][key] = t
        else:
            rules[1][key] = t 


for i in range(13):
    first = step(first)

print(len(first))
ans = first.count("#")
print(ans)