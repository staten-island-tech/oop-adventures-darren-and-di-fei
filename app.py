import json
import random
rebirths = json.load(open("rebirth.json"))
monsters = json.load(open("monsters.json"))
from inventory import *
from rebirths import *

monster = "Lv.1 Gnome"
sword = "Starter Sword"
armor = "Starter Armor"
shield = "Starter Shield"

exp = 0
rebirth_points = 0

exp_mult = 1
rp_mult = 1
dmg_mult = 1
hp_mult = 1
def_mult = 1

zone = "Forest - 1"
win = None

def rebirth_calc():
    Rebirth()
    global exp,rebirth_points,inventory,sword,armor,shield
    rebirth_points = rebirth_points + (exp/1000 * rp_mult)
    exp = 0
    inventory = {}
    sword = "Starter Sword"
    armor = "Starter Armor"
    shield = "Starter Shield"
def exp_calc(monster):
    generate_item(monster)
    global exp
    global exp_mult
    for i in monsters:
        if monster == i["name"]:
            exp = exp + (i["exp"] * exp_mult)
def equip_item():
    global inventory, sword, armor, shield

    equip_status = True
    while equip_status == True:
        equip_query = input(f"What item do you want to equip?\nYou currently have {sword}, {armor}, and {shield} equipped.\n{inventory}.\nType \"back\" to stop equpping an item. ")
        if equip_query in inventory:
            inventory[equip_query] = inventory[equip_query] - 1
            if inventory[equip_query] <= 0:
                del inventory[equip_query]
            for i in swords:
                if equip_query  == i["name"]:
                    x = "sword"
            for i in shields:
                if equip_query == i["name"]:
                    x = "shield"
            for i in armors:
                if equip_query == i["name"]:
                    x = "armor"
            if x == "sword":
                if sword in inventory:
                    inventory[sword] = inventory[sword] + 1
                else:
                    inventory[sword] = 1
                sword = equip_query
                equip_status = False
            elif x == "shield":
                if shield in inventory:
                    inventory[shield] = inventory[shield] + 1
                else:
                    inventory[shield] = 1
                shield = equip_query
                equip_status = False
            else:
                if armor in inventory:
                    inventory[armor] = inventory[armor] + 1
                else:
                    inventory[armor] = 1
                armor = equip_query
                equip_status = False
        elif equip_query.lower() == "back":
            equip_status = False
        else:
            print("That is not a valid item in your inventory. Try again.")
def view_inventory():
    global inventory
    view_status = True
    while view_status == True:
        inventory_query = input(f"{inventory}\nINSPECT, DELETE, or EQUIP an item?\nType \"back\" to stop viewing your inventory. ").lower()
        if inventory_query == "inspect":
            inspect_item()
            view_status = False
        elif inventory_query == "delete":
            delete_item()
        elif inventory_query == "equip":
            view_status = False
            equip_item()
            view_status = False
        elif inventory_query == "back":
            view_status = False
        else:
            print("That is not a valid action. Try again.")
def Purchase():
    global dmg_mult,def_mult,hp_mult,rebirth_points
    purchase_status = True
    while purchase_status == True:
        test = []
        for i in rebirth_shop:
            print(i["name"], i["price"])
            test.append(i["name"])
        purchase_query = input(f"Which upgrade do you want to purchase?\nType \"back\" to stop purchasing. ")
        if purchase_query == "back":
            purchase_status = False
        elif purchase_query not in test:
            print("This is not a valid upgrade/action. Try again.")
        else:
            x = True
            z = 0
            while x == True:
                if purchase_query == rebirth_shop[z]["name"]:
                    if rebirth_shop[z]["price"] > rebirth_points:
                        print("You do not have enough rebirth points to purchase this upgrade.")
                        purchase_status = False
                        break
                    else:
                        rebirth_points = rebirth_points - rebirth_shop[z]["price"]
                        if rebirth_shop[z]["type"] == "Damage":
                            dmg_mult = dmg_mult * rebirth_shop[z]["multiplier"]
                        elif rebirth_shop[z]["type"] == "Armor":
                            dmg_mult = dmg_mult * rebirth_shop[z]["multiplier"]
                        elif rebirth_shop[z]["type"] == "Defense":
                            def_mult = def_mult * rebirth_shop[z]["multiplier"]
                        del rebirth_shop[z]
                        break
                else:
                    z = z + 1
def view_shop():
    view_status = True
    while view_status == True:
        view_query = input(f"PURCHASE upgrade?\n{rebirth_shop}\nType \"back\" to stop viewing the shop. ").lower()
        if view_query == "purchase":
            Purchase()
            view_status = False
        elif view_query == "back":
            view_status = False
        else:
            print("That is not a valid action. Try again.")
def teleport_zone():

    global zone
    biome_status = True
    while biome_status == True:
        biome_teleport = input("What biome do you want to teleport to?\nFOREST, OCEAN, UNDERWORLD, HEAVEN, or YOUR BASEMENT?\nType \"back\" to stop teleporting to a biome. ").lower() 
        if biome_teleport == "forest":
            biome = "Forest"
            biome_status = False
        elif biome_teleport == "ocean":
            biome = "Ocean"
            biome_status = False
        elif biome_teleport == "underworld":
            biome = "Underworld"
            biome_status = False
        elif biome_teleport == "heaven":
            biome = "Heaven"
            biome_status = False
        elif biome_teleport == "your basement":
            biome = "Your Basement"
            biome_status = False
        elif biome_teleport == "back":
            biome_status = False
        else:
            print("That is not a valid biome/action. Try again.")
    zone_status = True
    while zone_status == True:
        if biome == "Your Basement":
            zone_query = input("Which zone do you want to teleport to?\n1: Your Basement - 1\n2: Your Basement - 2\n3: Your Basement - 3\n4: Your Basement - 4\n5: Your Basement - 5\nType the number before the colon to select a zone.\nType \"back\" to stop selecting a zone. ").lower()
            if zone_query == "1":
                zone = "Your Basement - 1"
                zone_status = False
            elif zone_query == "2":
                zone = "Your Basement - 2"
                zone_status = False
            elif zone_query == "3":
                zone = "Your Basement - 3"
                zone_status = False
            elif zone_query == "4":
                zone = "Your Basement - 4"
                zone_status = False
            elif zone_query == "5":
                zone = "Your Basement - 5"
                zone_status = False
            elif zone_query == "back":
                zone_status = False
            else:
                print("That is not a valid zone/action. Try again.")
        elif biome == "Forest" or biome == "Ocean" or biome == "Underworld" or biome == "Heaven":
            zone_query = input(f"Which zone do you want to teleport to?\n1: {biome} - 1\n2: {biome} - 2\n3: {biome} - 3\n4: {biome} - 4\n5: {biome} - 5\n6: {biome} - 6\n7: {biome} - 7\n8: {biome} - 8\n9: {biome} - 9\n10: {biome} - 10\nType the number before the colon to select a zone.\nType \"back\" to stop selecting a zone. ").lower()
            if zone_query == "1":
                zone = f"{biome} - 1"
                zone_status = False
            elif zone_query == "2":
                zone = f"{biome} - 2"
                zone_status = False
            elif zone_query == "3":
                zone = f"{biome} - 3"
                zone_status = False
            elif zone_query == "4":
                zone = f"{biome} - 4"
                zone_status = False
            elif zone_query == "5":
                zone = f"{biome} - 5"
                zone_status = False
            elif zone_query == "6":
                zone = f"{biome} - 6"
                zone_status = False
            elif zone_query == "7":
                zone = f"{biome} - 7"
                zone_status = False
            elif zone_query == "8":
                zone = f"{biome} - 8"
                zone_status = False
            elif zone_query == "9":
                zone = f"{biome} - 9"
                zone_status = False
            elif zone_query == "10":
                zone = f"{biome} - 10"
                zone_status = False
            elif zone_query == "back":
                zone_status = False
            else:
                print("That is not a valid zone/action. Try again.")
def Combat(sword,armor,shield,monster):
    
    global dmg_mult, hp_mult, def_mult, monster_hp,win

    for i in monsters:
        if i ["name"] == monster:
            monster_hp = i["hp"]
            monster_damage = i["damage"]
    for i in swords:
        if i["name"] == sword:
            your_damage = i["damage"]
            attack_turn = i["turns"]
    for i in armors:
        if i ["name"] == armor:
            your_hp = (i["hp"]  * hp_mult) + 100
    for i in shields:
        if i["name"] == shield:
            your_defense = i["defense"]
    
    while monster_hp > 0 and your_hp > 0:
        turns = 2
        block_count = 0
        while turns > 0 and monster_hp > 0:
            if turns == 2 or (turns == 1 and attack_turn == 1):
                move_decide = input(f"\tYou have {turns} turn(s) left. Do you want to ATTACK or BLOCK? ").lower()
                if move_decide == "attack":
                    monster_hp = monster_hp - (your_damage * dmg_mult)
                    if monster_hp <= 0:
                        print(f"You killed {monster}!")
                        win = True
                        monster_hp = 0
                    else:
                        print(f"You hit {monster} for {your_damage * dmg_mult} damage. {monster} has {monster_hp} HP left.")
                        turns = turns - attack_turn
                elif move_decide == "block":
                    block_count = block_count + 1
                    print(f"You block with {shield}. You have blocked {block_count} time(s).")
                    turns = turns - 1
                else:
                    print("That is not a valid action. Try again.")
            elif turns == 1 and attack_turn == 2:
                block_count = block_count + 1
                print(f"You automatically block with {shield}. You have blocked {block_count} time(s).")
                turns = turns - 1
        if monster_hp > 0:
            incoming_damage = monster_damage - (your_defense * block_count * def_mult)
            if incoming_damage <= 0:
                incoming_damage = 0
            your_hp = your_hp - incoming_damage
            if your_hp <= 0:
                print(f"You died to {monster}.")
                win = False
            else:
                print(f"{monster} hits you for {incoming_damage} HP. You have {your_hp} HP left.")
def generate_item(monster):
    global item
    item_rng = random.uniform(1,100)
    for i in monsters:
        if monster == i["name"]:
            monster_stats = i
    for i in monster_stats["drops"].values():
        item_rng = item_rng - i
        if item_rng <= 0:
            x = i
            break
    for i in monster_stats["drops"]:
        if monster_stats["drops"].get(i) == x:
            item = i
    if item != "Nothing":
        print(f"You obtained {item}!")
    elif item == "Nothing":
        item = None

hub_status = True
while hub_status == True:
    hub_query = input("TELEPORT, VIEW STATS, VIEW INVENTORY, REBIRTH, VIEW REBIRTH SHOP, VIEW EQUIPMENT, or FIGHT?\nType \"exit\" to exit the game without killing the terminal. YOUR DATA DOES NOT CURRENTLY SAVE WHEN YOU EXIT THE GAME. ").lower()
    if hub_query == "teleport":
        teleport_zone()
        for i in monsters:
            if zone == i["zone"]:
                monster = i["name"]
        hub_query = "fight"
    if hub_query == "fight":
        fight_status = True
        while fight_status == True:
            fight_query = input(f"You are currently in zone {zone}.\nDo you want to fight {monster}?\n(Yes) (No) ").lower()
            if fight_query == "y" or fight_query == "yes":
                Combat(sword,armor,shield,monster)
                if win == True:
                    exp_calc(monster)
                    if item != None:
                        add_item(item)
            elif fight_query == "n" or fight_query == "no":
                fight_status = False
            else:
                print("That is not a valid action. Try again.")
    elif hub_query == "view stats":
        print(f"EXP: {exp}, Rebirth Points: {rebirth_points}, DMG Multiplier: {dmg_mult}, HP Multiplier: {hp_mult}, DEF Multiplier: {def_mult}")
    elif hub_query == "view inventory":
        view_inventory()
    elif hub_query == "view equipment":
        print(f"Sword: {sword}, Armor: {armor}, Shield: {shield}")
    elif hub_query.lower() == "exit":
        hub_status = False
    elif hub_query == "view rebirth shop":
        view_shop()
    elif hub_query == "rebirth":
        rebirth_calc()
    else:
        print("That is not a valid action. Try again.")