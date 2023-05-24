import json
import random
import subtraction
data = open("test.json", encoding="utf8")
chest = json.load(data)
data2 = open("test2.json", encoding="utf8")
loot = json.load(data2)


key_list = []
def find_Item():
    bob = ""
    x = random.uniform(0,100)
    print(x)
    if x - chest[0]["#Poor"] <= 0:
        bob = "Poor"
        item = random.choice(chest[0]["#Poor_Items"])
        print(item)
        print(bob)
    elif x - chest[0]["#Common"] > 0:
        bob = "Common"
        item = random.choice(chest[0]["#Common_Item"])
        print(item)
        print(bob)

    


find_Item()

