
roundto = 1000

red = []
green = []
with open("9.txt") as file:
    for line in file:
        a,b = line.strip().split(",")
        red.append([int(a)//roundto,int(b)//roundto])

for i,tile in enumerate(red):
    other = red[i-1]
    if tile[0] == other[0]:
        ys = min(tile[1],other[1])
        ye = max(tile[1],other[1])
        green += [[tile[0],y] for y in range(ys,ye+1)]
    elif tile[1] == other[1]:
        ys = min(tile[0],other[0])
        ye = max(tile[0],other[0])
        green += [[x,tile[1]] for x in range(ys,ye+1)]

for y in range (100):
    l = ""
    for x in range(100):
        if [x,y] in red:
            l += "#"
        elif [x,y] in green:
            l += "X"
        else:
            l+= "."
    print(l)



