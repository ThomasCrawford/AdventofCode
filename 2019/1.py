def fuel(mass):
    return max(mass//3 -2,0)

def total_fuel(mass):
    fuel_count = fuel(mass)
    additional_fuel = fuel(mass)
    while fuel(additional_fuel):
        additional_fuel = fuel(additional_fuel)
        fuel_count +=additional_fuel
    return fuel_count

ans1 = 0
ans2 = 0
with open("input1.txt") as file:
    for line in file:
        mass = int(line.strip())
        ans1 += fuel(mass)
        ans2 += total_fuel(mass)
print(ans1)
print(ans2)
