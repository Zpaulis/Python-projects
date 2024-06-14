def revert():
        import json
        from __read_firestore_db_v2 import get_towns
        f_path = "TownEditor/lat_towns.json"
        # get all firestore documents and save as JSON in workspace
        all_towns = get_towns()
        print(f"Ieraksti saglabāti failā {f_path}.")
        with open(f_path, 'w',encoding="utf-8") as f:
                json.dump(all_towns, f) # Save all recipes to JSON file
        return (f_path)