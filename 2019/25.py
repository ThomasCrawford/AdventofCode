from intcode23 import Intcode
import re
from itertools import combinations

def disp(li):
    print("".join([chr(x) for x in li]))

def all_combinations(lis):
    list_of_lists = []
    for i,_ in enumerate(lis):
        list_of_lists += list(combinations(lis,i))
    list_of_lists.append(lis)
    return list_of_lists

def drop(bot, list_of_items):
    for item in drop_list:
        cmd = "drop " + item + "\n"
        bot.inputs += [ord(x) for x in cmd]
        bot.run()
    # return bot

def take(bot, list_of_items):
    for item in drop_list:
        cmd = "take " + item + "\n"
        bot.inputs += [ord(x) for x in cmd]
        bot.run()
    # return bot

def cmd(bot, string):
    bot.inputs += [ord(x) for x in string + "\n"]
    out = bot.run()
    return "".join([chr(x) for x in out])

with open("input25.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

bot = Intcode(list(data),[])

route = "north\n\
take astronaut ice cream\n\
south\n\
west\n\
take mouse\n\
north\n\
take ornament\n\
west\n\
north\n\
take easter egg\n\
north\n\
west\n\
north\n\
take wreath\n\
south\n\
east\n\
south\n\
east\n\
take hypercube\n\
north\n\
east\n\
take prime number\n\
west\n\
south\n\
west\n\
south\n\
west\n\
take mug\n\
west\n\
"


cmd(bot,route)


# bot.run()
bot.inputs += [ord(x) for x in "inv\n"]
item_string = "".join([chr(x) for x in bot.run()])
items = [x[2:] for x in item_string.split("\n")[2:-3]]


for drop_list in all_combinations(items):
    drop(bot,drop_list)
    # print(cmd(bot, "inv"))
    result = cmd(bot,"north")
    # print(drop_list)
    if "Alert!" not in result:
        print(result)
        quit()
    take(bot,drop_list)


# # Manual
# while True:
#     out = bot.run()
#     disp(out)
#     inp = input()
#     bot.inputs += [ord(x) for x in inp]
#     bot.inputs += [ord("\n")]


