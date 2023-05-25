import json
import random
data = open("test.json", encoding="utf8")
chest = json.load(data)
data2 = open("test2.json", encoding="utf8")
loot = json.load(data2)
x = random.uniform(0,100)
chance_1 = x - chest[0]["#Poor"]
chance_2 = chance_1 - chest[0]["#Common"]
chance_3 = chance_2 - chest[0]["#Uncommon"]
chance_4 = chance_3 - chest[0]["#Rare"]
chance_5 = chance_4 - chest[0]["#Epic"]
chance_6 = chance_5 - chest[0]["#Legendary"]

