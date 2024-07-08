seed = 7672
# seed = 42


cells = {}

def level(x,y):
    v = ((x+10)*y + seed )* (x+10)
    return int(str(v)[-3]) -5

## Naive approach:
# def get_sum(x1,y1, size):
#     ans = 0
#     for x in range(x1, x1+size):
#         for y in range(y1, y1+size):
#             ans += cells[(x,y)]
#     return ans

# Better approach: precalculates rectangles
def get_sum2(x1,y1, size):
    x1 -= 1
    y1 -= 1
    return cv.get((x1,y1),0)+cv.get((x1+size,y1+size),0) - cv.get((x1 + size,y1),0) - cv.get((x1,y1 + size),0)


for x in range(1,301):
    for y in range(1,301):
        cells[(x,y)] = level(x,y)

#cv is cumulative charge up to and including (x,y)
cv = {}
for x in range(1,301):
    for y in range(1,301):
        cv[(x,y)] = cv.get((x-1,y),0)+cv.get((x,y-1),0) - cv.get((x-1,y-1),0) + cells[(x,y)]

def largest(size):
    best = 0
    ans1 = [0,0]
    for x in range(1, 301-size):
        for y in range(1,301-size):
            this = get_sum2(x,y,size)
            if this > best:
                best = this
                ans1 = [x,y]
    return best, ans1

print(f'Part 1: {largest(3)[1]}')

record = 0
ans2 = 0
for i in range(1,101):
    this = largest(i)
    if this[0]> record:
        ans2 = this[1] + [i]
        record = this[0]

print(f'Part 2: {ans2}')




