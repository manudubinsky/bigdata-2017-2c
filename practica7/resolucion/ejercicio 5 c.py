from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.tweets.aggregate([{"$group":{"_id": "$lang", "total":{"$sum": 1}}}])

var = 1

for document in cursor:
  ##print (var)
  ##print ("*******************")
  print (document)
  var +=1

