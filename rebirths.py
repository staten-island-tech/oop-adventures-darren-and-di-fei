import json
rebirths = json.load(open("rebirth.json"))
rebirth_shop = rebirths

def Rebirth():
    rebirth_status = True
    while rebirth_status == True:
        rebirth_query = input(f"Do you want to rebirth? (Yes) (No)\nYou will lose all items.\nYou will gain 1 rebirth point for every 1000 EXP points you have. ").lower()
        if rebirth_query == "yes" or rebirth_query == "y":
            rebirth_status = False
        elif rebirth_query == "no" or rebirth_query == "n":
            rebirth_status = False
        else:
            print("That is not a valid action. Try again.")