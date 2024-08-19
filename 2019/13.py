from intcode import Intcode

with open("input13.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

def run(start):
    bot = Intcode(data, [])
    outs = []
    while bot.active:
        outs.append(bot.run())
    return outs

def disp(disp_data):
    canvas = {}
    for i in range(len(disp_data)//3):
        canvas[disp_data[i] + disp_data[i+1]*1j] = disp_data[i+2]
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

state = run(0)
ans1 = len([x for x in state[2::3] if x == 2])
print(ans1)

disp(state)
