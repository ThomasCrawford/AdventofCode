from intcode import Intcode
from collections import defaultdict
import cmath

def def_value():
    return 0


with open("input11.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

def run(start):
    canvas = defaultdict(def_value)
    p = 0
    d = -1*1j
    bot = Intcode(data, [start])
    while bot.active:
        color = bot.run()
        turn = bot.run()
        if bot.active:
            canvas[p] = color
            if turn == 0:
                d *= -1j
            elif turn == 1:
                d *= 1j
            p += d
            bot.input(canvas[p])
    return canvas

def disp(canvas):
    xs = [p.real for p in canvas]
    ys = [p.imag for p in canvas]
    for y in range(int(min(ys)),int(max(ys)+1)):
        out = ""
        for x in range(int(min(xs)),int(max(xs)+1)):
            out += "#" if canvas[(x+y*1j)] == 1 else "."
        print(out)

ans1 = len(run(0))
print(ans1)

disp(run(1))

