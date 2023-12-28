from itertools import combinations

# hp, damage, armor

boss_stats = [100,8,2]

def does_player_win(player, boss):
    hp1, d1, a1 = player
    hp2, d2, a2 = boss
    dmg_per_turn_1 = max(d1-a2,1)
    turns_for_player = hp2//dmg_per_turn_1 + (hp2%dmg_per_turn_1>0)
    dmg_per_turn_2 = max(d2-a1,1)
    turns_for_boss = hp1//dmg_per_turn_2 + (hp1%dmg_per_turn_2>0)
    return turns_for_player <= turns_for_boss

def is_loadout_sufficient(equiped):
    stats = [sum(values) for values in zip(*equiped)]
    player_stats = [100, stats[1],stats[2]]
    return does_player_win(player_stats, boss_stats)


weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armor = [[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[0,0,0],[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

sufficient_loadouts_costs = []
insufficient = []

for w in weapons:
    for a in armor:
        for r1, r2 in combinations(rings,2):
            if is_loadout_sufficient([w,a,r1,r2]):
                sufficient_loadouts_costs.append(w[0]+a[0]+r1[0]+r2[0])
            else:
                insufficient.append(w[0]+a[0]+r1[0]+r2[0])
print(f'Part 1: {min(sufficient_loadouts_costs)}')
print(f'Part 2: {max(insufficient)}')
