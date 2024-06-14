def get_towns():
    try:
        import firebase_admin
        # initialise firestore database
        from firebase_admin import credentials
        from firebase_admin import firestore
        cred = credentials.Certificate("/Users/paulismacbook/Python projects/TownEditor/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    except:
        print("pietiks inicializēt!")
    # create database instance
    db = firestore.client()
    # get data from firestore
    # get all towns data to list of dictonaries
    result = db.collection("towns").get()
    all_towns = ([])
    # TODO Insert controle for success
    for one_doc in result:
        all_towns.append(one_doc.to_dict())
    # print(all_towns)
    print(f"Datu bāzes garums - {len(all_towns)}")
    return all_towns
