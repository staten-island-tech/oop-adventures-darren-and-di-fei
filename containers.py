import json
import random
data = open("test.json", encoding="utf8")
chest = json.load(data)
data2 = open("test2.json", encoding="utf8")
loot = json.load(data2)


key_list = []
x = random.uniform(0,100)
for i in chest:
    for i in i["items"]:
        for k in i:
            key_list.append(k)
print(key_list)