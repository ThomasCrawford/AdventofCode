
def dist(a,b,c):
    reorders = [[a-c,b-c],[a-b,c-b],[b-a, c-a]]
    for x,y in reorders:
        if x == 0:
            return abs(y)
        elif y==0:
            return abs(x)
        elif x*y < 0:
            return abs(x)+abs(y)

def up_to_n(n,data):
    a = data[:n+1].count('n') - data[:n+1].count('s')
    b = data[:n+1].count('sw') - data[:n+1].count('ne')
    c = data[:n+1].count('se') - data[:n+1].count('nw')
    return dist(a,b,c)

data = []
with open("input_11.txt") as file:
    for line in file:
        data = line.strip().split(',')

a = data.count('n') - data.count('s')
b = data.count('sw') - data.count('ne')
c = data.count('se') - data.count('nw')

print(f'Part 1: {dist(a,b,c)}')

max_dist = 0
for i,_ in enumerate(data):
    max_dist = max(max_dist, up_to_n(i,data))
print(f'Part 2: {max_dist}')

