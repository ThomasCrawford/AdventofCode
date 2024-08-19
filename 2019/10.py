
def redu(x,y):
    if x == 0:
        return 0,int(y/abs(y))
    for n in range(2,abs(x)+1):
        if x%n==0 and y%n==0:
            return redu(x//n, y//n)
    return x,y


def block(center,other,blocked):
    n=2
    x_step, y_step = redu(other[0]-center[0],other[1]-center[1])
    x = other[0] + x_step
    y = other[1] + y_step
    while 0<=x<=width and 0<=y<=height:
        blocked.add((x,y))
        x += x_step
        y += y_step
    return blocked

def visable(data, center):
    blocked = set()
    for other in data:
        if other not in blocked and other != center:
            blocked = block(center, other, blocked)
    return [p for p in data if p not in blocked and p != center]

def slope(run, rise):
    if run == 0:
        return rise*10000
    else:
        return rise/run

def hemisphere(x, y):
    return -1 if x >= 0 else 1

def score(asteroid, center):
    x = asteroid[0]-center[0]
    y = asteroid[1]-center[1]
    return hemisphere(x,y), slope(x,y)

data = set()
with open ("input10.txt") as file:
    for y, line in enumerate(file):
        for x, v in enumerate(line.strip()):
            if v == "#":
                data.add((x,y))
            width = x
        height = y

#Part 1
candidates = [(len(visable(data,center)),center) for center in data]
candidates.sort()
ans1 = candidates[-1][0]
print(ans1)

#Part 2
base = candidates[-1][1]

blocked = set()
asteroids = visable(data, base)
ordered = [(score(asteroid,base), asteroid) for asteroid in asteroids]
ordered.sort()

ans2 = ordered[199][1][0]*100 + ordered[199][1][1]
print(ans2)

