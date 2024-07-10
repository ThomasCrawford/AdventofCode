import cmath


class Elf:

    directions = [1,1j,-1,-1j]
    game_over = False

    def __init__(self, p, t, elf_attack):
        self.t = t
        self.p = p
        self.hp = 200
        self.attack = 3 if t == "G" else elf_attack
        self.alive = True

    @staticmethod
    def sort(lists):
        sorted_list = sorted(lists, key=lambda x: (x[1].imag, x[1].real))
        uniques = {}
        for l in sorted_list:
            if l[0] not in uniques:
                uniques[l[0]] = l
        return list(uniques.values())

    def move(self, elves, data):
        others = [elf for elf in elves if elf != self]
        occupied = [elf.p for elf in elves]
        avail = [z for z in data if z not in occupied]
        enemies = [other.p for other in others if other.t != self.t and other.alive]
        if not enemies:
            Elf.game_over = True

        poss_target_spaces = [e + d for e in enemies for d in Elf.directions if e+d in avail or e+d == self.p]

        #If no movement needed
        if self.p in poss_target_spaces:
            return

        seen = set() 
        live = [[self.p + d, d] for d in Elf.directions if self.p+d in avail] # space, "first" first step that can lead to this
        while live and not any([x[0] in poss_target_spaces for x in live]):
            next_gen = [[s[0]+d,s[1]] for d in Elf.directions for s in live]
            next_gen = [x for x in next_gen if x[0] in avail and x[0] not in seen]
            live = Elf.sort(next_gen)
            for x in live:
                seen.add(x[0])
        poss = [x for x in live if x[0] in poss_target_spaces]
        if poss:
            self.p += sorted(poss, key=lambda x: (x[0].imag, x[0].real))[0][1]

    def attack1(self,elves):
        #find target:
        adj_spaces = [self.p + d for d in Elf.directions]
        adj_enemies = [elf for elf in elves if elf.p in adj_spaces and elf.t != self.t]

        #attack
        if adj_enemies:
            target = sorted(adj_enemies, key=lambda x: ( x.hp, x.p.imag, x.p.real))[0]
            target.hp -= self.attack
            if target.hp <= 0:
                target.alive = False
                target.p = -10

    def turn(self, elves, data):
        self.move(elves, data)
        self.attack1(elves)



def sort_elves(elves):
    return sorted(elves, key=lambda x: (x.p.imag, x.p.real))

def disp(elves, data):
    elf_locations = {elf.p: elf for elf in elves}
    for y in range(int(min([z.imag for z in data])), int(max([z.imag for z in data]))+1):
        out = ""
        for x in range(int(min([z.real for z in data])), int(max([z.real for z in data]))+1):
            if x+y*1j in elf_locations:
                out += elf_locations[x+y*1j].t
            elif x+y*1j in data:
                out += "."
            else:
                out+= "#"
        print(out)


def run(elf_attack):
    data = []
    elves = []
    Elf.game_over = False

    with open("input_15.txt") as file:
        for k,line in enumerate(file):
            for i,v in enumerate(line.strip()):
                if v in ["E", "G"]:
                    elves.append(Elf(i+k*1j, v, elf_attack))
                    data.append(i+k*1j)
                elif v == ".":
                    data.append(i+k*1j)

    round_num = -1
    while not Elf.game_over:
        round_num += 1
        for elf in elves:
            elf.turn(elves, data)
        elves = sort_elves(elves)

    outcome = round_num * sum([elf.hp for elf in elves if elf.alive == True ])
    return elves, outcome, round_num


elves, ans1, round_num = run(3)
print(f'Part 1: {ans1}')


# Part 2:

elf_attack = 3
while True:
    elf_attack += 1
    elves, outcome, round_num = run(elf_attack)
    dead_elves = [elf for elf in elves if not elf.alive and elf.t == "E"]
    if not dead_elves:
        print(f'Part 2: {outcome}')
        break
    print(f'With {elf_attack} attack, {len(dead_elves)} elves died by round {round_num}')


