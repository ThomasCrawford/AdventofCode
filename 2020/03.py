slope = 3


data = []
with open("input03.txt") as file:
    for line in file:
        data.append(line.strip())

width = len(data[0])

def count(data, x_step, y_step):
    ans,x,y = 0,0,0
    while y < len(data):
        if data[y][x] == "#":
            ans += 1
        x = (x + x_step)%width
        y += y_step
    return ans

ans1 = count(data, 3, 1)
print(ans1)

# Part 2

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
ans2 = 1
for x,y in slopes:
    ans2 *= count(data,x,y)
print(ans2)


