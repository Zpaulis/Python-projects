import json
from read_firestore_db_v2 import get_towns
# get all firestore documents and save as JSON in workspace
all_towns = get_towns()
print(all_towns)
with open('TownEditor/lat_towns.json', 'w',encoding="utf-8") as f:
        json.dump(all_towns, f) # Save all recipes to JSON file