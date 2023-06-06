import json
swords = json.load(open("swords.json"))
shields = json.load(open("shields.json"))
armors = json.load(open("armor.json"))

inventory = {}

def add_item(item):
    global inventory
    if item in inventory:
        inventory[item] = inventory[item] + 1
    else:
        inventory[item] = 1

class Inspect():
    def __init__(self,name):
        self.name = name
class Inspect_Sword(Inspect):
    def __init__(self,name,damage,turns):
        super().__init__(name)
        self.damage = damage
        self.turns = turns
    def __str__(self):
        return f"Name: {self.name}, Damage: {self.damage}, Turns: {self.turns}"
class Inspect_Armor(Inspect):
    def __init__(self,name,hp):
        super().__init__(name)
        self.hp = hp
    def __str__(self):
        return f"Name: {self.name}, HP: {self.hp}"
class Inspect_Shield(Inspect):
    def __init__(self,name,defense):
        super().__init__(name)
        self.defense = defense
    def __str__(self):
        return f"Name: {self.name}, Defense: {self.defense}"
    
def inspect_item():
    global inventory
    inspect_status = True
    while inspect_status == True:
        inspect_query = input(f"Which item do you want to inspect?\n{inventory}\nType \"back\" to stop inspecting an item. ")
        if inspect_query in inventory:
            for i in swords:
                if inspect_query == i["name"]:
                    name = i["name"]
                    damage = i["damage"]
                    turns = i["turns"]
                    print(Inspect_Sword(name,damage,turns))
            for i in armors:
                if inspect_query == i["name"]:
                    name = i["name"]
                    hp = i["hp"]
                    print(Inspect_Armor(name,hp))
            for i in shields:
                if inspect_query == i["name"]:
                    name = i["name"]
                    defense = i["defense"]
                    print(Inspect_Shield(name,defense))
            inspect_status = False
        elif inspect_query.lower() == "back":
            inspect_status = False
        else:
            print("That is not a valid action. Try again.")

def delete_item():
    global inventory
    delete_status = True
    while delete_status == True:
        delete_query = input(f"Which item do you want to delete?\n{inventory}\n Type \"back\" to stop deleting an item. ")
        if delete_query in inventory:
            delete_quantity = input(f"How many {delete_query} do you want to delete?\nYou have {inventory[delete_query]} {delete_query}.\nType \"all\" to delete all items, and type \"back\" to stop deleting items. ")
            if int(delete_quantity) >= inventory[delete_query]:
                del inventory[delete_query]
            elif delete_quantity < inventory[delete_query]:
                inventory[delete_query] = inventory[delete_query] - delete_quantity
            elif delete_quantity == "all":
                del inventory[delete_query]
            elif delete_quantity == "back":
                delete_status = False
            else:
                print("That is not a valid action. Try again.")
            delete_status = False
        elif delete_query.lower() == "back":
            delete_status = False
        else:
            print("That is not a valid action. Try again.")