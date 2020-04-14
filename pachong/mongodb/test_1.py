import pymongo

client = pymongo.MongoClient(host="127.0.0.1",port=27017)
db = client.test
#print(db.test_2.find()[0])
db = client.admin
r = db.authenticate("wangyiqing8866","wyq123456789")
db = client.test
print(db.test_2.find()[0])

