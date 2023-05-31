
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


room_find_num = 1
room_find = map[room_find_num]["room"]
while room_find != current_room:
    room_find_num = room_find_num + 1
    room_find = map[room_find_num]["room"]
mobs = map[room_find_num]["monster"]
print(mobs)
current_mob = input(("which mob do you want to fight right now?(please include HR/Common/HR2): "))


def determine_mob():
    if "(HR)" in current_mob:
        current_mob1 = current_mob.replace("(HR)", '')
        HR_monsters = difficulty_monster[1]
    for values in HR_monsters.items():
        values1 = str(values)
        if "Monster_Name" in values1:
            values = values1.replace("Monster_Name",current_mob1)
            print(values)


p = True
while p == True:
    if current_mob in mobs:
        determine_mob()
        p = False
        
    else:
        print("try again, not an option")

class Mob:
    def __init__(self,id,name,difficulty):
        self.id = id
        self.name = name
        self.difficulty = difficulty
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Rarity: {self.difficulty}"









"""room_status = " "
if room_status == "cleared":
    room_find_num = 1
    room_find = map[room_find_num]["room"]
    while room_find != current_room:
        room_find_num = room_find_num + 1
        room_find = map[room_find_num]["room"]
    mobs = map[room_find_num]["monster"]

if room_status == "completed":
    room_find_num = 1
    room_find = map[room_find_num]["room"]
    while room_find != current_room:
        room_find_num = room_find_num + 1
        room_find = map[room_find_num]["room"]
    connection = map[room_find_num]["connection"]
    room_select = True
    while room_select == True:
        test = input(f"What room do you want to go to next? {connection} ")
        if test in connection:
            current_room = test
            room_select = False
        else:
            print("Invalid room. Try again")
"""
