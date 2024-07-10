seed = "084601"


def step(scoreboard, Elf_1, Elf_2):
    s = scoreboard[Elf_1] + scoreboard[Elf_2]
    if s > 9:
        scoreboard.append(1)
    scoreboard.append(s%10)
    l = len(scoreboard)
    Elf_1 = (Elf_1 +scoreboard[Elf_1] + 1)%l
    Elf_2 = (Elf_2 +scoreboard[Elf_2] + 1)%l
    return scoreboard, Elf_1, Elf_2

scoreboard = deque([3,7])
Elf_1 = 0
Elf_2 = 1

#Part 1
while len(scoreboard) < 10 + int(seed):
    scoreboard, Elf_1, Elf_2 = step(scoreboard, Elf_1, Elf_2)

ans1 = "".join(str(x) for x in scoreboard[int(seed): int(seed) + 11])
print(f'Part 1: {ans1}')


#Part 2
scoreboard = [3,7]
Elf_1 = 0
Elf_2 = 1

seed_len = len(seed)
target = [int(x) for x in seed]

while target != scoreboard[-1*seed_len:] and target != scoreboard[-1*seed_len-1:-1]:
    scoreboard, Elf_1, Elf_2 = step(scoreboard, Elf_1, Elf_2)

if target == scoreboard[-1*seed_len:]:
    ans2 = len(scoreboard)-seed_len
else:
    ans2 = len(scoreboard)-seed_len -1

print(f'Part 2: {ans2}')

