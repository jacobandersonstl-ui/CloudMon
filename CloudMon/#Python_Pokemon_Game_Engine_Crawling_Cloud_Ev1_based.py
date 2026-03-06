#Python Pokemon Game Engine Crawling Cloud Ev1 Based; Engine Codenamed 'PEv1' (Poke-Engine v1)

import random

x = 0
y = 0
game_state = "EXPLORING"
current_tile = "grass"
what_mon_used = False
player_mon = {
    "name": "Quarrion",
    "type": ["Ground", "Fire"],
    "hp": 20,
    "max_hp": 20,
    "lvl": 5,
    "attack": 10,
    "defense": 10,
    "speed": 5,
    "Moves": [
        {"name": "Tackle", "attack": 5, "type": "Normal"},
        {"name": "Ember", "attack": 10, "type": "Fire"}
    ]
}
player_party = [player_mon]
monster_list = [
    {
        "name": "Warkron",
        "type": ["Water"],
        "hp": 10,
        "max_hp": 10,
        "lvl": 5,
        "attack":10,
        "defense": 5,
        "speed": 10,
        "Moves": [
            {"name": "Tackle", "attack": 5, "type": "Normal"},
            {"name": "Ember", "attack": 10, "type": "Fire"}
        ]
    },
    {
        "name": "Lizioto",
        "type": ["Grass"],
        "hp": 20,
        "max_hp": 20,
        "lvl": 5,
        "attack": 4,
        "defense": 10,
        "speed": 10,
        "Moves": [
            {"name": "Tackle", "attack": 5, "type": "Normal"},
            {"name": "Ember", "attack": 10, "type": "Fire"}
        ]
    },
    {
        "name": "Quarrion",
        "type": ["Ground", "Fire"],
        "hp": 20,
        "max_hp": 20,
        "lvl": 5,
        "attack": 10,
        "defense": 10,
        "speed": 5,
        "Moves": [
            {"name": "Tackle", "attack": 5, "type": "Normal"},
            {"name": "Ember", "attack": 10, "type": "Fire"}
        ]
    },
]


def save_game():
    with open("savefile.txt", "w") as f:
        f.write(f"{x}\n")
        f.write(f"{y}\n")
        f.write(f"{player_mon['name']}\n")
        f.write(f"{player_mon['hp']}\n")
        f.write(f"{player_mon['max_hp']}\n")
        f.write(f"{player_mon['lvl']}\n")
        f.write(f"{player_mon['attack']}\n")
        f.write(f"{player_mon['defense']}\n")
        f.write(f"{player_mon['speed']}\n")
        f.write(f"{','.join(player_mon['type'])}\n")
        f.flush()
    print(">>> Game Saved Successfully!")

def load_game():
    global x, y, player_mon
    try:
        with open("savefile.txt", "r") as f:
            lines = f.readlines()
            x = int(lines[0].strip())
            y = int(lines[1].strip())
            player_mon["name"] = lines[2].strip()
            player_mon['hp'] = int(lines[3].strip())
            player_mon["max_hp"] = int(lines[4].strip())
            player_mon['lvl'] = int(lines[5].strip())
            player_mon['attack'] = int(lines[6].strip())
            player_mon["defense"] = int(lines[7].strip())
            player_mon["speed"] = int(lines[8].strip())
            player_mon["type"] = lines[9].strip().split(",")
        print(">>> Game Loaded Successfully!")
    except FileNotFoundError:
        print(">>> No save file found! New Game Starting.")

def player_move():
    print(f"\n", "="*30)
    player_move_choice = input(f"\nMoves: \n1. {player_mon['Moves'][0]['name']}\n2. {player_mon['Moves'][1]['name']}\nWhat move will you use: ")
    print(f"\n", "="*30)
    if player_move_choice == "1":
        print(f"\nYou hit {active_monster['name']} for {player_mon['Moves'][0]['attack']}")
        active_monster['hp'] -= player_mon["Moves"][0]['attack']
    elif player_move_choice == "2":
        print(f"\nYou hit {active_monster['name']} for {player_mon['Moves'][1]['attack']}")
        active_monster['hp'] -= player_mon["Moves"][1]['attack']
    else:
        input("\nMake your choice before the enemy CloudMon does!")
        player_move()

print("--- Welcome to PEv1 ---")
choice = input("1. New Game\n2. Load Game\nChoice: ")

if choice == "2":
    load_game()
else:
    print("Starting New Game.")

while True:
        if game_state == "EXPLORING":
            for cloudmon in player_party:
                print(f"Party: {cloudmon['name']}")
            print("Current location: ", x, ",", y)
            move = input("Where do you want to go? N, E, S, W, or Q to Quit: ").upper().strip()
            if move == "N":
                print("Ok! Going North!")
                y += 1
            elif move == "E":
                print("Ok! Going East!")
                x += 1
            elif move == "S":
                print("Ok! going South!")
                y -= 1
            elif move == "W":
                print("Ok! Going West!")
                x -= 1
            elif move == "Q":
                save_game()
                print("Ok! Bye!")
                quit()

            if x >=3 and x <= 15:
                current_tile = "tall grass"
            else:
                current_tile = "grass"

            if current_tile == "tall grass":
                chance = random.randint(1, 10)
                if chance <= 3:
                    active_monster = random.choice(monster_list).copy()
                    input(f"\nA Wild {active_monster['name']} Has Appeared! (Press Enter to continue)")
                    game_state = "BATTLE"
        elif game_state == "BATTLE":
            print(f"\n" + "="*30)
            print(f"{active_monster['name']} (LVL {active_monster['lvl']})")
            print(f"HP: {active_monster['hp']}")
            print("-" * 10)
            print(f"Your CloudMon: {player_mon['name']} (LVL {player_mon['lvl']})")
            print(f"HP: {player_mon['hp']}")
            print("="*30)


            if len(player_party) > 1 and not what_mon_used:
                what_mon = input(f"What CloudMon will you use? 1: {player_party[0]['name']}, 2: {player_party[1]['name']}")
                if what_mon == "1":
                    player_mon.update(player_party[0])
                    what_mon_used = True
                elif what_mon == "2":
                    player_mon.update(player_party[1])
                    what_mon_used = True
            action = input("\nType: '1' for Attack, '2' for Capture, or '3' to Run: ").upper().strip()

            if player_mon["hp"] <= 0:
                input(f"\nYour {player_mon['name']} fainted! Press Enter to return to 0, 0 and heal your CloudMon!")
                x, y = 0, 0
                player_mon["hp"] = player_mon["max_hp"]
                game_state = "EXPLORING"

            if action == "1":
                player_move()


                if active_monster['hp'] <= 0:
                    input(f"\nWild {active_monster['name']} fainted. {player_mon['name']} gained 1 level!")
                    player_mon["lvl"] += 1
                    player_mon["max_hp"] += 5
                    player_mon["hp"] = player_mon["max_hp"]
                    game_state = "EXPLORING"
                    player_party.append(active_monster)

                if active_monster["hp"] > 0:
                    e_damage = active_monster["attack"]
                    player_mon["hp"] -= e_damage
                    print(f"Wild {active_monster['name']} dealt {e_damage} to your {player_mon['name']}!")

            elif action == "2":
                catch_chance = max(20, 1 - active_monster['hp'] / active_monster['max_hp'] * 100)
                roll = random.randint(1, 100)
                if roll <= catch_chance:
                    print(f"You Caught {active_monster['name']}! Congrats!")
                    player_party.append(active_monster)
                    game_state = "EXPLORING"
                elif roll <= catch_chance and len(player_party) >= 2:
                    input(f"\nYour Party is Full! You have to let the {active_monster['name']} go free. (Press Enter)")
                    game_state = "EXPLORING"

            elif action == "3":
                print("Ypu got away safely!")
                game_state = "EXPLORING"

            


