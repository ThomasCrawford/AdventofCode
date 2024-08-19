from test_intcode import Intcode
from collections import defaultdict
import time

def def_value():
    return -1

with open("input13.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

def run(bot, inp):
    bot.inputs.append(inp)
    bot.waiting = False
    outs = bot.run()
    return bot, outs

def update(screen, new_data):
    for i in range(len(new_data)//3):
        screen[new_data[i*3] + new_data[i*3+1]*1j] = new_data[i*3+2]
    return screen

def disp(canvas):
    print(canvas[-1])
    for y in range(26):
        out = ""
        for x in range(43):
            if canvas[(x+y*1j)] == 0:
                out += "."
            elif canvas[(x+y*1j)] == 1:
                out += "|"
            elif canvas[(x+y*1j)] == 2:
                out += "="
            elif canvas[(x+y*1j)] == 3:
                out += "_"
            elif canvas[(x+y*1j)] == 4:
                out += "O"
            else:
                out += "?"
        print(out)

def next_move(screen):
    ball = [int(p.real) for p in screen if screen[p] == 4][0]
    paddle = [int(p.real) for p in screen if screen[p] == 3][0]
    if ball == paddle:
        return 0
    elif ball > paddle:
        return 1
    elif ball < paddle:
        return -1
#Part 2
data[0] = 2

bot = Intcode(data, [])
screen = defaultdict(def_value)
m = 0


while True:
    bot, disp_data = run(bot, m)
    if disp_data==False:
        print(bot.output[-1])
        break
    update(screen, disp_data)
    # disp(screen)
    m = next_move(screen)




#To pre-script moves, use:

# moves = [0,0,0] + [1]*19 + [0]*30

# for m in moves:
#     bot, disp_data = run(bot, m)
#     update(screen, disp_data)
#     disp(screen)
#     time.sleep(0.4)


## To Play, use:

# while True:
#     m = int(input())
#     bot, disp_data = run(bot, m)
#     update(screen, disp_data)
#     disp(screen)
