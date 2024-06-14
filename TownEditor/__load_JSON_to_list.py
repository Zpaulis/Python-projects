def gettowns(f_path):
    import json
    # load data from JSON to list of dictionaries
    with open(f_path, encoding='utf-8') as f:
        data = json.load(f)
        towns = list(data)
    f.close()
    return towns
