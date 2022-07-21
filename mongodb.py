import pymongo
client = pymongo.MongoClient("mongodb+srv://mangeshyadavv:mangeshyadavv@cluster0.dogay.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"mangesh",
    "email" : "mangeshyadavv@gmail.com",
    "surname" : "yadav"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )