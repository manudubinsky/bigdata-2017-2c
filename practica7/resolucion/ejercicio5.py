from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.tweets.find({"user.name": "Annie Sullivan"})

var = 1

for document in cursor:
  print (var)
  print ("*******************")
  print (document)
  var +=1

