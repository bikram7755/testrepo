import pymongo
client=pymongo.MongoClient('mongodb+srv://root:root@cluster0.cr61eot.mongodb.net/?retryWrites=true&w=majority')
# client=pymongo.MongoClient('mongodb+srv://root:root@cluster0.cr61eot.mongodb.net/')

db=client.test
print(db)

d={
    'fname':'bikram',
    'lname':'shah',
    'faculty':'computer'
}


datas=[
    {
        'name':'hari',
        'class':10,
        'subject':['C','C++','Java']
    },
    {
        'name':'manoj',
        'class':9,
        'subject':['ECT','C++','Java']
    },
    {
        'name':'monu',
        'class':9,
        'subject':['ECT','EDC','Java']
    }


]
# print(d)
#
# mydb=client['mydatabasename']
# std=mydb['student']
# std.insert_one(d)
# print("data inserted")
# print(datas)
database=client['mydatabase']
collection=database['student']
# collection.insert_one(d)
# collection.insert_many(datas)
records=collection.find()
for i in records:
    for j in i.items():
        print(j[1])
