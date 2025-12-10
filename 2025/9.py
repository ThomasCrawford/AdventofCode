import itertools

def area(a,b):
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)

def is_valid(a,b):
    x0 = min(a[0],b[0])
    x1 = max(a[0],b[0])
    y0 = min(a[1],b[1])
    y1 = max(a[1],b[1])
    for v in red:
        if x0<v[0]<x1 and y0<v[1]<y1:
            return False
    if y0 <= min(cutoffs) and y1 >= max(cutoffs) :
        return False
    return True
    

red = []
with open("9.txt") as file:
    for line in file:
        a,b = line.strip().split(",")
        red.append([int(a),int(b)])

ans1 = max([area(a,b) for a,b in itertools.combinations(red,2)])
print(ans1)

#part 2
for i,p in enumerate(red):
    if red[i][0]-red[i-1][0] >50000:
        cutoffs = [red[i][1],red[i+1][1]]

ans2 = max([area(a,b) for a,b in itertools.combinations(red,2) if is_valid(a,b)])
print(ans2)
