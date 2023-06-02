
import json 
import random
x = open("Crypt_02_HR.json")
map = json.load(x)
y = open("test2.json")
difficulty_monster = json.load(y)
"""from room_select import current_room"""
z = random.randint(0,len(map[0]["spawns"])-1)
current_room = map[0]["spawns"][z]
print(f"You are currently in room {current_room}")



"""Common = difficulty_monster["id"].index("(Common)")
HR = difficulty_monster["id"].index("(HR)")
HR2 = difficulty_monster["id"].index("(HR2)")"""
for i in difficulty_monster:
    if "(Common)" in i["id"]:
        print("hi")