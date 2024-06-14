def savetowns(town_list, f_path):
    import json
    # save list of dictionaries to JSON file
    with open(f_path, 'w', encoding='utf-8') as f:
        json.dump(town_list, f)
    f.close()