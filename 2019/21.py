from intcode13 import Intcode


code = "\
NOT C T\n\
OR T J\n\
NOT B T\n\
OR T J\n\
AND D J\n\
NOT A T\n\
OR T J\n\
WALK\n\
"

with open("input21.txt") as file:
    for line in file:
        data = [int(x) for x in line.strip().split(",")]

bot = Intcode(list(data),[])
bot.run_and_print()
for x in code:
    bot.input(ord(x))
if not bot.run_and_print():
    bot.display_output()


code = "\
NOT C T\n\
OR T J\n\
NOT B T\n\
OR T J\n\
AND D J\n\
AND H J\n\
NOT A T\n\
OR T J\n\
RUN\n\
"

bot = Intcode(list(data),[])
bot.run_and_print()
for x in code:
    bot.input(ord(x))
if not bot.run_and_print():
    bot.display_output()
