import json 
import random
data = open("Crypt_02_HR.json", encoding="utf8")
Map = json.load(data)


x = random.randint(0,len(Map[0]["spawns"]))
current_room = (Map[0]["spawns"][x])
print("current room " + current_room)
""" for i in Map:
    if current_room == Map[i]["room"]:
        connections_list = Map[i]["connection"] 
movement_query = input("which room would you like to go next?")
if movement_query in connections_list:
    print("yes") """