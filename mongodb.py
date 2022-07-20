import pymongo
client = pymongo.MongoClient("mongodb+srv://Manasa_SM:Bhargav$93@manasa.atdo0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "manasa",
    "email": "manasa@ineuron.ai",
    "surname": "pallakki"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )