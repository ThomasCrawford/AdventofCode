from intcode23 import Intcode


def run1(computer_ids):
    for i, bot in computer_ids.items():
        bot.step()
        if len(bot.output) >= 3:
            j = bot.output.pop(0)
            if j == 255:
                print(f'Part 1: {bot.output.pop(1)}')
                return False
            computer_ids[j].inputs.append(bot.output.pop(0))
            computer_ids[j].inputs.append(bot.output.pop(0))
    return True

def step2(computer_ids, nat):
    for i, bot in computer_ids.items():
        bot.step()
        if len(bot.output) >= 3:
            j = bot.output.pop(0)
            if j == 255:
                a = bot.output.pop(0)
                b = bot.output.pop(0)
                nat = [a,b]
            else:
                computer_ids[j].inputs.append(bot.output.pop(0))
                computer_ids[j].inputs.append(bot.output.pop(0))
    return computer_ids, nat

def is_active(computer_ids):
    return any([bot.inputs for bot in computer_ids.values()]) or \
                    any([not bot.waiting for bot in computer_ids.values()])

def run2(computer_ids, nat):
    while is_active(computer_ids):
        computer_ids, nat = step2(computer_ids, nat)
    return computer_ids, nat

with open("input23.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

# Part 1
computer_ids = {}
for i in range(50):
    bot = Intcode(list(data),[i])
    bot.idnum = i
    computer_ids[i] = bot

while run1(computer_ids):
    pass


# Part 2
computer_ids = {}
nat = []
for i in range(50):
    bot = Intcode(list(data),[i])
    bot.idnum = i
    computer_ids[i] = bot

seen = set()
current = 0
while current not in seen:
    computer_ids, nat = run2(computer_ids,nat)
    computer_ids[0].inputs += nat
    seen.add(current)
    current = nat[1]

print(f'Part 2: {current}')





