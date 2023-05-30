interaction_object = ""
import json 
import random
x = open("Crypt_02_HR.json")
map = json.load(x)
"""from room_select import current_room"""
room_status = " "
y = random.randint(0,len(map[0]["spawns"])-1)
current_room = map[0]["spawns"][y]
print(f"You are currently in room {current_room}")


room_find_num = 1
room_find = map[room_find_num]["room"]
while room_find != current_room:
    room_find_num = room_find_num + 1
    room_find = map[room_find_num]["room"]
mobs = map[room_find_num]["monster"]
print(mobs)
mob =  input(print("which mob do you want to fight right now?"))

def fight():
    if mob in mobs:
        print("hi")
    else: 
        print("Invalid mob. Try again")

fight()
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
y = random.randint(0,len(map[0]["spawns"])-1)
current_room = map[0]["spawns"][y]
print(f"You are currently in room {current_room}")

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
        print("Invalid room. Try again")"""