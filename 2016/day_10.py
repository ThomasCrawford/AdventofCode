import heapq
import re

chip1 = 17
chip2 = 61


class Bot:
    reg = {}
    outputs = {}

    def __init__(self, bot_id, low_target, high_target):
        self.id = bot_id
        self.chips = []
        self.high_target = high_target
        self.low_target = low_target
        Bot.reg[self.id] = self


    def try_give(self):
        assert len(self.chips) == 2
        a = self.high_target
        b = self.low_target
        #checks if there is room 
        if a[0] == 'b':
            if len(Bot.reg[a].chips) >1:
                return False
        if b[0] == 'b':
            if len(Bot.reg[b].chips) >1:
                return False

        if b[0] == 'b':
            Bot.reg[b].receive(self.chips[0])
        else:
            Bot.outputs[b] = self.chips[0]
        if a[0] == 'b':
            Bot.reg[a].receive(self.chips[1])
        else:
            Bot.outputs[a] = self.chips[1]
        self.chips = []
        return True


    def receive(self, chip):
        self.chips.append(chip)
        self.chips.sort()
        if self.chips == [chip1, chip2]:
            print(f'Part 1: {self.id}')

# class Output:
#     reg = {}
#     def __init__(self,output_id):
#         self.id = output_id
#         self.chips = []
#         Output.reg[self.id] = self


starting_chips = []
bot_q = []

regex1 = r'value (\d+) goes to (\w+ \d+)'
regex2 = r'(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)'

with open("input_10.txt") as file:
    for line in file:
        match_value = re.match(regex1,line)
        match_bot = re.match(regex2,line)
        if match_value:
            value, bot_id = match_value.groups()
            starting_chips.append([value,bot_id])
        elif match_bot:
            bot_id, low_target, high_target = match_bot.groups()
            Bot(bot_id,low_target,high_target)


for start in starting_chips:
    value, bot = start
    Bot.reg[bot].receive(int(value))
    if len(Bot.reg[bot].chips) == 2:
        bot_q.append(bot)


while bot_q:
    bot_id = bot_q.pop(0)
    bot = Bot.reg[bot_id]
    possible = bot.try_give()
    if not possible:
        bot_q.append(bot_id)
    for target in [bot.high_target, bot.low_target]:
        if target[0] == 'b':
            if len(Bot.reg[target].chips) == 2:
                bot_q.append(target)

ans = Bot.outputs['output 0'] * Bot.outputs['output 1'] * Bot.outputs['output 2']
print(f'Part 2: {ans}')