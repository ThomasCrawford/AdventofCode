from collections import defaultdict

def def_value():
    return 0

def place_order(needed, ingredient, qty):
    inputs, outs = recipes[ingredient]
    batch_count = [x[0] for x in outs if x[1] == ingredient][0]
    mult = qty // batch_count + (qty % batch_count > 0)
    for i in inputs:
        needed[i[1]] += i[0]*mult
    for out in outs:
        needed[out[1]] -= out[0]*mult
    return needed

def ore_for_n_fuel(n):
    needed = defaultdict(def_value)
    needed["FUEL"] = n
    while not all([needed[x] <= 0 for x in needed if x != "ORE"]):
        for key in needed:
            if key != "ORE" and needed[key] > 0:
                needed = place_order(needed, key, needed[key])
                break
    return needed["ORE"]

recipes = {}
with open("input14.txt") as file:
    for line in file:
        a, b = line.strip().split(" => ")
        inputs = [[int(x.split(" ")[0]),x.split(" ")[1]]  for x in a.split(", ")]
        outputs = [[int(x.split(" ")[0]),x.split(" ")[1]]  for x in b.split(", ")]
        for ing in [out[1] for out in outputs]:
            recipes[ing] = inputs, outputs


ans1 = ore_for_n_fuel(1)
print(ans1)

#Part 2
target = 1000000000000 # 1trillion

under = 1
over = int(target)
while over - under >1:
    guess = (over + under)//2 
    if ore_for_n_fuel(guess) > target:
        over = guess
    else:
        under = guess
print(under)

