


with open("05.txt") as file:
    content = file.read()

r,u = content.split("\n\n")

rules = []
updates = []

for line in r.split("\n"):
    a,b = line.strip().split('|')
    rules.append([int(a),int(b)])
for line in u.split("\n")[:-1]:
    updates.append([int(x) for x in line.strip().split(',')]) 



def check(update, rules):
    for [a,b] in rules:
        if a in update and b in update and update.index(a) > update.index(b):
            return False
    return True

def reorder(update, rules):
    for [a,b] in rules:
        if a in update and b in update and update.index(a) > update.index(b):
            new_update = update[:update.index(b)] + [a] + update[update.index(b)+1:update.index(a)]+ [b] + update[update.index(a)+1:]
            return reorder(new_update,rules)
    return update


ans1 = 0
ans2 = 0
for update in updates:
    m = int(len(update)/2)
    if check(update, rules):
        ans1 += update[m]
    else:
        ans2 += reorder(update,rules)[m]

print(ans1)
print(ans2)
