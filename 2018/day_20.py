import cmath


def split(word):
    pcount = 0
    result = []
    start = 0
    for i, l in enumerate(word):
        if l == "(":
            pcount += 1
        elif l == ")":
            pcount -= 1
        elif l == "|" and pcount == 0:
            result.append(word[start:i])
            start = i+1
    result.append(word[start:])

    return result

def find_open_paren(word):
    pcount = 0
    for i, l in enumerate(word[::-1]):
        if l == ")":
            pcount += 1
        elif l == "(":
            pcount -= 1
            if pcount == 0:
                return i


def combine(word, points):
    directions = {"N": -1j, "S": 1j, "E": 1, "W": -1}
    while word and word[-1] in directions:
        l = word[-1]
        word = word[:-1]
        points = set([2*directions[l] + z for z in points])
        points.add(directions[l])
    if word and word[-1] == ")":
        new_words = set()
        start = find_open_paren(word)
        for subword in split(word[-1*start:-1]):
            new_words.update(combine(subword, points))
        return combine(word[:-1*start-1], new_words)
    return points



def display(points):
    xmin = int(min([z.real for z in points]))
    xmax = int(max([z.real for z in points]))
    ymin = int(min([z.imag for z in points]))
    ymax = int(max([z.imag for z in points]))
    for y in range(ymin-1, ymax+2):
        out = ""
        for x in range(xmin-1, xmax +2):
            if x == 0 and y == 0:
                out += "X"
            elif x%2 == 0 and y%2 == 0:
                out += "."
            elif x%2 == 0 and x+y*1j in points:
                out += "-"
            elif x+y*1j in points:
                out += "|"
            else:
                out += "#"
        print(out)


# def furthest(points):
#     directions = [1,-1,1j,-1j]
#     seen = set()
#     q = [0]
#     gen = 0
#     while q:
#         newq = set()
#         for p in q:
#             for d in directions:
#                 if p+d in points and p+2*d not in seen:
#                     newq.add(p+2*d)
#         seen.update(q)
#         q = newq
#         gen +=1
#     return gen -1

def path_length(points):
    directions = [1,-1,1j,-1j]
    seen = {}
    q = [0]
    gen = 0
    while q:
        newq = set()
        for p in q:
            for d in directions:
                if p+d in points and p+2*d not in seen:
                    newq.add(p+2*d)
        for z in q:
            seen[z] = gen
        q = newq
        gen +=1
    return seen

# print(combine("E(N|S)EEE", []))

# print(split("NS|S(E|W)"))

# def doors(word, found):



with open("input_20.txt") as file:
    for line in file:
        word = line.strip()[1:-1]

points = combine(word, [])
paths = path_length(points)
ans1 = max(paths.values())

ans2 = len([room for room in paths if paths[room]>=1000])
# display(points)
print(ans1)
print(ans2)





# print(word)





