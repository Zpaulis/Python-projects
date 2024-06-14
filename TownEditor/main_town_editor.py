cmd = "q"
from __load_JSON_to_list import gettowns
from __save_list_to_JSON import savetowns
from save_towns_to_json import revert
# download data base from Cloud Firestore data base (func. get_towns() in file __read_firestore_db_v2.py)
# then save data as JSON in file "TownEditor/lat_towns.json" (func. revert() in file save_towns_to_json.py)
f_path = revert()
# function gettowns() in file _load_JSON_to_list.py read JSON file and return list of dict.
towns = gettowns(f_path)
# TODO Create nice user interface instead of "Northon-like"
while True:
    cmd = str(input("A = pilsētu saraksts, Q = quit, R = revert, S = save, P = display, E = edit. Ievadiet komandu: ")).lower()
    print(cmd)
    if cmd == "q":
        break
    elif cmd == "a": # Display all town names
         for i in range(len(towns)):
            print (towns[i]["name"])
    elif cmd == "r": # download data base from Cloud and revert JSON file
        f_path = revert()
        towns = gettowns(f_path)
        print ("Izmaiņas atceltas, dati atjaunoti no Firestore")
    elif cmd == "s":
        #TODO Save Town list to Cloud Firestore - have to backup cloud data base before
        print("Līdz mākonim tālu!")
        continue
    elif cmd == "p": # Display one town dictionary
        key = input ("Kuru pilsētu rādīt? ")
        for town in towns:
            if town["name"] == key:
                # print ("vēlāk!")
                for k, v in town.items():
                    print (k, v) 
    elif cmd == "e": # Edit Towns dictionaries list
        edt = "q"
        while True:
            edt = str(input ("I = insert, D = delete, U = update, S = save JSON, C = cancel. Ievadiet komandu: ")).lower()
            if edt == "c" or edt == "q": # return to main menu
                break 
            elif edt == "i": # Insert new Town dictionary
                one_more_town = {}
                one_more_town["name"] = input("Ievadiet pilsētas nosaukumu: ")
                one_more_town["area"] = int(input ("Ievadiet pilsētas platību "))
                one_more_town["population"] = int(input ("Ievadiet iedzīvotāju skaitu "))
                # TODO And so on
                towns.append(one_more_town)
                print(f"{one_more_town} pievienota pilsētu sarakstam")
            elif edt == "d": # Delete one dictionary from list
                bad_town = input("Kuru pilsētu izdzēst no saraksta? ")
                for town in towns:
                    if town["name"] == bad_town: # Delete bad_town dict. from towns list
                        for i in range(len(towns)):
                            if towns[i]["name"] == bad_town:
                                print (towns[i])
                                del towns[i]
                                print (f"{bad_town}? Nav vairs tādas pilsētas sarakstā!")
                                break
            elif edt == "u": # Edit existing data in dict.
                bad_town = input("Kuru pilsētu labosim? ")
                for i in range(len(towns)):
                    if towns[i]["name"] == bad_town:
                        print (towns[i].keys())
                        bad_key = input("Kuru parametru labosim? ")
                        print (towns[i][bad_key])
                        good_value = input("Ievadiet pareizo vērtību: ")
                        for key, value in towns[i].items():
                            towns[i][bad_key] = good_value
                        print (f"LABOTS: {towns[i]}")
            elif edt == "s":
                # Save towns to lat_towns.json
                savetowns(towns, f_path)
                print("Pieglabāts!")
print("Visu labu!")
