
import json 
import random

x = open("Crypt_02_HR.json")
y = open("test2.json")
map = json.load(x)
difficulty_monster = json.load(y)

z = random.randint(0,len(map[0]["spawns"])-1)
current_room = map[0]["spawns"][z]
print(f"You are currently in room {current_room}")
index_num = 0


room_find_num = 1
room_find = map[room_find_num]["room"]
while room_find != current_room:
    room_find_num = room_find_num + 1
    room_find = map[room_find_num]["room"]
mobs = map[room_find_num]["monster"]
print(mobs)


monster_list = []
index_num = 0
difficulty_list = []
spawns_list = []
id_list = []
mobs_amount = []
current_mob_status = ""
def determine_mob():
    for i in difficulty_monster:
        if "(Common)" in current_mob:
            index_num = 0
        elif "(HR)" in current_mob:
            index_num = 1
        elif "(HR2)" in current_mob:
            index_num = 2 
        break


    for i in difficulty_monster:
        if index_num == 0:
            for i in difficulty_monster[0]:
                monster_list.append(i)
        elif index_num == 1:
            for i in difficulty_monster[1]:
                monster_list.append(i)
        elif index_num == 2:
            for i in difficulty_monster[2]:
                monster_list.append(i)
        break


    rolls = range(difficulty_monster[index_num]["rolls"])
    for i in rolls:
        rng = random.randint(0,100)
        for i in monster_list:
            difficulty = i
            rng = rng - difficulty_monster[index_num][i]
            if rng <= 0:
                difficulty_list.append(difficulty)
                break


    if "(HR)" in current_mob:
        current_mob1 = current_mob.replace("(HR)", '')
    elif "(HR)" in current_mob:
        current_mob1 = current_mob.replace("(Common)", '')
    elif "(HR2)" in current_mob:
        current_mob1 = current_mob.replace("(HR2)", '')
    print(f"{current_mob1}{i}")
    mob_quantity_list = list(mobs.values())
    mobs1 = list(mobs)
    index_mob = mobs1.index(current_mob)
    mob_leftover = mob_quantity_list[index_mob] - 1
    d = {current_mob : mob_leftover}
    mobs.update(d)
    print(mobs)
    mob_leftover1 = range(mob_leftover)
    for i in mob_leftover1:
        if i == "0":
            mobs.remove(mobs[i])
            mobs.update


p = True
while p == True:
    current_mob = input(("which mob do you want to fight right now?(please include HR/Common/HR2): "))
    if current_mob in mobs:
        determine_mob()
        p = False
    else:
        print("try again, not an option")






fight = "successful"
if fight == "successful":
    p = True
    while p == True:
        current_mob = input(("which mob do you want to fight right now?(please include HR/Common/HR2): "))
        if current_mob in mobs:
            determine_mob()
            p = False
        else:
            print("try again, not an option")