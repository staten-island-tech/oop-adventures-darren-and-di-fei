"""import json
import random
data = open("test.json", encoding="utf8")
chest = json.load(data)
data2 = open("test2.json", encoding="utf8")
loot = json.load(data2)
from subtraction import chance_1,chance_2,chance_3,chance_4,chance_5,chance_6
global rarity
rarity = ""
def find_Poor():
    x = random.uniform(0,100)
    print(x)
    if chance_1 <= 0:
        rarity = "Poor"
        item = random.choice(chest[0]["#Poor_Items"])
        print(item)
        print(rarity)
    elif chance_1 > 0:
        find_Common()

def find_Common():
    if chance_2 <= 0:
        rarity = "Common"
        item = random.choice(chest[0]["#Common_Items"])
        print(item)
        print(rarity)
    elif chance_2 > 0:
        find_Uncommon()

def find_Uncommon():
    if chance_3 <= 0:
        rarity = "Uncommon"
        item = random.choice(chest[0]["#Uncommon_Items"])
        print(item)
        print(rarity)
    elif chance_3 > 0:
        find_Rare()

def find_Rare():
    if chance_4 <= 0:
        rarity = "Rare"
        item = random.choice(chest[0]["#Rare_Items"])
        print(item)
        print(rarity)
    elif chance_4 > 0:
        find_Epic()

def find_Epic():
    if chance_5 <= 0:
        rarity = "Epic"
        item = random.choice(chest[0]["#Epic_Items"])
        print(item)
        print(rarity)
    elif chance_5 > 0:
        find_Legendary()

def find_Legendary():
    if chance_6 <= 0:
        rarity = "Legendary"
        item = random.choice(chest[0]["#Legendary_Items"])
        print(item)
        print(rarity)
find_Poor()

"""
import json
import random
chest = json.load(open("test.json"))
items = json.load(open("test2.json"))

container_list = []
rarity_list = []
spawns_list = []
id_list = []
item_list = []
index_num = 0

id = input("Input ID (testing) ")

for i in chest:
    if i["id"] == id:
        container_id = i
        break
    index_num = index_num + 1

for i in container_id:
    container_list.append(i)

rolls = range(chest[index_num]["rolls"])
for i in rolls:
    rng = random.uniform(0,100)
    for i in container_list:
        rarities = i
        rng = rng - chest[index_num][i]
        if rng <= 0:
            rarity_list.append(rarities)
            break

for i in rarity_list:
    spawns_list.append(f"{i}_Items")

for i in spawns_list:
    id_list.append(random.choice(chest[index_num][i]))

class Item:
    def __init__(self,id,name,rarity,slots):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.slots = slots
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Rarity: {self.rarity}, Slots: {self.slots}"

while len(id_list) > 0:
    for i in items:
        if i["id"] in id_list:
            id = i["id"]
            name = i["name"]
            rarity = i["rarity"]
            slots = i["slots"]
            item_list.append(Item(id,name,rarity,slots))
            id_list.pop(0)

for i in item_list:
    print(i)