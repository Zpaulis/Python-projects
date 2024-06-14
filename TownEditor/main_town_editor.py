cmd = "q"
from __load_JSON_to_list import gettowns
from save_towns_to_json import revert
revert()
towns = gettowns()
while True:
    cmd = str(input("Q = quit, R = revert, S = save, P = display, E = edit. Ievadiet komandu:")).lower()
    print(cmd)
    if cmd == "q":
        break
    elif cmd == "r":
        revert()
        towns = gettowns()
        print ("Izmaiņas atceltas, dati atjaunoti no Firestore")
    elif cmd == "s":
        #TODO Save Town list to Cloud Firestore
        continue
    elif cmd == "p":
        key = input ("Kuru pilsētu rādīt? ")
        for town in towns:
            if town["name"] == key:
                # print ("vēlāk!")
                for k, v in town.items():
                    print (k, v) 
    elif cmd == "e":
        edt = "q"
        while True:
            edt = input ("I = insert, D = delete, U = update, S = save JSON, C = cancel. Ievadiet komandu:")
            if edt == "c" or edt == "q":
                break
            elif edt == "i":
                one_more_town = {}
                one_more_town["name"] = input("Ievadiet pilsētas nosaukumu: ")
                one_more_town["area"] = int(input ("Ievadiet pilsētas platību "))
                # TODO And so on
                towns.append(one_more_town)
                print(f"{one_more_town} pievienota pilsētu sarakstam")
            elif edt == "d":
                bad_town = input("Kuru pilsētu izdzēst no saraksta? ")
                for town in towns:
                    if town["name"] == bad_town:
                        # TODO Delete town dict. from towns list
                        print (f"{bad_town}? Nav vairs tādas pilsētas sarakstā!")
            elif edt == "u":
                bad_town = input("Kuru pilsētu labosim? ")
                # TODO Edit existing data in dict.
            elif edt == "s":
                # TODO save towns to lat_towns.json
                print("Vēlāk!")
print("Visu labu!")
