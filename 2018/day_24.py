import re

class Group:
    def __init__(self, team, match):
        self.team = team
        self.count = int(match[0])
        self.hp = int(match[1])
        self.weak = []
        self.immune = []
        self.dmg = int(match[3])
        self.atk_type = match[4]
        self.initiative = int(match[5])
        modifiers = match[2].split("; ") 
        for modifier in modifiers:
            if "weak" in modifier:
                self.weak = modifier.replace("weak to ","").split(", ")
            elif "immune" in modifier:
                self.immune = modifier.replace("immune to ","").split(", ")
        self.targeted = False
        self.target = None

    def mod(self, other):
        if self.atk_type in other.immune:
            return 0
        elif self.atk_type in other.weak:
            return 2
        else:
            return 1

    def find_target(self, groups):
        avail = [g for g in groups if g.team != self.team and g.targeted == False]
        targets = [[Group.mod(self, t), t.count*t.dmg, t.initiative, t] for t in avail]
        targets.sort()
        if targets and self.mod(targets[-1][-1])>0:
            self.target = targets[-1][-1]
            self.target.targeted = True

    def reset_targets(self):
        self.targeted = False
        self.target = None

    def attack(self):
        if self.target and self.count > 0:
            other = self.target
            damage = self.dmg*self.count*self.mod(other)
            units_killed = damage//other.hp
            other.count -= units_killed
            return units_killed
        return 0

regex = r'(\d+) units each with (\d+) hit points(?: \((.*?)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)'

data = ""
with open("input_24.txt") as file:
    for line in file:
        data += line
a,b = data.split("\n\n")


def evaluate(boost):

    groups = []
    for match in re.findall(regex, a):
        groups.append(Group("Immune System", match))
    for g in groups:
        g.dmg += boost
    for match in re.findall(regex, b):
        groups.append(Group("Infection", match))

    while len(set([g.team for g in groups])) > 1:
        
        #Target selection
        groups.sort(key=lambda x: (-1*x.count*x.dmg, -1*x.initiative))
        for group in groups:
            group.find_target(groups)

        #Attack Phase
        groups.sort(key=lambda x: -1*x.initiative)
        units_killed = 0
        for group in groups:
            if group.count > 0:
                units_killed += group.attack()

        #Clean up
        groups = [g for g in groups if g.count > 0]
        for g in groups:
            g.reset_targets()
        if not units_killed:
            return groups

    return groups

def immune_win(boost):
    groups = evaluate(boost)
    return all([group.team == "Immune System" for group in groups])

groups = evaluate(0)    
ans1 = sum([g.count for g in groups])
print(ans1)

#Part 2

boost = 1
while not immune_win(boost):
    boost += 1
groups = evaluate(boost)    
ans2 = sum([g.count for g in groups])
print(ans2)

