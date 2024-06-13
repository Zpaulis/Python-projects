import firebase_admin
# initialise firestore database
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/paulismacbook/Python projects/TownEditor/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
# create database instance
db=firestore.client()
# get data from firestore

# try to get one document
# result = db.collection('towns').document('ainazi').get()
# print(result.to_dict())
# get all towns now
result = db.collection('towns').get()
for one_doc in result:
    print(one_doc.to_dict())
