import heapq

BOSS_HP = 71
BOSS_DAMAGE = 10

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
    "boss_hp": BOSS_HP,
    "hp": 50,
    "manna": 500,
    "shield": 0,
    "poison": 0,
    "recharge": 0
}

def effects_activate(game_state):
    if game_state["poison"]:
        game_state["poison"] -= 1
        game_state["boss_hp"] -= 3
    if game_state["recharge"]:
        game_state["recharge"] -= 1
        game_state["manna"] += 101
    if game_state["shield"]:
        game_state["shield"] -= 1
    return (game_state)

def take_turn(game_state,spell_name):
    new_game_state = game_state.copy()

    # spell updates game state
    spell = spells[spell_name] 
    new_game_state["boss_hp"] -= spell['damage']
    new_game_state["manna"] -= spell['cost']
    new_game_state["hp"] += spell['heal']
    new_game_state["shield"] += spell['shield']
    new_game_state["poison"] += spell['poison']
    new_game_state["recharge"] += spell['recharge']


    # start of boss's turn:
    new_game_state = effects_activate(new_game_state)
    if new_game_state["boss_hp"] <= 0:
        return "Win"

    # boss attacks
    boss_dmg = BOSS_DAMAGE
    if new_game_state["shield"]:
        boss_dmg = max(boss_dmg - 7,1) + 1 #hard mode equivalent to boss doing +1 damage
    new_game_state["hp"] -= boss_dmg
    if new_game_state["hp"] <= 0:
        return "Lose"

    # start of next turn
    new_game_state = effects_activate(new_game_state)
    if new_game_state["boss_hp"] <= 0:
        return "Win"

    return new_game_state

def available_spells(game_state):
    can_cast = []
    for spell in spells:
        if spells[spell]["cost"] <= game_state["manna"]:
            if not (spells[spell]["shield"] and game_state["shield"]) and \
                    not (spells[spell]["poison"] and game_state["poison"]) and \
                    not (spells[spell]["recharge"] and game_state["recharge"]):
                can_cast.append(spell)
    return can_cast

queue = []
heapq.heappush(queue, (0,0, init_game_state))
found = False
counter = 0

while not found:
    manna_spent,_, current_state = heapq.heappop(queue)
    for spell in available_spells(current_state):
        manna_cost = spells[spell]['cost']
        next_state = take_turn(current_state, spell)
        print(current_state, counter)
        if next_state == "Lose":
            pass
        elif next_state == "Win":
            print(manna_spent+manna_cost)
            found = True
        else:
            heapq.heappush(queue,(manna_spent + manna_cost, counter, next_state))
    counter += 1

