def gettowns():
    import json
    # load data from JSON to list of dictionaries
    with open("TownEditor/lat_towns.json", encoding='utf-8') as f:
        data = json.load(f)
        towns = list(data)
    # for i in towns:
    #     for k, v in i.items():
    #         print (k, v) 
    #     print(type(i))
    f.close()
    return towns
