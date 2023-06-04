
import json
import random
chest = json.load(open("test1.json"))
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
    