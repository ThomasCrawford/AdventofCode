BOSS_HP = 71
BOSS_DAMAGE = 8

spells = {
    "Magic_Missile": {
        "cost": 53,
        "damage": 4,
        "heal": 0,
        "shield": 0,
        "poison": 0,
        "recharge": 0
    },
    "Drain": {
        "cost": 73,
        "damage": 2,
        "heal": 2,
        "shield": 0,
        "poison": 0,
        "recharge": 0
    },
    "Shield": {
        "cost": 113,
        "damage": 0,
        "heal": 0,
        "shield": 6,
        "poison": 0,
        "recharge": 0
    },
    "Poison": {
        "cost": 173,
        "damage": 0,  
        "heal": 0,
        "shield": 0,
        "poison": 6,
        "recharge": 0
    },
    "Recharge": {
        "cost": 229,
        "damage": 0,
        "heal": 0,
        "shield": 0,
        "poison": 0,
        "recharge": 5
    }
}


init_game_state = {
    "boss_hp": 71,
    "hp": 50,
    "manna": 500,
    "shield": 0,
    "poison": 0,
    "recharge": 0,
    "manna_used": 0
}

def effects_activate(game_state):
    if game_state["poison"]:
        game_state["poison"] -= 1
        game_state["boss_hp"] -= 3
        if game_state["boss_hp"]<=0:
            print("Boss Dead")
    if game_state["recharge"]:
        game_state["recharge"] -= 1
        game_state["manna"] += 101
    if game_state["shield"]:
        game_state["shield"] -= 1
    return (game_state)

def take_turn(game_state,spell_name):
    new_game_state = game_state

    # spell updates game state
    spell = spells[spell_name] 
    new_game_state["boss_hp"] -= spell['damage']
    new_game_state["manna"] -= spell['cost']
    new_game_state["hp"] += spell['heal']
    new_game_state["shield"] += spell['Shield']
    new_game_state["poison"] += spell['poison']
    new_game_state["recharge"] += spell['Recharge']
    new_game_state["manna_used"] += spell['cost']

    if new_game_state["boss_hp"] <= 0:
        return True

    # start of boss's turn:
    new_game_state = effects_activate(new_game_state)

    # boss attacks
    boss_dmg = BOSS_DAMAGE
    if new_game_state["shield"]:
        boss_dmg = max(boss_dmg - 7,1)
    new_game_state["hp"] -= boss_dmg
    if new_game_state["hp"] <= 0:
        return False
    # start of next turn
    new_game_state = effects_activate(new_game_state)

    return new_game_state

def available_spells(game_state):
    can_cast = []
    for spell in spells:
        if spell["cost"] <= game_state["manna"]:
            if 
            









# test_game_state = {
#     "boss_hp": 14,
#     "hp": 10,
#     "manna": 250,
#     "shield": 0,
#     "poison": 0,
#     "recharge": 0,
#     "manna_used": 0
# }

# print(test_game_state)
# game_state = take_turn(test_game_state, "Recharge")
# print(game_state)
# game_state = take_turn(test_game_state, "Shield")
# print(game_state)
# game_state = take_turn(test_game_state, "Drain")
# print(game_state)
# game_state = take_turn(test_game_state, "Poison")
# print(game_state)
# game_state = take_turn(test_game_state, "Magic_Missile")
# print(game_state)
