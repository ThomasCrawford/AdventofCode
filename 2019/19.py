from intcode13 import Intcode


with open("input19.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

def in_beam(x,y):
    bot = Intcode(list(data),[x,y])
    bot.run()
    return bot.output[0]


ans1 = 0

for y in range(50):
    for x in range(50):
        ans1 += in_beam(x,y)
print(f'Part 1: {ans1}')



# Part 2




x = 0
y = 100

while True:
    if not in_beam(x,y):
        x += 1
    else:
        if in_beam(x+99, y-99):
            print(f'Part 2: {x*10000+y-99}')
            break
        else:
            y += 1



#15231121 too high
