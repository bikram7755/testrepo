import pymongo
client=pymongo.MongoClient('mongodb+srv://root:root@cluster0.cr61eot.mongodb.net/?retryWrites=true&w=majority')
db=client.test
print(db)

d={
    'name':'hari',
    'sirname':'jha',
    'crn':'PUR078MSInE003'

}

db1=client['college']
coll=db1['student']
coll.insert_one(d)