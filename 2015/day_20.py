
goal = 36000000

def num_gifts2(house_num):
    factors = set()
    for i in range(1,51):
        if house_num%i == 0:
            factors.add(house_num/i)
    return int(sum(factors)) *11

def num_gifts (house_num):
    factors = set()
    for i in range(1,int(house_num**0.5)+1):
        if house_num%i == 0:
            factors.add(i)
            factors.add(house_num/i)
    return int(sum(factors)) *10


best_so_far = 0
i = 100
while best_so_far < goal:
    i += 100
    gifts_here = num_gifts(i)
    if gifts_here > best_so_far:
        best_so_far = gifts_here
print(f'Part 1: {i}')

best_so_far = 0
i = 100
while best_so_far < goal:
    i += 10
    gifts_here = num_gifts2(i)
    if gifts_here > best_so_far:
        best_so_far = gifts_here
print(f'Part 2: {i}')

